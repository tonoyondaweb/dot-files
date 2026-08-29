---
@context: "https://schema.org"
@type: "ItemList"
@id: "moc:project-catalog"
name: "Master Project Catalog"
description: "Master index of all projects, repositories, and active milestones"
dateModified: "2026-08-28"
tags:
  - moc/projects
---

# Master Project Catalog

## Active Projects
| Project | Status | Code Repository | Active Epics |
| :--- | :--- | :--- | :--- |

```dataview
TABLE status, codeRepository, hasPart AS "Active Epics"
FROM "projects"
WHERE file.name = "index"
```
