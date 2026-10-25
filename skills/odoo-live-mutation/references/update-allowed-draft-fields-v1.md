# `update_allowed_draft_fields.v1` contract

Load only after the shared contract approves the exact target cell. Development
and staging approvals come from disposable matrix evidence per cell, including
Odoo 20 Community and Enterprise. Production remains read-only.

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
- Bind the full-precision version token, not the whole-second `write_date`.
  With helper `oc_mcp_mutation` 1.1.0 or later, read the computed field
  `oc_mcp_write_version` (the row's `write_date` with microseconds, read from
  SQL) in the bounded preview read and pass it as `expected_write_date`. The
  helper then rejects a concurrent edit made inside the same second as the
  preview, which Odoo's whole-second API serialization cannot show. A token
  without microseconds still works but keeps the old whole-second blind spot;
  record which form was bound.
- After an update, use the returned `write_version` as the token for any
  follow-up preview instead of re-reading `write_date`.
