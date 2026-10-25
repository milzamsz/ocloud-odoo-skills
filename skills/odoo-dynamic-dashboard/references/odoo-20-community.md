# Odoo 20.0 Community: dynamic dashboard facts

Evidence: addon `dynamic_dashboard_ai_nexgen` version `20.0.1.0.15` (vendor NexGen
Solutions, license OPL-1) read from source and installed on a disposable Odoo 20.0
Community database. "Source" means read in code; "runtime" means observed on an
installed database.

## Addon

- Depends on `base`, `bus`, `mail`, `web`. Application module.
- Main models: `dynamic.dashboard` (board), `dynamic.dashboard.item` (tile/chart),
  `dynamic.dashboard.kpi` (KPI tree), `dynamic.dashboard.filter` (global filter).
- Item data for Odoo-model items is read with the ORM as the viewing user
  (source): ACLs and record rules apply.
- SQL items run on the database cursor inside a savepoint (source): no ACL or
  record rule applies. See `sql-items.md`.
- On create, an item's `grid_x`, `grid_y`, `grid_w`, `grid_h` are replaced by an
  automatic size and position unless the context has `dd_skip_auto_layout`
  (source). Writes that change the type, model, or group-by repack the whole board
  (runtime); pass the same context on such writes, and remember `noupdate="1"` data is
  not rewritten by a module update, so fix an installed item with a write.
- Known defect (runtime): a KPI with `computation_mode` `model` and aggregation
  `sum` or `average` fails, because the addon calls `read_group` with the
  pre-Odoo-20 argument order. Count KPIs, formula and children KPIs over count
  KPIs, and every ORM item work. For amounts with a target, use a tile with
  `enable_target` and `dynamic.dashboard.target.line` records instead.
- Runtime check: a fixture dashboard with ORM tiles, a count KPI with target, a
  monthly bar, a pie with segment colour, a SQL item, and a many2one filter
  installed on a disposable database; all items computed without error and every
  `grid_*` value was kept.
- The built-in AI wizard calls an external LLM configured in Settings. It is not
  needed and not used by this skill.
- The JSON import wizard keeps only part of an export (no domain, no filters, no
  dashboard settings, layout replaced). Do not use it to deliver dashboards.

## Odoo 20 platform facts that matter here

- Data XML `<record>` accepts a `context` attribute, evaluated with `ref`
  available (source, `odoo/tools/convert.py`). Use it for `dd_skip_auto_layout`.
- Many2one and Many2many values for `ir.model` and `ir.model.fields` are set with
  `search=` domains in XML; resolve by technical names, never by numeric id.
- Security files use `security/ir.access.csv`; `ir.model.access.csv` no longer loads.
- `read_group` takes `(domain, groupby, aggregates)`; the addon already uses
  `formatted_read_group`, so no custom code is needed for ORM items.
- A manifest `license` must be an Odoo license selection value, not `MIT`.

## Groups

- `dynamic_dashboard_ai_nexgen.group_dashboard_user`: view dashboards.
- `dynamic_dashboard_ai_nexgen.group_dashboard_manager`: create and edit dashboards.
- `dynamic_dashboard_ai_nexgen.group_analysis_manager`: data marts (Python code).
- `dynamic_dashboard_ai_nexgen.group_dashboard_admin`: external connections.

Dashboards are visible to `group_ids` (default internal users); items to
`allowed_group_ids` when set. Every model has a multi-company rule.
