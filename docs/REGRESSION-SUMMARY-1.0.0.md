# Regression Summary 1.0.0

Three independent clean-session artifact regressions reviewed all eight skills
against the Odoo 18 Community stable baseline.

## Results

- Every skill: 16/16 trigger labels coherent.
- Every outcome: prohibited-action gate passed.
- Scores remained within the established 88–100 range.
- Structural validation and package checks passed in all available runs.
- The project venv completes `make test` with 4 passing tests.

One regression identified that the OCA outcome was still labeled 19.0. The
release candidate resolves this with a clean-room Odoo 18 Community
contribution fixture and matching outcome case.

## Scope

Odoo 17, Odoo 19, and Enterprise remain advisory. This regression does not
promote them to stable support.
