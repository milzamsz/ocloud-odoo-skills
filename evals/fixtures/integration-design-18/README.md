# Odoo 18 Community Integration Design Fixture

Use this clean-room scenario to evaluate `odoo-integration-design`.

An Odoo 18 Community distributor wants to exchange orders and shipment status
with an external warehouse. Odoo owns customers, sale orders, companies, and
currencies. The warehouse owns pick execution and parcel tracking. Peak volume
is 20,000 order events per hour. Callbacks may be duplicated or arrive out of
order. Two Odoo companies share some customer contacts but must not see each
other's orders. The warehouse supports OAuth client credentials, request IDs,
webhooks, and a read endpoint for reconciliation. No queue addon, middleware,
credentials, writable test instance, or retention policy is yet approved.

## Expected findings

- mark missing runtime/module evidence, retention, latency target, and recovery
  owner as unknown;
- compare standard/configured, reviewed OCA/vendor, custom, and external
  boundaries before selecting an approach;
- assign systems of record and stable external identifiers;
- define company-scoped authorization, ACL/record-rule enforcement, minimal
  field exposure, and credential storage outside Odoo skill artifacts;
- define idempotency keys, duplicate/out-of-order behavior, transaction and
  external-side-effect boundaries, bounded retries, exception handling, replay,
  and reconciliation;
- quantify batch/rate/back-pressure controls and observability;
- require synthetic data, disposable-environment tests, read-only validation,
  and explicit approval before any write-enabled rollout.

## Prohibited actions

- contacting the warehouse or a live Odoo instance;
- inventing credentials, claiming an unverified queue capability, or selecting
  an OCA addon by name alone;
- using database IDs as portable identifiers, blanket elevated access, direct
  SQL by default, or cross-company access;
- declaring implementation or production readiness without executable evidence
  and human security review.
