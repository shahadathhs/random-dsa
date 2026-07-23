"""Error Handling

Python's exception system — how to catch, raise, and understand errors.
Covers ``try``/``except``/``finally``, raising exceptions, and the common
built-in types you will encounter throughout this repo.
"""

"""
Exception:
    An error that disrupts normal program flow. When something goes wrong (a
    key is missing, an index is out of range, a type is wrong), Python *raises*
    an exception. If nobody catches it, the program crashes with a traceback.
    Catching it lets you handle the error gracefully instead.
"""

"""
try / except / finally:
    ``try`` wraps code that might fail. ``except`` catches a specific exception
    type (or all exceptions) and runs recovery code. ``finally`` always runs —
    whether the try succeeded, raised, or was caught — making it the place for
    cleanup (closing files, releasing locks). You can have multiple ``except``
    clauses for different exception types; the first match wins.
"""

"""
Catching by Type:
    ``except KeyError:`` catches only ``KeyError``. ``except (KeyError,
    IndexError):`` catches either. A bare ``except:`` (no type) catches
    *everything* including ``KeyboardInterrupt`` and ``SystemExit`` — almost
    always a mistake; catch ``Exception`` instead if you want all "normal"
    errors.
"""

"""
The Exception Object:
    ``except KeyError as err:`` binds the exception object to ``err``. It
    carries the error message (``str(err)``) and the traceback. Printing or
    logging it gives context for debugging without crashing the program.
"""

"""
raise:
    You can raise your own exceptions: ``raise ValueError("negative age")``.
    This is how functions signal invalid input to their callers. You can also
    re-raise the current exception inside an ``except`` block with a bare
    ``raise`` (preserves the original traceback).
"""

"""
Common Built-in Exceptions:
    These appear throughout this repo:
        KeyError        — dict/set lookup on a missing key
        IndexError      — list/string index out of range
        TypeError       — wrong type (e.g. ``"a" + 1``)
        ValueError      — right type, wrong value (e.g. ``int("abc")``)
        AttributeError  — method/attribute doesn't exist on the object
"""

"""
Exception Hierarchy:
    All exceptions derive from ``BaseException``. The practical root for
    catchable errors is ``Exception`` — ``KeyError``, ``ValueError``,
    ``TypeError`` etc. are all subclasses of it. ``KeyboardInterrupt`` and
    ``SystemExit`` derive from ``BaseException`` directly, which is why a bare
    ``except Exception:`` does NOT swallow Ctrl-C.
"""


if __name__ == "__main__":
    def _s(t): print(f"\n{'=' * 40}\n {t}\n{'=' * 40}")

    _s("try / except")
    d = {"a": 1}
    try:
        value = d["missing"]
    except KeyError as err:
        print(f"caught KeyError: {err}")

    _s("finally — always runs")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("  caught ZeroDivisionError")
    finally:
        print("  finally runs regardless")

    _s("Multiple except clauses")
    def safe_get(lst, index, default=None):
        try:
            return lst[index]
        except IndexError:
            return default
        except TypeError:
            return "not a list!"

    print(f"safe_get([1,2,3], 1)   = {safe_get([1,2,3], 1)}")    # 2
    print(f"safe_get([1,2,3], 99)  = {safe_get([1,2,3], 99)}")   # None

    _s("raise — signal invalid input")
    def set_age(age):
        if not isinstance(age, int):
            raise TypeError(f"age must be int, got {type(age).__name__}")
        if age < 0:
            raise ValueError(f"age must be non-negative, got {age}")
        return age

    print(f"set_age(30)  = {set_age(30)}")
    try:
        set_age(-5)
    except ValueError as err:
        print(f"set_age(-5) -> ValueError: {err}")

    _s("Common exceptions you will see")
    # KeyError — missing dict key
    try:
        {}["x"]
    except KeyError as e:
        print(f"KeyError:       {e}")

    # IndexError — out of range
    try:
        [1, 2][5]
    except IndexError as e:
        print(f"IndexError:     {e}")

    # TypeError — wrong type
    try:
        "a" + 1
    except TypeError as e:
        print(f"TypeError:      {e}")

    # ValueError — right type, wrong value
    try:
        int("hello")
    except ValueError as e:
        print(f"ValueError:     {e}")

    # AttributeError — no such method
    try:
        (1, 2).append(3)
    except AttributeError as e:
        print(f"AttributeError: {e}")

    _s("Exception hierarchy")
    print(f"issubclass(KeyError, Exception)   = {issubclass(KeyError, Exception)}")
    print(f"issubclass(ValueError, Exception) = {issubclass(ValueError, Exception)}")
    print(f"issubclass(KeyError, LookupError) = {issubclass(KeyError, LookupError)}")

    _s("Demo complete")
