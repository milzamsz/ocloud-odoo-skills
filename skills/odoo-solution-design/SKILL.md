---
name: odoo-solution-design
description: Use this skill when translating an Odoo business requirement into a functional and technical solution, deciding between standard features, configuration, OCA or vendor addons, native low-code, custom addons, and external services, or documenting scope, process, impacts, assumptions, risks, and acceptance criteria before implementation.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients. Requires a confirmed Odoo context for version-sensitive decisions.
metadata:
  version: "1.0.0"
  author: OCloud
  status: stable
  risk: advisory
  odoo:
    versions: ["18.0"]
    editions: [community]
  hermes:
    tags: [odoo, solution-design, functional, architecture]
---

# Odoo Solution Design

## Purpose

Convert a business problem into the simplest viable Odoo solution while preserving security, accounting correctness, maintainability, and upgradeability.

## Preconditions

- Load or produce an Odoo context summary.
- Identify actors, current process, target outcome, constraints, and success criteria.
- Separate business requirements from the technology suggested by the requester.

## Use when

- a new Odoo feature or workflow is proposed;
- someone requests a custom module before alternatives are evaluated;
- comparing Community, Enterprise, OCA, or external integration options;
- preparing a BRD, scope, architecture decision, or implementation plan;
- an existing customization should be simplified or replaced.

## Do not use when

- implementing an already approved and sufficiently specified change;
- performing a code-only review without redesign authority;
- answering a narrow factual Odoo question.

## Workflow

### 1. Define the real business goal

Document:

- problem and affected users;
- operational, financial, compliance, or customer impact;
- current process and failure points;
- target outcome and measurable success;
- must-have versus optional requirements.

### 2. Map the business process

Describe:

- actors and permissions;
- trigger and inputs;
- operational documents;
- state transitions;
- validation and exception paths;
- outputs, reports, notifications, and audit evidence;
- stock, accounting, tax, or integration impact.

### 3. Evaluate solution levels in order

1. **Standard**: feature exists in target edition.
2. **Configured**: settings, master data, workflow, security, automated actions, or views are sufficient.
3. **Third-party**: reviewed OCA or vendor addon fits.
4. **Low-code**: supported native customization is appropriate and maintainable.
5. **Custom**: an OCloud addon is justified.
6. **External**: middleware or external service is a better boundary.

For each option, assess fit, gaps, cost, complexity, lock-in, maintainability, security, and upgrade impact.
Do not omit a level: mark it `not applicable` with evidence when it does not fit.
For OCA, search the correct functional repositories and target-version branches,
then verify manifest dependencies, license, maintenance state, tests, and overlap
with standard behavior. A module name or marketplace listing is not proof of fit.

### 4. Challenge the proposed technology

Reject unnecessary custom code, middleware, asynchronous infrastructure, or AI when simpler Odoo behavior satisfies the requirement. Conversely, reject fragile configuration tricks when a small explicit addon is safer.

### 5. Define component classification

Classify every material component as Standard, Configured, Third-party, Low-code, Custom, or External.

### 6. Design functional behavior

Define:

- models and business objects conceptually;
- states and transitions;
- permissions and company scope;
- user actions and validation;
- automation and schedules;
- reporting;
- error and recovery behavior.

Do not jump to fields and methods before process behavior is coherent.

### 7. Evaluate cross-cutting impacts

At minimum:

- access rights and record rules;
- multi-company and multi-currency;
- accounting entries, posting, reconciliation, and tax;
- performance and volume;
- integrations and idempotency;
- migration and existing data;
- monitoring, backup, and rollback;
- Community/Enterprise availability.

When accounting is relevant, distinguish operational documents from journal
entries and state debit/credit direction, posting trigger and timing,
reconciliation, currency, and tax assumptions. For multi-company scope, state
record ownership, allowed companies, company-dependent configuration,
intercompany behavior, and consolidation/reporting boundaries.

### 8. Select implementation level

Use the simplest architecture that is secure, observable, recoverable, and maintainable. Define triggers for evolving from MVP to a more scalable design.

## Required output

Use `assets/solution-design-template.md` and include:

- executive summary;
- context and assumptions;
- current and target process;
- option comparison;
- recommended decision and rejected alternatives;
- component classification;
- functional requirements;
- architecture and integration impact;
- security and accounting impact;
- data and migration considerations;
- implementation phases;
- acceptance criteria;
- risks and blockers.

## Verification

- Standard and configuration were evaluated before custom development.
- OCA or trusted alternatives were considered where relevant.
- Exact Odoo version and edition are stated.
- Accounting is explained beyond UI behavior when relevant.
- Unknown regulatory or compatibility claims are marked for verification.
- Acceptance criteria are testable.

## References to load

- Read `references/component-classification.md` for classification examples.
- Read `references/architecture-levels.md` when scale or availability drives architecture.
