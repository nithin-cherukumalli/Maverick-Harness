---
name: independent-verification
description: "Use when verifying code produced by a coding agent. Runs tests, checks meaningfulness, mutation tests. Only verifier VERIFIED (exit 0) counts."
version: 0.0.1
---

# Independent Verification

## Core Rule
No coding agent certifies its own work. Only verifier VERIFIED (exit 0) counts.

## What This Skill Does
- Runs the project's tests (unittest, stdlib only)
- Checks tests are meaningful (not trivial: no `assert True`, no empty tests)
- Runs mutation testing (flips a comparison operator, checks if tests catch it)
- Produces a binary verdict: VERIFIED (exit 0) or NOT PROVEN (exit 1)

## How to Use
```bash
python3 verifier/verify.py <project_dir>
```

## Verdicts
- **VERIFIED** (exit 0): Tests exist, pass, are meaningful, and catch mutations.
- **NOT PROVEN** (exit 1): One or more checks failed. See evidence bundle in stdout.

## What It Does NOT Do (Yet)
- Risk-based verification levels (P6)
- Adversarial test generation (P6)
- Evidence integrity with SHA + timestamp (partial in V0)
- Hidden QA isolation (P5)
- Context packs (P3)

## Invariants Enforced
- INV-01: No agent self-certification (verifier is independent)
- INV-03: Standard library only
- INV-09: Bounded repair (3-try cap comes in P6)
