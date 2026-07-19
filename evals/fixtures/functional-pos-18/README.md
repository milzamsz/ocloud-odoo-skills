# Odoo 18 CE POS fixture

## Scenario

A retailer has two shops, cash and card payments, intermittent connectivity,
manager-controlled refunds, and one stock location per shop. It needs a POS
process design, not implementation or live configuration.

## Required findings

- session opening, ordering, payment, refund, cash movement, and closing states;
- cashier versus manager controls;
- payment acceptance distinguished from Odoo synchronization;
- offline limits, reconnection evidence, and duplicate prevention;
- stock and accounting handoffs;
- explicit Odoo 18 Community scope, assumptions, and unknowns;
- testable acceptance criteria and completion evidence.

## Prohibited actions

- changing a live Odoo configuration or database;
- claiming a receipt proves payment reconciliation;
- promising unlimited offline operation;
- inventing Enterprise or payment-provider behavior;
- implementing code instead of composing the appropriate Phase 1 skill.

## Expected artifact

A completed `assets/pos-process-design.md`.
