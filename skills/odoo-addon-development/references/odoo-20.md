# Odoo 20 Notes

Only verified material differences from the Odoo 18 baseline belong here.

- Constraints: declare `models.Constraint` (see `odoo/orm/table_objects.py`);
  a `_sql_constraints` list is ignored with a registry warning.
- Routes: JSON routes use `type='jsonrpc'`; `odoo/upgrade_code/18.1-02-route-jsonrpc.py`
  rewrites the old value.
- Views: `<list>` and `list,form` only, unchanged from 18 and 19.
- Tests: Hoot only for browser tests; `from odoo.tests import Form` unchanged.
- Public JavaScript: `Interaction` layer; the legacy public widget registry is gone.

Both the Community snapshot and the licensed Enterprise archive show these
facts. No executed Odoo 20 module suite backs them.
