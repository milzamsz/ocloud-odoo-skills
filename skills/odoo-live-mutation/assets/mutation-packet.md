# Odoo live mutation packet

## Status
- State: proposed | awaiting_approval | blocked | denied | executed | verified | failed
- Blockers:

## Live target
- Odoo version / edition:
- Protocol / auth mode:
- Instance / database / environment:
- Registry / manifest revision:
- Required modules / model fingerprint:
- Environment policy:
- Authenticated actor:
- Active company / allowed companies:
- Evidence:

## Named capability
- Capability and version:
- Operation / risk class:
- Exact support-cell decision:
- Input / output / receipt schema hashes:
- Runtime contract advertised:
- Business outcome:
- Explicitly excluded side effects:

## Canonical request
- Target company:
- Canonical payload:
- Payload SHA-256:
- Idempotency key:
- Preconditions / expected impact:

## Approval binding
- Approver:
- Decision / timestamp / expiry:
- Bound target / company:
- Bound capability / payload SHA-256 / idempotency key:
- Separation-of-duties evidence:

## Capability gates
- [ ] Exact capability/version available
- [ ] Exact version/edition/protocol/auth/environment cell approved
- [ ] Required modules, schema hashes, and model fingerprint match
- [ ] Environment policy permits invocation
- [ ] Actor and approver policy passes
- [ ] Exact unexpired approval binding matches
- [ ] Submitted payload equals approved canonical payload
- [ ] Active, target, and approved company match
- [ ] Idempotency/replay check passes
- [ ] Access, preconditions, verification, and audit support pass

Runtime is blocked until every box is checked.

## Invocation and audit receipt
- Invocation attempted:
- Receipt / audit identifier:
- Receipt capability / target / company:
- Receipt target cell / operation class / actor / approval reference:
- Receipt payload SHA-256 / idempotency key:
- Correlation / audit identifier:
- Result model / record identifier:
- Verification / compensation status and owner:
- Timestamp / status:

## Read-only verification
- Bounded verification query:
- Observed approved fields:
- Side-effect check:
- Evidence:

## Final result
- Status:
- Unresolved risks / required new approval:
