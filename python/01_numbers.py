"""Numbers

Python's numeric types and arithmetic operators. Covers integers, floats,
the division family, conversions, and the common built-in math functions.
"""

"""
Integer (int):
    Whole numbers with no fractional part — ``42``, ``-7``, ``0``. Python's
    ``int`` has arbitrary precision: it grows as large as memory allows, unlike
    C/Java where overflow wraps at a fixed width.
"""

"""
Float (float):
    Double-precision (64-bit) floating-point numbers — ``3.14``, ``-0.5``,
    ``2.0``. Floating-point cannot represent every real number exactly, so
    ``0.1 + 0.2 == 0.3`` is ``False`` — a universal IEEE 754 quirk, not a bug.
"""

"""
Division Family:
    Python has *three* division operators, each for a different intent:
        /   true division  — always returns float (``7 / 2 == 3.5``)
        //  floor division — truncates toward negative infinity (``7 // 2 == 3``)
        %   modulo         — remainder after floor division (``7 % 2 == 1``)
    The ``//`` and ``%`` pair satisfies:  ``x == (x // y) * y + (x % y)``
"""

"""
Exponent:
    ``**`` raises to a power — ``2 ** 10 == 1024``. Both base and exponent may
    be floats: ``9 ** 0.5 == 3.0`` (square root via ½ power).
"""

"""
Conversion:
    ``int()`` and ``float()`` convert between types or parse strings.
    ``int(3.9)`` truncates toward zero (gives ``3``, not ``4``). ``int("42")``
    parses a string. ``float("3.14")`` does the same for floats.
"""


if __name__ == "__main__":
    def _s(t): print(f"\n{'=' * 40}\n {t}\n{'=' * 40}")

    _s("Arithmetic operators")
    print(f"7  + 2  = {7 + 2}")    # 9
    print(f"7  - 2  = {7 - 2}")    # 5
    print(f"7  * 2  = {7 * 2}")    # 14
    print(f"7  ** 2 = {7 ** 2}")   # 49

    _s("Division family")
    print(f"7  /  2 = {7 / 2}")    # 3.5  (float)
    print(f"7  // 2 = {7 // 2}")   # 3    (int)
    print(f"7  %  2 = {7 % 2}")    # 1    (remainder)
    print(f"-7 // 2 = {-7 // 2}")  # -4   (floors toward -inf, not toward zero)

    _s("Exponent")
    print(f"2 ** 10  = {2 ** 10}")   # 1024
    print(f"9 ** 0.5 = {9 ** 0.5}")  # 3.0  (square root)

    _s("Conversion")
    print(f"int(3.9)    = {int(3.9)}")       # 3  (truncates, not rounds)
    print(f"int('42')   = {int('42')}")      # 42
    print(f"float(5)    = {float(5)}")       # 5.0
    print(f"float('3.14') = {float('3.14')}")  # 3.14

    _s("Built-in math functions")
    print(f"abs(-7)   = {abs(-7)}")    # 7
    print(f"min(3,1,2)= {min(3, 1, 2)}")  # 1
    print(f"max(3,1,2)= {max(3, 1, 2)}")  # 3
    print(f"round(3.14159, 2) = {round(3.14159, 2)}")  # 3.14
    print(f"pow(2, 10) = {pow(2, 10)}")  # 1024  (same as 2 ** 10)

    _s("Float precision gotcha")
    print(f"0.1 + 0.2 == 0.3  -> {0.1 + 0.2 == 0.3}")  # False!
    print(f"0.1 + 0.2         -> {0.1 + 0.2}")          # 0.30000000000000004

    _s("Demo complete")
