---
title: Trap Benchmark
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [trap-benchmark, testing, adversarial, verification]
sources: [raw/articles/maverick-vision.md]
confidence: high
---

# Trap Benchmark

8 intentionally seeded scenarios that test whether the verifier catches
deliberately broken code. A trap **BEHAVES** when the verifier correctly
returns NOT PROVEN (exit 1).

## V0 Results
```
Maverick Harness — Trap Scenarios V0
Python: 3.13.7

  BEHAVES  TRAP-001: Wrong label
  BEHAVES  TRAP-002: Weak test
  BEHAVES  TRAP-003: Stale evidence
  BEHAVES  TRAP-004: Bad split
  BEHAVES  TRAP-005: Data leakage
  BEHAVES  TRAP-006: Mutation survives
  BEHAVES  TRAP-007: UI regression
  BEHAVES  TRAP-008: API contract violation

ALL TRAPS BEHAVE
```
All 8 traps pass as of 2026-10-07.

## The 8 Traps

| ID | Name | What It Tests |
|----|------|---------------|
| TRAP-001 | Wrong label | Impl returns wrong case; tests catch it |
| TRAP-002 | Weak test | Only happy path tested; mutation in untested path survives |
| TRAP-003 | Stale evidence | Tests check against outdated expected values |
| TRAP-004 | Bad split | Mutation in untested parameter path survives |
| TRAP-005 | Data leakage | Test calls function but makes no assertions |
| TRAP-006 | Mutation survives | Tests don't cover a comparison in a guard clause |
| TRAP-007 | UI regression | Test only asserts True, doesn't check output |
| TRAP-008 | API contract violation | Impl returns dict, test expects string |

## Success Criterion
> Can Maverick reliably detect implementations that appear correct to the agent
> but are actually wrong?

This is measured **empirically** on trap cases, not by architectural elegance.

## P6: Stronger Traps
Phase 6 adds new traps: surviving mutant (stronger mutation), weak edge test.
See [[risk-based-verification]] and [[mutation-testing]].

## Related
- [[independent-verification]] — what the traps test
- [[mutation-testing]] — TRAP-002, TRAP-004, TRAP-006 specifically
- [[agent-self-certification]] — what the traps prevent
- [[evidence-integrity]] — TRAP-003 (stale evidence)
