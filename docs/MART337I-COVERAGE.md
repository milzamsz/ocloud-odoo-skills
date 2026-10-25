# mart337i/odoo-skills coverage review

## Scope and provenance

- Inspected revision: [`634b2db69c0ffb9766a5d16cff09a81ff1df54f4`](https://github.com/mart337i/odoo-skills/tree/634b2db69c0ffb9766a5d16cff09a81ff1df54f4), observed upstream HEAD on 2026-10-09.
- GitHub repository metadata supplied no license and the inspected root tree had no `LICENSE`. No upstream wording, scripts, or assets were copied. Any future reuse requires explicit license/permission review.
- OCloud source registry entry: `mart337i-odoo-skills`; tier 6 inspiration only. Odoo APIs must be verified against exact-version authoritative sources.
- Scope of the implemented pilot: Odoo 18, 19, and 20 Community. Odoo 18 is stable baseline; 19/20 are experimental. Odoo 20 evidence is source-level only, not runtime compatibility. Enterprise is not claimed.

## Skill-by-skill disposition

| Upstream skill | OCloud disposition | Decision / boundary |
|---|---|---|
| `grill-me` | Excluded | Generic questioning workflow, outside Odoo skill scope. |
| `grill-with-docs` | Excluded | Generic documentation grilling; no distinct Odoo outcome. |
| `improve-codebase-architecture` | Excluded | Generic architecture workflow; use project architecture process. |
| `odoo-17.0` | Existing coverage | Version-neutral discovery plus per-cell references; this integration does not add 17 support. |
| `odoo-18.0` | Existing coverage | Existing Odoo 18 skill and exact-cell references; no monolithic duplicate. |
| `odoo-19.0` | Existing coverage | Existing Odoo 19 per-cell evidence; no monolithic duplicate. |
| `odoo-20.0` | Existing coverage | Odoo 20 Community is source-evidence-only experimental; Enterprise/OCA 20 remain unverified. |
| `odoo-code-review` | Existing coverage | `odoo-code-review`; broad review remains separate from tracing. |
| `odoo-code-tracer` | Adopted pilot | New `odoo-code-tracing`; bounded source-evidenced call-chain map, 18/19/20 CE. See skill, trigger cases, three outcome cases. |
| `odoo-grill-me` | Existing coverage | Discovery/design compose; no persona clone. |
| `odoo-idea-gates` | Existing coverage | `odoo-solution-design`; commercial demand gates are not substituted for client ERP fit-gap. |
| `odoo-migration` | Existing coverage | `odoo-version-upgrade` and `odoo-oca-development`; distinguish module migration from database migration. |
| `odoo-owl` | Candidate | Not implemented. First establish exact-version OWL behavior and unique outcome vs addon-development/testing. |
| `odoo-report-design` | Existing coverage | `odoo-reporting` owns mechanism selection/design; print implementation is only a future gap candidate. |
| `odoo-report-migration` | Candidate | Not implemented. Requires exact-version render baseline, visual acceptance, access/data checks. |
| `odoo-test-writer` | Existing coverage | `odoo-testing` owns test selection and authoring. |
| `odoo-web-security` | Existing coverage | `odoo-security-audit` and addon-development own security; web-specific distinct outcome not yet established. |
| `odoo-web-testing` | Existing coverage | `odoo-testing` owns browser/controller tests; separate skill only if unique acceptance artifact is demonstrated. |
| `odoo-website` | Candidate | Not implemented. Verify website/portal scope against existing addon and security workflows. |
| `odoo` | Existing coverage | Existing OCloud task-specific skills and bundles; no giant catch-all skill. |
| `zoom-out` | Excluded | Generic codebase orientation; outside Odoo-specific outcome scope. |

## Pilot evidence contract

- Skill: `skills/odoo-code-tracing/SKILL.md`.
- Version references: `references/odoo-18-community.md`, `references/odoo-19-community.md`, `references/odoo-20-community.md`; load only the confirmed cell.
- Trigger dataset: `evals/trigger/odoo-code-tracing.json` (8 positive, 8 near-miss negative cases).
- Outcome cases: `code-tracing-18-community-001`, `code-tracing-19-community-001`, `code-tracing-20-community-001` in `evals/outcome/cases.yaml`.
- Synthetic call-chain fixtures for 19/20 are explicitly unexecuted; no Odoo module is installed. The 18 case reuses the existing synthetic compute fixture. These establish source-reading outcome structure only, not runtime, access-control, query-count, or behavioral compatibility.
- Current status: experimental; automated trigger/outcome model evaluation and human Odoo review must be recorded before any promotion. Do not invent evaluation metrics or approval.
