### Refactoring

**You own the contract. Structure changes. Behavior does not.** A missing feature or real bug found on the way splits into its own ticket.

1. **What.** Agree with the user why this structure must change and what better means (fewer states, fewer layers, a seam for a coming feature).
2. Pin the behavior. An explorer maps the subsystem. A worker writes a characterization test or equivalence harness before any structure moves. Type check and lint are not a pin.
3. **How.** Name the target shape as if built today (**principle-model-the-domain**, **principle-redesign-from-first-principles**). The reshape must delete branches or invalid states, not add indirection. Present it with alternatives. The user picks.
4. Subtract first (**principle-subtract-before-you-add**). Dead code, one-caller wrappers, and orphan references go before the new shape. The smallest change that reaches the target ships (**principle-laziness-protocol**).
5. Brief the move in small behavior-preserving units, each keeping the pin green. Workers run with `isolation: "worktree"`. An API reshape migrates every caller and deletes the old API in the same wave.
6. Prove behavior is unchanged on the real artifact (**principle-prove-it-works**).
7. Keep it only if reader load drops (**principle-minimize-reader-load**). Otherwise revert.
8. Run **Review** (`playbooks/review.md`). **Accept:** the user sees the equivalence proof and the reader-load change. Then **Opening a PR** (`playbooks/opening-a-pr.md`).

**Reply:** the structure that changed, the pin it held against, the equivalence proof, the reader-load change, and what got reverted.
