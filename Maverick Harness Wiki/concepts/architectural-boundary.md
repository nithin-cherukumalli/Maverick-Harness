---
title: Architectural Boundary
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [boundary, architecture, dependency]
sources: [raw/articles/maverick-vision.md]
confidence: high
---

# Architectural Boundary

A structural divide that separates the abstract (high-level policy) from the
concrete (implementation details), with all source code dependencies pointing
toward the abstract side.

## Maverick's Boundaries
Maverick has several explicit [[trust-boundaries|architectural boundaries]]:
- **Agent/Verifier boundary**: the agent is on the concrete side (volatile,
  untrusted); the verifier is on the abstract side (stable, trusted)
- **Genesis/Maverick boundary**: Genesis is on the abstract side (project
  state, invariants); Maverick accesses it via [[genesis-cli-contract|CLI only]]
- **Hidden QA boundary**: QA tests are on the abstract side; the agent cannot
  reach them (see [[hidden-qa-isolation]])
- **Proposal/Decision boundary**: proposals are on the concrete side; decisions
  are on the abstract side (see [[proposal-vs-decision]])

## Dependency Direction
All dependencies point toward the stable, abstract side:
- Agent depends on verifier (not vice versa)
- Maverick depends on Genesis CLI (not Genesis internals)
- Proposals depend on decisions (not vice versa)

This matches the Dependency Inversion Principle: depend on abstractions, not
concretions. The [[coding-agent|agent]] is volatile and concrete; the
[[independent-verification|verifier]] is stable and abstract.

## Anti-Pattern: Boundary Violation
When the agent can reach the verifier or hidden QA, the boundary is violated.
This is [[agent-self-certification|self-certification]] — the concrete side
has access to the abstract side's judgment.

## Related
- [[trust-boundaries]] — the specific trust levels at each boundary
- [[hidden-qa-isolation]] — the QA boundary
- [[agent-self-certification]] — what happens when boundaries are violated
- [[control-plane-architecture]] — the boundary diagram
- [[genesis-cli-contract]] — the Genesis boundary contract

## External References
- [ext:clean-architecture/Boundary-Lines] — architectural boundaries, DIP
- [ext:clean-architecture/Dependency-Rule] — dependencies point inward
