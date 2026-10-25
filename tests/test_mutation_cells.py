"""Cell-set rule of the cross-repository mutation capability validator."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.validate_mutation_capabilities import EXPECTED_CELLS, cell_set_errors  # noqa: E402


def test_baseline_cells_are_valid():
    assert cell_set_errors(set(EXPECTED_CELLS)) == []


def test_odoo20_pair_is_accepted_together():
    assert cell_set_errors(EXPECTED_CELLS | {"odoo20-community", "odoo20-enterprise"}) == []


def test_odoo20_single_edition_is_rejected():
    assert cell_set_errors(EXPECTED_CELLS | {"odoo20-community"}) == [
        "optional cells must be declared together: ['odoo20-community', 'odoo20-enterprise']"
    ]


def test_missing_baseline_or_unknown_cell_is_rejected():
    assert cell_set_errors(EXPECTED_CELLS - {"odoo17-community"})
    assert cell_set_errors(EXPECTED_CELLS | {"odoo21-community"})
