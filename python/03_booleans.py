"""Booleans & Truthiness

True, False, and the concept of truthiness — which values Python treats as
"true" or "false" in a boolean context, plus the ``and`` / ``or`` / ``not``
operators and short-circuit evaluation.
"""

"""
bool:
    Python's boolean type has exactly two values: ``True`` and ``False``
    (capitalized). They are a subclass of ``int`` — ``True == 1`` and
    ``False == 0`` — which is why ``sum([True, False, True])`` returns ``2``.
"""

"""
Truthiness:
    Every object in Python can be tested in a boolean context (``if x:``).
    ``bool(x)`` returns ``False`` for a fixed set of "empty" or "zero" values:
    ``False``, ``None``, ``0``, ``0.0``, ``""``, ``[]``, ``{}``, ``set()``,
    ``tuple()``. Everything else is truthy. This lets you write ``if items:``
    instead of ``if len(items) > 0:``.
"""

"""
and / or / not:
    ``and`` returns the first falsy operand (or the last if all are truthy).
    ``or`` returns the first truthy operand (or the last if all are falsy).
    ``not`` always returns a real ``bool`` (``True`` or ``False``). Note that
    ``and``/``or`` do NOT necessarily return ``True``/``False`` — they return
    the operand itself, which is truthy or falsy as needed.
"""

"""
Short-Circuit Evaluation:
    ``and`` and ``or`` evaluate left to right and stop as soon as the answer is
    determined. ``a and b`` skips ``b`` if ``a`` is falsy (result is already
    known). ``a or b`` skips ``b`` if ``a`` is truthy. This is commonly used
    for safe defaults: ``name = user_input or "anonymous"``.
"""


if __name__ == "__main__":
    def _s(t): print(f"\n{'=' * 40}\n {t}\n{'=' * 40}")

    _s("bool() — explicit conversion")
    print(f"bool(1)       = {bool(1)}")       # True
    print(f"bool(0)       = {bool(0)}")       # False
    print(f"bool('')      = {bool('')}")      # False
    print(f"bool('hi')    = {bool('hi')}")    # True
    print(f"bool([])      = {bool([])}")      # False
    print(f"bool([0])     = {bool([0])}")     # True  (non-empty list)
    print(f"bool(None)    = {bool(None)}")    # False

    _s("Truthiness in conditionals")
    items = []
    if items:
        print("items is truthy")
    else:
        print("empty list is falsy -> skipped")

    items = [0]
    if items:
        print("[0] is truthy -> entered (contains an element)")

    _s("and / or return the operand, not True/False")
    print(f"'' and 'b'    = {repr('' and 'b')}")      # '' (first falsy)
    print(f"'a' and 'b'   = {repr('a' and 'b')}")     # 'b' (all truthy -> last)
    print(f"0 or 'default'= {repr(0 or 'default')}")  # 'default' (first falsy)
    print(f"'x' or 'y'    = {repr('x' or 'y')}")      # 'x' (first truthy)

    _s("not — always returns a real bool")
    print(f"not 0   = {not 0}")    # True
    print(f"not 'x' = {not 'x'}")  # False

    _s("Short-circuit — right side never evaluated")
    def side_effect():
        print("  (side effect fired!)")
        return True

    print("False and ...:")
    False and side_effect()        # side_effect NOT called
    print("True or ...:")
    True or side_effect()          # side_effect NOT called

    _s("Practical: safe defaults")
    user_input = ""
    name = user_input or "anonymous"
    print(f'empty input -> name = "{name}"')  # anonymous

    _s("bool is a subclass of int")
    print(f"True + True  = {True + True}")    # 2
    print(f"sum([True, False, True]) = {sum([True, False, True])}")  # 2

    _s("Demo complete")
