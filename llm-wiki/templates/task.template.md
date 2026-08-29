---
@context: "https://schema.org"
@type: "Action"
@id: "task:{{PROJECT_ID}}-TASK-{{NUM}}"
name: "{{TITLE}}"
isPartOf: "[[projects/{{PROJECT_ID}}/epics/{{EPIC_ID}}/epic|{{EPIC_ID}}]]"
actionStatus: "PotentialActionStatus" # PotentialActionStatus | ActiveActionStatus | CompletedActionStatus | BlockedActionStatus
ticketStatus: "ready"                # backlog | ready | in_progress | blocked | in_review | completed
priority: "P2"
dependencies: []
assignee: null
targetRepository: "studio/code/{{PROJECT_ID}}"
resultCommit: null
dateCreated: "{{DATE}}"
dateModified: "{{DATE}}"
tags:
  - type/task
  - status/ready
---

# {{PROJECT_ID}}-TASK-{{NUM}}: {{TITLE}}

## Objective
*Exact verifiable unit of work to be accomplished.*

## Acceptance Criteria
- [ ] Conforms to seam test specification.
- [ ] Strict TDD loop executed (test -> build -> test -> fix).
- [ ] No regression on existing test suite.

## Seam & Spec References
- Spec: `[[../specs/]]`

## Execution Log
*(Worker agent appends execution notes, TDD test runs, and reflections here)*
