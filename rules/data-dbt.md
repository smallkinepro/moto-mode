---
description: Rules for SQL, dbt models, ingest, and analytics work
globs: ["**/*.sql", "models/**", "dbt_project.yml", "**/*.yml"]
alwaysApply: false
---
# Data and dbt rules

## Sources
- Run `data-ingest-gate` before loading any new source: public or licensed, terms checked, no personal data, provenance recorded.
- Every load writes source URL, pulled-at time, row count, and a content hash or etag.
- Raw data is immutable. Fix it in staging models, never by editing the landed file.

## Modeling
- Layers: `staging` (rename, cast, 1:1 with source) -> `intermediate` (joins, logic) -> `marts` (business grain, what reports read).
- Every model states its grain in the description and has a `unique` + `not_null` test on that grain.
- No `select *` past staging. Name columns explicitly.
- Incremental models need a documented full-refresh path and a test that catches duplicates.
- Pin the warehouse engine and client versions; a client major bump is its own PR with the warehouse compatibility checked.

## Verification
- `dbt build` green on the intended target, not only on a local dev target.
- Smoke checks after build: row counts within an expected band, max date fresh, no unexpected nulls in keys.
- Run `pipeline-ship` before calling a refresh green.

## Operations
- No new schedules or cron refreshes without approval (`guardrails/approval-gates.md`). On-demand first.
- Credentials come from environment variables or a secret store. Never print connection strings.
- Cost: dev runs use sampled or limited data; document any full scan that costs money.

## Reporting
- Reports read only from marts. Run `report-publish-bar` before anything goes on a public URL.
- Describe anomalies as questions to investigate, never as accusations about a named party.
