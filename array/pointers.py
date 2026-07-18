"""Pointers

An index variable that walks an array to track a position of interest — not a
memory pointer (as in C), but an integer index into the backing store. This
module documents the technique end to end: one pointer (linear scan), two
pointers (opposite ends and fast/slow), the sliding-window special case, and
three pointers (Dutch national flag, in-place merge).

Each pattern gets a concept glossary entry below and a canonical implementation
later in the file so the abstract idea has something concrete to attach to.
"""

"""
Pointer (Algorithmic):
    An integer index variable that names a position of interest inside an
    array. Unlike a C pointer (which is a raw memory address), an algorithmic
    pointer is just `i`, `left`, `right`, etc. — a slot number used to read or
    write `arr[i]`. The word "pointer" survives because the variable "points
    at" an element, and the patterns that move several of them in concert are
    what this module is about.
"""

"""
Why Pointers Beat Searching:
    A naive algorithm often re-scans the array for each element (nested loops,
    O(n^2)). Pointers let us move through the data deliberately — advancing the
    one whose element is "behind", retreating the one that's "ahead", holding
    one still while another scans — so each element is touched O(1) times and
    the whole pass is O(n). The win comes from exploiting structure (sortedness,
    a window, a partition) that the brute-force version ignores.
"""

"""
Invariant:
    A condition that is true before and after every step of a loop, even as the
    pointers move. Stating the invariant up front is how a pointer algorithm is
    reasoned about: "everything left of `slow` is unique", "everything right of
    `right` is larger than target", "lo..hi always holds the current window".
    Every pattern below carries one; the code is correct exactly while its
    invariant holds.
"""

"""
Termination:
    A pointer loop must end. The two questions to answer up front: which
    pointer(s) advance each step, and what condition stops the loop? Opposite-
    end pointers stop when they meet (`left >= right`); same-direction pointers
    usually run until the fast one falls off the end; sliding windows stop when
    `hi` reaches `n`. Getting termination right is the difference between a
    clean O(n) and an infinite loop or off-by-one.
"""

"""
Single Pointer (Linear Scan):
    One index walks the array from one end to the other, accumulating a result.
    This is the simplest pointer pattern and the building block of every other
    one: a `for i in range(n)` loop is a single pointer in disguise. Use it
    whenever the answer depends on visiting every element once, with no need to
    compare two positions at the same time — running totals, min/max, counting,
    find-first. O(n) time, O(1) space.
"""

"""
Two Pointers — Opposite Ends (Meet in the Middle):
    Place one pointer at each end and step them toward each other. The shape of
    the data (usually sorted) decides which pointer moves: in a sorted pair-sum
    the smaller side advances to grow the sum, the larger side retreats to
    shrink it; in a reverse the pointers simply swap and advance together. The
    invariant is "every unprocessed pair still straddles the live pointers", so
    the first time they cross, all relevant pairs have been considered. O(n)
    time, O(1) space. Requires sorted input when used for searching.
"""

"""
Two Pointers — Same Direction (Fast & Slow):
    Both pointers start at the same end and move the same way, but at different
    speeds or under different conditions. `slow` marks the boundary of a
    "result so far" region and only advances when the `fast` scout finds an
    element worth keeping. The invariant is "everything at or before `slow` is
    part of the answer", so when `fast` reaches the end the prefix `[0..slow]`
    holds the filtered result. Classic uses: dedupe a sorted array in place,
    move zeroes to the end, partition around a pivot. O(n) time, O(1) space.
"""

"""
Sliding Window:
    A same-direction two-pointer special case where the two pointers bound a
    contiguous subarray (the "window") that slides across the input. The
    invariant is "lo..hi-1 always holds the current window". In a FIXED-size
    window both pointers advance together by one each step — add the new
    element, drop the old one, never rescan the middle. In a VARIABLE-size
    window the pointers move independently: expand `hi` to grow the window,
    shrink `lo` to restore an invariant (sum <= k, all-distinct, etc.). O(n)
    time, O(k) or O(1) space depending on what bookkeeping the window needs.
"""

