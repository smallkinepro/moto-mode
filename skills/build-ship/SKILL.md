---
name: build-ship
description: >-
  Builder's checklist for implementing a ticket and handing it to review:
  scoped diff, build, lint, and tests green, tests that fail without the
  change, a real behavior check, a secret scan, and an honest completion note.
  Use for any code change before opening or updating a PR.
metadata:
  phase: "4-build"
  layer: L0
---
# Build ship

## When to use

Every code change, before it goes to review.

## Steps

- [ ] Read the ticket, its spec requirements, and the relevant ADRs before editing
- [ ] Reproduce the bug or confirm the current behavior
- [ ] Make the **smallest change** that meets the acceptance checks, with no drive-by refactors or redesigns
- [ ] Add or update tests, and confirm at least once that they **fail without the change**
- [ ] Run `<build command>`, `<lint command>`, and `<test command>`, and record the exact commands and results
- [ ] **Behavior check:** exercise the changed path yourself (run the flow, click the button, call the endpoint). A passing build is not behavior.
- [ ] For UI: check desktop and narrow widths, and take screenshots of the changed screens
- [ ] For state or schema changes: plan a migration so existing users' data or saves keep working
- [ ] **Secret scan:** no credentials, tokens, or personal data in the diff, logs, or fixtures
- [ ] **Scope check:** the diff contains only ticket scope, and follow-ups are filed as new tickets
- [ ] Write the completion note (below)

## Completion note

```markdown
**Ticket:** <link>
**Change:** <one paragraph>
**Evidence:** <commands and results, screenshots, test names>
**Acceptance checks:** <each ticked with evidence>
**Not done / known gaps:** <honest list, or "none">
**Follow-ups filed:** <links>
```

## Done means

A reviewer can confirm every claim from the note without rerunning anything. Shipping to an environment also requires [`ship-verify`](../ship-verify/SKILL.md).

## Anti-patterns

- Marking done after checking localhost only, when the ticket targets a deployed environment
- Calling something "fixed" when it's partly fixed
- Changing production config, domains, or data without an explicit ask
