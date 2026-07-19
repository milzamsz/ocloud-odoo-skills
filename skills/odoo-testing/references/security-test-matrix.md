# Security Test Matrix

Test authorization at the ORM or route boundary, not only whether a button is
hidden. Construct the smallest matrix relevant to the feature.

| Actor/context | Read | Create | Write | Unlink | Special action |
|---|---:|---:|---:|---:|---:|
| intended group, own company | expected allow/deny | expected | expected | expected | expected |
| internal user without group | deny unless explicitly public-to-users | deny | deny | deny | deny |
| intended group, other company | deny for company-owned data | deny or force own company | deny | deny | deny |
| portal/public | deny unless explicitly designed | deny | deny | deny | deny |
| superuser | setup only, not proof | setup only | setup only | setup only | setup only |

Rules:

- Use `with_user` and, where relevant, an explicit allowed-company context.
- Invalidate cached fields before a denial assertion when prior superuser reads
  could mask the operation being tested.
- Assert `AccessError` (or the exact designed exception), and assert that denied
  creates/writes leave no changed data.
- ACL tests must cover operations; record-rule tests must cover record sets.
- For company-owned records, prove both visibility and relational company
  consistency. `check_company=True` does not replace a record rule.
- Add invalid-state and repeated-call rows for public model methods, cron, or
  integration callbacks.
- Add CSRF/authentication cases for state-changing routes; UI `groups` and
  modifiers are not server-side security.

Verified Odoo 18 CE evidence:

- `odoo/addons/test_access_rights/tests/test_ir_rules.py` uses realistic users,
  cache invalidation, and `AccessError` assertions for record rules.
- `odoo/addons/test_new_api/tests/test_company_checks.py` exercises company
  consistency and unauthorized allowed-company contexts.
- `odoo/tests/common.py` supplies transactional cases and user-aware
  environments.

The minimal fixture intentionally grants create/read/write but denies unlink;
its tests prove the allowed create and denied unlink as a non-superuser.
