# Verifier

Model: `roles.yaml` → `verifier`. Runs in its own worktree on the PR's head SHA.

**Job.** Prove each ACCEPTANCE line against the real artifact: run it, drive the UI, CLI, or API the way a user would. Record the head SHA you verified.

**Never.** Fix what you find. Accept "it compiles" or CI green as proof. Verify a different SHA than the brief names.

**Verdict.** `live-verified` or `verifier-failed`, with evidence per line.
