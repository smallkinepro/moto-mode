# AGENTS.md

Entry point for any coding agent working in a repo that uses this stack. Read this first, then the rule file for your kind of work.

## Team model

Work moves through one owner per stage. Each role is a template in [`seats/`](seats/).

| Role | Owns | Never does |
|---|---|---|
| Chief of staff | Intake, priorities, assignment, approvals routing | Writes production code |
| Designer / researcher | Specs, prior-art scouting, rules, skills, docs | Merges or deploys |
| Builder | Code changes, tests, PRs | Changes scope without a spec update |
| Data engineer | Ingest, models, pipeline tests | Publishes reports without the report bar |
| Reviewer | Independent verification against the spec | Fixes the code it is reviewing |

One job per role. When a task needs two roles, it is two tasks.

## Gates

Nothing is "done" until its gate passes with evidence (command, commit SHA, output). See [`workflows/`](workflows/).

1. **Spec lock** — `skills/spec-lock-pass` before build starts.
2. **Build** — `skills/build-ship` before a PR is opened.
3. **Verify** — the specialty verify skill (`native-game-headless-verify`, `pipeline-ship`, `design-qa`, ...) plus an independent review.
4. **Ship** — `skills/ship-verify` before anyone says "live" or "merged".
5. **Retro** — `skills/skill-evolution-after-failure` after any correction or failed gate.

Human approval is required for the actions in [`guardrails/approval-gates.md`](guardrails/approval-gates.md). An agent asks; it does not assume.

## Where things live

```
AGENTS.md            this file
rules/               always-on rules: _global + software, data-dbt, docs
workflows/           intake -> spec-lock -> build -> verify -> ship -> retro
guardrails/          approvals, secrets, destructive ops, public safety, cost
skills/<slug>/       Agent Skills (SKILL.md), name == folder
seats/               role templates
scripts/             validate.py (structure), render_rules.py (rules -> .cursor/rules, CLAUDE.md),
                     smoke_install.py (Cursor, Claude Code, Codex install smoke tests)
```

## Rules to load

- Always: [`rules/_global.md`](rules/_global.md)
- Application code: [`rules/software.md`](rules/software.md)
- SQL, dbt, pipelines: [`rules/data-dbt.md`](rules/data-dbt.md)
- READMEs, specs, user-facing text: [`rules/docs.md`](rules/docs.md)
