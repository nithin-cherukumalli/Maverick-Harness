---
title: Deferred Decisions
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [defer-decisions, patterns, architecture, dependency]
sources: [raw/articles/maverick-vision.md, raw/articles/genesis-project-plan.md]
confidence: high
---

# Deferred Decisions

Shape the system so that the choice of database, web framework, deployment
mechanism, and other details can be postponed until maximum information is
available.

## The Core Heuristic
> The longer you wait to make those decisions, the more information you have
> with which to make them properly.

## How Maverick Defers Decisions
- **No database until measured miss** (INV-06, see [[miss-measurement]]) — the
  system works with files and derived indexes until the miss rate proves otherwise
- **No external dependencies** (INV-03, see [[stdlib-only-constraint]]) — every
  dependency is a decision, not an accident
- **No config without a user** — configurations are deferred until someone
  explicitly needs them
- **Agent ideas are proposals** (INV-05, see [[proposal-vs-decision]]) —
  architectural suggestions are deferred until the human decides

## The Anti-Pattern: Premature Commitment
- Choosing SQLite before measuring miss rates
- Adding vector search before proving [[context-packs|context packs]] fail
- Adopting a framework before domain logic is stable
- Letting the agent make architectural decisions

## Related
- [[miss-measurement]] — the decision gate for databases
- [[stdlib-only-constraint]] — the decision gate for dependencies
- [[proposal-vs-decision]] — the decision gate for agent ideas
- [[context-packs-vs-rag]] — why RAG is premature for Maverick
- [[architectural-boundary]] — keeping details on the outside

## External References
- [ext:clean-architecture/Defer-Decisions-Framework] — defer until maximum info
- [ext:clean-architecture/Database-as-Detail] — the database is a detail
