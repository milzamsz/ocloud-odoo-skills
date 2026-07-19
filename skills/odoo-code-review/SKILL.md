---
name: odoo-code-review
description: Use this skill when reviewing an Odoo addon, repository, patch, or pull request for functional correctness, ORM behavior, manifest dependencies, XML inheritance, security, multi-company behavior, performance, upgradeability, maintainability, missing tests, documentation, or production readiness. Do not use it as the primary workflow for implementing a new feature.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients with read access to the target repository.
metadata:
  version: "0.1.0"
  author: OCloud
  status: experimental
  risk: read-only
  odoo:
    versions: ["17.0", "18.0", "19.0"]
    editions: [community, enterprise]
  hermes:
    tags: [odoo, review, quality, production-readiness]
---

# Odoo Code Review

## Purpose

Produce an evidence-based, prioritized review that separates release blockers, functional bugs, security risks, performance issues, upgrade risks, refactoring, and missing verification.

## Preconditions

- Confirm version, edition, repository instructions, and target diff.
- Understand the approved requirement or state that it is unavailable.
- Keep the review read-only unless the user explicitly asks for fixes.

## Workflow

### 1. Establish review scope

Identify:

- files and modules changed;
- intended behavior;
- affected business processes;
- version and edition;
- deployment and migration assumptions;
- whether accounting, stock, portal, website, or multi-company behavior is affected.

### 2. Review manifest and dependencies

Check:

- version and license;
- dependency completeness and unnecessary dependencies;
- file loading order;
- assets;
- installability and application flags;
- external Python dependencies;
- hooks and migrations.

### 3. Review ORM and business logic

Check:

- inheritance strategy;
- recordset correctness;
- compute dependencies, store, inverse, and search;
- constraints and state validation;
- create/write/unlink semantics;
- batch behavior and N+1 queries;
- transaction and idempotency;
- company and currency behavior;
- error handling.

### 4. Review views, data, reports, and assets

Check:

- valid XML and stable inheritance;
- version-correct view syntax;
- groups and state visibility;
- external ID stability;
- `noupdate` lifecycle;
- report correctness and escaping;
- OWL component lifecycle and asset registration where relevant.

### 5. Review security

Load `odoo-security-audit` for material security scope. At minimum inspect ACLs, record rules, public methods, `sudo()`, controllers, SQL, HTML, attachments, and company isolation.

### 6. Review upgradeability

Check:

- core modifications;
- copied standard code;
- brittle selectors;
- stored field semantic changes;
- model or field renames;
- XML ID changes;
- migration scripts;
- installation and uninstall behavior.

### 7. Review tests and evidence

Check whether tests prove:

- intended behavior;
- negative permissions;
- state transitions;
- multi-company boundaries;
- migration and existing data;
- integration error handling;
- query or performance expectations when relevant.

### 8. Validate findings

For each finding:

- cite file and relevant location;
- distinguish confirmed defect from inference;
- explain business or operational impact;
- propose the smallest safe remediation;
- define verification.

Do not inflate the report with generic style preferences.

## Severity

- **Critical**: unauthorized access, data loss, financial misstatement, or likely outage.
- **High**: material security, cross-company, workflow, migration, or accounting failure.
- **Medium**: correctness, performance, or maintainability issue with limited immediate impact.
- **Low**: non-blocking quality or documentation issue.
- **Observation**: contextual note or future improvement.

## Required output

Use `assets/review-report.md` and order findings by severity. Separate:

1. release blockers;
2. functional bugs;
3. security findings;
4. migration and upgrade risks;
5. performance issues;
6. maintainability and refactoring;
7. missing tests and documentation;
8. recommended remediation sequence.

If no material issue is found, state what was reviewed and what could not be verified.

## References to load

- Read `references/review-checklist.md` for broad addon reviews.
- Read `references/performance-review.md` when query volume or scheduled processing is relevant.
