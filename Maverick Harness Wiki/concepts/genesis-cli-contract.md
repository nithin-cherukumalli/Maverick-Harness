---
title: Genesis CLI Contract (INV-08)
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [genesis, dependency, boundary, process]
sources: [raw/articles/genesis-project-plan.md]
confidence: high
---

# Genesis CLI Contract (INV-08)

Genesis stays **unmodified**. Maverick talks to it **only through its CLI**.
Genesis version is **pinned**.

## Why?
- Genesis is a **strong, independent system** for project state management
- Duplicating its functionality in Maverick creates competing systems
- Modifying Genesis internals creates a fork that won't track upstream
- Direct file access bypasses Genesis's own invariants and gates

## The Contract
1. **Read-only access** to `.genesis/` files during BUILD (CURRENT.md is the
   only file updated, and only after a phase transition)
2. **CLI calls** for any state operations (query tasks, update gates, etc.)
3. **Version pinning** — Genesis version recorded in `context-graph.json`
   as `genesis_version: "pinned-1.0.0"`

## What Maverick Does NOT Do
- Edit `.genesis/DONE.html` mid-loop (it's locked)
- Modify `.genesis/context-graph.json` (read-only)
- Create competing task systems
- Bypass Genesis gates

## Related
- [[genesis-system]] — the system being contracted with
- [[maverick-vs-genesis]] — why they're complementary
- [[trust-boundaries]] — Genesis is UNMODIFIED
- [[control-plane-architecture]] — Genesis in the flow
