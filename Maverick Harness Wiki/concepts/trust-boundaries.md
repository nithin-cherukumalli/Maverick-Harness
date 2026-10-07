---
title: Trust Boundaries
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [trust-boundary, verification, isolation]
sources: [raw/articles/maverick-vision.md, raw/articles/genesis-project-plan.md]
confidence: high
---

# Trust Boundaries

Who is trusted for what in the Maverick system.

## Trust Classification

| Entity | Trust Level | Can Do | Cannot Do |
|--------|-------------|--------|-----------|
| [[coding-agent|Coding Agent]] | UNTRUSTED | Implement code, write tests, propose ideas | Certify own work, access hidden QA, make decisions |
| [[independent-verification|Verifier]] | TRUSTED | Run tests, mutation testing, produce verdict | Be modified by the agent |
| [[hidden-qa-isolation|Hidden QA]] | OUTSIDE AGENT REACH | Test the agent's code | Be edited by the agent |
| [[genesis-system|Genesis]] | UNMODIFIED | Track project state | Be modified by Maverick (CLI only, INV-08) |
| Human | SOLE DECISION MAKER | Make decisions, approve, escalate | (none — human is final authority) |

## Invariants That Enforce Boundaries
- INV-01: No agent self-certification
- INV-02: Hidden QA outside agent reach
- INV-05: Agent ideas are proposals, not decisions
- INV-08: Genesis unmodified (CLI only, version pinned)

## Related
- [[agent-self-certification]] — what happens when trust boundaries are violated
- [[hidden-qa-isolation]] — the QA boundary in detail
- [[genesis-cli-contract]] — the Genesis boundary
- [[proposal-vs-decision]] — the decision boundary
- [[bounded-repair-loop]] — escalation to human

## External References
- [ext:security-engineering] — threat modeling, least privilege, defense in depth
- [ext:clean-architecture/Boundary-Lines] — architectural boundaries
