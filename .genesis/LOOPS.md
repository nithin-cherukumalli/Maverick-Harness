# Maverick Harness — Loop Definitions

Loops prompt the agent, not the human. Read CURRENT.md before running any loop.

---

## L0 — Pre-Flight (run before any session)

**Takes 1 minute. Never skip.**

```bash
# 1. Read current state
cat .genesis/CURRENT.md

# 2. Check git is clean
git status --porcelain  # should be empty (or only .genesis/CURRENT.md)

# 3. Verify traps still pass
cd trap-project && python3 run_traps.py  # should print ALL TRAPS BEHAVE

# 4. Check invariants
grep -r "self.certif" verifier/  # should return nothing (no self-certification)
```

**Exit condition**: Traps pass, git clean → proceed to L1.

---

## L1 — BUILD (implement the current phase)

**Entry**: L0 passed, phase identified from PLAN.md

**Steps**:
1. Read the phase's outcome and freeze boundary from PLAN.md
2. Check context-graph.json for relevant invariants
3. Identify the specific files to change
4. Write the code change (standard library only, one function before a class)
5. Run the phase's demo command

**Hard rules during BUILD**:
- No coding agent certifies its own work (INV-01)
- No external dependencies without user decision (INV-03)
- No config without a user (INV-05)
- No SQLite/graph/embeddings until measured miss (INV-06)
- Agent ideas are "proposal", not "decision" (INV-05)

**Exit condition**: Demo command passes → proceed to L3.

---

## L3 — REVIEW (after any code change)

**Steps**:
1. Check diff for any self-certification logic (agent judging its own work)
2. Check diff for any external dependencies added without user decision
3. Check diff for any config/decision made without user (should be "proposal")
4. Check diff for any database/embeddings added without measured miss
5. Verify every number in docs comes from a command (INV-07)

**Exit condition**: No violations → proceed to L4.

---

## L4 — VERIFY (separate context, not the same agent that built it)

**The maker does not grade its own work.**

In Hermes, this runs as a delegate_task subagent with:
- Isolated context (no BUILD conversation history)
- Instructions: check DONE.html gates for the current phase only
- Binary verdict: PASS or FAIL

**Gate questions (per phase)**:
- P0: Do traps pass? Is git clean? Does .genesis/ exist?
- P1: Does breaking verify.py turn CI red?
- P2: Does `maverick verify` give a verdict and checkpoint on VERIFIED?
- P3: Do 8+ of 10 sample tasks get the right pages?
- P4: Does a fake "use Redis" suggestion stay a proposal, not a decision?
- P5: Are agent edits to QA blocked in a real session?
- P6: Are new traps (surviving mutant, weak edge test) caught?
- P7: Are 5 questions answered with correct [[page]] citations?
- P8: Does the miss log exist? Is DB deferred unless misses > 20%?

**Exit condition**: All gates pass → update CURRENT.md, commit, move to next phase.
If gates fail → repair (max 3 tries per INV-09), then BLOCKED → HUMAN.
