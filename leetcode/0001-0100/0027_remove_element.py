"""27. Remove Element

Given an integer array ``nums`` and an integer ``val``, remove all occurrences
of ``val`` in place. The order of the remaining elements may be changed. Return
``k`` — the number of elements not equal to ``val``. The first ``k`` slots of
``nums`` must hold the kept values; the tail beyond ``k`` is ignored.

LeetCode: https://leetcode.com/problems/remove-element/
Difficulty: Easy

Documents the fast/slow overwrite: ``slow`` bounds the kept prefix while
``fast`` scans, writing every value that survives the filter. A companion
two-pointer-from-both-ends approach is shown for the case where order need not
be preserved.
"""

"""
Problem:

    Given an integer array nums and an integer val, remove all occurrences of
    val in nums in-place. The order of the elements may be changed. Then return
    the number of elements in nums which are not equal to val.

    Consider the number of elements in nums which are not equal to val be k, to
    get accepted, you need to do the following things:

    - Change the array nums such that the first k elements of nums contain the
      elements which are not equal to val. The remaining elements of nums are
      not important as well as the size of nums.
    - Return k.

    Custom Judge:

        The judge will test your solution with the following code:

        int[] nums = [...]; // Input array
        int val = ...; // Value to remove
        int[] expectedNums = [...]; // The expected answer with correct length.
                                    // It is sorted with no values equaling val.

        int k = removeElement(nums, val); // Calls your implementation

        assert k == expectedNums.length;
        sort(nums, 0, k); // Sort the first k elements of nums
        for (int i = 0; i < actualLength; i++) {
            assert nums[i] == expectedNums[i];
        }

        If all assertions pass, then your solution will be accepted.

    Example 1:
        Input:  nums = [3,2,2,3], val = 3
        Output: 2, nums = [2,2,_,_]
        Explanation: Your function should return k = 2, with the first two
        elements of nums being 2. It does not matter what you leave beyond the
        returned k (hence they are underscores).

    Example 2:
        Input:  nums = [0,1,2,2,3,0,4,2], val = 2
        Output: 5, nums = [0,1,4,0,3,_,_,_]
        Explanation: Your function should return k = 5, with the first five
        elements of nums containing 0, 0, 1, 3, and 4. Note that the five
        elements can be returned in any order.

    Constraints:
        0 <= nums.length <= 100
        0 <= nums[i] <= 50
        0 <= val <= 100
"""

"""
Overwrite, Don't Shift:
    Removing an element by shifting everything after it left by one is O(n)
    *per removal*, which compounds to O(n^2) when many values match. The
    overwrite technique avoids shifting entirely: scan once with a write pointer
    and copy each surviving value forward into the next kept slot. Removed
    values are never physically deleted — they are overwritten from behind, and
    the tail past the returned ``k`` is simply ignored. One pass, O(n).
"""

"""
Fast & Slow Pointers (Order-Preserving Overwrite):
    ``slow`` is the next slot to receive a kept value; ``fast`` scans every
    element. Whenever ``nums[fast]`` differs from ``val`` it is copied into
    ``nums[slow]`` and ``slow`` advances. The invariant is "everything before
    ``slow`` is a kept value, in original order", so when ``fast`` finishes the
    prefix ``[0..slow)`` holds the answer. Relative order is preserved because
    survivors are written left-to-right in encounter order.
"""

"""
Two Pointers From Both Ends (Order-Not-Preserved):
    When the problem states order may change (as here), a second approach writes
    *fewer* values: place ``left`` at the front and ``right`` at the back.
    Advance ``left`` while it points at a kept value; when it hits ``val``,
    overwrite it with ``nums[right]`` and retreat ``right`` — do NOT advance
    ``left`` yet, because the swapped-in value still needs checking. The loop
    ends when ``left`` passes ``right``, and ``left`` is the count. This copies
    only the removed slots (each overwrite replaces one ``val``), so it does at
    most ``min(count_val, k)`` writes vs. the overwrite approach's ``k`` writes.
    Trade-off: it scrambles the relative order of the survivors.
"""

"""
In Place (No Output Array):
    The result must occupy ``nums`` itself, and only the count ``k`` is
    returned — the judge reads ``nums[0..k-1]`` (sorting them before comparing,
    so order genuinely does not matter for acceptance). That rules out building
    a fresh list; both approaches below keep extra space at O(1).
"""

"""
Time-Space Trade-off:
    - Fast/slow overwrite  : O(n) time, O(1) space — preserves order; writes
      every kept value forward (k writes).
    - Both-ends overwrite  : O(n) time, O(1) space — order NOT preserved; writes
      only the removed slots (at most min(count_val, k) writes). Fewer writes
      when matches are rare.
"""

"""
0027_remove_element module/
|
|-- remove_element()        # fast/slow overwrite      — O(n) time, O(1) space
`-- remove_element_ends()   # both-ends overwrite       — O(n) time, O(1) space
"""


