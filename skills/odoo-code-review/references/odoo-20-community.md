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

## Skill-specific evidence

- Flag `_sql_constraints` (silently ignored), `type='json'` routes, `<tree>` views, QUnit suites, and legacy public widgets as 20 incompatibilities with source citations.
- Review bearer-scoped `/json/1/` usage for read-only intent and API-key handling.

## Community boundary

The Community snapshot contains no `web_enterprise`, `account_accountant`, or
`account_reports`. Do not infer Enterprise from business terminology; confirm
the edition marker on the target.

## Application rule

Apply the version-neutral workflow in `SKILL.md`. Odoo 20 support is
verified-experimental: source evidence only, no executed module suite, no
runtime database, and no OCA 20 coverage beyond the local OpenUpgrade snapshot.
Differences not demonstrated by target evidence remain Unknown.
