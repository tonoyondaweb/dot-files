# dot-files

Personal configuration. The main thing here is **flow**, the agent workflow I run through T3 Code.

## flow

Plain files, no installer. Point any agent at them however it loads instructions and skills.

```
flow/
├── AGENTS.md            # operating rules: tracks, stages, gates, delegation
├── roles.yaml           # role → provider/model/effort registry (regenerate with setup-flow)
├── roles/*.md           # one card per role: job, never, done-when
├── agents/flow-agent.md # preamble every delegate brief starts with
├── harness/t3.md        # flow terms → T3 primitives (delegate_task, worktrees, PR watch)
├── templates/brief.md   # brief template and per-role REPORT schemas
├── skills/              # vendored skills (see skills/README.md) + setup-flow
└── licenses/            # upstream licenses for vendored skills
```

### How this machine loads it

| Agent | Wiring |
| --- | --- |
| Claude Code (the T3 Lead, Claude children) | `~/.claude/CLAUDE.md` contains `@~/workspace/code/dot-files/flow/AGENTS.md`. Each `flow/skills/*` is symlinked into `~/.claude/skills/`. A global `~/.claude/AGENTS.md` is **not** read (tested on Claude Code 2.1.301). |
| OpenCode, Antigravity children | Nothing global. Every brief opens with `agents/flow-agent.md`, which makes the child read `AGENTS.md`, its role card, and named skills by absolute path. |
| Open Code Review | `npm install -g @alibaba-group/open-code-review`. Used in delegation mode (`ocr delegate`), so no OCR model key. |
| Learning notes | `~/learn`, a local git repo with no remote. |
