# Maverick Harness — Agent Working Contract

This is the shared contract for coding agents in this repository. It complements, but never replaces, the Genesis state spine.

## Start every task

1. Read `.genesis/KICKOFF.md`, then its required state files: `.genesis/CURRENT.md`, `.genesis/context-graph.json`, `.genesis/PLAN.md`, and `.genesis/LOOPS.md`.
2. Treat `CURRENT.md` and `PLAN.md` as the source of truth for the active phase and next action; do not infer status from a roadmap or wiki page.
3. Read `Maverick Harness Wiki/index.md`, then retrieve only the pages relevant to the task.
4. If `.maverick/context.md` exists, read it as a recent-session handoff. It is helpful context, not an authority over Genesis or the user.

## During the task

- Obey all invariants in `.genesis/context-graph.json`.
- Do not modify `.genesis/` during ordinary implementation. Update it only through the project workflow after the required verification.
- Keep proposals distinct from decisions. Only the human makes decisions.
- Verify changes with the demo command for the active phase and preserve the independent-verification boundary.

## End every task

Before the final response, write a concise factual handoff: what changed or was verified; outcome (`completed`, `blocked`, or `no_change`); important files and wiki pages; and any proposal (never a decision).

Run the shared write-back hook:

```bash
python3 hooks/end_of_session.py record \
  --agent <agent-name> \
  --status <completed|blocked|no_change> \
  --summary "<factual handoff>" \
  --changed-file <path> \
  --wiki-page <page-slug>
```

The hook writes local, machine-readable session context under `.maverick/`. It must not edit `.genesis/`, declare a human decision, or claim a phase is verified without the required independent-verification evidence.

## Context precedence

1. User direction
2. `.genesis/` current state, invariants, and gates
3. Verified implementation and command output
4. Wiki design knowledge
5. `.maverick/` recent-session handoff
