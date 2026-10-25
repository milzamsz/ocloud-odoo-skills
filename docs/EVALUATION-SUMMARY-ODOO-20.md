# Odoo 20 Skill Outcome Evaluation Summary

Date: 2026-10-25. Fixture commit: `a94d257`. Protocol: `evals/MANUAL-EVALUATION.md`.

## Scope

Every version-claiming skill (23 of 24; `odoo-live-mutation` claims no cell by
design) was executed once per Odoo 20 cell (Community and Enterprise) on its
`*-20-{community,enterprise}-domain-001` outcome case against the executed
`domain-eval-20` fixture: 46 runs.

## Method

- Executor: a fresh agent session per case (Claude Sonnet) that loaded only
  the skill's `SKILL.md`, the Odoo 20 reference for the cell, and the
  conditional references the skill names; read the fixture; produced the
  skill's output artifact from its `assets/` template. Repository, Odoo, and
  databases were read-only or unavailable; the fixture README's recorded runs
  (install, tests, neutralize, `upgrade_code`) were citable evidence.
- Grader: a separate agent session per batch (Claude Sonnet) scoring each
  required finding and prohibited action with quoted evidence, and the five
  protocol scores. Pass requires every required finding met, no prohibited
  action observed, and a weighted total of at least 70.
- Records (one YAML per case, protocol template) and artifacts are kept under
  the gitignored `evals/results/unreleased/` directory; they contain no
  customer data or credentials.

## Result

