---
title: Traditional Testing vs Independent Verification
created: 2026-10-07
updated: 2026-10-07
type: comparison
tags: [verification, testing, comparison]
sources: [raw/articles/maverick-vision.md]
confidence: high
---

# Traditional Testing vs Independent Verification

## The Difference

| Dimension | Traditional Testing | [[independent-verification|Independent Verification]] |
|-----------|-------------------|---------------------------------------------------|
| **Who writes tests** | Developer (or agent) | Agent writes, but verifier checks meaningfulness |
| **Who runs tests** | Same developer | Separate verifier (outside agent control) |
| **Who judges** | Same developer | Verifier produces binary verdict |
| **Test quality** | Assumed | Checked ([[mutation-testing|mutation testing]]) |
| **Meaningfulness** | Assumed | Checked (AST analysis — no `assert True`) |
| **Evidence** | "Tests passed" | Evidence bundle (SHA, env, timestamp, exit code) |
| **Gaming** | Possible (agent optimizes tests) | Prevented (verifier is independent) |
| **Repair** | Unlimited | [[bounded-repair-loop|Bounded (max 3)]] |

## The Core Insight
"All tests passed" is **evidence**, not **proof**. Traditional testing treats
test passage as proof. Independent verification treats it as one input to a
verdict that also checks test quality, mutation survival, and evidence integrity.

## V0 Verification Levels
1. Tests execute (exit code 0)
2. Tests are meaningful (AST: real assertions, not `assert True`)
3. [[mutation-testing|Mutation detected]] (flip operator, tests must catch it)

Traditional testing only does level 1.

## Related
- [[independent-verification]] — the full mechanism
- [[agent-self-certification]] — why traditional testing fails with agents
- [[mutation-testing]] — the key difference (tests must catch bugs)
- [[trap-benchmark]] — 8 scenarios proving the difference
- [[evidence-integrity]] — what "proof" looks like

## External References
- [ext:clean-architecture/Design-for-Testability-Principle] — tests as first-class
- [ext:llmops-ai-agents/Evaluation-Systems] — evaluation is an architecture
