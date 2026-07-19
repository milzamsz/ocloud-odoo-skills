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
- All Phase 3 trigger datasets contain 8 positive and 8 negative cases.
- Plugin: 39 tests passed, including cross-instance MCP guard denial,
  prefixed-tool post-call audit, duplicate conflict, returned-record negatives,
  draft approval/idempotency persistence, and Hermes contract tests.
- MCP agent: formatting and clippy passed; 62 tests passed.
- Staging configuration validates and release artifacts are current after
  vendoring the capability schema into the self-contained staging bundle and
  removing undeclared quotation/vendor-bill capabilities from its policy.
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

`create_crm_lead_draft.v1` passes unit and contract gates, but live staging
execution remains **blocked** pending fresh staging credentials, reviewed
write-enabled compatibility lock, live Odoo ACL/company negative cases, and
rollback/replay evidence. Production remains read-only.

The mutation skill and capability remain explicitly limited to Odoo 18
Community. Multi-version read coverage does not widen that mutation contract.

The local capability path now rejects multiple duplicate candidates, preserves
post-write verification failures as conflicts requiring manual review, binds
prefixed MCP calls to the selected instance, audits prefixed tools, records
approval/reviewer/result/verification metadata through a strict scalar
allowlist, and fsyncs the approval-store directory after atomic replacement.

## Residual risks

- Live Phase 7 staging scenario suite is still incomplete.
- Plugin-local domain skills still register; retire only after clean-profile
  Hermes loads the public Phase 2/3 skills.
- Multi-host draft stores and crash mid-`executing` need manual recovery.
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
