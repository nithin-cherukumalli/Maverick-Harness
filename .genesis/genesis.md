# Genesis Checklist

Genesis is complete when all items are true.

## Setup Checklist

- [x] **G0** — Cognitive design in DONE.html section 1: 5-question diagnostic, cognitive job, autonomy level, failure modes, trust boundaries
- [x] **G1** — .genesis/ spine scaffolded: DONE.html, context-graph.json, PLAN.md, CURRENT.md, LOOPS.md, KICKOFF.md, wiki/, genesis.md, AGENT-ADAPTERS.md
- [x] **G2** — context-graph.json has real invariants: INV-01 through INV-10
- [x] **G3** — wiki/index.md seeded with agentic-swe-kit concept pointers + Obsidian vault with 28 interlinked pages
- [x] **G4** — DONE.html section 2 has binary phase gates with verified status
- [x] **G5** — PLAN.md has 9 milestones (P0-P8) each with demo command, freeze boundary, and done condition
- [x] **G6** — KICKOFF.md has session prompts; L0 Pre-Flight runnable

## Genesis Status: COMPLETE

---

## What a new AI session needs to know (summary)

**The product**: Maverick Harness is a small control layer around coding agents. Genesis keeps project state. Maverick adds independent verification and automatic context. The harness itself has no AI — it supervises coding agents deterministically.

**Core rule**: No coding agent certifies its own work. Only verifier VERIFIED (exit 0) counts.

**The stack**: Python 3 standard library only. One repo. Installed into ~/.claude.

**Current state**: P0 — Setup COMPLETE. Traps pass (ALL TRAPS BEHAVE). V0 built. Wiki vault populated (28 pages). Ready for L4 VERIFY.

**The most important invariants**:
- INV-01: No agent self-certification. Only verifier VERIFIED (exit 0) counts.
- INV-02: Hidden QA outside agent's reach.
- INV-05: Agent ideas are "proposal". Only human makes "decision".
- INV-09: Bounded repair — max 3 attempts, then BLOCKED -> HUMAN.

---

## File purposes (quick lookup)

| File | Read it when... |
|------|----------------|
| CURRENT.md | Starting any session |
| context-graph.json | Touching any code file |
| PLAN.md | Deciding what phase to work on next |
| DONE.html | Verifying a phase is truly done |
| LOOPS.md | Running a build or verify cycle |
| KICKOFF.md | Starting a fresh agent session |
| wiki/index.md | Looking for engineering patterns to apply |
| AGENT-ADAPTERS.md | Mapping genesis primitives to Hermes |