"""
Three Pointers:
    When the problem has three regions to track at once, a third pointer joins
    the dance. The flagship example is the Dutch national flag partition: sort
    an array of 0/1/2 (or "less than / equal to / greater than pivot") in one
    pass with three pointers — `lo` for the next 0 slot, `hi` for the next 2
    slot, and a scanning `mid` walking between them. The invariant is "before
    `lo` is all 0s, after `hi` is all 2s, between them is unprocessed or 1s".
    Three pointers also appear in in-place merges (read-i, read-j, write-k) —
    see leetcode/0001-0100/0088_merge_sorted_array.py for that pattern.
"""

"""
Sortedness Requirement:
    Opposite-end searching (pair-sum, palindrome-style comparisons after
    normalisation, etc.) relies on the data being ordered: that ordering is
    what tells you which pointer to move and guarantees you never need to
    backtrack. Fast/slow and sliding-window patterns do NOT need sorted input —
    they exploit positional structure (adjacency, a window) instead. Mistaking
    the two is a classic bug: applying meet-in-the-middle to unsorted data
    silently returns wrong answers.
"""

"""
Time-Space Trade-off:
        - Single pointer        : O(n) time, O(1) space — visit-everything pass.
        - Opposite ends         : O(n) time, O(1) space — needs sorted input.
        - Same direction        : O(n) time, O(1) space — in-place filtering.
        - Sliding window        : O(n) time, O(1) space — subarray queries.
        - Three pointers        : O(n) time, O(1) space — three-way partition.

    Every pattern above is O(n) time and O(1) space: the whole point of using
    pointers instead of nested loops or extra arrays is to keep the cost linear
    and constant. The brute-force alternatives they replace are usually O(n^2)
    time or O(n) space.
"""

"""
pointers module/
|
|-- linear_max()               # single pointer      — O(n) time, O(1) space
|-- reverse_inplace()          # opposite ends       — O(n) time, O(1) space
|-- has_pair_sum_sorted()      # opposite ends       — O(n) time, O(1) space
|-- remove_duplicates_sorted() # fast & slow         — O(n) time, O(1) space
|-- move_zeroes()              # fast & slow         — O(n) time, O(1) space
|-- max_window_sum()           # fixed sliding       — O(n) time, O(1) space
`-- dutch_flag_sort()          # three pointers      — O(n) time, O(1) space
"""


# ---------------------------------------------------------------------------
# 1. Single pointer
# ---------------------------------------------------------------------------

def linear_max(arr):
    """Return the largest value in ``arr`` using a single-pointer scan.

    One index walks the array once, carrying the largest value seen so far.
    Textbook single pointer: visit every element, accumulate, done.

    Time:  O(n) — one pass.
    Space: O(1) — only the running maximum.

    Args:
        arr (list[int]): Non-empty list of integers.

    Returns:
        int: The maximum element.
    """
    best = arr[0]  # Sentinel: the first element is the max of a one-element scan.

    # One pointer, i, marches from the second slot to the end.
    for i in range(1, len(arr)):
        if arr[i] > best:
            best = arr[i]  # Tighten the running maximum.

    return best


# ---------------------------------------------------------------------------
# 2. Two pointers — opposite ends
# ---------------------------------------------------------------------------

def reverse_inplace(arr):
    """Reverse ``arr`` in place using two pointers at opposite ends.

    Swap the outer pair, then the next pair inward, until the pointers meet.

    Time:  O(n)   — each element is swapped once.
    Space: O(1)   — only two indices and a temp slot.

    Args:
        arr (list): The list to reverse; mutated in place.

    Returns:
        None: ``arr`` is reversed in place.
    """
    left, right = 0, len(arr) - 1

    # Invariant: arr[0..left-1] and arr[right+1..] hold the reversed ends.
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # Swap the outer pair.
        left += 1
        right -= 1


def has_pair_sum_sorted(arr, target):
    """Return True if two distinct values in SORTED ``arr`` sum to ``target``.

    Two pointers at opposite ends: too small a sum -> advance ``left`` to grow
    it; too large -> retreat ``right`` to shrink it. Sortedness is what makes
    those moves safe (no value we skipped past could ever have been the
    answer).

    Time:  O(n)   — each pointer moves at most n times total.
    Space: O(1)   — only two indices.

    Args:
        arr (list[int]): A list of integers sorted non-decreasingly.
        target (int): The desired pair sum.

    Returns:
        bool: True if some pair of distinct elements sums to ``target``.
    """
    left, right = 0, len(arr) - 1

    # Invariant: any untested pair still straddles [left, right].
    while left < right:
        current = arr[left] + arr[right]

        if current == target:
            return True
        elif current < target:
            left += 1   # Sum too small -> need a larger left operand.
        else:
            right -= 1  # Sum too large -> need a smaller right operand.

    return False


