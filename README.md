# 🧩 RANDOM DSA

> My personal **Python + DSA playground** — a *random* but growing mix of Python
> fundamentals, data structures & algorithms built from scratch, solved
> coding-interview problems (LeetCode & friends), and plain-English notes on how
> it all works. Built to *understand*, not just to use.

<p align="left">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white">
  <img alt="Dependencies" src="https://img.shields.io/badge/dependencies-none-brightgreen">
  <img alt="Status" src="https://img.shields.io/badge/status-growing-blueviolet">
</p>

---

## 🗂️ What's inside

This repo intentionally mixes several kinds of content — hence *random*-dsa.
The throughline is simple: **learn Python by building things from the ground
up**, and learn DSA by implementing every structure and pattern yourself.

| | Type | What it is |
| :--: | :--- | :--------- |
| 🐍 | **Python fundamentals** | Language features explored hands-on — data model, comprehensions, iterators, decorators, context managers, and more. |
| 🏗️ | **Data structures** | Core structures implemented from first principles (no built-in shortcuts). |
| ⚙️ | **Algorithms & patterns** | Pointer techniques, rotation, sliding windows, and other patterns coded from scratch. |
| 🧮 | **Problem solutions** | Solved LeetCode / interview problems, often with multiple approaches compared. |

Everything is grouped into **topic folders**. It's a grab-bag by design: whatever
I'm learning next lands here.

---

## 📁 Folder layout

```
random-dsa/
├── python/            Python language fundamentals (numbers, strings, lists, dicts, …)
├── data_structures/   Structures built from first principles (dynamic array, hash map)
├── algorithms/        Technique & pattern guides (pointers, rotation, two-sum)
└── leetcode/          Interview problems, one per file, grouped in range folders
```

Each file is **self-contained** — open any one and it explains itself from a
concept glossary at the top down through the implementation to a runnable demo.

---

## ⚡ Running the code

No dependencies — just **Python 3** and **make**. Every file runs its own demo.

### LeetCode solutions — via the Makefile

Solutions live in `leetcode/<range>/<num>_<name>.py` (range folders of 100).
Drive them by problem number:

```bash
make run N=1                             # run problem 1's demo (number auto-padded)
make list                                # list every solved problem
make test                                # run all demos
make new N=217 NAME=contains_duplicate   # scaffold a new problem from the template
make help                                # show all targets
```

See [`leetcode/README.md`](leetcode/README.md) for the folder layout and naming
convention.

### Concept guides & Python modules — via the Makefile

The `python/`, `data_structures/`, and `algorithms/` files are fully self-contained:

```bash
make ds FILE=python/05_lists.py
make ds FILE=data_structures/dynamic_array.py
make ds FILE=algorithms/pointers.py
```

Browse any folder to see what's there — each file opens with a concept glossary
that explains itself.

---

## 🎯 Philosophy

- ✍️ **Learn by building** — everything written from first principles, minimizing built-in shortcuts. Understanding the *why* behind a dict or a list matters before reaching for one.
- 📖 **Documented deeply** — every file opens with a concept glossary and carries docstrings + complexity notes on each function. Someone should be able to understand the approach from the file alone.
- 🔬 **Multiple angles** — problems solved several ways (brute force → optimal) to make the trade-offs concrete.
- 🐍 **Python fluency alongside DSA** — the language is learned through use, not in isolation. Dunder methods, iterators, comprehensions, and the data model show up naturally when you build your own structures and solve real problems with them.

---
