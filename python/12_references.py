"""Mutable Objects & References

How Python's variable model works — references, aliasing, shallow vs deep copy,
and why "mutable" is the source of many subtle bugs. Essential for understanding
why our ``DynamicArray`` stores ``None`` sentinels and why ``HashSet`` wraps a
``HashMap`` instead of copying its internals.
"""

"""
Variables Are Names, Not Boxes:
    In Python, a variable is a *name* that points to an object, not a box that
    holds a value. ``a = [1, 2, 3]`` creates a list object in memory and binds
    the name ``a`` to it. ``b = a`` binds a *second name* to the *same* object
    — there is one list, two names. This is called aliasing.
"""

"""
id() and is:
    ``id(obj)`` returns the object's memory address (a unique integer).
    ``a is b`` returns ``True`` if ``a`` and ``b`` are the *same object*
    (same ``id``). ``a == b`` checks *value equality* — they may be different
    objects with the same contents. ``is`` is identity; ``==`` is equality.
"""

"""
Aliasing:
    When two names point to the same mutable object, changes through one name
    are visible through the other. ``a = [1]; b = a; b.append(2)`` — now ``a``
    is also ``[1, 2]``. This is the #1 source of bugs for beginners. It does
    NOT happen with immutable types (int, str, tuple) because you cannot change
    them in place — you can only rebind the name.
"""

"""
Shallow Copy:
    ``list.copy()``, ``list[:]``, and ``copy.copy()`` create a new outer object
    but share the inner elements. ``a = [[1], [2]]; b = a.copy(); b[0].append(99)``
    — both ``a`` and ``b`` see the change because the inner list is shared.
    Fine for flat lists of immutables; dangerous for nested structures.
"""

"""
Deep Copy:
    ``copy.deepcopy()`` recursively copies every level — the outer object AND
    every nested mutable object. ``a = [[1]]; b = copy.deepcopy(a); b[0].append(2)``
    — ``a`` is unaffected. Use this when you need a fully independent clone of
    a nested structure.
"""

"""
Mutable Default Argument:
    A classic trap: ``def f(items=[])``. The default list is created ONCE at
    function definition time and shared across all calls. ``f()`` appends to
    the same list every time. Fix: ``def f(items=None)`` and create inside.
"""

"""
Mutable vs Immutable:
    Immutable types (int, float, str, tuple, frozenset) cannot change after
    creation — any "modification" creates a new object. Mutable types (list,
    dict, set) can change in place. This matters for aliasing (only mutable
    objects have the aliasing problem), hashing (only immutables can be dict
    keys / set members), and function arguments (mutables can be modified by
    the callee; immutables effectively cannot).
"""


if __name__ == "__main__":
    import copy

    def _s(t): print(f"\n{'=' * 40}\n {t}\n{'=' * 40}")

    _s("Variables are names, not boxes")
    a = [1, 2, 3]
    b = a            # second name, same object
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"id(a) = {id(a)}")
    print(f"id(b) = {id(b)}")
    print(f"a is b = {a is b}")    # True — same object

    _s("Aliasing — change through one name, see through the other")
    b.append(4)
    print(f"b.append(4)")
    print(f"a = {a}")              # [1, 2, 3, 4] — a changed too!

    _s("is vs ==")
    x = [1, 2]
    y = [1, 2]       # same contents, different object
    print(f"x = {x}, y = {y}")
    print(f"x == y  = {x == y}")  # True  (same value)
    print(f"x is y  = {x is y}")  # False (different objects)

    _s("Immutable types — no aliasing problem")
    s1 = "hello"
    s2 = s1
    s2 = s2 + "!"     # creates a NEW string; s1 unchanged
    print(f's1 = "{s1}"')        # hello
    print(f's2 = "{s2}"')        # hello!

    _s("Shallow copy — new outer, shared inner")
    original = [[1, 2], [3, 4]]
    shallow = original.copy()
    print(f"original = {original}")
    print(f"shallow  = {shallow}")
    print(f"original is shallow = {original is shallow}")          # False
    print(f"original[0] is shallow[0] = {original[0] is shallow[0]}")  # True!
    shallow[0].append(99)
    print(f"shallow[0].append(99)")
    print(f"original = {original}")   # [[1,2,99],[3,4]] — inner shared!

    _s("Deep copy — fully independent")
    original2 = [[1, 2], [3, 4]]
    deep = copy.deepcopy(original2)
    deep[0].append(99)
    print(f"original2 = {original2}")   # [[1,2],[3,4]] — unaffected
    print(f"deep      = {deep}")        # [[1,2,99],[3,4]]

    _s("Mutable default argument trap")
    def bad(items=[]):
        items.append(1)
        return items

    print(f"bad() call 1 = {bad()}")   # [1]
    print(f"bad() call 2 = {bad()}")   # [1, 1] — same list!

    def good(items=None):
        if items is None:
            items = []
        items.append(1)
        return items

    print(f"good() call 1 = {good()}")  # [1]
    print(f"good() call 2 = {good()}")  # [1] — fresh each time

    _s("Why immutables can be dict keys, mutables cannot")
    d = {(1, 2): "tuple key works"}     # tuple is immutable
    print(f"d[(1,2)] = {d[(1, 2)]}")
    try:
        hash([1, 2])                    # list is mutable
    except TypeError as err:
        print(f"hash([1,2]) -> TypeError: {err}")

    _s("Demo complete")
