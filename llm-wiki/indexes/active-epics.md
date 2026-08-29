---
@context: "https://schema.org"
@type: "ItemList"
@id: "moc:active-epics"
name: "Active Epics & Work Planning Dashboard"
description: "Cross-project status dashboard of in-flight epics and milestone progress"
dateModified: "2026-08-28"
tags:
  - moc/epics
---

# Active Epics & Work Planning Dashboard

## In-Flight Milestones

```dataview
TABLE actionStatus AS "Status", priority AS "Priority", isPartOf AS "Project"
FROM "projects"
WHERE file.name = "epic"
```
