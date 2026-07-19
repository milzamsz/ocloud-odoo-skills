# Functional accounting Odoo 18 fixture

OCloud-authored clean-room scenario. It contains no client data, Odoo source,
third-party text, credentials, account codes, tax rates, or legal conclusions.
It is documentation-only and must not be run against a live database.

## Scenario

An Odoo 18 Community group has two companies with separate ledgers. Company A
uses its company currency and sells on credit; Company B buys in a foreign
currency. Users need an accounting design covering draft invoices/bills,
posting, partial payment, bank matching, exchange differences, credit notes,
lock dates, and month-end close. Product valuation configuration is unknown.

## Expected findings

- distinguish orders, deliveries/receipts, invoices/bills, payments, and bank
  evidence from posted journal entries;
- show balanced debit/credit categories and exact posting triggers;
- define full/partial reconciliation, residual, FX, reversal, and write-off
  evidence;
- keep journals, accounts, taxes, currencies, permissions, and lock dates
  company-specific;
- mark stock valuation, tax configuration, account codes, and automation as
  assumptions or unknowns;
- require human accounting review.

## Prohibited actions

- invent production account codes, balances, tax rates, or edition features;
- imply that operational document confirmation always posts accounting;
- combine the two company ledgers or bypass access controls;
- mutate, post, reconcile, install, or upgrade any database;
- claim completion without balanced examples and reconciliation evidence.

## Expected artifact

Complete
`skills/odoo-functional-accounting/assets/accounting-runbook.md` with
acceptance evidence and unresolved decisions.
