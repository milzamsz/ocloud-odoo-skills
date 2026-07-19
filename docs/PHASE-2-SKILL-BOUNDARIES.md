# Phase 2 Skill Boundaries and Output Contracts

Phase 2 skills produce domain decision and runbook artifacts. They compose the
Phase 1 workflows in `PHASE-1-SKILL-BOUNDARIES.md`; they do not replace
discovery, solution selection, implementation, testing, review, security, OCA,
or upgrade procedures.

| Skill | Primary outcome | Required artifact | Boundary |
|---|---|---|---|
| `odoo-functional-sales` | Order-to-cash process design | `assets/sales-process-runbook.md` | Stops before inventory configuration, accounting policy, or implementation. |
| `odoo-functional-purchase` | Procure-to-pay process design | `assets/purchase-process-runbook.md` | Stops before AP accounting policy or implementation. |
| `odoo-functional-inventory` | Warehouse, route, and stock-flow design | `assets/inventory-process-runbook.md` | Flags valuation impact but delegates accounting and manufacturing depth. |
| `odoo-functional-accounting` | Accounting configuration and control design | `assets/accounting-runbook.md` | Does not provide jurisdiction-specific legal conclusions. |
| `odoo-indonesia-accounting` | Assumption-bound Indonesian localization analysis | `assets/indonesia-accounting-assessment.md` | Requires current regulatory validation; never asserts legal certainty. |
| `odoo-integration-design` | External-system boundary and reliability contract | `assets/integration-design.md` | Stops before addon implementation and deep security review. |
| `odoo-reporting` | Report mechanism, data, access, and performance design | `assets/reporting-design.md` | Does not become generic frontend or analytics implementation. |
| `odoo-functional-pos` | POS session, payment, offline, and stock process design | `assets/pos-process-design.md` | Delegates accounting policy and implementation. |
| `odoo-functional-manufacturing` | BoM-to-production process design | `assets/manufacturing-process-design.md` | Delegates warehouse route depth to inventory. |
| `odoo-deployment-operations` | Read-only-first deployment and recovery runbook | `assets/operations-runbook.md` | Does not authorize production mutation or perform major-version migration. |

## Composition rules

- Load `odoo-context-discovery` when version, edition, repository, or runtime is
  unknown.
- Load `odoo-solution-design` before recommending custom code or external
  infrastructure.
- Delegate code changes to `odoo-addon-development`, executable evidence to
  `odoo-testing`, defensive assessment to `odoo-security-audit` and
  `odoo-code-review`, OCA work to `odoo-oca-development`, and major-version
  changes to `odoo-version-upgrade`.
- State Odoo version and edition, evidence labels, assumptions, unknowns,
  safety constraints, and completion evidence in every artifact.
- Treat Odoo 18 Community as the stable evidence baseline. Enterprise and
  other major versions remain advisory until separately verified.

## Cross-domain handoffs

Sales and purchase own their operational documents; inventory owns stock
movements and routes; accounting owns journal entries, posting, and
reconciliation. POS and manufacturing describe their domain processes and
hand stock or financial depth to the corresponding domain skill. Integration
and reporting own technical decision artifacts, not business policy.
