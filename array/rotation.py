"""Array Rotation

Rotate an array to the right by ``k`` steps: every element shifts forward
circularly, and the last ``k`` elements wrap to the front. This module documents
the technique end to end: the trivial extra-array baseline, the elegant
three-reverse algorithm, and the star of the show — cyclic replacement (a.k.a.
juggling), which rotates in place in a single pass using O(1) space and nothing
but a single temp variable.

Each pattern gets a concept glossary entry below and a canonical implementation
later in the file so the abstract idea has something concrete to attach to.
"""

"""
Rotation (Right / Left):
    Rotating right by ``k`` means every element moves forward ``k`` slots,
    wrapping around the end — ``[1,2,3,4,5]`` rotated right by 2 becomes
    ``[4,5,1,2,3]``. Rotating left by ``k`` is the mirror: elements shift
    backward and the first ``k`` wrap to the tail. This module focuses on
    right rotation; a left rotation by ``k`` is simply a right rotation by
    ``n - k``.
"""

"""
Normalize k First:
    Rotating by ``n`` (the array length) is a no-op — every element returns to
    its own slot. The same is true for any multiple of ``n``, so ``k`` should
    be reduced modulo ``n`` before doing any work: ``k %= n``. Without this,
    ``k = n`` or ``k = 0`` would loop forever or waste time, and ``k > n``
    would do redundant full cycles. After normalization ``0 <= k < n``, which
    also guarantees the GCD and cycle-count math below stays well-behaved.
"""

"""
Index Mapping:
    Right rotation by ``k`` sends the element at index ``i`` to index
    ``(i + k) % n``. The modulo is the "wrap": once a position steps past the
    last slot it re-enters from the front. This single formula is the whole
    mechanism — every approach below is just a different way of applying it.
"""

"""
Cycle / Orbit:
    If you repeatedly apply the index mapping to a position — ``i -> (i + k) % n
    -> (i + 2k) % n -> ...`` — you eventually return to ``i``, forming a closed
    loop called a cycle (or orbit). Every index belongs to exactly one cycle;
    cycles never partially overlap (they either coincide completely or are
    disjoint). The array partitions into a set of independent cycles, and
    rotating is equivalent to rotating each cycle by one step.
"""

"""
GCD Determines Cycle Count:
    The number of distinct cycles is ``gcd(n, k)``. Here is why. After ``t``
    applications of the mapping you land at ``(i + t*k) % n``. You return to
    the start ``i`` exactly when ``t*k`` is a multiple of ``n``, and the
    *smallest* such ``t`` is ``n / gcd(n, k)`` (the cycle length). Since every
    cycle has that same length and the ``n`` indices are partitioned among
    them, the cycle count is ``n / (n / gcd(n, k)) = gcd(n, k)``. Two special
    cases make this concrete:

        - ``gcd(n, k) == 1``: a single cycle visits all ``n`` elements. One
          pass starting at index 0 rotates everything.
        - ``gcd(n, k) == n`` (i.e. ``k == 0`` after normalization): ``n``
          cycles of length 1 — every element stays put. Nothing to do.
"""

"""
Cyclic Replacement (Juggling):
    The in-place rotation technique that follows the cycles. Pick a starting
    index, remember its value in a ``temp`` variable, then walk the cycle:
    compute where ``temp`` belongs, grab the value sitting there (new
    ``temp``), place the old ``temp`` into that slot, and repeat. Each step
    places one element into its final position — no element is ever moved
    twice. When the cycle closes (the next target is the starting index), move
    on to the next unvisited cycle. Because ``gcd(n, k)`` cycles partition the
    array, starting at ``0, 1, 2, ..., gcd(n, k) - 1`` guarantees every index
    is visited exactly once.
"""

