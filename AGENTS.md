# AGENTS.md

## Repo layout

- `rules/` global and domain rules
- `skills/<slug>/SKILL.md` skills (`name` must equal folder)
- `workflows/`, `guardrails/`, `seats/`

## Checks

Run `python3 scripts/validate.py` before pushing.
Edit `rules/*.md` only, then run `python3 scripts/render_rules.py` to regenerate `.cursor/rules/*.mdc` and `CLAUDE.md`.
Run `python3 scripts/smoke_install.py all` to smoke-test the Cursor, Claude Code, and Codex installs.
