# Maverick Harness — Kickoff

Read this at the start of every session.

## Session Start Prompt

```
You are working on Maverick Harness — a control layer around coding agents.
Read .genesis/CURRENT.md for current state.
Read .genesis/context-graph.json for invariants (INV-01 through INV-10).
Read .genesis/PLAN.md for the active milestone.
Read .genesis/LOOPS.md for the loop you're in.

CORE RULE: No coding agent certifies its own work. Only verifier VERIFIED (exit 0) counts.

CONSTRAINTS:
- Standard library only. One function before a class. No config without a user.
- Genesis stays unmodified. Talk to it only through its CLI. Pin its version.
- Build one phase at a time. A phase is done only when its test passes.
- No SQLite, graph, embeddings or memory DB until a measured miss justifies it.
- Any number in a doc must come from a command. Otherwise write "unknown".
- Agent ideas are "proposal". Only the human makes a "decision".
```

## Before You Write Code
1. Check CURRENT.md — what phase are we in?
2. Check context-graph.json — what invariants apply?
3. Check PLAN.md — what's the demo command for this phase?
4. Run L0 Pre-Flight from LOOPS.md

## After You Write Code
1. Run the demo command for the current phase
2. If it passes, run L3 REVIEW
3. If L3 passes, run L4 VERIFY (separate context via delegate_task)
4. If VERIFY passes, update CURRENT.md and commit
5. If VERIFY fails, repair (max 3 tries per INV-09), then BLOCKED → HUMAN

## Phase Transition
- A phase is NOT done until L4 VERIFY passes (separate context).
- Update DONE.html §2 gate status to PASS only after VERIFY.
- Update CURRENT.md to reflect the new active phase.
- Commit with message: "P<n>: <outcome> — VERIFIED"
