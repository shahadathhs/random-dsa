# Contributing

Thanks for your interest in **random-dsa**! This is a learning-first repo:
solutions are documented deeply, run their own demos, and use no third-party
dependencies.

Repo: <https://github.com/shahadathhs/random-dsa>

## Prerequisites

- **Python 3** (`python3 --version`)
- **make** (preinstalled on macOS/Linux; on Windows use WSL or Git Bash)

No `pip install` needed — the repo has zero dependencies.

## Running things

```bash
git clone https://github.com/shahadathhs/random-dsa.git
cd random-dsa

make run N=1          # run a LeetCode solution's demo by problem number
make list             # list all solved problems
make test             # run every solution's demo
make help             # show all targets
```

Data-structure modules run directly, e.g. `python3 hash_map/hash_map.py`.

## Adding a LeetCode solution

1. **Scaffold** from the template — the range folder is picked automatically:

   ```bash
   make new N=217 NAME=contains_duplicate
   # -> leetcode/0201-0300/0217_contains_duplicate.py
   ```

2. **Fill it in**, following the house style (see `leetcode/0001-0100/0001_two_sum.py`):
   - Module docstring: short summary + LeetCode URL + difficulty.
   - `Problem:` block — paste the official problem statement verbatim.
   - Concept glossary — one `"""..."""` block per idea the solution uses.
   - Structure tree — list each function with its time/space complexity.
   - The solution function(s), each with a `Time:` / `Space:` / `Args:` / `Returns:` docstring and inline comments on the tricky lines.
   - A demo under `if __name__ == "__main__"` using `section()` / `check()` imported from `_demo`.

3. **Verify** it runs and every check passes:

   ```bash
   make run N=217
   ```

4. **Tick the box** for the problem in `leetcode/README.md`.

## Conventions

- **File naming:** `<4-digit-number>_<snake_case_title>.py` (zero-padded).
- **Folder naming:** `<lo>-<hi>` in blocks of 100 (`0001-0100`, `0101-0200`, …).
- **Style:** free functions (not `class Solution`), no type-hint imports, demos
  print labelled `PASS`/`FAIL` via the shared helpers.
- Keep each file **self-explanatory** — someone should understand the approach
  from the file alone.

## Commit messages

Conventional-commit style is used throughout, e.g.
`feat: add solution for 217 contains-duplicate`.
