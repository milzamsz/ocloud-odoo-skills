---
name: odoo-live-read
description: Use this skill when reading bounded business evidence from a configured Odoo 18 Community instance with an exact model, domain, fields, company scope, limit, order, purpose, sensitivity, and redaction plan. Do not use it for metadata-only context, unrestricted export, interpretation without a Phase 2 skill, or mutation.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients. Verified for Odoo 18.0 Community with the reconciled Odoo MCP read contract.
metadata:
  version: "0.1.0"
  author: OCloud
  status: experimental
  risk: read-only
  odoo:
    versions: ["18.0"]
    editions: [community]
  hermes:
    tags: [odoo, live, read, evidence]
---

# Odoo Live Read

## Purpose

Produce and execute a bounded, least-data live read plan and return evidence without changing Odoo or turning a question into unrestricted extraction.

## Preconditions and composition

- Require `odoo-context-discovery` and `odoo-live-context`; do not query records until instance, Odoo 18 Community, profile, company, model, and read access are verified.
- Load the relevant Phase 2 domain skill before choosing fields or interpreting business meaning. Use `odoo-functional-accounting` for posting, reconciliation, tax, or financial meaning and `odoo-security-audit` for access concerns.
- Use `odoo-solution-design` for design recommendations and delegate implementation, testing, review, OCA, and upgrade work to their Phase 1 owners.
- Never request, store, display, or infer credentials.

## Allowed tools

Use only: `odoo_search`, `odoo_search_read`, `odoo_read`, `odoo_count`, `odoo_read_group`, `odoo_name_search`, and `odoo_name_get`. The selected profile must include the tool, and Odoo ACLs and record rules remain authoritative.

## Workflow

1. State the question and select the Phase 2 domain skill that owns interpretation.
2. Define the exact model, domain, fields, company scope, finite limit, deterministic order, purpose, sensitivity, redaction, freshness, and completion evidence.
3. Minimize data: prefer `odoo_count` for counts, `odoo_read_group` for bounded aggregation, `odoo_search` for IDs, `odoo_read` for known IDs, and `odoo_search_read` for a bounded combined query. Use name tools only for bounded lookup or display labels.
4. Preview the plan and block empty fields, unbounded limits, unexplained cross-company reads, secret-bearing fields, broad personal-data extraction, or a tool absent from policy.
5. Execute only the approved read plan. Never retry a denial with broader scope or elevated access.
6. Record query shape, result count/class, redaction, truncation, correlation identifier, freshness, and whether the evidence answers the question. Do not place raw records in audit metadata.

## Safety rules

- Production is read-only. This skill never authorizes mutation in any environment.
- Never call defaults, onchange, model discovery/metadata, access checks, reports, generic methods, write, workflow, copy, batch, or cleanup tools; return to `odoo-live-context` for metadata/access.
- Preserve ACLs, record rules, allowed companies, field restrictions, and least privilege.
- Treat financial, personal, credential-like, document, and client data as sensitive; request only necessary fields and redact the output.

## Required output

Copy `assets/live-read-evidence.md`. Include context, domain owner, bounded request, exact tool, policy checks, sensitivity/redaction, result summary, audit-safe evidence, unknowns, and completion status.

## Verification

- The read matches the previewed model, domain, fields, company, limit, order, and purpose.
- Only an allowed tool was used and no denial was bypassed.
- Results are bounded, minimized, redacted, and interpreted by the relevant Phase 2 skill.
- No credentials, mutation, unrestricted export, or raw business data entered audit metadata.

## Reference to load

Read `references/bounded-read.md` before invoking a record tool.

## Failure and escalation

Return `blocked` when context, domain ownership, policy, sensitivity, company scope, or bounds are unresolved. Escalate policy defects to plugin/MCP owners and accounting, privacy, legal, or security interpretation to the responsible reviewer.
