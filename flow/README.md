# Flow Framework

This directory contains the Flow framework for autonomous AI coding agents.

Flow gives agents structured playbooks, modular skills, and engineering principles.

## Structure

```
flow/
├── agents/    # Agent personality and configuration files
├── docs/      # Guides and instructional documents
└── skills/    # Reusable skill folders, playbooks, and scripts
```

## Agents

The [agents](file:///Users/tonoy/workspace/dot-files/flow/agents) directory defines agent roles:

• [flow-agent.md](file:///Users/tonoy/workspace/dot-files/flow/agents/flow-agent.md): Main Flow subagent. It routes tasks through playbooks and follows strict verification standards.
• [comment-sicko.md](file:///Users/tonoy/workspace/dot-files/flow/agents/comment-sicko.md): Specialized reviewer that deletes unnecessary code comments.

## Documentation

The [docs/guide](file:///Users/tonoy/workspace/dot-files/flow/docs/guide) directory contains a complete guide for the framework:

• [README.md](file:///Users/tonoy/workspace/dot-files/flow/docs/guide/README.md): Overview and table of contents.
• [01-setup.md](file:///Users/tonoy/workspace/dot-files/flow/docs/guide/01-setup.md): Installation and model selection.
• [02-flow.md](file:///Users/tonoy/workspace/dot-files/flow/docs/guide/02-flow.md): Task routing and goal specification.
• [03-understand.md](file:///Users/tonoy/workspace/dot-files/flow/docs/guide/03-understand.md): Investigation before editing code.
• [04-design.md](file:///Users/tonoy/workspace/dot-files/flow/docs/guide/04-design.md): Architecture exploration and multi-model reviews.
• [05-build-and-clean.md](file:///Users/tonoy/workspace/dot-files/flow/docs/guide/05-build-and-clean.md): Test-driven development and code cleanup.
• [06-verify-and-ship.md](file:///Users/tonoy/workspace/dot-files/flow/docs/guide/06-verify-and-ship.md): Real application verification and pull requests.
• [07-overnight.md](file:///Users/tonoy/workspace/dot-files/flow/docs/guide/07-overnight.md): Long autonomous sessions and decision logs.
• [08-principles.md](file:///Users/tonoy/workspace/dot-files/flow/docs/guide/08-principles.md): Principle names to guide agents.
• [09-make-it-yours.md](file:///Users/tonoy/workspace/dot-files/flow/docs/guide/09-make-it-yours.md): Customization and skill testing.
• [10-recipes-and-pitfalls.md](file:///Users/tonoy/workspace/dot-files/flow/docs/guide/10-recipes-and-pitfalls.md): Prompt examples and common errors.

## Skills

The [skills](file:///Users/tonoy/workspace/dot-files/flow/skills) directory contains modular instructions:

• [flow](file:///Users/tonoy/workspace/dot-files/flow/skills/flow/SKILL.md): Central engine that routes requests to playbooks.
• **Workflow Skills**: [tdd](file:///Users/tonoy/workspace/dot-files/flow/skills/tdd/SKILL.md), [architect](file:///Users/tonoy/workspace/dot-files/flow/skills/architect/SKILL.md), [interrogate](file:///Users/tonoy/workspace/dot-files/flow/skills/interrogate/SKILL.md), [arena](file:///Users/tonoy/workspace/dot-files/flow/skills/arena/SKILL.md), [swarm](file:///Users/tonoy/workspace/dot-files/flow/skills/swarm/SKILL.md), and [unslop](file:///Users/tonoy/workspace/dot-files/flow/skills/unslop/SKILL.md).
• **Investigation Skills**: [how](file:///Users/tonoy/workspace/dot-files/flow/skills/how/SKILL.md), [why](file:///Users/tonoy/workspace/dot-files/flow/skills/why/SKILL.md), [teach](file:///Users/tonoy/workspace/dot-files/flow/skills/teach/SKILL.md), and [recall](file:///Users/tonoy/workspace/dot-files/flow/skills/recall/SKILL.md).
• **Verification Skills**: [create-verification-skill](file:///Users/tonoy/workspace/dot-files/flow/skills/create-verification-skill/SKILL.md) and [maintain-verification-skill](file:///Users/tonoy/workspace/dot-files/flow/skills/maintain-verification-skill/SKILL.md).
• **23 Principles**: Leaf skills with naming prefix `principle-*` (for example, [principle-fix-root-causes](file:///Users/tonoy/workspace/dot-files/flow/skills/principle-fix-root-causes/SKILL.md) and [principle-prove-it-works](file:///Users/tonoy/workspace/dot-files/flow/skills/principle-prove-it-works/SKILL.md)).

## Scripts

The [scripts](file:///Users/tonoy/workspace/dot-files/flow/skills/flow/scripts) directory contains CLI utilities:

• `watch-pr`: CLI tool to monitor pull requests and triage review feedback.
• `orch`: Orchestration runner and state store.
• `worktree-audit.sh`: Script to inspect and clean git worktrees.
