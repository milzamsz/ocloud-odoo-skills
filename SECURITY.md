# Security Policy

## 1. Scope

This policy covers skill instructions, references, scripts, assets, source records, evaluation fixtures, bundles, and distribution metadata.

## 2. Security principles

- Treat third-party skills as untrusted input.
- Treat executable scripts as software supply-chain artifacts.
- Keep credentials outside the repository.
- Default live Odoo access to read-only.
- Require explicit approval for state-changing operations.
- Apply least privilege and company isolation.
- Preserve audit evidence for controlled operations.

## 3. Prohibited content

Do not commit:

- passwords, API keys, session cookies, database URLs, or private keys;
- client records, database dumps, filestore data, invoices, payroll, or tax identifiers;
- proprietary Odoo Enterprise source code;
- copied third-party content without approved license handling;
- obfuscated scripts;
- silent downloads or remote execution;
- commands that delete broad paths or databases without bounded validation;
- production credentials embedded in examples.

## 4. Odoo-specific risk areas

Every relevant skill must consider:

- ACL completeness and excessive permissions;
- record-rule interaction and global rule restrictions;
- multi-company data leakage;
- field group restrictions;
- public methods callable over RPC;
- `sudo()` scope and justification;
- controller authentication and CSRF;
- portal and public attachment access;
- SQL injection and ORM bypass;
- unsafe HTML, Markup, and dynamic evaluation;
- unrestricted file upload;
- journal posting, reversal, reconciliation, and period impact;
- module installation or upgrade side effects.

## 5. Script security requirements

Scripts must:

- reject ambiguous or root paths for destructive file operations;
- use argument arrays rather than shell interpolation;
- avoid `shell=True` unless justified and safely bounded;
- avoid logging secret values;
- support dry-run where mutation is possible;
- constrain network destinations when network use is required;
- pin or document dependencies;
- expose clear exit codes;
- include tests for validation and failure paths.

## 6. Skill supply-chain controls

- Register source URL, authority, license status, and review date.
- Review all referenced local files before release.
- Scan installed third-party skills before extracting concepts.
- Do not bypass Hermes security scanning merely to make installation succeed.
- Prefer pinned releases or commits for evaluation inputs.
- Review dependency updates and generated lock files.

## 7. Reporting a vulnerability

Report privately to the repository security contact once defined. Include:

- affected skill or script;
- impact;
- reproduction steps;
- affected versions;
- suggested mitigation;
- whether credentials or customer data may be involved.

Do not publish client data or active production exploit details.

## 8. Response targets

- Critical: immediate triage and disable affected distribution where possible.
- High: triage within one business day.
- Medium and low: schedule according to release risk.

## 9. Release response

When a released skill is unsafe:

1. mark it deprecated or remove it from current catalog;
2. publish an advisory;
3. release a corrected version;
4. identify affected versions;
5. add a regression test;
6. review adjacent skills for the same pattern.
