"""Strings

Python's text type — creation, indexing, slicing, common methods, formatting,
and the immutability that underlies it all.
"""

"""
String (str):
    An immutable sequence of Unicode characters. Created with single quotes
    (``'hi'``), double quotes (``"hi"``), or triple quotes (``\"\"\"multi
    line\"\"\"``). The quote style is purely stylistic — they produce the same
    ``str`` type.
"""

"""
Indexing:
    Access a single character by position — ``s[0]`` is the first, ``s[-1]`` is
    the last. Negative indices count backward from the end, so ``s[-1]`` is
    shorthand for ``s[len(s) - 1]``.
"""

"""
Slicing:
    Extract a substring with ``s[start:stop:step]``. ``stop`` is exclusive.
    Omitting a bound defaults to the start/end of the string. ``s[::-1]``
    reverses the string (step ``-1`` walks backward).
"""

"""
Immutability:
    Strings cannot be changed after creation — ``s[0] = 'X'`` raises
    ``TypeError``. Every method that "modifies" a string (``.upper()``,
    ``.strip()``, etc.) returns a *new* string; the original is untouched. This
    is why ``s = s.upper()`` rebinds the name rather than mutating in place.
"""

"""
f-strings:
    Embed expressions inside string literals with ``f"..."`` —
    ``f"Hello, {name}!"``. The expression inside ``{}`` is evaluated and
    inserted. Added in Python 3.6; the older alternatives are ``%`` formatting
    and ``str.format()``, both still valid but less readable.
"""


if __name__ == "__main__":
    def _s(t): print(f"\n{'=' * 40}\n {t}\n{'=' * 40}")

    _s("Quotes")
    a = 'single'
    b = "double"
    c = """triple
line"""
    print(f"'{a}' == \"{b}\" -> {a == 'single'}")  # True (same type)
    print(f"triple-line length: {len(c)}")

    _s("Indexing")
    s = "Python"
    print(f"s[0]  = '{s[0]}'")    # P
    print(f"s[-1] = '{s[-1]}'")   # n
    print(f"s[-2] = '{s[-2]}'")   # o

    _s("Slicing")
    print(f"s[0:3]   = '{s[0:3]}'")    # Pyt  (stop is exclusive)
    print(f"s[:3]    = '{s[:3]}'")     # Pyt
    print(f"s[3:]    = '{s[3:]}'")     # hon
    print(f"s[::-1]  = '{s[::-1]}'")   # nohtyP  (reversed)

    _s("Common methods")
    t = "  Hello World  "
    print(f"'{t}'.strip()        = '{t.strip()}'")
    print(f"'{t}'.upper()        = '{t.upper().strip()}'")
    print(f"'{t}'.lower()        = '{t.lower().strip()}'")
    print(f"'a,b,c'.split(',')   = {'a,b,c'.split(',')}")
    print(f"'-'.join(['x','y'])  = {'-'.join(['x', 'y'])}")

    _s("f-strings vs .format()")
    name = "Alice"
    age = 30
    print(f"f-string:  f'My name is {name}, age {age}'")
    print(".format(): {}".format("My name is {}, age {}".format(name, age)))

    _s("ord() and chr()")
    print(f"ord('A') = {ord('A')}")   # 65  (ASCII value)
    print(f"chr(97)  = '{chr(97)}'")  # a

    _s("Immutability")
    s = "hello"
    print(f"s.upper() returns new string: '{s.upper()}'")
    print(f"original s is unchanged:      '{s}'")
    try:
        s[0] = 'H'
    except TypeError as err:
        print(f"s[0] = 'H' -> TypeError: {err}")

    _s("Demo complete")
