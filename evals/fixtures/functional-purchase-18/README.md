# Functional purchase Odoo 18 Community fixture

OCloud-authored clean-room scenario; it contains no Odoo or third-party code.

## Scenario

A two-company distributor buys stock and services from multiple vendors.
Approvals vary by amount, stock may arrive partially, and vendor bills require
matching against ordered or received quantities. The team needs a procure-to-pay
operational runbook.

## Required findings

- Confirm Odoo 18 Community and label missing module/configuration evidence.
- Separate demand, RFQ, purchase order, receipt, and vendor bill.
- Define actors, states, approval and bill-control decisions, variance and
  exception paths, company boundaries, acceptance criteria, and evidence.
- Delegate routes/receipt execution to Inventory and posting/tax/reconciliation
  to Accounting.

## Prohibited actions

- Do not mutate a database or implement an addon.
- Do not claim Enterprise features or invent tax/account/tolerance policy.
- Do not treat operational documents as journal entries.

## Expected artifact

Complete `skills/odoo-functional-purchase/assets/purchase-process-runbook.md`,
citing available evidence and labeling assumptions and unknowns.
