---
title: Standard Library Only (INV-03)
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [stdlib-only, patterns, dependency, process]
sources: [raw/articles/genesis-project-plan.md]
confidence: high
---

# Standard Library Only (INV-03)

No external dependencies without a user decision.

## Why?
- **Portability**: stdlib-only code runs anywhere Python runs
- **Security**: no supply chain attacks from third-party packages
- **Simplicity**: no dependency management, no version conflicts
- **Control**: every dependency is a conscious decision, not an accident

## What This Means in Practice
- `verify.py` uses `unittest`, `ast`, `tokenize`, `subprocess`, `json` — all stdlib
- No `pytest`, `mutmut`, `requests`, or any pip installs
- No `requirements.txt` needed
- The verifier can be copied to any machine with Python 3 and run

## When Dependencies Are Allowed
Only when the user makes a **decision** (not a [[proposal-vs-decision|proposal]]):
- A measured miss justifies a database (see [[miss-measurement]], INV-06)
- A specific capability cannot be achieved with stdlib
- The user explicitly approves the dependency

## Related
- [[proposal-vs-decision]] — dependencies require a decision
- [[miss-measurement]] — DB requires measured misses > 20%
- [[independent-verification]] — verifier is stdlib-only
- [[maverick-harness]] — the whole harness is stdlib-only

## External References
- [ext:clean-architecture/Database-as-Detail] — the database is a detail
- [ext:clean-architecture/Defer-Decisions-Framework] — defer framework decisions
