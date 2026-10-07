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
| 20.0 Community | `environments/odoo20ce` | `odoo-20-ce-source`, `odoo-20-developer`, `odoo-20-applications` | verified-experimental |

## Observed source facts

- Release metadata matches each inspected environment's configured major version.
- The inspected Odoo 20.0 Community tree reports `(20, 0, 0, FINAL, 0, '')` in `odoo/odoo/release.py` and contains the modules enumerated in `evals/fixtures/version-matrix-20-community/README.md`.
- The Odoo 20.0 environment tree has no Git metadata; that fixture records SHA-256 hashes of the release file and selected manifests. These hashes identify the snapshot but do not establish its upstream origin.
- In the inspected Odoo 20.0 Community tree, `addons/web_enterprise` and `addons/account_accountant` are absent. This is a local source-tree observation only.
- Existing Enterprise rows rely on their separate licensed local evidence; the Odoo 20.0 Community observation provides no Enterprise evidence.

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
