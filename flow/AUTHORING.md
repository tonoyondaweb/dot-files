# Authoring flow

How to edit flow itself. The structure follows [p3-stack](https://github.com/uzairansaruzi/p3-stack), which ports [pstack](https://github.com/cursor/plugins/tree/main/pstack) to T3. flow keeps its own skill set and its own worktree rule.

## Layout

- `skills/flow/SKILL.md` is the router. It holds the start-up, the trigger-to-skill table, the principles index, autonomy, subagents, the reply rules, and the playbook list.
- `skills/flow/playbooks/<name>.md` is one playbook: a bold ownership line, numbered steps, and a `**Reply:**` line. Steps are copied verbatim into the Lead's todolist, so each step is one action.
- `skills/principle-<name>/SKILL.md` is a principle, vendored from p3-stack. Each is `disable-model-invocation: true` and read by path.
- Vendored workflow skills stay as their upstream wrote them. Record the source and commit in `skills/README.md`.
- `harness/t3.md` is the only place T3 mechanics are spelled out. Playbooks name T3 tools but defer details there.

## Rules

- Restricted skill set. A playbook may route only to skills in `skills/` and principles in `skills/principle-*`. Adding a skill is a decision recorded on a wayfinder ticket first.
- Isolation. Code-writing children use `delegate_task` with `isolation: "worktree"`. Never route a child through `t3_thread_launch` or `create_threads`.
- Absolute paths. Anything a child reads is named as `<flow>/...`, which the preamble resolves to `~/workspace/code/dot-files/flow`. Never a path relative to the child's checkout.
- No model slugs outside `roles.yaml`. Playbooks name roles.
- No packaging. flow is plain files. Wiring is symlinks documented in the repo README.
- No workspace coupling. flow never writes to or depends on the user's `AGENTS.md`, `CLAUDE.md`, or agent config. The only entry points are `/flow` and the delegate preamble.
- Thin over complete. Keep the shortest file that still changes behavior.

## Definition of done for a change

1. Every skill or principle a file names resolves: `grep -ohE 'principle-[a-z-]+' -r skills | sort -u` and each one exists under `skills/`.
2. No foreign mechanisms remain in `skills/flow/`, `skills/principle-*`, `roles/`, `templates/`, and `agents/` (not `harness/t3.md`, whose mapping table names them on purpose): grep for `Cursor`, `Task tool`, `subagent_type`, `t3_thread_launch` outside the "not for children" notes, `p3-models`, `/loop`, and skill names flow does not ship (`how`, `why`, `architect`, `arena` as a whole word (the `arena-runners` panel is flow's own), `swarm`, `interrogate`, `unslop`, `tdd`, `show-me-your-work`, `figure-it-out`).
3. `/flow` still prints its `flow: active` line in a fresh Claude Code session and a fresh OpenCode session.
