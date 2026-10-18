### Feature

**You own the design. Plan, brief, verify.** Children implement. You write no product code.

1. **Align.** Read the spec and the build issue. Map the affected code with explorers (`isolation: "shared"`): one per angle (subsystem, data flow, tests), 2 to 4 in one turn, within the in-flight cap. A simple change gets one. Read their pointers and merge them yourself. Flag unfamiliar tech in the same turn: the Learn researcher starts alongside the explorers, then **Learn** runs before Contract.
2. **Contract.** Name the data shape and its structure (**principle-model-the-domain**, **principle-foundational-thinking**). Write the throughput checkpoint as four todo items, keeping any that do not apply with `n/a: <reason>`:
   - **Blocking first steps.** Gates that run before fan-out.
   - **Independent units.** Disjoint files or layers parallelize. Shared writes serialize.
   - **Shared mutable state.** Split the target first (**principle-separate-before-serializing-shared-state**).
   - **Smallest safe decomposition.** If one worker is best, name why.
   A contested design that crosses a function boundary gets a design arena first: the `arena-runners` panel sketches it in one turn, a judge from `cross-judge-pool` picks, and you fold the best parts in (**principle-exhaust-the-design-space**).
   Write one brief per unit from `<flow>/templates/brief.md`, each unit ending in a check (**principle-sequence-verifiable-units**). Commit the sketch (types, seams, stubs) to `feat/<slug>` before spawning anyone.
3. **Build.** Spawn one worker per unit with `delegate_task`, `isolation: "worktree"`, `mode: "async"`, where units share no files. Use a rolling window under the in-flight cap (`<flow>/harness/t3.md`): spawn each unit as soon as its blockers land, never in batches. Cross-cutting or subtle units go to `hardest-tasks`. A unit that fails twice gets replanned by you (**principle-attack-the-premise**). The user hears only when the replan needs a product decision.
4. **Verify.** Spawn the verifier (`isolation: "worktree"` at the head SHA) unless all three hold: VERIFY is a fixed command covering every ACCEPTANCE line, the blast radius is local only, and nothing a consumer touches behaves differently. When skipped, re-run VERIFY yourself and record `lead-verified`. A new head SHA voids any verdict. CI green is an input, not a verdict (**principle-prove-it-works**). UI changes are proven on the real surface with `preview_*` or `device_*`: by the verifier if its harness exposes them, otherwise by you.
5. **Review.** Run **Review** (`playbooks/review.md`).
6. **Merge.** Merge the unit branches into one PR and run **Opening a PR** (`playbooks/opening-a-pr.md`).

**Reply:** what was built and for whom, the data shape chosen and why, the throughput checkpoint, the verdict (`live-verified` or `lead-verified`) with its head SHA, the review outcome, the PR link, and open decisions.
