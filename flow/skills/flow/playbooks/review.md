### Review

**You own the triage.** Runs on the head SHA the verifier or `lead-verified` passed.

1. Standards axis via Open Code Review in delegation mode, so no OCR model key is needed. `ocr delegate preview --from main --to <head>` lists the files. `ocr delegate rule <files>` gives the resolved rules.
2. In the same turn, spawn the review panel from the registry (each with the diff, the rules for its axis, and `isolation: "shared"`) and the adversary. The panel's Opus member applies the OCR rules.
3. Triage every finding into Act-on (at most 5), Consider, Noted, Dismissed. Dismiss with a concrete reason. Findings two families agree on rank first.
4. Each fix round is a fresh worker with consolidated scope, `isolation: "worktree"`. Then re-run `ocr` on just the fix commits, plus only the axes that raised Act-on items.
5. After 2 fix rounds, stop and hand the PR to the user with the remaining findings.

**Reply:** findings by bucket with reasons, what each fix round changed, and what is left for the user.
