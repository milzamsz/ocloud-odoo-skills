# `update_allowed_draft_fields.v1` contract

Load only after the shared contract approves the exact target cell. Development
and staging are approved for Odoo 17/18/19 Community and Enterprise from
disposable matrix evidence. Production remains read-only.

The runtime invokes only the installed, fingerprinted `oc_mcp_mutation` helper.
Do not emulate it with a read followed by a generic write.

## Outcome and bounds

Atomically update only the contract-enumerated fields on one draft `sale.order`
or draft vendor bill. Bind record ID, trusted company, expected `write_date`,
allowed changed fields, evidence reference, payload digest, and idempotency key.

The runtime must check company, `state=draft`, expected `write_date`, and the
field allowlist in the same Odoo transaction as the write. A read-then-generic-
write sequence is unsupported. Never change lines, amounts, state, company,
posting, confirmation, payment, reconciliation, or workflow fields.

## Required evidence

- Reject empty, unknown, stale, cross-company, or non-draft updates.
- Require a new preview and approval after any field or `write_date` change.
- Verify only approved fields changed and state/company remain unchanged.
- Return the normalized `draft_write` receipt; stale or concurrent writes are
  conflicts and uncertain writes are not retried.
- Account for Odoo's whole-second `write_date` API precision when assessing
  sub-second concurrency risk.
