---
description: Rules for application and game code changes
globs: ["**/*.{ts,tsx,js,jsx,py,rs,go}", "Cargo.toml", "package.json"]
alwaysApply: false
---
# Software rules

## Before writing code
- Read the spec and its acceptance checks. If they are not testable, stop and send it back through `spec-lock-pass`.
- Run the existing build and tests first so you know the baseline is green.
- Check for an existing library or helper before writing one (`oss-scout-gate` for new dependencies).

## While writing
- Pin toolchains and dependencies (exact versions for anything with a fast-moving API). Bump deliberately, in its own PR.
- Keep tunable numbers in data files (RON, TOML, JSON), not in code.
- Validate input at boundaries; trust types inside. No silent catch-all error handling.
- No dead code, commented-out blocks, or TODOs without an owner.
- Comments explain why, not what.

## Tests
- Every behavior change gets a test that fails without the change.
- Test observable behavior, not private implementation.
- Deterministic tests only: fixed seeds, fixed clocks, no network in unit tests.
- Headless or simulation modes are first-class: if a feature cannot be checked without a screen, add a headless path.

## CI
- CI is the source of truth; "works on my machine" is not a pass.
- Every job and long step has a timeout.
- Cache by a single shared key saved by one job; record warm vs cold wall time.
- A required check that is flaky is a bug to fix, not a check to skip.

## PRs
- One concern per PR. Title says the behavior change.
- Body: what, why, how verified (commands + output), risks, follow-ups.
- Run `build-ship` before opening; a separate reviewer runs the specialty verify skill.
