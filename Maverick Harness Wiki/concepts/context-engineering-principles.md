---
title: Context Engineering Principles
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [context-engineering, context-packs, evidence, patterns]
sources: [raw/articles/maverick-vision.md]
confidence: high
---

# Context Engineering Principles

The context engine answers: **"What is the minimum sufficient context required
for this agent to make a good decision on this task?"**

It does NOT answer: "How much context can we give the agent?"

## Core Principles

### 1. Minimum Sufficient Context
Goal: minimum sufficient context with maximum relevance and provenance.
Not: maximum context with maximum coverage.

### 2. Select, Don't Store
The context engine [[context-engine-selection|selects from existing sources]]
(Genesis, Wiki, codebase). It does not create a competing store. Per INV-12:
Maverick does not duplicate Genesis or Wiki. It selects from them.

### 3. Authority Labels
Every piece of information in a context pack carries its [[authority-hierarchy|authority level]]:
AUTHORITATIVE, OBSERVED, KNOWLEDGE, or DERIVED. Per INV-11: derived context
must never silently become authoritative.

### 4. Source Tracing
Every item in the pack has a traceable source (INV-10). If the agent asks
"why does this constraint exist?", the answer is a specific Genesis decision
or invariant — not "the wiki said so."

### 5. Token Efficiency
Prefer targeted retrieval over dumping entire files. A larger context window
is not a substitute for better context selection. The goal is:

```
20,000 tokens available
        |
Maverick selects
        |
3,000 relevant tokens
        |
agent
```

### 6. Evaluation Before Infrastructure
The context engine must be evaluated against representative tasks before its
infrastructure is expanded. If file-based + Wiki-based retrieval achieves the
required quality, keep it. If it demonstrably fails, identify the specific
failure and earn the next abstraction.

### 7. No Autonomous Memory
The context engine does not maintain autonomous memory, learning loops, or
self-updating indexes. It reads from [[genesis-system|Genesis]] and
[[maverick-harness|Wiki]] at selection time.

## What the Context Engine Is NOT
- NOT a memory system
- NOT a vector database
- NOT an embedding store
- NOT a replacement for Genesis or Wiki
- NOT a generic knowledge graph
- NOT a giant orchestration framework

It is a **decision layer over existing sources**.

## The Selection Process
```
task
  |
What does Genesis say?
  |
What decisions/invariants govern this?
  |
What does the Wiki know that's relevant?
  |
What code is actually affected?
  |
What recent failures/evidence matter?
  |
RANK
  |
COMPRESS
  |
CONTEXT PACK
```

## Related
- [[context-packs]] — the output format
- [[authority-hierarchy]] — how information is classified
- [[context-packs-vs-rag]] — why packs compound while RAG rediscovers
- [[deferred-decisions]] — earn every abstraction
- [[miss-measurement]] — when to add infrastructure
- [[trust-boundaries]] — the context engine is a SELECTOR, not a store
