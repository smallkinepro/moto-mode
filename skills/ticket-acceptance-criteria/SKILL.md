---
name: ticket-acceptance-criteria
description: >-
  Make a ticket buildable without follow-up questions: scope in and out,
  observable acceptance checks, dependencies with owners, sequence, and the
  gate skill each role will run. Use when writing or grooming a ticket before
  design or build starts.
license: MIT
metadata:
  phase: "1-intake"
  layer: L1
---
# Ticket acceptance criteria

## A ready ticket has
1. **Goal** in one sentence, in user terms.
2. **Scope.** In and out, explicitly. Out-of-scope ideas become separate tickets.
3. **Acceptance checks.** Observable and binary. Bad: "page is fast". Good: "Lighthouse performance >= 90 on the deploy preview at 390px".
4. **Dependencies.** Copy, assets, access, data, each with an owner.
5. **Sequence.** What this unblocks, and any due date.
6. **Gates.** Which skill each role runs (for example `design-qa`, `build-ship`, `ship-verify`).
7. **Links** to the locked spec and any brand or pricing locks.

## Before marking Ready
- Every acceptance check can be verified by someone other than the builder.
- Money, scope, or customer-facing promise changes go to a human, not into the ticket silently.
