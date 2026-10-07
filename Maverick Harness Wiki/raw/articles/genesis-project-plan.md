---
source_url: file:///Users/nitin/Documents/Maverick Harness/.genesis/PLAN.md
ingested: 2026-10-07
sha256: computed-on-write
---

# Genesis Project Plan — Maverick Harness

## Core Rule
No coding agent certifies its own work. Only verifier VERIFIED (exit 0) counts.

## Phases
P0 Setup: git init, install genesis-kit, unpack V0, run traps. DONE: traps pass, git clean.
P1 CI: run traps on every push. DONE: breaking verify.py turns CI red.
P2 CLI: maverick start | verify | status. DONE: verify gives verdict + checkpoint on VERIFIED.
P3 Context pack: max 8KB, every line sourced. DONE: 10 tasks, 8+ get right pages.
P4 Write-back: end-of-session hook, proposals vs decisions. DONE: fake "use Redis" stays proposal.
P5 Isolation: hidden QA outside agent reach. DONE: agent edits to QA blocked in real session.
P6 Stronger checks: risk levels, mutation testing, 3-try cap. DONE: new traps caught.
P7 Wiki: init vault, Obsidian, ingest, lint. DONE: 5 questions with [[page]] citations.
P8 Measure: log misses, DB only if > 20%. DONE: miss log exists.

## Constraints
- Standard library only. One function before a class. No config without a user.
- Genesis stays unmodified. Talk to it only through its CLI. Pin its version.
- Build one phase at a time. A phase is done only when its test passes.
- No SQLite, graph, embeddings or memory DB until a measured miss justifies it.
- Any number in a doc must come from a command. Otherwise write "unknown".
- Agent ideas are "proposal". Only the human makes a "decision".

## Invariants (from context-graph.json)
- INV-01: No agent self-certification. Only verifier VERIFIED (exit 0) counts.
- INV-02: Hidden QA tests outside the agent's reach.
- INV-03: Standard library only.
- INV-04: One function before a class. No premature abstraction.
- INV-05: Agent ideas are "proposal". Only human makes a "decision".
- INV-06: No SQLite/graph/embeddings until measured miss justifies it.
- INV-07: Any number in a doc must come from a command.
- INV-08: Genesis stays unmodified. CLI only. Version pinned.
- INV-09: Bounded repair — max 3 attempts, then BLOCKED to HUMAN.
- INV-10: Every context pack line shows its source ID.
