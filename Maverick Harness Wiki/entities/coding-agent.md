---
title: Coding Agent
created: 2026-10-07
updated: 2026-10-07
type: entity
tags: [coding-agent, autonomy, trust-boundary]
sources: [raw/articles/maverick-vision.md]
confidence: high
---

# Coding Agent

The entity that Maverick supervises. It implements code but **cannot certify
its own work** (INV-01, see [[agent-self-certification]]).

## The Problem
Coding agents are capable but **stochastic**. They can confidently produce
wrong work and then verify their own implementation, becoming simultaneously:
- Implementer
- Test author
- Test runner
- Judge

This is the core anti-pattern Maverick exists to prevent.

## Trust Classification
Per [[trust-boundaries]]:
- **UNTRUSTED** — cannot certify own work
- Cannot access [[hidden-qa-isolation|hidden QA tests]]
- Ideas are [[proposal-vs-decision|proposals]], not decisions
- Subject to [[bounded-repair-loop|bounded repair]] (max 3 tries)

## What the Agent Can Do
- Implement code changes
- Write tests (but those tests are verified by [[independent-verification|the verifier]])
- Propose ideas, architecture changes, tool additions
- Run within its sandbox

## What the Agent Cannot Do
- Say "done" without verifier VERIFIED (exit 0)
- Edit hidden QA tests
- Make decisions (only propose)
- Introduce dependencies without user approval (see [[stdlib-only-constraint]])
- Repair endlessly (see [[bounded-repair-loop]])

## Related
- [[claude-code]]
- [[human-in-the-loop]] — the agent's autonomy is bounded — the primary coding agent Maverick supervises
- [[agent-self-certification]] — the anti-pattern
- [[trust-boundaries]] — full trust classification
- [[bounded-repair-loop]] — repair limits
