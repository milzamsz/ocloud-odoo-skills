# Changelog

All notable changes to this repository will be documented here.

The format follows Keep a Changelog principles and the project uses semantic versioning.

## [Unreleased]

### Added

- Extended every version-claiming skill (23 of 24) to Odoo 20.0 Community and
  Enterprise as verified-experimental: a `20.0-enterprise` matrix cell backed by
  the licensed local archive (`odoo-20-ee-local-evidence`), a fingerprinted
  Enterprise fixture, an OpenUpgrade 20 snapshot source, per-skill
  `odoo-20-{community,enterprise}.md` references with source-verified facts
  (`odoo/orm` package and `models.Constraint`, `jsonrpc` routes, bearer JSON-2
  API, Hoot-only tests, `Interaction` public JavaScript, Enterprise module
  markers, absent `l10n_id_efaktur`), and 48 new outcome cases. OCA 20 beyond
  OpenUpgrade and `odoo-live-mutation` remain unclaimed.
- Served the fixture database from disposable Odoo 20 Community and
  Enterprise servers and exercised the live skills over the JSON-2 API with an
  `rpc`-scoped key: version and edition probes, `fields_get` metadata, bounded
  reads, record-rule scoping, 401 without a key, and DBML conversion of live
  metadata. Recorded in the live skills' Odoo 20 references that `ir.model` and
  `ir.model.fields` reads need the Access Rights group, `check_access` is
  private remotely, and legacy `read_group` kwargs are rejected.
- Ran the repository outcome evaluation for every version-claiming skill on
  both Odoo 20 cells (46 cases, fresh executor sessions, separate graders):
  46 of 46 pass, recorded in `docs/EVALUATION-SUMMARY-ODOO-20.md`; human review
  remains pending. Fixed defects the runs surfaced: the live-read and
  live-context 20 references named `/json/1/` for bounded reads, the accounting
  skill tied Enterprise evidence to Odoo 18 source, and two case wordings.
- Added the installable `domain-eval-20` fixture whose Odoo tests exercise one
  flow per skill domain (sales, purchase, inventory, accounting, Indonesian
  chart, POS, manufacturing, report rendering, portal, access control, metadata
  reads, automation, JSON-2 bearer API over HTTP) and executed it on disposable
  Odoo 20 Community and Enterprise databases, then neutralized and dropped them.
  Recorded the surfaced facts (`read_group` argument order, `MIT` rejected as a
  manifest license on update, JSON-2 served by the `rpc` addon, `upgrade_code`
  rewriter behavior) in every Odoo 20 reference with per-skill executed lines,
  and added 46 executable outcome cases.
- Added the installable `minimal-addon-20` fixture (`ir.access.csv`,
  `models.Constraint`) and executed it with its tests on disposable Odoo 20
  Community and Enterprise databases; recorded that `ir.model.access` is
  replaced by `ir.access` on 20 and that OWL is 3.0.0, in every Odoo 20
  reference, the security ACL reference, and four executable outcome cases.
- Added experimental `odoo-website-portal` (Odoo 17/18/19 Community and Enterprise)
  with a source-verified portal access pattern, website patterns, per-cell
  references naming the public JavaScript layer of each tree, a clean-room
  portal fixture, 8/8 triggers, and seven outcome cases.
- Added `references/restore-neutralization.md` to `odoo-deployment-operations`,
  `references/report-regression.md` to `odoo-reporting`, an OpenUpgrade retry
  discipline section to `odoo-version-upgrade`, and a verified Odoo 19 migration
  reference (Interaction layer, Hoot, RPC surface).
- Added a `code-trace-report.md` output template plus use-when, verification,
  and escalation sections to `odoo-code-tracing`, and placed it in the
  `odoo-review` bundle.
- Added closed evidence cells (`path:line`, `NOT FOUND`, `UNCERTAIN`,
  `AMBIGUOUS`) and a no-default version rule to `odoo-context-discovery`; a
  `_sudo` binding rule and attacker/entry-point/missing-control finding fields
  to `odoo-security-audit`.
