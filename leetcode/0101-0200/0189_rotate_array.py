"""189. Rotate Array

Given an integer array ``nums``, rotate it to the right by ``k`` steps in place.
Return nothing — ``nums`` is mutated directly.

LeetCode: https://leetcode.com/problems/rotate-array/
Difficulty: Medium

The follow-up asks for as many solutions as possible and an O(1)-space in-place
answer. This file shows three: extra array (baseline), three-reverse algorithm
(preferred), and cyclic replacement (the theoretical minimum on writes). A full
concept guide for all three lives in ``array/rotation.py``.
"""

"""
Problem:

    Given an integer array nums, rotate the array to the right by k steps, where
    k is non-negative.

    Example 1:
        Input:  nums = [1,2,3,4,5,6,7], k = 3
        Output: [5,6,7,1,2,3,4]
        Explanation:
            rotate 1 steps to the right: [7,1,2,3,4,5,6]
            rotate 2 steps to the right: [6,7,1,2,3,4,5]
            rotate 3 steps to the right: [5,6,7,1,2,3,4]

    Example 2:
        Input:  nums = [-1,-100,3,99], k = 2
        Output: [3,99,-1,-100]
        Explanation:
            rotate 1 steps to the right: [99,-1,-100,3]
            rotate 2 steps to the right: [3,99,-1,-100]

    Constraints:
        1 <= nums.length <= 10^5
        -2^31 <= nums[i] <= 2^31 - 1
        0 <= k <= 10^5

    Follow up:
        - Try to come up with as many solutions as you can. There are at least
          three different ways to solve this problem.
        - Could you do it in-place with O(1) extra space?
"""

"""
Normalize k:
    Rotating by ``n`` (the array length) is a no-op, so ``k`` is reduced modulo
    ``n`` first: ``k %= n``. Without this, ``k = 0`` or ``k = n`` would waste
    work, and ``k > n`` would do redundant full laps. After normalization
    ``0 <= k < n``, which also guarantees the GCD math for cyclic replacement
    stays well-behaved.
"""

"""
Extra Array (Baseline):
    The trivial answer: allocate a fresh array and place each element directly
    at ``new[(i + k) % n] = old[i]``, then copy back. O(n) extra space — it
    ignores the in-place follow-up entirely. Kept as a correctness baseline and
    to make the O(1)-space advantage of the other two approaches concrete.
"""

"""
Three-Reverse Algorithm:
    The preferred O(1)-space answer. Rotating right by ``k`` is equivalent to:
    (1) reverse the whole array, (2) reverse the first ``k`` elements,
    (3) reverse the remaining ``n - k``. Each reverse is the opposite-end
    two-pointer swap from ``array/pointers.py::reverse_inplace``, so the whole
    rotation is that primitive applied three times — no temp-array, no cycle
    tracking, no GCD. It touches each element twice vs. cyclic replacement's
    once, but it is far easier to get right and has excellent cache locality. A
    full walkthrough lives in ``array/rotation.py``.
"""

"""
Cyclic Replacement (Juggling):
    The theoretical-minimum on writes: every element is placed exactly once
    (``n`` total writes vs. the three-reverse algorithm's ~2n). An element at
    index ``i`` moves to ``(i + k) % n``; repeatedly applying that mapping forms
    closed cycles, and the array partitions into ``gcd(n, k)`` of them. Walk
    each cycle with a single temp variable: stash the start value, then push it
    to its target, grab the displaced value, and repeat until the cycle closes.
    O(1) space, O(n) time. Tricky to implement correctly; see
    ``array/rotation.py`` for the full guide including the GCD proof and the
    temp-variable dance.
"""

"""
Time-Space Trade-off:
    - Extra array       : O(n) time, O(n) space — simplest; ignores in-place.
    - Three-reverse     : O(n) time, O(1) space — 2n writes; preferred in
                          practice (simple, cache-friendly).
    - Cyclic replacement: O(n) time, O(1) space — n writes (each element placed
                          once); the theoretical minimum, but trickier.
"""

"""
0189_rotate_array module/
|
|-- rotate_extra()   # extra-array baseline — O(n) time, O(n) space
|-- rotate_reverse() # three-reverse alg.  — O(n) time, O(1) space
`-- rotate_cyclic()  # cyclic replacement  — O(n) time, O(1) space
"""


