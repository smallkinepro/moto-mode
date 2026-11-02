---
name: oss-scout-gate
description: >-
  Classify an open-source library, tool, or method as adopt, skill, build, or
  skip, with a duplicate check and a license and maintenance review. Use when
  researching prior art or evaluating a new dependency, so the team neither
  adopts duplicates nor misses real leverage.
metadata:
  phase: "1-discovery-and-spec"
  layer: L1
---
# OSS scout gate

## When to use

- Researching prior art for a spec
- Someone proposes a new dependency or tool
- A periodic scan of upstream releases

## Steps

For each candidate:

- [ ] **Map to a real need:** a current spec, ticket, or recurring pain. No need means skip or park.
- [ ] **Duplicate check:** search existing dependencies, scripts, and skills first
- [ ] **License:** permissive (MIT, Apache-2.0, BSD) is fine. Copyleft or unclear licenses get escalated.
- [ ] **Health:** last release, open security issues, maintainer activity
- [ ] **Security:** reject anything that sends data or credentials somewhere unexpected, or has unexplained network access
- [ ] **Classify:**
  - **Adopt:** take the library or tool, and note the effort and migration
  - **Skill:** it's really a reusable procedure, so write or update a skill
  - **Build:** small and core enough to own
  - **Skip:** a duplicate, the wrong layer, unmaintained, or risky
- [ ] **Scope the adoption:** dev-only or production, and what changes and what doesn't

## Output format

| Candidate | Class | Why (one line) | License | Last release | Effort |
|---|---|---|---|---|---|

## Done means

A short digest the owner can approve line by line. Adoptions become tickets. The scout doesn't assign or start the build.

## Anti-patterns

- Adopting because it's popular, without a mapped need
- Shipping a second tool that does what an existing script already does
