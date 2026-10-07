---
title: Bounded Repair Loop
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [bounded-repair, autonomy, escalation, process]
sources: [raw/articles/maverick-vision.md, raw/articles/genesis-project-plan.md]
confidence: high
---

# Bounded Repair Loop

When verification fails, the agent gets **at most 3 repair attempts**. After
that, the task is BLOCKED and escalated to the human.

```
IMPLEMENT -> VERIFY -> FAIL -> REPAIR -> VERIFY -> FAIL -> REPAIR -> VERIFY
                                                          |
                                              BLOCKED -> HUMAN (after 3rd fail)
```

## Why Bounded?
Without a cap, agents can:
- **Optimize against the verifier** — learn the test patterns and game them
- **Loop indefinitely** — burn tokens and time without convergence
- **Introduce regressions** — each repair may fix one thing and break another

## INV-09
> Bounded repair — max 3 attempts, then BLOCKED -> HUMAN.

This is invariant INV-09 in the project's [[trust-boundaries|trust model]].

## Repair Counter
The verifier tracks repair attempts. In V0, this is logged in the evidence
bundle. In P6, the 3-try cap is enforced programmatically.

## Related
- [[independent-verification]]
- [[repair-escalation]] — the full escalation protocol — what triggers the repair loop
- [[trust-boundaries]] — human is the escalation target
- [[agent-self-certification]] — unbounded repair is a form of self-certification
- [[risk-based-verification]] — high-risk changes may have stricter caps

## External References
- [ext:llmops-ai-agents/Bounded-Loops] — bounded loops from safety research
