# Build

**Owner:** builder. **Gate:** `build-ship`.

1. Branch from the latest main. Confirm the baseline build and tests are green.
2. Implement the smallest change that meets the acceptance checks.
3. Add tests that fail without the change.
4. Run build, lint, tests, and the secret scan locally.
5. Run `build-ship`. Open the PR with what, why, how verified, risks.
6. Hand off to the reviewer with the SHA and the gate output.

Scope creep goes into follow-up tickets, not this PR.
