---
name: odoo-reporting
description: Use this skill when designing an Odoo 18 Community report and choosing among list or pivot analysis, QWeb HTML/PDF, export, spreadsheet-compatible output, or an external analytics boundary while defining data sources, filters, ACLs, multi-company behavior, rendering, and performance. Do not use it for generic frontend work, report implementation, or security audit alone.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients. Odoo 18 Community is the verified baseline.
metadata:
  version: "0.1.0"
  author: OCloud
  status: experimental
  risk: advisory
  odoo:
    versions: ["18.0"]
    editions: [community]
  hermes:
    tags: [odoo, reporting, qweb, pdf, analytics]
---

# Odoo Reporting

## Purpose

Produce a reporting design that selects the simplest suitable mechanism and
defines trustworthy data, access, rendering, and performance behavior.

## Preconditions and composition

- Load `odoo-context-discovery` when version, edition, repository, installed
  modules, or runtime is unknown.
- Load `odoo-solution-design` before recommending custom code, third-party
  reporting components, or external analytics infrastructure.
- Delegate implementation to `odoo-addon-development`, executable evidence to
  `odoo-testing`, OCA work to `odoo-oca-development`, defensive assessment to
  `odoo-security-audit` and `odoo-code-review`, and major-version changes to
  `odoo-version-upgrade`.
- This skill owns the report decision artifact, not Phase 1 implementation,
  review, security, testing, or upgrade procedures.

## Use when

- choosing an operational view, pivot/graph, QWeb document, PDF, export,
  spreadsheet-compatible dataset, or external analytics boundary;
- defining a report's audience, metrics, data source, filters, layout, access,
  localization, volume, or performance budget;
- redesigning a slow, misleading, insecure, or hard-to-maintain Odoo report.

## Do not use when

- implementing an approved QWeb template or Python report model;
- building generic OWL/frontend behavior with no reporting decision;
- auditing code or ACLs without report redesign;
- designing a system-to-system data integration whose primary outcome is sync.

## Workflow

1. Confirm Odoo 18 Community, business decision, audience, frequency, delivery
   format, legal/audit needs, freshness, and acceptance criteria.
2. Define data semantics: source models, record grain, date basis, states,
   inclusions/exclusions, currency conversion, units, totals, and provenance.
3. Evaluate standard list/search/pivot/graph and existing reports first, then
   configured behavior, reviewed OCA/vendor options, custom QWeb/export code,
   and external analytics. Record evidence and rejected alternatives.
4. Select the mechanism:
   - operational exploration: list, search, pivot, or graph;
   - transactional printable document: QWeb HTML/PDF;
   - bounded portable data: export or spreadsheet-compatible output;
   - cross-system, high-volume, historical analytics: external boundary.
5. Define filters, grouping, sorting, pagination, drill-down, parameters,
   localization, paper format, page-break, attachment, and delivery behavior as
   applicable.
6. Define access using least privilege. Preserve model ACLs, record rules,
   allowed companies, sensitive-field restrictions, and report/action access.
   Never use elevated access merely to make a report complete.
7. Set a performance budget: expected rows/pages, query count, aggregation
   strategy, prefetch/batching, memory, render timeout, attachment caching and
   invalidation, and peak concurrency. Avoid per-row searches and unbounded
   render/export operations.
8. Specify fixtures and expected totals, access-denied cases, multi-company and
   multi-currency cases, rendering checks, load evidence, and human review.

## Decision rules

- Prefer standard views and reports when they answer the decision accurately.
- A PDF is a presentation artifact, not an analytics engine. Move unbounded or
  interactive analysis to an appropriate mechanism.
- Do not assume native spreadsheet authoring or Enterprise-only capabilities in
  Community. Label unverified features and external/OCA candidates explicitly.
- For accounting reports, distinguish operational documents from journal
  entries and define debit/credit signs, posting state, reconciliation, company,
  currency-rate date, and tax assumptions.

## Safety rules

Live Odoo access is read-only by default. Do not install report modules,
generate or attach documents, execute exports, email reports, warm caches, or
change actions without explicit authorization. Use synthetic data and a
disposable environment for rendering and load tests. Prevent report outputs,
logs, and fixtures from exposing secrets or client/personal data.

## Required output

Use `assets/reporting-design.md`. Include evidence labels, assumptions,
unknowns, CE/Enterprise boundaries, mechanism comparison, metric definitions,
data lineage, ACL/company controls, rendering behavior, performance budget,
test matrix, acceptance criteria, prohibited actions, and blockers.

## Verification

- The chosen mechanism matches audience, volume, interactivity, and audit need.
- Every metric has an unambiguous source, grain, filter, date, state, and
  currency/unit definition.
- ACLs, record rules, companies, sensitive fields, and denied cases are tested.
- Rendering and performance completion evidence is measurable.

## Reference to load

Read `references/odoo-18-community.md` before making version-sensitive report,
QWeb, PDF, analytics, or edition claims.

## Failure and escalation

Stop at a design with unresolved blockers when metric ownership, accounting
semantics, access policy, company/currency treatment, expected volume, or legal
retention is unknown. Escalate sensitive and accounting outputs for human
functional/security review.
