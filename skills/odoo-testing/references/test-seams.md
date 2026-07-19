# Test Seams

Choose the narrowest seam that proves the public behavior. Add a broader seam
only for risk the narrow test cannot observe.

| Risk | Odoo 18 seam | Required assertion |
|---|---|---|
| ORM behavior, compute, constraint | `TransactionCase` | persisted value and rejected invalid input |
| Onchange/form behavior | `Form` from `odoo.tests` | user-visible onchange/default result |
| ACL or record rule | realistic user with `with_user` | allowed operation and `AccessError` denial |
| Multi-company | users/records in distinct companies | own-company success and cross-company denial |
| HTTP route | `HttpCase` | authentication, authorization, input, and response |
| JS component | QUnit in `web.assets_tests` | rendered behavior and failure state |
| Critical UI journey | tour via `HttpCase` | end-to-end business outcome |
| Cron | direct method call | batching, repeated-call idempotency, failure handling |
| Integration | adapter boundary with mocked remote | payload, retry, timeout, idempotency |
| Upgrade | representative pre-upgrade data | post-upgrade invariants and reconciliation |
| Query regression | `assertQueryCount` after warm-up | bounded query count for representative batch |

Odoo 18 `TransactionCase` uses savepoints for methods and does not commit;
shared records belong in `setUpClass`. Ordinary addon test cases receive
`standard` and `at_install` tags. Reserve `post_install` for behavior that
needs the installed registry or HTTP/UI, and tag it explicitly.

Verified official paths:

- `odoo/tests/common.py` — `TransactionCase`, `HttpCase`, `tagged`, default tags,
  and query-count support.
- `odoo/tests/form.py` — server-side form/onchange helper.
- `odoo/tests/tag_selector.py` — test-tag selection.
- `odoo/tests/shell.py` — separate at-install and post-install suites.

Fixture application:
`evals/fixtures/minimal-addon-18/ocloud_minimal_18/tests/test_minimal_item.py`
uses `TransactionCase` for a constraint and realistic user access. A form,
HTTP, JS, or tour test would add no coverage for that fixture and is therefore
intentionally absent.
