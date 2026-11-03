# rules

`rules/*.md` are the source of truth. Each file carries Cursor-style frontmatter (`description`, `globs`, `alwaysApply`) so it can be rendered to other agents without editing.

| File | Applies to | alwaysApply |
|---|---|---|
| `_global.md` | everything | true |
| `software.md` | application and game code | false (globs) |
| `data-dbt.md` | SQL, dbt, pipelines | false (globs) |
| `docs.md` | Markdown | false (globs) |

## Rendering

`python3 scripts/render_rules.py` generates:
- `.cursor/rules/<name>.mdc`: the same rule, frontmatter kept (`globs` written in Cursor's comma-separated form).
- `CLAUDE.md`: `@rules/<name>.md` imports for Claude Code.
- `AGENTS.md` stays hand-written and links here, which covers Codex and other AGENTS.md readers.

Edit `rules/*.md`, then re-run the script. CI runs `python3 scripts/render_rules.py --check` and fails if the generated files are stale.
