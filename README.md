# Personal Development Environment & Agentic Harness

This repository contains my personal configurations, developer tooling, autonomous agent harness definitions, atomic skill libraries, and knowledge management systems. It serves as the unified source of truth for bootstrapping, configuring, and orchestrating my development environments across machines.

---

## Repository Structure

```
dot-files/
├── llm-wiki/               # LLM Wiki methodology, templates & deterministic DAG engine
│   ├── scripts/            # dag.py, sync-workspace.sh
│   ├── templates/          # Schema.org YAML frontmatter templates
│   └── specs/              # System architecture specification
├── docs/specs/             # Core specifications & harness definitions
│   ├── agent-definitions.md# 6-agent role architecture (Ideation, Architect, Worker, etc.)
│   └── skill-library.md    # Reusable atomic skills ledger and principles
└── ...                     # Shell, editor, and system configurations
```

---

## Key Components

### 1. LLM Wiki & Workspace Framework (`llm-wiki/`)
A modular system implementing Andrej Karpathy's LLM Wiki methodology combined with Google's Open Knowledge format (Schema.org / JSON-LD in YAML frontmatter) and Obsidian. 
- **Separation of Concerns:** Project specifications, PRDs, ADRs, and tickets live exclusively in the knowledge vault; code repositories contain only source code and tests.
- **Deterministic DAG Engine (`dag.py`):** Evaluates dependency graphs and task readiness deterministically without fuzzy markdown parsing.
- **Context Synchronization (`sync-workspace.sh`):** Automatically links code repositories to vault project contexts via gitignored symlinks.

### 2. Agent Harness & Role Definitions (`docs/specs/agent-definitions.md`)
Defines the specialized agent roles that form our execution harness:
- **Ideation Agent:** Functional requirement extraction and milestone roadmapping.
- **Primary Architect & Sub-Agents:** Milestone architecture design, seam definitions, and DAG ticket compilation.
- **Worker Agent:** Autonomous parallel execution using a strict TDD loop (`test -> build -> test -> fix`).
- **Advisor Agent:** Over-the-shoulder monitor preventing architectural drift.
- **Review Agent (Critic):** Adversarial gatekeeper reviewing completed PRs against architectural specs.

### 3. Core Skill Library (`docs/specs/skill-library.md`)
Ledger of atomic skills and global behavioral principles (e.g., `principle-guard-the-context-window`, `principle-never-block-on-the-human`, `principle-sequence-verifiable-units`).
