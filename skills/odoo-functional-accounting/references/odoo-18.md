# Odoo 18 Community accounting reference

Supported baseline: Odoo 18.0 Community. Confirm installed modules and target
source before relying on a feature. Enterprise-only workflows are advisory and
require official documentation or licensed source inspection.

## Core model

- `account.move` represents journal entries and accounting documents such as
  customer invoices, vendor bills, refunds, and miscellaneous entries.
- `account.move.line` carries debit, credit, account, partner, currency, tax,
  and reconciliation-relevant detail.
- Draft documents are editable accounting proposals. Posting validates the move,
  assigns the applicable sequence, and creates ledger impact; verify the exact
  trigger in configuration and target source.
- Reconciliation matches reconcilable journal items, commonly receivable,
  payable, bank, and cash items. It may be full or partial and can leave a
  residual, exchange difference, or approved write-off.

## Process boundaries

- Sales orders, purchase orders, deliveries, receipts, and payment instructions
  are operational documents. They do not become journal entries merely by
  confirmation; identify the configured invoice, valuation, payment, or manual
  posting event.
- A customer invoice normally debits receivable and credits income, plus tax
  liability where configured. A vendor bill normally debits expense or asset
  and credits payable. These are patterns, not account-code prescriptions.
- Payment registration and bank statement processing can involve liquidity and
  outstanding accounts. State both the posting and later reconciliation steps.
- Stock accounting depends on product category, valuation, costing, and installed
  modules; do not infer entries from a receipt or delivery alone.

## Controls to verify

Company ownership, journal and account configuration, currency and rates, taxes
and fiscal positions, lock dates, sequence behavior, posting permissions,
reversal policy, outstanding/suspense accounts, and reconciliation evidence.

Relevant Odoo 18 Community source modules include `account` and localization
modules present in the target checkout. Inspect payment, bank statement, and
reconciliation models in that checkout rather than extrapolating Enterprise
accounting applications.
