# Repository map

Where things live, and which documents describe current rules versus a past
release. Source of truth: the tree itself and [../../README.md](../../README.md).

## Directories

| Path | Holds | Notes |
|---|---|---|
| `skills/<name>/` | One skill: `SKILL.md`, `references/`, `assets/`, optional `scripts/` | Directory name equals the frontmatter `name`. Each skill must be self-contained. |
| `bundles/*.yaml` | Hermes bundles that group installed skills | Members must exist in `skills/`. |
| `skills.sh.json` | Tap groupings | Must list exactly the skills in `skills/` (`make package-check`). |
| `.claude-plugin/` | Claude Code plugin and local marketplace manifests | Points at `./skills`. |
| `evals/trigger/<skill>.json` | Activation prompts, positive and near-miss negative | One file per skill. |
| `evals/outcome/cases.yaml` | Outcome scenarios for every skill | Also proves version-cell claims. |
| `evals/fixtures/` | Small OCloud-authored repos and files used by outcome cases | Includes `version-matrix-<v>-<edition>` cell fixtures and Odoo 20 test addons. |
| `evals/live/` | Read-only Odoo 20 live-evaluation harness | Proxy, seeder, briefs. See [evaluations.md](evaluations.md). |
| `evals/results/` | Evaluation records | Gitignored. Never commit it. |
| `sources/SOURCES.yaml` | Source registry with authority tier and license status | Schema: `schemas/source-registry.schema.json`. |
| `sources/VERSION-MATRIX.yaml` | Claimable Odoo version and edition cells | See [version-matrix.md](version-matrix.md). |
| `sources/SOURCE-POLICY.md` | Clean-room rules for outside material | |
| `schemas/` | JSON schemas for trigger sets, source registry, skill contract | |
| `templates/skill/` | Starting point for a new skill | Copy, then rename. |
| `templates/overlay/` | Starting point for a private client overlay | See [../PRIVATE-OVERLAY.md](../PRIVATE-OVERLAY.md). |
| `scripts/` | `validate_repository.py`, `package_check.py`, `validate_mutation_capabilities.py` | Run through `make`. |
| `tests/` | pytest for validators and skill scripts | |
| `prompts/` | Reusable prompts for authoring, review, and evaluation work | |
| `docs/adr/` | Architecture decision records 0001 to 0005 | Short and still binding. |
| `docs/wiki/` | This wiki | Checked by `make validate`. |

## Root documents

Current and normative: [AGENTS.md](../../AGENTS.md), [PRODUCT-SCOPE.md](../../PRODUCT-SCOPE.md),
[ARCHITECTURE.md](../../ARCHITECTURE.md), [TECHNICAL.md](../../TECHNICAL.md),
[DESIGN.md](../../DESIGN.md), [DOMAIN-MODEL.md](../../DOMAIN-MODEL.md),
[CONTRIBUTING.md](../../CONTRIBUTING.md), [SECURITY.md](../../SECURITY.md),
[LICENSE-POLICY.md](../../LICENSE-POLICY.md).

Status and history: [README.md](../../README.md) (project status),
[CHANGELOG.md](../../CHANGELOG.md), [MANIFEST.md](../../MANIFEST.md) (package counts),
[PLAN.md](../../PLAN.md) (original phased plan; phases 0 to 2 are done).

## `docs/` documents

Current rules, read when the task touches them:

- [SKILL-AUTHORING-STANDARD.md](../SKILL-AUTHORING-STANDARD.md), [TESTING-AND-EVALUATION.md](../TESTING-AND-EVALUATION.md), [DEVELOPMENT-WORKFLOW.md](../DEVELOPMENT-WORKFLOW.md), [RELEASE-AND-DISTRIBUTION.md](../RELEASE-AND-DISTRIBUTION.md)
- [ODOO-SOURCE-HIERARCHY.md](../ODOO-SOURCE-HIERARCHY.md), [VERSION-EVIDENCE.md](../VERSION-EVIDENCE.md)
- [HERMES-INTEGRATION.md](../HERMES-INTEGRATION.md), [PRIVATE-OVERLAY.md](../PRIVATE-OVERLAY.md)
- Skill boundaries: [PHASE-1-SKILL-BOUNDARIES.md](../PHASE-1-SKILL-BOUNDARIES.md), [PHASE-2-SKILL-BOUNDARIES.md](../PHASE-2-SKILL-BOUNDARIES.md), [PHASE-3-SKILL-BOUNDARIES.md](../PHASE-3-SKILL-BOUNDARIES.md)
- Phase 3 contracts: [PHASE-3-INTERFACE-CONTRACT.md](../PHASE-3-INTERFACE-CONTRACT.md), [PHASE-3-RISK-CLASSIFICATION.md](../PHASE-3-RISK-CLASSIFICATION.md), [CROSS-REPO-MUTATION-BASELINE.md](../CROSS-REPO-MUTATION-BASELINE.md)
- Third-party scope decisions: [THIRD-PARTY-COVERAGE.md](../THIRD-PARTY-COVERAGE.md), [MART337I-COVERAGE.md](../MART337I-COVERAGE.md)

Historical records, evidence for a past release; do not treat as current rules:

- [EVALUATION-SUMMARY-0.5.0.md](../EVALUATION-SUMMARY-0.5.0.md), [EXPERIMENTAL-RELEASE-0.5.0.md](../EXPERIMENTAL-RELEASE-0.5.0.md)
- [STABLE-RELEASE-1.0.0.md](../STABLE-RELEASE-1.0.0.md), [HUMAN-REVIEW-1.0.0.md](../HUMAN-REVIEW-1.0.0.md), [REGRESSION-SUMMARY-1.0.0.md](../REGRESSION-SUMMARY-1.0.0.md)
- [PHASE-2-EVALUATION-SUMMARY.md](../PHASE-2-EVALUATION-SUMMARY.md), [PHASE-3-EVALUATION-SUMMARY.md](../PHASE-3-EVALUATION-SUMMARY.md), [PHASE-3-PLUGIN-MIGRATION.md](../PHASE-3-PLUGIN-MIGRATION.md)
- [EVALUATION-SUMMARY-ODOO-20.md](../EVALUATION-SUMMARY-ODOO-20.md): the evidence behind the stable Odoo 20 cells. Add to it, do not rewrite it.
