"""Two Sum

Given an array of integers ``nums`` and an integer ``target``, return the
indices of the two numbers that add up to ``target``.

This module documents the core concepts and shows three approaches, trading
time for space and exploiting input structure (sortedness).
"""

"""
Problem — Two Sum:
    Find two distinct positions i and j such that nums[i] + nums[j] == target.
    Each input is assumed to have exactly one solution, and the same element may
    not be used twice. The answer may be returned in any order.
"""

"""
Complement:
    For a given number x and a target t, the complement is t - x — the exact
    value needed to pair with x to reach the target. The hash-map approach works
    by asking, for each number, "have I already seen its complement?"
"""

"""
Hash Map / Dictionary:
    A data structure that maps keys to values with average O(1) insertion and
    lookup. Here it maps each number to the index where it was seen, turning the
    "is the complement present?" question into a constant-time lookup.
"""

"""
Brute Force:
    The most direct strategy: try every possible pair. It is simple and needs no
    extra memory, but its O(n^2) time makes it impractical for large inputs. It
    is useful as a baseline and correctness reference.
"""

"""
Two Pointers:
    A technique that uses two indices moving toward each other from opposite ends
    of a SORTED array. If the current sum is too small, advance the left pointer
    (to increase it); if too large, retreat the right pointer (to decrease it).
    This finds the pair in O(n) time using O(1) extra space.
"""

"""
Time–Space Trade-off:
    Different solutions to the same problem balance running time against memory:
        - Brute force  : O(n^2) time, O(1) space  — no extra memory.
        - Hash map     : O(n)   time, O(n) space  — memory buys speed.
        - Two pointers : O(n)   time, O(1) space  — but requires sorted input.
"""

"""
Index Invalidation (sorted caveat):
    The two-pointer method requires a sorted array, but sorting reorders
    elements and therefore destroys the original indices. Its returned indices
    refer to the SORTED array, not the caller's original array. To report
    original indices you must pair each value with its original index BEFORE
    sorting.
"""

"""
two_sum module/
│
├── two_sum()              # hash map      — O(n)   time, O(n) space
├── two_sum_brute_force()  # nested loops  — O(n^2) time, O(1) space
└── two_sum_sorted()       # two pointers  — O(n)   time, O(1) space (needs sorted input)
"""


def two_sum(nums, target):
    """Return indices of the two numbers that sum to ``target`` using a hash map.

    Single pass: for each number, check whether its complement was already seen;
    if so we have the pair, otherwise remember the current number's index.

    Time:  O(n)   — one pass, O(1) average dictionary operations.
    Space: O(n)   — up to n entries stored in the lookup map.

    Args:
        nums (list[int]): The list of integers to search.
        target (int): The target sum.

    Returns:
        list[int] | None: The two indices whose values sum to ``target``,
        or None if no such pair exists.
    """
    num_to_index = {}

    # Walk through the list of numbers, checking for complements
    for index, num in enumerate(nums):
        # Calculate the complement of the current number
        complement = target - num

        # Check if the complement exists in the dictionary
        if complement in num_to_index:
            return [num_to_index[complement], index]

        # Store AFTER checking so we never pair an element with itself.
        num_to_index[num] = index

    return None  # Return None if no solution is found


def two_sum_brute_force(nums, target):
    """Return indices of the two numbers that sum to ``target`` by trying every pair.

    Time:  O(n^2) — every pair (i, j) is examined.
    Space: O(1)   — no auxiliary storage.

    Args:
        nums (list[int]): The list of integers to search.
        target (int): The target sum.

    Returns:
        list[int] | None: The two indices whose values sum to ``target``,
        or None if no such pair exists.
    """
    # Iterate through each number, pairing it with every other number
    for i, first in enumerate(nums):

        for j in range(i + 1, len(nums)):
            second = nums[j]

            # Check if the current pair sums to the target
            if first + second == target:
                return [i, j]

    return None  # Return None if no solution is found


def two_sum_sorted(nums, target):
    """Return indices of the two numbers that sum to ``target`` in a SORTED array.

    Uses the two-pointer technique from both ends inward.

    Time:  O(n)   — each pointer moves inward at most n times total.
    Space: O(1)   — only two indices are tracked.

    Note:
        ``nums`` MUST already be sorted in non-decreasing order. The returned
        indices refer to the sorted array — see the "Index Invalidation" note
        above if you need indices into an unsorted original.

    Args:
        nums (list[int]): A list of integers sorted in non-decreasing order.
        target (int): The target sum.

    Returns:
        list[int] | None: The two indices whose values sum to ``target``,
        or None if no such pair exists.
    """
    left, right = 0, len(nums) - 1

    while left < right:
        # Calculate the current sum of the two numbers at the left and right pointers
        current_sum = nums[left] + nums[right]

        # Check if the current sum matches the target
        if current_sum == target:
            return [left, right]

        # Move the left pointer to the right if the current sum is less than the target
        elif current_sum < target:
            left += 1

        # Move the right pointer to the left if the current sum is greater than the target
        else:
            right -= 1

    return None  # Return None if no solution is found


# ---------------------------------------------------------------------------
# Demo / manual test harness
#
# Verifies all three approaches agree on shared cases, then probes edge cases:
# negatives, zeros, duplicates, no-solution, and tiny inputs.
#
# To run:  python3 two_sum.py
# ---------------------------------------------------------------------------

def _section(title):
    """Print a visual divider so each phase of the demo stands out."""
    print(f"\n{'=' * 60}\n {title}\n{'=' * 60}")


def _check(label, got, expected):
    """Print a labelled PASS/FAIL comparison of an actual vs. expected result."""
    status = "PASS" if got == expected else "FAIL"
    print(f"[{status}] {label:<38} got={str(got):<10} expected={expected}")


if __name__ == "__main__":
    # --- 1. Hash map vs. brute force agree on the same (unsorted) input ----
    _section("1. Hash map vs. brute force (order-independent inputs)")
    nums = [2, 7, 11, 15]
    _check("two_sum([2,7,11,15], 9)", two_sum(nums, 9), [0, 1])
    _check("two_sum_brute_force(..., 9)", two_sum_brute_force(nums, 9), [0, 1])

    # --- 2. Two-pointer method on a sorted array --------------------------
    _section("2. Two pointers (requires a sorted array)")
    _check("two_sum_sorted([2,7,11,15], 26)", two_sum_sorted([2, 7, 11, 15], 26), [2, 3])

    # --- 3. Edge cases ----------------------------------------------------
    _section("3. Edge cases")
    # Duplicates: the same value used at two different indices.
    _check("duplicates [3,3], target 6", two_sum([3, 3], 6), [0, 1])
    # Negative numbers and a negative target.
    _check("negatives [-3,4,3,90], target 0", two_sum([-3, 4, 3, 90], 0), [0, 2])
    # Zeros pairing to zero.
    _check("zeros [0,4,0], target 0", two_sum([0, 4, 0], 0), [0, 2])
    # No valid pair exists -> None.
    _check("no solution [1,2,3], target 100", two_sum([1, 2, 3], 100), None)
    # Fewer than two elements -> None.
    _check("single element [5], target 5", two_sum([5], 5), None)
    _check("empty list [], target 0", two_sum([], 0), None)
    # An element must not be paired with itself.
    _check("no self-pair [3,2,4], target 6", two_sum([3, 2, 4], 6), [1, 2])

    _section("Demo complete")
