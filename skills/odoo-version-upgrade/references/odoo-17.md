# Odoo 17.0 Migration Reference

Advisory source-side context for the clean-room 17 → 18 fixture:

- preserve the source field `legacy_reference` by record identity before the
  Odoo 18 target replaces it with `external_reference`;
- preserve the existing view record while renaming XML ID
  `view_upgrade_sample_form` to `upgrade_sample_form_view`;
- inventory every installed custom/OCA module and its exact 17.0 branch before
  declaring target coverage;
- capture source counts, values, company scope, accounting/stock balances, and
  attachment/integration baselines before migration.

These are fixture-grounded migration obligations, not broad Odoo 17 API
compatibility claims. Verify additional deltas against exact source and target
branches.
