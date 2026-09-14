---
name: to-spec
description: "Turn the current conversation and resolved decisions into a technical specification and publish it: no interview, just synthesis of what you've already discussed."
disable-model-invocation: true
---

This skill takes the current conversation context, resolved decision issues, and codebase understanding and produces a specification. Do NOT interview the user; just synthesize what you already know.

## Process

1. Explore the repo to understand the current state of the codebase if you haven't already. Use the `understand` skill if needed. Respect any ADRs in the area you are touching.

2. Sketch out the seams at which the feature will be tested. Existing seams should be preferred to new ones. Use the highest seam possible. The fewer seams across the codebase, the better.

3. Write the spec using the template below. Save it to `docs/specs/<feature-slug>.md` and link/post it to the parent GitHub initiative issue using `gh issue comment`.

4. Once drafted, run the multi-model **interrogate** skill against the draft specification to surface hidden assumptions, unhandled failures, and boundary leaks. Present findings to the user for final approval and lock before execution starts.

<spec-template>

## Problem Statement

The problem that the user is facing, from the user's perspective.

## Solution

The solution to the problem, from the user's perspective.

## User Stories

A numbered list of user stories. Each user story should be in the format of:

1. As an <actor>, I want a <feature>, so that <benefit>

This list of user stories should be extensive and cover all aspects of the feature.

## Implementation Decisions

A list of implementation decisions that were made. This can include:

- The modules that will be built/modified
- The interfaces of those modules that will be modified
- Technical clarifications from the developer
- Architectural decisions and ADR links
- Schema changes
- API contracts
- Specific interactions

Do NOT include specific file paths or volatile code snippets. They may end up being outdated very quickly.

Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it within the relevant decision and note briefly that it came from a prototype.

## Testing Decisions

A list of testing decisions that were made. Include:

- A description of what makes a good test (only test external behavior, not implementation details per `principle-test-behavior-not-implementation`)
- Which modules will be tested
- Verification criteria for unit, live runtime, and performance checks

## Out of Scope

A description of the things that are out of scope for this spec.

## Further Notes

Any further notes about the feature.

</spec-template>
