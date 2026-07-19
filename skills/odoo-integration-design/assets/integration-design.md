# Odoo Integration Design

## Outcome and scope
- Odoo version/edition:
- Evidence labels:
- Assumptions and unknowns:
- Explicitly prohibited actions:

## Systems, actors, and ownership
| Entity/field | System of record | Direction | Identifier | Company scope | Retention/deletion |
|---|---|---|---|---|---|

## Option assessment
| Standard/configured | Third-party/OCA | Custom | External | Decision and evidence |
|---|---|---|---|---|

## Contract and mapping
- Trigger and transport:
- Endpoint/job and schema version:
- Validation, pagination, ordering, and limits:
- State, currency, time-zone, and identifier mapping:

## Security and privacy
- Authentication and credential lifecycle:
- Authorization, ACLs, record rules, and company isolation:
- Exposed fields and sensitive-data controls:
- Threats requiring security review:

## Reliability and recovery
- Idempotency key and duplicate result:
- Transaction boundary and external side effects:
- Timeouts, retries, backoff, and terminal errors:
- Concurrency, ordering, replay, and exception handling:
- Reconciliation and compensation:

## Performance and operations
- Volume, peaks, latency, and availability:
- Batch, rate, query, and retention limits:
- Logs, correlation IDs, metrics, and alerts:
- Owners and support runbook:

## Rollout and evidence
- Disposable-environment test plan:
- Read-only validation:
- Approval gate before writes:
- Rollback/disable plan:
- Acceptance criteria:
- Risks and blockers:
