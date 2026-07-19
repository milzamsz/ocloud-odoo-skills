# Odoo 18 Community Integration Notes

Verified baseline: Odoo 18 Community. Do not infer Enterprise capabilities or
compatibility with another major version.

- Odoo HTTP controllers define routes and authentication modes. Inspect the
  target Odoo 18 source and existing project controllers before fixing route,
  request, response, or CSRF behavior in a contract.
- Controller authentication does not replace ORM access controls. Apply model
  ACLs, record rules, company rules, field restrictions, and business checks to
  every exposed operation.
- Use stable external identifiers or an explicit mapping model; database IDs
  are not portable integration identifiers.
- Use ORM boundaries by default. For bulk work, bound batches and measure
  queries, transactions, lock duration, worker occupancy, and retries.
- Community provides core HTTP, scheduled actions, mail, and ORM facilities.
  A durable job queue, connector framework, or vendor API adapter is not assumed
  to be standard; assess a target-version OCA/vendor component or middleware.
- Odoo transaction rollback does not undo a completed external side effect.
  Design idempotency, outbox/confirmation state, compensation, and
  reconciliation explicitly.
- Keep API credentials outside skill artifacts and addon source. Live calls and
  writes require explicit authorization.

Relevant official source areas to inspect in a target checkout include
`odoo/http.py`, `odoo/addons/base`, model access definitions, and the specific
business addon's models/controllers. This reference is concise guidance, not a
substitute for source inspection.
