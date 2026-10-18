# dot-files

Personal configuration. The main thing here is **flow**, the agent workflow I run through T3 Code.

## flow

Plain files, no installer. Point any agent at them however it loads instructions and skills.

```
flow/
├── AGENTS.md            # rules for everyone; points the Lead at the router
├── AUTHORING.md         # how to edit flow itself
├── roles.yaml           # role → provider/model/effort registry (regenerate with setup-flow)
├── roles/*.md           # one card per role: job, never, done-when
├── agents/flow-agent.md # preamble every delegate brief starts with
├── harness/t3.md        # flow terms → T3 primitives (delegate_task, worktrees, PR watch)
├── templates/brief.md   # brief template and per-role REPORT schemas
├── skills/flow/         # /flow router: triggers, principles index, playbooks/
├── skills/principle-*/  # 20 principles, read by path (not linked)
├── skills/              # vendored workflow skills (see skills/README.md) + setup-flow
└── licenses/            # upstream licenses for vendored skills
```

### How this machine loads it

| Agent | Wiring |
| --- | --- |
| Claude Code (the T3 Lead, Claude children) | `~/.claude/CLAUDE.md` contains `@~/workspace/code/dot-files/flow/AGENTS.md`. Each workflow skill in `flow/skills/` (not the `principle-*` ones) is symlinked into `~/.claude/skills/`. A global `~/.claude/AGENTS.md` is **not** read (tested on Claude Code 2.1.301). |
| OpenCode (threads and children) | `~/.config/opencode/AGENTS.md` is a symlink to `flow/AGENTS.md`. OpenCode also reads the skills in `~/.claude/skills`, but hides user-invoke-only ones and makes no slash commands from skills, so `~/.config/opencode/command/flow.md` is a symlink to `flow/harness/opencode/command/flow.md` to provide `/flow`. |
| Antigravity | Nothing global. `~/.gemini/GEMINI.md`, `~/.gemini/config/AGENTS.md` and `~/.gemini/config/rules/AGENTS.md` were all ignored under T3's Antigravity driver (tested). Children get flow from the brief preamble (`agents/flow-agent.md`). Do not use Antigravity as a top-level Lead. |
| Open Code Review | `npm install -g @alibaba-group/open-code-review`. Used in delegation mode (`ocr delegate`), so no OCR model key. |
| Learning notes | `~/learn`, a local git repo with no remote. |
