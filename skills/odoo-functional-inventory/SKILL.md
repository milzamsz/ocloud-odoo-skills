---
name: odoo-functional-inventory
description: Use this skill when designing or validating an Odoo 18 Community inventory and warehouse process, including warehouses, locations, routes, replenishment, receipts, internal transfers, deliveries, returns, lots or serials, counts, exceptions, and stock valuation impact flags. Do not use it for sales, purchasing, manufacturing, accounting valuation policy, or addon implementation.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients. Requires confirmed Odoo 18 Community context for version-sensitive decisions.
metadata:
  version: "0.1.0"
  author: OCloud
  status: experimental
  risk: advisory
  odoo:
    versions: ["18.0"]
    editions: [community]
  hermes:
    tags: [odoo, inventory, stock, warehouse, functional]
---

# Odoo Functional Inventory

## Purpose

Produce an evidence-backed Odoo 18 Community inventory and warehouse design and configuration runbook covering movement, replenishment, traceability, exceptions, controls, and accounting impact flags.

## Use when

- mapping warehouses, locations, operation types, routes, rules, replenishment, or stock moves;
- defining receipts, internal transfers, deliveries, returns, lots/serials, packages, counts, and exceptions;
- validating whether a proposed stock process fits Odoo 18 Community.

## Do not use when

- the primary outcome is sales, procurement, manufacturing, or detailed stock accounting policy;
- an approved design only needs implementation, testing, review, security audit, OCA contribution, or upgrade work.

## Required inputs and composition

1. Require `odoo-context-discovery` when version, edition, repository layout, modules, or company context is unknown.
2. Require `odoo-solution-design` before recommending custom code or a third-party component.
3. Delegate code to `odoo-addon-development`, tests to `odoo-testing`, security analysis to `odoo-security-audit`, review to `odoo-code-review`, OCA work to `odoo-oca-development`, and major-version work to `odoo-version-upgrade`.
4. Obtain products, companies, warehouses, locations, demand/supply sources, units, tracking, ownership, packaging, lead times, replenishment policy, count policy, exceptions, volume, and success criteria.

## Workflow

1. Confirm Odoo 18.0 Community and identify installed `stock` and integration capabilities from evidence.
2. Map physical and virtual locations, warehouses, operation types, routes, rules, and company ownership.
3. Map operational documents and transitions for receipt, internal transfer, delivery, return, scrap, adjustment/count, and replenishment.
4. Define reservation, partial processing, backorder, cancellation, traceability, package, ownership, and negative-stock exception behavior.
5. Specify master data and configuration: storable products, units, lots/serials, lead times, routes, reorder rules, removal strategy assumptions, and responsible roles.
6. Mark boundaries: Sales owns commercial order policy; Purchase owns procurement approval; Manufacturing owns BoMs and production; Accounting owns valuation method, accounts, journal entries, posting, and reconciliation. Record valuation impact flags only.
7. Evaluate Standard then Configured behavior. Invoke `odoo-solution-design` for Third-party, Low-code, Custom, or External options.
8. Define permissions, multi-company isolation, audit evidence, acceptance criteria, unknowns, and handoffs.

## Safety and decision rules

- Treat live systems as read-only unless the user explicitly authorizes the exact mutation.
- Do not claim Enterprise behavior or compatibility; this skill supports Odoo 18 Community only.
- Keep picking, stock move, move line, quant, and accounting entry conceptually distinct.
- Never recommend inventory adjustment as a shortcut around unresolved document flows.
- Do not invent valuation, account, costing, tax, or legal conclusions.
- Label facts as Confirmed, Inferred, Assumed, or Unknown and cite source paths.

## Required output

Use `assets/inventory-process-runbook.md`. Include context, evidence, topology, document/state map, routes and replenishment, traceability, exceptions, domain handoffs, valuation impact flags, permissions/company scope, acceptance criteria, risks, unknowns, and delegated next actions.

## Verification

- Version and Community edition are confirmed.
- Warehouses, locations, routes/rules, operation types, and company ownership are coherent.
- Partial/backorder/return/count/traceability paths and permissions are addressed.
- Valuation is flagged without inventing accounting policy.
- No implementation or sibling-domain workflow is silently designed.
- Every completion claim has evidence or a testable acceptance criterion.

## Reference to load

Read `references/odoo-18-community.md` only after Odoo 18.0 Community is confirmed.

## Failure and escalation

Stop and report a blocker when edition, installed modules, product type, ownership, company, route, traceability, or valuation policy materially changes the design. Escalate manufacturing, accounting, tax, legal, security, and customization decisions to the owning skill or human reviewer.