# ---------------------------------------------------------------------------
# 3. Two pointers — same direction (fast & slow)
# ---------------------------------------------------------------------------

def remove_duplicates_sorted(arr):
    """Return the count of unique values, compacting SORTED ``arr`` in place.

    Fast/slow pointers: ``slow`` is the boundary of the deduped prefix, ``fast``
    scouts ahead. Each time ``fast`` finds a value not equal to ``arr[slow]``,
    ``slow`` advances and that fresh value is written in. Duplicates are
    overwritten from behind.

    Time:  O(n)   — one pass.
    Space: O(1)   — in place.

    Args:
        arr (list[int]): A list of integers sorted non-decreasingly.

    Returns:
        int: The number of unique elements; the first that many slots of
        ``arr`` now hold those unique values in order.
    """
    if not arr:
        return 0

    slow = 0  # Invariant: arr[0..slow] is the deduped prefix.

    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1            # Make room for a new unique value.
            arr[slow] = arr[fast]

    return slow + 1  # Count = last index + 1.


def move_zeroes(arr):
    """Move every zero in ``arr`` to the end, preserving order, in place.

    Fast/slow variant where ``slow`` is the next slot to receive a non-zero.
    ``fast`` scans; whenever it sees a non-zero it is swapped into ``slow``'s
    slot, which advances. After the pass, every non-zero sits in the front
    prefix and zeroes fill the tail.

    Time:  O(n)   — one pass.
    Space: O(1)   — in place.

    Args:
        arr (list[int]): The list to compact; mutated in place.

    Returns:
        None: Non-zeroes shifted to the front, zeroes to the back.
    """
    slow = 0  # Invariant: arr[0..slow-1] holds the non-zeroes seen so far.

    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1


# ---------------------------------------------------------------------------
# 4. Sliding window (fixed size)
# ---------------------------------------------------------------------------

def max_window_sum(arr, k):
    """Return the largest sum of any contiguous subarray of length ``k``.

    Fixed-size sliding window: sum the first k elements, then slide the window
    right one slot at a time — add the new tail element, subtract the old head,
    never rescan the middle. Turns an O(n * k) brute force into O(n).

    Time:  O(n)   — one pass; each element enters and leaves the sum once.
    Space: O(1)   — only the running sum and the best so far.

    Args:
        arr (list[int]): The list to scan.
        k (int): Window size; must satisfy 1 <= k <= len(arr).

    Returns:
        int: The maximum sum of any length-k subarray.
    """
    # Seed the sum with the first window.
    window_sum = sum(arr[:k])
    best = window_sum

    # Slide: drop arr[lo], add arr[hi]. lo = hi - k tracks the leaving element.
    for hi in range(k, len(arr)):
        window_sum += arr[hi]          # New element enters on the right.
        window_sum -= arr[hi - k]      # Old element leaves on the left.
        if window_sum > best:
            best = window_sum

    return best


# ---------------------------------------------------------------------------
# 5. Three pointers (Dutch national flag)
# ---------------------------------------------------------------------------

def dutch_flag_sort(arr):
    """Sort an array of 0/1/2 in place using three pointers.

    Dutch national flag partition: ``lo`` is the next slot for a 0, ``hi`` is
    the next slot for a 2, and ``mid`` scans between them. When ``mid`` sees a 0
    it swaps with ``lo`` and both advance; when it sees a 2 it swaps with ``hi``
    and only ``hi`` retreats (the value swapped down from ``hi`` is unprocessed,
    so ``mid`` must inspect it again); a 1 is left in place and ``mid``
    advances. One pass sorts the whole array.

    Time:  O(n)   — each step advances ``mid`` or retreats ``hi``.
    Space: O(1)   — in place.

    Args:
        arr (list[int]): A list whose values are all in {0, 1, 2}.

    Returns:
        None: ``arr`` is sorted in place.
    """
    lo, mid, hi = 0, 0, len(arr) - 1

    # Invariant: arr[0..lo-1] are all 0, arr[hi+1..] are all 2,
    #            arr[lo..mid-1] are all 1, arr[mid..hi] are unprocessed.
    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1  # Already in the "ones" region; just advance.
        else:  # arr[mid] == 2
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1  # Do NOT advance mid: the swapped-in value is unprocessed.


