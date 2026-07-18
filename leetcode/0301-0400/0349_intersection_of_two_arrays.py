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
Build the Lookup from the Smaller Array:
    The lookup set is queried once per element of the array we walk, but its
    build cost and footprint scale with the size of the array we hash. Hashing
    the smaller input therefore shrinks both the build pass and the lookup's
    memory without changing the result — intersection is symmetric. With the
    constraints (<= 1000 per side) this rarely matters, but it costs nothing
    and pays off when the inputs are lopsided (e.g. 5 vs 1000).
"""

"""
Time-Space Trade-off:
    - Two sets (recommended): O(n + m) time, O(min(n, m) + result) space —
      the lookup is built from the *smaller* array, so it never exceeds
      min(n, m) entries; the result set is bounded by the same.
    - Built-in `&`         : O(n + m) time, O(n + m) space — same asymptotic
      time, but CPython builds a set for *both* inputs, so memory peaks higher
      than the asymmetric version. Concise and idiomatic.
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
|-- intersection()          # two sets, smaller as lookup — O(n + m) time, O(min(n, m) + result) space
`-- intersection_builtin()  # set `&`                        — O(n + m) time, O(n + m) space
"""


def intersection(nums1, nums2):
    """Return the unique values present in both ``nums1`` and ``nums2``.

    Builds the lookup set from the *smaller* input, then walks the *larger* one
    collecting every value the lookup contains into a result set (which
    deduplicates for free). Intersection is symmetric, so the choice of which
    side to hash is purely a cost optimisation: hashing fewer elements shrinks
    both the build pass and the lookup's memory footprint.

    Time:  O(n + m)        — one pass to build the lookup (min(n, m)), one to
                             scan the other array (max(n, m)).
    Space: O(min(n, m) + r) — lookup set (<= min(n, m)) plus result set
                             (r <= min(n, m)).

    Args:
        nums1 (list[int]): First input array.
        nums2 (list[int]): Second input array.

    Returns:
        list[int]: The unique values appearing in both arrays, in any order.
    """
    # Hash the smaller array so the lookup set — and its build pass — stay
    # small. The other array is what we iterate.
    if len(nums1) < len(nums2):
        lookup = set(nums1)
        other = nums2
    else:
        lookup = set(nums2)
        other = nums1

    result = set()  # Set (not list) so repeats collapse automatically.

    for num in other:
        # A value is in the intersection iff the other array also has it.
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
