---
name: odoo-data-model-diagram
description: Use this skill when producing an evidence-backed logical Odoo model diagram or drawDB-importable DBML from addon source, configured Odoo MCP metadata, or both. Do not use it for physical PostgreSQL reverse engineering, business-record extraction, or Odoo mutation.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients. Requires repository evidence, a configured read-only Odoo MCP connection, or both; the bundled converter requires Python 3.11+.
metadata:
  version: "0.1.0"
  author: OCloud
  status: experimental
  risk: read-only
  odoo:
    versions: ["17.0", "18.0", "19.0"]
    editions: [community, enterprise]
  hermes:
    tags: [odoo, data-model, erd, dbml, drawdb]
---

# Odoo Data Model Diagram

## Purpose

Produce a bounded logical ORM diagram that can be imported into drawDB as DBML.
It documents Odoo models and relations; it is not a claim about the physical
PostgreSQL schema.

## Use when

- documenting custom-addon models, fields, inheritance, or relations;
- creating an Odoo ERD, model map, or DBML diagram for design or review;
- comparing source declarations with the current live model metadata;
- preparing a bounded technical handoff before addon implementation or upgrade.

## Do not use when

- reverse engineering physical PostgreSQL tables, indexes, or join tables;
- extracting business records or analysing business-process state transitions;
- implementing an approved addon, changing drawDB, or extending the MCP server.

## Required inputs

- Target Odoo version and edition, confirmed by evidence.
- Explicit root model names, or a bounded reason to resolve an unknown root name.
- Repository or addon path when source evidence is requested.
- Selected instance and profile when live metadata evidence is requested.
- Requested field profile: standard (default) or full detail (explicit request only).

## Preconditions and composition

- Load `odoo-context-discovery` for repository, version, edition, and addon
  evidence when those facts are not already confirmed.
- For live metadata, require `odoo-live-context` to verify the selected instance,
  profile, version and edition, company scope, and effective read access first.
- Use `odoo-solution-design` for a prospective model design and
  `odoo-addon-development` for implementation. This skill does not approve a
  model change.

## Live metadata allowlist

After `odoo-live-context` verifies the selected instance, profile, version and
edition, company scope, and read access, use only these `odoo-rust-mcp` tools:

- `odoo_list_models`: one bounded query only when a requested root model name is
  unknown; never enumerate the instance.
- `odoo_get_model_metadata`: named roots and direct relation targets only.
- `odoo_check_access` with `operation=read`: exact model access verification when
  `odoo-live-context` has not already completed it.

Never call `odoo_read`, `odoo_search_read`, `odoo_count`, `odoo_name_search`,
`odoo_name_get`, `odoo_read_group`, `odoo_default_get`, `odoo_onchange`,
`odoo_generate_report`, `odoo_execute`, `odoo_execute_capability`,
`odoo_create`, `odoo_create_batch`, `odoo_update`, `odoo_delete`,
`odoo_copy`, `odoo_workflow_action`, cleanup tools, or SQL tools.

Use the configured instance identifier supplied by the selected profile. Never
request, store, display, or infer credentials, and never hard-code client
instance details in a diagram request.

## Workflow

1. Confirm target Odoo version and edition. Read exactly one matching
   `references/odoo-{17,18,19}-{community,enterprise}.md` file.
2. Ask for explicit root models. If names are uncertain, use one bounded
   `odoo_list_models` query to find candidates; do not enumerate the instance.
3. Include each root and one relation hop, with at most 30 models. Split a
   larger request into bounded-context diagrams or obtain explicit confirmation
   before expanding it.
4. Gather source evidence for `_name`, `_inherit`, `_inherits`, `_auto`,
   `_table`, field declarations, stored/computed/related behavior, constraints,
   and module ownership. Gather live metadata only for the selected models.
5. Use live metadata as the current-model and current-field baseline. Overlay
   source-only structural facts on matching items. Record source-only, live-only,
   and conflicting evidence; never silently reconcile a difference.
6. Select the standard field profile: `id`, display/name, requested and custom
   fields, relation fields, required fields, `state`, `active`, `company_id`,
   `currency_id`, and audit fields. Full-field output requires an explicit
   request.
7. Normalize the evidence using the contract in
   [references/dbml-mapping.md](references/dbml-mapping.md), then run:

   ```bash
   python3 scripts/model_graph_to_dbml.py --input model-graph.json --output diagram.dbml
   ```

8. Import the resulting DBML into a Generic drawDB diagram. Inspect unresolved
   stubs, synthetic many-to-many bridges, notes, and relation endpoints.
9. Copy [assets/data-model-diagram-report.md](assets/data-model-diagram-report.md)
   into the deliverable and link the DBML artifact.

## Diagram rules

- Quote Odoo technical model names such as `sale.order` in DBML.
- A `many2one` becomes a reference to the target model's `id`.
- Do not turn `one2many` into a duplicate physical column; it is represented by
  its inverse `many2one` when that metadata is in scope.
- Represent `many2many` with a clearly labelled synthetic logical bridge, never
  an asserted database join-table name.
- Keep required, readonly, compute, related, store, index, selection, and
  inheritance facts in notes unless direct physical-schema evidence proves a
  database constraint.
- Use an explicitly labelled stub when a relation target is unavailable.

## Safety

- Never read business records, credentials, or configuration secrets.
- Never call create, write, delete, execute, workflow, report, cleanup, or SQL
  tools.
- Do not infer installed modules, physical table names, database constraints, or
  Enterprise availability from a model label or metadata alone.
- Keep source and live evidence identifiers separate from client data.

## Required output

Provide:

- a drawDB-importable `*.dbml` logical model diagram;
- a report based on `assets/data-model-diagram-report.md`;
- roots, scope, evidence sources, source/live drift, omissions, stubs, and
  physical-schema limitations;
- confirmed, inferred, assumed, and unknown facts; and
- the next safe handoff skill.

## Verification

- DBML parses in drawDB and each reference endpoint exists.
- No diagram exceeds the agreed scope without recorded approval.
- Every physical-schema statement has direct source or database evidence.
- The report identifies all source/live differences and contains no record data.

## References to load

- Read [references/evidence-and-scope.md](references/evidence-and-scope.md)
  before source or live metadata collection.
- Read [references/dbml-mapping.md](references/dbml-mapping.md) before
  normalizing metadata or generating DBML.
- Read one matching Odoo version/edition reference after context confirmation.

## Failure and escalation

Return `blocked` without further live calls when version and edition, instance
and profile, read access, company scope, or required metadata cannot be
verified. Do not broaden access, elevate privileges, or fall back to
business-record reads. Escalate policy defects to the plugin or MCP owner and
model-design questions to `odoo-solution-design` or a human reviewer.
