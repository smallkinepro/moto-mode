# Public safety

Run before a repo, site, report, or package goes public. Every item must pass.

## Identity and contact
- [ ] Only the names and links the owner chose to publish appear.
- [ ] No personal email addresses. Commits use the host's noreply address (check `git log --format='%ae' | sort -u`).
- [ ] Images have EXIF stripped.

## Internal details
- [ ] No internal agent or role names, agent ids, or UUIDs from the team's tooling.
- [ ] No private repo names, internal hostnames, local paths, or chat channel names.
- [ ] No employer, client, or customer names, and nothing derived from their work.

## Content
- [ ] No secrets (gitleaks clean on full history).
- [ ] Denylist scan clean (patterns kept in a CI secret).
- [ ] Examples use generic or public data only.
- [ ] Licenses of copied material are compatible and attributed.

## History
- [ ] Fresh history or audited history: every commit passes the checks above, not only the tip.

A human signs off on this checklist and gives the final yes to flip visibility.
