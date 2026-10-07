---
source_url: file:///Users/nitin/.claude/projects/-Users-nitin/memory/maverick_vision.md
ingested: 2026-10-07
sha256: 3a8a694bc5358abb8ba622fd2df21124d71461f35f7aea08b2849a1728c2bbff
---

---
name: maverick_vision
description: Complete architectural and philosophical vision for Maverick control plane
metadata: 
  node_type: memory
  type: project
  originSessionId: aa1189c4-6e09-40c2-918b-7d111b307791
---

# Maverick: The Complete Vision

## The Core Problem

Coding agents are capable but stochastic. They can confidently produce wrong work and then verify their own implementation, becoming simultaneously:

- Implementer
- Test author
- Test runner
- Judge

**Core invariant:** No coding agent may certify its own implementation.

## The Three Systems

### Genesis
**"What are we building and what constitutes done?"**

Project operating system that manages:
- Requirements (FR, NFR, AC)
- Decisions and their costs
- Invariants (must-hold assertions)
- Tasks with dependencies
- Gates (must pass before next phase)
- Evidence and approvals

**Don't duplicate this in Maverick.** Orchestrate it.

### ci-triage-live
**"How do we learn to reason rigorously about an engineering problem?"**

Methodology laboratory teaching:
- Problem framing before data
- Ground truth validation before training
- Hypothesis before experiment
- Evidence integrity and provenance
- Detection of subtle traps (label columns, data leakage, bad splits)

**Reference implementation, not a framework.**

### Maverick
**"How do we enforce this discipline in an agentic workflow?"**

Control plane with four major responsibilities:

1. **Orchestration** — automated agent lifecycle
2. **Context engineering** — curated context packs, not full dumps
3. **Independent verification** — tests/adversarial/mutation/evidence
4. **Risk-based gates** — verification intensity matches risk level

## The Architecture

```
                              HUMAN
                         intent / judgment
                                │
                    ┌────────────────────┐
                    │      MAVERICK      │
                    │   CONTROL PLANE    │
                    └─────────┬──────────┘
                              │
             ┌────────────────┼─────────────────┐
             │                │                 │
             ▼                ▼                 ▼
        ┌─────────┐      ┌─────────┐      ┌──────────┐
        │ GENESIS │      │   WIKI  │      │ MEMORY   │
        │ project │      │knowledge│      │ / EVENTS │
        │ state   │      │         │      │ context  │
        └────┬────┘      └────┬────┘      └────┬─────┘
             └────────────────┼─────────────────┘
                       CONTEXT PACK
                              │
                       CODING AGENT
                              │
                         CODE CHANGE
                              │
                    ┌───────────────────┐
                    │ MAVERICK VERIFY   │
                    │                   │
                    │ tests             │
                    │ protected QA      │
                    │ adversarial QA    │
                    │ mutation testing  │
                    │ evidence checking │
                    └─────────┬─────────┘
                              │
                           VERDICT
                     ┌────────┴─────────┐
                     ▼                  ▼
                  PROVEN            NOT PROVEN
                     │                  │
              Genesis approve       Repair (max 3x)
```

## Key Concepts

### Context Packs
Instead of dumping 50k tokens into the agent:
- Task
- Affected components
- Relevant requirements
- Relevant decisions
- Relevant invariants
- Relevant prior failures
- Relevant knowledge
- Latest verified state

### Independent Verification Levels

1. **Tests execute** (exit code 0)
2. **Tests are meaningful** (can they detect the bug?)
3. **Implementation survives adversarial cases** (what breaks it?)
4. **Mutations are detected** (tests fail when code deliberately breaks)
5. **Evidence integrity** (SHA, environment, timestamp tied to candidate)

### Trap Benchmark

Test Maverick's effectiveness by intentionally seeding:

- TRAP-001: Wrong label (agent uses 'flaky' not 'IsFlaky')
- TRAP-002: Weak test (only happy path)
- TRAP-003: Stale evidence (tests on wrong build)
- TRAP-004: Bad split (random vs grouped)
- TRAP-005: Data leakage (feature computed from label)
- TRAP-006: Mutation survives (test suite too weak)
- TRAP-007: UI regression (code works but UX broke)
- TRAP-008: API contract violation

**Success:** Maverick catches these reliably.

### Bounded Repair Loop
```
IMPLEMENT → VERIFY → FAIL → REPAIR → VERIFY → FAIL → REPAIR → VERIFY

Maximum: 3 attempts, then BLOCKED → HUMAN
```

This prevents agents from optimizing against the verifier.

### Evidence Integrity
```json
{
  "candidate": "a81f92c",
  "task": "TASK-142",
  "command": "pytest tests/qa",
  "environment": "python-3.13",
  "exit_code": 0,
  "timestamp": "2025-10-06T14:22:33Z",
  "verifier_identity": "maverick-v1.2",
  "result": "PASS"
}
```

Stale evidence example: code compiled against old build, tests run anyway.

## Risk-Based Verification

Not every change needs the nuclear arsenal.

- **Low risk** (README, docs) → basic gates
- **Medium risk** (business logic) → unit, integration, regression, evidence
- **High risk** (auth, payments, security, AI decisions) → full verification, adversarial, mutation, independent model, human approval

## What NOT to Do

- ❌ Build another coding agent (Maverick controls agents)
- ❌ Replace Genesis (it's strong)
- ❌ Create competing task system (use Genesis tasks)
- ❌ Immediately introduce giant distributed memory stack (start: files + SQLite + derived indexes)
- ❌ Blindly use vector search for everything
- ❌ Trust agent-generated tests without verification
- ❌ Call "all tests passed" proof (it's evidence)
- ❌ Let agent endlessly repair itself
- ❌ Measure by architecture impressiveness

## The Experiment-Driven Approach

**NOT:** Design Maverick in abstract, then build it.

**INSTEAD:**

1. Run ci-triage-live with an agent
2. Document exactly where agent fails/games
3. Each failure → Maverick capability

Example:
```
Observed failure: Agent used wrong label column
     ↓
Maverick capability: Ground truth validation gate
     ↓
Implementation: Check label column provenance before training
```

## Success Metric

> **Can Maverick reliably detect implementations that appear correct to the agent but are actually wrong?**

This is measured empirically on trap cases, not by architectural elegance.

## Implementation Roadmap

### v0 (Minimal viable)
```
maverick-harness/
├── verifier/
│   └── verify.py
├── skills/
│   └── independent-verification/
├── trap-project/
└── README.md
```

### v1 (Core capabilities)
```
maverick-harness/
├── core/
│   ├── context-engine/
│   ├── lifecycle/
│   └── risk-engine/
├── verifier/
│   ├── evidence/
│   ├── qa/
│   ├── adversarial/
│   └── mutation/
├── skills/
│   ├── independent-verification/
│   ├── agentic-engineering/
│   └── llm-wiki/
└── ...
```

**Principle:** Earn each directory by having concrete need for it.

## Related Concepts

- **Supermemory research** → context curation
- **Isolated testing** → protected QA
- **Adversarial verification** → mutation testing
- **Evidence integrity** → provenance tracking
- **Hypothesis-driven experiments** → from ci-triage-live
- **Bounded loops** → from safety research