"""
The Temp Variable Dance (Step by Step):
    The mechanics of a single cycle, made concrete. Say ``n = 5``, ``k = 2``,
    and we start at index ``0`` (value ``A``):

        Step 0:  temp = nums[0] = A           (remember what we're moving)
        Step 1:  target = (0 + 2) % 5 = 2
                 swap temp with nums[2]        -> nums[2] = A, temp = C
        Step 2:  target = (2 + 2) % 5 = 4
                 swap temp with nums[4]        -> nums[4] = C, temp = E
        Step 3:  target = (4 + 2) % 5 = 1
                 swap temp with nums[1]        -> nums[1] = E, temp = B
        Step 4:  target = (1 + 2) % 5 = 3
                 swap temp with nums[3]        -> nums[3] = B, temp = D
        Step 5:  target = (3 + 2) % 5 = 0  -> back to start, cycle closes

    At closure the value still in ``temp`` (``D``) belongs at the starting
    index — place it there as the final write. The cycle is done; every slot
    in it holds its final value. Notice only ONE extra variable (``temp``) is
    used throughout — no array is allocated.
"""

"""
Move Counting (Stop Condition):
    An alternative to tracking cycle starts with GCD: simply count how many
    elements have been placed and stop after ``n``. Each step of the temp
    dance places exactly one element, so after ``n`` placements the whole
    array is rotated. If a cycle closes before ``n`` placements, bump the
    starting index by 1 and begin a new cycle. This sidesteps the GCD entirely
    at the cost of a counter variable — useful when you don't want to reason
    about ``gcd(n, k)`` up front. Both formulations are correct and produce
    identical results; the GCD version is more elegant, the counter version is
    more mechanical.
"""

"""
Three-Reverse Algorithm (Three-Point Reverse):
    A well-known O(1)-space rotation technique. Observe that rotating right by
    ``k`` is equivalent to: (1) reverse the whole array, (2) reverse the first
    ``k`` elements, (3) reverse the remaining ``n - k`` elements. Each reverse
    is the opposite-end two-pointer swap from ``pointers.py`` (see
    ``reverse_inplace``), so the entire rotation is just that primitive applied
    three times in a specific order — no temp-array, no cycle tracking, no GCD.
    It touches each element twice (once in, once out) vs. cyclic replacement's
    once, but it is far easier to get right and has excellent cache locality.
    Example (``n = 5``, ``k = 2``):

        [1,2,3,4,5]  -> reverse all   -> [5,4,3,2,1]
                      -> reverse [0:2] -> [4,5,3,2,1]
                      -> reverse [2:5] -> [4,5,1,2,3]
"""

"""
Extra Array (Baseline):
    The trivial approach: allocate a fresh array, place each element directly
    at ``new[(i + k) % n] = old[i]``, then copy back. O(n) time but O(n) extra
    space — it ignores the in-place challenge entirely. Kept here as a
    correctness baseline and to make the space advantage of the other two
    approaches concrete.
"""

"""
Time-Space Trade-off:
        - Extra array       : O(n) time, O(n) space — simplest; ignores in-place.
        - Three-reverse     : O(n) time, O(1) space — 2n writes; cache-friendly;
        - Cyclic replacement: O(n) time, O(1) space — n writes (each element
                              placed once); the theoretical minimum, but trickier
                              to implement correctly.

    All three are O(n) time. The cyclic approach wins on raw write count
    (exactly ``n`` placements vs. the three-reverse algorithm's ~2n); the
    three-reverse algorithm wins on simplicity and cache behaviour. In practice
    the three-reverse algorithm is almost always preferred unless the
    write-count difference is critical.
"""

"""
rotation module/
|
|-- _gcd()                  # Euclidean algorithm   — helper for cyclic approach
|-- _reverse_range()        # in-place reverse      — helper for the three-reverse algorithm
|-- rotate_cyclic()         # cyclic replacement    — O(n) time, O(1) space (GCD-based)
|-- rotate_cyclic_compact() # cyclic replacement    — O(n) time, O(1) space (counter-based)
|-- rotate_reverse()        # three-reverse algorithm — O(n) time, O(1) space
`-- rotate_extra()          # extra-array baseline  — O(n) time, O(n) space
"""


def _gcd(a, b):
    """Return the greatest common divisor of ``a`` and ``b`` (Euclid's algorithm).

    Repeatedly replace the larger operand with its remainder when divided by
    the smaller, until one of them reaches zero. The other is the GCD. This
    tells cyclic replacement how many independent cycles the array splits into.

    Time:  O(log(min(a, b))).
    Space: O(1).
    """
    while b:
        a, b = b, a % b
    return a


