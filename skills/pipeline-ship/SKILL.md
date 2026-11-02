---
name: pipeline-ship
description: >-
  Ship checklist for a data pipeline or transformation project: build green on
  the intended target, tests on model grains, freshness, row-count and
  max-date smoke checks, no secrets in logs, and no unapproved schedules. Use
  after models change or before a refresh is called green.
metadata:
  phase: "4-build"
  layer: L1
---
# Pipeline ship

## When to use

- Transformation models changed (SQL models, dataframes, dbt-style projects)
- Before a manual or scheduled refresh is reported as green

## Steps

- [ ] Install dependencies, then run the full build (models and tests) against the **intended target** (local for CI, the real warehouse for production)
- [ ] Sources are declared, with freshness expectations where it matters
- [ ] Tests cover **primary-key uniqueness and not-null on every published model's grain** at minimum
- [ ] Relationship and accepted-value tests on the key dimensions
- [ ] **Smoke:** query row counts and the max snapshot or event date for the published models, and record them in a run audit
- [ ] Compare counts with the previous run, and flag swings over a threshold (for example ±20%)
- [ ] Memory and runtime are within limits on the target machine. A full rebuild must finish, not just incremental runs.
- [ ] No secrets in stdout, artifacts, or committed profiles
- [ ] **Schedules:** don't add or claim a recurring schedule unless the owner approved it
- [ ] If anything deploys through CI, also run [`ship-verify`](../ship-verify/SKILL.md)

## Fail closed

A red build, missing tests on published models, a missing smoke check, or an unapproved schedule means it's not done.

## Done means

Build and tests are green on the intended target, the smoke numbers are recorded, and the completion note lists them.

## Anti-patterns

- Reporting "pipeline green" from a partial or incremental run
- Charts or reports reading raw tables instead of tested models
