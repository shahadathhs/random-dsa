"""88. Merge Sorted Array

Given two integer arrays ``nums1`` (length ``m + n``, last ``n`` slots reserved
as zeros) and ``nums2`` (length ``n``), both sorted non-decreasing, merge them
in place into ``nums1``.

LeetCode: https://leetcode.com/problems/merge-sorted-array/
Difficulty: Easy

Documents the backwards three-pointer merge: write the largest surviving value
into the back of ``nums1`` so the unprocessed prefix is never overwritten.
"""

"""
Problem:

    You are given two integer arrays nums1 and nums2, sorted in non-decreasing
    order, and two integers m and n, representing the number of elements in
    nums1 and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    The final sorted array should not be returned by the function, but instead
    be stored inside the array nums1. To accommodate this, nums1 has a length of
    m + n, where the first m elements denote the elements that should be merged,
    and the last n elements are set to 0 and should be ignored. nums2 has a
    length of n.

    Example 1:
        Input:  nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        Output: [1,2,2,3,5,6]
        Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
        The result of the merge is [1,2,2,3,5,6].

    Example 2:
        Input:  nums1 = [1], m = 1, nums2 = [], n = 0
        Output: [1]

    Example 3:
        Input:  nums1 = [0], m = 0, nums2 = [1], n = 1
        Output: [1]
        Explanation: Because m = 0, there are no elements in nums1. The 0 is
        only there to ensure the merge result can fit.

    Constraints:
        nums1.length == m + n
        nums2.length == n
        0 <= m, n <= 200
        1 <= m + n <= 200
        -10^9 <= nums1[i], nums2[j] <= 10^9

    Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""

"""
In Place:
    The result must occupy ``nums1`` itself — no return value, no fresh array
    allocated. That constraint is what makes the choice of merge direction
    non-trivial: writing from the front would clobber the unprocessed tail of
    ``nums1``'s own values before they could be read.
