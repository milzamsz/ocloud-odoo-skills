# Odoo 19.0 Enterprise

Use only after context discovery confirms Odoo 19.0 Enterprise.

## Verified baseline

Read-only local source evidence confirms `base`, `sale_crm`, `sale_stock`, `purchase_stock`, `stock_account`, `mrp_account`, and `l10n_id` are available in the observed 19.0 Enterprise tree. Presence is not proof of installation or configuration in a target database.

## Edition boundary

Enterprise evidence is licensed and read-only. Confirm installed modules; `web_enterprise` and `account_accountant` are edition markers, not authorization or proof that every Enterprise application is installed. Never redistribute proprietary source.

## Application rule

Apply the version-neutral workflow in `SKILL.md`. Inspect target source, manifests, installed modules, ACLs, record rules, and company context before using version-sensitive APIs or business behavior. Differences not demonstrated by target evidence remain Unknown.

## Completion evidence

Record release/edition evidence, relevant module/source paths, exact tests, and unresolved deltas. A source-tree check alone does not prove installation, live access, or end-to-end behavior.
