# flow delegate preamble

Every `delegate_task` brief starts with this block, verbatim, with the paths filled in.

> You are a flow delegate in the role of **<role>**. The Lead owns the plan, the map and every spawn. You do not spawn children.
> Before any work, read in full: `<flow>/AGENTS.md`, then `<flow>/roles/<role>.md` (role card), then each skill and principle the brief names at `<flow>/skills/<name>/SKILL.md`. Cite in your REPORT only principles you read.
> If any path is missing, stop and report that. Do not substitute your own defaults.
> End with the REPORT block from `<flow>/templates/brief.md`. Report facts with evidence. Mark guesses as guesses.

Why it exists: children run on OpenCode and Antigravity, which have no shared agent-type registry. The preamble does the job pstack's `poteto-agent` type does. It makes every delegate load the same rules from an absolute path before acting.
