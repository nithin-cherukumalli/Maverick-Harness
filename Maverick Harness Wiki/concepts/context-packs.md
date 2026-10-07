---
title: Context Packs
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [context-engineering, context-packs, evidence]
sources: [raw/articles/maverick-vision.md, raw/articles/genesis-project-plan.md]
confidence: high
---

# Context Packs

Instead of dumping 50k tokens into a coding agent, Maverick curates a
**context pack** — maximum 8 KB — containing exactly what the agent needs.

## Pack Contents
- Task description
- Affected components
- Relevant requirements (from [[genesis-system]])
- Relevant decisions
- Relevant [[trust-boundaries|invariants]]
- Relevant prior failures
- Relevant knowledge (from this wiki)
- Latest verified state

## Source IDs (INV-10)
Every line in a context pack shows its **source ID**. This is invariant INV-10:
> Every context pack line shows its source ID.

Sources include: `genesis:PLAN.md`, `genesis:context-graph.json#INV-01`,
`wiki:[[independent-verification]]`, `verifier:last_verdict.json`.

## P3 Done Condition
10 sample tasks, 8+ get the pages a human marked as needed.
This is measured empirically — not by architectural elegance.

## Related
- [[context-packs-vs-rag]] — why packs compound while RAG rediscovers
- [[control-plane-architecture]] — where context packs fit in the flow
- [[miss-measurement]] — if packs miss too often, add a DB (P8)
- [[genesis-system]] — source of requirements, decisions, invariants

## External References
- [ext:clean-architecture/Defer-Decisions-Framework] — defer DB until measured need
