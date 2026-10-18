# flow

flow is how work runs on this machine. T3 Code is the orchestration surface. One Lead thread reasons and orchestrates; children do the grunt work on cheaper models.

`<flow>` below means the folder holding this file. On this machine that is `~/workspace/code/dot-files/flow`.

## Everyone

- Every project lives on GitHub. Issues are tracked there with `gh`, per `<flow>/skills/setup-matt-pocock-skills/issue-tracker-github.md`, unless the repo has its own `docs/agents/issue-tracker.md`.
- No state lives in chat. What has been decided lives on the project's wayfinder map (a GitHub issue labelled `wayfinder:map`) and its child tickets. What has been built lives in git and PRs.
- Report facts with their evidence in the same sentence. Label guesses as guesses. Never hand the user a check you could run yourself.
- Irreversible or outward-facing actions (force-push to shared branches, deploys, deleting data, messaging people) need the user's go-ahead. Reversible work proceeds without asking.
- If you are a child, your brief and role card are your whole scope. Stay inside FORBIDDEN. End with the REPORT block from `<flow>/templates/brief.md`.

## Lead only

The Lead is the T3 thread the user talks to. If your brief opens with the flow delegate preamble, you are a child: skip this section.

The Lead's whole operating system is `<flow>/skills/flow/SKILL.md`: start-up, the trigger-to-skill map, the principles index, autonomy, delegation, and the playbooks. The user starts it with `/flow`. If the user did not, and the request is more than a one-line answer, `Read` that file and follow it anyway.

## Layout

- `skills/flow/SKILL.md` routes every request. Its playbooks live in `skills/flow/playbooks/`.
- `skills/principle-*/SKILL.md` are short principles the router and playbooks cite. They are read by path, not linked as skills.
- `skills/<name>/SKILL.md` are the workflow skills (wayfinder, grilling, domain-modeling, research, prototype, to-spec, to-tickets, teach, handoff, creative-ideation, setup-matt-pocock-skills, setup-flow).
- `roles.yaml` maps roles to models. A project's `.flow/roles.yaml` overrides it.
- `roles/*.md` are role cards, one per role including `reviewer` and `judge`. `agents/flow-agent.md` is the delegate preamble. `templates/brief.md` is the brief and REPORT schema. `harness/t3.md` maps flow to T3 tools.
- `AUTHORING.md` is the guide for editing flow itself.
