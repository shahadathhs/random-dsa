"""217. Contains Duplicate

Given an integer array ``nums``, return True if any value appears at least
twice, and False if every element is distinct.

LeetCode: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy

Documents two approaches: a brute-force pair check and the optimal hash-set
scan, trading O(n) memory for O(n) time.
"""

"""
Problem:

    Given an integer array nums, return true if any value appears at least
    twice in the array, and return false if every element is distinct.

    Example 1:
        Input:  nums = [1,2,3,1]
        Output: true
        Explanation: The element 1 occurs at the indices 0 and 3.

    Example 2:
        Input:  nums = [1,2,3,4]
        Output: false
        Explanation: All elements are distinct.

    Example 3:
        Input:  nums = [1,1,1,3,3,4,3,2,4,2]
        Output: true

    Constraints:
        1 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9
"""

"""
Hash Set:
    A collection of unique values with average O(1) membership tests and
    insertion. Here it records the values seen so far, turning "have I already
    encountered this number?" into a constant-time lookup. A set (not a map) is
    the right tool because we only care whether a value exists, not any data
    attached to it.
"""

"""
Early Exit:
    We check membership BEFORE inserting, and return the moment a repeat is
    found. On inputs with an early duplicate this stops well before scanning the
    whole array; only a fully-distinct array forces the complete pass.
"""

"""
Brute Force:
    Compare every pair (i, j). Simple and needs no extra memory, but its O(n^2)
    time is impractical for the constraint n <= 10^5 (~10^10 comparisons). Kept
    here as a correctness baseline.
"""

"""
Time-Space Trade-off:
    - Brute force : O(n^2) time, O(1) space  — no extra memory.
    - Hash set    : O(n)   time, O(n) space  — memory buys speed (recommended).

    A third option — sort, then check adjacent pairs — is O(n log n) time and
    O(1) extra space, sitting between the two when memory is tight.
"""

"""
0217_contains_duplicate module/
│
├── contains_duplicate()              # hash set     — O(n)   time, O(n) space
└── contains_duplicate_brute_force()  # nested loops — O(n^2) time, O(1) space
"""


def contains_duplicate(nums):
    """Return True if any value in ``nums`` appears at least twice.

    Single pass with a set: for each number, if it was already seen we have a
    duplicate; otherwise remember it and continue.

    Time:  O(n)   — one pass, O(1) average set operations.
    Space: O(n)   — up to n distinct values stored in the set.

    Args:
        nums (list[int]): The list of integers to inspect.

    Returns:
        bool: True if a duplicate exists, False if all elements are distinct.
    """
    seen = set()

    for num in nums:
        # Membership is checked BEFORE insertion, so a repeat is caught the
        # moment its second occurrence is reached.
        if num in seen:
            return True

        seen.add(num)

    return False  # Reached the end without a repeat -> all distinct.


def contains_duplicate_brute_force(nums):
    """Return True if any value in ``nums`` appears at least twice, checking every pair.

    Time:  O(n^2) — every pair (i, j) is compared.
    Space: O(1)   — no auxiliary storage.

    Args:
        nums (list[int]): The list of integers to inspect.

    Returns:
        bool: True if a duplicate exists, False if all elements are distinct.
    """
    for i, first in enumerate(nums):

        for j in range(i + 1, len(nums)):
            # Any matching later element means a duplicate.
            if first == nums[j]:
                return True

    return False  # No pair matched -> all distinct.


# ---------------------------------------------------------------------------
# Demo / manual test harness  (section/check live in leetcode/_demo.py)
#
# To run:  make run N=217
# ---------------------------------------------------------------------------

from _demo import section, check

if __name__ == "__main__":
    section("1. Basic cases (hash set vs. brute force agree)")
    for fn in (contains_duplicate, contains_duplicate_brute_force):
        name = fn.__name__
        check(f"{name}([1,2,3,1])", fn([1, 2, 3, 1]), True)
        check(f"{name}([1,2,3,4])", fn([1, 2, 3, 4]), False)
        check(f"{name}([1,1,1,3,3,4,3,2,4,2])", fn([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)

    section("2. Edge cases")
    check("single element [1]", contains_duplicate([1]), False)
    check("empty list []", contains_duplicate([]), False)
    check("two equal [7,7]", contains_duplicate([7, 7]), True)
    check("negatives [-1,-2,-1]", contains_duplicate([-1, -2, -1]), True)
    check("all distinct negatives [-1,-2,-3]", contains_duplicate([-1, -2, -3]), False)

    section("Demo complete")
