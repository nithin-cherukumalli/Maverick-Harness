---
source_url: file:///Users/nitin/Documents/Maverick Harness/trap-project/run_traps.py
ingested: 2026-10-07
sha256: 215470b350c120ad8e1cc793cd756a1d92764d445c23c9b87a9d8c9b57e85ee2
---

# trap-project/run_traps.py — V0 Source Code

```python
#!/usr/bin/env python3
"""Maverick Harness — Trap Scenarios (V0)

Runs 8 trap scenarios against verify.py. Each trap has a deliberately broken
implementation. A trap "BEHAVES" when verify.py correctly returns NOT PROVEN
(exit 1) — meaning the verifier caught the bug.

Success criterion: prints "ALL TRAPS BEHAVE" when all 8 traps are caught.

Standard library only (INV-03).
"""
import sys
import os
import subprocess
import tempfile
import textwrap

# Resolve verify.py path relative to this file
VERIFY_SCRIPT = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "verifier", "verify.py")
)


def create_project(impl_source, test_source):
    """Create a temporary project directory with impl.py and test_impl.py."""
    tmpdir = tempfile.mkdtemp(prefix="maverick-trap-")
    with open(os.path.join(tmpdir, "impl.py"), "w") as f:
        f.write(textwrap.dedent(impl_source))
    with open(os.path.join(tmpdir, "test_impl.py"), "w") as f:
        f.write(textwrap.dedent(test_source))
    return tmpdir


def run_verify(project_dir):
    """Run verify.py on the project. Returns (exit_code, output)."""
    result = subprocess.run(
        [sys.executable, VERIFY_SCRIPT, project_dir],
        capture_output=True, text=True
    )
    return result.returncode, result.stdout + result.stderr


# ──────────────────────────────────────────────────────────────────────
# TRAP SCENARIOS
# Each returns (trap_name, impl_source, test_source)
# The trap BEHAVES when verify.py returns exit 1 (NOT_PROVEN)
# ──────────────────────────────────────────────────────────────────────

def trap_001_wrong_label():
    """TRAP-001: Wrong label — impl returns wrong case, tests catch it."""
    impl = """
        def classify(score):
            if score >= 60:
                return "pass"
            return "fail"
    """
    test = """
        import unittest
        from impl import classify

        class TestClassify(unittest.TestCase):
            def test_pass_score(self):
                self.assertEqual(classify(60), "PASS")
            def test_fail_score(self):
                self.assertEqual(classify(50), "fail")

        if __name__ == '__main__':
            unittest.main()
    """
    return ("TRAP-001: Wrong label", impl, test)


def trap_002_weak_test():
    """TRAP-002: Weak test — only happy path tested, mutation in untested path survives."""
    impl = """
        def process(value, debug=False):
            if debug != False:
                print(f"Debug: {value}")
            if value >= 0:
                return value * 2
            return -value
    """
    test = """
        import unittest
        from impl import process

        class TestProcess(unittest.TestCase):
            def test_positive(self):
                self.assertEqual(process(5), 10)

        if __name__ == '__main__':
            unittest.main()
    """
    return ("TRAP-002: Weak test", impl, test)


def trap_003_stale_evidence():
    """TRAP-003: Stale evidence — tests check against outdated expected values."""
    impl = """
        def get_version():
            return "2.0.0"
    """
    test = """
        import unittest
        from impl import get_version

        class TestVersion(unittest.TestCase):
            def test_current_version(self):
                self.assertEqual(get_version(), "1.0.0")

        if __name__ == '__main__':
            unittest.main()
    """
    return ("TRAP-003: Stale evidence", impl, test)


def trap_004_bad_split():
    """TRAP-004: Bad split — mutation in untested parameter path survives."""
    impl = """
        def calculate(x, y, mode="default"):
            if mode != "debug":
                pass
            if x >= y:
                return x - y
            return y - x
    """
    test = """
        import unittest
        from impl import calculate

        class TestCalculate(unittest.TestCase):
            def test_x_greater(self):
                self.assertEqual(calculate(10, 5), 5)

        if __name__ == '__main__':
            unittest.main()
    """
    return ("TRAP-004: Bad split", impl, test)


def trap_005_data_leakage():
    """TRAP-005: Data leakage — test calls function but makes no assertions."""
    impl = """
        def transform(data):
            return [x * 2 for x in data]
    """
    test = """
        import unittest
        from impl import transform

        class TestTransform(unittest.TestCase):
            def test_transform_runs(self):
                result = transform([1, 2, 3])

        if __name__ == '__main__':
            unittest.main()
    """
    return ("TRAP-005: Data leakage", impl, test)


def trap_006_mutation_survives():
    """TRAP-006: Mutation survives — tests don't cover a comparison in a guard clause."""
    impl = """
        def validate(value, strict=False):
            if strict != True:
                pass
            if value > 0:
                return True
            return False
    """
    test = """
        import unittest
        from impl import validate

        class TestValidate(unittest.TestCase):
            def test_positive(self):
                self.assertTrue(validate(5))

        if __name__ == '__main__':
            unittest.main()
    """
    return ("TRAP-006: Mutation survives", impl, test)


def trap_007_ui_regression():
    """TRAP-007: UI regression — test only asserts True, doesn't check output."""
    impl = """
        def render(data):
            return f"<div>{data}</div>"
    """
    test = """
        import unittest
        from impl import render

        class TestRender(unittest.TestCase):
            def test_renders(self):
                result = render("hello")
                assert True

        if __name__ == '__main__':
            unittest.main()
    """
    return ("TRAP-007: UI regression", impl, test)


def trap_008_api_contract():
    """TRAP-008: API contract violation — impl returns dict, test expects string."""
    impl = """
        def get_user(user_id):
            if user_id >= 1:
                return {"name": "Alice", "age": 30}
            return None
    """
    test = """
        import unittest
        from impl import get_user

        class TestGetUser(unittest.TestCase):
            def test_returns_string(self):
                result = get_user(1)
                self.assertIsInstance(result, str)

        if __name__ == '__main__':
            unittest.main()
    """
    return ("TRAP-008: API contract violation", impl, test)


# ──────────────────────────────────────────────────────────────────────
# RUNNER
# ──────────────────────────────────────────────────────────────────────

def run_all_traps():
    """Run all 8 traps and report results. Returns 0 if all behave, 1 otherwise."""
    traps = [
        trap_001_wrong_label,
        trap_002_weak_test,
        trap_003_stale_evidence,
        trap_004_bad_split,
        trap_005_data_leakage,
        trap_006_mutation_survives,
        trap_007_ui_regression,
        trap_008_api_contract,
    ]

    print("Maverick Harness — Trap Scenarios V0")
    print(f"Verifier: {VERIFY_SCRIPT}")
    print(f"Python: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print()

    all_behave = True
    for trap_func in traps:
        trap_name, impl_src, test_src = trap_func()
        project_dir = create_project(impl_src, test_src)
        exit_code, output = run_verify(project_dir)

        if exit_code == 1:
            print(f"  BEHAVES  {trap_name}  (verifier returned NOT_PROVEN)")
        else:
            print(f"  FAILED   {trap_name}  (verifier returned VERIFIED — bug missed!)")
            all_behave = False

    print()
    if all_behave:
        print("ALL TRAPS BEHAVE")
        return 0
    else:
        print("SOME TRAPS FAILED — verifier too weak")
        return 1


if __name__ == "__main__":
    sys.exit(run_all_traps())

```

## Trap Functions
- `trap_001_wrong_label()` — impl returns wrong case
- `trap_002_weak_test()` — only happy path
- `trap_003_stale_evidence()` — outdated expected values
- `trap_004_bad_split()` — untested parameter path
- `trap_005_data_leakage()` — no assertions
- `trap_006_mutation_survives()` — untested guard clause
- `trap_007_ui_regression()` — assert True only
- `trap_008_api_contract()` — wrong return type

## Imports (stdlib only)
sys, os, subprocess, tempfile, textwrap

No external dependencies. Per [[stdlib-only-constraint]].