def _reverse_range(nums, lo, hi):
    """Reverse ``nums[lo:hi]`` in place using opposite-end swaps.

    ``lo`` is inclusive, ``hi`` is exclusive. Used by the three-reverse
    rotation technique to reverse the whole array, then the two halves.

    Time:  O(hi - lo) — each element in the range is swapped once.
    Space: O(1)       — two indices and a temp.
    """
    left, right = lo, hi - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def rotate_cyclic(nums, k):
    """Rotate ``nums`` right by ``k`` in place using cyclic replacement.

    Walks each of the ``gcd(n, k)`` independent cycles. For every cycle: stash
    the starting value in ``temp``, then repeatedly jump to the target index
    ``(current + k) % n``, swap ``temp`` into that slot (placing one element
    home) and take the displaced value as the new ``temp``. When the next
    target is the cycle's start, the cycle is closed. Each element is placed
    exactly once.

    Time:  O(n)   — exactly ``n`` placements total across all cycles.
    Space: O(1)   — one ``temp`` variable, a few indices, and the GCD.

    Args:
        nums (list): The list to rotate. Mutated in place.
        k (int):     Number of steps to rotate right (normalized mod ``n``).

    Returns:
        None: ``nums`` is rotated in place.
    """
    n = len(nums)
    if n == 0:
        return

    k %= n  # Normalize: rotating by n (or a multiple) is a no-op.
    if k == 0:
        return

    cycles = _gcd(n, k)  # Number of independent cycles to walk.

    for start in range(cycles):
        current = start
        temp = nums[start]  # Stash the first value; its slot is now "open".

        # Walk the cycle: push temp to its target, grab the displaced value,
        # advance. Stop when we return to the cycle's start.
        while True:
            nxt = (current + k) % n
            nums[nxt], temp = temp, nums[nxt]  # Place temp, grab displaced.
            current = nxt

            if current == start:  # Cycle closed — on to the next one.
                break


def rotate_cyclic_compact(nums, k):
    """Rotate ``nums`` right by ``k`` via cyclic replacement (compact swap form).

    Same algorithm as :func:`rotate_cyclic` but expressed with a count-based
    stop condition (no GCD needed) and a single swap per step. ``counted``
    tracks total placements; the loop runs until all ``n`` elements are placed.
    If a cycle closes early, the next start index is tried.

    Time:  O(n)   — exactly ``n`` placements.
    Space: O(1)   — temp, two indices, and a counter.
    """
    n = len(nums)
    if n == 0:
        return

    k %= n
    if k == 0:
        return

    placed = 0  # Total elements placed in their final position so far.
    start = 0   # Starting index of the current cycle.

    while placed < n:
        current = start
        temp = nums[start]

        while True:
            nxt = (current + k) % n
            nums[nxt], temp = temp, nums[nxt]  # Place temp, grab displaced.
            current = nxt
            placed += 1

            if current == start:  # Cycle closed — move to the next cycle.
                break

        start += 1


def rotate_reverse(nums, k):
    """Rotate ``nums`` right by ``k`` in place using the three-reverse algorithm.

    (1) Reverse the whole array, (2) reverse the first ``k`` elements,
    (3) reverse the remaining ``n - k``. Each reverse is a simple opposite-end
    swap, so the whole rotation uses O(1) extra space.

    Time:  O(n)   — each element is swapped ~twice total.
    Space: O(1)   — the reverse helper uses only indices.

    Args:
        nums (list): The list to rotate. Mutated in place.
        k (int):     Number of steps to rotate right (normalized mod ``n``).

    Returns:
        None: ``nums`` is rotated in place.
    """
    n = len(nums)
    if n == 0:
        return

    k %= n
    if k == 0:
        return

    _reverse_range(nums, 0, n)   # Reverse the entire array.
    _reverse_range(nums, 0, k)   # Reverse the first k elements.
    _reverse_range(nums, k, n)   # Reverse the remaining n-k elements.


