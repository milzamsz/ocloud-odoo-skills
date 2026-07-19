# Changelog

All notable changes to this repository will be documented here.

The format follows Keep a Changelog principles and the project uses semantic versioning.

## [Unreleased]

### Added

- Added a six-cell Odoo 17/18/19 Community/Enterprise support matrix,
  licensed-source-safe evidence registry, 121 exact version/edition skill
  references, six matrix fixtures, and 102 matrix outcome scenarios.
- Added repository validation that rejects unsupported skill metadata claims
  unless matrix, source, reference, fixture, and outcome evidence agree.
- Added a complete local Odoo 17 Community environment and verified core
  module/edition markers across all six development environments.
- Added Phase 3 controlled-live scaffolding: skill boundaries, cross-repo
  interface contract, risk classification, plugin-skill migration policy,
  private overlay guidance/template, and a foundation-only `odoo-live` bundle.
- Added experimental `odoo-live-context`, `odoo-live-read`, and
  `odoo-live-mutation` skills with synthetic fixtures, trigger datasets,
  outcome cases, and the completed live bundle.
- Hardened the sibling plugin/MCP capability path for cross-instance guard
  scoping, prefixed-tool auditing, multi-candidate duplicate conflicts,
  returned-record verification failures, approval evidence metadata, and
  crash-durable approval storage.
- Added ten experimental Odoo 18 Community domain skills for Sales, Purchase,
  Inventory, Accounting, Indonesian accounting, integration design, reporting,
  POS, Manufacturing, and deployment operations.
- Added Phase 2 skill boundaries, three domain bundles, output templates,
  Odoo 18 references, clean-room fixtures, trigger datasets, and outcome cases.
- Registered Odoo 18 functional application and Indonesian localization source
  references without redistributing Odoo or Enterprise code.
- Recorded automated Phase 2 evaluation evidence and the remaining human,
  regression, and clean-profile gates for a future `v1.1.0` promotion.

### Changed

- Expanded all Phase 1 and Phase 2 skills plus Phase 3 live context/read to
  Odoo 17/18/19 Community and Enterprise verified-experimental coverage.
  `odoo-live-mutation` remains explicitly Odoo 18 Community only.
- Extended the tap manifest, README, and package manifest for experimental
  Phase 2 distribution while retaining the Phase 1 stable baseline.

### Fixed

- Phase 3 review: aligned `create_crm_lead_draft.v1` skill/fixture field names
  with the closed runtime schema; clarified metadata vs business-read ownership
  in risk classification; narrowed plugin-local CRM routing notes.
- Corrected Hermes tap identifiers in the experimental 0.5.0 release notes to
  `milzamsz/ocloud-odoo-skills`.
- Phase 2 audit: aligned boundary artifact names, corrected
  `odoo-deployment-operations` risk metadata to `read-only`, and grounded
  Sales/Purchase/Inventory/POS/Manufacturing/Indonesia references in verified
  CE bridge modules and packaging boundaries without claiming statutory or
  Enterprise support.

## [1.0.0] - 2026-07-20

### Changed

- Promoted all eight Phase 1 skills to stable with an Odoo 18 Community
  evidence baseline; Odoo 17/19 and Enterprise remain advisory.
- Strengthened context evidence, OCA contribution, and 17 → 18 upgrade
  reference contracts from release-review findings.

### Added

- Named maintainer approval and stable release evidence.
- Three independent clean-session regression reviews across all eight skills.

## [0.5.1] - 2026-07-19

### Fixed

- Rephrased context-discovery repository-guidance examples so Hermes' community
  skill scanner does not misclassify read-only instruction discovery as
  persistence behavior.

## [0.5.0] - 2026-07-19

### Added

- Root MIT License covering original OCloud-authored repository content.
- Comprehensive development documentation.
- Phase 1 skill scaffolds.
- Hermes bundle definitions.
- Source governance and version matrix.
- Structural validation and evaluation scaffolding.
- Frozen output templates and documented non-overlapping boundaries for all
  eight Phase 1 skills.
- Community-like and Enterprise-dependent clean-room metadata fixtures.
- OCloud-authored installable Odoo 18 Community minimal-addon fixture with a
  manifest, model, ACL, list/form views, and transactional Odoo tests.
- Addon-development and testing outcome cases with explicit runtime evidence
  requirements and prohibited shortcuts.

### Changed

- Deepened `odoo-context-discovery` with evidence rules observed from the
  read-only `erp-ocloud` and `erp-ca` layouts, an ambiguous near-miss fixture,
  8 positive/8 negative triggers, and stricter outcome evidence.
- Deepened `odoo-solution-design` with mandatory
  Standard → Configured → Third-party → Low-code → Custom → External
  evaluation, OCA lookup gates, multi-company/accounting fields, a full vendor
  bill email fixture, 8 positive/8 negative triggers, and stricter outcome
  criteria.
- Registered official Odoo vendor-bill documentation and the OCA organization
  as discovery sources; no third-party or Enterprise code was copied.
- Deepened `odoo-addon-development` and `odoo-testing` references from verified
  Odoo 18 Community ORM, view, security, and test source paths; retained only
  verified material Odoo 17/19 deltas.
- Expanded both development/testing trigger datasets to 8 positive and 8
  negative cases, including adjacent-skill and generic-development near misses.
- Registered the official Odoo 18 Community source reference; source paths are
  cited in prose without redistributing Odoo source.
- Deepened `odoo-code-review` and `odoo-security-audit` references and report
  assets for evidence quality, ACL and record-rule composition, company
  isolation, scoped elevation, controller auth/CSRF, parameterized SQL,
  HTML/XSS, and batched ORM review.
- Added a safe, non-installable static defect corpus covering broad ACLs,
  company leakage, `sudo()`, controller authorization/CSRF, unsafe SQL,
  unsafe HTML, and N+1 behavior; expanded both review outcome cases and
  prohibited actions.
- Expanded both review/security trigger datasets to 8 positive and 8 negative
  prompts, including generic Python, Flask, Django, and FastAPI near misses.
- Grounded Odoo 18 controller, company-context, SQL composition, and HTML
  sanitization notes in the read-only Community source workspace; no source
  code was copied.
- Deepened `odoo-oca-development` with target-branch evidence rules, observed
  19.0 conventions, an explicit incomplete-local-OCA-18 gap, OpenUpgrade
  boundaries, 8 positive/8 negative triggers, and an outcome case.
- Deepened `odoo-version-upgrade` with separated code/schema/data/XML-ID/config
  planning, reconciliation evidence and tolerances, 8 positive/8 negative
  triggers, and a clean-room 17→18 source/target addon fixture covering a field
  rename and XML-ID change.
- Registered OCA maintainer-tools and branch-specific server-tools 19.0 and
  account-financial-tools 18.0 evidence. No live database mutation or
  third-party/Enterprise source redistribution was performed.
- Enforced source registry governance, 8/8 trigger minimums, and outcome safety
  contracts in repository validation; added a repeatable manual Claude/Codex
  evaluation protocol.
- Hardened package checks so the tap manifest and all four bundles must resolve
  exactly to the eight packaged skills.
- Added experimental 0.5.0 release notes and clean-profile Hermes smoke-test
  gates.

## [0.1.0] - Planned

- Initial experimental release with `odoo-context-discovery` and repository validation.
