---
name: code-review-checklist
description: >-
  Independent review of a pull request against its spec: re-run checks on the
  exact SHA, walk acceptance checks with evidence, and inspect correctness,
  tests, security, scope, and docs. Use when reviewing any code change written
  by someone else, human or agent.
license: MIT
metadata:
  phase: "5-verify"
  layer: L0
---
# Code review checklist

You did not write this change. Do not fix it; report.

## Setup
1. Check out the exact head SHA. Confirm CI is green on that SHA.
2. Re-run build and tests locally. Quote the result.

## Spec
3. Walk each acceptance check: pass or fail with evidence.
4. Flag anything in the diff the spec didn't ask for.

## Correctness
5. Edge cases: empty, null, max size, concurrency, time zones, retries.
6. Errors are handled at boundaries and not swallowed.
7. New tests fail without the change (revert the source, run the test).

## Security and safety
8. No secrets, no new unvetted dependencies, input validated, no injection paths.
9. Destructive operations follow `guardrails/destructive-ops.md`.

## Maintainability
10. Names say what things are. No dead code or stray debug output.
11. Docs and config updated in the same PR.

## Verdict
Approve, or request changes with each failing item quoted with file and line. A second failure of the same class goes to `skill-evolution-after-failure`.
