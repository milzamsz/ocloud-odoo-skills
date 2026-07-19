# Odoo Reporting Design

## Outcome and scope
- Business decision and audience:
- Odoo version/edition:
- Evidence labels:
- Assumptions and unknowns:
- Explicitly prohibited actions:

## Mechanism decision
| Standard view/report | Configured | Third-party/OCA | Custom QWeb/export | External analytics | Decision/evidence |
|---|---|---|---|---|---|

## Data contract
| Metric/field | Source and grain | Filters/states | Date basis | Company/currency/unit | Owner |
|---|---|---|---|---|---|

## Interaction and rendering
- Parameters, filters, groups, sort, and drill-down:
- Format, localization, paper/page behavior:
- Delivery, attachment, cache, and invalidation:
- Empty, partial, and error behavior:

## Access and privacy
- Audience and least-privilege groups:
- ACLs, record rules, and allowed companies:
- Sensitive fields and output retention:
- Required denied/cross-company cases:

## Performance budget
- Expected rows/pages, frequency, and concurrency:
- Query, duration, memory, and output-size limits:
- Aggregation, batching, prefetch, and pagination:
- Timeout and degraded-mode behavior:

## Accounting controls, if applicable
- Operational documents versus journal entries:
- Debit/credit signs and posting states:
- Reconciliation, tax, rate-date, and rounding assumptions:

## Verification and rollout
- Synthetic fixture and expected totals:
- Rendering/localization checks:
- Security and multi-company test matrix:
- Performance evidence:
- Approval gate before live generation/delivery:
- Acceptance criteria:
- Risks and blockers:
