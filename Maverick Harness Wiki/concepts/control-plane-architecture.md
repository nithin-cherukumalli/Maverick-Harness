---
title: Control Plane Architecture
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [control-plane, architecture, orchestration]
sources: [raw/articles/maverick-vision.md]
confidence: high
---

# Control Plane Architecture

The full flow of the Maverick system.

```
                              HUMAN
                         intent / judgment
                                |
                    +------------------------+
                    |       MAVERICK         |
                    |    CONTROL PLANE       |
                    +----------+-------------+
                               |
             +-----------------+-----------------+
             |                 |                 |
             v                 v                 v
        +---------+       +---------+       +----------+
        | GENESIS |       |  WIKI   |       | MEMORY   |
        | project |       |knowledge|       | / EVENTS |
        |  state  |       |         |       |  context |
        +----+----+       +----+----+       +----+-----+
             |                 |                 |
             +-----------------+-----------------+
                               |
                       CONTEXT PACK
                               |
                       CODING AGENT
                               |
                        CODE CHANGE
                               |
                    +---------------------+
                    |  MAVERICK VERIFY    |
                    |                     |
                    |  tests              |
                    |  protected QA       |
                    |  adversarial QA     |
                    |  mutation testing   |
                    |  evidence checking  |
                    +----------+----------+
                               |
                            VERDICT
                     +-------+----------+
                     v                  v
                  PROVEN            NOT PROVEN
                     |                  |
              Genesis approve     Repair (max 3x)
```

## Components

| Component | Role | Trust Level |
|-----------|------|-------------|
| Human | Intent, judgment, decisions | SOLE DECISION MAKER |
| Maverick | Control plane: orchestrate, verify | TRUSTED |
| [[genesis-system|Genesis]] | Project state | UNMODIFIED (CLI only) |
| Wiki | Knowledge base | Read by context packs |
| Memory/Events | Session context | TBD (P8) |
| [[context-packs|Context Pack]] | Curated 8KB context | Every line sourced |
| [[coding-agent|Agent]] | Implements code | UNTRUSTED |
| [[independent-verification|Verify]] | Tests, mutation, evidence | TRUSTED |

## Flow
1. Human provides intent
2. Maverick orchestrates: pulls from Genesis + Wiki + Memory
3. Context pack is assembled (8KB max, every line sourced)
4. Agent receives context pack + implements code change
5. Verifier independently verifies the change
6. Verdict: VERIFIED (exit 0) -> Genesis approves / NOT PROVEN -> Repair (max 3x)
7. After 3 failures -> BLOCKED -> HUMAN

## Related
- [[maverick-harness]] — the control plane itself
- [[genesis-system]] — project state
- [[context-packs]] — the curated context
- [[independent-verification]] — the verifier
- [[bounded-repair-loop]] — the repair flow
- [[trust-boundaries]] — trust classification
- [[cognitive-job]] — what the system thinks about

## External References
- [ext:clean-architecture/Boundary-Lines] — Maverick is itself a boundary
- [ext:clean-architecture/Dependency-Rule] — dependencies point inward
