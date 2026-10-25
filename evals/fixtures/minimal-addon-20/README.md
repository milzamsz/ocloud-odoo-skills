# Minimal addon fixture (Odoo 20)

OCloud-authored, installable clean-room addon `ocloud_minimal_20` used as the
executable evidence for Odoo 20.0 Community and Enterprise claims. It is the
Odoo 18 fixture ported to the verified Odoo 20 conventions:

- `security/ir.access.csv` with columns `id,name,model_id,group_id/id,operation,domain`
  (the `ir.model.access` model and its CSV no longer exist in 20);
- a `models.Constraint` table object instead of a `_sql_constraints` list
  (which Odoo 20 ignores with a warning);
- `<list>` views and `list,form` action mode;
- `new_test_user` imported from `odoo.tests.common`.

## Runtime evidence (2026-10-25)

Installed with `-i ocloud_minimal_20 --test-enable --test-tags=/ocloud_minimal_20
--stop-after-init` on fresh disposable databases created for the run and
dropped afterwards. Addons path: the instance test configuration plus this
fixture directory. No existing database was touched.

| Cell | Instance | Result |
|---|---|---|
| 20.0 Community | `environments/odoo20ce` (local Community snapshot) | exit 0; `ocloud_minimal_20: 5 tests 0.08s 75 queries`; `0 failed, 0 error(s) of 3 tests` |
| 20.0 Enterprise | `environments/odoo20ee` (addons path includes the licensed `odoo_20.0+e.20261008` archive) | exit 0; `ocloud_minimal_20: 5 tests 0.08s 75 queries`; `0 failed, 0 error(s) of 3 tests` |

The constraint test logs an expected `bad query` error from `odoo.sql_db`
while the violation is raised inside `assertRaises`; that line is the proof
that the `models.Constraint` object was created on the table.

Evidence covers install, ACL load through `ir.access`, view parsing, the
constraint, and access-control tests for this addon only. It does not prove
behavior of any business application, migration path, or OCA module on 20.
