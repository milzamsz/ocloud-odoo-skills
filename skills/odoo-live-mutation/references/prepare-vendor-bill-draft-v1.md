# `prepare_vendor_bill_draft.v1` contract

Load only after the shared contract approves the exact target cell. All current
target cells remain blocked.

## Outcome and bounds

Create one draft `account.move` with forced `move_type=in_invoice` and trusted
company. Bind vendor, currency, invoice/due dates, payment term, vendor reference,
and approved lines. Purchase orders and receipts are evidence, not authorization
to create or alter procurement documents.

Never post, pay, reconcile, create purchase/receipt records, or invent accounts,
taxes, quantities, prices, currency, or matching tolerances.

## Required evidence

- Require AP ownership, vendor/company access, accounting and purchase evidence,
  discrepancies, duplicate review, and an accounting-authorized reviewer.
- Explain that a draft bill is an operational accounting document with no posted
  journal entry yet; debit/credit and tax effects occur only when later posted.
- Verify `state=draft`, `move_type=in_invoice`, company, vendor, currency, dates,
  reference, lines, taxes, quantities, prices, and purchase/receipt evidence.
- Return the normalized `draft_write` receipt with manual correction owner. An
  uncertain create is blocked and not retried.
