.PHONY: all svg check clean

PYTHON ?= python3

all:
	$(PYTHON) scripts/build_logo_suite.py

svg:
	$(PYTHON) scripts/build_logo_suite.py --svg-only

check:
	$(PYTHON) scripts/build_logo_suite.py --check

clean:
	rm -rf dist/svg dist/png preview/*.png preview/*.svg dist/manifest.json
