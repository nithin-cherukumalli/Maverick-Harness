# Maverick Harness — Current State

**Last updated**: 2026-10-07T15:10:00+05:30 (IST)
**Active phase**: P1 — CI
**Previous phase**: P0 — Setup (VERIFIED)

## What's Done
- [x] P0 VERIFIED — all 8 L4 checks pass, traps pass, git clean, .genesis/ complete
- [x] Architectural directive internalized — context engine is a decision layer, not a memory system
- [x] context-graph.json updated — architecture, authority hierarchy, 14 invariants (INV-01 through INV-14)
- [x] Wiki enriched — 36 pages, 4 new concepts (authority-hierarchy, context-engineering-principles, context-engine-selection, ownership-model)

## Active Invariants (14 total)
- INV-01: No agent self-certification (only verifier exit 0 counts)
- INV-02: Hidden QA outside agent reach
- INV-03: Standard library only
- INV-05: Agent ideas are proposals, not decisions
- INV-08: Genesis unmodified (CLI only, version pinned)
- INV-09: Bounded repair (max 3 attempts, then BLOCKED -> HUMAN)
- INV-10: Every context pack line shows its source ID
- INV-11: Derived context must never silently become authoritative
- INV-12: Maverick does not duplicate Genesis or Wiki — it selects from them
- INV-13: Context engineering answers "what does the agent need NOW?", not "how much?"
- INV-14: Every abstraction must be earned by a demonstrated failure or measured need

## What's Known to Be Broken
- Nothing currently

## Blockers
- None

## Next Action (P1 — CI)
1. Create .github/workflows/trap-ci.yml
2. Workflow runs `python3 trap-project/run_traps.py` on every push
3. P1 done condition: breaking verify.py turns CI red
4. Demo: modify verify.py to always return 0, push, confirm CI fails
