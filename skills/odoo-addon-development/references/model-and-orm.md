# Model and ORM

## Odoo 18 CE evidence

Use the ORM as the transaction and authorization boundary. Verify unfamiliar
behavior in the target checkout rather than relying on cross-version memory.

- A model is registered through `models.Model` with `_name`, or extends an
  existing model with `_inherit`. Import every model module from `models/__init__.py`.
- Declare every input read by a stored or non-stored compute in `@api.depends`;
  compute over `self` as a recordset and assign the field for every record.
- Prefer recordset operations and batched `create`/`write` inputs. Search or
  browse outside loops; prefetch cannot rescue a new query issued per record.
- Use `@api.constrains` for invariants that require ORM values and SQL
  constraints for database-level invariants. Test both rejection and valid
  updates.
- ACLs grant model operations and record rules restrict records. Neither is a
  substitute for the other; exercise the operation as a non-superuser.
- For company-owned records, define `company_id`, use company-aware relational
  checks where appropriate, and add record rules plus cross-company tests.
  `_check_company_auto` and `check_company=True` check relational consistency;
  they do not create visibility rules.
- `sudo()` changes the security context. Keep any justified use narrow and
  restore the intended user before returning records or performing later work.
- Do not commit manually in business code. Let the request/test transaction own
  commit and rollback unless a documented framework boundary requires otherwise.

Verified official source paths in the Odoo 18 CE checkout:

- `odoo/models.py` and `odoo/fields.py` — recordsets, field descriptors,
  compute dependencies, relational fields, and company checks.
- `odoo/addons/base/models/ir_model.py` and
  `odoo/addons/base/models/ir_rule.py` — ACL and record-rule enforcement.
- `odoo/addons/test_new_api/tests/test_company_checks.py` — company-consistency
  and allowed-company behavior exercised by Odoo's own tests.

See the registered Odoo 18 developer documentation in `sources/SOURCES.yaml`;
these notes are OCloud-authored paraphrases, not copied source.
