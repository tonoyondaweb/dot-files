### Pause safely

**You own a clean stop.** Explicit only. "Keep going" or "don't stop" means do not pause.

1. Stop at a safe boundary. Start nothing new. `task_cancel` any running children so no writer is left.
2. Take no irreversible action to pause.
3. Make the work durable. Each worktree with uncommitted edits gets one `wip:` commit on its branch.
4. Update the map. Close finished tickets and note the in-flight one with its branch.
5. `Read` `<flow>/skills/handoff/SKILL.md` and write the handoff, pointing at the map rather than restating it.

**Reply:** where the work stands, the commits made, the handoff path, and the first action on resume.
