# Odoo 18.0 Community

Use only after context discovery confirms Odoo 18.0 Community.

## Verified baseline

Read-only local source evidence confirms `base`, `sale_crm`, `sale_stock`, `purchase_stock`, `stock_account`, `mrp_account`, and `l10n_id` are available in the observed 18.0 Community tree. Presence is not proof of installation or configuration in a target database.

## Edition boundary

Community evidence excludes Enterprise-only behavior. Do not recommend `web_enterprise`, `account_accountant`, or another Enterprise module unless edition evidence changes and the Enterprise reference is loaded.

## Application rule

Apply the version-neutral workflow in `SKILL.md`. Inspect target source, manifests, installed modules, ACLs, record rules, and company context before using version-sensitive APIs or business behavior. Differences not demonstrated by target evidence remain Unknown.

## Completion evidence

Record release/edition evidence, relevant module/source paths, exact tests, and unresolved deltas. A source-tree check alone does not prove installation, live access, or end-to-end behavior.
