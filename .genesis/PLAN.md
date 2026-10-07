# Maverick Harness — Plan

## Core Rule
No coding agent certifies its own work. Only verifier VERIFIED (exit 0) counts.

## How to Read This Plan
Each phase has one outcome, one demo command (the milestone's contract), a freeze boundary, and assigned skills. A phase is done only when its demo command passes and L4 VERIFY confirms.

---

## P0 — Setup
**Outcome**: Repo initialized as its own git repo, V0 unpacked, traps pass.
**Demo command**: `cd trap-project && python3 run_traps.py` → prints `ALL TRAPS BEHAVE`
**Freeze boundary**: trap-project/ and verifier/ are frozen. No modifications except adding new traps (P6).
**Assigned skills**: genesis, agentic-swe-master
**Done when**: traps pass, git clean (no uncommitted changes), .genesis/ exists and genesis ritual complete.

---

## P1 — CI
**Outcome**: Traps run on every push. Breaking verify.py turns CI red.
**Demo command**: `git push` with a deliberately broken verify.py → CI fails (red)
**Freeze boundary**: .github/workflows/trap-ci.yml is frozen.
**Assigned skills**: production-readiness
**Done when**: CI runs traps on push, breaking verify.py makes CI fail.

---

## P2 — CLI
**Outcome**: `maverick start | verify | status` wrapping Genesis + verify.py only.
**Demo command**: `maverick verify` on toy project → VERIFIED verdict + checkpoint
**Freeze boundary**: CLI interface (start/verify/status subcommands) frozen.
**Assigned skills**: modular-architecture, engineering-mindset
**Done when**: on the toy project, verify gives a verdict and a checkpoint on VERIFIED.

---

## P3 — Context Pack
**Outcome**: One pack (max 8 KB) from Genesis + wiki index + last verdict. Every line shows its source ID.
**Demo command**: `maverick context <task>` → pack with every line sourced
**Freeze boundary**: Context pack format (source ID on every line) frozen.
**Assigned skills**: data-systems-engineering
**Done when**: 10 sample tasks, 8+ get the pages a human marked as needed.

---

## P4 — Write-back
**Outcome**: End-of-session hook saves verdicts and logs agent ideas as proposals.
**Demo command**: Run session with fake "use Redis" suggestion → proposal logged, never a decision
**Freeze boundary**: Proposal/decision separation frozen.
**Assigned skills**: security-engineering
**Done when**: a fake "use Redis" suggestion never becomes a decision.

---

## P5 — Isolation
**Outcome**: Hidden QA moved out of agent's reach, hooks tested in live Claude Code session.
**Demo command**: Agent attempts to edit QA file → blocked in real session
**Freeze boundary**: QA isolation boundary frozen.
**Assigned skills**: security-engineering, production-readiness
**Done when**: agent edits to QA are blocked in a real session.

---

## P6 — Stronger Checks
**Outcome**: Risk levels, mutation testing on risky changed files only, 3-try repair cap.
**Demo command**: `maverick verify --risk high` → mutation testing runs, surviving mutant caught
**Freeze boundary**: Risk level definitions frozen.
**Assigned skills**: llmops-ai-agents, production-readiness
**Done when**: new traps (surviving mutant, weak edge test) caught.

---

## P7 — Wiki
**Outcome**: Init vault, open in Obsidian, ingest notes, lint.
**Demo command**: `maverick wiki ask "What is independent verification?"` → answer with [[page]] citation
**Freeze boundary**: Wiki schema frozen.
**Assigned skills**: data-systems-engineering
**Done when**: 5 questions answered with correct [[page]] citations.

---

## P8 — Measure
**Outcome**: Log every miss. Add a database only if misses stay above 20%.
**Demo command**: `maverick misses` → miss log with count and rate
**Freeze boundary**: Measurement schema frozen.
**Assigned skills**: production-readiness, llmops-ai-agents
**Done when**: miss log exists, DB decision deferred unless misses > 20%.
