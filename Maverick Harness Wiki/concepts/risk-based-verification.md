---
title: Risk-Based Verification
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [risk-level, verification, process]
sources: [raw/articles/maverick-vision.md]
confidence: high
---

# Risk-Based Verification

Not every change needs the full verification arsenal. Verification intensity
matches the **risk level** of the change.

## Risk Levels

| Level | Examples | Verification |
|-------|----------|-------------|
| **Low** | README, docs, comments | Basic gates (tests pass) |
| **Medium** | Business logic, API changes | Unit, integration, regression, evidence |
| **High** | Auth, payments, security, AI decisions | Full verification: adversarial, mutation, independent model, human approval |

## P6: Implementation
Phase 6 implements risk-based verification:
- Risk levels assigned per changed file
- [[mutation-testing|Mutation testing]] only on risky changed files (not all files)
- 3-try [[bounded-repair-loop|repair cap]] enforced
- New traps: surviving mutant, weak edge test

## Why Risk-Based?
- **Performance**: running full mutation testing on every file is slow
- **Signal-to-noise**: low-risk changes don't need adversarial testing
- **Focus**: high-risk changes get the most scrutiny

## Related
- [[independent-verification]] — the base mechanism
- [[mutation-testing]] — applied selectively by risk level
- [[bounded-repair-loop]] — repair caps may vary by risk
- [[trap-benchmark]] — P6 adds risk-based traps
