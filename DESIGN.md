# Skill Design System

## 1. Design goals

The design system makes skills predictable for agents and maintainers. A reader should quickly understand why a skill activates, what evidence it requires, which actions are safe, and what output proves completion.

## 2. Skill taxonomy

### 2.1 Foundation skills

Cross-domain workflows used before or across Odoo work:

- context discovery;
- solution design;
- code review;
- security audit;
- testing;
- upgrade.

### 2.2 Engineering skills

Implementation-focused workflows:

- addon development;
- OCA development;
- controllers;
- OWL frontend;
- QWeb reports;
- integrations;
- performance.

### 2.3 Functional skills

Business-process workflows:

- CRM and Sales;
- Purchase;
- Inventory;
- Manufacturing;
- POS;
- Project and Services;
- Helpdesk;
- Website and eCommerce.

### 2.4 Accounting and localization skills

- accounting foundations;
- reconciliation;
- taxes and withholding;
- Indonesian localization;
- PSAK-oriented analysis;
- migration reconciliation.

### 2.5 Operations skills

- deployment review;
- backup and restore planning;
- module upgrade runbook;
- monitoring;
- incident triage.

## 3. Naming convention

Use `odoo-<outcome>`.

Good:

- `odoo-security-audit`
- `odoo-version-upgrade`
- `odoo-indonesia-tax-design`

Avoid:

- `odoo-expert`
- `odoo-everything`
- `odoo-python-xml-js-super-skill`
- names containing a version unless the entire skill is intentionally version-pinned.

## 4. Description design

The description is the trigger contract. It must include:

- user intent;
- distinctive Odoo concepts;
- scenarios where it should activate;
- boundaries that separate it from adjacent skills.

Example:

```yaml
description: Use this skill when reviewing an Odoo addon or pull request for ORM correctness, manifest and dependency issues, XML inheritance, security, multi-company behavior, performance, upgradeability, missing tests, or production readiness. Do not use it as the primary implementation workflow for a new feature.
```

## 5. Core document pattern

```markdown
# Skill title

## Purpose
## Use when
## Do not use when
## Required inputs
## Preconditions
## Workflow
## Decision rules
## Safety rules
## Required output
## Verification
## References to load
## Failure and escalation
```

The sections may be adjusted, but the contract must remain visible.

## 6. Progressive disclosure pattern

### Keep in `SKILL.md`

- task boundary;
- mandatory workflow;
- critical safety constraints;
- output contract;
- instructions for selecting references.

### Move to `references/`

- detailed API notes;
- version differences;
- examples by domain;
- long checklists;
- migration cases;
- official source index.

### Move to `scripts/`

- deterministic repository inspection;
- manifest parsing;
- ACL coverage checks;
- XML parsing;
- evaluation utilities.

### Move to `assets/`

- report templates;
- YAML output schemas;
- sample fixtures;
- checklists intended for copying.

## 7. Control calibration

### Flexible guidance

Use when several valid approaches exist. Explain goals, constraints, and trade-offs.

Example: selecting an Odoo integration pattern.

### Prescriptive guidance

Use when sequence and safety are fragile.

Example: database migration must run on a disposable copy with backup verification before cutover planning.

## 8. Output design

Every skill returns a structured artifact, not merely observations.

### Context discovery

- confirmed facts;
- evidence;
- unresolved assumptions;
- risks;
- allowed next actions.

### Solution design

- business problem;
- standard/configured/OCA/custom/external options;
- recommendation;
- impacts and risks;
- acceptance criteria.

### Code review

- critical findings;
- bugs;
- security findings;
- upgrade risks;
- performance findings;
- refactoring;
- missing tests;
- prioritized remediation.

### Security audit

- threat surface;
- finding severity;
- exploit scenario;
- affected code;
- required fix;
- verification method.

## 9. Severity model

| Severity | Definition |
|---|---|
| Critical | Likely unauthorized access, data loss, financial misstatement, or production outage. |
| High | Material security, accounting, cross-company, or workflow failure requiring release blocking. |
| Medium | Correctness, performance, or maintainability issue with limited immediate impact. |
| Low | Non-blocking quality or documentation issue. |
| Observation | Context or future improvement without current defect. |

## 10. Evidence labels

Use explicit labels:

- **Confirmed**: observed in code, configuration, test, or official target-version source.
- **Inferred**: supported by evidence but not directly confirmed.
- **Assumed**: temporary working assumption.
- **Unknown**: information required before a safe decision.

## 11. Version design

A skill must never silently blend version-specific syntax.

Required pattern:

1. Discover version.
2. Load matching version reference.
3. If unsupported, inspect target source and official documentation.
4. Mark unvalidated guidance.
5. Add a regression fixture before claiming support.

## 12. Edition design

Each skill must distinguish:

- Community capability;
- Enterprise capability;
- OCA or third-party capability;
- custom OCloud capability.

Never describe an Enterprise feature as generally available in Community.

## 13. Functional and accounting design

Functional skills must describe:

- actors and responsibilities;
- operational documents;
- state transitions;
- validations;
- exceptions;
- permissions;
- resulting stock, financial, or tax impact.

Accounting skills must additionally describe:

- debit and credit effect;
- posting timing;
- reconciliation;
- currency and tax assumptions;
- operational document versus journal entry distinction.

## 14. Anti-patterns

- giant general-purpose skill;
- copying official documentation into references;
- copying community content without license review;
- tool commands that assume paths or containers;
- `sudo()` as routine problem-solving advice;
- “run tests” without defining required evidence;
- claiming success because code parses;
- adding every possible option instead of recommending a default;
- using role-play claims instead of operational instructions;
- embedding secrets, tokens, URLs with credentials, or client identifiers.

## 15. Review checklist

A reviewer confirms:

- scope is coherent;
- description triggers correctly;
- adjacent skill boundaries are clear;
- version and edition behavior is explicit;
- core file remains concise;
- references are loaded conditionally;
- scripts are justified and safe;
- output is testable;
- sources are registered;
- evaluations cover near misses;
- no unsupported authority claims exist.
