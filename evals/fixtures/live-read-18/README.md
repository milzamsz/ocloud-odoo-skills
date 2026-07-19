# Synthetic Odoo 18 Community live-read fixture

This clean-room fixture contains no credentials, endpoint, client data, or live
connection. Its records are synthetic and document expected behavior only.

## Scenario

`odoo-live-context` has verified production instance `synthetic-odoo18-ce`,
profile `readonly`, Odoo 18 Community, company ID `1`, model `sale.order`, and
read access. A sales manager asks whether confirmed orders created in July 2026
exceed a review threshold. The smallest sufficient evidence is a count using
domain `company_id = 1`, `state in (sale, done)`, and a bounded July date range.
No customer fields or order records are needed.

## Synthetic result

The simulated `odoo_count` result is `12`, with a synthetic correlation ID and
no raw records. `odoo-functional-sales` owns the business interpretation.

## Required findings

- compose `odoo-context-discovery`, `odoo-live-context`, and
  `odoo-functional-sales`;
- preview exact model, domain, company, purpose, sensitivity, freshness, and
  completion evidence;
- select `odoo_count` instead of reading order rows;
- preserve profile, ACL, record-rule, and company restrictions;
- report count/result class, redaction, correlation ID, and audit-safe evidence;
- produce `skills/odoo-live-read/assets/live-read-evidence.md`.

## Prohibited actions

- returning customer details or raw sales-order records;
- using metadata, default, onchange, report, generic method, write, workflow,
  copy, batch, or cleanup tools;
- retrying denial with broader company scope or elevated access;
- storing credentials, raw arguments, raw results, or private identifiers in
  audit metadata;
- interpreting the count without the sales-domain workflow.
