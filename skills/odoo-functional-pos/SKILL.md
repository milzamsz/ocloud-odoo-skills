---
name: odoo-functional-pos
description: Use this skill when designing an Odoo Point of Sale process covering opening and closing sessions, orders, payments, cash control, refunds, offline operation, and stock handoff. Do not use it for generic sales order design, accounting policy, inventory route design, or POS addon implementation.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients. Verified for Odoo 18.0 Community.
metadata:
  version: "0.1.0"
  author: OCloud
  status: experimental
  risk: advisory
  odoo:
    versions: ["18.0"]
    editions: [community]
  hermes:
    tags: [odoo, pos, functional]
---

# Odoo Functional POS

## Purpose

Produce an evidence-based POS process design for Odoo 18 Community, from session opening through payment, stock handoff, reconciliation inputs, and session closing.

## Preconditions and composition

- State version, edition, companies, shops, actors, devices, payment methods, and connectivity constraints.
- Load `odoo-context-discovery` when version, edition, repository, or runtime is unknown.
- Load `odoo-solution-design` before recommending custom code, third-party addons, or external infrastructure.
- Delegate implementation, tests, reviews, security audits, OCA work, and upgrades to the corresponding Phase 1 skills.

## Workflow

1. Map cashier, manager, customer, and back-office responsibilities and permissions.
2. Describe configuration prerequisites: POS, products, taxes, pricelists, stock location, payment methods, and cash control.
3. Map session opening, order capture, payment, receipt, refund, cash movement, session closing, and exception states.
4. Define offline assumptions, synchronization risks, duplicate prevention, device/browser recovery, and evidence needed after reconnect.
5. Identify stock effects and hand route, replenishment, lot/serial, and valuation depth to `odoo-functional-inventory`.
6. Identify payment and tax outputs, but hand journals, posting, debit/credit, and reconciliation policy to `odoo-functional-accounting`.
7. Separate confirmed CE behavior from assumptions and Enterprise-only or third-party proposals.

## Decision and safety rules

- Prefer standard CE configuration before custom behavior.
- Never treat an accepted terminal payment as proof that Odoo recorded or reconciled it.
- Do not promise uninterrupted offline behavior; document tested limits and recovery.
- Do not expose unrestricted refunds, price changes, cash movements, or session closing.
- Do not mutate a live POS or production database while producing this artifact.

## Required output

Copy `assets/pos-process-design.md`. Include process states, role controls, payment and cash controls, offline recovery, stock/accounting handoffs, exceptions, acceptance criteria, evidence, assumptions, and unknowns.

## Verification

- Opening-to-closing and refund paths are complete.
- Payment success, Odoo order state, stock effect, and accounting handoff are distinguished.
- Offline and reconnection cases have observable acceptance criteria.
- Odoo 18 Community support is explicit.

## Reference to load

Read `references/odoo-18-community.md` for the verified CE baseline and inspect target source when a detail affects implementation.

## Failure and escalation

Stop and mark unknowns when payment-provider behavior, fiscal requirements, edition capability, or recovery behavior is unverified. Escalate accounting policy and production changes to their owning workflows.
