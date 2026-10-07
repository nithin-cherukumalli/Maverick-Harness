---
title: Ownership Model
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [architecture, boundary, dependency]
sources: [raw/articles/maverick-vision.md]
confidence: high
---

# Ownership Model

Each system owns exactly one thing. No overlaps. No duplication.

## The Model

| System | Owns | Does NOT Own |
|--------|------|-------------|
| [[genesis-system|Genesis]] | What we're building and project state | Verification, context selection, knowledge |
| [[maverick-harness|LLM Wiki / Obsidian]] | What we've learned | Project state, decisions, verification |
| Codebase | Actual implementation | Project state, knowledge |
| Maverick Context Engine | What info the agent needs right now | Project state, knowledge, decisions, verification |
| Maverick Verifier | Whether the implementation is proven | Project state, context, knowledge, decisions |
| Human | Final authority | (nothing — human is final) |

## The Anti-Pattern: Maverick Becomes Everything
```
Maverick (BAD)
  |-- project manager    <- that's Genesis
  |-- memory system      <- that's the Wiki
  |-- wiki               <- that's the Wiki
  |-- code index         <- that's the codebase
  |-- coding agent       <- that's Claude Code
  |-- planner            <- that's Genesis
  |-- test framework     <- that's the verifier
  |-- verifier           <- correct, but only this
  |-- database           <- not earned yet
  |-- UI                 <- not needed
```

Instead:
```
Genesis     -> project state
Wiki        -> knowledge
Codebase    -> implementation
Maverick    -> selection + verification
Agent       -> implementation
Human       -> authority
```

That is a very clean architecture. Per INV-12: Maverick does not duplicate
Genesis or Wiki. It selects from them.

## Related
- [[architectural-boundary]] — the boundaries between systems
- [[genesis-cli-contract]] — the Genesis boundary
- [[context-engine-selection]] — what the context engine selects vs owns
- [[maverick-vs-genesis]] — complementary, not competing
- [[trust-boundaries]] — trust levels for each system
