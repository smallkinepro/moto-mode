---
name: native-game-headless-verify
description: >-
  Verify a native (non-web) game build with evidence: release build, a
  deterministic scripted headless run, an offscreen render check, a remote
  command smoke test, a data-file edit check, and green CI. Use before calling
  a desktop game build done, for example a Rust or Bevy game with a headless mode.
license: MIT
metadata:
  phase: "5-verify"
  layer: L1
---
# Native game headless verify

Every step records the command, the commit SHA, and the actual output. If a step can't run, say so; never mark it passed.

## 1. Build
- Check out the exact SHA under review.
- Release build exits 0 (for example `cargo build --release`). Note warnings that matter.
- Unit and simulation tests pass in no-render mode.

## 2. Headless state run (hard gate)
- Run the scripted headless pass for N frames with a committed input script.
- Open the JSON state output and quote the fields the script should produce (player moved, score at least the expected value, win flag).
- Determinism: run twice and diff the JSON. Any difference fails.

## 3. Headless render run
- Run with an offscreen camera and screenshot. Open the PNG.
- Fail if it is missing, one solid color, garbled, or disagrees with the JSON.
- Say which GPU path rendered it (real GPU or a software driver such as lavapipe).
- If the project marks the render check warn-only, report it without blocking.

## 4. Remote command smoke test
- Start the game with its local command interface on (for example Bevy Remote Protocol on localhost).
- With a scripted client: list methods, pause, change one thing, step a known number of frames, query state. Quote request and response.
- An AI/MCP bridge check may be marked warn-only; report it either way.

## 5. Data files
- Edit one value in a content or tuning file (RON, TOML), rerun step 2, confirm the output changes. Revert.

## 6. CI
- Green on the same SHA, including the headless job. Attach links to the run and artifacts.
- Report wall time and whether the cache was warm or cold.

## CI pitfalls (Rust)
- Linker bus error: set `debug = "line-tables-only"` in the CI profile and free disk before building.
- Cache `~/.cargo/bin` so installed tools survive; save one shared cache key from one job only.
- Keep only the pinned toolchain installed.
- Put `timeout-minutes` on every step; a hung software renderer otherwise burns the job default.

## Report
SHA, each step pass/fail/warn with quoted evidence, render path, CI link, wall time, and gaps.
