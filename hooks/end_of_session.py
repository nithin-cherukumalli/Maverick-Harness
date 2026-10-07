#!/usr/bin/env python3
"""Record a safe local handoff when an agent session ends.

Genesis remains the authority for phase state, verification, and human
decisions. This hook only maintains local context under ``.maverick/``.
"""
import argparse
import datetime
import json
import subprocess
import sys
from pathlib import Path


def utc_now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def project_path(value):
    return Path(value).resolve()


def run_text(command, cwd):
    try:
        result = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
    except OSError:
        return "unknown"
    if result.returncode == 0 and result.stdout.strip():
        return result.stdout.strip()
    return "unknown"


def git_snapshot(project_dir):
    return {
        "head": run_text(["git", "rev-parse", "--short", "HEAD"], project_dir),
        "changed_files": run_text(["git", "status", "--short"], project_dir),
    }


def active_phase(project_dir):
    current = project_dir / ".genesis" / "CURRENT.md"
    if not current.exists():
        return "unknown"
    for line in current.read_text(encoding="utf-8").splitlines():
        if line.startswith("**Active phase**:"):
            return line.split(":", 1)[1].strip()
    return "unknown"


def runtime_dir(project_dir):
    directory = project_dir / ".maverick"
    directory.mkdir(exist_ok=True)
    return directory


def build_event(project_dir, agent, status, summary="", changed_files=None,
                wiki_pages=None, proposals=None, session_id=None, reason=None):
    return {
        "timestamp": utc_now(),
        "agent": agent,
        "status": status,
        "summary": summary.strip(),
        "changed_files": changed_files or [],
        "wiki_pages": wiki_pages or [],
        "proposals": proposals or [],
        "session_id": session_id,
        "reason": reason,
        "active_phase": active_phase(project_dir),
        "git": git_snapshot(project_dir),
    }


def append_history(project_dir, event):
    path = runtime_dir(project_dir) / "session-history.jsonl"
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, sort_keys=True) + "\n")


def render_context(event):
    lines = [
        "# Local Agent Context",
        "",
        "> Local runtime handoff. Genesis remains the source of truth for phase status and gates.",
        "",
        "## Latest Session",
        f"- Timestamp: {event['timestamp']}",
        f"- Agent: {event['agent']}",
        f"- Status: {event['status']}",
        f"- Genesis active phase: {event['active_phase']}",
        f"- Git HEAD: {event['git']['head']}",
        f"- Changed files at write-back: {event['git']['changed_files'] or 'none'}",
    ]
    if event.get("summary"):
        lines.extend(["", "## Factual Handoff", event["summary"]])
    if event.get("changed_files"):
        lines.extend(["", "## Files Reported by Agent"])
        lines.extend(f"- `{path}`" for path in event["changed_files"])
    if event.get("wiki_pages"):
        lines.extend(["", "## Wiki Pages Consulted"])
        lines.extend(f"- [[{page}]]" for page in event["wiki_pages"])
    if event.get("proposals"):
        lines.extend(["", "## Proposals — Require Human Decision"])
        lines.extend(f"- {proposal}" for proposal in event["proposals"])
    return "\n".join(lines) + "\n"


def write_context(project_dir, event):
    path = runtime_dir(project_dir) / "context.md"
    path.write_text(render_context(event), encoding="utf-8")
    return path


def record(args):
    project_dir = project_path(args.project_dir)
    event = build_event(
        project_dir, args.agent, args.status, args.summary, args.changed_file,
        args.wiki_page, args.proposal, args.session_id,
    )
    append_history(project_dir, event)
    print(f"Local session context written to {write_context(project_dir, event)}")
    return 0


def record_claude_event(args):
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        print("Expected Claude Code SessionEnd JSON on stdin", file=sys.stderr)
        return 2
    project_dir = project_path(payload.get("cwd") or args.project_dir)
    event = build_event(
        project_dir, "claude-code", "session_ended",
        session_id=payload.get("session_id"), reason=payload.get("reason"),
    )
    append_history(project_dir, event)
    write_context(project_dir, event)
    return 0


def save_verdict(project_dir, verdict):
    """Save a verifier result for compatibility with the original hook API."""
    path = runtime_dir(project_path(project_dir)) / "last_verdict.json"
    path.write_text(json.dumps(verdict, indent=2) + "\n", encoding="utf-8")
    print(f"Verdict saved to {path}")


def log_proposal(project_dir, idea_text):
    """Log an agent idea as a proposal, never as a decision."""
    path = runtime_dir(project_path(project_dir)) / "proposals.log"
    with path.open("a", encoding="utf-8") as handle:
        handle.write(f"[{utc_now()}] PROPOSAL: {idea_text}\n")
    print("Proposal logged (NOT a decision — human must approve)")


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-dir", default=".")
    parser.add_argument("--from-claude-stdin", action="store_true")
    commands = parser.add_subparsers(dest="command")

    manual = commands.add_parser("record", help="record a factual agent handoff")
    manual.add_argument("--agent", required=True)
    manual.add_argument("--status", required=True, choices=("completed", "blocked", "no_change"))
    manual.add_argument("--summary", required=True)
    manual.add_argument("--changed-file", action="append", default=[])
    manual.add_argument("--wiki-page", action="append", default=[])
    manual.add_argument("--proposal", action="append", default=[])
    manual.add_argument("--session-id")

    return parser.parse_args()


def main():
    args = parse_args()
    if args.from_claude_stdin:
        return record_claude_event(args)
    if args.command == "record":
        return record(args)
    print("Use 'record' or --from-claude-stdin", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
