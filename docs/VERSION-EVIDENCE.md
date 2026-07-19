# Version and Edition Evidence

Date: 2026-07-20

This document records source-level evidence for the six supported target
cells. It contains no credentials, database data, client data, or proprietary
Enterprise source.

| Cell | Read-only environment | Registered sources | Status |
|---|---|---|---|
| 17.0 Community | `environments/odoo17ce` | `odoo-17-ce-source` | verified-experimental |
| 17.0 Enterprise | `environments/odoo17ee` | `odoo-17-ce-source`, `odoo-17-ee-local-evidence` | verified-experimental |
| 18.0 Community | `environments/odoo18ce` | `odoo-18-ce-source` | stable |
| 18.0 Enterprise | `environments/odoo18ee` | `odoo-18-ce-source`, `odoo-18-ee-local-evidence` | verified-experimental |
| 19.0 Community | `environments/odoo19ce` | `odoo-19-ce-source` | verified-experimental |
| 19.0 Enterprise | `environments/odoo19ee` | `odoo-19-ce-source`, `odoo-19-ee-local-evidence` | verified-experimental |

## Observed source facts

- Release metadata matches each environment's configured major version.
- The observed trees include `base`, `sale_crm`, `sale_stock`,
  `purchase_stock`, `stock_account`, `mrp_account`, and `l10n_id`.
- Community trees do not include `web_enterprise` or `account_accountant`.
- Enterprise trees include `web_enterprise` and `account_accountant`.

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
