"""26. Remove Duplicates from Sorted Array

Given a sorted array ``nums``, remove duplicates in place so each unique value
appears once, keeping relative order. Return ``k`` — the count of unique
elements. The first ``k`` slots of ``nums`` must hold the unique values in
order; the tail beyond ``k`` is ignored.

LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Difficulty: Easy

Documents the fast/slow two-pointer: ``slow`` bounds the deduped prefix while
``fast`` scouts ahead, overwriting duplicates from behind. The same pattern
appears in ``array/pointers.py::remove_duplicates_sorted``.
"""

"""
Problem:

    Given an integer array nums sorted in non-decreasing order, remove the
    duplicates in-place such that each unique element appears only once. The
    relative order of the elements should be kept the same.

    Consider the number of unique elements in nums to be k. After removing
    duplicates, return the number of unique elements k.

    The first k elements of nums should contain the unique numbers in sorted
    order. The remaining elements beyond index k - 1 can be ignored.

    Custom Judge:

        The judge will test your solution with the following code:

        int[] nums = [...]; // Input array
        int[] expectedNums = [...]; // The expected answer with correct length

        int k = removeDuplicates(nums); // Calls your implementation

        assert k == expectedNums.length;
        for (int i = 0; i < k; i++) {
            assert nums[i] == expectedNums[i];
        }

        If all assertions pass, then your solution will be accepted.

    Example 1:
        Input:  nums = [1,1,2]
        Output: 2, nums = [1,2,_]
        Explanation: Your function should return k = 2, with the first two
        elements of nums being 1 and 2 respectively. It does not matter what you
        leave beyond the returned k (hence they are underscores).

    Example 2:
        Input:  nums = [0,0,1,1,1,2,2,3,3,4]
        Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
        Explanation: Your function should return k = 5, with the first five
        elements of nums being 0, 1, 2, 3, and 4 respectively.

    Constraints:
        1 <= nums.length <= 3 * 10^4
        -100 <= nums[i] <= 100
        nums is sorted in non-decreasing order.
"""

"""
Sortedness Enables One Pass:
    In an *unsorted* array a duplicate of ``nums[i]`` could appear anywhere, so
    deduping needs a membership test (hash set) or a full sort first. But when
    the input is already sorted, duplicates are *adjacent*: every run of equal
    values sits in a single contiguous block. That lets a single forward scan
    compare each element only with its immediate predecessor and catch every
    duplicate — no set, no sorting, no looking back.
"""

"""
Fast & Slow Pointers (Overwrite In Place):
    ``slow`` marks the boundary of the deduped prefix and only advances when
    ``fast`` finds a value not equal to ``nums[slow]``; that fresh value is
    written into ``nums[slow]``, overwriting the duplicate that sat there. The
    invariant is "everything at or before ``slow`` is unique and in order", so
    when ``fast`` falls off the end the prefix ``[0..slow]`` holds the answer.
    Duplicates are not removed from the array — they are *overwritten from
    behind*, and the tail beyond the returned ``k`` is simply ignored.
"""

"""
In Place (No Output Array):
    The result must occupy ``nums`` itself, and only the count ``k`` is
    returned — the judge reads ``nums[0..k-1]``. That rules out building a fresh
    list; the overwrite-from-behind technique keeps extra space at O(1) (two
    index variables) while preserving the relative order of the unique values.
"""

"""
Time-Space Trade-off:
    - Fast/slow overwrite: O(n) time, O(1) space — optimal; exploits the input
      being pre-sorted so duplicates are adjacent.
    - (Alternative) hash set would be O(n) time but O(n) space and would lose
      the sort order, so it is strictly worse here.
"""

"""
0026_remove_duplicates_from_sorted_array module/
|
|-- remove_duplicates()  # fast/slow overwrite — O(n) time, O(1) space
"""


def remove_duplicates(nums):
    """Dedupe sorted ``nums`` in place; return the count of unique values.

    Fast/slow pointers: ``slow`` bounds the unique prefix; ``fast`` scans from
    the second slot. Each time ``fast`` finds a value different from
    ``nums[slow]``, ``slow`` advances and the fresh value is written into it,
    overwriting the duplicate that occupied that slot. The first ``slow + 1``
    slots of ``nums`` end up holding the unique values in original order; the
    tail is left untouched and ignored by the caller.

    Time:  O(n)   — one pass; ``fast`` visits every element once.
    Space: O(1)   — only the ``slow`` index (``fast`` is the loop variable).

    Args:
        nums (list[int]): A list of integers sorted non-decreasingly. Mutated
            in place: its first ``k`` slots hold the unique values.

    Returns:
        int: ``k``, the number of unique elements (so ``nums[0..k-1]`` is the
        deduped prefix).
    """
    slow = 0  # Invariant: nums[0..slow] holds the unique prefix.

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1              # Make room for a new unique value.
            nums[slow] = nums[fast]  # Overwrite the duplicate from behind.

    return slow + 1  # Count = last unique index + 1.


# ---------------------------------------------------------------------------
# Demo / manual test harness  (section/check live in leetcode/_demo.py)
#
# To run:  make run N=26
# ---------------------------------------------------------------------------

from _demo import section, check


if __name__ == "__main__":
    section("1. Basic cases")
    a = [1, 1, 2]
    k = remove_duplicates(a)
    check("k for [1,1,2]", k, 2)
    check("prefix [1,1,2]", a[:k], [1, 2])

    b = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(b)
    check("k for [0,0,1,1,1,2,2,3,3,4]", k, 5)
    check("prefix", b[:k], [0, 1, 2, 3, 4])

    section("2. Edge cases")
    # Already unique: slow never advances past each element, k == len.
    c = [1, 2, 3, 4]
    k = remove_duplicates(c)
    check("already unique [1,2,3,4]", k, 4)
    check("prefix unchanged", c[:k], [1, 2, 3, 4])

    # All the same value: slow stays at 0, k == 1.
    d = [7, 7, 7, 7]
    k = remove_duplicates(d)
    check("all same [7,7,7,7]", k, 1)
    check("prefix", d[:k], [7])

    # Single element: loop body never runs, k == 1.
    e = [5]
    k = remove_duplicates(e)
    check("single element [5]", k, 1)
    check("prefix", e[:k], [5])

    # Two equal elements.
    f = [3, 3]
    k = remove_duplicates(f)
    check("two equal [3,3]", k, 1)
    check("prefix", f[:k], [3])

    # Two distinct elements.
    g = [3, 4]
    k = remove_duplicates(g)
    check("two distinct [3,4]", k, 2)
    check("prefix", g[:k], [3, 4])

    # Negatives (still sorted non-decreasingly).
    h = [-3, -3, -1, 0, 0, 2]
    k = remove_duplicates(h)
    check("negatives [-3,-3,-1,0,0,2]", k, 4)
    check("prefix", h[:k], [-3, -1, 0, 2])

    section("Demo complete")
