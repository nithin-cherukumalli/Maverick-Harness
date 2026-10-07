# Agent Adapters — Hermes

## Loop Primitives → Hermes Mapping

| Genesis Primitive | Hermes Implementation |
|---|---|
| L0 Pre-Flight | terminal: run pre-flight bash checks |
| L1 BUILD | terminal + write_file + patch: implement code |
| L3 REVIEW | terminal: git diff; search_files: check violations |
| L4 VERIFY | delegate_task: separate subagent verifies (isolated context) |
| KICKOFF.md prompts | Loaded at session start; read .genesis/KICKOFF.md |

## Skill Resolution

| Skill Call | Hermes Command |
|---|---|
| agentic-swe-master | skill_view(name='agentic-swe-master') |
| genesis | skill_view(name='genesis') |
| engineering-mindset | skill_view(name='engineering-mindset') |
| production-readiness | skill_view(name='production-readiness') |
| security-engineering | skill_view(name='security-engineering') |
| modular-architecture | skill_view(name='modular-architecture') |
| data-systems-engineering | skill_view(name='data-systems-engineering') |
| llmops-ai-agents | skill_view(name='llmops-ai-agents') |

## L4 VERIFY — Separate Verifier

Per genesis rule: "the maker does not grade its own work."

In Hermes, L4 VERIFY runs as a delegate_task subagent with:
- Isolated context (no conversation history from BUILD)
- Instructions to check DONE.html gates for the current phase only
- Binary verdict: PASS or FAIL
- On FAIL: repair instructions sent back, max 3 retries (INV-09)

## Genesis CLI

Genesis is talked to ONLY through its CLI (INV-08). In Hermes:
- .genesis/ files are read-only during BUILD (do not modify mid-loop)
- CURRENT.md is the only file updated after a phase transition
- DONE.html is locked — change scope via the user, not silently
