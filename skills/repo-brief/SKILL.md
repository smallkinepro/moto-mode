---
name: repo-brief
description: >-
  Produce a compact, secret-free snapshot of a repository (structure, entry
  points, build and test commands, conventions) so another agent can review or
  change it without reading everything. Use before handing an unfamiliar
  codebase to a builder, reviewer, or researcher.
metadata:
  phase: "1-discovery-and-spec"
  layer: L1
---
# Repo brief

## When to use

- An agent is about to work in a repo it hasn't seen
- A reviewer needs context without the builder's whole history

## Steps

- [ ] **Exclude secrets first:** `.env*`, key files, credential configs, and anything in `.gitignore`
- [ ] Generate a packed snapshot with an ignore-aware repo packer if one is available (for example `npx repomix@latest`), or write the brief by hand:
  - [ ] Purpose (from the README, in one paragraph)
  - [ ] Directory tree, two levels deep, with generated and vendor folders excluded
  - [ ] Entry points and main modules
  - [ ] Build, test, lint, and run commands
  - [ ] Conventions: language versions, formatting, branching, commit style
  - [ ] Where config, data, and docs live
  - [ ] Known gotchas from the README, CONTRIBUTING, or ADRs
- [ ] If the pack is huge, fall back to the README, the manifest files, and the tree
- [ ] Hand off the file path plus a one-paragraph intent (what to look for or change). Don't paste huge packs into chat.

## Done means

The receiving agent can find the right files and run the build without exploring blind, and no secrets are in the brief.

## Anti-patterns

- Packing credentials or private data
- Using a brief instead of a clone when the task needs edits or test runs
