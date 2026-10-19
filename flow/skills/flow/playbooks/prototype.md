### Prototype

**The user owns the decision. You own the evidence.** The prototype is throwaway. The real build follows Feature.

Speed over polish. Code quality does not matter here. The rigor is in picking the right design cheaply.

1. Name the decision the prototype exists to inform, and confirm it with the user. No decision means no prototype.
2. `Read` `<flow>/skills/prototype/SKILL.md` and brief a worker from it, `isolation: "worktree"`. The skill decides where the code sits. The worktree branch is the throwaway branch and never merges to `main`.
3. When comparing competing directions, spawn the `arena-runners` panel in one turn, one variant each, every runner in its own worktree. A judge (`<flow>/roles/judge.md`) from `cross-judge-pool`, of a different family than yours when possible, scores them read-only against a rubric you write first (**principle-exhaust-the-design-space**). Variants of one idea go behind one switcher instead, each labeled.
4. Observe the thing being decided: screenshots via `preview_*` or `device_*` for visual decisions, printed output or timing for behavioral ones. The observation is the test.
5. Present the evidence and your recommendation. The user decides. Record the decision, the user's reason, and the evidence on the wayfinder ticket. Hand the chosen direction back to Shape or Feature.

**Reply:** the variants explored, the evidence, the tradeoffs, your recommendation, and the scratch path. Say plainly that it is throwaway.
