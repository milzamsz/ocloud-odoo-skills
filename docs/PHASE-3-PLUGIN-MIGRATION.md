# Phase 3 Plugin Skill Migration

The plugin currently registers concise local domain skills for CRM, reporting,
procurement, inventory, accounting, and Indonesian tax analysis. They overlap
the public Phase 2 domain skills.

## Decision

- Public procedural depth lives in `ocloud-odoo-skills`.
- Plugin-local skills remain thin runtime routing notes only while external
  skills are unavailable. `odoo-crm` is already reduced to routing plus the
  closed `create_crm_lead_draft.v1` boundary.
- Do not expand plugin-local domain content.
- Phase 3 live skills may reference tool names and plugin context, but they do
  not copy plugin implementation or grant access.

## Migration gate

Remove or redirect a local plugin skill only after a clean Hermes profile loads
the corresponding public skill and contract tests prove registration, trigger,
and resource availability. Until then, retain existing plugin behavior to
avoid a runtime regression.
