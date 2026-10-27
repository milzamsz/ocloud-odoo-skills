# Odoo 20.0 Migration Reference

Target-side notes verified against the local Odoo 20.0 Community snapshot and
licensed Enterprise archive.

- `_sql_constraints` is ignored at registry load (warning only); every
  constraint must become a `models.Constraint` object or it silently disappears.
- Route `type='json'` becomes `type='jsonrpc'`; `odoo/upgrade_code/18.1-02-route-jsonrpc.py`
  is the upstream rewriter.
- `ir.model.access` is removed; port `security/ir.model.access.csv` to `security/ir.access.csv` (`operation` letters, optional `domain`); `odoo/upgrade_code/19.4-00-ir-access.py` automates it.
- OWL 3.0.0; `odoo/upgrade_code/owl3-migration.py` rewrites OWL 2 components and templates.
- QUnit is removed; browser suites must move to Hoot.
- `procurement.group` is removed in favor of `stock.reference` and `reference_ids`; drop or remap any `group_id` or `procurement_group_id` usage. `purchase.order.line.taxes_id` is renamed `tax_ids`, and `po_lead` is gone.
- The legacy public widget registry is removed; website JavaScript must use
  `Interaction` classes.
- OpenUpgrade 20.0 is available locally only as a snapshot of OCA pull request
  6046 (commit `10f253d0290cfe9291771113b92c2d64edfa8020`, 2026-09-29), not an
  upstream release, plus local 19→20 and experimental 18→20 scripts. Treat
  per-module coverage as unaccepted until verified on a disposable copy.
- Enterprise: `account_accountant`, `account_reports`, `documents`, and
  `web_studio` are present in the archive. The legacy `l10n_id_efaktur` module
  is replaced by `l10n_id_efaktur_coretax` in both editions, so a dependency
  on the old module must be remapped during the port.

## Observed in an 18 Enterprise → 19 → 20 Community rehearsal (2026-10)

One production-size database, upgraded twice from the same backup with identical
snapshots; each item cost at least one failed run.

- A module named `studio_customization` is reserved in 20 for Studio exports:
  `-u all` skips it. Rename the module (and its XML IDs) on the source copy before
  the hops.
- Stored selection values that 20 dropped survive OpenUpgrade and break business
  flows later, e.g. `product.template.tracking = 'none'` (now empty) and payment
  state `in_process`. Compare every stored value with the field's 20 selection
  after the hop and map them in an end script.
- Payment methods become provider-owned. The upstream payment end script only
  remaps to methods created by module data, and module data creates none where
  the 19 XML ID already existed (`noupdate`). Wire transfer and cash on delivery
  providers therefore end with no method: checkout and the backend stop offering
  them. Fix in a project `payment` end script that sorts before the upstream one:
  copy each legacy method onto its *custom* providers only (copying onto gateway
  providers fails on brand/primary methods) and move the module XML ID onto the
  copy. Also repoint custom providers from the 19 view
  `payment_custom.redirect_form` to `payment.generic_redirect_form`; otherwise
  the obsolete view cannot be deleted and the checkout flow has no form.
- Modules merged in 20 (e.g. `website_sale_collect_wishlist`) leave module
  records with no source. An auto-install trigger later flags them
  `to install`, and every subsequent install logs "inconsistent states". Set
  such records `uninstallable`.
- Owl template inheritance (`t-inherit` + xpath) is applied in the browser only:
  a stale xpath passes install, upgrade, and view validation, then fails at
  runtime. Check every Owl xpath statically against the 20 sources, including
  core extensions of the same parent.
- Website assets that a theme copied per website keep 19 paths (e.g. the ripple
  effect moved from `js/content/` to `interactions/`) and log "Could not get
  content" on every bundle.

No schema, accounting, or stock migration coverage is claimed beyond these
observations.
