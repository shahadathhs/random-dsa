# Python & DSA Progress

## Part 0 — Python Basics

### Learning

Foundational Python before any DSA topic. Lives in `python/`.

#### Variables & Types

- [X] **Numbers** (`python/01_numbers.py`)
  - integers, floats, arithmetic operators
  - `//` floor division, `%` modulo, `**` exponent
  - `int()` / `float()` conversion
  - `abs()`, `min()`, `max()`, `round()`, `pow()`

- [X] **Strings** (`python/02_strings.py`)
  - single/double/triple quotes
  - indexing and slicing
  - concatenation and repetition
  - `len()`, `.upper()`, `.lower()`, `.strip()`, `.split()`, `.join()`
  - f-strings and `.format()`
  - `ord()`, `chr()`
  - immutability — why strings can't be modified in place

- [X] **Booleans & Truthiness** (`python/03_booleans.py`)
  - `True`, `False`, `bool()`
  - truthiness of empty collections, `0`, `None`, `""`
  - `and`, `or`, `not`
  - short-circuit evaluation

#### Control Flow

- [X] **Conditionals & Loops** (`python/04_control_flow.py`)
  - `if` / `elif` / `else`
  - `for` loops, `range()`, `enumerate()`
  - `while` loops
  - `break`, `continue`, `pass`
  - `else` on loops (runs when no `break`)

#### Collections

- [X] **Lists** (`python/05_lists.py`)
  - creation, indexing, slicing
  - `append()`, `insert()`, `pop()`, `remove()`, `del`
  - `in` operator, `.index()`, `.count()`
  - `.sort()`, `.reverse()`, `sorted()`
  - mutable — aliasing and copying (`copy()`, slicing)
  - list comprehensions

- [X] **Tuples** (`python/06_tuples.py`)
  - creation, indexing, unpacking
  - immutability — why `(key, value)` pairs are tuples
  - single-element tuples `(x,)`
  - tuple vs list — when to use which

- [X] **Dictionaries** (`python/07_dicts.py`)
  - creation, access, modification
  - `.get()`, `.keys()`, `.values()`, `.items()`
  - `in` operator
  - `del`, `.pop()`
  - iteration order (insertion order in Python 3.7+)
  - dict comprehensions

- [X] **Sets** (`python/08_sets.py`)
  - creation, `.add()`, `.remove()`, `.discard()`
  - `in` operator
  - union, intersection, difference
  - set comprehensions
  - why sets are O(1) membership

#### Functions

- [X] **Functions** (`python/09_functions.py`)
  - `def`, parameters, `return`
  - default arguments, keyword arguments
  - `*args`, `**kwargs`
  - scope (local, global, `nonlocal`)
  - lambda expressions

- [X] **Error Handling** (`python/10_errors.py`)
  - `try` / `except` / `finally`
  - raising exceptions (`raise ValueError(...)`)
  - common built-in exceptions (`KeyError`, `IndexError`, `TypeError`, `ValueError`)

---

## Part 1 — Arrays & Hash Maps

### Learning

#### Python Fundamentals

New concepts beyond Part 0, needed to build custom collections.

- [X] **dunder methods / data model** (`python/11_dunder_methods.py`)
  - `__init__`, `__len__`, `__str__`, `__repr__`
  - `__getitem__` / `__setitem__` / `__delitem__` (indexing)
  - `__contains__` (`in` operator)
  - `__iter__` (for loops)
  - how custom classes feel native via built-in operations

- [X] **mutable objects & references** (`python/12_references.py`)
  - variables are names, not boxes
  - aliasing — two names, same object
  - `is` vs `==` (identity vs equality)
  - shallow copy vs deep copy
  - mutable default argument trap
  - why immutables can be dict keys / set members

#### DSA Concepts

- [X] **Static Array**
  - indexing, fixed-size contiguous memory
  - O(1) random access
  - address formula: `base + index × element_size`

- [X] **Dynamic Array** (`data_structures/dynamic_array.py`)
  - capacity vs. size
  - resizing (doubling growth factor)
  - amortized O(1) append
  - insert/delete and shifting

- [X] **Pointers** (`algorithms/pointers.py`)
  - single pointer (linear scan)
  - two pointers — opposite ends (meet in the middle)
  - two pointers — same direction (fast & slow)
  - sliding window (fixed & variable size)
  - three pointers (Dutch national flag)

- [X] **Array Rotation** (`algorithms/rotation.py`)
  - normalize k (`k %= n`)
  - cyclic replacement (juggling), GCD cycle count
  - three-reverse algorithm
  - extra array baseline

- [X] **Hash Map & Hash Set** (`data_structures/hash_map.py`)
  - hash functions (polynomial rolling hash)
  - buckets, collisions, separate chaining
  - load factor, resize, rehash
  - dunder methods for native feel
  - composition — HashSet delegates to HashMap

### Practice

#### Phase 1 — Arrays & Hash Maps

Classics that every software engineer should know.

- [X] **Two Sum** (0001) — complements, one-pass hash map
- [X] **Contains Duplicate** (0217) — membership testing, hash map / hash set intuition
- [X] **Valid Anagram** (0242) — counting frequencies, intro to frequency maps
- [X] **Intersection of Two Arrays** (0349) — hash sets, membership lookups

#### Phase 2 — Two Pointers

- [X] **Valid Palindrome** (0125) — left/right pointers
- [X] **Merge Sorted Array** (0088) — in-place thinking, backwards three-pointer merge
- [X] **Squares of a Sorted Array** (0977) — two-pointer intuition, fill from back
- [X] **Remove Duplicates from Sorted Array** (0026) — slow/fast pointer variation

#### Phase 3 — In-Place Array Manipulation

- [X] **Remove Element** (0027) — shifting vs. overwriting, both-ends variant
- [X] **Move Zeroes** (0283) — in-place operations, swap vs. overwrite
- [X] **Rotate Array** (0189) — multiple approaches and trade-offs

---

## Part 2 — Stacks

### Learning

#### Python Fundamentals

New concepts beyond Part 0 and Part 1, needed for stack/queue work.

- [ ] **deque** (`python/13_deque.py`)
  - `collections.deque`, doubly-linked-list internals
  - O(1) `popleft` vs list's O(n)
  - `appendleft` / `popleft` for queue usage
  - `maxlen` — bounded deque (auto-evict)
  - list vs deque trade-offs

#### DSA Concepts

- [ ] **Stack** (`stack/stack.py`)
  - LIFO
  - push
  - pop
  - peek
  - is_empty
  - size
  - array implementation
  - complexity

- [ ] **Call Stack**
  - function frames
  - recursion
  - stack overflow

- [ ] **Monotonic Stack**
  - increasing stack
  - decreasing stack
  - next greater/smaller intuition

### Practice

#### Phase 1 — Stack Fundamentals

- [ ] **0020. Valid Parentheses**
- [ ] **1047. Remove All Adjacent Duplicates in String**
- [ ] **0682. Baseball Game**
- [ ] **0844. Backspace String Compare**
- [ ] **0155. Min Stack**

#### Phase 2 — Monotonic Stack

- [ ] **0496. Next Greater Element I**
- [ ] **0739. Daily Temperatures**
- [ ] **0503. Next Greater Element II**
- [ ] **0084. Largest Rectangle in Histogram**
