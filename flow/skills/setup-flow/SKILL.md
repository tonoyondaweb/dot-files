---
name: setup-flow
description: Configure which models flow uses per role and at what reasoning budget. Detects your available models and writes a platform-agnostic configuration that overrides skill defaults. Use for /setup-flow, "configure flow models", "flow budget", or changing flow model choices.
---

# Setup flow

Configure model assignments for flow per role.
Writes `~/.config/flow/models.yaml` (or project-local `.flow/models.yaml`), and optionally `~/.cursor/rules/flow-models.mdc` when running inside Cursor.

## Steps

### 1. Detect available models

Enumerate the model slugs you can pass to subagents or tasks in this session. That is the dependable source. If the environment or CLI lists entitled models, prefer it for completeness. If you cannot detect any, ask the user to paste the slugs they have access to. Never write a real slug you have not confirmed is available. The aliases `inherit-parent` and `auto` are always valid even though they are not detected slugs.

### 2. Load current state

The default role-to-model mapping is shown in step 5 below. Search for existing configuration in this precedence:
1. Path in `$FLOW_MODELS_PATH` environment variable (if set)
2. Project-local `.flow/models.yaml`
3. User configuration `~/.config/flow/models.yaml` (or `~/.flow/models.yaml`)
4. Legacy/Cursor rule `~/.cursor/rules/flow-models.mdc` (or `~/.cursor/rules/pstack-models.mdc`)

If an existing configuration exists, read it and treat its `budget` line and its role values as the current choices. Otherwise start from the defaults.

### 3. Budget, map, and confirm

**(a) Ask for a budget.** Prefer AskQuestion or multiple choice options. Offer these four options with these exact labels, and name the current budget when configuration records one:

- `unlimited — keep max`
- `large — xhigh reasoning`
- `medium — high reasoning`
- `small — medium reasoning`

**(b) Apply it.** Build the working table from the skill defaults, and on a re-run keep any role you changed by family, list, or alias (`inherit-parent`, `auto`). `unlimited` leaves every effort as in that table. `large`, `medium`, and `small` set the effort token of every real slug, panel entries included, to `xhigh`, `high`, or `medium`. The effort token is the last token, or the one before a trailing `fast`, on the ladder `max` > `xhigh` > `high` > `medium` > `low`. If the result is not a detected slug, use the same family's detected slug with the highest effort at or below the target, else mark the role as needing a choice. `inherit-parent` and `auto` do not change. So `small` turns `claude-fable-5-1-thinking-max` into `claude-fable-5-1-thinking-medium`, and `grok-4.6-fast-xhigh` into `grok-4.6-medium-fast` when only that form is detected.

**(c) Show the roles and confirm.** Show every role with its model, marking any real slug not in the detected set as needing a choice. Ask whether to accept as-is or change specific roles, offering the detected models plus `inherit-parent` and `auto` (both mean: this role runs on the parent model) as the options. Prefer structured questions over free text. For panel roles (arena runners, architect runners, interrogate reviewers) the value is a list, and one subagent runs per entry, alias entries included, so the list length sets the count. `arena cross-judge pool` is also a list, but Arena selects one value from it whose model family differs from the parent's when possible. `swarm workers` is the default model for every worker unless a race or comparison assigns another model per arm.

### 4. Validate

Every real slug written must be in the detected set. `inherit-parent` and `auto` always pass. If a chosen real slug is not available, stop and ask again.

### 5. Write the configuration

Write the configuration to `~/.config/flow/models.yaml` (or project `.flow/models.yaml`).

```yaml
# flow model configuration. One entry per role. Delete a key to fall back to the skill default.
# `inherit-parent` or `auto` as a value: the role runs on the parent agent model.
budget: unlimited # max

models:
  feature: grok-4.6-fast-xhigh
  refactoring: grok-4.6-fast-xhigh
  bug-fix: grok-4.6-fast-xhigh
  perf-issue: grok-4.6-fast-xhigh
  hillclimb: grok-4.6-fast-xhigh
  judgment_and_prose: claude-fable-5-1-thinking-max
  hardest_tasks: claude-fable-5-1-thinking-max
  how_explorer: grok-4.6-fast-xhigh
  how_explainer: claude-fable-5-1-thinking-max
  why_investigators: grok-4.6-fast-xhigh
  why_synthesizer: claude-fable-5-1-thinking-max
  reflect_tooling: gpt-5.6-sol-max
  reflect_judgment_divergent_synthesizer: claude-fable-5-1-thinking-max
  arena_runners:
    - claude-fable-5-1-thinking-max
    - gpt-5.6-sol-max
    - grok-4.6-fast-xhigh
    - claude-opus-5-thinking-xhigh
  arena_cross_judge_pool:
    - claude-fable-5-1-thinking-max
    - gpt-5.6-sol-max
    - grok-4.6-fast-xhigh
    - claude-opus-5-thinking-xhigh
  swarm_workers:
    - grok-4.6-fast-xhigh
  architect_runners:
    - claude-fable-5-1-thinking-max
    - gpt-5.6-sol-max
    - grok-4.6-fast-xhigh
    - claude-opus-5-thinking-xhigh
  interrogate_reviewers:
    - claude-fable-5-1-thinking-max
    - gpt-5.6-sol-max
    - grok-4.6-fast-xhigh
    - claude-opus-5-thinking-xhigh
```

If operating inside Cursor or when Cursor rule compatibility is desired, also write `~/.cursor/rules/flow-models.mdc` with `alwaysApply: true`.

### 6. Confirm

Tell the user the configuration was written and that it applies to new sessions. Re-running this skill updates it.

### 7. Offer a verification skill (optional)

Check whether the project has a way to drive the real app for proof (a `verify-*` skill in `.agents/skills/`, or an existing harness). If not, offer once: "want a project-local verification skill, so agents can drive the app the way a user does and prove changes work? I can generate one with /create-verification-skill." On yes, invoke `/create-verification-skill` (resolves wherever flow is installed: workspace, user, or plugin). On no, move on without pushing.
