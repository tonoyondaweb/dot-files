# Vault Navigation Codex & Agent Protocol

Welcome, Agent. This Obsidian vault is the **Single Source of Truth for Knowledge, Architecture, and Work Planning**.
Code repositories NEVER contain specifications, PRDs, ADRs, or tickets—they all live exclusively in this vault.

---

## 1. Vault Directory Map
```
vault/
├── inbox/         # Staging area for raw notes, meeting dumps, and external captures.
├── knowledge/     # Curated domain knowledge, patterns, and tool definitions (Schema.org DefinedTerm).
├── projects/      # Project-specific planning: index.md, ADRs, and Epics with task DAGs.
├── indexes/       # Maps of Content (MOCs) providing O(1) jump points across the vault.
├── assets/        # Media, diagrams, Excalidraw files, attachments.
├── templates/     # Standard Schema.org frontmatter templates.
└── scripts/       # Local automation utilities: dag.py, sync-workspace.sh.
```

---

## 2. Fast Navigation via Maps of Content (MOCs)
Do not perform expensive recursive scans across the vault. Use the centralized MOCs:
- **Project Index:** `[[indexes/project-catalog]]` - Master list of all projects and linked code repos.
- **Concept Catalog:** `[[indexes/concept-catalog]]` - Catalog of domain terms, design patterns, and libraries.
- **Active Epics:** `[[indexes/active-epics]]` - Live status of all in-flight milestones and tasks.

---

## 3. Graph Traversal Protocols
Traverse notes using their Schema.org frontmatter and `[[wikilinks]]`:
- **Upwards:** Follow `isPartOf` (Task -> Epic -> Project).
- **Downwards:** Follow `hasPart` (Project -> Epics -> Tasks).
- **Sideways:** Follow `about` or `mentions` (Project/Epic -> Knowledge concepts).
- **Precedence:** Follow `dependencies` in task subdocuments.

---

## 4. Deterministic Task Operations
When interacting with project epics and tasks:
```bash
# Query the next available ready task for an epic
python3 scripts/dag.py next --epic projects/<project-id>/epics/<epic-id>

# Check overall epic task status (shows blocked vs ready)
python3 scripts/dag.py status --epic projects/<project-id>/epics/<epic-id>

# Atomically claim a task
python3 scripts/dag.py claim <TASK-ID> --agent <your-agent-name> --epic projects/<project-id>/epics/<epic-id>

# Mark task completed with commit hash (auto-unblocks downstream tasks)
python3 scripts/dag.py complete <TASK-ID> --commit <SHA> --epic projects/<project-id>/epics/<epic-id>
```
