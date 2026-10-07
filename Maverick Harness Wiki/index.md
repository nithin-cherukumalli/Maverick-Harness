---
title: Wiki Index
created: 2026-10-07
updated: 2026-10-07
type: schema
tags: [schema]
---

# Maverick Harness Wiki — Index

> Content catalog. Every wiki page listed under its type with a one-line summary.
> Read this first to find relevant pages for any query.
> Last updated: 2026-10-07 | Total pages: 20

## Entities
- [[maverick-harness]] — The control-plane product: supervises coding agents with independent verification
- [[genesis-system]] — Project state OS: requirements, decisions, invariants, tasks, gates
- [[coding-agent]] — The supervised entity: implements code but cannot certify own work
- [[claude-code]] — The primary coding agent Maverick supervises (installed in ~/.claude)

## Concepts
- [[independent-verification]] — Only verifier VERIFIED (exit 0) counts; no agent self-certification
- [[bounded-repair-loop]] — Max 3 repair attempts, then BLOCKED to HUMAN
- [[context-packs]] — Curated max 8KB context with source IDs, not full dumps
- [[trust-boundaries]] — Who is trusted for what: agent UNTRUSTED, verifier TRUSTED, human SOLE DECIDER
- [[trap-benchmark]] — 8 seeded scenarios testing if the verifier catches intentionally broken code
- [[mutation-testing]] — Flip a comparison operator; if tests still pass, suite is too weak
- [[evidence-integrity]] — SHA, environment, timestamp, exit code tied to each verification candidate
- [[risk-based-verification]] — Low/medium/high risk determines verification intensity
- [[proposal-vs-decision]] — Agent ideas are "proposal"; only the human makes a "decision"
- [[hidden-qa-isolation]] — QA tests outside the agent's reach; agent cannot edit them
- [[agent-self-certification]] — The core anti-pattern: agent as implementer + test author + judge
- [[cognitive-job]] — What thinking the system performs: deterministic verification, no LLM reasoning
- [[genesis-cli-contract]] — Genesis is unmodified; talk to it only through its CLI; pin its version
- [[stdlib-only-constraint]] — No external dependencies without a user decision
- [[miss-measurement]] — Log every miss; add a DB only if misses stay above 20%
- [[control-plane-architecture]] — Human -> Maverick -> {Genesis, Wiki, Memory} -> Context Pack -> Agent -> Verify

## Comparisons
- [[maverick-vs-genesis]] — Maverick verifies + contexts; Genesis tracks state; complementary not competing
- [[context-packs-vs-rag]] — Wiki compiles once and compounds; RAG rediscovers per query
- [[traditional-testing-vs-independent-verification]] — Agent-authored tests vs external verifier

## External References
- [ext:clean-architecture/Boundary-Lines] — Architectural boundaries, trust boundaries
- [ext:clean-architecture/Design-for-Testability-Principle] — Tests as first-class citizens
- [ext:clean-architecture/Defer-Decisions-Framework] — Defer DB/framework decisions
- [ext:clean-architecture/Database-as-Detail] — The database is a detail
- [ext:security-engineering] — Threat modeling, least privilege, defense in depth
- [ext:llmops-ai-agents] — Agent architecture, evaluation, bounded loops
- [ext:pragmatic-programmer] — DRY, orthogonality, tracer bullets
