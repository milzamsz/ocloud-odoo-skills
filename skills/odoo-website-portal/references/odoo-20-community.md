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
- The JSON-2 model-method API is `/json/2/<model>/<method>` in the
  auto-installed `rpc` addon (`addons/rpc/controllers/json2.py`): `POST`,
  `auth='bearer'`, `bearer_scope='rpc'`, read-only detected per method. API keys
  are the bearer credential. The `web` addon's `/json/<path>` (`auth='user'`)
  and `/json/1/<path>` routes (`addons/web/controllers/json.py`) are the
  view-oriented variant, not the integration API.
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

- Executed: `_portal_ensure_token`, custom `access_url`, portal `/my` over HTTP, `ir.access` domain row for portal reads (`domain-eval-20`).
- `portal.mixin`, `CustomerPortal._document_check_access`, and `website.page` are present; public JavaScript must use `Interaction` because the legacy public widget registry is absent.

## Observed while building a theme + shop on Odoo 20 Community (2026-10)

Executed on an upgraded production copy; each point broke something first.

Themes and multi-website:
- In a module named `theme_*`, `<template>` and `<asset>` load as `theme.ir.ui.view` / `theme.ir.asset` (`odoo/tools/convert.py`); pages and menus are `theme.website.page` / `theme.website.menu`. They are copied only onto websites whose `theme_id` is the module, so other websites stay untouched. Apply with `ir.module.module.button_choose_theme()` under `website_id` context and a user in `website.group_website_restricted_editor`.
- Per-website setup belongs in `theme.utils._<theme>_post_copy(mod)` (`website/models/theme_models.py`); `enable_view` / `disable_view` toggle per-website copies.
- A new website gets its own `/` page that shadows the theme's `/` page; remove it in the post-copy hook. A `theme.website.menu` with `page_id` is cascade-deleted with that page, so give the home menu a URL only.
- `request.website` is gone in controllers; use `request.env.website`.
- The running server caches the domain → website lookup and asset bundle versions in memory: change `website.domain` through the ORM (SQL leaves the cache stale) and reload the theme module or restart after editing SCSS.
- Website SCSS compiles with libsass: modern `rgb(r g b / a)` syntax fails, and `px` values in `$o-website-values-palettes` (e.g. `btn-border-width`, `input-border-radius`) fail with "Incompatible units" — use `rem`.
- `backdrop-filter` on the header makes it the containing block of the fixed mobile off-canvas menu, which then widens the page on phones.

`website_sale` (native mechanisms that replaced custom code):
- Selling one stock product in packs: put pack UoMs (relative to the stock UoM) on the product's `uom_ids` and the stock UoM in `website.restricted_uom_ids`; the product page shows them as pills and `_get_main_uom()` picks the first.
- "Ask for price" products: `website.prevent_sale` with `prevent_sale_for = 'zero_price'` and a fixed price 0 on the website pricelist; the tile and product page then link to `website._get_contact_us_url()`, which can be overridden (e.g. to a WhatsApp link).
- Filtering by product tags needs the view `website_sale.filter_products_tags` active; only tags with `visible_to_customers` appear.
- `delivery.carrier.fixed_price` is stored on the carrier's product `list_price`: carriers sharing one delivery product overwrite each other's price. Writing `delivery_type` resets `allow_cash_on_delivery`; set it in a separate write.
- Checkout lists payment *methods*, deduplicated by `code`, and a provider without an active method is invisible. A custom provider also needs `redirect_form_view_id = payment.generic_redirect_form`. `payment.provider` has no `state` (use `is_live`, `is_published`, `active`); pricelist discount rules use `compute_price = 'discount'` with `price_discount`.
- Binary fields accept `odoo.tools.binary.BinaryBytes`, not raw bytes; `ir.config_parameter.get_param` is gone (typed getters such as `get_int`).

## Community boundary

The Community snapshot contains no `web_enterprise`, `account_accountant`, or
`account_reports`. Do not infer Enterprise from business terminology; confirm
the edition marker on the target.

## Application rule

Apply the version-neutral workflow in `SKILL.md`. Odoo 20 support is
verified-experimental: source evidence plus two executed fixture addons on
disposable CE and EE databases (one representative flow per skill domain);
OCA 20.0 branches exist upstream but are
mostly unported; all six installable OCA 20 modules with tests pass on both
editions (see the `odoo-oca-development` references).
Differences not demonstrated by target evidence remain Unknown.
