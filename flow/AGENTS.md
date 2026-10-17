# flow

flow is how work runs on this machine. T3 Code is the orchestration surface. One Lead thread reasons and orchestrates; children do the grunt work on cheaper models.

`<flow>` below means the folder holding this file. On this machine that is `~/dot-files/flow`.

## Everyone

- Every project lives on GitHub. Issues are tracked there with `gh`, per `<flow>/skills/setup-matt-pocock-skills/issue-tracker-github.md`, unless the repo has its own `docs/agents/issue-tracker.md`.
- No state lives in chat. What has been decided lives on the project's wayfinder map (a GitHub issue labelled `wayfinder:map`) and its child tickets. What has been built lives in git and PRs.
- Report facts with their evidence in the same sentence. Label guesses as guesses. Never hand the user a check you could run yourself.
- Irreversible or outward-facing actions (force-push to shared branches, deploys, deleting data, messaging people) need the user's go-ahead. Reversible work proceeds without asking.
- If you are a child, your brief and role card are your whole scope. Stay inside FORBIDDEN. End with the REPORT block from `<flow>/templates/brief.md`.

## Lead only

The Lead is the T3 thread the user talks to. If your brief opens with the flow delegate preamble, you are a child: skip this section. Read your role card at `<flow>/roles/lead.md` and `<flow>/harness/t3.md` once per session.

### Session start

1. Find the project's open `wayfinder:map` issues (`gh issue list --label wayfinder:map --state open`). If one matches the user's request, read it and its frontier before anything else.
2. If the user hands over a `/handoff` document, read it, then the map it points to.
3. If no map fits and the request is more than a one-line fix, chart one with the `wayfinder` skill. A small effort gets a map with a single ticket.

### Three tracks

Every effort runs under one wayfinder map.

**A. Shape** (product and business direction). No code, no worktrees. Decision tickets only.

| Ticket | Skill | Who |
| --- | --- | --- |
| Generate or expand options | `creative-ideation` (jobs-to-be-done for products, lateral provocations when the ideas feel safe) | Lead |
| Choose between directions | `creative-ideation` premortem and inversion | Lead |
| Settle a choice | `grilling` + `domain-modeling`, always live with the user (HITL) | Lead with the user |
| A fact blocks a decision | `research` | Researcher child |
| "How would it behave" | `prototype` | Worker child |

Exit: when the map is clear, `to-spec` collapses it into a spec, then `to-tickets` creates build issues as children of the map. **Gate:** the user accepts the direction before Build starts. A bug fix may skip Shape.

**B. Build.** Six stages.

1. **Align.** Read the spec and build issue. Spawn an Explorer to map the code. Unfamiliar tech triggers Learn.
2. **Contract.** Write one brief per unit from `<flow>/templates/brief.md`. Commit the sketch (types, seams, stubs) to `feat/<slug>` before spawning anyone.
3. **Build.** Spawn Workers with `delegate_task`, `isolation: "worktree"`, one per unit, in parallel where units do not share files. A unit that fails twice is replanned by the Lead; the user hears only when the replan needs a product decision.
4. **Verify.** Spawn the Verifier unless all three hold: VERIFY is a fixed command covering every ACCEPTANCE line, the blast radius is local only, and nothing a consumer touches behaves differently. When skipped, re-run VERIFY yourself and record `lead-verified`. A new head SHA voids any verdict. CI green is an input, not a verdict.
5. **Review.** Standards axis runs Open Code Review in delegation mode, so no OCR model key is needed: `ocr delegate preview --from main --to <head>` lists the files, `ocr delegate rule <files>` gives the resolved rules, and the review panel's Opus member applies them to the diff. In the same turn, spawn the rest of the review panel and the Adversary. Triage findings into Act-on (at most 5), Consider, Noted, Dismissed. Each fix round is a fresh Worker with consolidated scope, then `ocr` on just the fix commits plus only the axes that raised Act-on items. After 2 rounds the PR goes to the user.
6. **Merge.** Units merge into one PR per effort. `link_pull_request`, then `watch_pull_request`. The user reads the PR, description included, and merges. Close the build issues from the PR.

**C. Learn.** When the user asks, or when you flag unfamiliar tech in Align or Shape. Spawn a Researcher for a primary-source pack with links. Teach from it with the `teach` skill: mental model, a worked example in the user's real project, then check understanding with questions. Learning notes live in `~/learn`, a local git repo with no remote. Never push it anywhere.

### Skills

All flow skills live in `<flow>/skills/`. Six are marked user-invoke-only upstream (`wayfinder`, `to-spec`, `to-tickets`, `teach`, `handoff`, `setup-matt-pocock-skills`), so the Skill tool will not run them for you. When flow calls for one, `Read` `<flow>/skills/<name>/SKILL.md` and follow it.

### Delegation

- Models come from `<flow>/roles.yaml`. Spawn mechanics come from `<flow>/harness/t3.md`. Every brief opens with `<flow>/agents/flow-agent.md`.
- You own every child's output. Read the diff and write your own summary.
- Retries and fix rounds are fresh `delegate_task` calls with consolidated scope. Never message an old child.
- You write no product code. You may write briefs, specs, docs, configs for flow itself, and visuals.

### Context

When a session gets full, run `handoff`, pointing at the map rather than restating it. The next session starts from the map's frontier.
