"""Shared demo helpers for the LeetCode solution files.

Every solution file has a small ``if __name__ == "__main__"`` harness that runs
labelled PASS/FAIL checks. These two helpers back that harness so each file does
not re-declare them. Import them at the top of a solution file:

    from _demo import section, check

The sibling import works because running ``python3 leetcode/<file>.py`` puts the
``leetcode/`` directory on ``sys.path``.
"""


def section(title):
    """Print a visual divider so each phase of the demo stands out."""
    print(f"\n{'=' * 60}\n {title}\n{'=' * 60}")


def check(label, got, expected):
    """Print a labelled PASS/FAIL comparison of an actual vs. expected result."""
    status = "PASS" if got == expected else "FAIL"
    print(f"[{status}] {label:<38} got={str(got):<10} expected={expected}")
