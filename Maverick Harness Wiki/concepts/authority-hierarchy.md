---
title: Authority Hierarchy
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [trust-boundary, context-engineering, evidence]
sources: [raw/articles/maverick-vision.md]
confidence: high
---

# Authority Hierarchy

Information is treated according to its authority level. Derived context must
never silently become authoritative (INV-11).

## The Four Levels

### AUTHORITATIVE
- Human-approved decisions
- [[genesis-system|Genesis]] specifications
- [[trust-boundaries|Genesis invariants]]
- Approved architecture decisions

Always included in context packs. Never overridden by lower levels.

### OBSERVED
- Current code
- [[evidence-integrity|Verification evidence]]
- Test results
- Recorded failures

Included when relevant. Can be overridden by AUTHORITATIVE.

### KNOWLEDGE
- [[maverick-harness|LLM Wiki / Obsidian]]
- Research
- Patterns
- Lessons

Included when relevant. Must not contradict AUTHORITATIVE or OBSERVED without flagging.

### DERIVED
- Agent summaries
- Inferences
- Recommendations
- Predictions

Labeled as DERIVED. Must never silently become AUTHORITATIVE.

## The Core Rule
> An agent suggestion such as "we should use Redis" is only a [[proposal-vs-decision|proposal]]
> until a human-approved Genesis decision establishes it.

This is exactly [[proposal-vs-decision|INV-05]] expressed at the information level:
the Wiki might say "probably PostgreSQL" but only a Genesis `DEC-017: PostgreSQL`
makes it authoritative.

## Why This Matters for Context Packs
The context engine must label information by authority level so the agent
understands what's a hard constraint vs. a suggestion. Without this:
- The agent treats a Wiki recommendation as a decision
- A derived inference becomes treated as specification
- The agent "follows" advice that was never approved

See [[context-packs]] for how authority labels appear in packs.

## Related
- [[trust-boundaries]] — trust levels for entities
- [[proposal-vs-decision]] — the proposal/decision boundary
- [[context-packs]] — where authority labels appear
- [[context-engineering-principles]] — how authority guides selection
- [[deferred-decisions]] — decisions are deferred until human approval
