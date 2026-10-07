---
title: Maverick Harness
created: 2026-10-07
updated: 2026-10-07
type: entity
tags: [maverick, control-plane, verification]
sources: [raw/articles/maverick-vision.md, raw/articles/genesis-project-plan.md]
confidence: high
---

# Maverick Harness

A small **control layer** around coding agents. Genesis keeps project state.
Maverick adds **independent verification** and **automatic context**.

The harness itself has no AI — it is a **deterministic control plane** that
supervises coding agents. It does not implement code; it verifies code that
agents produce.

## Core Rule
No coding agent certifies its own work. Only verifier VERIFIED (exit 0) counts.
See [[agent-self-certification]] for why this matters.

## Three Systems
1. **[[genesis-system]]** — "What are we building and what constitutes done?"
   Manages requirements, decisions, invariants, tasks, gates, evidence.
2. **Maverick** — "How do we enforce discipline in an agentic workflow?"
   Orchestration, context engineering, independent verification, risk-based gates.
3. **Wiki** (this vault) — knowledge base with [[context-packs]] curation.

## Architecture
See [[control-plane-architecture]] for the full flow:
Human -> Maverick -> {Genesis, Wiki, Memory} -> Context Pack -> Agent -> Verify -> Verdict

## Four Responsibilities
1. **Orchestration** — automated agent lifecycle
2. **Context engineering** — curated [[context-packs]], not full dumps
3. **Independent verification** — tests, adversarial, mutation, evidence
4. **Risk-based gates** — verification intensity matches [[risk-based-verification|risk level]]

## Phase Roadmap
| Phase | Outcome | Status |
|-------|---------|--------|
| P0 | Repo init, V0 built, traps pass | DONE |
| P1 | CI runs traps on push | PENDING |
| P2 | CLI: start/verify/status | PENDING |
| P3 | Context pack max 8KB with source IDs | PENDING |
| P4 | Write-back hook, proposals vs decisions | PENDING |
| P5 | Hidden QA isolated from agent | PENDING |
| P6 | Risk levels, mutation testing, 3-try cap | PENDING |
| P7 | Wiki vault, citations | IN PROGRESS |
| P8 | Log misses, DB only if > 20% | PENDING |

## What NOT to Do
- Build another coding agent (Maverick controls agents)
- Replace Genesis (see [[maverick-vs-genesis]])
- Create competing task system (use Genesis tasks)
- Introduce memory DB without measured miss (see [[miss-measurement]])
- Trust agent-generated tests without verification
- Let agent endlessly repair (see [[bounded-repair-loop]])

## Stack
- Python 3 standard library only (see [[stdlib-only-constraint]])
- One repo, installed into ~/.claude
- No external dependencies without user decision

## Related
- [[independent-verification]]
- [[verification-checks]] — the four checks in V0
- [[human-in-the-loop]] — supervised autonomy, not full automation — the core mechanism
- [[trap-benchmark]] — 8 scenarios testing verifier effectiveness
- [[evidence-integrity]] — provenance tracking for each verification
- [[cognitive-job]] — what thinking the system performs

## External References
- [ext:clean-architecture/Boundary-Lines] — Maverick is a boundary between agent and truth
- [ext:pragmatic-programmer/Tracer-Bullets] — V0 is a tracer bullet: thin end-to-end slice
