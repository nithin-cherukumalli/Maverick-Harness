---
title: Repair and Escalation
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [bounded-repair, escalation, autonomy, process]
sources: [raw/articles/maverick-vision.md, raw/articles/genesis-project-plan.md]
confidence: high
---

# Repair and Escalation

When the verifier returns NOT PROVEN, the agent enters a repair loop. The
escalation path determines what happens next.

## The Repair Loop
```
IMPLEMENT -> VERIFY -> NOT PROVEN -> REPAIR -> VERIFY -> NOT PROVEN -> REPAIR -> VERIFY
                                                                          |
                                                              BLOCKED -> HUMAN (3rd fail)
```

## Three Outcomes
1. **VERIFIED** on first try — ideal, no repair needed
2. **NOT PROVEN -> REPAIR -> VERIFIED** — agent fixed the issue within 3 tries
3. **NOT PROVEN after 3 repairs** — BLOCKED, escalate to human

## Escalation Protocol
When the agent hits the 3-try cap:
1. The task is marked BLOCKED in [[genesis-system|Genesis]]
2. The evidence bundles from all 3 attempts are attached
3. The human reviews the evidence and decides:
   - Provide more context and retry
   - Fix the code manually
   - Adjust the verification requirements (only human can do this per [[proposal-vs-decision]])
   - Abort the task

## Why Not Unlimited Repair?
- Agents can **optimize against the verifier** — learning test patterns
- Each repair may **introduce regressions** — fixing one thing, breaking another
- **Token costs** increase without convergence
- **Time** is wasted on a task the agent cannot complete

## P6: Stronger Escalation
Phase 6 adds risk-based escalation:
- Low-risk: 2 tries (not worth spending more)
- Medium-risk: 3 tries (current default)
- High-risk: 3 tries + human approval required even on VERIFIED

## Related
- [[bounded-repair-loop]] — the core invariant (INV-09)
- [[independent-verification]] — what triggers repair
- [[trust-boundaries]] — human is the escalation target
- [[risk-based-verification]] — risk-level affects escalation
- [[evidence-integrity]] — each repair gets its own evidence bundle
- [[proposal-vs-decision]] — only human can adjust verification requirements
