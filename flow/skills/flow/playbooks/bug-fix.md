### Bug fix

**You own the diagnosis. Children reproduce and fix.** A bug fix may skip Shape but still gets a map, often one ticket.

Every shipped line traces to runtime evidence. A change that "might help" is a hypothesis, not a fix. When evidence refutes a hypothesis, revert what it motivated.

1. Reproduce on the matching surface: a test, a script, `preview_*` for browser UIs, `device_*` for simulators. Ask the user only with a specific reason those cannot reach it. If it will not reproduce, synthesize the trigger or instrument until it fires.
2. Find the root cause (**principle-fix-root-causes**). Seed hypotheses in one turn: explorers map the affected code by angle (2 to 4, one when the area is small), and the researcher (`isolation: "shared"`, REPORT only) mines regression history from `git log`, blame, and issues. Then rule hypotheses out one at a time with runtime evidence until one survives. Each cut depends on the last result, so this search stays sequential.
3. Brief the fix from `<flow>/templates/brief.md`. The failing repro is an ACCEPTANCE line. Spawn a worker with `isolation: "worktree"`.
4. Verify on the same surface. The original repro now passes. Run Feature step 4's verifier rule.
5. Order the commits so the failing repro lands before the fix (**principle-sequence-verifiable-units**).
6. Run **Review** (`playbooks/review.md`), then **Opening a PR** (`playbooks/opening-a-pr.md`).

**Reply:** what was broken, the root cause, the fix, and the failing-then-passing repro output verbatim.
