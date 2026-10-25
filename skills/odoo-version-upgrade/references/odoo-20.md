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

No schema, accounting, or stock migration coverage is claimed beyond these
observations.
