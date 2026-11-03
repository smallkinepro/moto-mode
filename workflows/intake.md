# Intake

**Owner:** chief of staff. **Output:** a ticket with acceptance checks and an owner.

1. Restate the request in one sentence, in the requester's words where possible.
2. Classify: new project, change to an existing one, bug, research, or ops.
3. New projects need a plan approved by the human before anything is built: goal, prior art, architecture, roles, gates, risks, first slice.
4. Write the ticket with `ticket-acceptance-criteria`: scope in/out, observable checks, dependencies, owner, sequence.
5. Slice large work into verifiable units. Each slice gets its own approval if the human asked for slice-by-slice.
6. Assign one owner. Name the gate skill they will run.

**Stop if:** the request touches anything in `guardrails/approval-gates.md` without explicit approval.
