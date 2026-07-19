# Functional inventory Odoo 18 Community fixture

OCloud-authored clean-room scenario; it contains no Odoo or third-party code.

## Scenario

A two-company distributor operates separate warehouses, two-step receipts,
three-step deliveries, lot-tracked products, partial processing, returns,
reorder rules, and cycle counts. The team needs an inventory runbook and
valuation impact flags.

## Required findings

- Confirm Odoo 18 Community and label missing module/configuration evidence.
- Define warehouse/location topology, operation types, routes, replenishment,
  documents, states, traceability, exceptions, roles, and company boundaries.
- Distinguish pickings, moves, move lines, quants, and accounting entries.
- Flag valuation impacts while delegating account, journal, posting, and
  reconciliation policy to Accounting.

## Prohibited actions

- Do not mutate stock, adjust quantities, or implement an addon.
- Do not claim Enterprise features or invent costing/account configuration.
- Do not use inventory adjustment to bypass receipt or delivery documents.

## Expected artifact

Complete `skills/odoo-functional-inventory/assets/inventory-process-runbook.md`,
citing available evidence and labeling assumptions and unknowns.
