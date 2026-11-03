---
name: agent-design-bar
description: >-
  Design or revise an agent role (seat) so it stays single-purpose and
  verifiable: one job, voice, anti-jobs, verify path, and minimal tools. Use
  when creating a new agent role, splitting one that drifts, or reviewing a
  role template.
license: MIT
metadata:
  phase: "2-spec"
  layer: L1
---
# Agent design bar

## Required fields
1. **One job.** One sentence. If it needs "and", consider two roles.
2. **Voice.** Short and consistent; how it reports.
3. **Does.** The three to five things it actually does.
4. **Anti-jobs.** Explicit list of what it must not do, especially the neighbor role's job.
5. **Verify path.** Which gate skills it runs before saying done (see `specialty-skill-tree`).
6. **Tools.** Only what the job needs. Remove leftovers. Write access is the exception.
7. **Approvals.** Which actions it must escalate (`guardrails/approval-gates.md`).

## Checks
- No role reviews its own output.
- Every gate in the workflow has exactly one owning role.
- Coding roles point at `build-ship` and `ship-verify` plus their specialty verify skill.

## After creating
Register which skills the role is assigned on handoffs, and add the template under `seats/`.