def rotate_extra(nums, k):
    """Rotate ``nums`` right by ``k`` using a fresh array (correctness baseline).

    Places each element directly at its target index in a new array, then copies
    back. O(n) extra space — ignores the in-place follow-up.

    Time:  O(n) — two passes (place, copy back).
    Space: O(n) — a fresh array of length ``n``.

    Args:
        nums (list[int]): The array to rotate. Mutated in place (via copy-back).
        k (int):          Steps to rotate right (normalized mod ``n``).

    Returns:
        None: ``nums`` is rotated in place.
    """
    n = len(nums)
    if n == 0:
        return

    k %= n

    result = [0] * n
    for i in range(n):
        result[(i + k) % n] = nums[i]

    nums[:] = result


def rotate_reverse(nums, k):
    """Rotate ``nums`` right by ``k`` in place using the three-reverse algorithm.

    (1) Reverse the whole array, (2) reverse the first ``k`` elements,
    (3) reverse the remaining ``n - k``. Each reverse is a simple opposite-end
    swap, so the whole rotation uses O(1) extra space. This is the preferred
    in-place answer — simple, correct, and cache-friendly.

    Time:  O(n) — each element is swapped ~twice total.
    Space: O(1) — the reverse helper uses only indices.

    Args:
        nums (list[int]): The array to rotate. Mutated in place.
        k (int):          Steps to rotate right (normalized mod ``n``).

    Returns:
        None: ``nums`` is rotated in place.
    """
    n = len(nums)
    if n == 0:
        return

    k %= n
    if k == 0:
        return

    def reverse(lo, hi):
        """Reverse nums[lo..hi] in place via opposite-end swaps."""
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1

    reverse(0, n - 1)   # Step 1: reverse the entire array.
    reverse(0, k - 1)   # Step 2: reverse the first k elements.
    reverse(k, n - 1)   # Step 3: reverse the remaining n-k elements.


def rotate_cyclic(nums, k):
    """Rotate ``nums`` right by ``k`` in place using cyclic replacement.

    Walks each of the ``gcd(n, k)`` independent cycles with a single temp
    variable: stash the start value, push it to its target ``(i + k) % n``,
    grab the displaced value, and repeat until the cycle closes. Each element
    is placed exactly once — the theoretical minimum on writes.

    Time:  O(n) — exactly ``n`` placements.
    Space: O(1) — one temp variable and a few indices.

    Args:
        nums (list[int]): The array to rotate. Mutated in place.
        k (int):          Steps to rotate right (normalized mod ``n``).

    Returns:
        None: ``nums`` is rotated in place.
    """
    n = len(nums)
    if n == 0:
        return

    k %= n
    if k == 0:
        return

    # Euclid's algorithm — tells us how many independent cycles to walk.
    a, b = n, k
    while b:
        a, b = b, a % b
    cycles = a

    for start in range(cycles):
        current = start
        temp = nums[start]

        while True:
            nxt = (current + k) % n
            nums[nxt], temp = temp, nums[nxt]  # Place temp, grab displaced.
            current = nxt

            if current == start:  # Cycle closed.
                break


# ---------------------------------------------------------------------------
# Demo / manual test harness  (section/check live in leetcode/_demo.py)
#
# To run:  make run N=189
# ---------------------------------------------------------------------------

from _demo import section, check


if __name__ == "__main__":
    section("1. Basic cases (all three approaches agree)")
    for fn in (rotate_extra, rotate_reverse, rotate_cyclic):
        name = fn.__name__

        a = [1, 2, 3, 4, 5, 6, 7]
        fn(a, 3)
        check(f"{name}([1..7], 3)", a, [5, 6, 7, 1, 2, 3, 4])

        b = [-1, -100, 3, 99]
        fn(b, 2)
        check(f"{name}([-1,-100,3,99], 2)", b, [3, 99, -1, -100])

    section("2. Edge cases")
    cases = [
        ("k = 0 (no-op)",        [1, 2, 3],       0, [1, 2, 3]),
        ("k = n (full lap)",     [1, 2, 3],       3, [1, 2, 3]),
        ("k > n (10 on len 7)",  [1, 2, 3, 4, 5, 6, 7], 10, [5, 6, 7, 1, 2, 3, 4]),
        ("k = 1",                [1, 2, 3, 4],    1, [4, 1, 2, 3]),
        ("k = n-1",              [1, 2, 3, 4],    3, [2, 3, 4, 1]),
        ("single element",       [42],            5, [42]),
        ("two elements k=1",     [1, 2],          1, [2, 1]),
        ("all same value",       [0, 0, 0, 0],    2, [0, 0, 0, 0]),
        ("with negatives",       [-1, -100, 3, 99], 2, [3, 99, -1, -100]),
    ]
    for label, arr, k, expected in cases:
        for fn in (rotate_extra, rotate_reverse, rotate_cyclic):
            a = arr[:]
            fn(a, k)
            check(f"{fn.__name__}: {label}", a, expected)

    section("Demo complete")
