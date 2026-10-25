# Domain evaluation fixture (Odoo 20)

OCloud-authored, installable clean-room addon `ocloud_domain_eval_20`. Its
Odoo tests exercise one representative flow per skill domain on Odoo 20 so
that each skill's Odoo 20 claim rests on executed behavior, not only on source
reading. Every test names the skills it backs.

## Runs (2026-10-25)

Fresh disposable databases, created for the run and dropped afterwards.
Addons path: the instance test configuration plus this fixture directory.

| Cell | Instance | Install | Test result |
|---|---|---|---|
| 20.0 Community | `environments/odoo20ce` | `-i ocloud_domain_eval_20` (132 modules) | first pass 16/17 (one test bug, see below); after fixing the test, `-u` rerun on the same database: `0 failed, 0 error(s) of 15 tests` |
| 20.0 Enterprise | `environments/odoo20ee` (addons path includes the licensed `odoo_20.0+e.20261008` archive) | `-i ocloud_domain_eval_20,web_enterprise,account_accountant` (220 modules; markers logged as installed) | same: `0 failed, 0 error(s) of 15 tests` after the `-u` rerun |

Both databases were then neutralized: `odoo-bin neutralize` left 1 active cron of 34 (CE) and 54 (EE), replaced the mail servers with one neutralization placeholder, and set `database.is_neutralized`. They were dropped with `odoo-bin db drop`.

## What each test proves (skill mapping)

| Test | Skills | Evidence |
|---|---|---|
| `test_release_and_edition_markers` | context-discovery, solution-design | `release.version_info[0] == 20`; `web_enterprise`/`account_accountant` installed on EE, absent on CE |
| `test_access_csv_constraint_and_portal_rule` | addon-development, testing, security-audit | `security/ir.access.csv` with `crud`/`r` rows and a domain row loads; `ir.model.access` is not in the registry; `models.Constraint` enforced; portal user reads own record, denied on another partner's |
| `test_sales_order_to_cash` | functional-sales, functional-inventory, code-tracing | confirm creates one delivery; assign, pick, validate; quant 5 → 3; invoice created and posted, untaxed 200 |
| `test_purchase_to_pay` | functional-purchase | confirm, receipt validated, vendor bill created and posted, untaxed 150 |
| `test_invoice_payment_and_reconciliation` | functional-accounting | receivable line debit equals total; payment register wizard; `payment_state` paid or in_payment |
| `test_indonesian_chart_loads` | indonesia-accounting | `try_loading("id", company)` installs > 50 accounts, taxes, IDR |
| `test_pos_session_open_and_close` | functional-pos | `open_ui` → `opening_control`; `set_opening_control` → `opened`; `close_session_from_ui` → `closed` |
| `test_manufacturing_order` | functional-manufacturing | BoM, MO confirm/assign, `qty_producing`, `button_mark_done` → done, component 10 → 8 |
| `test_report_renders_html` | reporting | `_render_qweb_html("sale.report_saleorder")` contains the order name |
| `test_portal_mixin_token_and_url` | website-portal | `_portal_ensure_token`, overridden `access_url`, a `website` record exists |
| `test_metadata_and_bounded_reads` | data-model-diagram, live-context, live-read | `ir.model.fields` relations for `sale.order`; `_read_group(domain, groupby, aggregates)`; bounded `search_read` |
| `test_server_action_automation_and_mail_template` | solution-design, integration-design | code server action runs; `base.automation` has `on_create_or_write`; `mail.template._render_field` |
| `test_project_task_timesheet` | (project and timesheet gap) | task and timesheet line, `effective_hours` 2.0 |
| `test_json2_requires_bearer_and_reads` (HttpCase) | integration-design, live-context, live-read, security-audit | `/json/2/res.partner/search_read` is 401/403 without a bearer key and returns one record with an `rpc`-scoped API key (route lives in the auto-installed `rpc` addon) |
| `test_portal_home_for_portal_user` (HttpCase) | website-portal | portal login, `/my` returns 200, unknown note id is not served |

## Odoo 20 facts the runs surfaced (now in the skill references)

- `read_group` and `_read_group` take `(domain, groupby, aggregates)`; the
  18-era `(domain, fields, groupby)` order raises
  `Granularity set on a no-datetime field`.
- The manifest `license` must be one of the `ir.module.module` selection
  values. `MIT` installs but fails on module update with
  `Wrong value for ir.module.module.license: 'MIT'`; use
  `Other OSI approved licence` for MIT code.
- `ir.model.access` is absent; `ir.access` rows carry `operation` letters and
  an optional `domain` (a portal-scoped row works without a record rule).
- JSON-2 (`/json/2/<model>/<method>`) is served by the auto-installed `rpc`
  addon with `auth='bearer'`, `bearer_scope='rpc'`, and per-method read-only
  detection; the `/json/1/` route in `web` is the view-oriented variant.
- `odoo-bin upgrade_code --script 18.1-00-sql-constraint` and
  `--script 19.4-00-ir-access` rewrite the Odoo 18 minimal fixture to exactly
  the hand-ported form, but the access CSV is appended after the views in the
  manifest `data` list (load-order convention broken); the full
  `--from 18.0 --to 20.0` chain aborts in `19.3-00-account-groups.py` when run
  against a single custom addon.

## Limits

One representative flow per domain, default configuration, no demo data,
no multi-company or multi-currency variants, no PDF rendering (HTML only),
no OCA module. The `-u` rerun reused the database created by the first
install; the first install itself succeeded on both editions.
