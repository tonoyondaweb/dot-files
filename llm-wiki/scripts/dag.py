#!/usr/bin/env python3
"""
dag.py - Deterministic DAG Task Evaluator and State Engine
Maintains synchronization between compiled dag.json and Obsidian task markdown subdocuments.
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path

def parse_frontmatter(content):
    """Simple parser for YAML frontmatter without external dependencies."""
    if not content.startswith("---"):
        return {}, content
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    
    yaml_text = parts[1]
    body = parts[2]
    
    data = {}
    current_key = None
    in_list = False
    
    for line in yaml_text.splitlines():
        trimmed = line.strip()
        if not trimmed or trimmed.startswith("#"):
            continue
        
        # Check list item
        if in_list and line.startswith("  - "):
            val = trimmed[2:].strip().strip("\"'")
            # strip Obsidian wikilink syntax [[...]]
            val = re.sub(r"^\[\[(?:.*[/\\])?([^|\]]+)(?:\|.*)?\]\]$", r"\1", val)
            data[current_key].append(val)
            continue
            
        # Check key-value
        if ":" in line and not line.startswith(" "):
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            current_key = key
            
            if not val or val == "[]":
                data[key] = []
                in_list = True
            elif val.startswith("[") and val.endswith("]"):
                # Inline list [a, b]
                raw_items = val[1:-1].split(",")
                items = []
                for it in raw_items:
                    it_clean = it.strip().strip("\"'")
                    it_clean = re.sub(r"^\[\[(?:.*[/\\])?([^|\]]+)(?:\|.*)?\]\]$", r"\1", it_clean)
                    if it_clean:
                        items.append(it_clean)
                data[key] = items
                in_list = False
            else:
                in_list = False
                val = val.strip("\"'")
                if val == "null":
                    data[key] = None
                elif val == "true":
                    data[key] = True
                elif val == "false":
                    data[key] = False
                else:
                    data[key] = val
        elif line.startswith("  "):
            # Continuation or unexpected indent
            pass
            
    return data, body

def update_frontmatter_in_file(file_path, updates):
    """Updates key-value pairs in YAML frontmatter preserving file structure."""
    if not os.path.exists(file_path):
        return
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        return

    parts = content.split("---", 2)
    if len(parts) < 3:
        return

    yaml_text = parts[1]
    body = parts[2]
    lines = yaml_text.splitlines()

    for key, val in updates.items():
        found = False
        formatted_val = f'"{val}"' if isinstance(val, str) else (json.dumps(val) if val is not None else "null")
        new_line = f"{key}: {formatted_val}"
        
        for idx, line in enumerate(lines):
            if re.match(rf"^{re.escape(key)}:\s*", line):
                lines[idx] = new_line
                found = True
                break
        if not found:
            lines.append(new_line)

    new_content = "---\n" + "\n".join(lines) + "\n---" + body
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

def resolve_epic_dir(explicit_path=None):
    """Finds target epic directory from CLI argument, current working dir, or .context symlink."""
    if explicit_path:
        p = Path(explicit_path).resolve()
        if p.is_dir():
            return p
        raise FileNotFoundError(f"Specified epic directory not found: {explicit_path}")
        
    cwd = Path.cwd()
    # 1. Cwd is an epic directory
    if (cwd / "epic.md").exists() or (cwd / "dag.json").exists():
        return cwd
        
    # 2. Inside a code repo with .context
    context_epics = cwd / ".context" / "epics"
    if context_epics.is_dir():
        epics = [d for d in context_epics.iterdir() if d.is_dir() and not d.name.startswith(".")]
        if len(epics) == 1:
            return epics[0]
        elif len(epics) > 1:
            # Look for active action status or return first
            for e in epics:
                dag_file = e / "dag.json"
                if dag_file.exists():
                    return e
            return epics[0]

    # 3. Running from vault/projects/.../epics/<epic>
    if "epics" in cwd.parts:
        idx = cwd.parts.index("epics")
        if len(cwd.parts) > idx + 1:
            epic_path = Path(*cwd.parts[:idx+2])
            if epic_path.is_dir():
                return epic_path

    raise RuntimeError("Could not automatically locate epic directory. Please use --epic <path>.")

def load_or_compile_dag(epic_dir, force_recompile=False):
    dag_path = epic_dir / "dag.json"
    if dag_path.exists() and not force_recompile:
        with open(dag_path, "r", encoding="utf-8") as f:
            return json.load(f), dag_path
            
    # Compile from tasks/*.md
    tasks_dir = epic_dir / "tasks"
    tasks = {}
    if tasks_dir.is_dir():
        for task_file in sorted(tasks_dir.glob("*.md")):
            with open(task_file, "r", encoding="utf-8") as f:
                fm, _ = parse_frontmatter(f.read())
            task_id = fm.get("@id") or task_file.stem
            # Clean "task:" prefix if present
            task_id = re.sub(r"^task:", "", task_id)
            
            title = fm.get("name") or task_file.stem
            raw_status = fm.get("ticketStatus") or fm.get("status") or "ready"
            dependencies = fm.get("dependencies") or []
            assignee = fm.get("assignee")
            commit_hash = fm.get("resultCommit")
            
            tasks[task_id] = {
                "id": task_id,
                "title": title,
                "status": raw_status,
                "dependencies": dependencies,
                "blockedBy": [],
                "file": f"tasks/{task_file.name}",
                "assignee": assignee,
                "commitHash": commit_hash
            }

    # Evaluate blocked / ready status
    for t_id, t_info in tasks.items():
        if t_info["status"] in ["completed", "in_review", "in_progress"]:
            continue
        unresolved = [dep for dep in t_info["dependencies"] if dep in tasks and tasks[dep]["status"] != "completed"]
        if unresolved:
            t_info["status"] = "blocked"
            t_info["blockedBy"] = unresolved
        else:
            t_info["status"] = "ready"
            t_info["blockedBy"] = []

    dag_data = {
        "epicId": epic_dir.name,
        "project": epic_dir.parent.parent.name,
        "tasks": tasks
    }

    with open(dag_path, "w", encoding="utf-8") as f:
        json.dump(dag_data, f, indent=2)

    return dag_data, dag_path

def save_dag(dag_path, dag_data):
    with open(dag_path, "w", encoding="utf-8") as f:
        json.dump(dag_data, f, indent=2)

def cmd_compile(args):
    epic_dir = resolve_epic_dir(args.epic)
    dag_data, dag_path = load_or_compile_dag(epic_dir, force_recompile=True)
    print(f"[✓] Compiled DAG for epic '{dag_data['epicId']}' with {len(dag_data['tasks'])} task(s) into {dag_path}")

def cmd_next(args):
    epic_dir = resolve_epic_dir(args.epic)
    dag_data, _ = load_or_compile_dag(epic_dir)
    tasks = dag_data.get("tasks", {})

    ready_tasks = [t for t in tasks.values() if t.get("status") == "ready"]
    
    if args.json:
        print(json.dumps(ready_tasks if args.all else (ready_tasks[0] if ready_tasks else None), indent=2))
    else:
        if not ready_tasks:
            print("No tasks currently in 'ready' state.")
        elif args.all:
            print(f"Ready tasks ({len(ready_tasks)}):")
            for t in ready_tasks:
                print(f"  - [{t['id']}] {t['title']} (File: {t['file']})")
        else:
            t = ready_tasks[0]
            print(f"Next Ready Task: [{t['id']}] {t['title']}")
            print(f"File: {epic_dir / t['file']}")

def cmd_claim(args):
    epic_dir = resolve_epic_dir(args.epic)
    dag_data, dag_path = load_or_compile_dag(epic_dir)
    task_id = args.task_id
    agent_name = args.agent or "worker-agent"

    if task_id not in dag_data["tasks"]:
        print(f"[!] Error: Task '{task_id}' not found in dag.json", file=sys.stderr)
        sys.exit(1)

    task = dag_data["tasks"][task_id]
    if task["status"] == "blocked":
        print(f"[!] Warning: Task '{task_id}' is BLOCKED by {task.get('blockedBy', [])}", file=sys.stderr)
        if not args.force:
            sys.exit(1)

    task["status"] = "in_progress"
    task["assignee"] = agent_name
    save_dag(dag_path, dag_data)

    # Sync markdown frontmatter
    task_md_path = epic_dir / task["file"]
    update_frontmatter_in_file(task_md_path, {
        "ticketStatus": "in_progress",
        "actionStatus": "ActiveActionStatus",
        "assignee": agent_name
    })

    print(f"[✓] Claimed task [{task_id}] by '{agent_name}'. Status updated to 'in_progress'.")

def cmd_complete(args):
    epic_dir = resolve_epic_dir(args.epic)
    dag_data, dag_path = load_or_compile_dag(epic_dir)
    task_id = args.task_id
    commit_hash = args.commit or "HEAD"

    if task_id not in dag_data["tasks"]:
        print(f"[!] Error: Task '{task_id}' not found in dag.json", file=sys.stderr)
        sys.exit(1)

    task = dag_data["tasks"][task_id]
    task["status"] = "completed"
    task["commitHash"] = commit_hash
    task["blockedBy"] = []

    # Update markdown frontmatter for completed task
    task_md_path = epic_dir / task["file"]
    update_frontmatter_in_file(task_md_path, {
        "ticketStatus": "completed",
        "actionStatus": "CompletedActionStatus",
        "resultCommit": commit_hash
    })

    # Recalculate blocked/ready states for downstream tasks
    newly_unblocked = []
    for other_id, other_task in dag_data["tasks"].items():
        if other_task["status"] == "blocked":
            other_task["blockedBy"] = [dep for dep in other_task["dependencies"] if dag_data["tasks"].get(dep, {}).get("status") != "completed"]
            if not other_task["blockedBy"]:
                other_task["status"] = "ready"
                newly_unblocked.append(other_id)
                # Update markdown frontmatter for unblocked task
                other_md_path = epic_dir / other_task["file"]
                update_frontmatter_in_file(other_md_path, {
                    "ticketStatus": "ready",
                    "actionStatus": "PotentialActionStatus"
                })

    save_dag(dag_path, dag_data)

    print(f"[✓] Completed task [{task_id}] (Commit: {commit_hash}).")
    if newly_unblocked:
        print(f"[+] Newly UNBLOCKED and promoted to READY: {', '.join(newly_unblocked)}")

def cmd_status(args):
    epic_dir = resolve_epic_dir(args.epic)
    dag_data, _ = load_or_compile_dag(epic_dir)
    
    if args.json:
        print(json.dumps(dag_data, indent=2))
        return

    tasks = dag_data.get("tasks", {})
    print(f"=== Epic: {dag_data.get('epicId')} (Project: {dag_data.get('project')}) ===")
    print(f"{'TASK ID':<18} {'STATUS':<14} {'ASSIGNEE':<16} {'BLOCKED BY / COMMIT'}")
    print("-" * 75)
    for t_id, t in tasks.items():
        extra = ""
        if t["status"] == "blocked":
            extra = f"Blocked by: {', '.join(t.get('blockedBy', []))}"
        elif t["status"] == "completed":
            extra = f"Commit: {t.get('commitHash') or 'done'}"
        print(f"{t_id:<18} {t['status']:<14} {str(t.get('assignee') or '-'):<16} {extra}")

def main():
    parser = argparse.ArgumentParser(description="Deterministic DAG Task CLI & State Engine")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # compile
    p_compile = subparsers.add_parser("compile", help="Compile tasks/*.md into dag.json")
    p_compile.add_argument("--epic", help="Path to epic directory")

    # next
    p_next = subparsers.add_parser("next", help="Get next ready task")
    p_next.add_argument("--epic", help="Path to epic directory")
    p_next.add_argument("--all", action="store_true", help="List all ready tasks")
    p_next.add_argument("--json", action="store_true", help="Output JSON format")

    # claim
    p_claim = subparsers.add_parser("claim", help="Claim a ready task")
    p_claim.add_argument("task_id", help="ID of task to claim")
    p_claim.add_argument("--agent", help="Name of claiming agent", default="worker-agent")
    p_claim.add_argument("--epic", help="Path to epic directory")
    p_claim.add_argument("--force", action="store_true", help="Force claim even if blocked")

    # complete
    p_complete = subparsers.add_parser("complete", help="Complete a task")
    p_complete.add_argument("task_id", help="ID of task to mark complete")
    p_complete.add_argument("--commit", help="Commit hash or reference", default="HEAD")
    p_complete.add_argument("--epic", help="Path to epic directory")

    # status
    p_status = subparsers.add_parser("status", help="Show DAG status")
    p_status.add_argument("--epic", help="Path to epic directory")
    p_status.add_argument("--json", action="store_true", help="Output JSON format")

    args = parser.parse_args()
    
    if args.command == "compile":
        cmd_compile(args)
    elif args.command == "next":
        cmd_next(args)
    elif args.command == "claim":
        cmd_claim(args)
    elif args.command == "complete":
        cmd_complete(args)
    elif args.command == "status":
        cmd_status(args)

if __name__ == "__main__":
    main()
