---
name: report-publish-bar
description: >-
  Bar for publishing an analytics report or dashboard: reads only from tested
  marts, builds and deploys cleanly, frames anomalies as questions not
  accusations, states scope and sources, and leaks no personal or internal
  details. Use before any report or dashboard goes on a shared or public URL.
license: MIT
metadata:
  phase: "6-ship"
  layer: L1
---
# Report publish bar

## Data
1. Every chart and table binds to a dbt mart or approved export, never a raw file.
2. Upstream `pipeline-ship` passed on the same data snapshot.

## Build and deploy
3. The report build succeeds in CI.
4. The deploy URL returns 200 and key pages render real numbers (check after client-side rendering, not just the server stub).

## Framing
5. Anomalies are leads to investigate, never claims of wrongdoing about a named party.
6. The page states the data domain, the sources with attribution, the snapshot date, and known limits.

## Privacy and hygiene
7. No secrets, tokens, internal tool names, local paths, or handoff notes on the page or in its metadata.
8. No personal data and no names of people the report does not intend to publish.
9. Grep the built output for the team's denylist before deploy.

## Fail closed
Empty marts, broken deploy, accusatory framing, missing scope, or any leak: do not publish. Pair with `ship-verify` for the deploy itself.
