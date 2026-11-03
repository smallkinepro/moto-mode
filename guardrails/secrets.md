# Secrets

- Secrets live in the platform secret store or environment variables. Never in code, config files, fixtures, logs, PR text, issues, or skills.
- `gitleaks` runs on full history in CI. A hit blocks merge; rotate the secret, then clean history. Deleting the line is not enough.
- Never print a secret to verify it. Check length or a hash prefix.
- Denylists of sensitive terms are themselves sensitive: store the pattern list as a CI secret and print "pattern withheld" on hits.
- Agents do not read credential files, browser cookies, or tokens to grant themselves access. Ask for scoped access instead.
- Log redaction is on by default for any tool that supports it.
