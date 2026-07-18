"""349. Intersection of Two Arrays

Given two integer arrays ``nums1`` and ``nums2``, return their intersection —
the unique values present in both — in any order.

LeetCode: https://leetcode.com/problems/intersection-of-two-arrays/
Difficulty: Easy

Documents the two-set approach: turn one array into a lookup set, then collect
members of the other that appear in it.
"""

"""
Problem:

    Given two integer arrays nums1 and nums2, return an array of their
    intersection. Each element in the result must be unique and you may return
    the result in any order.

    Example 1:
        Input:  nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2]

    Example 2:
        Input:  nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        Output: [9,4]
        Explanation: [4,9] is also accepted.

    Constraints:
        1 <= nums1.length, nums2.length <= 1000
        0 <= nums1[i], nums2[i] <= 1000
"""

"""
Set Intersection:
    The intersection of two collections is the set of values that belong to
    both. Repeats inside either input don't matter — only membership does — so
    the result is naturally a set of distinct values, matching the problem's
    "each element must be unique" requirement.
"""

"""
Hash Set as Lookup:
    A hash set stores unique values with average O(1) membership tests. Building
    one set from the first array and walking the second turns "is this value in
    the other array?" into a constant-time question — no nested scan, no need to
    repeatedly search.
"""

"""
Result Set:
    Collecting matches into a second set (rather than a list) deduplicates
    automatically: even if a value occurs many times in nums1, it lands in the
    result once. We materialise it as a list only at the end, since callers
    expect a sequence.
"""

"""
Time-Space Trade-off:
    - Two sets (recommended): O(n + m) time, O(n + m) space — one lookup set
      plus a result set; the obvious hash-based solution.
    - Built-in `&`         : O(n + m) time, O(n + m) space — same complexity,
      just expressed as `set(nums1) & set(nums2)`; concise and idiomatic.
    - Boolean array        : O(n + m) time, O(1001) = O(1) space — viable only
      because the constraints pin values to 0..1000; a fixed-size presence
      array replaces the lookup set. Useful when the value range is small and
      known.

    A brute-force O(n * m) nested scan is omitted: with n, m <= 1000 it would
    run up to a million comparisons for no benefit over the set approach.
"""

"""
0349_intersection_of_two_arrays module/
|
|-- intersection()          # two sets  — O(n + m) time, O(n + m) space
`-- intersection_builtin()  # set `&`   — O(n + m) time, O(n + m) space
"""


def intersection(nums1, nums2):
    """Return the unique values present in both ``nums1`` and ``nums2``.

    Builds a lookup set from ``nums2``, then walks ``nums1`` adding each value
    that the lookup contains into a result set, which deduplicates for free.

    Time:  O(n + m)   — one pass to build the lookup (m), one to scan (n).
    Space: O(n + m)   — lookup set (<= m) plus result set (<= min(n, m)).

    Args:
        nums1 (list[int]): First input array.
        nums2 (list[int]): Second input array.

    Returns:
        list[int]: The unique values appearing in both arrays, in any order.
    """
    lookup = set(nums2)   # O(m) build; O(1) average membership test.
    result = set()        # Set (not list) so repeats collapse automatically.

    for num in nums1:
        # A value in nums1 is in the intersection iff nums2 also has it.
        if num in lookup:
            result.add(num)

    return list(result)


def intersection_builtin(nums1, nums2):
    """Return the intersection of ``nums1`` and ``nums2`` using Python's set ``&``.

    `set & set` keeps every element present in both operands, discarding
    duplicates in the process — exactly the problem's specification, in one
    expression. Internally CPython does the same lookup-set walk as the manual
    version, so the complexity is identical; this is just the idiomatic spelling.

    Time:  O(n + m)   — build two sets, then intersect.
    Space: O(n + m)   — both input sets live in memory at once.

    Args:
        nums1 (list[int]): First input array.
        nums2 (list[int]): Second input array.

    Returns:
        list[int]: The unique values appearing in both arrays, in any order.
    """
    return list(set(nums1) & set(nums2))


# ---------------------------------------------------------------------------
# Demo / manual test harness  (section/check live in leetcode/_demo.py)
#
# To run:  make run N=349
# ---------------------------------------------------------------------------

from _demo import section, check

if __name__ == "__main__":
    section("1. Basic cases (both approaches agree, order-independent)")
    for fn in (intersection, intersection_builtin):
        name = fn.__name__
        # Order is unspecified, so compare via sorted() for a deterministic check.
        check(f"{name}([1,2,2,1], [2,2])",
              sorted(fn([1, 2, 2, 1], [2, 2])), [2])
        check(f"{name}([4,9,5], [9,4,9,8,4])",
              sorted(fn([4, 9, 5], [9, 4, 9, 8, 4])), [4, 9])

    section("2. Edge cases")
    check("no overlap", sorted(intersection([1, 2, 3], [4, 5, 6])), [])
    check("identical arrays", sorted(intersection([1, 2, 3], [1, 2, 3])), [1, 2, 3])
    check("nums1 subset of nums2", sorted(intersection([1, 1], [1, 2, 3])), [1])
    check("nums2 subset of nums1", sorted(intersection([1, 2, 3, 4], [2, 4])), [2, 4])
    check("single shared element", sorted(intersection([7], [7])), [7])
    check("single different element", sorted(intersection([7], [8])), [])
    check("zeroes shared", sorted(intersection([0, 0, 0], [0])), [0])
    check("duplicates in both, single match",
          sorted(intersection([5, 5, 5], [5, 5])), [5])

    section("Demo complete")
