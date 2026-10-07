---
title: Maverick vs Genesis
created: 2026-10-07
updated: 2026-10-07
type: comparison
tags: [maverick, genesis, comparison]
sources: [raw/articles/maverick-vision.md, raw/articles/genesis-project-plan.md]
confidence: high
---

# Maverick vs Genesis

They are **complementary, not competing**.

## The Question Each Answers

| System | Question | Role |
|--------|----------|------|
| [[genesis-system|Genesis]] | "What are we building and what constitutes done?" | Project operating system |
| [[maverick-harness|Maverick]] | "How do we enforce this discipline in an agentic workflow?" | Control plane / verifier |

## What Each Owns

| Responsibility | Genesis | Maverick |
|---------------|---------|----------|
| Requirements (FR, NFR, AC) | Owns | Does not duplicate |
| Decisions and costs | Owns | Logs proposals only |
| Invariants | Owns | Reads via CLI |
| Tasks with dependencies | Owns | Does not duplicate |
| Gates | Owns | Respects, does not bypass |
| Evidence and approvals | Owns | Produces evidence, Genesis stores |
| Independent verification | Does not do | Owns |
| Context engineering | Does not do | Owns |
| Risk-based gates | Does not do | Owns |
| Agent lifecycle | Does not do | Owns |

## The Interface
Per [[genesis-cli-contract|INV-08]], Maverick talks to Genesis **only through
its CLI**. Genesis is unmodified. Its version is pinned.

## What NOT to Do
- Build another project state system in Maverick
- Create competing task systems
- Modify Genesis internals
- Bypass Genesis gates

## Related
- [[genesis-system]] — the project OS
- [[maverick-harness]] — the control plane
- [[genesis-cli-contract]] — the interface contract
- [[control-plane-architecture]] — how they fit together
- [[proposal-vs-decision]] — Genesis tracks decisions, Maverick logs proposals
