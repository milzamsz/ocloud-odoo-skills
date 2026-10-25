# Odoo 20.0 Enterprise

Use only after context discovery confirms Odoo 20.0 Enterprise.

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
- Executed domain evidence: the repository fixture `domain-eval-20` installs
  and passes on disposable Odoo 20 Community and Enterprise databases, with
  one test per skill domain (its README maps tests to skills).
- `read_group`/`_read_group` take `(domain, groupby, aggregates)`; the old
  `(domain, fields, groupby)` order raises a granularity error.
- Manifest `license` must be an `ir.module.module` selection value; `MIT`
  installs but breaks module update, so declare `Other OSI approved licence`.
- JSON-2 `/json/2/<model>/<method>` is served by the auto-installed `rpc`
  addon (`auth='bearer'`, `bearer_scope='rpc'`, per-method read-only); the
  `web` addon's `/json/1/` route is the view-oriented variant.

## Skill-specific evidence

- Executed: `upgrade_code` rewriters produce the 20 constraint and `ir.access.csv` forms; manifest `license` `MIT` is rejected on update, so OCA-style manifests must use an accepted selection value.
- Local OCA 20 evidence is limited to the OpenUpgrade snapshot (OCA PR 6046 at commit `10f253d0290cfe9291771113b92c2d64edfa8020`, not a release). Other OCA 20.0 branches must be inspected upstream before a port is declared possible.
- OCA module ports to 20 must replace `_sql_constraints` with `models.Constraint` and `type='json'` with `jsonrpc`.

## Enterprise boundary (verified in the licensed archive)

`web_enterprise`, `account_accountant`, `account_reports`, `documents`,
`web_studio`, `sale_subscription`, `stock_enterprise`, `mrp_workorder`,
`pos_enterprise`, `quality_control`, `helpdesk`, `planning`, and `sign` are
present with `OEEL-1` manifests. `l10n_id_efaktur` is absent from this
archive. Enterprise evidence is licensed and read-only; never redistribute
proprietary source, and confirm installed modules on the target before relying
on any Enterprise application.

## Application rule

Apply the version-neutral workflow in `SKILL.md`. Odoo 20 support is
verified-experimental: source evidence plus two executed fixture addons on
disposable CE and EE databases (one representative flow per skill domain);
no OCA 20 coverage beyond the local OpenUpgrade snapshot.
Differences not demonstrated by target evidence remain Unknown.
