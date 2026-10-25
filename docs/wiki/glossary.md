# Glossary

Terms as this repository uses them.

- **Skill:** a directory under `skills/` with a `SKILL.md`. It owns one primary outcome. See [skill-anatomy.md](skill-anatomy.md).
- **Phase 1, 2, 3:** foundation workflows, then domain and technical skills, then controlled live integration. See [skill-catalog.md](skill-catalog.md).
- **Status:** a skill's maturity: `draft`, `experimental`, `stable`, or `deprecated`.
- **Risk:** the most a skill may do: `read-only`, `advisory`, `controlled-write`, or `destructive`.
- **Cell:** one Odoo major version in one edition, such as `20.0-enterprise`, listed in `sources/VERSION-MATRIX.yaml`. In the mutation contract, a cell also fixes protocol, auth mode, and environment. See [version-matrix.md](version-matrix.md).
- **Claim:** a skill declaring support for a cell through `metadata.odoo`. It needs a reference, an outcome case, a fixture, and registered sources.
- **Edition:** `community` or `enterprise`. Never inferred from source presence alone.
- **Reference:** a file in a skill's `references/`, loaded on demand. Version references are named `odoo-<major>-<edition>.md`.
- **Asset:** an output template in a skill's `assets/`, such as a report, runbook, or packet skeleton.
- **Trigger dataset:** `evals/trigger/<skill>.json`, prompts labelled to trigger or not.
- **Near-miss negative:** a prompt that looks related but belongs to another skill or to generic work, so the skill must not trigger.
- **Outcome case:** an entry in `evals/outcome/cases.yaml` with required findings and prohibited actions.
- **Fixture:** a small OCloud-authored input under `evals/fixtures/`.
- **Source registry:** `sources/SOURCES.yaml`. Each entry has an authority tier and a license status.
- **Clean room:** studying outside material and writing original text, without copying.
- **Bundle:** a Hermes YAML file in `bundles/` that groups already installed skills.
- **Tap:** a Hermes skill source. `skills.sh.json` declares the groupings for this tap.
- **Overlay:** a private repository of client-specific procedures loaded after these skills. It can narrow policy but never widen it. See [../PRIVATE-OVERLAY.md](../PRIVATE-OVERLAY.md).
- **Capability:** a named, versioned mutation such as `create_quotation_draft.v1`. It is the only way to write.
- **Operation class:** `read`, `draft_write`, `accounting_suspense_write`, `state_transition`, `administrative`, or `destructive`.
- **Shared contract:** `support.yaml` in `odoo-rust-mcp-agent`, which decides capability support per cell.
- **Packet:** the approval document `odoo-live-mutation` builds for one invocation.
- **Envelope:** the signed, approval-bound request the plugin sends to the runtime.
- **Receipt:** the normalized result the runtime returns. Completion evidence is the receipt, not a record ID.
- **Idempotency key:** a one-time key that turns a retry into a `replay` of the first result.
- **Write version:** `oc_mcp_write_version`, the full-precision `write_date` token for guarded draft updates.
- **JSON-2:** Odoo 20's external model API, `POST /json/2/<model>/<method>`, with API key bearer auth.
