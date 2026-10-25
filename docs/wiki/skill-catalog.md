# Skill catalog

Every skill, one row each. `make validate` fails when a directory under
`skills/` has no row here, so add the row in the same change as the skill.
Source of truth: each skill's `SKILL.md` frontmatter, `bundles/*.yaml`, and
the boundary documents [../PHASE-1-SKILL-BOUNDARIES.md](../PHASE-1-SKILL-BOUNDARIES.md),
[../PHASE-2-SKILL-BOUNDARIES.md](../PHASE-2-SKILL-BOUNDARIES.md),
[../PHASE-3-SKILL-BOUNDARIES.md](../PHASE-3-SKILL-BOUNDARIES.md).

Cells: "17–20 CE/EE" means Odoo 17.0, 18.0, 19.0 and 20.0, each in Community
and Enterprise. Every skill's output template is in its `assets/` folder.

## Phase 1: foundation workflows

| Skill | Primary outcome | Status | Risk | Cells | Bundles |
|---|---|---|---|---|---|
| `odoo-context-discovery` | Verified version, edition, repository, runtime, and risk context | stable | read-only | 17–20 CE/EE | all eight |
| `odoo-solution-design` | Standard-first decision: standard, configuration, OCA, low-code, custom, or external | stable | advisory | 17–20 CE/EE | accounting, design, dev, functional, platform |
| `odoo-addon-development` | Implemented addon change with security, tests, and docs | stable | controlled-write | 17–20 CE/EE | dev |
| `odoo-code-review` | Prioritized correctness and readiness findings | stable | read-only | 17–20 CE/EE | review |
| `odoo-security-audit` | Defensive findings on ACLs, rules, `sudo()`, routes, SQL, HTML | stable | read-only | 17–20 CE/EE | dev, live, review, upgrade |
| `odoo-testing` | Executable verification evidence | stable | controlled-write | 17–20 CE/EE | dev, review, upgrade |
| `odoo-oca-development` | Branch-specific OCA contribution readiness | stable | controlled-write | 17–20 CE/EE | upgrade |
| `odoo-version-upgrade` | Major-version migration plan and evidence | stable | destructive | 17–20 CE/EE | upgrade |

## Phase 2: domain and technical skills

| Skill | Primary outcome | Status | Risk | Cells | Bundles |
|---|---|---|---|---|---|
| `odoo-functional-sales` | CRM and order-to-cash process design | experimental | advisory | 17–20 CE/EE | functional |
| `odoo-functional-purchase` | Procure-to-pay process design | experimental | advisory | 17–20 CE/EE | functional |
| `odoo-functional-inventory` | Warehouse, route, and stock-flow design | experimental | advisory | 17–20 CE/EE | functional |
| `odoo-functional-accounting` | Accounting configuration, posting, reconciliation, closing | experimental | advisory | 17–20 CE/EE | accounting |
| `odoo-indonesia-accounting` | Assumption-bound Indonesian localization and tax analysis | experimental | advisory | 17–20 CE/EE | accounting |
| `odoo-integration-design` | External-system boundary, idempotency, and recovery contract | experimental | advisory | 17–20 CE/EE | platform |
| `odoo-reporting` | Report mechanism, data, access, and performance design | experimental | advisory | 17–20 CE/EE | platform |
| `odoo-functional-pos` | POS session, payment, offline, and stock design | experimental | advisory | 17–20 CE/EE | functional |
| `odoo-functional-manufacturing` | BoM-to-production process design | experimental | advisory | 17–20 CE/EE | functional |
| `odoo-deployment-operations` | Read-only-first deployment, backup, rollback runbook | experimental | read-only | 17–20 CE/EE | platform |
| `odoo-data-model-diagram` | Logical ORM diagram as DBML, with a converter script | experimental | read-only | 17–20 CE/EE | platform |
| `odoo-code-tracing` | Source-evidenced call chain and side-effect map | experimental | advisory | 18 CE, 19 CE, 20 CE/EE | review |
| `odoo-website-portal` | Website, portal, and public-route design | experimental | advisory | 17–20 CE/EE | platform |

## Phase 3: controlled live integration

| Skill | Primary outcome | Status | Risk | Cells | Bundles |
|---|---|---|---|---|---|
| `odoo-live-context` | Verified live instance, company, model, and access context | experimental | read-only | 17–20 CE/EE | live |
| `odoo-live-read` | Bounded read plan and evidence | experimental | read-only | 17–20 CE/EE | live |
| `odoo-live-mutation` | Approval-bound packet for one named capability | experimental | controlled-write | set by the shared contract, not frontmatter | live |

## Routing between neighbours

- Version, edition, or repository unknown: start with `odoo-context-discovery`.
- Any custom code or infrastructure proposal: `odoo-solution-design` first.
- Code change: `odoo-addon-development`. Proof: `odoo-testing`.
  Broad review: `odoo-code-review`. Security depth: `odoo-security-audit`.
  One concrete execution path: `odoo-code-tracing`.
- Sales and purchase own their documents; inventory owns stock moves and
  routes; accounting owns journal entries, posting, and reconciliation.
- Live metadata and access: `odoo-live-context`. Business records:
  `odoo-live-read`. Writes: only `odoo-live-mutation`, and only for a named
  capability the contract approves.