# ---------------------------------------------------------------------------
# Demo / manual test harness
#
# One section per pattern, each showing the canonical case plus an edge case.
#
# To run:  python3 array/pointers.py   (or:  make ds FILE=array/pointers.py)
# ---------------------------------------------------------------------------

def _section(title):
    """Print a visual divider so each phase of the demo stands out."""
    print(f"\n{'=' * 60}\n {title}\n{'=' * 60}")


def _check(label, got, expected):
    """Print a labelled PASS/FAIL comparison of an actual vs. expected result."""
    status = "PASS" if got == expected else "FAIL"
    print(f"[{status}] {label:<42} got={str(got):<14} expected={expected}")


if __name__ == "__main__":
    # 1. Single pointer
    _section("1. Single pointer — linear_max()")
    _check("linear_max([3,1,4,1,5,9,2,6])", linear_max([3, 1, 4, 1, 5, 9, 2, 6]), 9)
    _check("linear_max([-5,-2,-9])", linear_max([-5, -2, -9]), -2)
    _check("linear_max([42])", linear_max([42]), 42)

    # 2. Opposite ends
    _section("2. Two pointers — opposite ends")
    a = [1, 2, 3, 4, 5]
    reverse_inplace(a)
    _check("reverse_inplace([1,2,3,4,5])", a, [5, 4, 3, 2, 1])
    b = [1, 2, 3]
    reverse_inplace(b)
    _check("reverse_inplace([1,2,3])", b, [3, 2, 1])

    _check("has_pair_sum_sorted([1,2,3,4,6], 10)",
           has_pair_sum_sorted([1, 2, 3, 4, 6], 10), True)
    _check("has_pair_sum_sorted([1,2,3,4,6], 11)",
           has_pair_sum_sorted([1, 2, 3, 4, 6], 11), False)
    _check("has_pair_sum_sorted([-3,0,1,2], -2)",
           has_pair_sum_sorted([-3, 0, 1, 2], -2), True)
    _check("has_pair_sum_sorted([1,2], 10)",
           has_pair_sum_sorted([1, 2], 10), False)

    # 3. Fast & slow
    _section("3. Two pointers — same direction (fast & slow)")
    d = [1, 1, 2, 2, 3, 4, 4, 5]
    n = remove_duplicates_sorted(d)
    _check("remove_duplicates_sorted -> count", n, 5)
    _check("remove_duplicates_sorted -> prefix", d[:n], [1, 2, 3, 4, 5])

    z = [0, 1, 0, 3, 12]
    move_zeroes(z)
    _check("move_zeroes([0,1,0,3,12])", z, [1, 3, 12, 0, 0])
    z2 = [1, 2, 3]
    move_zeroes(z2)
    _check("move_zeroes([1,2,3]) (no zeroes)", z2, [1, 2, 3])

    # 4. Sliding window
    _section("4. Sliding window — max_window_sum()")
    _check("max_window_sum([1,2,3,4,5], 3)", max_window_sum([1, 2, 3, 4, 5], 3), 12)
    _check("max_window_sum([-1,2,-3,4,-5], 2)", max_window_sum([-1, 2, -3, 4, -5], 2), 1)
    _check("max_window_sum([5], 1)", max_window_sum([5], 1), 5)

    # 5. Three pointers
    _section("5. Three pointers — dutch_flag_sort()")
    f = [2, 0, 2, 1, 1, 0]
    dutch_flag_sort(f)
    _check("dutch_flag_sort([2,0,2,1,1,0])", f, [0, 0, 1, 1, 2, 2])
    f2 = [1, 0, 2]
    dutch_flag_sort(f2)
    _check("dutch_flag_sort([1,0,2])", f2, [0, 1, 2])
    f3 = [2, 2, 2]
    dutch_flag_sort(f3)
    _check("dutch_flag_sort([2,2,2])", f3, [2, 2, 2])

    _section("Demo complete")