46 of 46 cases pass. Weighted totals range from 94.8 to 98.0 (mean 96.7 over
the counted runs). `version-upgrade-20-enterprise-domain-001` failed on run 1
(weighted 82.6: the artifact marked the rewriter output Unknown instead of
citing the recorded run, because its prompt, unlike the other 45, did not say
the README's recorded runs were citable) and passed on run 2 (95.5) under the
same conditions as the rest. Both records are kept.

| Case | Skill | Run | Findings met | Prohibited observed | Weighted | Result |
|---|---|---|---|---|---|---|
| `addon-development-20-community-domain-001` | odoo-addon-development | 1 | 3/3 | 0 | 97.5 | pass |
| `addon-development-20-enterprise-domain-001` | odoo-addon-development | 1 | 3/3 | 0 | 95.2 | pass |
| `code-review-20-community-domain-001` | odoo-code-review | 1 | 3/3 | 0 | 97.5 | pass |
| `code-review-20-enterprise-domain-001` | odoo-code-review | 1 | 3/3 | 0 | 94.8 | pass |
| `code-tracing-20-community-domain-001` | odoo-code-tracing | 1 | 3/3 | 0 | 97.2 | pass |
| `code-tracing-20-enterprise-domain-001` | odoo-code-tracing | 1 | 3/3 | 0 | 96 | pass |
| `context-discovery-20-community-domain-001` | odoo-context-discovery | 1 | 3/3 | 0 | 97.0 | pass |
| `context-discovery-20-enterprise-domain-001` | odoo-context-discovery | 1 | 3/3 | 0 | 95.0 | pass |
| `data-model-diagram-20-community-domain-001` | odoo-data-model-diagram | 1 | 3/3 | 0 | 96.8 | pass |
| `data-model-diagram-20-enterprise-domain-001` | odoo-data-model-diagram | 1 | 3/3 | 0 | 97.4 | pass |
| `deployment-operations-20-community-domain-001` | odoo-deployment-operations | 1 | 3/3 | 0 | 97.7 | pass |
| `deployment-operations-20-enterprise-domain-001` | odoo-deployment-operations | 1 | 3/3 | 0 | 96.4 | pass |
| `functional-accounting-20-community-domain-001` | odoo-functional-accounting | 1 | 3/3 | 0 | 97.0 | pass |
| `functional-accounting-20-enterprise-domain-001` | odoo-functional-accounting | 1 | 3/3 | 0 | 97.4 | pass |
| `functional-inventory-20-community-domain-001` | odoo-functional-inventory | 1 | 3/3 | 0 | 97.5 | pass |
| `functional-inventory-20-enterprise-domain-001` | odoo-functional-inventory | 1 | 3/3 | 0 | 95.2 | pass |
| `functional-manufacturing-20-community-domain-001` | odoo-functional-manufacturing | 1 | 3/3 | 0 | 97.4 | pass |
| `functional-manufacturing-20-enterprise-domain-001` | odoo-functional-manufacturing | 1 | 3/3 | 0 | 97.0 | pass |
| `functional-pos-20-community-domain-001` | odoo-functional-pos | 1 | 3/3 | 0 | 98.0 | pass |
| `functional-pos-20-enterprise-domain-001` | odoo-functional-pos | 1 | 3/3 | 0 | 97.4 | pass |
| `functional-purchase-20-community-domain-001` | odoo-functional-purchase | 1 | 3/3 | 0 | 97.5 | pass |
| `functional-purchase-20-enterprise-domain-001` | odoo-functional-purchase | 1 | 3/3 | 0 | 95.2 | pass |
| `functional-sales-20-community-domain-001` | odoo-functional-sales | 1 | 3/3 | 0 | 97.5 | pass |
| `functional-sales-20-enterprise-domain-001` | odoo-functional-sales | 1 | 3/3 | 0 | 95.2 | pass |
| `indonesia-accounting-20-community-domain-001` | odoo-indonesia-accounting | 1 | 3/3 | 0 | 98.0 | pass |
| `indonesia-accounting-20-enterprise-domain-001` | odoo-indonesia-accounting | 1 | 3/3 | 0 | 97.4 | pass |
| `integration-design-20-community-domain-001` | odoo-integration-design | 1 | 3/3 | 0 | 97.5 | pass |
| `integration-design-20-enterprise-domain-001` | odoo-integration-design | 1 | 3/3 | 0 | 97.2 | pass |
| `live-context-20-community-domain-001` | odoo-live-context | 1 | 3/3 | 0 | 96.9 | pass |
| `live-context-20-enterprise-domain-001` | odoo-live-context | 1 | 3/3 | 0 | 96.4 | pass |
| `live-read-20-community-domain-001` | odoo-live-read | 1 | 3/3 | 0 | 97.4 | pass |
| `live-read-20-enterprise-domain-001` | odoo-live-read | 1 | 3/3 | 0 | 95.6 | pass |
| `oca-development-20-community-domain-001` | odoo-oca-development | 1 | 3/3 | 0 | 96.0 | pass |
| `oca-development-20-enterprise-domain-001` | odoo-oca-development | 1 | 3/3 | 0 | 95.0 | pass |
| `reporting-20-community-domain-001` | odoo-reporting | 1 | 3/3 | 0 | 98.0 | pass |
| `reporting-20-enterprise-domain-001` | odoo-reporting | 1 | 3/3 | 0 | 97.4 | pass |
| `security-audit-20-community-domain-001` | odoo-security-audit | 1 | 3/3 | 0 | 97.5 | pass |
| `security-audit-20-enterprise-domain-001` | odoo-security-audit | 1 | 3/3 | 0 | 96.0 | pass |
| `solution-design-20-community-domain-001` | odoo-solution-design | 1 | 3/3 | 0 | 97.5 | pass |
| `solution-design-20-enterprise-domain-001` | odoo-solution-design | 1 | 3/3 | 0 | 95.2 | pass |
| `testing-20-community-domain-001` | odoo-testing | 1 | 3/3 | 0 | 97.0 | pass |
| `testing-20-enterprise-domain-001` | odoo-testing | 1 | 3/3 | 0 | 95.2 | pass |
| `version-upgrade-20-community-domain-001` | odoo-version-upgrade | 1 | 3/3 | 0 | 97.5 | pass |
| `version-upgrade-20-enterprise-domain-001` | odoo-version-upgrade | 2 | 3/3 | 0 | 95.5 | pass |
| `website-portal-20-community-domain-001` | odoo-website-portal | 1 | 3/3 | 0 | 97.4 | pass |
| `website-portal-20-enterprise-domain-001` | odoo-website-portal | 1 | 3/3 | 0 | 96.4 | pass |

## Independent second grading pass (2026-10-25)

A second, independent grader (Claude Opus, four fresh sessions, no access to
the first pass's records) regraded all 46 artifacts strictly against the case
definitions and additionally checked one factual claim per artifact against
the fixture source files, not only the README.

- Result: 46 of 46 pass; both passes agree on every case; no prohibited
  action observed by either grader.
- Fact checks: 43 hold. Three do not, all for the same reason: the artifacts
  were produced before the multi-company and multi-currency tests were added
  to the fixture, so their test counts and "no multi-company run" statements
  describe the earlier fixture state. One further note: the `live-context`
  Enterprise artifact's test creates a sale order on the disposable database
  within its own test; the grader counted "no business record is mutated" as
  met because the claim is scoped to non-disposable data.
- Minor citation slips the second pass noted (line numbers off by one, a
  `/json/1/` versus `/json/2/` slip in the live-read artifact that is already
  corrected in the reference) affect no required finding.
- Records: `evals/results/unreleased/odoo-20-domain-grades-pass2/` (gitignored).

## OCA 20 (2026-10-25)

OCA 20.0 branches exist upstream; at server-tools commit `56685223` the only
installable module with tests, `base_view_inheritance_extension`, installs and
passes its 12 tests on fresh Odoo 20 Community and Enterprise databases (see
the `domain-eval-20` fixture README). Most OCA 20.0 modules remain unported.

## What the runs showed about the skills

- Every executor selected the correct Odoo 20 cell reference and kept the
  Community/Enterprise boundary; none inferred Enterprise from path names or
  claimed live or OCA 20 behavior.
- Executors consistently marked as Unknown what the case did not supply
  (live instance, business volumes, hosting, regulatory sources), which is the
  intended behavior of the evidence rules.
- Defects found and fixed during the evaluation: the `odoo-live-read` and
  `odoo-live-context` 20 references named `/json/1/` for bounded reads (the
  model-method JSON-2 path is `/json/2/` in the `rpc` addon); the
  `odoo-functional-accounting` skill said Enterprise requires licensed Odoo 18
  source regardless of target; two case findings were imprecise
  (neutralization authorization wording, "two components" versus two units).
- Executor-reported friction worth a later pass: `odoo-addon-development`
  lists both `odoo-20-{edition}.md` and `odoo-20.md`, which reads as two
  "exactly one" files; `test-seams.md` and `model-and-orm.md` are labelled as
  Odoo 18 evidence and were used as general guidance only.

## Human review

- Reviewer: milzamsz (repository maintainer), 2026-10-25.
- Result: pass. The reviewer approved the Odoo 20 Community and Enterprise
  evidence set: fixture suites from fresh installs, the 46-case skill outcome
  evaluation, the live JSON-2 runs, and the multi-company and multi-currency
  variants. Every evaluation record's `human_review` was set to `pass` with
  this reviewer and date.
- Consequence: the `20.0-community` and `20.0-enterprise` cells in
  `sources/VERSION-MATRIX.yaml` are promoted to `stable`. OCA 20 remains
  unclaimed beyond the local OpenUpgrade snapshot, and `odoo-live-mutation`
  remains blocked by its capability contract.

## Limits

- Grading was automated by two independent model passes that agree on every
  case; the human review above is the maintainer's acceptance of the evidence
  set.
- Each case covers one representative flow per skill domain with default
  configuration, plus one multi-company and one multi-currency variant added
  after the evaluation and executed on fresh databases of both editions. The evaluation sessions had no MCP instance; the live skills'
  transport was exercised separately against disposable Odoo 20 CE and EE
  servers over JSON-2 (see the `domain-eval-20` fixture README, "Live JSON-2
  runs"), not through `odoo-rust-mcp`.
- Graders' output-contract and clarity scores are judgement calls not checked
  line by line against each template.
