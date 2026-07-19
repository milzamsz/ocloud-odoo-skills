.PHONY: validate test lint format package-check

validate:
	python3 scripts/validate_repository.py

lint:
	ruff check scripts tests

format:
	ruff format scripts tests

test:
	pytest -q

package-check: validate
	python3 scripts/package_check.py
