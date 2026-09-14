# Understand the code before changing it

Editing code you don't understand is how subtle regressions ship. flow gives you four ways in. `/how` explains what the code does now. `/why` digs up the reasons it's shaped that way. `/understand` blends both into one explanation. `/recall` rebuilds your own recent context on a topic.

![A detective studies a machine blueprint with a magnifying glass while robots fetch case files; the evidence board behind her links clues under /how and /why.](./images/understanding.jpg)

## Trace behavior with `/how`

```text
/how do we dedupe notifications? is there an n+1 when we look up subscribers?
```

Ask the question you actually have. [`/how`](../../skills/how/SKILL.md) reads the code and answers at the level of a senior engineer onboarding you onto the subsystem, with the runtime flow, the key types, and the non-obvious parts. For a big subsystem it fans out two to four read-only explorers first. For a narrow question it just reads and explains.

## Dig up history with `/why`

```text
/why was the retry limit set to five? does the reason still hold?
```

[`/why`](../../skills/why/SKILL.md) works like a detective on a cold case. It starts from source control, then queries whatever evidence categories your MCPs expose, such as the issue tracker, long-form docs, team chat, observability, error tracking, and analytics, all in parallel. The report cites everything, separates direct evidence from inference, and says "appears to" when the record is thin. A null result gets reported too, because "nobody wrote down why" is itself an answer.

The two compose naturally. `do why first then how` is a perfectly good prompt when you suspect the history explains the mess.

## Actually understand it with `/understand`

```text
/understand how this PR changes retries. convince me it fixes the cause and not the symptom.
```

[`/understand`](../../skills/understand/SKILL.md) is for when a summary isn't enough. It runs `/how` and `/why`, for a small change maybe just one of them, and weaves the findings into a plain explanation that builds up diagram by diagram. The "convince me" framing is worth stealing. It turns the explanation into an argument you can poke at instead of a tour.

## Rebuild your own context with `/recall`

```text
/recall catch me up on the export work from last week
```

[`/recall`](../../skills/recall/SKILL.md) mines your own recent chats plus the shared record (issues, prior fixes, errors still firing) and hands back a brief on where things stand and what's next. Use it when you're returning to a topic cold. If you want to resume one specific chat, that's the Session pickup playbook below, not `/recall`.

## Take over prior work with Session pickup

When another agent (or you, last week) left a branch mid-flight:

```text
/flow pick up branch tonoy/fix-auth-tokens
```

Match it to the Session pickup playbook (`playbooks/session-pickup.md`). It audits the diff against main, reads git log, runs the test suite to verify current state, reconstructs the plan, and resumes execution without re-doing completed work.
