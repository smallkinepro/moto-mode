---
name: specialty-skill-tree
description: >-
  Map of which skills each specialty runs, in layers: L0 gates for every
  change, L1 craft skills per specialty, L2 deep skills learned from repeat
  failures. Use when assigning work, standing up a new role, or deciding which
  skill should own a lesson.
license: MIT
metadata:
  phase: "1-intake"
  layer: L0
---
# Specialty skill tree

Skills are generic recipes. Project names and role assignments live in tickets, not here.

| Layer | Purpose | When |
|---|---|---|
| L0 gates | Every change | Always before done |
| L1 craft | A specialty's normal job | Every task in that specialty |
| L2 deep | Patterns learned from repeats | When an L1 skill links to it, or after a repeat failure |

## L0 gates
- `spec-lock-pass`, `build-ship`, `code-review-checklist`, `ship-verify`, `skill-evolution-after-failure`

## L1 by specialty
| Specialty | Skills |
|---|---|
| Planning | `ticket-acceptance-criteria` |
| Research | `oss-scout-gate`, `repo-brief` |
| Web and app UI | `design-qa` |
| Native and game | `native-game-headless-verify` |
| Data engineering | `data-ingest-gate`, `pipeline-ship` |
| Analytics | `report-publish-bar` |
| Team design | `agent-design-bar`, `agent-skill-spec-check` |

## L2
Added by `skill-evolution-after-failure` when the same failure class repeats. Reference each L2 from its parent L1.

## Adding a specialty
Define its L1 skill first, then its role with `agent-design-bar`, then add a row here.
