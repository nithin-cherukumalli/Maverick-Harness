---
title: Evidence Integrity
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [evidence, verification, trust-boundary]
sources: [raw/articles/maverick-vision.md]
confidence: high
---

# Evidence Integrity

Each verification run produces an **evidence bundle** that ties the verdict
to the specific code candidate, environment, and timestamp.

## Evidence Bundle (V0)
```json
{
  "candidate": "a81f92c",
  "environment": "python-3.13",
  "exit_code": 0,
  "timestamp": "2026-10-07T14:47:36Z",
  "verifier_identity": "maverick-v0",
  "result": "VERIFIED",
  "reason": "All checks passed"
}
```

## Stale Evidence Problem
TRAP-003 tests for stale evidence: tests run against the wrong build but
report success. The evidence bundle's `candidate` field (git SHA) and
`timestamp` make stale evidence detectable.

## P6: Full Evidence Integrity
- SHA of the code candidate (not just git SHA)
- Environment fingerprint (Python version, OS, dependencies)
- Timestamp with timezone
- Verifier identity and version
- Full test output attached

## Related
- [[independent-verification]] — evidence is the output of verification
- [[trap-benchmark|TRAP-003]] — stale evidence trap
- [[trust-boundaries]] — evidence is produced by the TRUSTED verifier
- [[bounded-repair-loop]] — each repair attempt gets its own evidence bundle
