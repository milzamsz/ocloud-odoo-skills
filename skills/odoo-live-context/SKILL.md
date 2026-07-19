---
name: odoo-live-context
description: Use this skill when a configured live Odoo connection must verify the selected instance, environment, Odoo 17, 18, or 19 version and Community/Enterprise edition, profile, company scope, available models, metadata, or effective read access before querying business records. Do not use it for record extraction, repository-only discovery, or mutation.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients. Verified for Odoo 17.0, 18.0, or 19.0 Community or Enterprise with the reconciled Odoo MCP read contract.
metadata:
  version: "0.1.0"
  author: OCloud
  status: experimental
  risk: read-only
  odoo:
    versions: ["17.0", "18.0", "19.0"]
    editions: [community, enterprise]
  hermes:
    tags: [odoo, live, context, metadata]
---

# Odoo Live Context

## Purpose

Produce verified live instance, company, model, and access context without reading business records or changing Odoo.

## Preconditions and composition

- Require `odoo-context-discovery` for repository, deployment, version, and edition evidence; live metadata supplements rather than replaces it.
- Use `odoo-solution-design` when the evidence leads to a design choice.
- Load the relevant Phase 2 skill before interpreting domain meaning; use `odoo-security-audit` for access-control concerns.
- Require a configured instance selected through the Hermes plugin. Never request, store, display, or infer credentials.

## Allowed tools

Use only these reconciled metadata tools when present in the selected profile: `odoo_list_models`, `odoo_get_model_metadata`, and `odoo_check_access`. Presence in the MCP manifest is not authorization; plugin policy, MCP policy, Odoo ACLs, and record rules remain authoritative.

## Workflow

1. Record the selected `instance_id`, environment, profile, expected Odoo version and edition, freshness, and evidence source.
2. Confirm Odoo 17, 18, or 19 Community or Enterprise from configured and live evidence. Mark any conflict **Unknown** and stop version-sensitive conclusions.
3. Establish the intended company scope from trusted configured context; do not discover companies by querying business records.
4. Use `odoo_list_models` only with a bounded purpose, then `odoo_get_model_metadata` only for named models.
5. Use `odoo_check_access` for the exact model and required read operation. Missing access is evidence, not a reason to elevate privileges.
6. Record Confirmed, Inferred, Assumed, and Unknown facts and identify the Phase 2 skill required before any domain interpretation.

## Safety rules

- Production is read-only. This skill never authorizes mutation in any environment.
- Do not call record tools, unrestricted extraction, generic methods, reports, defaults, onchange, write, workflow, copy, batch, or cleanup tools.
- Do not bypass ACLs or record rules, broaden company scope, use elevated access, or expose private identifiers or raw metadata beyond the stated purpose.
- Stop on an unpinned instance, stale or unreconciled manifest, profile mismatch, unsupported version/edition, unexplained company scope, or unavailable required tool.

## Required output

Copy `assets/live-context.md`. Include context envelope, evidence labels, exact tools used, bounded models, access results, unknowns, blockers, and permitted read-only next actions.

## Verification

- Instance, environment, profile, Odoo 17, 18, or 19 Community or Enterprise, and company scope are evidence-backed.
- Every tool is in the exact allowlist and selected profile.
- No business records or credentials were requested or returned.
- Access denial remains denied and unresolved conflicts remain explicit.

## Reference to load

Read exactly one `references/odoo-{17,18,19}-{community,enterprise}.md` file after the target version and edition are confirmed.

Read `references/read-only-context.md` before invoking a metadata tool.

## Failure and escalation

Return `blocked` without further calls when identity, policy, version, company scope, or access cannot be verified. Escalate policy defects to plugin/MCP owners and domain questions to the relevant Phase 2 skill or human reviewer.
