"""Sets

Python's mutable, unordered collection of unique, hashable elements — the
built-in that ``data_structures/hash_map.py::HashSet`` reimplements from
scratch. Covers membership, modification, set operations, and comprehensions.
"""

"""
Set:
    An unordered collection of *unique* elements. Created with curly braces
    ``{1, 2, 3}`` or ``set()``. Duplicates are silently dropped. Elements must
    be hashable (ints, strings, tuples-of-hashables — but not lists or dicts).
    Under the hood, a set is a hash map with no values — see
    ``data_structures/hash_map.py::HashSet``.
"""

"""
Empty Set Gotcha:
    ``{}`` creates an empty *dict*, not an empty set (braces were dicts first).
    To create an empty set, use ``set()`` explicitly.
"""

"""
O(1) Membership:
    ``x in my_set`` is average O(1) — a hash lookup — vs. ``x in my_list`` which
    is O(n). This is the single biggest reason to use sets: if you are doing
    repeated membership tests, convert the list to a set first.
"""

"""
add() / remove() / discard():
    ``.add(x)`` inserts ``x`` (no-op if already present). ``.remove(x)`` deletes
    ``x`` and raises ``KeyError`` if absent. ``.discard(x)`` deletes ``x``
    silently if absent — the safe version when you are not sure the element
    exists.
"""

"""
Set Operations:
    Sets support mathematical set algebra with operators or methods:
        ``a | b``  union        — elements in either
        ``a & b``  intersection — elements in both
        ``a - b``  difference   — in a but not in b
        ``a ^ b``  symmetric diff — in exactly one
    Each has a method form too (``a.union(b)``) that accepts any iterable; the
    operator form requires both operands to be sets.
"""

"""
Set Comprehension:
    ``{expr for item in iterable if condition}`` — like a list comprehension
    but builds a set, so duplicates are automatically removed. Useful for
    extracting the unique values from a sequence.
"""


if __name__ == "__main__":
    def _s(t): print(f"\n{'=' * 40}\n {t}\n{'=' * 40}")

    _s("Creation")
    a = {1, 2, 3}
    b = set([2, 3, 4, 4, 4])  # duplicates dropped
    print(f"{{1,2,3}}        = {a}")
    print(f"set([2,3,4,4,4]) = {b}")  # {2, 3, 4}

    _s("Empty set gotcha")
    empty_set = set()
    print(f"set()  -> {empty_set}, type={type(empty_set).__name__}")
    not_a_set = {}
    print(f"{{}}    -> {not_a_set}, type={type(not_a_set).__name__}")  # dict!

    _s("O(1) membership vs list O(n)")
    big_set = set(range(1000))
    big_list = list(range(1000))
    print(f"999 in set  = {999 in big_set}")    # O(1)
    print(f"999 in list = {999 in big_list}")   # O(n)
    print("(set is dramatically faster for large collections)")

    _s("add() / remove() / discard()")
    s = {1, 2}
    s.add(3)
    print(f"add(3)       -> {s}")
    s.add(2)              # already present — no-op
    print(f"add(2) again -> {s}")
    s.discard(99)         # absent — no error
    print(f"discard(99)  -> {s}")
    s.remove(1)           # present — removed
    print(f"remove(1)    -> {s}")

    _s("Set operations")
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print(f"a = {a}, b = {b}")
    print(f"a | b  (union)        = {a | b}")        # {1,2,3,4,5,6}
    print(f"a & b  (intersection) = {a & b}")        # {3,4}
    print(f"a - b  (difference)   = {a - b}")        # {1,2}
    print(f"a ^ b  (symmetric)    = {a ^ b}")        # {1,2,5,6}

    _s("Practical: deduplicate a list")
    items = [1, 2, 2, 3, 3, 3, 4]
    unique = list(set(items))
    print(f"{items} -> set -> {sorted(unique)}")  # [1,2,3,4]

    _s("Set comprehension")
    nums = [1, 2, 2, 3, 4, 4, 5]
    unique_squares = {x ** 2 for x in nums}
    print(f"squares of {nums} -> {sorted(unique_squares)}")  # {1,4,9,16,25}

    _s("Demo complete")
