---
title: Mutation Testing
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [mutation-testing, testing, verification]
sources: [raw/articles/maverick-vision.md]
confidence: high
---

# Mutation Testing

A technique to measure **test suite quality** — not just whether tests pass,
but whether tests can **detect deliberately introduced bugs**.

## How It Works (V0)
1. Find the first comparison operator (`==`, `!=`, `<`, `>`, `<=`, `>=`) in the
   implementation file using Python's `tokenize` module
2. Flip it to its opposite (`==` to `!=`, `<` to `>=`, etc.)
3. Run the tests against the mutated code
4. If tests **still pass** -> mutation survived -> test suite is too weak
5. If tests **fail** -> mutation caught -> test suite is meaningful

## V0 Limitations
- Only flips the **first** comparison operator (not all operators)
- Only one mutation per run
- P6 will add: risk-based mutation (only on risky changed files), multiple
  mutations, stronger operators

## Trap Scenarios Using Mutation
- [[trap-benchmark|TRAP-002]]: Weak test — mutation in untested path survives
- [[trap-benchmark|TRAP-004]]: Bad split — mutation in untested parameter survives
- [[trap-benchmark|TRAP-006]]: Mutation survives — guard clause not covered

## Standard Library Only
Uses `tokenize` and `ast` from the standard library. No `mutmut` or other
external mutation testing frameworks (see [[stdlib-only-constraint]]).

## Related
- [[independent-verification]]
- [[verification-checks]] — mutation testing is check 4 — mutation testing is check 4
- [[trap-benchmark]] — 3 of 8 traps specifically test mutation detection
- [[risk-based-verification]] — P6 adds risk-based mutation testing
- [[traditional-testing-vs-independent-verification]] — why mutation matters
