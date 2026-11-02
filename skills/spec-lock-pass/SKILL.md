---
name: spec-lock-pass
description: >-
  Clarity gate for a spec before design or build spends a cycle on it. Checks
  testable requirements, non-goals, locked versus open decisions, failure
  states, and tunable numbers. Use before asking for spec approval or handing
  a spec to design or build.
metadata:
  phase: "1-discovery-and-spec"
  layer: L1
---
# Spec lock pass

## When to use

- A spec draft is ready for owner approval
- Build or design keeps asking "is this decided?"
- A spec changed after it was locked

## Steps

- [ ] **Core behavior:** one sentence on what the user does and why it's valuable
- [ ] **Numbered requirements** (`R1`, `R2`, ...), each observable and testable
- [ ] **Non-goals** listed explicitly
- [ ] **Locks versus open:** every decision is marked locked or open. Open items have an owner and the phase they must close by.
- [ ] **Failure and empty states:** user-facing outcomes for errors, empty data, timeouts, and bad input, not just the happy path
- [ ] **Numbers that change behavior** (limits, timers, thresholds, prices) are named, given a value, and marked tunable or locked
- [ ] **Rules as logic:** behavior rules written as precise conditions, tables, or pseudocode, not prose
- [ ] **Anti-jobs:** what this change must not drag other roles into
- [ ] **Acceptance signals** that map to requirement IDs
- [ ] **Deviations section** for places where the current system differs from the spec
- [ ] **Locks are written in the spec file.** A lock that exists only in chat doesn't count.

## Done means

Design and build can implement without re-asking what's locked, and the owner has approved a specific version (record the date and version in the spec).

## Anti-patterns

- Requirements that describe implementation instead of behavior
- "TBD" without an owner
- Silent edits after the lock. Add a change note instead.
