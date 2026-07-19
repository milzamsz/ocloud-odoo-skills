# Odoo 18 Notes

Supported baseline: Odoo 18 Community. Enterprise behavior requires separate
licensed source evidence and must not be inferred from Community.

## Addon shape

- A minimal installable addon needs `__manifest__.py`, package imports, declared
  dependencies, and every data file listed in dependency order.
- Models, ACL CSV, XML views, and tests are ordinary addon files; test modules
  must be imported by `tests/__init__.py`.
- Odoo's test loader assigns `standard` and `at_install` to normal
  `TransactionCase` classes. Use `tagged('-at_install', 'post_install')` only
  when the behavior genuinely requires a fully installed registry or HTTP/UI.
- `TransactionCase` runs test methods under savepoints within a transaction and
  closes without committing. Put shared setup in `setUpClass`.
- Import the form helper from `odoo.tests`; the compatibility import from
  `odoo.tests.common` emits a deprecation warning in 18.

## Version-sensitive syntax

- Use `<list>` for list views and `list,form` for the corresponding action.
- Use direct Python expressions in view modifiers such as `invisible` and
  `readonly`; verify inherited targets against the actual Odoo 18 architecture.
- Declare test assets in manifest asset bundles only when JS/QUnit/tour coverage
  exists.

Verified official source paths in
`environments/odoo18ce/odoo`:

- `odoo/tests/common.py` and `odoo/tests/form.py`
- `odoo/tests/tag_selector.py`
- `odoo/addons/test_new_api/__manifest__.py`
- `odoo/addons/base/views/*.xml`

The installable clean-room example is
`evals/fixtures/minimal-addon-18/ocloud_minimal_18`.
