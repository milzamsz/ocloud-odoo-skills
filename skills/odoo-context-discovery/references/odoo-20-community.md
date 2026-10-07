# Odoo 20.0 Community context discovery

Load only after repository/runtime evidence identifies the target as Odoo 20.0.
The content below is based on a local Community source snapshot and the official
Odoo 20.0 documentation indexes; it does not establish the identity or state of
a target database.

## Verified source boundary

- Local source root: `/home/milzam/Workspace/odoo-dev/environments/odoo20ce/odoo`.
- `odoo/odoo/release.py` reports `version_info = (20, 0, 0, FINAL, 0, '')`.
- This source tree has no `.git` metadata. Do not report a branch, commit, or
  clean/dirty Git state for it. Its release and selected manifest SHA-256
  fingerprints are recorded in
  `evals/fixtures/version-matrix-20-community/README.md`.
- The inspected Community tree contains modules including `base`, `web`,
  `account`, `sale`, `purchase`, `stock`, `mrp`, `point_of_sale`, `l10n_id`,
  `bus`, and `mail`. Module presence is not evidence that a target database
  installed, configured, licensed, or grants access to them.
- The inspected tree does not contain `addons/web_enterprise` or
  `addons/account_accountant`. Treat this only as a boundary observation about
  this local source snapshot, not as proof about every Odoo 20 product or
  database.

## Discovery procedure

1. Read project instructions and instance configuration without printing or
   copying credentials. Record the actual source/addons paths, database target,
   environment, and whether the source tree is a Git checkout.
2. Verify the actual source release from its own `odoo/odoo/release.py`; do not
   infer Odoo 20 solely from a directory name or config label.
3. Establish edition evidence independently. Inspect only authorized local
   source/module markers; do not infer Enterprise from a license field or
   Community from an application’s appearance.
4. For a live target, separately verify its reported version, edition, installed
   modules, company/context, authorization, and evidence freshness using
   authorized read-only mechanisms. Local source facts never substitute for
   live-target evidence.
5. Select Odoo 20 Community procedures only after exact version and edition are
   confirmed. If version evidence conflicts, stop version-specific guidance and
   report both observations plus the unresolved source of truth.
6. Apply target-specific tests before claiming that an addon installs, upgrades,
   or behaves correctly. The source evidence here does not include a disposable
   Odoo 20 database or an executed module suite.

## Sources and limits

- Odoo 20 Community source reference: <https://github.com/odoo/odoo/tree/20.0>
- Odoo 20 developer documentation index:
  <https://www.odoo.com/documentation/20.0/developer.html>
- Odoo 20 applications documentation index:
  <https://www.odoo.com/documentation/20.0/applications.html>

Only the documentation landing/index pages were inspected for this baseline.
Use relevant version-pinned pages and local Odoo 20 source before asserting a
feature-specific API or business workflow. No Odoo 20 Enterprise, OCA 20,
production runtime, or migration-path support is established here.
