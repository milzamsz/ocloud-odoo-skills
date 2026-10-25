# Version and Edition Evidence

Date: 2026-10-07

This document records source-level evidence for the supported target cells. It
contains no credentials, database data, client data, or proprietary Enterprise
source.

| Cell | Read-only environment | Registered sources | Status |
|---|---|---|---|
| 17.0 Community | `environments/odoo17ce` | `odoo-17-ce-source` | verified-experimental |
| 17.0 Enterprise | `environments/odoo17ee` | `odoo-17-ce-source`, `odoo-17-ee-local-evidence` | verified-experimental |
| 18.0 Community | `environments/odoo18ce` | `odoo-18-ce-source` | stable |
| 18.0 Enterprise | `environments/odoo18ee` | `odoo-18-ce-source`, `odoo-18-ee-local-evidence` | verified-experimental |
| 19.0 Community | `environments/odoo19ce` | `odoo-19-ce-source` | verified-experimental |
| 19.0 Enterprise | `environments/odoo19ee` | `odoo-19-ce-source`, `odoo-19-ee-local-evidence` | verified-experimental |
| 20.0 Community | `environments/odoo20ce` | `odoo-20-ce-source`, `odoo-20-developer`, `odoo-20-applications` | stable |
| 20.0 Enterprise | `libraries/odoo-enterprise/odoo_20.0+e.20261008` (licensed archive) | `odoo-20-ce-source`, `odoo-20-ee-local-evidence` | stable |

## Observed source facts

- Release metadata matches each inspected environment's configured major version.
- The inspected Odoo 20.0 Community tree reports `(20, 0, 0, FINAL, 0, '')` in `odoo/odoo/release.py` and contains the modules enumerated in `evals/fixtures/version-matrix-20-community/README.md`.
- The Odoo 20.0 environment tree has no Git metadata; that fixture records SHA-256 hashes of the release file and selected manifests. These hashes identify the snapshot but do not establish its upstream origin.
- In the inspected Odoo 20.0 Community tree, `addons/web_enterprise` and `addons/account_accountant` are absent. This is a local source-tree observation only.
- The Odoo 20.0 Enterprise archive reports the same release tuple, carries `web_enterprise`, `account_accountant`, and `account_reports` with `OEEL-1` manifests, and lacks `l10n_id_efaktur`; `evals/fixtures/version-matrix-20-enterprise/README.md` records its SHA-256 fingerprints. Only the archive was used as evidence.
- Across both Odoo 20 trees: the ORM is the `odoo/orm/` package and `_sql_constraints` is ignored with a warning, `odoo/http/` is a package with JSON routes typed `jsonrpc`, the JSON-2 API is `/json/1/<path>` with bearer API keys, Hoot replaces QUnit, and the public `Interaction` layer replaces the legacy public widget registry.
- Executed evidence for Odoo 20: the clean-room fixture `evals/fixtures/minimal-addon-20` was installed with its tests on fresh disposable databases on both the Community snapshot and the Enterprise instance (addons path including the licensed archive) on 2026-10-25, and the databases were dropped afterwards; its README records the commands and summaries. The run also established that `ir.model.access` no longer exists on 20 and is replaced by `ir.access` with `security/ir.access.csv`.
- Executed domain evidence for Odoo 20: `evals/fixtures/domain-eval-20` (one test per skill domain: sales, purchase, inventory, accounting, Indonesian chart, POS, manufacturing, report rendering, portal, access control, metadata reads, automation, JSON-2 bearer API over HTTP) installed and passed on disposable Community (132 modules) and Enterprise (220 modules, `web_enterprise` and `account_accountant` installed) databases on 2026-10-25; both were neutralized and dropped. The runs surfaced the `read_group` argument order, the rejected `MIT` manifest license on update, and the `rpc` addon hosting JSON-2. `odoo-bin upgrade_code` rewriters were executed on a scratch copy of the 18 fixture.
- Skill-level Odoo 20 evidence: each of the 23 version-claiming skills was executed on its Community and Enterprise outcome case by a fresh agent session and graded by a separate session against required findings and prohibited actions; 46 of 46 pass (`docs/EVALUATION-SUMMARY-ODOO-20.md`); human review passed (milzamsz, 2026-10-25).
- OCA 20.0 evidence is limited to a local OpenUpgrade snapshot of OCA pull request 6046 (`openupgrade-20-local-snapshot`), which is not an upstream release.

These facts establish a source baseline only. They do not prove that a module
is installed, configured, licensed for a particular user, accessible through
ACLs/record rules, or behaviorally identical across releases.

## Claim chain

For every metadata claim:

1. the cell is claimable in `sources/VERSION-MATRIX.yaml`;
2. every matrix source ID exists in `sources/SOURCES.yaml`;
3. the skill contains `references/odoo-<major>-<edition>.md`;
4. the matrix fixture exists;
5. an outcome case covers the skill, version, and edition.

`scripts/validate_repository.py` enforces this chain. Stable promotion still
requires clean-profile regression and named human Odoo review.

## Enterprise handling

Enterprise evidence is obtained through licensed, read-only local inspection.
Only behavioral deltas and module gates may be written here. Enterprise source
code, proprietary text, private URLs, and client data must not be copied.
