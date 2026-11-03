# Destructive operations

Before any `rm -rf`, `DROP`, `TRUNCATE`, `git reset --hard`, `git push --force`, migration, or bulk update:

1. **Name the target exactly.** No globs or variables you have not printed first.
2. **Dry run.** List what will be affected (`--dry-run`, `SELECT count(*)` with the same `WHERE`, `git log` of commits to be dropped).
3. **Backup or reversal path.** Snapshot, branch, or export first. Write down how to undo it.
4. **Approval.** Shared branches, production data, or anything outside the workspace need a human yes (see `approval-gates.md`).
5. **Verify after.** Show the post-state matches the intent.

Prefer reversible alternatives: archive over delete, new branch over reset, `--force-with-lease` over `--force`, additive migrations over destructive ones.
