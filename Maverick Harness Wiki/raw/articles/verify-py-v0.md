---
source_url: file:///Users/nitin/Documents/Maverick Harness/verifier/verify.py
ingested: 2026-10-07
sha256: 900c3aedea176a855b44c51eb9e200cf4e6b0202713178e65de6da2181ba6d5a
---

# verifier/verify.py — V0 Source Code

```python
#!/usr/bin/env python3
"""Maverick Harness — Independent Verifier (V0)

Verifies a code change by:
1. Finding and running the project's tests (unittest, stdlib only)
2. Checking that tests are meaningful (not trivial: no assert True, no empty tests)
3. Running mutation testing (flip a comparison operator, check if tests catch it)
4. Producing a binary verdict: VERIFIED (exit 0) or NOT PROVEN (exit 1)

Standard library only. No external dependencies (INV-03).
"""
import sys
import os
import subprocess
import ast
import json
import datetime
import io
import tokenize


def find_test_files(project_dir):
    """Find all test files (test_*.py or *_test.py) in the project directory."""
    tests = []
    for f in os.listdir(project_dir):
        if f.endswith(".py") and (f.startswith("test_") or f.endswith("_test.py")):
            tests.append(os.path.join(project_dir, f))
    return tests


def find_impl_files(project_dir):
    """Find implementation files (non-test .py files, excluding __init__.py)."""
    impls = []
    for f in os.listdir(project_dir):
        if f.endswith(".py") and not f.startswith("test_") and not f.endswith("_test.py"):
            if f != "__init__.py":
                impls.append(os.path.join(project_dir, f))
    return impls


def run_tests(project_dir):
    """Run tests using unittest discover. Returns (exit_code, output)."""
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover",
         "-s", project_dir, "-p", "test_*.py", "-v"],
        capture_output=True, text=True, cwd=project_dir
    )
    return result.returncode, result.stdout + result.stderr


def has_real_assertions(test_file):
    """Check if a test file has real assertions (not just 'assert True' or empty tests).

    Uses AST to find:
    - assert statements that are not 'assert True'
    - unittest assert methods (assertEqual, assertTrue, assertRaises, etc.)
    """
    with open(test_file) as f:
        source = f.read()
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return False, "Syntax error in test file"

    assert_methods = {
        "assertEqual", "assertNotEqual", "assertTrue", "assertFalse",
        "assertIs", "assertIsNot", "assertIsNone", "assertIsNotNone",
        "assertIn", "assertNotIn", "assertRaises", "assertAlmostEqual",
        "assertNotAlmostEqual", "assertGreater", "assertGreaterEqual",
        "assertLess", "assertLessEqual", "assertRegex", "assertNotRegex",
        "assertIsInstance", "assertNotIsInstance",
    }

    for node in ast.walk(tree):
        # Check for bare 'assert' statements
        if isinstance(node, ast.Assert):
            if isinstance(node.test, ast.Constant) and node.test.value is True:
                continue  # Skip 'assert True'
            return True, "Real assert statement found"
        # Check for unittest assert methods (self.assertEqual, etc.)
        if isinstance(node, ast.Attribute) and hasattr(node, "attr"):
            if node.attr in assert_methods:
                return True, f"Real assertion method: {node.attr}"

    return False, "No real assertions found (tests are empty or trivial)"


def find_first_comparison_operator(source):
    """Find the first comparison operator in source using tokenize."""
    try:
        tokens = list(tokenize.generate_tokens(io.StringIO(source).readline))
    except tokenize.TokenError:
        return None
    for tok in tokens:
        if tok.type == tokenize.OP and tok.string in ("==", "!=", "<", ">", "<=", ">="):
            return tok
    return None


def flip_operator(op):
    """Flip a comparison operator to its opposite."""
    flips = {"==": "!=", "!=": "==", "<": ">=", ">": "<=", "<=": ">", ">=": "<"}
    return flips.get(op, op)


def create_mutation(source):
    """Create a mutated version of source by flipping the first comparison operator.

    Returns the mutated source string, or None if no comparison operator found.
    """
    op_token = find_first_comparison_operator(source)
    if not op_token:
        return None
    flipped = flip_operator(op_token.string)
    lines = source.split("\n")
    line_idx = op_token.start[0] - 1
    col = op_token.start[1]
    line = lines[line_idx]
    new_line = line[:col] + flipped + line[col + len(op_token.string):]
    lines[line_idx] = new_line
    return "\n".join(lines)


def mutation_test(project_dir, impl_files):
    """Run a mutation test: flip the first comparison operator in the first impl file,
    then check if tests still pass.

    Returns (mutation_caught: bool, message: str).
    If mutation_caught is False, the test suite is too weak (mutation survived).
    """
    for impl_file in impl_files:
        with open(impl_file) as f:
            original = f.read()
        mutated = create_mutation(original)
        if not mutated:
            continue  # No comparison operators in this file, try next

        # Write mutated version
        with open(impl_file, "w") as f:
            f.write(mutated)

        # Run tests against mutated code
        exit_code, _ = run_tests(project_dir)

        # Restore original
        with open(impl_file, "w") as f:
            f.write(original)

        if exit_code == 0:
            return False, "Mutation survived (tests did not catch flipped operator)"
        else:
            return True, "Mutation caught by tests"

    # No comparison operators found in any impl file
    return True, "No comparison operators to mutate (skipped)"


def get_git_sha(project_dir):
    """Get the short git SHA of the project, or 'unknown'."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, cwd=project_dir
        )
        return result.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def collect_evidence(project_dir, exit_code, reason):
    """Build an evidence bundle for the verification run."""
    return {
        "candidate": get_git_sha(project_dir),
        "environment": f"python-{sys.version_info.major}.{sys.version_info.minor}",
        "exit_code": exit_code,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "verifier_identity": "maverick-v0",
        "result": "VERIFIED" if exit_code == 0 else "NOT_PROVEN",
        "reason": reason,
    }


def verify(project_dir):
    """Verify a project. Returns exit 0 (VERIFIED) or exit 1 (NOT PROVEN).

    Checks (in order, first failure short-circuits):
    1. Test files exist
    2. Tests pass (unittest)
    3. Tests are meaningful (have real assertions)
    4. Mutation testing (tests catch a flipped operator)
    """
    project_dir = os.path.abspath(project_dir)
    reasons = []

    # Check 1: Tests exist
    test_files = find_test_files(project_dir)
    if not test_files:
        reasons.append("No test files found")
        evidence = collect_evidence(project_dir, 1, "; ".join(reasons))
        print(json.dumps(evidence, indent=2))
        return 1

    # Check 2: Tests pass
    exit_code, output = run_tests(project_dir)
    if exit_code != 0:
        reasons.append("Tests failed")
        evidence = collect_evidence(project_dir, 1, "; ".join(reasons))
        print(json.dumps(evidence, indent=2))
        return 1

    # Check 3: Tests are meaningful
    for test_file in test_files:
        meaningful, msg = has_real_assertions(test_file)
        if not meaningful:
            reasons.append(f"Tests not meaningful: {msg}")
            evidence = collect_evidence(project_dir, 1, "; ".join(reasons))
            print(json.dumps(evidence, indent=2))
            return 1

    # Check 4: Mutation testing
    impl_files = find_impl_files(project_dir)
    caught, msg = mutation_test(project_dir, impl_files)
    if not caught:
        reasons.append(f"Mutation survived: {msg}")
        evidence = collect_evidence(project_dir, 1, "; ".join(reasons))
        print(json.dumps(evidence, indent=2))
        return 1

    # All checks passed
    evidence = collect_evidence(project_dir, 0, "All checks passed")
    print(json.dumps(evidence, indent=2))
    return 0


if __name__ == "__main__":
    project_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    sys.exit(verify(project_dir))

```

## Functions
- `find_test_files(project_dir)` — discover test_*.py and *_test.py files
- `find_impl_files(project_dir)` — discover non-test .py files
- `run_tests(project_dir)` — execute unittest discover, returns (exit_code, output)
- `has_real_assertions(test_file)` — AST analysis: no `assert True`, real assertion methods
- `find_first_comparison_operator(source)` — tokenize: find first `==`, `!=`, `<`, `>`, `<=`, `>=`
- `flip_operator(op)` — flip comparison operator to opposite
- `create_mutation(source)` — produce mutated source with flipped operator
- `mutation_test(project_dir, impl_files)` — flip operator, run tests, check if caught
- `get_git_sha(project_dir)` — get short git SHA or "unknown"
- `collect_evidence(project_dir, exit_code, reason)` — build evidence bundle JSON
- `verify(project_dir)` — main entry: 4 checks, binary verdict

## Imports (stdlib only)
sys, os, subprocess, ast, json, datetime, io, tokenize

No external dependencies. Per [[stdlib-only-constraint]].
