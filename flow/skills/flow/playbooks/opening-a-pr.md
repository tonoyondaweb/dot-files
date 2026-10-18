### Opening a PR

Invoked at the end of every code playbook.

**Commits.** Small and ordered, each one landable and telling the story. Units merge into one PR per effort.

**Titles.** Conventional Commits: `type(scope): subject`, with `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, or `perf`. Short and imperative. No trailing period.

**Descriptions.** A briefing, not a lab notebook. A reviewer with the diff should learn in under a minute why the change exists, what it leaves out, what it could break, and how it was proved. Use `##` sections in this order, dropping any with nothing to say:

- `## Why`. The problem and the approach in one to three sentences. Link the map and the build issues.
- `## What changed`. One to three bullets.
- `## Scope`. What it covers and what it deliberately leaves out.
- `## Tradeoffs`. Only rejected alternatives a reviewer would ask about.
- `## Blast Radius`. Who or what it touches and why that is safe or risky.
- `## Verification`. One to three bullets, each a real run and its outcome, plus the verdict and head SHA. Attach screenshots or recordings when they prove a claim.

**Forge.** `gh` creates, edits, and views. Open the PR ready, never as a draft. Add `Closes #<n>` for each build issue.

**T3.** Call `link_pull_request` with the full URL the moment the PR opens. Then run **Babysit** in `drive` mode (`playbooks/babysit.md`). The user reads the PR, description included, and merges. You never merge.
