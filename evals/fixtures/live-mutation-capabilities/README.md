# Controlled mutation capability fixture

This synthetic fixture contains no endpoint, credentials, client data, or live
authorization. The shared target matrix is Odoo 17/18/19 Community/Enterprise;
every mutation cell is blocked until exact runtime evidence and reviews approve it.

Evaluate one packet for each capability:

1. `create_crm_lead_draft.v1`: valid lead payload, duplicate conflict, and no
   assignment/stage/activity/chatter side effects.
2. `create_quotation_draft.v1`: one header and two lines; verify company,
   customer, currency, pricelist, prices, discounts, taxes, UoM, and `draft`.
3. `prepare_vendor_bill_draft.v1`: draft `in_invoice` with PO/receipt evidence;
   posting, payment, reconciliation, and procurement creation are prohibited.
4. `update_allowed_draft_fields.v1`: stale `write_date` and concurrent-write
   cases must be denied by an atomic Odoo-side conditional update.
5. `import_bank_transaction_draft.v1`: posted suspense and unreconciled result;
   require debit/credit, currency, suspense, accounting review, and correction owner.

For each capability test missing/expired approval, reviewer mismatch, payload
mutation, company mismatch, unknown field, invalid state, identical/changed/
concurrent replay, duplicate/lost response, output-schema failure, audit-sink
failure, verification failure, and manual compensation ownership.

## Required decisions

- Return `blocked` when the exact version, edition, protocol, auth mode, required
  modules, model fingerprint, schema hashes, source/runtime evidence, reference,
  fixture, outcome, staging decision, or required review is absent.
- Return `denied` for production, raw CRUD, bulk write, posting, reconciliation,
  workflow, cleanup, changed approval binding, stale update, or cross-company scope.
- Return a prior validated receipt for an identical completed replay. Never retry
  an uncertain mutation automatically.
- Validate every branch against the shared receipt vocabulary: approval required,
  created/updated, duplicate, conflict, denied, replay, uncertain, and verification
  failure.

## Expected artifact

Complete `skills/odoo-live-mutation/assets/mutation-packet.md`. No case authorizes
a real mutation, and a record ID without a validated receipt is incomplete.
