---
name: odoo-integration-design
description: Use this skill when designing an Odoo 17, 18, or 19 Community or Enterprise integration with an external system, including API or controller boundaries, authentication, idempotency, retries, queues, webhooks, data ownership, reconciliation, observability, security, and performance. Do not use it for generic API coding, addon implementation, or a security audit alone.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients. Odoo 17, 18, or 19 Community or Enterprise is the verified baseline.
metadata:
  version: "0.1.0"
  author: OCloud
  status: experimental
  risk: advisory
  odoo:
    versions: ["17.0", "18.0", "19.0"]
    editions: [community, enterprise]
  hermes:
    tags: [odoo, integration, api, architecture]
---

# Odoo Integration Design

## Purpose

Produce an external-system integration contract that is secure, idempotent,
observable, recoverable, and explicit about data ownership.

## Preconditions and composition

- Load `odoo-context-discovery` when version, edition, repository, runtime, or
  installed modules are unknown.
- Load `odoo-solution-design` before recommending custom code, middleware, or
  asynchronous infrastructure; compare Standard, Configured, Third-party/OCA,
  Custom, and External options.
- Delegate implementation to `odoo-addon-development`, executable checks to
  `odoo-testing`, OCA contribution work to `odoo-oca-development`, defensive
  review to `odoo-security-audit` and `odoo-code-review`, and major-version
  changes to `odoo-version-upgrade`.
- This skill defines the boundary and contract; it does not duplicate those
  Phase 1 procedures or authorize live writes.

## Use when

- connecting Odoo to ecommerce, payment, logistics, identity, finance, or
  another ERP;
- choosing pull, push, webhook, scheduled batch, queue, or middleware patterns;
- defining authentication, mapping, retries, deduplication, reconciliation, or
  operational ownership.

## Do not use when

- designing a generic API with no Odoo-specific boundary;
- implementing an already approved addon or controller;
- auditing existing code without redesign authority;
- designing only a report, QWeb template, dashboard, or frontend.

## Workflow

1. Confirm Odoo 17, 18, or 19 Community or Enterprise, participating systems, actors, data sensitivity,
   expected volume, latency, availability, and regulatory constraints.
2. Define the system of record per entity and field. Map identifiers,
   companies, currencies, time zones, lifecycle states, and deletion policy.
3. Evaluate standard import/export and supported APIs, reviewed OCA/vendor
   components, external middleware, then custom Odoo code. Record rejected
   options and evidence.
4. Select direction and transport. Specify trigger, endpoint or job boundary,
   request/response schema, versioning, pagination, ordering, and size limits.
5. Design authentication and authorization with least privilege, secret
   rotation outside the skill, ACL and record-rule enforcement, company scope,
   input validation, and safe error disclosure.
6. Define an idempotency key, duplicate behavior, retryable versus terminal
   errors, bounded backoff, timeout, concurrency, ordering, dead-letter or
   exception handling, replay rules, and reconciliation.
7. Set performance controls: batch size, rate limits, queue/back-pressure
   threshold, indexed lookup keys, query budget, retention, and peak volume.
8. Define logs, correlation IDs, metrics, alerts, ownership, support runbook,
   rollback/compensation, and evidence needed before enabling writes.

## Decision rules

- Prefer an external boundary when orchestration, credential isolation, burst
  handling, or lifecycle independence outweighs in-Odoo simplicity.
- Do not assume a queue addon. Verify target branch, license, dependencies,
  maintenance, ACL behavior, and operational burden before selecting OCA.
- Treat controller authentication as only one layer; model ACLs, record rules,
  company isolation, field exposure, and business authorization still apply.
- Never use blanket elevated access or direct SQL as the default integration
  design. Document any exception and require focused security review.

## Safety rules

Live Odoo access is read-only by default. Do not send test webhooks, create
records, replay messages, rotate credentials, install modules, or change
configuration without explicit authorization. Use synthetic data and a
disposable environment for executable validation. Never include secrets or
personal/client data in the artifact.

## Required output

Use `assets/integration-design.md`. Include evidence labels, assumptions,
unknowns, CE/Enterprise boundaries, option analysis, ownership and mapping,
security/company controls, idempotency and failure semantics, performance
limits, observability, reconciliation, rollout, acceptance criteria, and
prohibited actions.

## Verification

- Every mutation has authorization, idempotency, retry, and reconciliation
  behavior.
- ACLs, record rules, multi-company isolation, secret handling, and field
  exposure are explicit.
- Volume and failure assumptions are quantified or marked unknown.
- Completion evidence is testable without mutating a live system.

## Reference to load

Read exactly one `references/odoo-{17,18,19}-{community,enterprise}.md` file after the target version and edition are confirmed.

Read `references/odoo-18-community.md` for Odoo 17, 18, or 19 Community or Enterprise boundaries before
making version-sensitive claims.

## Failure and escalation

Stop at a design with unresolved blockers when data ownership, legal basis,
credentials, target API contract, company isolation, or recovery ownership is
unknown. Escalate security-sensitive designs for human review.