- Added validator rules: description must start with "Use this skill when",
  `metadata.status`/`metadata.risk` enums, brace-expanded backtick reference
  paths must exist, packaged files never loaded by `SKILL.md` warn, secret
  literals in skill files fail, and repository paths that break single-skill
  installs warn. Covered by `tests/test_validator_rules.py`.
- Added `.claude-plugin/plugin.json` and `marketplace.json` so the checkout
  installs as a Claude Code plugin; documented the project-level install path.
- Registered `unclecatvn-agent-skills`, `atakhadiviom-odoo-skill`, and
  `19prince-claude-odoo-builder` as inspiration-only sources and recorded the
  four-repository review in `docs/THIRD-PARTY-COVERAGE.md`; no upstream text or
  scripts were copied.
- Added experimental `odoo-code-tracing` for evidence-bounded call-chain tracing across Odoo 18/19/20 Community, with version-specific references, synthetic outcome fixtures, and an upstream skills coverage review; 19/20 claims remain experimental and no upstream content was copied.

- Added experimental `odoo-data-model-diagram` with bounded source/live model
  evidence, logical DBML generation, drawDB parser verification, clean-room
  fixtures, six-cell version coverage, and no physical-schema or live-write claims.
  Its live workflow names an explicit `odoo-rust-mcp` metadata allowlist
  (`odoo_list_models`, `odoo_get_model_metadata`, `odoo_check_access` with
  `operation=read`) and an explicit denylist that excludes record reads, counts,
  generic execution, reports, workflow, cleanup, and mutation tools.
- Froze the four-repository mutation-alignment baseline, manifest hashes, existing
  owner changes, test gates, and exact supported/blocked starting posture.
- Added capability-local mutation references for CRM lead, quotation, vendor-bill
  draft, atomic allowed-field update, and bank suspense import plus a cross-repo
  capability contract validator and shared five-capability evaluation fixture.
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

- Corrected the Hermes tap identifier to `milzamsz/ocloud-odoo-skills` in the
  README and Hermes integration guide; refreshed `MANIFEST.md` counts (24
  skills, 24 trigger datasets, 146 outcome cases, Odoo 20 Community cell).
- Removed the contradiction between "read exactly one version reference" and
  an unconditional Odoo 18 Community read in eight skills; the 18 Community
  file is now described as the executed baseline. Wired the previously
  unreachable `odoo-{17,18,19}.md` notes into `odoo-addon-development` and
  `odoo-version-upgrade`; removed the unclaimed Odoo 16 placeholder and the
  stale `odoo-18-community.md` claim file from `odoo-live-mutation`.
- Named Hoot as the Odoo 18+ browser test runner in `odoo-testing` and the
  public JavaScript layer per version in `odoo-addon-development`.
- Rephrased repository fixture mentions inside skill references so single-skill
  installs no longer point at paths that are not shipped.
- Bumped `odoo-context-discovery`, `odoo-addon-development`,
  `odoo-security-audit`, `odoo-testing`, and `odoo-version-upgrade` to 1.1.0 and
  `odoo-code-tracing`, `odoo-deployment-operations`, and `odoo-reporting` to
  0.2.0 for the body changes above.
- Replaced the draft-update blocker with an atomic Odoo-side conditional update and recorded development/staging matrix evidence for all six Odoo 17/18/19 Community/Enterprise cells; production remains read-only.
- Bound final mutation execution to the signed `odoo_execute_capability`
  runtime envelope.
- Updated `odoo-live-mutation` to `0.2.0`, removed its unsupported Odoo 18
  Community metadata claim, required exact support-cell/schema/evidence/review
  gates, normalized receipts, and accounting-suspense classification.
- Expanded all Phase 1 and Phase 2 skills plus Phase 3 live context/read to
  Odoo 17/18/19 Community and Enterprise verified-experimental coverage.
  `odoo-live-mutation` remains blocked for every support cell pending evidence.
- Extended the tap manifest, README, and package manifest for experimental
  Phase 2 distribution while retaining the Phase 1 stable baseline.
- Documented a drift-confirmation procedure in the `odoo-data-model-diagram`
  evidence reference: positive-control checks before reporting a missing
  dependency, the `AbstractModel` registry trap, and pinning a deployed revision
  with independent field-presence and wording markers. Reference-only; no
  behaviour or output change.

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
