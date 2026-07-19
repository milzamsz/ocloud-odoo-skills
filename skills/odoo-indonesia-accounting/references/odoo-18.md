# Odoo 18 Community Indonesia accounting reference

Supported baseline: Odoo 18.0 Community with the target checkout's Indonesian
localization modules. Enterprise behavior is advisory and requires official
documentation or licensed source evidence.

## Evidence boundary

- Inspect `l10n_id` manifests, dependencies, chart templates, account groups,
  taxes, tax repartition lines, fiscal positions, and reports in the exact Odoo
  18 source and installed database.
- Names and XML identifiers show packaged configuration; they do not establish
  that a rate, form, filing interface, or accounting treatment is current or
  applicable to a particular entity.
- QRIS-related models, controllers, crons, and tests in `l10n_id` are packaged
  CE payment evidence. Treat them as technical capabilities, not proof of
  current bank, tax, or regulatory compliance.
- Record legal entity status, transaction date, counterparty status, currency,
  and authoritative effective-dated source before reaching a tax conclusion.
- Keep regulatory text and proprietary Enterprise source out of this skill.

## Accounting analysis

For every Indonesian scenario, distinguish the commercial document and tax
evidence from the posted `account.move` and its lines. Document:

1. tax base and timing assumption;
2. debit and credit account categories;
3. tax or withholding split;
4. posting trigger and responsible role;
5. payment, receivable/payable, and withholding reconciliation;
6. residuals, rounding, foreign exchange, amendment, and reversal;
7. company ownership and cross-company prohibition or approved flow.

Withholding may create a receivable for the party whose payment was withheld or
a payable for the withholding party, but the actual treatment depends on the
transaction and approved current guidance. Never supply a rate or account code
without case-specific evidence.

## PSAK boundary

Use PSAK-oriented analysis to identify recognition, measurement, presentation,
disclosure, and chart/report mapping questions. Do not equate an Odoo chart,
report, or module with PSAK compliance. Require qualified professional review.

## Completion evidence

Retain assumptions, source dates, target-source observations, balanced example
entries, reconciliation outcomes, company access checks, and reviewer sign-off.

## Evidence paths

Resolve paths relative to the verified Odoo source root:

- `addons/l10n_id/__manifest__.py`
- `addons/l10n_id/models/template_id.py`
- `addons/l10n_id/data/template/account.account-id.csv`
- `addons/l10n_id/data/template/account.tax-id.csv`
- `addons/l10n_id/models/qris_transaction.py`
- `addons/l10n_id/tests/test_qris.py`