def remove_element(nums, val):
    """Remove all ``val`` from ``nums`` in place, preserving order.

    Fast/slow overwrite: ``slow`` is the next kept slot, ``fast`` scans every
    element. Each value not equal to ``val`` is copied into ``nums[slow]`` and
    ``slow`` advances. Survivors land in their original relative order; removed
    values are overwritten from behind and the tail is ignored.

    Time:  O(n)   — one pass; ``fast`` visits every element once.
    Space: O(1)   — only the ``slow`` index.

    Args:
        nums (list[int]): The list to filter. Mutated in place: its first ``k``
            slots hold the kept values.
        val (int): The value to remove.

    Returns:
        int: ``k``, the number of elements not equal to ``val``.
    """
    slow = 0  # Invariant: nums[0..slow-1] holds the kept values in order.

    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1

    return slow


def remove_element_ends(nums, val):
    """Remove all ``val`` from ``nums`` in place, order NOT preserved.

    Both-ends overwrite: ``left`` advances past kept values; when it lands on
    ``val``, the value from ``right`` is copied over it and ``right`` retreats
    — but ``left`` does NOT advance, because the swapped-in copy still needs
    checking. The loop ends when ``left`` overtakes ``right``, and ``left`` is
    the count. Writes only the slots that held ``val``, so it can be faster than
    the order-preserving overwrite when matches are rare.

    Time:  O(n)   — one pass; each slot is visited at most once.
    Space: O(1)   — only the two indices.

    Args:
        nums (list[int]): The list to filter. Mutated in place: its first ``k``
            slots hold the kept values (in arbitrary order).
        val (int): The value to remove.

    Returns:
        int: ``k``, the number of elements not equal to ``val``.
    """
    left, right = 0, len(nums) - 1

    # Invariant: nums[0..left-1] are kept; nums[right+1..] are discarded.
    # left == right is still live: that slot may hold val and needs checking.
    while left <= right:
        if nums[left] == val:
            nums[left] = nums[right]  # Overwrite with an unvetted tail value...
            right -= 1                # ...then shrink the window WITHOUT moving
                                      # left, so the new nums[left] is rechecked.
        else:
            left += 1  # Kept value — advance past it.

    return left


# ---------------------------------------------------------------------------
# Demo / manual test harness  (section/check live in leetcode/_demo.py)
#
# To run:  make run N=27
# ---------------------------------------------------------------------------

from _demo import section, check


if __name__ == "__main__":
    section("1. Basic cases (both approaches agree on the kept *set*)")
    # The judge sorts nums[0..k] before comparing, so we check the sorted prefix
    # rather than the raw order — remove_element_ends does not preserve order.
    for fn in (remove_element, remove_element_ends):
        name = fn.__name__

        a = [3, 2, 2, 3]
        k = fn(a, 3)
        check(f"{name} k for [3,2,2,3], val=3", k, 2)
        check(f"{name} kept (sorted)", sorted(a[:k]), [2, 2])

        b = [0, 1, 2, 2, 3, 0, 4, 2]
        k = fn(b, 2)
        check(f"{name} k for [0,1,2,2,3,0,4,2], val=2", k, 5)
        check(f"{name} kept (sorted)", sorted(b[:k]), [0, 0, 1, 3, 4])

    section("2. Edge cases")
    # remove_element is order-preserving, so we can check the raw prefix.
    # No matches — k == len, array unchanged.
    c = [1, 2, 3]
    k = remove_element(c, 99)
    check("no matches [1,2,3], val=99", k, 3)
    check("prefix unchanged", c[:k], [1, 2, 3])

    # Everything matches — k == 0.
    d = [5, 5, 5]
    k = remove_element(d, 5)
    check("all match [5,5,5], val=5", k, 0)

    # Empty array — loop body never runs, k == 0.
    e = []
    k = remove_element(e, 1)
    check("empty [], val=1", k, 0)

    # Single element, matches.
    f = [7]
    k = remove_element(f, 7)
    check("single match [7], val=7", k, 0)

    # Single element, no match.
    g = [7]
    k = remove_element(g, 9)
    check("single no-match [7], val=9", k, 1)
    check("prefix", g[:k], [7])

    # val at the front only.
    h = [9, 1, 2, 3]
    k = remove_element(h, 9)
    check("front only [9,1,2,3], val=9", k, 3)
    check("prefix", h[:k], [1, 2, 3])

    # val at the back only.
    i = [1, 2, 3, 9]
    k = remove_element(i, 9)
    check("back only [1,2,3,9], val=9", k, 3)
    check("prefix", i[:k], [1, 2, 3])

    # val in the middle only.
    j = [1, 9, 2]
    k = remove_element(j, 9)
    check("middle [1,9,2], val=9", k, 2)
    check("prefix", j[:k], [1, 2])

    section("Demo complete")
