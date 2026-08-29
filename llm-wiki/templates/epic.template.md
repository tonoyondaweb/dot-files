---
@context: "https://schema.org"
@type: "PlanAction"
@id: "epic:{{PROJECT_ID}}-EPIC-{{NUM}}"
name: "{{TITLE}}"
isPartOf: "[[projects/{{PROJECT_ID}}/index|{{PROJECT_ID}}]]"
actionStatus: "ActiveActionStatus" # PotentialActionStatus | ActiveActionStatus | CompletedActionStatus
priority: "medium"
leadArchitect: "Primary Architect Agent"
dateCreated: "{{DATE}}"
hasPart: []
tags:
  - type/epic
  - status/active
---

# {{PROJECT_ID}}-EPIC-{{NUM}}: {{TITLE}}

## 1. Executive Intent & PRD
*Milestone scope, goals, and non-goals.*

## 2. Seams, Interfaces & Module Boundaries
*Defined by Architect Sub-Agents under `specs/`.*

## 3. Actionable Tickets & DAG
- Deterministic state maintained in `dag.json`.
- Granular subdocuments in `tasks/`.

## 4. Adversarial Review & Reflection
- Review reports stored under `reviews/`.
