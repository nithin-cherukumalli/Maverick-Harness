---
title: Independent Verification
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [verification, trust-boundary, evidence]
sources: [raw/articles/maverick-vision.md, raw/articles/genesis-project-plan.md]
confidence: high
---

# Independent Verification

The core mechanism of [[maverick-harness]]. A code change is verified by a
**separate, independent verifier** — not the agent that produced it.

## Five Verification Levels
1. **Tests execute** (exit code 0) — V0
2. **Tests are meaningful** (can they detect the bug?) — V0
3. **Adversarial cases** (what breaks it?) — P6
4. [[mutation-testing|Mutations detected]] (tests fail when code deliberately breaks) — V0 (basic)
5. [[evidence-integrity|Evidence integrity]] (SHA, environment, timestamp) — V0 (partial)

## The Verdict
Binary: **VERIFIED** (exit 0) or **NOT PROVEN** (exit non-zero).
Only VERIFIED counts. "All tests passed" from the agent is evidence, not proof.

## Why It Matters
See [[agent-self-certification]] — when the agent is implementer + test author +
test runner + judge, it can game its own verification. Independent verification
removes the judge role from the agent.

## How It Works (V0)
`verifier/verify.py` runs four checks in order (first failure short-circuits):
1. Test files exist
2. Tests pass (unittest)
3. Tests are meaningful (AST analysis — no `assert True`, real assertion methods)
4. Mutation testing (flip first comparison operator, check if tests catch it)

## Related
- [[agent-self-certification]] — the anti-pattern this prevents
- [[mutation-testing]] — check 4 in detail
- [[evidence-integrity]] — provenance for each verification
- [[trap-benchmark]] — 8 scenarios testing the verifier itself
- [[risk-based-verification]] — not every change needs all 5 levels
- [[traditional-testing-vs-independent-verification]] — comparison

## External References
- [ext:clean-architecture/Design-for-Testability-Principle] — tests as first-class citizens
- [ext:llmops-ai-agents/Evaluation-Systems] — evaluation is an architecture, not a script
