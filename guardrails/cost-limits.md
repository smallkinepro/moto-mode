# Cost limits

- Every agent task has a budget: wall-clock time, tool calls, or tokens. State it in the ticket for anything large.
- Usage limits are a stop signal. When a team-wide limit is near, the chief of staff pauses non-critical work and says so; agents do not start new work until resumed.
- No paid tools, plans, or API tiers without approval. Free tiers that auto-upgrade count as paid.
- CI: cache aggressively, set timeouts on every job, and cancel superseded runs.
- Data: sample in development. Full scans on metered warehouses need a reason in the PR.
- Schedules default off. A recurring job is an ongoing cost and needs approval.
- Report spend in the handoff when a task used a metered service.
