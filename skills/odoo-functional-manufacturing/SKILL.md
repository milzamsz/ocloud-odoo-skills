---
name: odoo-functional-manufacturing
description: Use this skill when designing an Odoo manufacturing process covering bills of materials, manufacturing orders, component consumption, work centers and operations, by-products, lots or serials, scrap, and backorders. Do not use it for warehouse route depth, accounting policy, maintenance, PLM, or addon implementation.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients. Verified for Odoo 17.0, 18.0, or 19.0 Community or Enterprise.
metadata:
  version: "0.1.0"
  author: OCloud
  status: experimental
  risk: advisory
  odoo:
    versions: ["17.0", "18.0", "19.0"]
    editions: [community, enterprise]
  hermes:
    tags: [odoo, manufacturing, mrp, functional]
---

# Odoo Functional Manufacturing

## Purpose

Produce an evidence-based Odoo 17, 18, or 19 Community or Enterprise design from bill of materials through production completion, exceptions, and inventory handoff.

## Preconditions and composition

- State version, edition, companies, products, units, warehouses, traceability needs, and production actors.
- Load `odoo-context-discovery` when version, edition, repository, or runtime is unknown.
- Load `odoo-solution-design` before recommending custom code, third-party addons, or external infrastructure.
- Delegate implementation, tests, reviews, security audits, OCA work, and upgrades to the corresponding Phase 1 skills.

## Workflow

1. Define manufactured products, components, BoM variants, quantities, units, by-products, and effective assumptions.
2. Map demand to manufacturing-order creation without taking ownership of warehouse route design.
3. Describe confirmation, component availability, reservation, production, consumption, finished quantity, and completion states.
4. Define operations, work centers, dependencies, capacity assumptions, and required operator evidence where applicable.
5. Define lots/serials, substitutions, partial production, backorders, scrap, cancellation, and rework exceptions.
6. Hand procurement, replenishment, locations, routes, and stock valuation depth to `odoo-functional-inventory`.
7. Hand journal entries, costing policy, debit/credit, posting, and reconciliation to `odoo-functional-accounting`.
8. Separate confirmed CE behavior from assumptions and Enterprise-only or third-party proposals.

## Decision and safety rules

- Prefer standard CE BoM and MO behavior before customization.
- Do not confuse planned quantities, reserved quantities, consumed quantities, and produced quantities.
- Require explicit traceability and exception ownership where lots or serials matter.
- Do not invent work-center capacity, lead time, costing, or quality policy.
- Do not mutate production or live inventory while producing the design.

## Required output

Copy `assets/manufacturing-process-design.md`. Include master data, state flow, roles, material and operation controls, exceptions, inventory/accounting handoffs, acceptance criteria, evidence, assumptions, and unknowns.

## Verification

- BoM-to-completion and partial/backorder paths are complete.
- Quantity and traceability states are unambiguous.
- Inventory route depth and accounting policy are delegated.
- Odoo 17, 18, or 19 Community or Enterprise support is explicit.

## Reference to load

Read exactly one `references/odoo-{17,18,19}-{community,enterprise}.md` file after the target version and edition are confirmed.

Read `references/odoo-18-community.md` for the verified CE baseline and inspect target source when a detail affects implementation.

## Failure and escalation

Stop and mark unknowns when units, traceability, subcontracting, capacity, costing, or edition capability is unverified. Escalate warehouse, accounting, and code changes to their owning workflows.
