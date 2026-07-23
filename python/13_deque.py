"""deque (Double-Ended Queue)

``collections.deque`` — a list-like sequence optimized for fast additions and
removals at *both* ends. The stack/queue workhorse that beats ``list`` when
you need O(1) operations at the front.
"""

"""
deque:
    A double-ended queue from the ``collections`` module. Supports O(1)
    ``append`` and ``pop`` at the *right* end (like a list), AND O(1) ``appendleft``
    and ``popleft`` at the *left* end (which a list cannot do — ``list.pop(0)``
    and ``list.insert(0, x)`` are O(n) because every element must shift).
"""

"""
list vs deque:
    For a pure STACK (push/pop at one end), ``list`` and ``deque`` are both
    O(1) — use whichever you prefer. For a QUEUE (push at back, pop from front)
    or any pattern that touches the front, ``deque`` wins decisively:
    ``deque.popleft()`` is O(1); ``list.pop(0)`` is O(n).

        Operation        list        deque
        append right     O(1)        O(1)
        pop right        O(1)        O(1)
        append left      O(n)        O(1)   <- deque wins
        pop left         O(n)        O(1)   <- deque wins
        random access    O(1)        O(n)   <- list wins
"""

"""
Internals (Doubly Linked List):
    A ``deque`` is implemented as a doubly-linked list of fixed-size blocks
    (not a single contiguous array like ``list``). This is why both ends are
    O(1) — adding/removing at either end just updates a pointer, no shifting.
    The trade-off: random access (``d[5000]``) is O(n) because it must walk
    the blocks, vs. O(1) for ``list``.
"""

"""
maxlen (Bounded deque):
    ``deque(maxlen=n)`` automatically discards from the opposite end when full.
    ``append`` past the limit silently drops the oldest item. Useful for ring
    buffers, sliding windows, and "keep last N" patterns without manual eviction.
"""


if __name__ == "__main__":
    from collections import deque

    def _s(t): print(f"\n{'=' * 40}\n {t}\n{'=' * 40}")

    _s("Creation")
    d = deque([1, 2, 3])
    empty = deque()
    print(f"deque([1,2,3]) = {d}")
    print(f"deque()        = {empty}")

    _s("Right end (same as list — stack usage)")
    d.append(4)
    print(f"append(4)  -> {d}")
    val = d.pop()
    print(f"pop() -> {val}, d = {d}")

    _s("Left end (deque's advantage — queue usage)")
    d.appendleft(0)
    print(f"appendleft(0) -> {d}")
    val = d.popleft()
    print(f"popleft() -> {val}, d = {d}")

    _s("Stack pattern (LIFO) — list or deque both O(1)")
    stack = deque()
    stack.append("a")
    stack.append("b")
    stack.append("c")
    print(f"stack: {stack}")
    print(f"pop:   {stack.pop()}")    # c
    print(f"pop:   {stack.pop()}")    # b
    print(f"stack: {stack}")

    _s("Queue pattern (FIFO) — deque wins O(1) vs list O(n)")
    queue = deque()
    queue.append("first")
    queue.append("second")
    queue.append("third")
    print(f"queue:   {queue}")
    print(f"popleft: {queue.popleft()}")   # first
    print(f"popleft: {queue.popleft()}")   # second
    print(f"queue:   {queue}")

    _s("maxlen — bounded deque (auto-evicts)")
    recent = deque(maxlen=3)
    for i in range(5):
        recent.append(i)
        print(f"  append({i}) -> {recent}")
    print("(oldest items silently dropped once maxlen is reached)")

    _s("Why NOT to use list.pop(0)")
    import time
    n = 100_000
    lst = list(range(n))
    dq = deque(range(n))
    t1 = time.perf_counter()
    for _ in range(1000):
        lst.pop(0)
    list_time = time.perf_counter() - t1
    t2 = time.perf_counter()
    for _ in range(1000):
        dq.popleft()
    deque_time = time.perf_counter() - t2
    print(f"1000 x list.pop(0):   {list_time:.4f}s")
    print(f"1000 x deque.popleft(): {deque_time:.6f}s")
    print(f"deque is ~{list_time / max(deque_time, 1e-9):.0f}x faster")

    _s("Demo complete")
