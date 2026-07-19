# SQL, HTML, and Elevation Review

## SQL

- Prefer the ORM so access rules, company behavior, flushing, and cache
  semantics remain visible.
- When SQL is necessary, require a documented reason and identify every value
  and identifier entering the query. Never build SQL by interpolation,
  concatenation, or f-strings.
- Pass values as parameters. For dynamic identifiers or composed statements,
  use the target-version SQL composition API and verify it against source.
- Direct SQL can bypass ACLs, record rules, ORM invariants, translations,
  computed-field behavior, and cache management even when injection is absent.
  Review authorization and transaction/cache effects separately.

## HTML and XSS

- Trace untrusted text from request, model, integration, or translation to HTML
  fields, QWeb output, email, and controller responses.
- Escape plain text at output. Sanitize only when the product intentionally
  accepts an HTML subset.
- `Markup` declares content safe; it does not sanitize it. Flag `Markup` around
  caller-controlled or formatted strings unless each untrusted component was
  escaped before composition.
- Review raw template output, HTML fields with sanitization disabled, URLs and
  attributes, and stored content that can become persistent XSS.

## `sudo()` and public methods

- First prove the caller may request the operation under the current record,
  group, company, owner, and business state.
- Elevate only the minimal recordset and operation. Do not return elevated
  records or values and do not use `sudo()` to conceal a missing access design.
- Public model methods can be RPC entry points. Treat caller-provided IDs,
  fields, domains, filenames, and target states as untrusted.

## Verification

Use static malicious-looking sentinel strings and negative unit cases; do not
execute injection or XSS payloads against a live service. Verify both the
security property and intended authorized behavior after remediation.
