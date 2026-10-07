---
title: Miss Measurement (P8)
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [miss-measurement, evidence, process, patterns]
sources: [raw/articles/genesis-project-plan.md]
confidence: high
---

# Miss Measurement (P8)

Log every miss. Add a database **only if misses stay above 20%**.

## INV-06
> No SQLite, graph, embeddings, or memory DB until a measured miss justifies it.

## The Principle
Don't build infrastructure for a problem you haven't measured. Start with
files and derived indexes. Only when the miss rate proves the current approach
is insufficient do you add a database.

## P8: What Gets Measured
- **Context pack misses**: tasks where the pack didn't include the pages a
  human marked as needed (see [[context-packs]], P3)
- **Verification misses**: code that passed verification but was actually wrong
  (caught by [[trap-benchmark|traps]] or human review)
- **Repair overruns**: tasks that hit the 3-try [[bounded-repair-loop|repair cap]]

## The 20% Threshold
If misses stay below 20%, the file-based approach is sufficient.
If misses stay above 20% **after measurement**, a database is justified.

## What "Measured" Means
Per INV-07: any number in a doc must come from a command.
The miss rate is computed by `maverick misses`, not estimated.

## Related
- [[context-packs]] — where misses are most likely to occur
- [[stdlib-only-constraint]] — no DB without measured justification
- [[proposal-vs-decision]] — adding a DB is a decision, not a proposal
- [[independent-verification]] — verification misses are logged

## External References
- [ext:clean-architecture/Database-as-Detail] — the database is a detail
- [ext:clean-architecture/Defer-Decisions-Framework] — defer until measured need
