---
title: Cognitive Job
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [verification, control-plane]
sources: [raw/articles/genesis-project-plan.md]
confidence: high
---

# Cognitive Job

What thinking the Maverick system performs.

## The Job
> Given a code change produced by a coding agent, **independently verify** it
> against hidden tests, adversarial cases, and evidence integrity — producing
> a binary **VERDICT** (VERIFIED exit 0 / NOT PROVEN exit non-zero).

## Key Characteristic
The harness itself performs **no LLM reasoning**. It is a **deterministic
control layer**. All "intelligence" is in the tests, mutation operators, and
evidence checking — not in probabilistic reasoning.

## Autonomy Level
- **Fully autonomous** for verification (runs without human input)
- **Human required** for decisions (see [[proposal-vs-decision]])
- **Human required** for escalation after 3 failed repairs (see [[bounded-repair-loop]])

## Failure Modes
1. Agent self-certifies -> prevented by INV-01
2. Agent edits hidden QA -> prevented by INV-02 + P5
3. Agent makes decision without human -> prevented by INV-05
4. Agent introduces DB without measured miss -> prevented by INV-06
5. Agent endlessly repairs -> prevented by INV-09
6. Verifier passes wrong code -> caught by [[trap-benchmark]]

## Related
- [[maverick-harness]]
- [[human-in-the-loop]] — autonomy boundaries require human touchpoints — the system that performs this job
- [[independent-verification]] — the mechanism
- [[trust-boundaries]] — autonomy boundaries
- [[control-plane-architecture]] — where the cognitive job fits
