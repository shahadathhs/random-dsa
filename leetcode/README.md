# LeetCode Solutions

One problem per file, one file per problem. Solutions are grouped into
**range-based subfolders** of 100 problems each so the folder never gets huge.

## Layout

```
leetcode/
├── _demo.py          # shared demo helpers (section, check)
├── TEMPLATE.py       # copy this to start a new problem
├── 0001-0100/
│   └── 0001_two_sum.py
├── 0101-0200/
└── 0201-0300/
```

## Naming convention

- **Folder:** `<lo>-<hi>` in blocks of 100 — `0001-0100`, `0101-0200`, `0201-0300`, …
- **File:** `<4-digit-number>_<snake_case_title>.py` — e.g. `0001_two_sum.py`, `0217_contains_duplicate.py`

Zero-padding to 4 digits keeps everything sorting in problem order.

## Workflow (via the Makefile at the repo root)

```bash
make new N=217 NAME=contains_duplicate   # scaffold into the right range folder
make run N=217                           # run one problem's demo (number auto-padded)
make list                                # list every solved problem
make test                                # run all demos
```

`make new` computes the range folder automatically and copies `TEMPLATE.py`.
Each solution imports `from _demo import section, check`; the Makefile sets
`PYTHONPATH=leetcode` so that import resolves from any range subfolder.

## Progress

### Phase 1 — Arrays & Hash Maps

- [x] `0001_two_sum.py` — Two Sum (Easy)
- [x] `0217_contains_duplicate.py` — Contains Duplicate (Easy)
- [x] `0242_valid_anagram.py` — Valid Anagram (Easy)
- [ ] `0349_intersection_of_two_arrays.py` — Intersection of Two Arrays (Easy)

### Phase 2 — Two Pointers

- [ ] `0125_valid_palindrome.py` — Valid Palindrome (Easy)
- [ ] `0088_merge_sorted_array.py` — Merge Sorted Array (Easy)
- [ ] `0977_squares_of_a_sorted_array.py` — Squares of a Sorted Array (Easy)
- [ ] `0026_remove_duplicates_from_sorted_array.py` — Remove Duplicates from Sorted Array (Easy)

### Phase 3 — Dynamic Array Thinking

- [ ] `0027_remove_element.py` — Remove Element (Easy)
- [ ] `0283_move_zeroes.py` — Move Zeroes (Easy)
- [ ] `0189_rotate_array.py` — Rotate Array (Medium)
