---
name: odoo-deployment-operations
description: Use this skill when producing a read-only-first Odoo deployment, backup, restore, release, monitoring, rollback, or incident-triage runbook for self-hosted operations. Do not use it to authorize production mutation, perform a major-version migration, design business processes, or replace hosting-specific documentation.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients. Verified for Odoo 18.0 Community.
metadata:
  version: "0.1.0"
  author: OCloud
  status: experimental
  risk: read-only
  odoo:
    versions: ["18.0"]
    editions: [community]
  hermes:
    tags: [odoo, deployment, backup, operations]
---

# Odoo Deployment Operations

## Purpose

Produce a recoverable Odoo 18 Community operations runbook with evidence, explicit decision gates, and no implicit authorization to change a live system.

## Preconditions and composition

- Confirm environment, hosting model, Odoo build, configuration sources, addons, database, filestore, proxy, workers, jobs, integrations, owners, maintenance window, and recovery objectives.
- Load `odoo-context-discovery` whenever any of that context is unknown.
- Load `odoo-solution-design` before proposing new infrastructure.
- Delegate code, tests, reviews, security audits, OCA work, and major-version changes to their corresponding Phase 1 skills. Use `odoo-version-upgrade` for a major-version migration.

## Authorization boundary

Read-only inspection is the default. Before any mutation, obtain authorization that names the exact target environment, exact command or structured action, intended changes, expected impact, maintenance window, backup evidence, verification, rollback trigger, and rollback action. General permission such as “deploy it” is insufficient when these details are unresolved. Never expand authorization to adjacent actions.

## Workflow

1. Build an evidence-backed topology and dependency summary without exposing secret values.
2. Classify the request: deployment review, backup/restore planning, same-version release, monitoring triage, incident triage, or major-version upgrade handoff.
3. Define immutable release inputs and compatibility checks for Odoo, addons, dependencies, configuration, database, and filestore.
4. Define a backup set containing the database and matching filestore plus required configuration and release metadata. Specify retention, access control, integrity evidence, and restore testing on an isolated target.
5. Define preflight, maintenance, release, health, functional smoke, data-integrity, monitoring, and go/no-go gates.
6. Define rollback triggers, decision owner, previous release inputs, database/filestore consistency strategy, and post-rollback verification.
7. For incidents, preserve evidence, identify blast radius, prefer reversible containment, and separate diagnosis from authorized remediation.

## Safety rules

- Never test restore or upgrade on the only database copy.
- Never claim a backup is usable without restore evidence.
- Keep database and filestore from the same recovery point.
- Do not print credentials, tokens, private keys, session data, or unredacted configuration.
- Direct SQL, destructive cleanup, module upgrades, restarts, restores, and deployments are mutations and require exact authorization.
- A rollback is also a mutation and requires its approved trigger and procedure.

## Required output

Copy `assets/operations-runbook.md`. Record topology, evidence, authorization state, backup/restore proof, ordered gates, monitoring, exact proposed mutations, verification, rollback, owners, assumptions, unknowns, and completion status.

## Verification

- Read-only observations are separated from proposed or authorized actions.
- The database and matching filestore are covered and an isolated restore test is defined.
- Every mutation has an exact authorization gate and observable verification.
- Rollback is executable in principle and preserves database/filestore consistency.
- Odoo 18 Community support and hosting assumptions are explicit.

## Reference to load

Read `references/odoo-18-community.md` after confirming the target. Hosting-specific instructions remain authoritative.

## Failure and escalation

Stop before mutation when identity, target, authorization, backup evidence, rollback, or owner is missing. Preserve diagnostics and escalate suspected compromise, data loss, accounting inconsistency, or unavailable recovery copies.
