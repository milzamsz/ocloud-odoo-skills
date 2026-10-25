# Odoo 20.0 Migration Reference

Target-side notes verified against the local Odoo 20.0 Community snapshot and
licensed Enterprise archive.

- `_sql_constraints` is ignored at registry load (warning only); every
  constraint must become a `models.Constraint` object or it silently disappears.
- Route `type='json'` becomes `type='jsonrpc'`; `odoo/upgrade_code/18.1-02-route-jsonrpc.py`
  is the upstream rewriter.
- QUnit is removed; browser suites must move to Hoot.
- The legacy public widget registry is removed; website JavaScript must use
  `Interaction` classes.
- OpenUpgrade 20.0 is available locally only as a snapshot of OCA pull request
  6046 (commit `10f253d0290cfe9291771113b92c2d64edfa8020`, 2026-09-29), not an
  upstream release, plus local 19→20 and experimental 18→20 scripts. Treat
  per-module coverage as unaccepted until verified on a disposable copy.
- Enterprise: `account_accountant`, `account_reports`, `documents`, and
  `web_studio` are present in the archive; `l10n_id_efaktur` is absent, so an
  Indonesian e-Faktur dependency is a migration blocker until resolved.

No schema, accounting, or stock migration coverage is claimed beyond these
observations.
