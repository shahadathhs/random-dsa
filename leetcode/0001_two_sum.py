"""1. Two Sum

Given an array of integers ``nums`` and an integer ``target``, return the
indices of the two numbers that add up to ``target``.

LeetCode: https://leetcode.com/problems/two-sum/
Difficulty: Easy

Documents the one-pass hash-map approach: trade O(n) memory for O(n) time.
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
Time-Space Trade-off:
    - Brute force : O(n^2) time, O(1) space  — try every pair.
    - Hash map    : O(n)   time, O(n) space  — memory buys speed (this file).
"""

"""
0001_two_sum module/
│
└── two_sum()   # one-pass hash map — O(n) time, O(n) space
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


# ---------------------------------------------------------------------------
# Demo / manual test harness  (section/check live in leetcode/_demo.py)
#
# To run:  python3 leetcode/0001_two_sum.py
# ---------------------------------------------------------------------------

from _demo import section, check

if __name__ == "__main__":
    section("1. Basic cases")
    check("two_sum([2,7,11,15], 9)", two_sum([2, 7, 11, 15], 9), [0, 1])
    check("two_sum([3,2,4], 6)", two_sum([3, 2, 4], 6), [1, 2])

    section("2. Edge cases")
    check("duplicates [3,3], target 6", two_sum([3, 3], 6), [0, 1])
    check("negatives [-3,4,3,90], target 0", two_sum([-3, 4, 3, 90], 0), [0, 2])
    check("zeros [0,4,0], target 0", two_sum([0, 4, 0], 0), [0, 2])
    check("no solution [1,2,3], target 100", two_sum([1, 2, 3], 100), None)
    check("single element [5], target 5", two_sum([5], 5), None)
    check("empty list [], target 0", two_sum([], 0), None)

    section("Demo complete")
