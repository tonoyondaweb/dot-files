# Brief template

The Lead fills one per child. Open with the preamble from `<flow>/agents/flow-agent.md`.

```
ROLE: <worker | hardest-tasks | explorer | researcher | verifier | adversary>
MAP: <wayfinder map issue URL>        TICKET: <issue URL>
BRANCH: <branch to check out / commit to>   BASE SHA: <sha>
SKILLS: <skill names to read, or none>
PRINCIPLES: <principle-* names that govern this unit, or none>
ISOLATION: <worktree | shared>

GOAL: <one sentence: what is true when this is done>
CONTEXT: <file pointers, not pasted content; prior reports for fix rounds>
ACCEPTANCE:
  - <observable behaviour 1>
  - <observable behaviour 2>
VERIFY: <exact command(s) that prove ACCEPTANCE, or "manual: <steps>">
FORBIDDEN:
  - <paths or actions out of scope>
REPORT: <the schema for this role, below>
```

## REPORT schemas

Every REPORT starts with `STATUS: done | blocked | failed`, includes `PRINCIPLES:` (each one applied and the choice it changed, or none), and ends with `GUESSES:` (anything not verified, or `none`).

**worker / hardest-tasks**
```
STATUS:
COMMITS: <sha  subject>, one per line
ACCEPTANCE: <line> → <evidence: command + output excerpt>
VERIFY: <command> → <exit code>
FILES: <paths touched>
DEVIATIONS: <where you departed from the brief and why, or none>
GUESSES:
```

**explorer**
```
STATUS:
ANSWER: <direct answer to the brief's question>
POINTERS: <path:line  what it is>, one per line
COMMANDS: <how to build / test / run, as found>
GIT STATUS: <output of git status --porcelain; must be empty>
GUESSES:
```

**researcher**
```
STATUS:
ANSWER: <direct answer>
CLAIMS: <claim> — <primary source URL>, one per line
OPEN: <what the sources did not settle>
FILE: <path of the findings file, if written>
GUESSES:
```

**verifier**
```
STATUS:
HEAD SHA: <sha verified>
VERDICT: live-verified | verifier-failed
ACCEPTANCE: <line> → pass | fail — <evidence>
REPRO: <steps for each failure>
GUESSES:
```

**adversary**
```
STATUS:
FINDINGS: <severity: high | medium | low> <path:line> — <failure scenario: input/state → wrong result>
CHECKED: <angles attacked that held up>
GUESSES:
```
