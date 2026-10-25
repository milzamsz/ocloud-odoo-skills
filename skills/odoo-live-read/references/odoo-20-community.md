# Odoo 20.0 Community

Use only after context discovery confirms Odoo 20.0 Community.

## Verified Odoo 20 source facts (both editions)

Read-only inspection of the local Odoo 20.0 Community snapshot and the licensed
Enterprise archive (fingerprints in the repository evaluation fixtures
`version-matrix-20-community` and `version-matrix-20-enterprise`). Source
presence is not proof of installation, licensing, configuration, or runtime
behavior.

- The ORM is the `odoo/orm/` package (`models.py`, split field modules,
  `table_objects.py`). `_sql_constraints` is no longer supported; the registry
  logs a warning (`odoo/orm/model_classes.py`) and `base` declares
  `models.Constraint` objects instead.
- `odoo/http/` is a package (`dispatcher.py`, `routing_map.py`). Route type
  `json` is rewritten to `jsonrpc` by `odoo/upgrade_code/18.1-02-route-jsonrpc.py`.
- The JSON-2 web API lives in `addons/web/controllers/json.py`: `/json/<path>`
  (`auth='user'`) and `/json/1/<path>` (`auth='bearer'`, `bearer_scope='rpc'`,
  read-only). API keys are the bearer credential.
- `base` views use `<list>` only; no `<tree>` architecture remains.
- Tests: `odoo/tests/form.py` and `Form` exported from `odoo.tests`, `tagged`,
  `HttpCase`. Hoot is the browser test library; QUnit is absent.
- Public JavaScript: the `Interaction` layer exists; the legacy public widget
  registry is absent.
- Operations: `odoo/modules/neutralize.py` plus per-module `data/neutralize.sql`
  files; `--workers` remains a server option.
- Reports: `ir_actions_report.py` keeps `_render_qweb_pdf` with wkhtmltopdf.
- `mail.template`, `base_automation`, and `ir.cron` are present.
- Access control: the `ir.model.access` model is gone; `ir.access`
  (`odoo/addons/base/models/ir_access.py`) is loaded from
  `security/ir.access.csv` with columns `id,name,model_id,group_id/id,operation,domain`,
  where `operation` is a subset of `crud` and `domain` optionally scopes the
  rule. `odoo/upgrade_code/19.4-00-ir-access.py` rewrites old CSVs.
- OWL is 3.0.0 (`addons/web/static/lib/owl/owl.js`); `odoo/upgrade_code/owl3-migration.py`
  is the upstream migration script. `18.1-00-sql-constraint.py` and
  `20.0-00-search-date-filters.py` rewrite constraints and search-view date
  filters.
- Executed evidence: the repository fixture `minimal-addon-20` installs and
  its tests pass on disposable Odoo 20 Community and Enterprise databases
  (see that fixture's README for the run record).

## Skill-specific evidence

- Bounded reads over JSON-2 go through `/json/1/<path>` (`bearer_scope='rpc'`, read-only); a key without that scope must fail the read, not be widened.

## Community boundary

The Community snapshot contains no `web_enterprise`, `account_accountant`, or
`account_reports`. Do not infer Enterprise from business terminology; confirm
the edition marker on the target.

## Application rule

Apply the version-neutral workflow in `SKILL.md`. Odoo 20 support is
verified-experimental: source evidence only, no executed module suite, no
runtime database, and no OCA 20 coverage beyond the local OpenUpgrade snapshot.
Differences not demonstrated by target evidence remain Unknown.
