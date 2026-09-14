# flow

flow is a platform-agnostic, fast, high-rigor coding harness for AI agents and coding assistants. It turns plain English requests into small verified PRs, designs before it writes, and never ships on "it compiles".

## Directory Structure

```
flow/
├── agents/         # Subagent definitions (e.g. flow-agent, comment-sicko)
├── docs/           # Documentation and guides
│   └── guide/      # 10-chapter guide to flow mode and playbooks
├── skills/         # Modular skills, playbooks, and principles
│   ├── flow/       # Core flow orchestrator, playbooks, and references
│   └── ...         # 55+ specialized skills and principle definitions
└── tests/          # Tests for flow harness utilities
```

## How It Works

1. You give your agent or coding assistant a task with `/flow`.
2. flow matches the task to a playbook (Feature, Bug fix, Perf issue, Prototype, etc.).
3. flow plans the change, invokes workflow skills (such as `architect` or `interrogate`), writes tests first (`tdd`), executes in an isolated worktree, and collects runtime evidence before opening a PR.

## Key Skills

The [skills](skills) directory contains modular instructions:

• [flow](skills/flow/SKILL.md): Central engine that routes requests to playbooks.
• **Planning & Architecture Skills**: [wayfinder](skills/wayfinder/SKILL.md), [grill-me](skills/grill-me/SKILL.md), [to-spec](skills/to-spec/SKILL.md), and [to-questionnaire](skills/to-questionnaire/SKILL.md).
• **Workflow Skills**: [tdd](skills/tdd/SKILL.md), [architect](skills/architect/SKILL.md), [interrogate](skills/interrogate/SKILL.md), [arena](skills/arena/SKILL.md), [swarm](skills/swarm/SKILL.md), and [unslop](skills/unslop/SKILL.md).
• **Investigation & Learning Skills**: [how](skills/how/SKILL.md), [why](skills/why/SKILL.md), [understand](skills/understand/SKILL.md), [learn](skills/learn/SKILL.md), [recall](skills/recall/SKILL.md), and [wait-what](skills/wait-what/SKILL.md).
• **Operations & Governance Skills**: [triage](skills/triage/SKILL.md), [writing-for-agents](skills/writing-for-agents/SKILL.md), [wizard](skills/wizard/SKILL.md), and [no-comments](skills/no-comments/SKILL.md).
• **Verification Skills**: [create-verification-skill](skills/create-verification-skill/SKILL.md) and [maintain-verification-skill](skills/maintain-verification-skill/SKILL.md).
• **23 Principles**: Leaf skills with naming prefix `principle-*` (for example, [principle-fix-root-causes](skills/principle-fix-root-causes/SKILL.md) and [principle-prove-it-works](skills/principle-prove-it-works/SKILL.md)).

## Scripts

The [scripts](skills/flow/scripts) directory contains CLI utilities:

• `watch-pr`: CLI tool to monitor pull requests and triage review feedback.
• `orch`: Orchestration runner and state store.
• `worktree-audit.sh`: Script to inspect and clean git worktrees.

## Acknowledgements

flow builds upon and adapts concepts from two primary foundations:

• **[pstack (`cursor/plugins/pstack`)](https://github.com/cursor/plugins/tree/main/pstack)**: The primary foundation and architecture for flow. pstack introduced the high-rigor autonomous execution paradigm, the playbook system, multi-model panels, verification harnesses, worktree isolation, and the core software design principles.
• **[Matt Pocock's Skills Library (`mattpocock/skills`)](https://github.com/mattpocock/skills)**: The foundation for conversational ideation and structured specification. These include the interactive architectural decision workflows ([`wayfinder`](skills/wayfinder/SKILL.md), [`grill-me`](skills/grill-me/SKILL.md), [`to-spec`](skills/to-spec/SKILL.md), [`to-questionnaire`](skills/to-questionnaire/SKILL.md)), conversational triage and curriculum learning ([`triage`](skills/triage/SKILL.md), [`learn`](skills/learn/SKILL.md)), and agent instruction standards ([`writing-for-agents`](skills/writing-for-agents/SKILL.md)).
