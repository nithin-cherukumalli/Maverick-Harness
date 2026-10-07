---
title: Human in the Loop
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [autonomy, escalation, process, trust-boundary]
sources: [raw/articles/maverick-vision.md, raw/articles/genesis-project-plan.md]
confidence: high
---

# Human in the Loop

Real agentic engineering is **supervised autonomy**, not full automation.
The human is always the final authority.

## Three Human Touchpoints
1. **Decisions** — agent ideas are [[proposal-vs-decision|proposals]]; only
   the human makes decisions
2. **Escalation** — after 3 failed [[bounded-repair-loop|repairs]], the task
   is BLOCKED and the human takes over
3. **Approval** — high-risk changes require human approval even on VERIFIED
   (P6, see [[risk-based-verification]])

## Why Not Full Autonomy?
Coding agents are stochastic. They can:
- Confidently produce wrong work
- Game their own verification (see [[agent-self-certification]])
- Introduce dependencies without approval (see [[stdlib-only-constraint]])
- Accumulate technical debt through "helpful" suggestions

Full autonomy without supervision is the [[agent-self-certification|self-certification
anti-pattern]] extended to the whole system.

## The Human's Role in [[control-plane-architecture|the Architecture]]
```
HUMAN (intent / judgment / decisions)
  |
  v
MAVERICK (orchestrates, verifies)
  |
  v
AGENT (implements, proposes)
  |
  v
VERIFY (produces verdict)
  |
  v
HUMAN (if BLOCKED after 3 tries)
```

## Related
- [[trust-boundaries]] — human is SOLE DECISION MAKER
- [[proposal-vs-decision]] — the decision touchpoint
- [[repair-escalation]] — the escalation touchpoint
- [[bounded-repair-loop]] — why repair is bounded
- [[risk-based-verification]] — approval touchpoint for high-risk changes
- [[agent-self-certification]] — what happens without human oversight

## External References
- [ext:llmops-ai-agents] — human-in-the-loop is an architecture decision
