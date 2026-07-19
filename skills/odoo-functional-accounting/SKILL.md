---
name: odoo-functional-accounting
description: Use this skill when designing or explaining Odoo accounting processes for chart of accounts, journals, receivables, payables, generic taxes, posting, reconciliation, period close, multi-company, or multi-currency, including explicit journal impact. Do not use it for jurisdiction-specific Indonesian conclusions or code implementation.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients. Stable guidance targets Odoo 17.0, 18.0, or 19.0 Community or Enterprise; Enterprise features are advisory.
metadata:
  version: "0.1.0"
  author: OCloud
  status: experimental
  risk: advisory
  odoo:
    versions: ["17.0", "18.0", "19.0"]
    editions: [community, enterprise]
  hermes:
    tags: [odoo, accounting, reconciliation, closing]
---

# Odoo Functional Accounting

## Purpose

Produce an evidence-based accounting process design or runbook for Odoo 17, 18, or 19 Community or Enterprise without inventing accounts, balances, tax treatment, or posting behavior.

## Required inputs

- business event, actors, companies, currencies, and reporting need;
- installed accounting/localization modules and exact edition;
- chart, journals, fiscal positions, taxes, payment terms, and lock-date policy;
- posting and reconciliation responsibility;
- sample transactions and expected evidence.

Mark missing information **Assumed** or **Unknown**. Load `odoo-context-discovery` when version, edition, modules, or company scope is not confirmed.

## Workflow

1. Define scope by company, currency, ledger, period, actors, and materiality.
2. Map each business event from its operational document to any resulting journal entry. A quotation, order, receipt, delivery, invoice draft, or payment instruction is not itself a posted journal entry. State the exact posting trigger and whether posting is manual or automatic.
3. For every expected entry, identify debit account/category, credit account/category, amount basis, currency, tax assumptions, partner, analytic dimensions if applicable, and reversal/correction path. Never infer a production account code.
4. Explain debit and credit economically: assets and expenses normally increase by debit; liabilities, equity, and income normally increase by credit. Verify actual account types and configuration before applying that rule.
5. Define receivable/payable and bank/cash reconciliation: items matched, full or partial status, exchange difference, write-off approval, residual amount, and evidence proving completion. Posting records the entry; reconciliation links eligible journal items and does not replace posting.
6. Cover exceptions: refunds/credit notes, cancellation or reversal, partial payment, overpayment, foreign currency, tax rounding, lock dates, duplicate documents, and opening balances.
7. Separate company ledgers and configuration. State intercompany and consolidation needs without implying Community provides an unverified consolidation feature.
8. Produce period-close checks for completeness, cutoff, subledger-to-ledger reconciliation, tax review, bank reconciliation, aged balances, suspense/outstanding accounts, FX, lock dates, and sign-off.
9. Use `odoo-solution-design` before recommending custom code. Delegate implementation, OCA selection, tests, security, review, and upgrades to the corresponding Phase 1 skills.

## Decision and safety rules

- Prefer standard configuration before third-party or custom behavior.
- Treat live systems as read-only unless the user explicitly authorizes a precise mutation.
- Require least privilege and company isolation for posting, reversal, reconciliation, lock dates, and configuration.
- Do not provide jurisdiction-specific tax or statutory conclusions; hand Indonesian scope to `odoo-indonesia-accounting`.
- Enterprise capabilities require licensed Odoo 18 source or official evidence and remain advisory.
- Escalate unresolved account mapping, tax, cutoff, currency, or legal questions to a qualified accountant before implementation or posting.

## Required output

Use `assets/accounting-runbook.md`. Include confirmed context, assumptions, operational-to-ledger map, debit/credit effects, posting timing, reconciliation criteria, company/currency/tax boundaries, controls, close checklist, exceptions, acceptance evidence, and unresolved decisions.

## Verification

- Debits equal credits for every illustrative entry.
- Operational documents are not conflated with journal entries.
- Posting and reconciliation are separately defined.
- No account, tax, edition, or legal claim is invented.
- Multi-company cases name the owning company and configuration boundary.
- Human accounting review is recorded before stable or production use.

## References to load

Read exactly one `references/odoo-{17,18,19}-{community,enterprise}.md` file after the target version and edition are confirmed.

- Read `references/odoo-18.md` for the supported Community baseline and Enterprise boundary.
