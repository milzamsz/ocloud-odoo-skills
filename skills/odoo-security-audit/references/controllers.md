# Controller Security

## Route contract

- Record route path, `type`, `auth`, methods, CSRF setting, CORS, and whether it
  reads or mutates state.
- `auth='public'` can execute for unauthenticated visitors. `auth='user'`
  authenticates a user but does not authorize that user to a requested record.
- Use explicit methods. State changes must not use GET.

## CSRF and external callbacks

- In Odoo 18 source, HTTP routes enable CSRF by default for unsafe methods;
  JSON routes disable it by default. Review the effective route, not an assumed
  universal default.
- Treat `csrf=False` as a trust-boundary decision, not automatically a defect.
  A legitimate external callback needs an alternative such as a verified
  signature, narrow credential, timestamp/replay control, and idempotency.
- Browser/session mutations should retain CSRF protection and include the
  expected token.

## Object authorization and elevation

- Parse and validate caller input, browse the narrow record, and enforce
  ownership/group/company/business-state access before mutation or `sudo()`.
- Do not search with `sudo()` and then return, render, or download the result
  merely because the route is authenticated.
- Check attachment and report routes for authorization to both the container
  record and binary object.

## Response and abuse controls

- Avoid leaking stack traces, existence oracles, secrets, internal paths, or
  elevated record values.
- Review upload size/type, path handling, webhook replay, idempotency, and rate
  concerns where the endpoint can cause cost or state change.

## Verification

Require static evidence and controlled tests for anonymous, portal, unrelated
user, other-company, malformed, replayed, and missing-token/signature requests
as applicable. Never probe a live customer route without explicit authorization.
