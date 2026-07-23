"""Functions

Reusable blocks of code — the most basic form of abstraction in Python.
Covers ``def``, parameters, defaults, keyword arguments, ``*args``/``**kwargs``,
scope, and lambda expressions.
"""

"""
Function (def):
    A named, reusable block of code that takes inputs (parameters), does work,
    and optionally returns a value. Defined with ``def name(params):`` and
    called with ``name(args)``. A function without an explicit ``return``
    returns ``None``.
"""

"""
Parameters vs Arguments:
    *Parameters* are the variables listed in the ``def`` line. *Arguments* are
    the actual values passed when calling. The terms are often used loosely but
    the distinction matters: the parameter is the slot; the argument is what
    fills it.
"""

"""
Default Arguments:
    A parameter can have a default value: ``def greet(name="World")``. If the
    caller omits that argument, the default is used. Defaults are evaluated
    ONCE at definition time, not per call — so mutable defaults (``def f(items=[])``)
    are a classic bug: the same list is shared across all calls. Use ``None``
    as a sentinel and create the mutable inside the function.
"""

"""
Keyword Arguments:
    When calling, you can name the parameter: ``greet(name="Alice")``. This
    makes the call self-documenting and allows arguments in any order. Required
    parameters can also be passed by keyword.
"""

"""
*args / **kwargs:
    ``*args`` collects extra positional arguments into a tuple. ``**kwargs``
    collects extra keyword arguments into a dict. Together they let a function
    accept any number of arguments. Often used in wrapper/decorator patterns
    and when forwarding arguments to another function.
"""

"""
Scope (LEGB):
    Python looks up names in this order: **L**ocal (inside the function) ->
    **E**nclosing (outer function, for nested defs) -> **G**lobal (module
    level) -> **B**uilt-in (``len``, ``print``, …). Assignment (``x = ...``)
    always creates a *local* variable unless declared ``global`` or ``nonlocal``.
    Reading a name searches outward through the layers.
"""

"""
Lambda:
    A small anonymous function: ``lambda params: expr``. Limited to a single
    expression (no statements, no multi-line body). Commonly used as a ``key``
    argument to ``sorted()``/``.sort()`` or in ``map()``/``filter()`` — though a
    list comprehension is often clearer than ``map``/``filter`` + lambda.
"""


if __name__ == "__main__":
    def _s(t): print(f"\n{'=' * 40}\n {t}\n{'=' * 40}")

    _s("Basic function")
    def add(a, b):
        return a + b

    print(f"add(2, 3) = {add(2, 3)}")

    def no_return():
        pass

    print(f"no explicit return -> {no_return()}")  # None

    _s("Default arguments")
    def greet(name="World"):
        return f"Hello, {name}!"

    print(greet())            # Hello, World!
    print(greet("Alice"))     # Hello, Alice!

    _s("Mutable default gotcha")
    def bad(items=[]):        # shared list across calls!
        items.append(1)
        return items

    print(f"bad() call 1 = {bad()}")  # [1]
    print(f"bad() call 2 = {bad()}")  # [1, 1] — same list!

    def good(items=None):     # correct pattern
        if items is None:
            items = []
        items.append(1)
        return items

    print(f"good() call 1 = {good()}")  # [1]
    print(f"good() call 2 = {good()}")  # [1] — fresh list each time

    _s("Keyword arguments")
    def describe(name, age, role):
        return f"{name} is {age}, role={role}"

    print(describe("Alice", 30, "admin"))
    print(describe(role="dev", name="Bob", age=25))  # any order

    _s("*args / **kwargs")
    def show_all(*args, **kwargs):
        print(f"  args   = {args}")     # tuple
        print(f"  kwargs = {kwargs}")   # dict

    show_all(1, 2, 3, name="Alice", active=True)

    _s("Scope (LEGB)")
    message = "global"

    def outer():
        message = "enclosing"

        def inner():
            message = "local"
            print(f"  inner sees: {message}")

        inner()
        print(f"  outer sees: {message}")

    outer()
    print(f"  global sees: {message}")

    _s("Lambda")
    nums = [3, 1, 4, 1, 5]
    print(f"sorted by default   = {sorted(nums)}")
    print(f"sorted reversed     = {sorted(nums, key=lambda x: -x)}")
    words = ["banana", "pie", "a"]
    print(f"sorted by length    = {sorted(words, key=lambda w: len(w))}")
    print(f"sorted by last char = {sorted(words, key=lambda w: w[-1])}")

    _s("Demo complete")
