# ---------------------------------------------------------------------------
# random-dsa — task runner
#
#   make run N=1                        Run the demo for problem 1
#   make run N=217                      (numbers are zero-padded automatically)
#   make test                          Run every solution's demo
#   make list                          List all solved problems
#   make new N=217 NAME=contains_duplicate   Scaffold a new problem from the template
#   make ds FILE=hash_map/hash_map.py  Run a data-structure module's demo
#   make help                          Show this help
#
# Solutions live in leetcode/<range>/<num>_<name>.py and import shared demo
# helpers from leetcode/_demo.py, so runs set PYTHONPATH=leetcode.
# ---------------------------------------------------------------------------

PY       := python3
LEETCODE := leetcode

# Zero-pad the requested problem number to 4 digits (N=1 -> 0001).
NUM := $(shell printf '%04d' $(N) 2>/dev/null)

.PHONY: help run test list new ds

help:
	@sed -n '2,13p' $(MAKEFILE_LIST) | sed 's/^# \{0,1\}//'

run:
	@test -n "$(N)" || { echo "Usage: make run N=<problem-number>"; exit 1; }
	@file=$$(ls $(LEETCODE)/*/$(NUM)_*.py 2>/dev/null | head -n1); \
	if [ -z "$$file" ]; then echo "No solution found for problem $(NUM)."; exit 1; fi; \
	echo "Running $$file"; echo; \
	PYTHONPATH=$(LEETCODE) $(PY) "$$file"

test:
	@fail=0; \
	for f in $(LEETCODE)/*/[0-9]*.py; do \
	  [ -e "$$f" ] || continue; \
	  echo "########## $$f ##########"; \
	  PYTHONPATH=$(LEETCODE) $(PY) "$$f" || fail=1; \
	  echo; \
	done; \
	if [ $$fail -ne 0 ]; then echo "Some demos failed."; exit 1; fi; \
	echo "All demos ran."

list:
	@ls $(LEETCODE)/*/[0-9]*.py 2>/dev/null | sed 's#.*/##; s#\.py$$##' | sort || true

new:
	@test -n "$(N)" -a -n "$(NAME)" || { echo "Usage: make new N=<number> NAME=<snake_title>"; exit 1; }
	@block=$$(( ($(N) - 1) / 100 )); lo=$$(( block * 100 + 1 )); hi=$$(( block * 100 + 100 )); \
	dir=$$(printf '%s/%04d-%04d' $(LEETCODE) $$lo $$hi); \
	dest=$$(printf '%s/%04d_%s.py' "$$dir" $(N) $(NAME)); \
	if [ -e "$$dest" ]; then echo "$$dest already exists."; exit 1; fi; \
	mkdir -p "$$dir"; \
	cp $(LEETCODE)/TEMPLATE.py "$$dest"; \
	echo "Created $$dest"; \
	echo "Next: fill in the problem, then run  make run N=$(N)"

ds:
	@test -n "$(FILE)" || { echo "Usage: make ds FILE=<path-to-module.py>"; exit 1; }
	@$(PY) "$(FILE)"
