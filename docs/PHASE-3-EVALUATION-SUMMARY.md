# Phase 3 Evaluation Summary

Date: 2026-07-20

## Scope

- `odoo-live-context`
- `odoo-live-read`
- `odoo-live-mutation`
- cross-repo interface, risk classification, private overlay, and plugin
  migration contracts

## Evidence

- Skills repository: 21 skills, 0 validation warnings/errors; lint passed; 5
  tests passed; package check passed.
- Mutation triggers contain 12 positive and 14 near-miss negative cases; the
  other Phase 3 trigger datasets retain at least 8 per class.
- Plugin: 53 tests passed and 5 optional PostgreSQL integration tests skipped. Registration
  and execution now require an approved exact support cell and validate generated
  input/output schemas. Approved creates dispatch only a signed runtime envelope;
  draft-field updates are explicitly denied until atomic execution exists.
- MCP agent: formatting and clippy passed; 69 tests passed. Policy and generation
  consume the shared contract, pin capability/receipt context in locks, and omit
  generic write backends when every named capability is blocked. When enabled,
  the disabled backend contains only `odoo_execute_capability`.
- MCP: 394 tests passed. Controlled mode rejects generic writes, validates the
  signed registry-bound envelope, uses durable idempotency state, performs
  post-write verification, and returns the normalized runtime receipt.
- Existing staging and production compatibility approvals predate the shared
  contract and intentionally require explicit reapproval.
- Read-only source/profile smoke now covers Odoo 17/18/19 Community and
  Enterprise. The Odoo 19 Community staging path remains the only existing
  end-to-end live-interface smoke; other cells are verified-experimental and
  still require disposable live ACL/record-rule scenarios.

## Review fixes (2026-07-20)

- Aligned `create_crm_lead_draft.v1` skill reference and mutation fixture text
  with the closed runtime input schema (`title`, nullable contact fields,
  `evidence_ref`, idempotency pattern; no caller-chosen company/team).
- Clarified risk-classification ownership of metadata vs business-record reads.
- Narrowed the plugin-local `odoo-crm` skill to a routing note that no longer
  claims team assignment on draft create.

## Mutation status

All five named capabilities remain **blocked** in every Odoo 17/18/19
Community/Enterprise target cell. Existing Odoo 19 Community evidence used
legacy JSON-RPC and does not approve the required JSON-2/API-key cell.
Production remains read-only.

The local capability path now rejects multiple duplicate candidates, preserves
post-write verification failures as conflicts requiring manual review, binds
prefixed MCP calls to the selected instance, audits prefixed tools, records
approval/reviewer/result/verification metadata through a strict scalar
allowlist, and fsyncs the approval-store directory after atomic replacement.
The final MCP boundary additionally suppresses mutation retries, propagates
legacy company context, and defaults cleanup to dry-run behind dual guards.

## Residual risks

- Disposable six-cell runtime scenario suites and exact reapprovals are incomplete.
- Plugin-local domain skills still register; retire only after clean-profile
  Hermes loads the public Phase 2/3 skills.
- Atomic Odoo-side draft update remains unavailable and is denied.
- Post-write audit failure cannot undo an already-created Odoo record.

## Promotion gates

Before any stable Phase 3 release:

1. named product, Odoo functional, security, accounting, and operations reviews;
2. live staging negative cases for ACL, company, replay, audit failure, and
   returned-record verification;
3. clean-profile Hermes installation of the three live skills and bundle;
4. no generic write primitive selectable by the agent;
5. no production write profile.

This implementation does not tag or publish a release.
## Capability alignment gate

Run `make capability-check CONTRACT=/path/to/odoo-rust-mcp-agent/config/capabilities/support.yaml`.
It checks runtime schemas, all six exact cells, evidence and named reviews, five
capability references, the shared fixture, outcomes, and environment decisions.
No mutation cell may be claimed when this gate fails.
