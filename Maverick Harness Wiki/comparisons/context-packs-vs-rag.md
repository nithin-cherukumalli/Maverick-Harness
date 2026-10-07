---
title: Context Packs vs RAG
created: 2026-10-07
updated: 2026-10-07
type: comparison
tags: [context-engineering, comparison]
sources: [raw/articles/maverick-vision.md]
confidence: medium
---

# Context Packs vs RAG

Two approaches to giving an agent the right context. Maverick uses **context packs**.

## The Difference

| Dimension | [[context-packs|Context Packs]] | Traditional RAG |
|-----------|----------------|-----------------|
| **Compilation** | Compiled once, kept current | Rediscovered from scratch per query |
| **Cross-references** | Already there ([[wikilinks]]) | Reconstructed by retrieval |
| **Contradictions** | Already flagged | May surface contradictory chunks |
| **Synthesis** | Reflects everything ingested | Raw chunks, no synthesis |
| **Size** | 8KB max, every line sourced | Variable, often 50k+ tokens |
| **Source tracking** | Every line has a source ID (INV-10) | Chunk similarity scores |
| **Human curation** | Human marks needed pages | Algorithmic retrieval |
| **Compounding** | Knowledge compounds over time | No memory between queries |

## Why Context Packs?
Based on the [Karpathy LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f):
the wiki compiles knowledge once and keeps it current. Cross-references are
already there. Contradictions have already been flagged. Synthesis reflects
everything ingested.

RAG rediscovers knowledge from scratch per query — it doesn't compound.

## P3: Measuring Pack Quality
10 sample tasks, 8+ must get the pages a human marked as needed.
If packs miss too often, that's measured by [[miss-measurement|P8]] and may
justify a database (INV-06).

## Related
- [[context-packs]] — the Maverick approach
- [[miss-measurement]] — when to add a DB
- [[control-plane-architecture]] — where packs fit
- [[stdlib-only-constraint]] — no vector DB without measured need
