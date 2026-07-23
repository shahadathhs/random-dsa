"""Dictionaries

Python's mutable, unordered-by-semantics mapping of keys to values — the
built-in that ``data_structures/hash_map.py`` reimplements from scratch.
Covers access, common methods, deletion, iteration, and comprehensions.
"""

"""
Dictionary (dict):
    A mutable mapping from unique, hashable keys to arbitrary values. Created
    with curly braces ``{'a': 1, 'b': 2}`` or ``dict(a=1, b=2)``. Average O(1)
    for get/set/delete via hashing — see ``data_structures/hash_map.py`` for the
    from-scratch implementation with separate chaining.
"""

"""
Access:
    ``d[key]`` returns the value or raises ``KeyError`` if absent. ``d.get(key)``
    returns the value or ``None`` (or a provided default) if absent — never
    raises. Use ``d[key]`` when the key *must* exist; use ``.get()`` when
    absence is a normal case.
"""

"""
get() with default:
    ``d.get(key, default)`` returns ``default`` instead of ``None`` when the key
    is missing. Useful for frequency counting:
    ``d[k] = d.get(k, 0) + 1`` — increment or initialize in one line.
"""

"""
keys() / values() / items():
    ``.keys()`` and ``.values()`` return views of just the keys or just the
    values. ``.items()`` returns ``(key, value)`` pairs — the standard way to
    iterate over a dict. All three return *live views*: they reflect changes to
    the dict in real time, not a frozen snapshot.
"""

"""
in operator:
    ``key in d`` checks key membership in O(1) average — it tests *keys*, never
    values. This is the hash-map lookup that makes dicts fast.
"""

"""
del / pop():
    ``del d[key]`` removes a key-value pair (raises ``KeyError`` if absent).
    ``d.pop(key)`` removes *and returns* the value — useful when you need the
    value after removal. ``d.pop(key, default)`` avoids the exception.
"""

"""
Iteration Order:
    Since Python 3.7, dicts preserve *insertion order* — iterating yields keys
    in the order they were first added. This is an implementation detail that
    became official. It does NOT mean dicts are "sorted" — they follow
    insertion order, not key order.
"""

"""
Dict Comprehension:
    Build a dict by transforming an iterable: ``{key_expr: val_expr for item in iterable if condition}``.
    Useful for inverting a dict (``{v: k for k, v in d.items()}``), filtering,
    or building a lookup table from a list.
"""


if __name__ == "__main__":
    def _s(t): print(f"\n{'=' * 40}\n {t}\n{'=' * 40}")

    _s("Creation")
    d = {"apple": 1, "banana": 2, "cherry": 3}
    d2 = dict(x=10, y=20)
    empty = {}
    print(f"{{'a':1, 'b':2}} = {d}")
    print(f"dict(x=10, y=20) = {d2}")

    _s("Access")
    print(f"d['apple']   = {d['apple']}")   # 1
    try:
        d["missing"]
    except KeyError as err:
        print(f"d['missing'] -> KeyError: {err}")

    _s("get() — never raises")
    print(f"d.get('apple')   = {d.get('apple')}")      # 1
    print(f"d.get('missing') = {d.get('missing')}")     # None
    print(f"d.get('missing', 0) = {d.get('missing', 0)}")  # 0 (custom default)

    _s("get() for frequency counting")
    text = "a b a c b a"
    freq = {}
    for word in text.split():
        freq[word] = freq.get(word, 0) + 1
    print(f"word counts: {freq}")  # {'a': 3, 'b': 2, 'c': 1}

    _s("keys() / values() / items()")
    print(f"keys()   = {list(d.keys())}")
    print(f"values() = {list(d.values())}")
    print(f"items()  = {list(d.items())}")

    _s("in — tests keys, not values")
    print(f"'apple' in d   = {'apple' in d}")   # True
    print(f"1 in d         = {1 in d}")         # False (1 is a value, not key)

    _s("Modification")
    d["date"] = 4           # add
    d["apple"] = 99         # overwrite
    print(f"after add/overwrite: {d}")

    _s("del / pop()")
    del d["banana"]
    print(f"del d['banana'] -> {d}")
    val = d.pop("cherry")
    print(f"pop('cherry')   -> returned {val}, dict={d}")

    _s("Iteration (insertion order)")
    d = {"z": 1, "a": 2, "m": 3}
    for key, value in d.items():
        print(f"  {key}: {value}")
    print("(order matches insertion: z, a, m — NOT sorted)")

    _s("Dict comprehension")
    original = {"a": 1, "b": 2, "c": 3}
    inverted = {v: k for k, v in original.items()}
    print(f"inverted {original} -> {inverted}")  # {1:'a', 2:'b', 3:'c'}
    evens = {k: v for k, v in original.items() if v % 2 == 0}
    print(f"filtered (even values) -> {evens}")   # {'b': 2}

    _s("Demo complete")
