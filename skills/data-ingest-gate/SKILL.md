---
name: data-ingest-gate
description: >-
  Gate before scraping, downloading, or loading any external dataset: confirm
  the source is public or licensed, terms allow the use, it holds no personal
  data, and provenance (URL, time, row count, hash) is recorded. Use before
  any new source lands in a warehouse or lake.
license: MIT
metadata:
  phase: "3-build"
  layer: L1
---
# Data ingest gate

All checks must pass. If any is unclear, stop the load and escalate. Do not almost-ship a borderline source.

## Checks
1. **Public or licensed by design.** Prefer official open-data APIs and bulk downloads. Record the canonical URL and the license or terms link.
2. **No personal data.** Aggregate or entity-level only. Reject anything with identifiers for individuals unless it is labeled synthetic and a human approved it.
3. **Terms and robots.** Prefer machine-readable endpoints. No HTML scraping of sites whose terms forbid it.
4. **Idempotent snapshot.** Write `pulled_at`, source URL, content hash or etag, and row count to a provenance table or file. Reloading the same snapshot must not duplicate rows.
5. **Secrets.** API keys come from the environment and never appear in logs or commits.
6. **Size and cost.** Note the download size and any metered cost; sample first in development.

## Done means
Provenance recorded, raw table or Parquet written, row count quoted, and this gate named in the handoff.
