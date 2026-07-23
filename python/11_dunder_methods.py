"""Dunder Methods (Special Methods)

Python's data model — the "magic methods" that let custom objects participate
in built-in operations like ``len()``, indexing, ``in``, iteration, and
``str()``. These are the methods that make ``DynamicArray`` and ``HashMap``
feel like native Python collections.
"""

"""
Dunder Method (Special Method):
    A method with double leading and trailing underscores — ``__init__``,
    ``__len__``, ``__getitem__``, etc. You rarely call them directly; Python
    calls them implicitly when you use the corresponding built-in operation.
    For example, ``len(obj)`` calls ``obj.__len__()``, ``obj[key]`` calls
    ``obj.__getitem__(key)``, and ``x in obj`` calls ``obj.__contains__(x)``.
    Implementing dunders is how you make a custom class "feel native."
"""

"""
__init__ (Constructor):
    Called when an object is created — ``MyClass()`` triggers
    ``__init__(self, ...)``. Sets up the initial state (attributes). Not a true
    constructor (the object already exists when it runs); it is an *initializer*.
"""

"""
__len__:
    Enables ``len(obj)``. Should return a non-negative integer. Also makes the
    object truthy/falsy in a boolean context — ``if obj:`` calls ``__len__``
    and treats 0 as falsy.
"""

"""
__getitem__ / __setitem__ (Indexing):
    ``__getitem__(self, key)`` enables ``obj[key]`` (read).
    ``__setitem__(self, key, value)`` enables ``obj[key] = value`` (write).
    The "key" can be an integer index, a string, or any hashable object — the
    implementation decides what keys are valid.
"""

"""
__delitem__:
    Enables ``del obj[key]``. Should remove the element at ``key`` and raise
    ``KeyError`` if it does not exist.
"""

"""
__contains__:
    Enables ``x in obj``. Should return ``True``/``False``. If not defined,
    Python falls back to iterating and checking equality — which is O(n).
    Defining it lets you provide an O(1) lookup instead.
"""

"""
__str__ / __repr__:
    ``__str__`` is the "nice" display for humans — ``str(obj)`` and ``print(obj)``.
    ``__repr__`` is the "unambiguous" display for developers — shown in
    tracebacks and the REPL when ``__str__`` is absent. Rule of thumb: ``__str__``
    reads well, ``__repr__`` should ideally let you reconstruct the object.
"""

"""
__iter__ / __next__:
    ``__iter__`` enables ``for x in obj:`` — should return an iterator object.
    The iterator's ``__next__`` returns the next element or raises
    ``StopIteration`` when exhausted. If ``__iter__`` is absent but
    ``__getitem__`` exists, Python falls back to integer indexing (0, 1, 2, …).
"""


if __name__ == "__main__":
    def _s(t): print(f"\n{'=' * 40}\n {t}\n{'=' * 40}")

    class SimpleStack:
        """A minimal stack to demonstrate dunder methods."""

        def __init__(self):
            self._items = []

        def push(self, value):
            self._items.append(value)

        # --- dunder methods ---

        def __len__(self):
            return len(self._items)

        def __getitem__(self, index):
            return self._items[index]

        def __setitem__(self, index, value):
            self._items[index] = value

        def __delitem__(self, index):
            del self._items[index]

        def __contains__(self, value):
            return value in self._items

        def __iter__(self):
            return iter(self._items)

        def __str__(self):
            return f"Stack{self._items}"

        def __repr__(self):
            return f"SimpleStack({self._items!r})"

    _s("__init__ — constructor")
    s = SimpleStack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"after push 1,2,3: {s}")

    _s("__len__ — len()")
    print(f"len(s) = {len(s)}")

    _s("__getitem__ — s[index]")
    print(f"s[0]  = {s[0]}")
    print(f"s[-1] = {s[-1]}")

    _s("__setitem__ — s[index] = value")
    s[0] = 99
    print(f"s[0] = 99 -> {s}")

    _s("__contains__ — x in s")
    print(f"99 in s  = {99 in s}")
    print(f"42 in s  = {42 in s}")

    _s("__delitem__ — del s[index]")
    del s[0]
    print(f"del s[0] -> {s}")

    _s("__iter__ — for x in s")
    for item in s:
        print(f"  {item}")

    _s("__str__ vs __repr__")
    print(f"str(s)  = {str(s)}")
    print(f"repr(s) = {repr(s)}")

    _s("Truthiness via __len__")
    s2 = SimpleStack()
    print(f"empty stack is falsy: {bool(s2)}")  # False (len == 0)
    print(f"if s2: -> {'entered' if s2 else 'skipped'}")
    s2.push(0)
    print(f"after push: if s2: -> {'entered' if s2 else 'skipped'}")

    _s("Demo complete")
