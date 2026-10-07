---
title: Testing API Design
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [test-quality, architecture, boundary]
sources: [raw/articles/maverick-vision.md]
confidence: high
---

# Testing API Design

Tests are first-class architectural components whose needs shape the design
of the production system — not an afterthought.

## The Testing API Principle
A dedicated Testing API hides application structure from tests, allowing both
sides to evolve independently. This prevents the Fragile Tests Problem where
tests break on trivial changes because they're coupled to volatile structure.

## Maverick's Testing Architecture
Maverick embodies this principle in several ways:
- The verifier's `verify()` function IS a testing API — it takes a project
  directory and returns a binary verdict
- [[hidden-qa-isolation|Hidden QA]] is a separate testing component that the
  agent cannot access
- [[trap-benchmark|Trap scenarios]] test the verifier itself (meta-testing)
- The evidence bundle is the testing API's structured output

## The Fragile Tests Problem
If tests mirror production code structure one-to-one, any refactoring breaks
tests even when behavior is preserved. The fix: test through a stable API,
not through internal structure.

In Maverick's case, the agent's tests are NOT trusted because they may be
fragile (only happy path, `assert True`). The verifier checks test quality
through [[mutation-testing]] and AST analysis.

## Dangerous Test Superpowers
Testing APIs have superpowers (bypassing security, forcing state) that must
NOT be deployed to production. Maverick's hidden QA has similar superpowers —
it can test things the production code cannot access. Per [[hidden-qa-isolation]],
these stay in a separate, non-deployed component.

## Related
- [[independent-verification]] — the verifier IS a testing API
- [[mutation-testing]] — checking test quality
- [[hidden-qa-isolation]] — superpowered tests outside agent reach
- [[agent-self-certification]] — what happens when tests are not first-class
- [[architectural-boundary]] — the boundary between tests and production

## External References
- [ext:clean-architecture/Design-for-Testability-Principle] — tests as first-class
