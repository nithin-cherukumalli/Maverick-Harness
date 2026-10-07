---
title: Verification Checks (V0)
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [verification, testing, evidence]
sources: [raw/articles/verify-py-v0.md]
confidence: high
---

# Verification Checks (V0)

The four checks that `verify.py` runs in order. First failure short-circuits.

## Check 1: Tests Exist
- Scans project directory for `test_*.py` or `*_test.py` files
- If none found: NOT PROVEN ("No test files found")
- Function: `find_test_files(project_dir)`

## Check 2: Tests Pass
- Runs `python -m unittest discover -s <dir> -p "test_*.py" -v`
- If exit code non-zero: NOT PROVEN ("Tests failed")
- Function: `run_tests(project_dir)`

## Check 3: Tests Are Meaningful
- AST analysis of each test file
- Looks for: `assert` statements (not `assert True`), unittest assertion methods
  (`assertEqual`, `assertTrue`, `assertRaises`, etc.)
- If only trivial assertions: NOT PROVEN ("Tests not meaningful")
- Function: `has_real_assertions(test_file)`

This catches [[trap-benchmark|TRAP-005]] (data leakage: no assertions) and
[[trap-benchmark|TRAP-007]] (UI regression: only `assert True`).

## Check 4: Mutation Testing
- Tokenizes the first implementation file
- Finds the first comparison operator (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Flips it to its opposite (e.g., `==` to `!=`)
- Runs tests against mutated code
- If tests still pass: NOT PROVEN ("Mutation survived")
- Restores original code after test
- Function: `mutation_test(project_dir, impl_files)`

This catches [[trap-benchmark|TRAP-002]] (weak test), TRAP-004 (bad split),
and TRAP-006 (mutation survives).

## Short-Circuit Behavior
Checks run in order. First failure produces an evidence bundle and exits.
Only if all four checks pass does the verifier return VERIFIED (exit 0).

## Related
- [[independent-verification]] — the overall mechanism
- [[mutation-testing]] — check 4 in detail
- [[trap-benchmark]] — the 8 scenarios testing these checks
- [[evidence-integrity]] — the output of each check
- [[risk-based-verification]] — future: more checks for high-risk changes
