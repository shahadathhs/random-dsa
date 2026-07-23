"""Tuples

Python's immutable, ordered sequence — the fixed-length cousin of lists.
Covers creation, unpacking, immutability, and when to choose a tuple over a
list.
"""

"""
Tuple:
    An ordered, *immutable* sequence. Created with parentheses ``(1, 2, 3)``
    or just commas ``1, 2, 3``. Once created, its length and contents cannot
    change — no ``append``, no ``insert``, no item assignment. This immutability
    is exactly why tuples are used for fixed groupings like ``(key, value)``
    pairs in a hash map.
"""

"""
Single-Element Tuple:
    ``(5)`` is just the integer ``5`` in parentheses — the comma is what makes
    a tuple. A one-element tuple must be written ``(5,)`` with a trailing comma.
    An easy source of bugs when returning a single value that should stay
    wrapped.
"""

"""
Unpacking:
    Assigning a tuple's elements to separate variables in one statement —
    ``a, b = (1, 2)`` or ``a, b = 1, 2``. Works with any iterable, not just
    tuples. The ``*`` operator collects the rest: ``first, *rest = [1, 2, 3, 4]``
    gives ``first=1, rest=[2, 3, 4]``. Swap two values without a temp: ``a, b = b, a``.
"""

"""
Immutability is Shallow:
    The tuple itself cannot grow or shrink, but if it contains a mutable object
    (like a list), that object can still be changed: ``t = ([1],); t[0].append(2)``
    works. The tuple's *structure* is frozen; the *contents* of its elements
    are not.
"""

"""
Tuple vs List:
    Use a tuple when the grouping is conceptually fixed — coordinates, RGB
    values, ``(key, value)`` pairs, function return values. Use a list when the
    collection will grow, shrink, or be sorted. Tuples are slightly faster and
    use less memory; they are also hashable (if all their elements are), so
    they can be used as dict keys and set members — lists cannot.
"""


if __name__ == "__main__":
    def _s(t): print(f"\n{'=' * 40}\n {t}\n{'=' * 40}")

    _s("Creation")
    a = (1, 2, 3)
    b = 1, 2, 3          # parentheses optional
    c = tuple([4, 5, 6]) # from an iterable
    empty = ()
    print(f"(1,2,3)     = {a}")
    print(f"1,2,3       = {b}")
    print(f"tuple([4,5,6])= {c}")
    print(f"empty tuple = {empty}")

    _s("Indexing & slicing (same as lists)")
    t = (10, 20, 30, 40)
    print(f"t[0]   = {t[0]}")
    print(f"t[-1]  = {t[-1]}")
    print(f"t[1:3] = {t[1:3]}")

    _s("Single-element tuple gotcha")
    not_a_tuple = (5)
    real_tuple = (5,)
    print(f"(5)    -> {not_a_tuple}, type={type(not_a_tuple).__name__}")
    print(f"(5,)   -> {real_tuple}, type={type(real_tuple).__name__}")

    _s("Unpacking")
    x, y, z = (1, 2, 3)
    print(f"x,y,z = (1,2,3) -> x={x}, y={y}, z={z}")
    first, *rest = (1, 2, 3, 4)
    print(f"first, *rest   -> first={first}, rest={rest}")
    a_val, b_val = 10, 20
    a_val, b_val = b_val, a_val  # swap without temp
    print(f"swapped         -> a={a_val}, b={b_val}")

    _s("Immutability")
    t = (1, 2, 3)
    try:
        t[0] = 99
    except TypeError as err:
        print(f"t[0] = 99 -> TypeError: {err}")
    try:
        t.append(4)
    except AttributeError as err:
        print(f"t.append(4)-> AttributeError: {err}")

    _s("Immutability is shallow")
    t = ([1, 2],)
    t[0].append(3)          # works! inner list is mutable
    print(f"t = ([1,2],); t[0].append(3) -> {t}")

    _s("Tuple is hashable (list is not)")
    t = (1, 2)
    print(f"hash((1, 2)) = {hash(t)}")
    d = {t: "value"}       # tuple as dict key — works
    print(f"dict key (1,2) -> {d[(1, 2)]}")
    try:
        hash([1, 2])
    except TypeError as err:
        print(f"hash([1,2]) -> TypeError: {err}")

    _s("Demo complete")
