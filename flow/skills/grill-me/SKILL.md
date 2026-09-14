---
name: grill-me
description: "Grill the user relentlessly about a plan, decision, or idea. Grounded in Flow architectural principles. Use when the user wants to stress-test their thinking, resolve a wayfinder decision issue, or uses any 'grill' trigger phrases."
disable-model-invocation: true
---

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Format a round like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

## Grounded in Flow Principles
When evaluating designs and recommending answers, ground questions and pushbacks in Flow's architectural principles:
- **Model the Domain** (`principle-model-the-domain`): Recommend explicit state representations (discriminated unions, state machines, reducers) over boolean flags.
- **Boundary Discipline** (`principle-boundary-discipline`): Challenge where external input validation happens. Keep domain cores clean.
- **Redesign from First Principles** (`principle-redesign-from-first-principles`): Ask whether a proposed change is being bolted onto an old design rather than structured cleanly from day one.
- **Attack the Premise** (`principle-attack-the-premise`): When an approach creates complex workarounds, challenge the unexamined assumption causing the complexity.
- **Idempotency** (`principle-make-operations-idempotent`): Question failure recovery and replay behavior.

If a decision fork is multi-faceted and involves complex user choices, run `/to-questionnaire`.

## Facts vs Decisions
Finding _facts_ is your job, never the user's. When a frontier question needs a fact from the environment (filesystem, git history, existing types), dispatch a sub-agent using the `understand` skill; don't ask the user for anything you could look up yourself. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait for the sub-agent to report; ask the rest of the frontier now. 

The _decisions_ are the user's: put each to them and wait.

## Session Completion
The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on it until the user confirms you have reached a shared understanding.

When grilling a `wayfinder` issue:
1. Post the resolved decision as an ADR comment on the GitHub issue using `gh issue comment`.
2. Close the issue using `gh issue close`.
3. If all issues on the parent map are resolved, invoke `/to-spec`.
