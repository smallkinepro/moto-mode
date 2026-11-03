# Verify

**Owner:** reviewer (not the builder). **Gate:** the specialty verify skill plus `code-review-checklist`.

| Work type | Verify skill |
|---|---|
| Web or app UI | `design-qa`, then `ship-verify` smoke |
| Native or game build | `native-game-headless-verify` |
| Data pipeline | `pipeline-ship` |
| New data source | `data-ingest-gate` |
| Report or dashboard | `report-publish-bar` |
| Published skills | `agent-skill-spec-check` |

1. Check out the exact SHA under review.
2. Re-run the checks yourself. Do not trust the builder's output.
3. Walk each acceptance check and mark pass/fail with evidence.
4. Fail goes back to build with the failing check quoted. Two fails of the same class trigger a retro.
