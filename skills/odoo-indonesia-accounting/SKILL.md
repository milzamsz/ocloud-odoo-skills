---
name: odoo-indonesia-accounting
description: Use this skill when analyzing or designing Odoo 17, 18, or 19 Community or Enterprise accounting for Indonesian localization, PSAK-oriented reporting assumptions, Indonesian tax configuration, withholding patterns, localization gaps, and multi-company controls. Require current authoritative validation; never present the result as legal or tax certainty.
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
    tags: [odoo, indonesia, accounting, localization]
---

# Odoo Indonesia Accounting

## Purpose

Produce an assumption-bound Indonesian accounting localization assessment and implementation runbook. Identify what Odoo 17, 18, or 19 Community or Enterprise provides, what configuration or extension may be needed, and which conclusions require a qualified Indonesian accountant or tax adviser.

## Required inputs

- legal entities, NPWP/tax status, currencies, transaction dates, and materiality;
- Odoo version, edition, installed `l10n_id`-related modules, and localization data;
- approved chart/account mapping, taxes, withholding scenarios, fiscal documents, and reporting obligations;
- effective dates and links or copies of current authoritative requirements;
- expected journal, reconciliation, filing/export, and audit evidence.

Label every claim **Confirmed**, **Inferred**, **Assumed**, or **Unknown**. Load `odoo-context-discovery` when context is incomplete, and `odoo-functional-accounting` for generic ledger and closing analysis.

## Workflow

1. Create an assumptions register with entity, transaction, tax type, counterparty, effective date, currency, source, owner, and expiry/revalidation date.
2. Inspect the exact Odoo 17, 18, or 19 Community or Enterprise localization modules and installed data. Treat module presence as evidence of packaged configuration, not proof of statutory completeness.
3. Map operational documents separately from journal entries. For each invoice, bill, payment, withholding evidence, adjustment, or filing/export, state the posting trigger, debit, credit, tax base, currency, partner, and reconciliation behavior.
4. Explain debit and credit effects. For example, a withholding pattern may split settlement between cash/bank and a withholding receivable or payable, but direction and accounts depend on the taxpayer's role and approved policy. Never invent account codes or rates.
5. Define posting versus reconciliation. Posting creates ledger impact; reconciliation matches receivable/payable, liquidity, or withholding-related items. State residual, partial, exchange-difference, and correction handling.
6. Build a localization gap matrix: Standard, Configured, reviewed Third-party/OCA, Custom, or External. Use `odoo-solution-design` before recommending custom code and `odoo-oca-development` before selecting an OCA module.
7. Cover company isolation, branch/entity assumptions, currencies, fiscal positions, tax repartition, sequences, access, lock dates, amendments, and audit trail.
8. Separate PSAK-oriented management/reporting mapping from a claim of PSAK compliance. Record recognition, measurement, presentation, and disclosure questions for professional review.
9. Define acceptance evidence using clean-room scenarios and a disposable database copy. Delegate implementation, testing, security, review, and upgrade work to Phase 1 skills.

## Decision and safety rules

- Do not claim legal, tax, filing, or PSAK certainty. Regulations, rates, forms, and electronic systems can change.
- Require an effective date and authoritative current source for every regulatory conclusion.
- Do not treat `l10n_id` installation, Enterprise access, or a third-party module as compliance certification.
- Enterprise behavior requires official evidence or licensed source inspection and remains advisory.
- Treat live Odoo as read-only unless an exact mutation is explicitly authorized.
- Stop before production configuration, posting, filing, or migration when entity status, rate, account mapping, effective date, or professional approval is unresolved.

## Required output

Use `assets/indonesia-accounting-assessment.md`. Include the assumptions register, localization inventory, requirement-to-feature gap matrix, operational-to-journal map, debit/credit and posting/reconciliation behavior, controls, evidence, and professional-review gates.

## Verification

- Odoo 17, 18, or 19 Community or Enterprise facts are separated from Enterprise advisory notes.
- Every regulatory statement has jurisdiction, effective date, source, and confidence.
- Illustrative entries balance and avoid invented accounts or rates.
- Operational documents, journal entries, posting, and reconciliation remain distinct.
- Multi-company ownership and configuration boundaries are explicit.
- Indonesian accounting/tax human review is required before stable or production use.

## References to load

Read exactly one `references/odoo-{17,18,19}-{community,enterprise}.md` file after the target version and edition are confirmed.

- Read `references/odoo-18.md` for the clean-room Community localization baseline.
