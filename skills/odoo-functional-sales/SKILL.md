---
name: odoo-functional-sales
description: Use this skill when designing or validating an Odoo 17, 18, or 19 Community or Enterprise sales and CRM order-to-cash process, including leads, opportunities, quotations, sales orders, delivery handoff, invoicing policy, pricelists, sales teams, exceptions, and completion evidence. Do not use it for inventory-only execution, accounting policy, or addon implementation.
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
    tags: [odoo, sales, crm, functional]
---

# Odoo Functional Sales

## Purpose

Produce an evidence-backed Odoo 17, 18, or 19 Community or Enterprise order-to-cash design and configuration runbook from lead or quotation through sales order, delivery handoff, and invoice readiness.

## Use when

- mapping CRM qualification, quotations, sales orders, pricelists, sales teams, or invoice policy;
- defining sales actors, document states, exceptions, permissions, and acceptance criteria;
- validating whether a proposed order-to-cash process fits Odoo 17, 18, or 19 Community or Enterprise.

## Do not use when

- the primary outcome is warehouse routing or picking execution (`odoo-functional-inventory`);
- the primary outcome is journal design, posting, reconciliation, or tax advice;
- an approved design only needs implementation, testing, review, security audit, OCA contribution, or upgrade work.

## Required inputs and composition

1. Require `odoo-context-discovery` when version, edition, repository layout, modules, or company context is unknown.
2. Require `odoo-solution-design` before recommending custom code or a third-party component.
3. Delegate code to `odoo-addon-development`, tests to `odoo-testing`, security analysis to `odoo-security-audit`, review to `odoo-code-review`, OCA work to `odoo-oca-development`, and major-version work to `odoo-version-upgrade`.
4. Obtain actors, products/services, companies, currencies, taxes, pricing rules, fulfillment policy, invoice policy, exceptions, volume, and success criteria.

## Workflow

1. Confirm Odoo 17.0, 18.0, or 19.0 Community or Enterprise and identify installed `crm`, `sale`, and `sale_management` capabilities from evidence.
2. Map actors and operational documents: lead/opportunity when used, quotation, sales order, delivery handoff, and customer invoice readiness.
3. Define state transitions, ownership, approvals, cancellation, returns, partial delivery, backorder, and invoice exceptions.
4. Specify master data and configuration: customers, products, units, pricelists, payment terms, fiscal assumptions, sales teams, warehouses, and invoicing policy.
5. Mark boundaries: Inventory owns route and picking detail; Accounting owns journal entries, posting, tax, payment, and reconciliation.
6. Evaluate Standard then Configured behavior. Invoke `odoo-solution-design` for Third-party, Low-code, Custom, or External options.
7. Define permissions, multi-company separation, audit evidence, acceptance criteria, unknowns, and handoffs.

## Safety and decision rules

- Treat live systems as read-only unless the user explicitly authorizes the exact mutation.
- Do not claim behavior from another edition; use only the confirmed target cell and installed-module evidence.
- Do not treat quotation, sales order, delivery, or invoice as the same document.
- Do not invent tax, account, fiscal-position, or legal conclusions.
- Label facts as Confirmed, Inferred, Assumed, or Unknown and cite source paths.

## Required output

Use `assets/sales-process-runbook.md`. Include context, evidence, actors, document/state map, configuration decisions, exception paths, inventory/accounting handoffs, permissions/company scope, acceptance criteria, risks, unknowns, and delegated next actions.

## Verification

- Version and edition are confirmed independently.
- Quotation, order, fulfillment handoff, and invoice readiness are distinct.
- Pricelist, invoice policy, partial/cancel/return paths, permissions, and multi-company behavior are addressed.
- No implementation or accounting policy is silently designed.
- Every completion claim has evidence or a testable acceptance criterion.

## Reference to load

Read exactly one `references/odoo-{17,18,19}-{community,enterprise}.md` file after the target version and edition are confirmed.

## Failure and escalation

Stop and report a blocker when edition, installed modules, company rules, pricing, fulfillment, or invoice policy materially changes the design. Escalate accounting, tax, legal, security, and customization decisions to the owning skill or human reviewer.
