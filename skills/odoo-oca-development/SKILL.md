---
name: odoo-oca-development
description: Use this skill when creating, porting, reviewing, or contributing an Odoo addon that follows Odoo Community Association practices, including repository and branch discovery, module layout, manifests, README fragments, licensing, pre-commit, pylint-odoo, migration scripts, changelog, commit messages, pull requests, and OpenUpgrade-related conventions.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients with access to the target OCA or OCA-style repository.
metadata:
  version: "1.0.0"
  author: OCloud
  status: stable
  risk: controlled-write
  odoo:
    versions: ["17.0", "18.0", "19.0"]
    editions: [community, enterprise]
  hermes:
    tags: [odoo, oca, community, contribution]
---

# Odoo OCA Development

## Purpose

Develop or contribute Odoo addons using the actual conventions of the target OCA repository and branch, while preserving reviewability, licensing, and upgradeability.

## Preconditions

- Confirm target Odoo version and repository branch.
- Read repository-specific contribution instructions and tooling.
- Verify whether the addon belongs in an existing OCA repository.
- Confirm license and dependency compatibility.

## Workflow

### 1. Discover repository rules

Inspect:

- root README and contribution guide;
- `.pre-commit-config.yaml`;
- lint and test configuration;
- copier or template metadata;
- existing modules on the same branch;
- maintainers and codeowners;
- repository-specific README fragment conventions.

Do not impose a generic OCA template when the target repository defines a newer or different pattern.

### 2. Confirm module placement and scope

- choose the correct functional repository;
- avoid duplicate modules;
- keep scope narrow and reusable;
- distinguish generic community value from client-specific behavior;
- avoid hard-coded company or country assumptions unless localization is the module's purpose.

### 3. Implement according to target branch

Follow the target branch for:

- manifest version and metadata;
- license;
- module layout;
- Python and XML style;
- security;
- tests;
- migration directories;
- README generation;
- translation files.

### 4. Run repository tooling

Use the exact configured tools. Typical checks may include pre-commit, Ruff or Flake8 variants, Pylint Odoo, XML checks, manifest checks, README generation, and Odoo tests. Do not invent a toolchain based on another OCA repository.

### 5. Prepare contribution history

- use focused commits;
- follow branch and module prefixes;
- separate migration or porting changes from features;
- document backward incompatibility;
- include tests and generated documentation;
- resolve lint by correcting code, not blanket disabling.

### 6. Review OCA-specific risks

- dependency on non-OCA proprietary modules;
- license incompatibility;
- duplicated standard or existing OCA functionality;
- client-specific fields or workflows;
- missing migration scripts;
- unstable external IDs;
- untranslated user-facing strings;
- undocumented configuration.

## Required output

Use `assets/contribution-report.md` and provide:

- target repository and branch;
- repository rules discovered;
- module scope and justification;
- files and tooling affected;
- license and dependency assessment;
- tests and commands;
- migration or porting notes;
- pull request readiness and blockers.

## Safety and provenance

OCA is not a substitute for verifying the target version and repository. OpenUpgrade migration examples are valuable evidence but must not be copied without understanding or license compliance.

## References to load

Read exactly one `references/odoo-{17,18,19}-{community,enterprise}.md` file after the target version and edition are confirmed.

- Read `references/oca-repository-checklist.md` before scaffolding or contributing.
- Read `references/openupgrade-boundary.md` when migration work is involved.