def rotate_extra(nums, k):
    """Rotate ``nums`` right by ``k`` using a fresh array (correctness baseline).

    Places each element directly at its target index in a new array, then
    copies back. O(n) extra space — ignores the in-place challenge.

    Time:  O(n)   — two passes (place, copy back).
    Space: O(n)   — a fresh array of length ``n``.

    Args:
        nums (list): The list to rotate. Mutated in place (via copy-back).
        k (int):     Number of steps to rotate right (normalized mod ``n``).

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

    nums[:] = result  # Copy back in place.


# ---------------------------------------------------------------------------
# Demo / manual test harness
#
# One section per pattern, each showing the canonical case plus edge cases.
# All three rotation approaches are cross-checked against each other.
#
# To run:  python3 array/rotation.py   (or:  make ds FILE=array/rotation.py)
# ---------------------------------------------------------------------------

def _section(title):
    """Print a visual divider so each phase of the demo stands out."""
    print(f"\n{'=' * 60}\n {title}\n{'=' * 60}")


def _check(label, got, expected):
    """Print a labelled PASS/FAIL comparison of an actual vs. expected result."""
    status = "PASS" if got == expected else "FAIL"
    print(f"[{status}] {label:<46} got={str(got):<20} expected={expected}")


if __name__ == "__main__":
    # --- 1. All approaches agree on the canonical case -------------------
    _section("1. Cross-check: right-rotate [1,2,3,4,5] by 2")
    for fn in (rotate_cyclic, rotate_cyclic_compact, rotate_reverse, rotate_extra):
        a = [1, 2, 3, 4, 5]
        fn(a, 2)
        _check(f"{fn.__name__}([1,2,3,4,5], 2)", a, [4, 5, 1, 2, 3])

    # --- 2. Temp-dance walkthrough (single cycle, gcd=1) -----------------
    _section("2. Temp-dance walkthrough (n=5, k=2 -> one cycle of 5)")
    print("Start:  [1, 2, 3, 4, 5]   (values A B C D E)")
    print()
    print("  temp=A; current=0")
    print("  -> place A at (0+2)%5=2, grab C   [1,2,A,4,5]  temp=C")
    print("  -> place C at (2+2)%5=4, grab E   [1,2,A,4,C]  temp=E")
    print("  -> place E at (4+2)%5=1, grab B   [1,E,A,4,C]  temp=B")
    print("  -> place B at (1+2)%5=3, grab D   [1,E,A,B,C]  temp=D")
    print("  -> D goes home at (3+2)%5=0       [D,E,A,B,C]")
    print()
    # Verify: right-rotate [A,B,C,D,E] by 2 should give [D,E,A,B,C].
    vals = ["A", "B", "C", "D", "E"]
    rotate_reverse(vals[:], 0)  # warm up (no-op)
    result = vals[:]
    rotate_reverse(result, 2)
    print(f"  verify rotate_reverse([A,B,C,D,E], 2) = {result}")

    # --- 3. Multi-cycle case (gcd > 1) -----------------------------------
    _section("3. Multi-cycle case (n=6, k=2 -> gcd=2 cycles)")
    print("gcd(6, 2) = 2 independent cycles, each of length 3:")
    print("  cycle 0: 0 -> 2 -> 4 -> 0")
    print("  cycle 1: 1 -> 3 -> 5 -> 1")
    b = [1, 2, 3, 4, 5, 6]
    rotate_cyclic(b, 2)
    _check("rotate_cyclic([1,2,3,4,5,6], 2)", b, [5, 6, 1, 2, 3, 4])

    # --- 4. Edge cases ---------------------------------------------------
    _section("4. Edge cases")
    cases = [
        ("k = 0 (no-op)",        [1, 2, 3],       0, [1, 2, 3]),
        ("k = n (full lap)",     [1, 2, 3],       3, [1, 2, 3]),
        ("k > n (7 on len 3)",   [1, 2, 3],       7, [3, 1, 2]),
        ("k = 1",                [1, 2, 3, 4],    1, [4, 1, 2, 3]),
        ("k = n-1",              [1, 2, 3, 4],    3, [2, 3, 4, 1]),
        ("single element",       [42],            5, [42]),
        ("two elements k=1",     [1, 2],          1, [2, 1]),
        ("with negatives",       [-1, -100, 3, 99], 2, [3, 99, -1, -100]),
    ]
    for label, arr, k, expected in cases:
        for fn in (rotate_cyclic, rotate_reverse, rotate_extra):
            a = arr[:]
            fn(a, k)
            _check(f"{fn.__name__}: {label}", a, expected)

    _section("Demo complete")
