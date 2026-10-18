### Learn

**You own the teaching.** Notes stay local.

1. Name what the user needs to understand and why, tied to their real project.
2. Spawn the researcher with the `research` skill for a primary-source pack with links, written to `~/learn/<topic>/sources.md` (`isolation: "shared"`, since `~/learn` is outside the repo). Don't wait on it: while it runs, pin down the mission with the user (what they already know, what they will build with it) per `teach`.
3. `Read` `<flow>/skills/teach/SKILL.md` and teach from the pack with `~/learn/<topic>/` as the teaching workspace: the mental model, a worked example in the user's real project, then questions that check understanding.
4. Commit the workspace in `~/learn`. It has no remote. Never push it anywhere.
5. Return to the playbook that triggered Learn, if any.

**Reply:** the mental model in a few sentences, the sources, the note's path, and what the user's answers showed they still need.
