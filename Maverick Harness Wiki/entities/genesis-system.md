---
title: Genesis System
created: 2026-10-07
updated: 2026-10-07
type: entity
tags: [genesis, control-plane, orchestration]
sources: [raw/articles/maverick-vision.md, raw/articles/genesis-project-plan.md]
confidence: high
---

# Genesis System

Genesis is the **project operating system** that manages:
- Requirements (FR, NFR, AC)
- Decisions and their costs
- [[trust-boundaries|Invariants]] (must-hold assertions)
- Tasks with dependencies
- Gates (must pass before next phase)
- Evidence and approvals

## Relationship to Maverick
Genesis and Maverick are **complementary, not competing**. See [[maverick-vs-genesis]].
Genesis answers "what are we building and what constitutes done?" Maverick answers
"how do we enforce this discipline in an agentic workflow?"

**Don't duplicate Genesis in Maverick. Orchestrate it.**

## The Genesis Contract
Per [[genesis-cli-contract]] (INV-08):
- Genesis stays **unmodified** — Maverick never edits Genesis internals
- Communication is **through its CLI only**
- Genesis version is **pinned**

## .genesis/ Spine
The genesis ritual creates a project state spine:
- `DONE.html` — definition of done (cognitive design + binary phase gates)
- `context-graph.json` — invariants, file map, trust boundaries, dependencies
- `PLAN.md` — milestones with demo commands and freeze boundaries
- `CURRENT.md` — rolling state (what's active, what's broken, next action)
- `LOOPS.md` — L0 Pre-Flight, L1 BUILD, L3 REVIEW, L4 VERIFY
- `KICKOFF.md` — session start prompts
- `wiki/index.md` — concept pointers

## Related
- [[maverick-harness]] — the verifier that wraps Genesis
- [[control-plane-architecture]] — how Genesis fits in the flow
- [[proposal-vs-decision]] — Genesis tracks decisions; Maverick logs proposals
- [[genesis-cli-contract]] — the interface contract

## External References
- [ext:clean-architecture/Dependency-Rule] — Genesis is an inner dependency, not to be modified
