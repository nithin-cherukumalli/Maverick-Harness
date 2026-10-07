# Maverick Harness — Current State

**Last updated**: 2026-10-07T15:15:00+05:30 (IST)
**Active phase**: P2 — CLI
**Previous phase**: P1 — CI (VERIFIED)

## What's Done
- [x] P0 VERIFIED — all 8 L4 checks pass
- [x] P1 VERIFIED — CI runs traps on push/PR; breaking verify.py turns CI red
- [x] Architectural directive internalized — context engine is a decision layer, not a memory system
- [x] context-graph.json updated — architecture, authority hierarchy, 14 invariants
- [x] Wiki enriched — 36 pages with authority hierarchy, context engineering, ownership model

## P1 Evidence
- CI workflow: `.github/workflows/trap-ci.yml` runs `python3 trap-project/run_traps.py` on push to main and PRs to main
- Green run: commit `bcc3c1f` → run 37607741747 → success (12s)
- Red run: PR #1 with broken verify.py → run 37609015588 → failure (11s)
- Test PR closed, branch deleted

## Active Invariants (14 total)
- INV-01: No agent self-certification (only verifier exit 0 counts)
- INV-02: Hidden QA outside agent reach
- INV-03: Standard library only
- INV-05: Agent ideas are proposals, not decisions
- INV-08: Genesis unmodified (CLI only, version pinned)
- INV-09: Bounded repair (max 3 attempts, then BLOCKED → HUMAN)
- INV-10: Every context pack line shows its source ID
- INV-11: Derived context must never silently become authoritative
- INV-12: Maverick does not duplicate Genesis or Wiki — it selects from them
- INV-13: Context engineering answers "what does the agent need NOW?", not "how much?"
- INV-14: Every abstraction must be earned by a demonstrated failure or measured need

## What's Known to Be Broken
- Nothing currently

## Blockers
- None

## Next Action (P2 — CLI)
1. Create `maverick` CLI with subcommands: start, verify, status
2. `maverick verify` on toy project → VERIFIED verdict + checkpoint
3. Demo: run `maverick verify` on trap-project, confirm VERIFIED
