---
name: odoo-context-discovery
description: Use this skill when an Odoo task requires discovering the exact version, edition, repository layout, addons paths, module dependencies, runtime, database environment, project instructions, OCA usage, or operational risk before analysis, implementation, review, testing, migration, or live-instance work.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients with access to the target repository or environment evidence.
metadata:
  version: "1.0.0"
  author: OCloud
  status: stable
  risk: read-only
  odoo:
    versions: ["17.0", "18.0", "19.0"]
    editions: [community, enterprise]
  hermes:
    tags: [odoo, discovery, repository, environment]
---

# Odoo Context Discovery

## Purpose

Establish a verified Odoo context before any material recommendation or change. Produce facts, evidence, unknowns, risks, and permitted next actions.

## Use when

- starting work in an unfamiliar Odoo repository;
- version or edition is uncertain;
- reviewing or upgrading an addon;
- selecting commands, tests, or references;
- connecting to an Odoo instance through a tool or MCP;
- a request mentions Odoo without enough environmental detail.

## Do not use when

- the task is a generic Python question unrelated to Odoo;
- a complete context summary already exists for the same repository revision and environment;
- the user only asks for a high-level explanation with no implementation or environment dependency.

## Safety

- Perform discovery read-only.
- Do not start containers, install modules, upgrade databases, or change configuration during discovery.
- Do not print secret values from environment files or configuration.
- Do not infer Enterprise from app names or accounting requirements alone.
- Do not treat a branch name as sufficient version proof when stronger evidence exists.

## Workflow

### 1. Find repository instructions

Inspect the nearest applicable instructions and project documents, including:

- repository-level agent guidance, readmes, and contribution guides;
- product, architecture, technical, and implementation documents;
- test, lint, deployment, and migration runbooks.

Record which documents control the task.

### 2. Identify repository and runtime layout

Look for:

- addon roots and aggregate repositories;
- Odoo core and Enterprise source paths;
- `odoo.conf`, Docker Compose, Dockerfiles, devcontainers, systemd units, or platform manifests;
- database and filestore configuration without revealing credentials;
- local, staging, production, or migration-copy environment markers.

### 3. Confirm Odoo version

Use this evidence order:

1. pinned image, dependency, or explicit configuration;
2. Odoo source release information or Git commit;
3. branch name;
4. addon manifest compatibility and code features;
5. user statement;
6. inference marked unresolved.

If evidence conflicts, report the conflict instead of choosing whichever version makes the next command convenient.

### 4. Confirm edition

Confirm Community or Enterprise using source availability, dependencies, deployment configuration, or explicit evidence. Record mixed Community plus Enterprise repositories when applicable.

### 5. Inventory target modules

For each relevant addon, capture:

- technical name;
- manifest version, license, category, and installability;
- dependencies;
- data files and loading order;
- Python, XML, JavaScript, report, security, controller, migration, and test areas;
- OCA or vendor origin when known.

### 6. Identify business and security context

Record whether the work affects:

- multi-company;
- multi-currency;
- accounting or taxes;
- stock valuation or logistics;
- portal, public, website, or eCommerce exposure;
- file attachments or personal data;
- scheduled jobs and integrations;
- posted or legally significant documents.

### 7. Identify development controls

Find the exact commands or scripts for:

- linting;
- tests;
- module installation and upgrade;
- database initialization or disposable copies;
- migration;
- backup and restore.

Do not invent commands when the repository already defines them.

### 8. Classify unresolved risk

Block or constrain the next step when version, edition, database target, production status, or destructive command scope remains unclear.

## Required output

Use the template in `assets/context-summary.yaml` and provide:

- confirmed facts and evidence paths;
- inferred or assumed items;
- unknowns;
- target modules;
- version and edition;
- runtime and environment;
- business and security flags;
- exact safe commands discovered;
- prohibited actions;
- recommended next skill or bundle.

## Verification

Before completing, confirm:

- every version and edition claim has evidence;
- no secrets are included;
- target module dependencies are listed;
- production and database mutation risks are explicit;
- unknowns are not disguised as facts.

## References to load

Read exactly one `references/odoo-{17,18,19}-{community,enterprise}.md` file after the target version and edition are confirmed.

- Read `references/evidence-priority.md` when version or edition evidence conflicts.
- Read `references/repository-markers.md` when repository structure is unfamiliar.
