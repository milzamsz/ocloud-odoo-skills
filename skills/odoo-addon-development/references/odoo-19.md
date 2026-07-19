# Odoo 19 Notes

Only verified material differences from the Odoo 18 baseline belong here.

- Odoo 19 retains `<list>` and `list` action modes; the Odoo 18 fixture's view
  naming does not need a 17-style syntax branch. Verified at
  `environments/odoo19ce/odoo/odoo/addons/base/views/*.xml`.
- The `odoo.tests.common.Form` compatibility import still emits the Odoo 18
  deprecation warning; use `from odoo.tests import Form`. Verified at
  `environments/odoo19ce/odoo/odoo/tests/common.py`.

No additional 19 compatibility is claimed. Add a 19 regression fixture before
declaring the Odoo 18 minimal addon verified on 19.
