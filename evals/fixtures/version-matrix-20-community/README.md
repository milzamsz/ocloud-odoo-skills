# Odoo 20.0 Community version evidence

Synthetic evaluation fixture backed by read-only inspection of
`/home/milzam/Workspace/odoo-dev/environments/odoo20ce/odoo` and the official
Odoo 20.0 documentation indexes.

- Release series: `20.0` (`odoo/odoo/release.py` reports `version_info = (20, 0, 0, FINAL, 0, '')`).
- Edition: Community. The inspected tree does not contain `addons/web_enterprise`
  or `addons/account_accountant`. This is evidence about this local source tree,
  not proof of product licensing or installed modules in a target database.
- Observed Community modules: `base`, `web`, `sale`, `sale_crm`, `sale_stock`,
  `purchase`, `purchase_stock`, `stock`, `stock_account`, `mrp`, `mrp_account`,
  `point_of_sale`, `account`, `l10n_id`, `bus`, and `mail`.
- The source checkout has no `.git` metadata. No upstream commit is asserted.
  The following SHA-256 hashes identify the inspected version and selected
  module manifests; hashes are not proof of upstream provenance:

  | Relative path under `.../odoo` | SHA-256 |
  |---|---|
  | `odoo/release.py` | `35c63174c5ffefa2693d4e6b6fd018d651179031d432513074ed06d6d6d494bb` |
  | `odoo/addons/base/__manifest__.py` | `09aa87b3eccd58a714e6c9520736ba04d8a9b0b3b3e53221437f89460a6df65f` |
  | `addons/web/__manifest__.py` | `8a78d282bcdd20d649bfa00c6c1180fa242dbc033f92c4d0d78d651068f00856` |
  | `addons/sale/__manifest__.py` | `6d5ef0d7b79ca0be7cb3349b5730c048772a01cb9ffc5fd4d9d3807c5aaeae5b` |
  | `addons/sale_crm/__manifest__.py` | `a6d83d9aa81122ad1d0818c268ff358320c1e1bc65172bcad809efa8a584fb67` |
  | `addons/sale_stock/__manifest__.py` | `49cbf2f136ac318079a8183414c3ae5646dc6af3ae61d4ad9c8940eb9bd93741` |
  | `addons/purchase/__manifest__.py` | `c47bd359caa677b42c8b2ee0f702aa533bad488bed43438cb32bac2a55e76588` |
  | `addons/purchase_stock/__manifest__.py` | `c5a2b06aeca2a5d98a857c0fbb3165d7f4391414976b6d533d3cd7c0fb60dac0` |
  | `addons/stock/__manifest__.py` | `5984d9b668fcb8d271b16736da8cba9a7c606a80972d20fcd41e4795c37b3af2` |
  | `addons/stock_account/__manifest__.py` | `0f8424ae748ed07778753bcf8330b3479217d72b5abfe438c7a17ad3d28cd78d` |
  | `addons/mrp/__manifest__.py` | `2d865d46fef465f7b7379dec6eda4a7d47bf4bf7399e023033140a4bb088f7ed` |
  | `addons/mrp_account/__manifest__.py` | `bbf34daed3a3580aec05a1f03f9c7536cc18c4abcf7a57d2715e18f56619a39c` |
  | `addons/point_of_sale/__manifest__.py` | `eb2bdb691527250bfd2a69d4de1d5fabe67cc5d03dcd681a1779f826a6769f77` |
  | `addons/account/__manifest__.py` | `44e871598c83615f67b9ef846fbfa8db240db3f8618fcae917be1aea64fe488b` |
  | `addons/l10n_id/__manifest__.py` | `a6c4d69131a3ff8f9f5807fbdafeefc4b1b6849c88b68d1a952cb6212b58a278` |
  | `addons/bus/__manifest__.py` | `065fe7d93966ae876fd9dfc3e98c1de2f0f41f583e8b393d86c9fe3cb8dc6040` |
  | `addons/mail/__manifest__.py` | `dc0dd179b2a868c643cfa9333ee9a1c495305de5bac6688c745481b34be4ab96` |
- Official references consulted: `https://github.com/odoo/odoo/tree/20.0`,
  `https://www.odoo.com/documentation/20.0/developer.html`, and
  `https://www.odoo.com/documentation/20.0/applications.html`. Only their
  landing/index pages were inspected at the time this fixture was prepared;
  individual feature pages must be checked before making workflow-specific claims.
- No source code, credentials, database data, client data, or proprietary
  Enterprise content is copied here.
- Module presence does not prove configuration, authorization, installation,
  runtime behavior, migration readiness, or parity with earlier releases.

Expected behavior: select Odoo 20.0 Community only when exact target evidence
confirms it; preserve the Community/Enterprise boundary; use the matching
skill-specific reference; clearly separate source evidence from target
installation/configuration and behavioral claims; and require target-specific
executable checks before completion claims.
