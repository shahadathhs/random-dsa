"""<NUM>. <Problem Name>

<One-paragraph statement of the problem in plain words: what the inputs are and
what to return.>

LeetCode: https://leetcode.com/problems/<slug>/
Difficulty: <Easy | Medium | Hard>

This module documents the core concepts and shows <N> approach(es), trading
time for space where relevant.
"""

"""
Problem:

    <Paste the official problem statement here, VERBATIM — description,
    examples, constraints, and any follow-up. Keeping it unedited makes each
    file self-contained and unambiguous about what was actually asked.>
"""

"""
<Concept 1>:
    <Define each idea the solution relies on — one block per concept. Copy the
    style of array/two_sum.py: Complement, Hash Map, Brute Force, etc.>
"""

"""
Time-Space Trade-off:
    <How the approaches compare, e.g.>
        - Brute force : O(n^2) time, O(1) space
        - Hash map    : O(n)   time, O(n) space
"""

"""
<num>_<name> module/
│
├── solve()              # <approach>  — O(?) time, O(?) space
└── solve_brute_force()  # <approach>  — O(?) time, O(?) space
"""


def solve(nums, target):
    """<One-line summary of what this returns and the approach used.>

    <A sentence or two on the mechanism.>

    Time:  O(?)   — <why>.
    Space: O(?)   — <why>.

    Args:
        nums (list[int]): <...>.
        target (int): <...>.

    Returns:
        <type>: <what, and the sentinel/None case>.
    """
    # ... implementation, with inline comments on the non-obvious lines ...
    return None


# ---------------------------------------------------------------------------
# Demo / manual test harness  (section/check live in leetcode/_demo.py)
#
# To run:  make run N=<num>
# ---------------------------------------------------------------------------

from _demo import section, check

if __name__ == "__main__":
    section("1. Basic cases")
    # check("solve(...)", solve(...), expected)

    section("2. Edge cases")
    # empty input, single element, duplicates, negatives, no-solution -> None ...

    section("Demo complete")
