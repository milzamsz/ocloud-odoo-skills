# Stable Release 1.0.0

## Stable contract

The eight Phase 1 procedural skills are stable for an Odoo 18.0 Community
evidence baseline. Odoo 17.0, Odoo 19.0, and Enterprise material is retained as
advisory context and must not be represented as equivalently verified support.

## Evidence

- repository validation, lint, tests, and package checks pass;
- three independent clean-session regression reviews cover all eight skills;
- trigger datasets provide 8 positive and 8 negative cases per skill;
- prohibited-action checks pass;
- the Odoo 18 Community minimal addon installs and tests on a disposable
  database;
- Hermes clean-profile scan and installation pass;
- named maintainer review is recorded in `HUMAN-REVIEW-1.0.0.md`.

Regression details are recorded in `REGRESSION-SUMMARY-1.0.0.md`.

## Remaining advisory limits

- Odoo 17/19 and Enterprise require exact source and runtime evidence;
- OCA 18 local checkout coverage is incomplete;
- production mutations remain in the future controlled plugin/MCP layer.
