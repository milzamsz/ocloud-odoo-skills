# Third-party skill coverage review (2026-10-24)

Four public repositories were inspected read-only as inspiration sources.
No text, scripts, or templates were copied. Every Odoo claim adopted below was
re-verified against the local Odoo 17/18/19/20 source trees before entering a
skill. Registry entries: `mart337i-odoo-skills`, `unclecatvn-agent-skills`,
`atakhadiviom-odoo-skill`, `19prince-claude-odoo-builder`.

| Repository | Revision | License | Posture |
|---|---|---|---|
| mart337i/odoo-skills | `634b2db` (unchanged since the 2026-10-09 review) | none in tree; derived from unclecatvn without its MIT notice | inspiration only |
| unclecatvn/agent-skills | `82ebbae` | MIT | inspiration only |
| atakhadiviom/odoo-skill | `d2f3629` | none (README says LGPL-3) | inspiration only |
| 19prince/claude-odoo-builder | `e8318db` | MIT | inspiration only |

## Ideas adopted (clean-room)

| Idea | Origin | Where it landed |
|---|---|---|
| Closed evidence cells (`path:line`, `NOT FOUND`, `UNCERTAIN`, `AMBIGUOUS`) and no version default | unclecatvn `odoo-workflow` | `odoo-context-discovery`, `odoo-code-tracing` output contracts |
| `_sudo` binding rule and attacker/entry/missing-control finding fields | unclecatvn, mart337i `odoo-web-security` | `odoo-security-audit` |
| Report rendering regression protocol (compare output not bytes; classify intended/noise/regression) | mart337i `odoo-report-migration` | `odoo-reporting/references/report-regression.md` |
| Website and portal outcome with verified access helper and JS layer per version | mart337i `odoo-website` (its invented portal helper was rejected) | new `odoo-website-portal` |
| Validator that tests the skills' own contracts (paths, enums, secrets, orphans) | unclecatvn CI | `scripts/validate_repository.py`, `tests/test_validator_rules.py` |
| Claude Code plugin manifest for discoverability | mart337i, unclecatvn | `.claude-plugin/` |

## Ideas recorded but not adopted

- Snapshot, dry-run, and rollback around live website writes (19prince): the
  mutation posture here stays capability-gated through `odoo-live-mutation`;
  a website write capability would need its own runtime contract first.
- Spec-driven task templates (atakhadiviom): overlaps `odoo-solution-design`
  output; revisit if an implementation-task artifact is requested.
- Automatic scratch-database definition of done (unclecatvn): database
  creation is a mutation here and stays behind explicit authorization.
- Anti-hallucination trap evaluations: planned as a separate evaluation change
  because they need executable fixtures per version.

## Claims checked against source and corrected

- Website `Interaction` classes exist in Odoo 19 and 20 trees, not in 17 or
  18; the legacy public widget registry is removed in 20.
- Hoot ships from Odoo 18; QUnit still ships in 17 to 19 and is gone in 20.
- `CustomerPortal._document_check_access` is the portal access helper in all
  inspected versions; no `_can_be_seen_by_portal_user` exists.

## Lessons folded in from OCloud delivery work

- OpenUpgrade rehearsal retry discipline (restore clean before every retry,
  project scripts before upstream in the upgrade path, first actionable
  traceback only, post-hop verification list) in
  `odoo-version-upgrade/references/openupgrade-workflow.md`.
- Restore-and-neutralize checklist for production copies in
  `odoo-deployment-operations/references/restore-neutralization.md`.
