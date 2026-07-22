"""283. Move Zeroes

Given an integer array ``nums``, move all ``0``'s to the end while maintaining
the relative order of the non-zero elements. The move must be done in place
without making a copy of the array.

LeetCode: https://leetcode.com/problems/move-zeroes/
Difficulty: Easy

Documents two fast/slow overwrite variants: one that writes zeroes in a second
pass (simplest to reason about) and one that swaps instead, answering the
follow-up by minimising the total number of write operations.
"""

"""
Problem:

    Given an integer array nums, move all 0's to the end of it while maintaining
    the relative order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.

    Example 1:
        Input:  nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]

    Example 2:
        Input:  nums = [0]
        Output: [0]

    Constraints:
        1 <= nums.length <= 10^4
        -2^31 <= nums[i] <= 2^31 - 1

    Follow up: Could you minimize the total number of operations done?
"""

"""
Overwrite, Don't Shift:
    Moving a zero out of the middle by shifting everything after it right by one
    is O(n) *per zero*, compounding to O(n^2). The overwrite technique avoids
    shifting entirely: scan once with a write pointer and copy each non-zero
    forward into the next kept slot, then fill the tail with zeroes. One pass to
    partition, one pass to zero-fill — O(n) total.
"""

"""
Fast & Slow Pointers (Two-Pass Overwrite):
    ``slow`` is the next slot to receive a kept (non-zero) value; ``fast`` scans
    every element. Each time ``fast`` sees a non-zero it is copied into
    ``nums[slow]`` and ``slow`` advances. After the scan the prefix
    ``[0..slow)`` holds every non-zero in original order; a second loop fills
    ``[slow..n)`` with zeroes. The invariant is "everything before ``slow`` is a
    non-zero in encounter order". Simple and obviously correct.
"""

"""
Fast & Slow Pointers (One-Pass Swap — Fewer Writes):
    The follow-up asks to minimise total operations. The two-pass version does
    exactly ``k`` copies plus ``(n - k)`` zero-writes — but when ``slow`` and
    ``fast`` are far apart, many of those copies are redundant: ``fast`` reads a
    non-zero, writes it forward, and a *separate* pass later writes a zero into
    the hole it left. The swap variant folds both into one: swap
    ``nums[slow]`` with ``nums[fast]`` so the non-zero moves forward *and* the
    zero moves back in a single operation. The guard ``slow != fast`` skips the
    self-swap when the two pointers coincide (no zeroes have been seen yet), so
    only positions that actually hold a zero are touched. Worst case still O(n)
    swaps, but never more than the two-pass version's ``(k + n - k)`` writes and
    often fewer in practice.
"""

"""
In Place (No Output Array):
    The move must happen inside ``nums`` with no copy of the array. Both
    approaches below keep extra space at O(1): only index variables are used.
"""

"""
Time-Space Trade-off:
    - Two-pass overwrite: O(n) time, O(1) space — k copies + (n-k) zero-writes;
      simplest to reason about.
    - One-pass swap     : O(n) time, O(1) space — at most k swaps; minimises
      total writes (answers the follow-up).
"""

"""
0283_move_zeroes module/
|
|-- move_zeroes()       # two-pass overwrite — O(n) time, O(1) space
`-- move_zeroes_swap()  # one-pass swap      — O(n) time, O(1) space (fewer writes)
"""


def move_zeroes(nums):
    """Move all zeroes in ``nums`` to the end, preserving non-zero order.

    Two-pass overwrite: ``slow`` is the next kept slot, ``fast`` scans. Each
    non-zero is copied into ``nums[slow]``; after the scan the tail is filled
    with zeroes.

    Time:  O(n)   — one scan + one zero-fill pass.
    Space: O(1)   — only the ``slow`` index.

    Args:
        nums (list[int]): The list to compact. Mutated in place.

    Returns:
        None: Non-zeroes shifted to the front (in order), zeroes to the back.
    """
    slow = 0  # Invariant: nums[0..slow-1] holds non-zeroes in encounter order.

    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1

    # Fill the remaining tail with zeroes.
    for i in range(slow, len(nums)):
        nums[i] = 0


def move_zeroes_swap(nums):
    """Move all zeroes in ``nums`` to the end via single-pass swaps.

    One-pass swap (answers the follow-up): when ``fast`` finds a non-zero, swap
    it with ``nums[slow]`` and advance ``slow``. The swap carries the non-zero
    forward *and* the zero backward in one operation, so no second zero-fill
    pass is needed. The ``slow != fast`` guard skips self-swaps while no zero
    has been encountered yet, avoiding needless writes.

    Time:  O(n)   — one pass.
    Space: O(1)   — only the ``slow`` index.

    Args:
        nums (list[int]): The list to compact. Mutated in place.

    Returns:
        None: Non-zeroes shifted to the front (in order), zeroes to the back.
    """
    slow = 0  # Invariant: nums[0..slow-1] holds non-zeroes in encounter order.

    for fast in range(len(nums)):
        if nums[fast] != 0:
            # Skip the self-swap while the two pointers track each other (no
            # zero seen yet) — avoids a redundant write to the same slot.
            if slow != fast:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


# ---------------------------------------------------------------------------
# Demo / manual test harness  (section/check live in leetcode/_demo.py)
#
# To run:  make run N=283
# ---------------------------------------------------------------------------

from _demo import section, check


if __name__ == "__main__":
    section("1. Basic cases (both approaches agree)")
    for fn in (move_zeroes, move_zeroes_swap):
        name = fn.__name__

        a = [0, 1, 0, 3, 12]
        fn(a)
        check(f"{name}([0,1,0,3,12])", a, [1, 3, 12, 0, 0])

        b = [0]
        fn(b)
        check(f"{name}([0])", b, [0])

    section("2. Edge cases")
    cases = [
        ("no zeroes [1,2,3]",      [1, 2, 3],       [1, 2, 3]),
        ("all zeroes [0,0,0]",     [0, 0, 0],       [0, 0, 0]),
        ("zero at front [0,1,2]",  [0, 1, 2],       [1, 2, 0]),
        ("zero at back [1,2,0]",   [1, 2, 0],       [1, 2, 0]),
        ("zero in middle [1,0,2]", [1, 0, 2],       [1, 2, 0]),
        ("alternating [0,1,0,2,0]",[0, 1, 0, 2, 0], [1, 2, 0, 0, 0]),
        ("two elements [0,1]",     [0, 1],          [1, 0]),
        ("two elements [1,0]",     [1, 0],          [1, 0]),
        ("negatives [0,-1,0,-2]",  [0, -1, 0, -2],  [-1, -2, 0, 0]),
    ]
    for label, inp, expected in cases:
        move_zeroes(inp)
        check(label, inp, expected)

    section("Demo complete")
