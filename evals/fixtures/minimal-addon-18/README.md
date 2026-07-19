# Minimal Odoo 18 Addon Fixture

This is an OCloud-authored, Community-only addon used to evaluate addon
development and testing guidance. It contains one model, an SQL constraint,
least-privilege ACL, list/form/action/menu XML, and transactional Odoo tests.
No Odoo or third-party code is copied.

## Expected verification

Use only a disposable Odoo 18 database. Add this directory to `addons_path`,
then install and test with the environment's normal wrapper. The equivalent
upstream command shape is:

`odoo-bin -d <disposable-db> -i ocloud_minimal_18 --test-enable --test-tags /ocloud_minimal_18 --stop-after-init`

Record the exact local wrapper, database provenance, exit status, and relevant
test summary. This repository's static checks verify fixture coherence; they do
not claim that an Odoo database run occurred.

Expected behavior:

- installation loads ACL before views;
- an internal user can create and update an item;
- the same user cannot delete it;
- quantity must be non-negative;
- list and form views load under Odoo 18 `<list>` syntax.

## Verified run

On 2026-07-19 this fixture was installed and tested against the local Odoo
18 Community source in `odoo-dev/environments/odoo18ce` using a uniquely named
disposable PostgreSQL database, dropped automatically after the run.

The direct Odoo command used the environment test config, added this fixture
root to `addons_path`, installed `ocloud_minimal_18`, selected
`/ocloud_minimal_18` test tags, and stopped after initialization.

Result: exit code 0; 3 test methods completed with 0 failures and 0 errors.
