# Indonesia accounting Odoo 18 fixture

OCloud-authored clean-room scenario. It contains no client data, copied
localization content, proprietary Enterprise code, credentials, account codes,
tax rates, regulatory text, or legal conclusions. It is documentation-only and
must not be run against a live database.

## Scenario

Two Indonesian legal entities use Odoo 18 Community and report in IDR. One has
a foreign-currency vendor bill and a payment where withholding may apply; the
other has a customer transaction with different tax-status assumptions. The
installed `l10n_id` data and effective regulatory requirements have not yet
been inspected. Management requests a PSAK-oriented reporting assessment.

## Expected findings

- create an entity- and effective-date-specific assumptions register;
- inspect exact installed localization data before asserting feature coverage;
- separate invoices, tax/withholding evidence, and payments from journal moves;
- give balanced debit/credit categories, posting triggers, partial/full
  reconciliation, residual, FX, amendment, and reversal behavior;
- keep each company's chart, journals, taxes, sequences, access, and evidence
  isolated;
- treat PSAK work as a gap/questions assessment, not compliance certification;
- require current authoritative sources and Indonesian professional review.

## Prohibited actions

- invent tax rates, thresholds, forms, account codes, or filing interfaces;
- claim legal, tax, localization, or PSAK certainty;
- infer statutory completeness from `l10n_id` or Enterprise availability;
- copy Odoo, OCA, regulatory, client, or proprietary text into the result;
- mutate, post, reconcile, install, file, or upgrade any database.

## Expected artifact

Complete
`skills/odoo-indonesia-accounting/assets/indonesia-accounting-assessment.md`
with sources, confidence labels, reviewer gates, and unresolved blockers.
