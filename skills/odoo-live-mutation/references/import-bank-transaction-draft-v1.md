# `import_bank_transaction_draft.v1` contract

The capability ID is retained for compatibility, but its operation class is
`accounting_suspense_write`, not `draft_write`. Load only after the shared
contract approves the exact target cell. All current target cells remain blocked.

## Outcome and accounting impact

Create one standard `account.bank.statement.line` for the trusted company and
bank journal. Odoo immediately posts the inherited move to the journal's
suspense account; the result must remain unreconciled.

Preview the signed amount, company currency and optional foreign-currency pair,
bank/journal side, suspense counterpart, debit/credit direction, transaction
date, external transaction ID, partner if supplied, and evidence references.
Do not reconcile, complete a statement, create partners/accounts, invoke a
workflow, delete, or hide discrepancies.

## Required evidence

- Require accounting approval, unique bank external ID, duplicate review,
  currency consistency, journal/company access, evidence, and discrepancies.
- Verify `state=posted`, `is_reconciled=false`, journal, company, signed amount,
  currencies, suspense lines, debit/credit balance, and external reference.
- Name the accountant who owns correction. Before reconciliation, correction is
  a reviewed manual deletion/reversal according to Odoo policy; after
  reconciliation use the normal accounting reversal/correction workflow.
- Return the normalized `accounting_suspense_write` receipt with compensation
  status and owner. Never retry an uncertain import automatically.
