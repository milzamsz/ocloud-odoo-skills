---
name: odoo-dynamic-dashboard
description: Use this skill when an AI agent must generate an installable dashboard for the NexGen dynamic_dashboard_ai_nexgen addon on Odoo 20 Community, from a business question to reviewed data XML with model, SQL, or KPI items, a fixed grid layout, and access controls. Do not use it for choosing a reporting mechanism in general, QWeb/PDF reports, standard pivot or graph views, or creating dashboard records directly in a live database.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients. Requires the dynamic_dashboard_ai_nexgen addon source or an installed instance on Odoo 20.0 Community; the bundled validator requires Python 3.11+.
metadata:
  version: "0.1.1"
  author: OCloud
  status: experimental
  risk: advisory
  odoo:
    versions: ["20.0"]
    editions: [community]
  hermes:
    tags: [odoo, dashboard, kpi, analytics, xml]
---

# Odoo Dynamic Dashboard

## Purpose

Turn a business question into a dashboard for the NexGen `dynamic_dashboard_ai_nexgen`
addon, delivered as Odoo data XML inside a custom addon. The XML is reviewed,
versioned, and installed by a normal module update; this skill never writes to
a database.

## Use when

- a user asks for a dashboard, KPI board, or set of charts built with the
  dynamic dashboard addon;
- an AI-generated dashboard must become repeatable and deployable across
  databases;
- an existing dashboard XML must be extended with new tiles, charts, SQL items,
  KPI hierarchies, or filters.

## Do not use when

- the mechanism is still open (dashboard vs pivot, QWeb, export): use
  `odoo-reporting` first;
- the request is a QWeb/PDF document or a standard list, pivot, or graph view;
- the user wants records created now in a live database: that is controlled
  mutation, owned by `odoo-live-mutation`, not this skill;
- the target is not Odoo 20 Community or the addon is not present.

## Required inputs

- Confirmed Odoo 20.0 Community and the addon version (manifest or installed module).
- The business question, audience, and the decisions the dashboard supports.
- The target custom addon that will own the XML (it must depend on
  `dynamic_dashboard_ai_nexgen` and on every module whose models it reads).
- Field evidence for every model used: addon source or bounded live metadata.

## Preconditions

- Load `odoo-context-discovery` when version, edition, addon path, or installed
  modules are unknown.
- Live metadata, if used, follows `odoo-live-context` and stays read-only:
  model metadata and access checks only, no record reads beyond what that skill allows.
- Hand implementation in the addon (manifest, tests) to `odoo-addon-development`.

## Workflow

1. Confirm version, edition, and addon version. Read `references/odoo-20-community.md`.
2. Write the design with `assets/dashboard-design.md`: question, audience, metrics
   (source model, measure, aggregation, grain, date field and period, filters),
   and who may see the dashboard and each item.
3. For each metric choose the data source, in this order: Odoo model (ORM) item,
   KPI definition, SQL item. Use SQL only when the ORM cannot express it, and
   read `references/sql-items.md` before writing any query.
4. Verify every model and field: stored, correct type (measures: integer, float,
   monetary; date filters: date or datetime), and installed. Never invent names.
5. Choose item types and sizes from `references/dashboard-model.md`; place items on
   the 12-column grid without overlap, headline tiles first.
6. Write the XML with the patterns in `references/xml-patterns.md`: `noupdate="1"`,
   `search=` lookups for models and fields, and the `dd_skip_auto_layout` context
   on every item so the grid is kept.
7. Run `scripts/validate_dashboard_xml.py <file.xml>` and fix every error; justify
   or fix every warning.
8. Add the file to the addon manifest `data` and the dependencies, then hand over
   for a module update on a disposable or development database.

## Decision rules

- Prefer ORM items: they run as the viewing user, so ACLs and record rules apply.
- SQL items bypass ACLs and record rules on the local database. Use them only with
  `allowed_group_ids` set, a company filter (`{company_id}`), and an explicit reason.
- Use KPI definitions for count targets, formulas, and parent/child roll-ups; show
  them on the board with an item linked by `kpi_id`. For amounts against a target,
  use a tile with target lines: sum and average KPIs fail on Odoo 20 with addon
  20.0.1.0.15.
- Do not use the addon's JSON import as a delivery format: it drops domains,
  filters, dashboard settings, and layout.
- Keep one dashboard per audience; 4 to 12 items. Put tiles and KPIs on the first row.
- Never enable the addon's own AI wizard or store API keys as part of this output.

## Safety rules

- Output files only. Do not create, update, or delete records in any database.
- No credentials, client data, or personal data in XML, names, or notes.
- SQL must be a single read-only SELECT that passes the validator; no dynamic SQL
  built from user input.

## Required output

- The completed `assets/dashboard-design.md`.
- The data XML file, with its validator output (no errors).
- The manifest changes (`depends`, `data`) for the owning addon.
- Open items: unknown fields, unverified access, assumptions.

## Verification

- `scripts/validate_dashboard_xml.py` reports no errors.
- The addon installs or updates on a disposable Odoo 20 Community database and the
  dashboard opens; each item shows data or an expected empty state.
- A user outside the allowed groups cannot open restricted items.

## References to load

- `references/odoo-20-community.md`: version facts and verified addon behavior.
- `references/dashboard-model.md`: models, fields, selection values, grid sizes, groups.
- `references/xml-patterns.md`: XML for dashboards, ORM items, SQL items, KPIs, filters.
- `references/sql-items.md`: only when an item uses SQL.

## Failure and escalation

Stop and report when a needed field does not exist, a metric's definition is
ambiguous, the addon or a source module is missing, or a SQL item would expose
data the audience may not see. Accounting metrics need the sign, posting state,
and company rules confirmed by a functional reviewer.
