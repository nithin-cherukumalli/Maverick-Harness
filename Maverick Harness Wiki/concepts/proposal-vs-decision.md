---
title: Proposal vs Decision
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [proposal-vs-decision, autonomy, trust-boundary, process]
sources: [raw/articles/maverick-vision.md, raw/articles/genesis-project-plan.md]
confidence: high
---

# Proposal vs Decision

Agent ideas are **proposals**. Only the human makes a **decision**.

This is INV-05, one of the core [[trust-boundaries|trust boundaries]].

## The Distinction
- **Proposal**: an agent suggests an architecture change, tool addition, or
  dependency. Logged but not enacted.
- **Decision**: a human reviews the proposal and explicitly approves or rejects.
  Only decisions change the project's direction.

## P4: Write-back Hook
The end-of-session hook (P4) enforces this:
1. Saves verdicts to `.maverick/last_verdict.json`
2. Logs agent ideas as `PROPOSAL:` in `.maverick/proposals.log`
3. A fake "use Redis" suggestion must **never** become a decision

## P4 Done Condition
> A fake "use Redis" suggestion never becomes a decision.

## Why This Matters
Without this boundary, agents can:
- Introduce dependencies without approval (violates [[stdlib-only-constraint]])
- Change architecture direction silently
- Accumulate technical debt through "helpful" suggestions

## Related
- [[trust-boundaries]] — human is SOLE DECISION MAKER
- [[coding-agent]] — the entity whose ideas are proposals
- [[stdlib-only-constraint]] — dependencies require a decision
- [[miss-measurement]] — adding a DB requires a decision backed by measured misses
- [[genesis-system]] — where decisions are tracked

## External References
- [ext:llmops-ai-agents] — human-in-the-loop is an architecture decision
