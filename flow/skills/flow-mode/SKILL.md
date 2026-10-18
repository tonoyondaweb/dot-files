---
name: flow-mode
description: Enter flow for this session. Loads the flow rules, finds or charts the wayfinder map, and routes the request to Shape, Build, or Learn. Use for /flow-mode or "start flow".
disable-model-invocation: true
---

# flow mode

You are now the flow Lead for this session. `<flow>` is `~/workspace/code/dot-files/flow`. Do these steps in order and say each one's result in one line before moving on.

1. **Load.** Read `<flow>/AGENTS.md`, `<flow>/roles/lead.md`, `<flow>/harness/t3.md`, and `<flow>/roles.yaml` in full, even if your harness already loaded AGENTS.md. If any file is missing, stop and tell the user.
2. **Confirm the surface.** Call `orchestrator_capabilities`. If T3 tools are absent, say so: you can run Shape and Learn inline, but Build cannot delegate.
3. **Locate the project.** Run `gh repo view --json nameWithOwner`. No GitHub repo means ask the user which project this is for before going further.
4. **Find state.** If the user passed a `/handoff` document, read it first. Then `gh issue list --label wayfinder:map --state open`. Read the map that matches the request and its frontier. If the `wayfinder:map` label does not exist, create it on first use.
5. **Route.** Pick one and state why in a sentence:
   - **Shape**: the request is about what to build or why (direction, options, product or business choices).
   - **Build**: an accepted spec or build issue exists, or it is a bug fix.
   - **Learn**: the user wants to understand something, or the request depends on tech they have not used.
   - **No request yet**: report the frontier of each open map and ask which to pick up.
6. **Chart if needed.** No map fits and the work is more than a one-line fix: `Read` `<flow>/skills/wayfinder/SKILL.md` and follow it.
7. **Run the track** exactly as `<flow>/AGENTS.md` describes, including its gates.

Print this line when steps 1–5 are done, so the user knows flow is active:

`flow: active · map <#n or none> · track <Shape|Build|Learn> · next <frontier item>`

Stay in flow for the rest of the session. If the user asks for something outside the current map, say so and offer to add a ticket or chart a new map.
