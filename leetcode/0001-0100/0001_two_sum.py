"""1. Two Sum

Given an array of integers ``nums`` and an integer ``target``, return the
indices of the two numbers that add up to ``target``.

LeetCode: https://leetcode.com/problems/two-sum/
Difficulty: Easy

Documents three approaches, trading time for space and exploiting input
structure (sortedness).
"""

"""
Problem:

    Given an array of integers nums and an integer target, return indices of the
    two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may
    not use the same element twice.

    You can return the answer in any order.

    Example 1:
        Input:  nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:
        Input:  nums = [3,2,4], target = 6
        Output: [1,2]

    Example 3:
        Input:  nums = [3,3], target = 6
        Output: [0,1]

    Constraints:
        2 <= nums.length <= 10^4
        -10^9 <= nums[i] <= 10^9
        -10^9 <= target <= 10^9
        Only one valid answer exists.

    Follow-up: Can you come up with an algorithm that is less than O(n^2) time
    complexity?
"""

"""
Complement:
    For a number x and a target t, the complement is t - x — the exact value
    needed to pair with x to reach the target. The hash-map approach asks, for
    each number, "have I already seen its complement?"
"""

"""
Hash Map / Dictionary:
    Maps keys to values with average O(1) insertion and lookup. Here it maps
    each number to the index where it was seen, turning "is the complement
    present?" into a constant-time lookup.
"""

"""
One Pass:
    We check for the complement BEFORE inserting the current number, so a single
    walk of the array both finds pairs and builds the lookup — no second loop,
    and no chance of pairing an element with itself.
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
Index Invalidation (sorted caveat):
    The two-pointer method requires a sorted array, but sorting reorders
    elements and therefore destroys the original indices. Its returned indices
    refer to the SORTED array, not the caller's original array. To report
    original indices you must pair each value with its original index BEFORE
    sorting.
"""

"""
Time-Space Trade-off:
    Different solutions to the same problem balance running time against memory:
        - Brute force  : O(n^2) time, O(1) space  — no extra memory.
        - Hash map     : O(n)   time, O(n) space  — memory buys speed.
        - Two pointers : O(n)   time, O(1) space  — but requires sorted input.
"""

"""
0001_two_sum module/
|
|-- two_sum()              # hash map      — O(n)   time, O(n) space
|-- two_sum_brute_force()  # nested loops  — O(n^2) time, O(1) space
`-- two_sum_sorted()       # two pointers  — O(n)   time, O(1) space (sorted input)
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

    # Walk through the numbers, checking each one's complement as we go.
    for index, num in enumerate(nums):
        complement = target - num

        # If the complement was seen earlier, we have the pair.
        if complement in num_to_index:
            return [num_to_index[complement], index]

        # Store AFTER checking so we never pair an element with itself.
        num_to_index[num] = index

    return None  # No pair sums to the target.


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
    # Iterate through each number, pairing it with every other number.
    for i, first in enumerate(nums):

        for j in range(i + 1, len(nums)):
            second = nums[j]

            # Check if the current pair sums to the target.
            if first + second == target:
                return [i, j]

    return None  # Return None if no solution is found.


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
        # Calculate the current sum of the two numbers at the pointers.
        current_sum = nums[left] + nums[right]

        # Check if the current sum matches the target.
        if current_sum == target:
            return [left, right]

        # Sum too small -> advance left to increase it.
        elif current_sum < target:
            left += 1

        # Sum too large -> retreat right to decrease it.
        else:
            right -= 1

    return None  # Return None if no solution is found.


# ---------------------------------------------------------------------------
# Demo / manual test harness  (section/check live in leetcode/_demo.py)
#
# Verifies all three approaches agree on shared cases, then probes edge cases:
# negatives, zeros, duplicates, no-solution, and tiny inputs.
#
# To run:  make run N=1
# ---------------------------------------------------------------------------

from _demo import section, check


if __name__ == "__main__":
    # --- 1. Hash map vs. brute force agree on the same (unsorted) input ----
    section("1. Hash map vs. brute force (order-independent inputs)")
    nums = [2, 7, 11, 15]
    check("two_sum([2,7,11,15], 9)", two_sum(nums, 9), [0, 1])
    check("two_sum_brute_force(..., 9)", two_sum_brute_force(nums, 9), [0, 1])

    # --- 2. Two-pointer method on a sorted array --------------------------
    section("2. Two pointers (requires a sorted array)")
    check("two_sum_sorted([2,7,11,15], 26)",
          two_sum_sorted([2, 7, 11, 15], 26), [2, 3])

    # --- 3. Edge cases ----------------------------------------------------
    section("3. Edge cases")
    # Duplicates: the same value used at two different indices.
    check("duplicates [3,3], target 6", two_sum([3, 3], 6), [0, 1])
    # Negative numbers and a negative target.
    check("negatives [-3,4,3,90], target 0", two_sum([-3, 4, 3, 90], 0), [0, 2])
    # Zeros pairing to zero.
    check("zeros [0,4,0], target 0", two_sum([0, 4, 0], 0), [0, 2])
    # No valid pair exists -> None.
    check("no solution [1,2,3], target 100", two_sum([1, 2, 3], 100), None)
    # Fewer than two elements -> None.
    check("single element [5], target 5", two_sum([5], 5), None)
    check("empty list [], target 0", two_sum([], 0), None)
    # An element must not be paired with itself.
    check("no self-pair [3,2,4], target 6", two_sum([3, 2, 4], 6), [1, 2])

    section("Demo complete")