"""

"""
Backwards Three-Pointer Merge:
    Stand three pointers at the last *real* element of each input (``i`` on the
    end of nums1's first ``m`` values, ``j`` on the end of nums2) and a write
    pointer ``k`` at the very back of nums1. At each step pick the larger of
    nums1[i] and nums2[j], copy it to nums1[k], and step that pointer plus ``k``
    leftwards. Writing from the back means every slot we overwrite is one we
    have already consumed (or one of the reserved zeros), so the live prefix is
    never disturbed. The loop ends as soon as ``j`` falls off nums2 — any
    remaining nums1 values are already in their correct front positions.
"""

"""
Copy-Then-Sort Baseline:
    The trivial in-place answer is: paste nums2 into the reserved tail of
    nums1, then sort the whole thing. Correct, two lines, but O((m+n) log
    (m+n)) time — it ignores the fact that both halves are *already* sorted.
    Kept here only as a baseline to make the three-pointer version's O(m+n)
    advantage concrete.
"""

"""
Time-Space Trade-off:
    - Backwards three-pointer: O(m + n) time, O(1) space — optimal; exploits
      both arrays being pre-sorted.
    - Copy then sort          : O((m+n) log (m+n)) time, O(1) space — ignores
      the sortedness of the inputs; simplest to write.
"""

"""
0088_merge_sorted_array module/
|
|-- merge()           # backwards three-pointer — O(m + n) time, O(1) space
`-- merge_copy_sort() # copy nums2 then sort    — O((m+n) log (m+n)) time, O(1) space
"""


def merge(nums1, m, nums2, n):
    """Merge sorted ``nums2`` into sorted ``nums1`` in place, writing from the back.

    Walks three pointers inward from the ends of the real data: ``i`` over
    nums1's first ``m`` values, ``j`` over nums2, and ``k`` at the back of the
    ``m + n`` buffer. Each iteration picks the larger of nums1[i] / nums2[j],
    writes it to nums1[k], and steps that pointer plus ``k`` left. Writing from
    the back means overwrites only hit already-consumed slots, so the live
    prefix of nums1 is never corrupted. The loop runs until nums2 is fully
    drained; any leftover nums1 prefix is already in place.

    Time:  O(m + n) — each slot of the buffer is written exactly once.
    Space: O(1)     — three index variables; no auxiliary storage.

    Args:
        nums1 (list[int]): Buffer of length ``m + n``; first ``m`` entries are
            the sorted source, last ``n`` are scratch zeros.
        m (int): Number of real elements in ``nums1``.
        nums2 (list[int]): Sorted source of length ``n``.
        n (int): Number of elements in ``nums2``.

    Returns:
        None: ``nums1`` is mutated in place to hold the merged result.
    """
    i = m - 1          # Last real element of nums1.
    j = n - 1          # Last element of nums2.
    k = m + n - 1      # Back of nums1's buffer — where we write next.

    # Drive on j: once nums2 is fully placed, any leftover nums1 prefix is
    # already correctly positioned at the front.
    while j >= 0:
        # Take from nums1 if it still has values AND its current one is larger;
        # otherwise take from nums2. The `i >= 0` guard must come first so we
        # never read nums1[-1] once nums1's prefix is exhausted.
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1

        k -= 1


def merge_copy_sort(nums1, m, nums2, n):
    """Merge ``nums2`` into ``nums1`` by overwriting the scratch tail and re-sorting.

    Correctness baseline only — exploits the sorted inputs not at all. Listed
    here to make the three-pointer version's advantage tangible.

    Time:  O((m + n) log (m + n)) — Timsort on the whole buffer.
    Space: O(1)                   — sort is in place (ignoring Timsort's tiny
                                    O(log n) auxiliary stack).

    Args:
        nums1 (list[int]): Buffer of length ``m + n``.
        m (int): Real element count in ``nums1``.
        nums2 (list[int]): Sorted source of length ``n``.
        n (int): Element count in ``nums2``.

    Returns:
        None: ``nums1`` is mutated in place.
    """
    # Drop the scratch zeros, append nums2, sort. A slice assignment mutates
    # nums1 in place rather than rebinding the name.
    nums1[m:] = nums2
    nums1.sort()


# ---------------------------------------------------------------------------
# Demo / manual test harness  (section/check live in leetcode/_demo.py)
#
# To run:  make run N=88
# ---------------------------------------------------------------------------

from _demo import section, check

if __name__ == "__main__":
    section("1. Basic cases (both approaches agree)")
    for fn in (merge, merge_copy_sort):
        name = fn.__name__

        a1 = [1, 2, 3, 0, 0, 0]
        fn(a1, 3, [2, 5, 6], 3)
        check(f"{name}([1,2,3,_,_,_], 3, [2,5,6], 3)", a1, [1, 2, 2, 3, 5, 6])

        a2 = [1]
        fn(a2, 1, [], 0)
        check(f"{name}([1], 1, [], 0)", a2, [1])

        a3 = [0]
        fn(a3, 0, [1], 1)
        check(f"{name}([0], 0, [1], 1)", a3, [1])

    section("2. Edge cases")
    cases = [
        ("nums2 fully smaller", [6, 7, 8, 0, 0, 0], 3, [1, 2, 3], 3,
         [1, 2, 3, 6, 7, 8]),
        ("nums2 fully larger", [1, 2, 3, 0, 0, 0], 3, [7, 8, 9], 3,
         [1, 2, 3, 7, 8, 9]),
        ("interleaved", [1, 3, 5, 0, 0, 0], 3, [2, 4, 6], 3,
         [1, 2, 3, 4, 5, 6]),
        ("negatives", [-3, -1, 0, 0], 2, [-2, 4], 2, [-3, -2, -1, 4]),
        ("both empty (m=0, n=0)", [0], 0, [], 0, [0]),
        ("duplicates across both", [1, 1, 0, 0], 2, [1, 1], 2, [1, 1, 1, 1]),
        ("nums1 prefix exhausted first", [5, 0, 0], 1, [1, 2], 2, [1, 2, 5]),
    ]
    for label, buf, m, src, n, expected in cases:
        merge(buf, m, src, n)
        check(label, buf, expected)

    section("Demo complete")
