---
name: odoo-version-upgrade
description: Use this skill when planning, analyzing, implementing, or validating an Odoo major-version upgrade or addon port, including source and target inventory, API and XML changes, module coverage, schema and data migration, OpenUpgrade, Enterprise dependencies, configuration changes, reconciliation, testing, cutover, rollback, and separation of compatibility work from feature development.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients with source and target code plus a disposable migration environment.
metadata:
  version: "1.0.0"
  author: OCloud
  status: stable
  risk: destructive
  odoo:
    versions: ["18.0"]
    editions: [community]
  hermes:
    tags: [odoo, upgrade, migration, openupgrade]
---

# Odoo Version Upgrade

## Purpose

Produce and execute a controlled, evidence-based Odoo upgrade plan that preserves business data, security, accounting integrity, and rollback capability.

## Mandatory safety

- Never migrate the only database copy.
- Verify backup and filestore availability before migration execution.
- Use a disposable copy for analysis and repeated trials.
- Keep source and target environments reproducible.
- Do not combine migration compatibility with unrelated feature work.
- Do not redistribute Odoo Enterprise source or proprietary migration content.
- Require explicit approval before any state-changing migration command.

## Preconditions

- Confirm source and target versions and editions.
- Inventory standard, Enterprise, OCA, vendor, and custom modules.
- Identify database size, filestore, integrations, scheduled jobs, and critical business periods.
- Define accepted downtime, data freeze, and rollback objectives.

## Workflow

### 1. Establish migration scope

Document:

- source and target versions;
- hosting and deployment model;
- module inventory and ownership;
- database and filestore size;
- integrations and external IDs;
- critical business processes;
- required historical data;
- regulatory and audit requirements.

### 2. Classify modules

Classify each module as:

- Odoo Standard;
- Enterprise;
- OCA;
- vendor third-party;
- OCloud custom;
- obsolete or replaced.

Record source availability, target compatibility, migration coverage, and replacement decision.

### 3. Analyze code compatibility

Inspect target-version changes affecting:

- ORM methods and decorators;
- fields and model names;
- view XML and modifiers;
- assets, JavaScript, and OWL;
- controllers and external APIs;
- reports;
- scheduled jobs;
- security behavior;
- manifest and dependencies.

### 4. Analyze schema and data

Identify:

- renamed or removed models and fields;
- changed field type or semantics;
- constraints and indexes;
- XML ID changes;
- property, company-dependent, translation, and attachment data;
- accounting, stock valuation, tax, and reconciliation changes;
- orphan or inconsistent data that must be repaired before migration.

### 5. Select migration path

Evaluate:

- official upgrade service where applicable;
- OpenUpgrade coverage;
- custom migration scripts;
- replacement or archival of unsupported modules;
- staged multi-version migration when required.

State the reason and limitations of the selected path.

### 6. Build repeatable migration environment

- pin source and target code;
- record dependencies;
- restore database and filestore copy;
- disable outbound integrations and email;
- neutralize scheduled jobs as required;
- capture commands and logs;
- make repeated runs disposable.

### 7. Implement migration scripts

Separate:

- pre-migration cleanup and renames;
- schema changes;
- data transformation;
- post-migration recomputation and repair;
- module-specific verification.

Scripts must be idempotent where the framework expects repeated trials and must fail loudly on violated assumptions.

### 8. Validate technically

Check:

- migration logs and unresolved errors;
- installed module state;
- database constraints;
- registry startup;
- views and assets;
- scheduled jobs;
- permissions;
- integrations;
- performance.

### 9. Reconcile business data

At minimum, where relevant:

- record counts and master data;
- open sales and purchase documents;
- inventory quantities and valuation;
- journal entries, trial balance, receivables, payables, taxes, and bank reconciliation;
- fixed assets and deferred balances;
- currencies and rates;
- attachments and reports.

### 10. Rehearse cutover and rollback

Define:

- data freeze;
- final backup;
- migration sequence;
- validation ownership;
- go/no-go criteria;
- rollback trigger and procedure;
- DNS, integration, and user communication;
- post-go-live monitoring.

## Required output

Use `assets/upgrade-plan.md` and include:

- executive summary;
- source/target inventory;
- module coverage matrix;
- code and data change analysis;
- selected migration path;
- migration script plan;
- technical and business reconciliation plan;
- rehearsal results;
- cutover and rollback;
- risks, blockers, and owners.

## Completion rule

A database that starts is not necessarily a successful migration. Completion requires functional and financial reconciliation against agreed evidence.

## References to load

- Read `references/openupgrade-workflow.md` when OpenUpgrade is selected.
- Read `references/reconciliation.md` for accounting or inventory databases.
- Read matching source and target version references before code changes.
