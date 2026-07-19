---
name: odoo-testing
description: Use this skill when designing, implementing, reviewing, or running tests for Odoo models, workflows, security, record rules, multi-company behavior, controllers, JavaScript, tours, reports, scheduled jobs, integrations, migrations, query counts, installation, or module upgrades, and when defining executable completion evidence.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients with access to a safe Odoo development or test environment.
metadata:
  version: "1.0.0"
  author: OCloud
  status: stable
  risk: controlled-write
  odoo:
    versions: ["17.0", "18.0", "19.0"]
    editions: [community, enterprise]
  hermes:
    tags: [odoo, testing, quality, verification]
---

# Odoo Testing

## Purpose

Choose and implement the smallest test suite that proves functional behavior, permissions, data integrity, migration safety, and relevant performance.

## Safety

- Run tests only in a disposable or designated test database.
- Never point test or upgrade commands at production.
- Use repository-defined commands and tags.
- Do not disable meaningful tests merely to make a pipeline pass.

## Workflow

### 1. Translate acceptance criteria into assertions

For each behavior define:

- setup;
- actor and company;
- action;
- expected records, state, or journal impact;
- denied or error cases;
- cleanup or transaction behavior.

### 2. Select test seams

| Change | Preferred seam |
|---|---|
| Model and business logic | Transaction or savepoint-based Python test according to target version and repository convention. |
| Form and onchange behavior | Odoo `Form` helper where appropriate. |
| ACL and record rules | Tests using realistic users, groups, and companies. |
| Controller | HTTP or route test with authentication and authorization cases. |
| JavaScript and OWL | QUnit or repository-standard JS tests. |
| End-to-end UI | Tour or browser test for critical journeys, not every field. |
| Report | Render and assert meaningful structure or values. |
| Cron | Direct method invocation, batching, idempotency, and repeated-run behavior. |
| Integration | Adapter contract tests, mocked remote failures, retries, and idempotency. |
| Migration | Before/after fixture and data reconciliation. |
| Performance | Query-count or bounded runtime test when regression risk is material. |

### 3. Cover permissions and companies

Include:

- authorized user success;
- unauthorized user denial;
- cross-company denial;
- portal or public behavior when relevant;
- `sudo()` containment;
- field and action visibility only when it affects security or functional behavior.

### 4. Cover states and accounting

Test valid and invalid transitions. When accounting is affected, verify accounts, debit and credit amounts, currency, tax, posting date, and reconciliation behavior as applicable.

### 5. Cover existing data and upgrades

For stored fields, semantic changes, renamed XML IDs, or module upgrades, test representative prior data and post-upgrade invariants.

### 6. Keep tests deterministic

- avoid current-time dependence without controlled dates;
- avoid external network calls;
- create minimum required records;
- isolate company and currency context;
- assert business outcomes, not incidental implementation details.

### 7. Run focused then broad verification

1. focused test module or tag;
2. affected addon suite;
3. installation on clean database when relevant;
4. upgrade on representative disposable database;
5. broader CI according to repository policy.

## Required output

Use `assets/test-evidence.md` and provide:

- behavior-to-test matrix;
- test files created or reviewed;
- users, groups, and company contexts;
- commands executed;
- pass/fail result;
- untested risks;
- evidence required before production release.

## Completion rule

A passing test that does not assert the business requirement is not completion. A screenshot of a green terminal is especially not accounting reconciliation, despite its soothing color.

## References to load

Read exactly one `references/odoo-{17,18,19}-{community,enterprise}.md` file after the target version and edition are confirmed.

- Read `references/test-seams.md` when selecting frameworks and test types.
- Read `references/security-test-matrix.md` for ACL, record-rule, and company tests.
