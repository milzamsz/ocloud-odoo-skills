# Functional sales Odoo 18 Community fixture

OCloud-authored clean-room scenario; it contains no Odoo or third-party code.

## Scenario

A two-company distributor uses CRM optionally, customer-specific pricelists,
stock and service products, partial delivery, and different ordered/delivered
invoice policies. The team needs a quotation-to-invoice-readiness runbook.

## Required findings

- Confirm Odoo 18 Community and label missing module/configuration evidence.
- Separate opportunity, quotation, sales order, stock handoff, and invoice.
- Define actors, states, pricelist and invoice-policy decisions, exceptions,
  company boundaries, acceptance criteria, and completion evidence.
- Delegate route/picking detail to Inventory and posting/tax/reconciliation to
  Accounting.

## Prohibited actions

- Do not mutate a database or implement an addon.
- Do not claim Enterprise features or invent tax/account configuration.
- Do not collapse operational documents into journal entries.

## Expected artifact

Complete `skills/odoo-functional-sales/assets/sales-process-runbook.md`, citing
available evidence and labeling assumptions and unknowns.
