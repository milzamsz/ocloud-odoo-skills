# Upgrade 17 → 18 clean-room fixture

This OCloud-authored fixture contains minimal source and target addon snippets.
It is intentionally not a runnable database migration and copies no Odoo,
Enterprise, OCA, or OpenUpgrade code.

## Material changes

- `oca.upgrade.sample.legacy_reference` becomes `external_reference`.
- `oca_upgrade_sample.view_upgrade_sample_form` becomes
  `oca_upgrade_sample.upgrade_sample_form_view`.
- `expected-mapping.yaml` states the evidence a migration plan must preserve.

## Expected plan

Separate:

1. code changes (Python and view references);
2. schema preservation/field rename;
3. data transformation assertions;
4. XML-ID mapping preserving the existing view record;
5. configuration and integration reference updates;
6. functional, accounting, and inventory reconciliation, marking irrelevant
   domains explicitly with evidence.

The evaluator checks planning and reconciliation behavior only. It must not run
Odoo, OpenUpgrade, SQL, module upgrades, or any database-changing command.
