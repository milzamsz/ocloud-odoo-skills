---
name: odoo-functional-purchase
description: Use this skill when designing or validating an Odoo 17, 18, or 19 Community or Enterprise procure-to-pay operational process, including requisition inputs, requests for quotation, purchase orders, receipt handoff, vendor bill matching readiness, vendor terms, approvals, exceptions, and completion evidence. Do not use it for sales, warehouse-only execution, accounting policy, or addon implementation.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients. Requires confirmed Odoo 17, 18, or 19 Community or Enterprise context for version-sensitive decisions.
metadata:
  version: "0.1.0"
  author: OCloud
  status: experimental
  risk: advisory
  odoo:
    versions: ["17.0", "18.0", "19.0"]
    editions: [community, enterprise]
  hermes:
    tags: [odoo, purchase, procurement, functional]
---

# Odoo Functional Purchase

## Purpose

Produce an evidence-backed Odoo 17, 18, or 19 Community or Enterprise procure-to-pay operational design and configuration runbook from purchasing demand through RFQ, purchase order, receipt handoff, and vendor bill matching readiness.

## Use when

- mapping RFQs, purchase orders, vendor terms, approvals, receipts, or bill control;
- defining procurement actors, document states, exceptions, permissions, and acceptance criteria;
- validating whether a proposed purchasing process fits Odoo 17, 18, or 19 Community or Enterprise.

## Do not use when

- the primary outcome is sales, warehouse route execution, or accounting AP policy;
- an approved design only needs implementation, testing, review, security audit, OCA contribution, or upgrade work.

## Required inputs and composition

1. Require `odoo-context-discovery` when version, edition, repository layout, modules, or company context is unknown.
2. Require `odoo-solution-design` before recommending custom code or a third-party component.
3. Delegate code to `odoo-addon-development`, tests to `odoo-testing`, security analysis to `odoo-security-audit`, review to `odoo-code-review`, OCA work to `odoo-oca-development`, and major-version work to `odoo-version-upgrade`.
4. Obtain demand sources, buyers, vendors, products, companies, currencies, taxes, approval thresholds, receipt policy, bill control, exceptions, volume, and success criteria.

## Workflow

1. Confirm Odoo 17.0, 18.0, or 19.0 Community or Enterprise and identify installed `purchase` and integration capabilities from evidence.
2. Map actors and operational documents: demand input, RFQ, purchase order, receipt handoff, and vendor bill matching readiness.
3. Define state transitions, ownership, approvals, cancellation, partial receipt, backorder, return, quantity/price variance, and bill exceptions.
4. Specify master data and configuration: vendors, products, units, lead times, vendor prices, currencies, payment terms, taxes as assumptions, warehouses, and bill control policy.
5. Mark boundaries: Inventory owns receipt and route execution; Accounting owns vendor bill posting, tax, payment, and reconciliation.
6. Evaluate Standard then Configured behavior. Invoke `odoo-solution-design` for Third-party, Low-code, Custom, or External options.
7. Define permissions, multi-company separation, audit evidence, acceptance criteria, unknowns, and handoffs.

## Safety and decision rules

- Treat live systems as read-only unless the user explicitly authorizes the exact mutation.
- Do not claim behavior from another edition; use only the confirmed target cell and installed-module evidence.
- Keep RFQ, purchase order, receipt, and vendor bill distinct.
- Do not invent tax, account, fiscal-position, tolerance, or legal conclusions.
- Label facts as Confirmed, Inferred, Assumed, or Unknown and cite source paths.

## Required output

Use `assets/purchase-process-runbook.md`. Include context, evidence, actors, document/state map, configuration decisions, exception paths, inventory/accounting handoffs, permissions/company scope, acceptance criteria, risks, unknowns, and delegated next actions.

## Verification

- Version and edition are confirmed independently.
- RFQ, purchase order, receipt handoff, and bill matching readiness are distinct.
- Bill control, partial/cancel/return/variance paths, permissions, and multi-company behavior are addressed.
- No implementation or accounting policy is silently designed.
- Every completion claim has evidence or a testable acceptance criterion.

## Reference to load

Read exactly one `references/odoo-{17,18,19}-{community,enterprise}.md` file after the target version and edition are confirmed.

## Failure and escalation

Stop and report a blocker when edition, installed modules, company rules, approvals, receipt policy, or bill control materially changes the design. Escalate accounting, tax, legal, security, and customization decisions to the owning skill or human reviewer.
