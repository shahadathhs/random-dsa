"""977. Squares of a Sorted Array

Given an integer array ``nums`` sorted in non-decreasing order, return an array
of the squares of each number sorted in non-decreasing order.

LeetCode: https://leetcode.com/problems/squares-of-a-sorted-array/
Difficulty: Easy

Documents the opposite-end two-pointer fill: because the largest magnitudes sit
at the ends of a sorted input, we build the result from the back, placing the
larger square each step.
"""

"""
Problem:

    Given an integer array nums sorted in non-decreasing order, return an array
    of the squares of each number sorted in non-decreasing order.

    Example 1:
        Input:  nums = [-4,-1,0,3,10]
        Output: [0,1,9,16,100]
        Explanation: After squaring, the array becomes [16,1,0,9,100].
        After sorting, it becomes [0,1,9,16,100].

    Example 2:
        Input:  nums = [-7,-3,2,3,11]
        Output: [4,9,9,49,121]

    Constraints:
        1 <= nums.length <= 10^4
        -10^4 <= nums[i] <= 10^4
        nums is sorted in non-decreasing order.

    Follow up: Squaring each element and sorting the new array is very trivial,
    could you find an O(n) solution using a different approach?
"""

"""
Squaring Breaks Sortedness:
    Squaring turns negatives into positives, so a sorted input can produce an
    unsorted squared array — e.g. [-4,-1,0,3,10] squares to [16,1,0,9,100]. The
    smallest magnitude lives near the middle of the input (where values cross
    zero) and the largest magnitudes sit at the two ends. That "largest at the
    ends" shape is exactly what the two-pointer approach exploits.
"""

"""
Two Pointers — Opposite Ends (Fill From the Back):
    Place one pointer at each end of ``nums`` and a write pointer ``k`` at the
    back of a fresh result array. At each step compare absolute values: the
    larger magnitude yields the larger square, so write its square to
    ``result[k]`` and step that pointer inward (and ``k`` left). Because the
    inputs are sorted, the ends always hold the largest remaining magnitudes,
    so filling from the back produces a sorted output without ever sorting.
    One pass, O(n).
"""

"""
Copy-Then-Sort Baseline:
    The trivial answer the follow-up calls out: square every element, then sort
    the result. Correct and one line, but O(n log n) — it ignores the fact that
    the input is already sorted. Kept here only as a baseline to make the
    two-pointer version's O(n) advantage concrete.
"""

"""
Time-Space Trade-off:
    - Two pointers (fill from back): O(n)        time, O(n) space — optimal;
      exploits the pre-sorted input.
    - Square then sort             : O(n log n)  time, O(n) space — ignores the
      sortedness; simplest to write.
"""

"""
0977_squares_of_a_sorted_array module/
|
|-- sorted_squares()           # two pointers, fill from back — O(n) time, O(n) space
`-- sorted_squares_copy_sort() # square then sort                 — O(n log n) time, O(n) space
"""


def sorted_squares(nums):
    """Return the squares of ``nums`` sorted non-decreasingly, in one pass.

    Two pointers at opposite ends compare absolute values; the larger magnitude
    gives the larger square, which is written to the back of a fresh result
    array. Both pointers walk inward and the write pointer retreats left, so
    the result is built largest-to-smallest — i.e. already sorted.

    Time:  O(n) — each element is squared and placed exactly once.
    Space: O(n) — a fresh result array of length ``n`` (the output itself).

    Args:
        nums (list[int]): List sorted non-decreasingly.

    Returns:
        list[int]: The square of each value, sorted non-decreasingly.
    """
    left, right = 0, len(nums) - 1
    k = len(nums) - 1            # Write pointer — fills result from the back.

    result = [0] * len(nums)

    # Loop until the pointers meet; the last element (left == right) is the
    # smallest magnitude and lands at result[0].
    while left <= right:
        if abs(nums[left]) < abs(nums[right]):
            result[k] = nums[right] ** 2
            right -= 1           # Larger magnitude was on the right; step it in.
        else:
            result[k] = nums[left] ** 2
            left += 1            # Larger-or-equal magnitude was on the left.
        k -= 1

    return result


def sorted_squares_copy_sort(nums):
    """Return sorted squares by squaring then sorting (correctness baseline).

    The trivial follow-up answer: it discards the sorted-input structure and
    pays O(n log n) for a full sort. Listed only to make the two-pointer
    version's advantage tangible.

    Time:  O(n log n) — Timsort over the squared values.
    Space: O(n)        — a fresh list of length ``n``.

    Args:
        nums (list[int]): List sorted non-decreasingly.

    Returns:
        list[int]: The square of each value, sorted non-decreasingly.
    """
    return sorted(x * x for x in nums)


# ---------------------------------------------------------------------------
# Demo / manual test harness  (section/check live in leetcode/_demo.py)
#
# To run:  make run N=977
# ---------------------------------------------------------------------------

from _demo import section, check


if __name__ == "__main__":
    section("1. Basic cases (both approaches agree)")
    for fn in (sorted_squares, sorted_squares_copy_sort):
        name = fn.__name__

        check(f"{name}([-4,-1,0,3,10])",
              fn([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
        check(f"{name}([-7,-3,2,3,11])",
              fn([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])

    section("2. Edge cases")
    # Only non-negative values: squares preserve the input order.
    check("all non-negative [0,2,3]",
          sorted_squares([0, 2, 3]), [0, 4, 9])
    # Only non-positive values: squares reverse the input order.
    check("all non-positive [-3,-2,-1]",
          sorted_squares([-3, -2, -1]), [1, 4, 9])
    # The crossover point (negative -> positive) is where sortedness breaks.
    check("straddles zero [-2,0,2]",
          sorted_squares([-2, 0, 2]), [0, 4, 4])
    # Single element.
    check("single element [5]", sorted_squares([5]), [25])
    check("single negative [-5]", sorted_squares([-5]), [25])
    # Zero only.
    check("only zero [0]", sorted_squares([0]), [0])
    # Duplicates that straddle zero in magnitude.
    check("equal magnitude [-3,3]", sorted_squares([-3, 3]), [9, 9])
    # Two elements, negative larger in magnitude than the positive.
    check("neg dominates [-5,1]", sorted_squares([-5, 1]), [1, 25])

    section("Demo complete")
