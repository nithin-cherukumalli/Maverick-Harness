#!/usr/bin/env python3
"""Maverick Harness — End-of-Session Hook (V0 stub)

When a coding agent session ends, this hook:
1. Saves the last verdict (if any) to .maverick/last_verdict.json
2. Logs any agent ideas as "proposal" (never "decision")

This is a stub — full implementation in P4.

Standard library only (INV-03).
"""
import sys
import os
import json
import datetime


def save_verdict(project_dir, verdict):
    """Save the last verdict to .maverick/last_verdict.json."""
    maverick_dir = os.path.join(project_dir, ".maverick")
    os.makedirs(maverick_dir, exist_ok=True)
    path = os.path.join(maverick_dir, "last_verdict.json")
    with open(path, "w") as f:
        json.dump(verdict, f, indent=2)
    print(f"Verdict saved to {path}")


def log_proposal(project_dir, idea_text):
    """Log an agent idea as a 'proposal' (never a 'decision').

    Per INV-05: Agent ideas are "proposal". Only the human makes a "decision".
    """
    maverick_dir = os.path.join(project_dir, ".maverick")
    os.makedirs(maverick_dir, exist_ok=True)
    path = os.path.join(maverick_dir, "proposals.log")
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(path, "a") as f:
        f.write(f"[{timestamp}] PROPOSAL: {idea_text}\n")
    print(f"Proposal logged (NOT a decision — human must approve)")


if __name__ == "__main__":
    # Stub: just print status
    print("Maverick end-of-session hook (V0 stub)")
    print("Full implementation in P4")
