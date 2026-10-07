# Maverick Harness — Roadmap

## Vision
A small control layer around coding agents. Genesis keeps project state.
Maverick adds independent verification and automatic context.

## Core Rule
No coding agent certifies its own work. Only verifier VERIFIED (exit 0) counts.

## Phases

| Phase | Outcome | Status |
|-------|---------|--------|
| P0 Setup | Repo init, V0 unpacked, traps pass | IN PROGRESS |
| P1 CI | Traps on every push, breaking verify turns CI red | PENDING |
| P2 CLI | `maverick start \| verify \| status` | PENDING |
| P3 Context Pack | 8KB pack with source IDs on every line | PENDING |
| P4 Write-back | End-of-session hook, proposals vs decisions | PENDING |
| P5 Isolation | Hidden QA outside agent reach, live Claude Code test | PENDING |
| P6 Stronger Checks | Risk levels, mutation testing, 3-try repair cap | PENDING |
| P7 Wiki | Obsidian vault, 5 questions with [[page]] citations | PENDING |
| P8 Measure | Log misses, DB only if > 20% | PENDING |

## Constraints
- Standard library only. One function before a class. No config without a user.
- Genesis stays unmodified. Talk to it only through its CLI. Pin its version.
- Build one phase at a time. A phase is done only when its test passes.
- No SQLite, graph, embeddings or memory DB until a measured miss justifies it.
- Any number in a doc must come from a command. Otherwise write "unknown".
- Agent ideas are "proposal". Only the human makes a "decision".

## Verification Levels (target)
1. Tests execute (exit code 0) — V0
2. Tests are meaningful (can detect the bug) — V0
3. Implementation survives adversarial cases — P6
4. Mutations are detected — V0 (basic), P6 (risk-based)
5. Evidence integrity (SHA, environment, timestamp) — V0 (partial), P6 (full)

## Trap Benchmark
- TRAP-001: Wrong label
- TRAP-002: Weak test
- TRAP-003: Stale evidence
- TRAP-004: Bad split
- TRAP-005: Data leakage
- TRAP-006: Mutation survives
- TRAP-007: UI regression
- TRAP-008: API contract violation

Success: ALL TRAPS BEHAVE
