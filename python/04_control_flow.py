"""Control Flow

Conditionals, loops, and the loop-control statements that direct execution.
Covers ``if``/``elif``/``else``, ``for`` with ``range()`` and ``enumerate()``,
``while``, ``break``/``continue``/``pass``, and the rarely-seen ``else`` clause
on loops.
"""

"""
if / elif / else:
    Python's conditional chain. Exactly one branch runs — the first whose
    condition is truthy. ``elif`` and ``else`` are optional. Unlike C/Java
    there are no parentheses around the condition and no switch/case (use
    ``elif`` chains or dict dispatch instead).
"""

"""
for:
    Python's ``for`` is a "for-each" — it iterates over any iterable (list,
    string, dict, range, …), yielding one element at a time. There is no
    C-style ``for (int i = 0; i < n; i++)``; ``range()`` fills that role.
"""

"""
range():
    Generates a sequence of integers on demand without storing them all in
    memory. ``range(n)`` yields ``0..n-1``. ``range(a, b)`` yields ``a..b-1``.
    ``range(a, b, step)`` adds a stride. It is lazy — values are produced one
    at a time, so ``range(10**9)`` costs almost no memory.
"""

"""
enumerate():
    Yields ``(index, value)`` pairs as you iterate — the Pythonic replacement
    for the C-style ``for i in range(len(items))`` pattern. The starting index
    defaults to 0 but can be changed with ``enumerate(items, start=1)``.
"""

"""
break / continue / pass:
    ``break`` exits the loop immediately. ``continue`` skips to the next
    iteration. ``pass`` is a no-op placeholder used where a statement is
    syntactically required (e.g. an empty function body) but you want to do
    nothing yet.
"""

"""
else on loops:
    A loop's ``else`` clause runs ONLY if the loop completed normally (no
    ``break`` was hit). This is useful for search loops: break when found,
    else-handle the not-found case without a separate flag variable. It is
    one of Python's least-known features.
"""


if __name__ == "__main__":
    def _s(t): print(f"\n{'=' * 40}\n {t}\n{'=' * 40}")

    _s("if / elif / else")
    score = 75
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    else:
        grade = 'F'
    print(f"score {score} -> grade {grade}")

    _s("for over a list")
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(f"  {fruit}")

    _s("range()")
    print(f"range(5)      -> {list(range(5))}")        # [0, 1, 2, 3, 4]
    print(f"range(2, 6)   -> {list(range(2, 6))}")     # [2, 3, 4, 5]
    print(f"range(0,10,3) -> {list(range(0, 10, 3))}") # [0, 3, 6, 9]

    _s("enumerate()")
    for i, fruit in enumerate(fruits):
        print(f"  [{i}] {fruit}")
    print("  with start=1:")
    for i, fruit in enumerate(fruits, start=1):
        print(f"  {i}. {fruit}")

    _s("while")
    count = 3
    while count > 0:
        print(f"  countdown: {count}")
        count -= 1
    print("  liftoff!")

    _s("break")
    for i in range(10):
        if i == 3:
            print(f"  broke at i={i}")
            break
        print(f"  i={i}")

    _s("continue")
    for i in range(6):
        if i % 2 == 0:
            continue  # skip even numbers
        print(f"  odd: {i}")

    _s("pass — placeholder")
    x = 5
    if x > 10:
        pass  # TODO: handle large values later
    else:
        print(f"  x={x} is not > 10 (pass did nothing)")

    _s("else on loop — runs when no break")
    search = "banana"
    for fruit in fruits:
        if fruit == search:
            print(f"  found {search}!")
            break
    else:
        print(f"  {search} not found")

    # Now search for something absent
    search = "grape"
    for fruit in fruits:
        if fruit == search:
            print(f"  found {search}!")
            break
    else:
        print(f"  {search} not found (else clause fired)")

    _s("Demo complete")
