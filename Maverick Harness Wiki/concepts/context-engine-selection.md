---
title: Context Engine Selection Model
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [context-engineering, architecture, dependency]
sources: [raw/articles/maverick-vision.md]
confidence: high
---

# Context Engine Selection Model

The context engine selects from existing sources. It does not own them.

## What It Selects From

| Source | What It Provides | Authority Level |
|--------|-----------------|-----------------|
| [[genesis-system|Genesis]] | Specs, tasks, decisions, invariants, gates | AUTHORITATIVE |
| [[genesis-system|Genesis]] | Current state, active milestone | OBSERVED |
| [[maverick-harness|LLM Wiki / Obsidian]] | Patterns, lessons, research | KNOWLEDGE |
| Codebase | Relevant files, symbols, structure | OBSERVED |
| Verification evidence | Previous failures, verdicts, repair history | OBSERVED |
| Agent proposals | Suggestions, recommendations | DERIVED |

## What It Produces
A [[context-packs|Context Pack]]: a small, structured, traceable artifact containing
exactly what the agent needs for the current task.

## The Selection Algorithm (P3)
P3 will implement the actual selection. The initial algorithm should be simple:
1. Read the task description
2. Extract key terms and affected components
3. From Genesis: fetch relevant specs, decisions, invariants
4. From Wiki: fetch relevant knowledge pages
5. From codebase: identify relevant files and symbols
6. From evidence: surface relevant failures
7. Rank by relevance and authority
8. Compress to fit within 8KB
9. Add source IDs to every line

If 8+ of 10 sample tasks get the right pages, the algorithm is good enough.
If not, measure the misses and improve — don't add infrastructure.

## What Selection Does NOT Do
- It does not store new knowledge (that's the Wiki)
- It does not track project state (that's Genesis)
- It does not make decisions (that's the human)
- It does not verify code (that's the verifier)

It selects. That's its entire job.

## Related
- [[context-engineering-principles]] — the principles guiding selection
- [[context-packs]] — the output format
- [[authority-hierarchy]] — how sources are classified
- [[deferred-decisions]] — earn every abstraction
- [[miss-measurement]] — when to add infrastructure
