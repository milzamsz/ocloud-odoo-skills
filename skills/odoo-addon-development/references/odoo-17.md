# Odoo 17 Notes

Only verified material differences from the Odoo 18 baseline belong here.

- Odoo 17 CE/EE view source uses `<tree>` and action `view_mode` values such as
  `tree,form`; Odoo 18 uses `list`. Verify at
  `environments/odoo17ee/odoo/odoo/addons/base/views/*.xml`.
- The compatibility import `odoo.tests.common.Form` is already marked deprecated
  in 17, but with `PendingDeprecationWarning`; prefer `from odoo.tests import
  Form` in code intended to move forward. Verified at
  `environments/odoo17ee/odoo/odoo/tests/common.py`.

No other 17-specific behavior is claimed by this reference. Inspect the target
17 source before backporting an Odoo 18 implementation.
