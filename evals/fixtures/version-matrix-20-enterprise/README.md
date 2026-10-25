# Odoo 20.0 Enterprise version evidence

Synthetic evaluation fixture backed by read-only inspection of the licensed
archive `$ODOO_DEV_ROOT/libraries/odoo-enterprise/odoo_20.0+e.20261008`
(tree `odoo-20.0+e.20261008/odoo`). Only that archive was used as evidence; no
instance-local custom addon was consulted.

- Release series: `20.0` (`odoo/release.py` reports `version_info = (20, 0, 0, FINAL, 0, '')`).
- Edition: `enterprise`. `addons/web_enterprise`, `addons/account_accountant`, and
  `addons/account_reports` are present with `OEEL-1` manifests. `documents`,
  `web_studio`, `sale_subscription`, `stock_enterprise`, `mrp_workorder`,
  `pos_enterprise`, `quality_control`, `helpdesk`, `planning`, and `sign` are
  also present. `l10n_id_efaktur` is absent from this archive.
- Core parity with the Community snapshot: `odoo/orm/table_objects.py`
  (`models.Constraint`), `<list>` views only in `base`, Hoot present, QUnit
  absent, public `Interaction` layer present, legacy public widget absent.
- The archive has no `.git` metadata. SHA-256 fingerprints identify the
  inspected files; hashes are not proof of upstream provenance:

  | Relative path under `.../odoo` | SHA-256 |
  |---|---|
  | `odoo/release.py` | `629060bdefc2ab3b644fecef82ea214656ebc3a564f5660ec24e1edc832de65f` |
  | `addons/web_enterprise/__manifest__.py` | `70eb191985830a8970b1c36f46a779aeb9f6779e461ca7f7e631102f4a61f14c` |
  | `addons/account_accountant/__manifest__.py` | `7c752fa8edabe1f1112a732a2fb99fa347b797ad799225325b2f8d2a8a90d98c` |
  | `addons/account_reports/__manifest__.py` | `a4e8c76d9cca95a5303e19175149d47ece9c8570c1cb119f6cb604328227be17` |
- No source code, credentials, database data, client data, or proprietary
  Enterprise content is copied here.
- Module presence does not prove licensing state, installation, configuration,
  authorization, runtime behavior, or parity with earlier releases.

Expected behavior: select Odoo 20.0 Enterprise only when exact target evidence
confirms both the release and a licensed Enterprise marker; preserve the
Community/Enterprise boundary; use the matching skill-specific reference; and
require target-specific executable checks before completion claims.
