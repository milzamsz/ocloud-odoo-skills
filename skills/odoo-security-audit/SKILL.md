---
name: odoo-security-audit
description: Use this skill when auditing an Odoo addon or integration for ACLs, record rules, field restrictions, multi-company isolation, unsafe public methods, RPC exposure, `sudo()` misuse, controller authentication, CSRF, portal or public access, attachments, SQL injection, ORM bypass, HTML sanitization, file uploads, secrets, or state-changing authorization.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients with read access to the target repository. This skill performs defensive review and does not authorize exploitation of live systems.
metadata:
  version: "0.1.0"
  author: OCloud
  status: experimental
  risk: read-only
  odoo:
    versions: ["17.0", "18.0", "19.0"]
    editions: [community, enterprise]
  hermes:
    tags: [odoo, security, acl, record-rules, controllers]
---

# Odoo Security Audit

## Purpose

Identify exploitable or material Odoo security defects and provide evidence, impact, remediation, and verification without changing the target system.

## Boundaries

- Audit defensively and read-only.
- Do not exploit production or access data beyond authorization.
- Use static fixtures or an explicitly authorized disposable environment for
  verification; never probe a live endpoint or database merely to confirm a
  finding.
- Do not recommend broad `sudo()` or administrator permissions as a fix.
- Do not expose secrets found during review; redact and report their location.
- Do not execute injection, XSS, CSRF, authorization-bypass, or cross-company
  payloads against live systems.

## Workflow

### 1. Map the attack and trust surface

Identify:

- internal users and groups;
- portal and public users;
- RPC-callable public methods;
- HTTP and JSON routes;
- scheduled jobs and integrations;
- file uploads and attachments;
- company-scoped records;
- sensitive financial, HR, personal, or tax data.

### 2. Review ACLs

Check every persistent model for intentional create, read, write, and unlink access. Flag:

- missing ACLs that break intended use;
- broad internal-user access;
- write or unlink access without business need;
- administrator-only behavior implemented through accidental absence rather than design.

### 3. Review record rules

Check:

- global versus group rule interaction;
- company restrictions;
- portal ownership rules;
- record-rule domains using user-controlled or incorrect fields;
- unintended access created by permissive group combinations;
- negative tests for cross-user and cross-company access.

### 4. Review fields and sensitive data

Check field-level groups, related fields, computed fields, exports, chatter, reports, and attachments for indirect exposure.

### 5. Review public methods and RPC

Any public model method may be callable over RPC when permissions allow. Verify:

- authorization and state checks occur inside the method;
- caller-controlled record IDs and values are validated;
- privileged operations are narrow;
- posted, approved, or legal documents cannot be mutated through an unguarded method.

### 6. Review `sudo()`

For every use:

- identify why normal access is insufficient;
- limit recordset and operation scope;
- validate caller authorization before elevation;
- avoid returning elevated records or sensitive values;
- confirm company boundaries;
- test unauthorized callers.

### 7. Review controllers

Check:

- route auth mode;
- HTTP method and mutation semantics;
- CSRF behavior;
- session and API authentication;
- object authorization after record lookup;
- request validation;
- error leakage;
- rate or abuse concerns where relevant;
- download and attachment authorization.

### 8. Review SQL, evaluation, and HTML

Check:

- parameterized SQL and justified ORM bypass;
- no string-built SQL;
- safe domain and expression evaluation;
- escaping and sanitization;
- `Markup` use;
- unsafe attribute access;
- template output and email rendering.

### 9. Review files and secrets

Check:

- upload type and size validation;
- storage and download permissions;
- path traversal;
- secrets in source, logs, examples, and configuration;
- webhook or integration signature validation.

### 10. Review business authorization

Security includes business state. Confirm users cannot bypass approval, posting, reconciliation, stock validation, cancellation, or reversal rules through alternate methods or imports.

## Required output

Use `assets/security-audit-report.md`. For each finding:

- ID and severity;
- confirmed or inferred status;
- affected code and surface;
- exploit or failure scenario described defensively;
- business impact;
- remediation;
- test or verification method.

Include a coverage summary and unverified surfaces.

## Release-blocking defaults

Treat as release blockers when confirmed:

- cross-company data leakage;
- public or portal unauthorized mutation;
- broad exposure of financial, HR, or personal data;
- SQL injection;
- arbitrary code or expression execution;
- unrestricted posted-document mutation;
- secret committed to source.

## References to load

- Read `references/acl-and-record-rules.md` for permission-heavy modules.
- Read `references/controllers.md` for HTTP, portal, website, or API modules.
- Read `references/sql-html-and-elevation.md` for SQL, HTML/XSS, public methods,
  or `sudo()` findings.
