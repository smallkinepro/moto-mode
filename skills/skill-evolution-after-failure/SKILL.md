---
name: skill-evolution-after-failure
description: >-
  Turn a human correction, failed gate, or repeated bug into a durable edit to
  the right skill or rule, so the same class of failure does not recur. Use
  after anything called done turns out wrong, or when a gate fails twice for
  the same reason.
license: MIT
metadata:
  phase: "7-retro"
  layer: L0
---
# Skill evolution after failure

## When
- A human reports a bug after work was called done.
- A verify gate fails a second time on the same task type.
- A role invents a workaround that should be standard.

## Steps
1. **Name the failure class** as a mechanism, not a symptom. Bad: "animation looked weird". Good: "position updated on a 200ms timer while animation frames used a separate clock".
2. **Find the owner skill** with `specialty-skill-tree`. Prefer editing an existing skill over adding one.
3. **Classify.** First time: add a checklist bullet to the owner skill. Second time: add or extend a deeper skill and link it from the parent.
4. **Edit the skill generically.** No repo names, people, or ids. Project specifics go in the handoff.
5. **Validate** with `agent-skill-spec-check`.
6. **Close the loop.** The next similar task's handoff names the updated skill.
7. **Tell the human** in one line what practice is now locked.

## Anti-patterns
- Saving one-off paths or gossip as skills.
- Duplicating a near-identical skill instead of editing the parent.
- Writing the lesson to memory when it is a procedure.
- Skipping it because "we'll remember".
