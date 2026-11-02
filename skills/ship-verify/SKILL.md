---
name: ship-verify
description: >-
  Evidence gate before saying anything is done, live, merged, or fixed: build
  command, commit SHA, deploy ready for that SHA, smoke checks on every touched
  URL and asset, a real behavior check, and an honest list of gaps. Use before
  any deploy, merge, or "it's live" handoff.
metadata:
  phase: "6-ship"
  layer: L0
---
# Ship verify

Don't claim done, announce "live", or ask anyone to "take a look" until this gate passes.

## When to use

- Before reporting any merge, deploy, or release as done
- Before a handoff that says a change is live

## Steps

Collect everything that applies, and paste it into the completion note:

- [ ] **Build:** the build command exited 0. Write down the command.
- [ ] **Commit:** the SHA on the branch that deploys
- [ ] **Deploy:** the target environment reports ready **for that SHA**, not just "a deploy finished"
- [ ] **Smoke:** a request to the live URL **and every critical route, asset, or endpoint touched** returns success. Include images, bundles, and data files, not only `/`.
- [ ] **Behavior check:** exercise the changed path on the live system (submit the form, run the flow, load the report). A passing build is not a behavior check.
- [ ] **Clients and caches:** if caches or stored state changed, tell users how to refresh or migrate
- [ ] **Diff honesty:** list what's still imperfect or waiting on someone else

## Feel and motion changes

If the change touches animation, scrolling, timers, or layout over imagery:

- [ ] Prefer continuous drivers (animation frames, CSS transforms) over intervals that cause layout thrash
- [ ] Nothing is drawn twice, and opaque UI doesn't cover key imagery

## Fail means not done

If a required check fails, fix it or narrow the claim. Never send a "partially live" message as success.

## Done means

A skeptical reader can confirm every claim from the note: SHA, deploy status, smoke results, behavior observed, and the gaps.

## Anti-patterns

- "Deployed" when the deploy is still building, or deployed a different SHA
- Smoke-testing the home page only
- Hiding known gaps to make the note look clean
