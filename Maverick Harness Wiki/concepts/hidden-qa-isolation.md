---
title: Hidden QA Isolation
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [isolation, trust-boundary, verification, security]
sources: [raw/articles/maverick-vision.md, raw/articles/genesis-project-plan.md]
confidence: high
---

# Hidden QA Isolation

Hidden QA tests are **outside the coding agent's reach**. The agent cannot
read, edit, or discover them.

## INV-02
> Hidden QA tests are outside the agent's reach (not in agent-editable directories).

## P5: Isolation
Phase 5 moves hidden QA out of the agent's reach and tests it in a **live
Claude Code session**:
- Agent attempts to edit a QA file -> blocked
- Tested in a real session, not just in theory

## P5 Done Condition
> Agent edits to QA are blocked in a real session.

## Why Hidden?
If the agent can see the QA tests, it can:
- **Optimize against them** — write code that passes tests without being correct
- **Edit them** — weaken tests to make its code pass
- **Game the verifier** — learn test patterns and exploit them

## Relationship to Trap Benchmark
The [[trap-benchmark|8 traps]] are currently in `trap-project/` which is frozen
after P0. In P5, they (or equivalent hidden QA) move to a location the agent
cannot access.

## Related
- [[trust-boundaries]] — hidden QA is OUTSIDE AGENT REACH
- [[independent-verification]] — hidden QA is part of the verification arsenal
- [[agent-self-certification]] — hidden QA prevents the agent from gaming tests
- [[claude-code]] — P5 tests in a live Claude Code session

## External References
- [ext:security-engineering] — principle of least privilege, isolation
- [ext:clean-architecture/Boundary-Lines] — boundary between agent and QA
