---
title: Agent Self-Certification (Anti-Pattern)
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [self-certification, anti-patterns, trust-boundary]
sources: [raw/articles/maverick-vision.md]
confidence: high
---

# Agent Self-Certification (Anti-Pattern)

The core anti-pattern Maverick exists to prevent.

## The Problem
Coding agents are capable but **stochastic**. They can confidently produce
wrong work and then verify their own implementation, becoming simultaneously:
- **Implementer** — writes the code
- **Test author** — writes the tests
- **Test runner** — runs the tests
- **Judge** — declares "done" or "tests passed"

When all four roles belong to the same entity, it can **game its own
verification** — consciously or unconsciously optimizing tests to pass
without actually being correct.

## The Fix
[[independent-verification|Independent verification]] removes the **judge**
role from the agent:
- The agent implements and writes tests
- A **separate verifier** (outside the agent's control) runs the tests,
  checks they're meaningful, and mutation-tests them
- Only the verifier's VERIFIED (exit 0) counts — INV-01

## Related Anti-Patterns
- **Infinite repair** — agent endlessly fixes its own work without convergence
  (see [[bounded-repair-loop]])
- **Eval debt** — shipping without golden datasets or regression gates
- **Premature abstraction** — building infrastructure before needing it
  (see [[stdlib-only-constraint]])

## Related
- [[independent-verification]] — the fix
- [[trust-boundaries]] — agent is UNTRUSTED
- [[coding-agent]] — the entity that must not self-certify
- [[trap-benchmark]] — tests that the verifier catches self-certified wrong code
- [[hidden-qa-isolation]] — prevents the agent from editing tests

## External References
- [ext:llmops-ai-agents/Evaluation-Systems] — evaluation is an architecture, not a script
