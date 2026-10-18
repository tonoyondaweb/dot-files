### Refactoring

**You own the contract. Structure changes. Behavior does not.** A missing feature or real bug found on the way splits into its own ticket.

1. Pin the behavior. An explorer maps the subsystem. A worker writes a characterization test or equivalence harness before any structure moves. Type check and lint are not a pin.
2. Name the target shape as if built today (**principle-model-the-domain**, **principle-redesign-from-first-principles**). The reshape must delete branches or invalid states, not add indirection.
3. Subtract first (**principle-subtract-before-you-add**). Dead code, one-caller wrappers, and orphan references go before the new shape. The smallest change that reaches the target ships (**principle-laziness-protocol**).
4. Brief the move in small behavior-preserving units, each keeping the pin green. Workers run with `isolation: "worktree"`. An API reshape migrates every caller and deletes the old API in the same wave.
5. Prove behavior is unchanged on the real artifact (**principle-prove-it-works**).
6. Keep it only if reader load drops (**principle-minimize-reader-load**). Otherwise revert.
7. Run **Review** (`playbooks/review.md`), then **Opening a PR** (`playbooks/opening-a-pr.md`).

**Reply:** the structure that changed, the pin it held against, the equivalence proof, the reader-load change, and what got reverted.
