---
name: setup-flow
description: Configure which model and effort each flow role uses. Reads the live T3 catalog and writes roles.yaml. Use for /setup-flow, "configure flow models", "flow budget", or changing a role's model.
disable-model-invocation: true
---

# Setup flow

Write the per-role model registry every flow skill reads. Ask whether it is global (`<flow>/roles.yaml`) or for this project (`.flow/roles.yaml` in the repo root). A project file wins over the global one.

1. **Detect.** Call `orchestrator_capabilities`. Keep only providers with `canRunChildTask: true`. The usable targets are each provider's `providerInstanceId/model` plus its effort options. Never write a target you have not seen there. `inherit-parent` is always valid: the role runs on the Lead's own model, so `delegate_task` omits `target`.
2. **Load.** Read the current `roles.yaml` if it exists. Treat its `budget` key and role entries as current. Drop entries for roles that no longer exist and list them.
3. **Budget.** Ask with `AskUserQuestion`: `small (low)` (default), `medium (medium)`, `large (high)`, `unlimited (max)`. Budget also sets the in-flight cap in `<flow>/harness/t3.md`. Pick targets from the two rosters: big (Opus 5.5, GLM-5.3) for lead, hardest-tasks, adversary, review, and judges; small (DeepSeek V4.1 Flash, GLM-5.3-Flash, Sonnet 5.5) for worker, explorer, researcher, verifier, and arena-runners. Apply the budget to every target's effort, panel entries included, using the nearest rung at or below the target the model offers. Antigravity slugs change suffix instead (`gemini-3.8-flash-high`). Keep roles the user pinned by hand.
4. **Confirm.** Show every role with its target. Mark anything not in the catalog as needing a choice. Ask whether to accept or change specific roles.
5. **Validate.** Every target must be in the detected set. Smoke-test each distinct target with one `delegate_task` (`mode: "wait"`, a one-line task: reply with your model name). A rejected target goes back to step 4.
6. **Write.** Overwrite the chosen file in full so reruns stay idempotent. Commit the global one to `dot-files`, a project one to that project.
