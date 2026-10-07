---
title: Wiki Schema
created: 2026-10-07
updated: 2026-10-07
type: schema
---

# Maverick Harness Wiki — Schema

## Domain
Agentic software engineering: independent verification of coding agents,
context engineering, trust boundaries, bounded autonomy, and the control-plane
architecture that enforces discipline in agentic workflows.

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `independent-verification.md`)
- Every wiki page starts with YAML frontmatter (title, created, updated, type, tags, sources)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- Provenance: on pages synthesizing 3+ sources, append `^[raw/articles/source.md]` markers
- Confidence: set `confidence: medium` or `low` for single-source or opinion-heavy claims

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | schema
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
confidence: high | medium | low
contested: true  # optional
---
```

## Tag Taxonomy
- **Core concepts**: verification, trust-boundary, context-engineering, autonomy, evidence
- **Architecture**: control-plane, orchestration, isolation, boundary, dependency
- **Testing**: mutation-testing, trap-benchmark, test-quality, adversarial
- **Process**: bounded-repair, proposal-vs-decision, risk-level, escalation
- **Systems**: genesis, maverick, coding-agent, wiki, memory
- **Patterns**: defer-decisions, stdlib-only, tracer-bullet, single-responsibility
- **Anti-patterns**: self-certification, infinite-repair, premature-abstraction, eval-debt
- **External-ref**: agentic-swe-kit, karpathy-llm-wiki, clean-architecture

Rule: every tag on a page must appear in this taxonomy. Add new tags here first.

## Page Thresholds
- Create a page when a concept appears in 2+ sources OR is central to one source
- Add to existing page when a source mentions something already covered
- DON'T create a page for passing mentions or minor details
- Split a page when it exceeds ~200 lines

## External References
The agentic-swe-kit wiki lives at `~/.agentic-swe-kit/wiki/` with 7 domains:
clean-architecture, designing-data-intensive-applications, distributed-systems,
llmops-ai-agents, pragmatic-programmer, release-it, security-engineering.

Reference these as `[ext:clean-architecture/Boundary-Lines]` in text, and link
to relevant concepts via the `external-refs` section at the bottom of pages.
