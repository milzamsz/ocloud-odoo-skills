---
name: odoo-addon-development
description: Use this skill when implementing or modifying an Odoo addon, including models, fields, computed behavior, constraints, views, actions, security, controllers, reports, assets, scheduled jobs, data files, migrations, tests, documentation, installation, or upgrade verification after the solution scope is understood.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients with repository and development environment access. Version-sensitive implementation requires confirmed Odoo context.
metadata:
  version: "1.0.0"
  author: OCloud
  status: stable
  risk: controlled-write
  odoo:
    versions: ["17.0", "18.0", "19.0"]
    editions: [community, enterprise]
  hermes:
    tags: [odoo, addon, development, python, xml]
---

# Odoo Addon Development

## Purpose

Implement the smallest approved Odoo change as an upgradeable addon with explicit security, tests, documentation, and executable verification.

## Preconditions

- Confirm Odoo version and edition with `odoo-context-discovery`.
- Read repository instructions and the approved solution or acceptance criteria.
- Identify the target addon, dependencies, test command, and safe database environment.
- Block unresolved product, security, accounting, or migration decisions.

## Use when

- creating a new addon;
- extending an existing model or view;
- adding business logic, controller, report, scheduled job, or integration adapter;
- fixing an Odoo-specific functional defect;
- implementing an approved upgrade-compatible change.

## Do not use when

- the requirement still needs solution selection;
- the primary task is audit or review only;
- the only available environment is production;
- the task requires modifying Odoo core without an approved exceptional decision.

## Safety

- Do not modify Odoo core by default.
- Do not run installation or upgrade on the only database copy.
- Do not bypass security with broad ACLs or blanket `sudo()`.
- Do not expose new public methods or controllers without authorization design.
- Do not use direct SQL unless ORM is inadequate and the need is documented, parameterized, tested, and transaction-aware.
- Keep compatibility changes separate from unrelated feature work.

## Workflow

### 1. Inspect before editing

Read:

- manifest and dependencies;
- related models and inherited methods;
- existing views and XML IDs;
- security files and record rules;
- tests and migration scripts;
- adjacent modules that already solve part of the requirement.

### 2. Define the change contract

State:

- user-visible behavior;
- model and state changes;
- permissions;
- accounting, stock, tax, or integration effects;
- migration needs;
- acceptance tests;
- explicit non-goals.

### 3. Choose extension strategy

Prefer documented inheritance and extension points. Avoid copying whole standard views or methods when a narrow extension works. Use stable XML selectors and preserve standard state transitions.

### 4. Implement the data model

Review:

- field type and required behavior;
- compute dependencies, storage, inverse, and search behavior;
- defaults and company-dependent behavior;
- SQL and Python constraints;
- related field access implications;
- deletion and referential behavior;
- indexing justified by real query patterns.

### 5. Implement business logic

- support recordsets correctly;
- use batch operations;
- avoid queries inside loops;
- validate authorization and state before mutation;
- make scheduled and integration work idempotent;
- preserve transaction semantics;
- provide actionable errors without exposing secrets.

### 6. Implement UI and data

- inherit existing views narrowly;
- verify version-correct modifiers and view architecture;
- control fields and actions by groups and state;
- order manifest data correctly;
- use stable external IDs;
- avoid `noupdate` unless lifecycle behavior is understood;
- include translations or translatable strings where required.

### 7. Implement security

Define and test:

- groups;
- ACLs;
- record rules;
- company isolation;
- field groups;
- controller auth and CSRF;
- portal or public exposure;
- `sudo()` scope.

### 8. Add tests

Load `odoo-testing` and implement tests appropriate to the change. Include negative access and state cases, not merely the happy path.

### 9. Add migration behavior

When fields, models, XML IDs, data semantics, or dependencies change, define installation, upgrade, existing data, uninstall, and rollback implications.

### 10. Verify

Use the repository's exact commands. At minimum, where available:

- lint and static checks;
- install on a clean disposable database;
- upgrade from a representative prior state;
- focused tests;
- access and multi-company tests;
- functional scenario;
- log review;
- documentation review.

## Required output

Use `assets/implementation-report.md` and provide:

- implementation summary;
- files changed;
- component classification;
- version and edition;
- security and accounting impact;
- tests added;
- commands executed and results;
- migration and rollback notes;
- unresolved risks.

## Completion rule

Code creation is not completion. Completion requires executable evidence aligned to acceptance criteria.

## References to load

Read exactly one `references/odoo-{17,18,19}-{community,enterprise}.md` file after the target version and edition are confirmed.

- Read `references/model-and-orm.md` for model-heavy changes.
- Read `references/views-and-assets.md` for XML, OWL, or asset changes.
- Read `references/controllers-and-integrations.md` for external interfaces.
- Read the matching version reference after context discovery.
