# Odoo 20 Notes

Only verified material differences from the Odoo 18 baseline belong here.

- Constraints: declare `models.Constraint` (see `odoo/orm/table_objects.py`);
  a `_sql_constraints` list is ignored with a registry warning.
- Routes: JSON routes use `type='jsonrpc'`; `odoo/upgrade_code/18.1-02-route-jsonrpc.py`
  rewrites the old value.
- Views: `<list>` and `list,form` only, unchanged from 18 and 19.
- Tests: Hoot only for browser tests; `from odoo.tests import Form` unchanged.
- Public JavaScript: `Interaction` layer; the legacy public widget registry is gone. OWL is 3.0.0.
- Access: `security/ir.access.csv` (`id,name,model_id,group_id/id,operation,domain`, operation such as `cru`) replaces `ir.model.access.csv`; the old model does not exist and the old CSV fails to load.
- Executed evidence: the repository fixture `minimal-addon-20` installs and its tests pass on disposable 20 Community and Enterprise databases.

Both the Community snapshot and the licensed Enterprise archive show these
facts. No executed Odoo 20 module suite backs them.
