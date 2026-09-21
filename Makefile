.PHONY: validate test lint format package-check capability-check

validate:
	python3 scripts/validate_repository.py

lint:
	ruff check scripts tests skills/*/scripts

format:
	ruff format scripts tests skills/*/scripts

test:
	pytest -q

package-check: validate
	python3 scripts/package_check.py

capability-check:
	python3 scripts/validate_mutation_capabilities.py --contract "$(CONTRACT)"
