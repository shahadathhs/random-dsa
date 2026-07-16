# 🧩 RANDOM DSA

> My personal **DSA playground** — a *random* but growing mix of data structures & algorithms built from scratch, solved coding-interview problems (LeetCode & friends), and plain-English notes on how it all works. Built to *understand*, not just to use.

<p align="left">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white">
  <img alt="Dependencies" src="https://img.shields.io/badge/dependencies-none-brightgreen">
  <img alt="Status" src="https://img.shields.io/badge/status-growing-blueviolet">
</p>

---

## 🗂️ What's inside

This repo intentionally mixes three kinds of content — hence *random*-dsa:

| | Type | What it is |
| :--: | :--- | :--------- |
| 🏗️ | **Data structures** | Core structures implemented from first principles (no built-in shortcuts). |
| ⚙️ | **Algorithms** | Classic algorithms (sorting, searching, traversal, …) coded from scratch. |
| 🧮 | **Problem solutions** | Solved LeetCode / interview problems, often with multiple approaches compared. |
| 📝 | **Notes** | Markdown write-ups on concepts, patterns, and complexity. |

Everything is grouped into **topic folders**. It's a grab-bag by design: whatever I'm learning next lands here.

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

See [`leetcode/README.md`](leetcode/README.md) for the folder layout and naming convention.

### Data-structure & algorithm modules — run directly

The `array/` and `hash_map/` files are fully self-contained:

```bash
python3 array/dynamic_array.py
make ds FILE=hash_map/hash_map.py        # equivalent, via make
```

Browse any folder to see what's there — each file opens with a concept glossary that explains itself.

---

## 🎯 Philosophy

- ✍️ **Learn by building** — written from first principles, minimizing built-in shortcuts.
- 📖 **Documented deeply** — every file opens with a concept glossary and carries docstrings + complexity notes on each function.
- 🔬 **Multiple angles** — problems solved several ways (brute force → optimal) to make the trade-offs concrete.
- 🐍 **Idiomatic Python** — dunder methods (`len`, `in`, indexing) make custom structures feel native.

---
