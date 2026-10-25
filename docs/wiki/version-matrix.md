# Version and edition matrix

How a skill claims an Odoo version and edition, and the verified differences
an agent most often gets wrong. Source of truth:
[../../sources/VERSION-MATRIX.yaml](../../sources/VERSION-MATRIX.yaml),
`validate_version_claims()` in [../../scripts/validate_repository.py](../../scripts/validate_repository.py),
[../VERSION-EVIDENCE.md](../VERSION-EVIDENCE.md),
[../../docs/adr/0004-version-aware-references.md](../adr/0004-version-aware-references.md).

## Cells

A cell is one Odoo major version in one edition, such as `20.0-enterprise`.

| Cell | Status |
|---|---|
| 17.0 Community / Enterprise | verified-experimental |
| 18.0 Community | stable (primary baseline) |
| 18.0 Enterprise | verified-experimental |
| 19.0 Community / Enterprise | verified-experimental |
| 20.0 Community / Enterprise | stable |

Statuses: `stable` and `verified-experimental` are claimable; `advisory` and
`blocked` are not. Read the live file before quoting this table.

## What a claim needs

For every `(version, edition)` pair a skill's frontmatter yields (see
[skill-anatomy.md](skill-anatomy.md#frontmatter)), the validator requires:

1. The cell exists in `VERSION-MATRIX.yaml` with a claimable status.
2. Every `source_ids` entry of the cell is registered in `sources/SOURCES.yaml`.
3. The cell's `fixture` directory exists under `evals/fixtures/`.
4. The skill has `references/odoo-<major>-<edition>.md`, for example `references/odoo-20-community.md`.
5. `evals/outcome/cases.yaml` has a case with that `skill`, `odoo_version`
   (a quoted string such as `'20.0'`), and `odoo_edition`. A missing
   `odoo_edition` counts as `community`.

Adding a whole new cell, such as Odoo 21, is a workflow of its own:
[workflows.md](workflows.md#add-an-odoo-version-or-edition-cell).

## Evidence rules

- Edition is never inferred from installed source alone. Enterprise needs
  edition evidence such as `web_enterprise` installed or the version suffix.
- Source presence is not runtime proof. Say "present in source" unless a
  disposable database run or live read proved behavior.
- Enterprise source is licensed. Record fingerprints and observations, never
  copy it into the repository.

## Verified Odoo 20 differences

Taken from the per-skill `references/odoo-20-*.md` files and
[../../skills/odoo-version-upgrade/references/odoo-20.md](../../skills/odoo-version-upgrade/references/odoo-20.md).
For 17 to 19, no API deltas are recorded beyond module presence; check the
target source.

| Area | Odoo 20 fact |
|---|---|
| ORM | The ORM is the `odoo/orm/` package. Declare `models.Constraint`; `_sql_constraints` is ignored with a warning. |
| Access | `ir.model.access` is gone. Use `security/ir.access.csv` with columns `id,name,model_id,group_id/id,operation,domain`, where `operation` is a subset of `crud`. |
| Routes | JSON routes use `type='jsonrpc'`. |
| External API | JSON-2 is `POST /json/2/<model>/<method>` in the auto-installed `rpc` addon, with an API key as bearer token, scope `rpc`. The `web` addon's `/json/1/…` is view-oriented, not the integration API. |
| Grouping | `read_group(domain, groupby, aggregates)`; the private `_read_group` uses the same order. |
| Manifest | `license` must be one of Odoo's selection values; `MIT` fails on module update. |
| Views | `<list>` only; no `<tree>`. |
| JavaScript | OWL 3.0.0. Hoot replaces QUnit. Public website code uses `Interaction` classes; the public widget registry is gone. |
| Stock and purchase | `stock.reference` replaces `procurement.group`. Purchase lines use `tax_ids`. `po_lead` is gone. |
| Indonesia | `l10n_id_efaktur_coretax` replaces `l10n_id_efaktur` in both editions. |
| Edition marker | At runtime `/web/webclient/version_info` reports `20.0+e` only when Enterprise is loaded, because `web_enterprise` patches the version. The source `release.py` always shows an empty suffix. |
| Live access | Non-admin users get 403 on technical models such as `ir.model`, `ir.model.fields`, `ir.access`, and `ir.cron`. |
| Timestamps | `write_date` is serialized to whole seconds over the APIs. |

`odoo/upgrade_code/` in the Odoo 20 source ships rewriters for several of
these, for example the route and access-file changes.
