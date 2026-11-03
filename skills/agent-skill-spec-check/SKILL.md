---
name: agent-skill-spec-check
description: >-
  Validate SKILL.md folders against the Agent Skills spec with the reference
  skills-ref validator: name equals folder slug, description present and says
  when to use it, no duplicates, no secrets. Use before publishing skills, in
  CI on any repo that ships skills/, or after editing a skill.
license: MIT
metadata:
  phase: "5-verify"
  layer: L1
---
# Agent skill spec check

Use the reference validator `skills-ref` from `agentskills/agentskills` (Apache-2.0) as a lint, pinned to a commit.

## Steps
1. Install:
   ```bash
   pip install "git+https://github.com/agentskills/agentskills.git@<sha>#subdirectory=skills-ref"
   ```
2. Validate:
   ```bash
   for d in skills/*/; do skills-ref validate "$d"; done
   ```
3. Fix common failures:
   - `name` must be lowercase letters, digits, and hyphens, and equal the folder name. Some apps store a display name ("Ship verify"); set the slug on export and keep the display name as the body title.
   - Two folders with the same `name` are duplicates; merge them.
   - `description` must say what the skill does and when to use it, under 1024 characters.
4. Optional: `skills-ref to-prompt skills/*` shows the block an agent sees. Check that descriptions read clearly side by side.
5. Grep skill bodies for secrets, internal names, and ids.

## Report
Valid vs failing count, fixes made, duplicates found.

## Out of scope
Renaming skills inside an app's own library; convert on export instead.
