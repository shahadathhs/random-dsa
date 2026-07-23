"""Lists

Python's mutable, ordered sequence — the workhorse collection. Covers creation,
indexing, slicing, methods, sorting, mutability/aliasing, and list
comprehensions.
"""

"""
List:
    An ordered, mutable sequence of arbitrary objects. Created with square
    brackets ``[1, 2, 3]`` or ``list()``. Elements need not be the same type.
    Under the hood a Python list is a dynamic array of object references (see
    ``data_structures/dynamic_array.py`` for the from-scratch version).
"""

"""
Indexing & Slicing:
    Same rules as strings: ``lst[0]`` is first, ``lst[-1]`` is last.
    ``lst[start:stop:step]`` extracts a sub-list (stop is exclusive).
    Slicing always returns a *new* list — the original is untouched.
"""

"""
Mutability & Aliasing:
    Lists are mutable — ``lst[0] = 'new'`` changes the list in place. But
    assignment (``b = a``) creates an alias (two names, same list), not a copy.
    ``b.append(x)`` also affects ``a``. To get an independent copy use
    ``a.copy()``, ``a[:]``, or ``list(a)``. Nested lists need ``copy.deepcopy()``
    since a shallow copy still shares the inner lists.
"""

"""
in operator:
    ``x in lst`` scans the list for ``x`` and returns ``True``/``False``. It is
    O(n) — a linear scan — unlike ``in`` on a set or dict key which is O(1).
"""

"""
sort() vs sorted():
    ``lst.sort()`` sorts in place and returns ``None``. ``sorted(lst)`` returns
    a new sorted list and leaves the original unchanged. Both accept
    ``reverse=True`` and ``key=`` (a function that extracts the comparison
    value, e.g. ``key=len``).
"""

"""
List Comprehension:
    A compact syntax to build a list by transforming and/or filtering another
    iterable: ``[expr for item in iterable if condition]``. Equivalent to a for
    loop with ``.append()`` but more readable for simple transforms. Supports
    nested loops and multiple ``if`` clauses, but readability degrades fast —
    fall back to a regular loop when it gets complex.
"""


if __name__ == "__main__":
    def _s(t): print(f"\n{'=' * 40}\n {t}\n{'=' * 40}")

    _s("Creation")
    a = [1, 2, 3]
    b = list("hello")
    c = [0] * 4
    print(f"[1,2,3]          = {a}")
    print(f"list('hello')    = {b}")
    print(f"[0] * 4          = {c}")

    _s("Indexing & slicing")
    lst = [10, 20, 30, 40, 50]
    print(f"lst[0]    = {lst[0]}")
    print(f"lst[-1]   = {lst[-1]}")
    print(f"lst[1:4]  = {lst[1:4]}")
    print(f"lst[::-1] = {lst[::-1]}")

    _s("Methods (mutate in place)")
    lst = [1, 2, 3]
    lst.append(4)
    print(f"append(4)  -> {lst}")
    lst.insert(0, 0)
    print(f"insert(0,0)-> {lst}")
    lst.pop()
    print(f"pop()      -> {lst}")
    lst.remove(2)
    print(f"remove(2)  -> {lst}")
    del lst[0]
    print(f"del lst[0] -> {lst}")

    _s("in / index / count")
    lst = [1, 2, 3, 2]
    print(f"2 in [1,2,3,2]   = {2 in lst}")
    print(f"lst.index(2)     = {lst.index(2)}")  # first match
    print(f"lst.count(2)     = {lst.count(2)}")

    _s("sort() vs sorted()")
    original = [3, 1, 4, 1, 5]
    print(f"sorted(original)  = {sorted(original)}")  # new list
    print(f"original unchanged= {original}")
    original.sort()
    print(f"original.sort()   = {original}")          # in place
    print(f"sorted(...,reverse=True) = {sorted(original, reverse=True)}")
    print(f"sorted('banana')  = {sorted('banana', key=lambda c: c)}")
    words = ["banana", "apple", "cherry"]
    print(f"sorted by length  = {sorted(words, key=len)}")

    _s("Aliasing vs copy")
    a = [1, 2, 3]
    b = a           # alias — same list
    b.append(4)
    print(f"after b=a; b.append(4) -> a={a}")  # a is [1,2,3,4]
    c = a.copy()    # independent copy
    c.append(99)
    print(f"after c=a.copy(); c.append(99) -> a={a}, c={c}")

    _s("List comprehensions")
    nums = range(6)
    squares = [x ** 2 for x in nums]
    print(f"squares          = {squares}")
    evens = [x for x in nums if x % 2 == 0]
    print(f"evens            = {evens}")
    pairs = [(x, y) for x in range(2) for y in range(2)]
    print(f"nested pairs     = {pairs}")

    _s("Demo complete")
