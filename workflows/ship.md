# Ship

**Owner:** builder, with human approval where the guardrails require it. **Gate:** `ship-verify`.

1. Confirm CI is green on the exact SHA being merged or deployed.
2. Merge or deploy only with the approvals in `guardrails/approval-gates.md` (anything public, paid, or irreversible).
3. Run `ship-verify`: deploy is ready for that SHA, every touched URL or artifact smoke-tested, one real behavior check.
4. Report: SHA, links to CI and deploy, gate result, known gaps.

"Live" means a person can use it right now at the link you posted.
