# workflows

Six stages, one owner each, one gate between each. A stage is not finished until its gate passes with evidence.

```mermaid
flowchart LR
  I[Intake<br/>chief of staff] --> S[Spec lock<br/>designer]
  S -->|spec-lock-pass| B[Build<br/>builder]
  B -->|build-ship| V[Verify<br/>reviewer]
  V -->|specialty verify| SH[Ship<br/>builder]
  SH -->|ship-verify| D((Done))
  V -. fail .-> B
  SH -. fail .-> B
  V -. failure or correction .-> R[Retro<br/>designer]
  SH -. failure or correction .-> R
  R -->|skill-evolution-after-failure| S
```

| Stage | Doc | Gate skill | Human approval? |
|---|---|---|---|
| Intake | [intake.md](intake.md) | ticket-acceptance-criteria | Priority and new projects |
| Spec lock | [spec-lock.md](spec-lock.md) | spec-lock-pass | Spec sign-off |
| Build | [build.md](build.md) | build-ship | No |
| Verify | [verify.md](verify.md) | specialty verify + code-review-checklist | No |
| Ship | [ship.md](ship.md) | ship-verify | Public, paid, or irreversible actions |
| Retro | [retro.md](retro.md) | skill-evolution-after-failure | No |
