---
title: Claude Code
created: 2026-10-07
updated: 2026-10-07
type: entity
tags: [claude-code, coding-agent, maverick]
sources: [raw/articles/maverick-vision.md, raw/articles/genesis-project-plan.md]
confidence: medium
---

# Claude Code

The primary coding agent that Maverick supervises. Maverick Harness installs
into `~/.claude` to integrate with Claude Code's hook system.

## Integration Points
- **Hooks**: end-of-session hooks (P4) save verdicts and log proposals
- **Skills**: Claude Code skills (like `independent-verification`) teach the
  agent about verification awareness
- **Settings**: `.claude/settings.local.json` configures the integration

## P5: Live Session Testing
Phase 5 tests hooks in a **live Claude Code session** — verifying that agent
edits to hidden QA are actually blocked in a real session, not just in theory.

## Related
- [[coding-agent]] — the general concept
- [[hidden-qa-isolation]] — what P5 tests
- [[proposal-vs-decision]] — how agent ideas are logged
