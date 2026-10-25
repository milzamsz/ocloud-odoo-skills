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
- Fact checks: 42 hold. Three (testing on both cells, accounting on
  Community) do not because the artifacts were produced before the
  multi-company and multi-currency tests were added to the fixture, so their
  test counts and "no multi-company run" statements describe the earlier
  fixture state. The fourth, `live-context` Enterprise, said the test only
  searches and reads while it also creates a sale order on the disposable
  database; the grader counted "no business record is mutated" as met because
  the claim is scoped to non-disposable data.
- Minor citation slips the second pass noted (line numbers off by one, a
  `/json/1/` versus `/json/2/` slip in the live-read artifact that is already
  corrected in the reference) affect no required finding.
- Records: `evals/results/unreleased/odoo-20-domain-grades-pass2/` (gitignored).

## OCA 20 (2026-10-25)

OCA 20.0 branches exist upstream for all eleven repositories checked. Every
module that is installable and ships tests (six modules across five
repositories) installs together and passes 60 tests on fresh Odoo 20 Community
and Enterprise databases (see the `domain-eval-20` fixture README). Most OCA
20.0 modules remain unported.

## Live per-skill evaluation against running Odoo 20 servers (2026-10-25)

Every version-claiming skill was executed again on a new
`*-20-{community,enterprise}-live-001` case (46 cases) against running Odoo 20
Community and Enterprise servers instead of recorded runs.

- Targets: fresh databases with the `domain-eval-20` fixture and seeded
  business data (delivered and invoiced sale order, draft order, confirmed
  purchase and manufacturing orders, POS config, a second company on the
  Indonesian chart, a project), Enterprise with `web_enterprise` and
  `account_accountant` installed.
- Access: executors never held a credential. They queried through a read-only
  JSON-2 proxy (`evals/live/`) that forwards only read methods, logs every call
  per case, and refuses anything else. A refused call fails the case.
- Each case adds two required findings to its domain findings: at least two
  version- or edition-sensitive claims grounded in live queries, and every
  cited live query present in the proxy log. Graders (Claude Opus) checked
  findings against the artifact and cited queries against the log.

Result: 46 of 46 pass, 481 logged live calls, zero refused calls in the counted
runs. Eight cases needed a second run, each archived with its first run:

- `functional-sales` and `functional-inventory` (Community) each attempted one
  non-read method in run 1; the proxy refused and the grader failed them. The
  brief was sharpened and both passed with read methods only.
- `data-model-diagram` and `live-context` (both editions) failed run 1 because
  `ir.model.fields` is denied to a non-admin user, so the required
  `ir.model.fields` read could not happen; the skills correctly fell back to
  `fields_get` and recorded the denial. Run 2 used an evaluator holding the
  Access Rights group and met the finding unchanged.
- `context-discovery` (both editions) failed run 1 on the cross-edition marker
  finding and, on Enterprise, on the release tuple. A logged read-only version
  call was added to the proxy and the other edition's executed fixture run was
  cited as fixture evidence; both passed.

Facts the live runs established and folded into the references: the JSON-2
model-method route is `/json/2/<model>/<method>` in the `rpc` addon (the
earlier `/json/1/` wording was wrong and is corrected), `procurement.group` is
replaced by `stock.reference`, `purchase.order.line.taxes_id` is `tax_ids`,
`po_lead` is gone, `l10n_id_efaktur` is replaced by `l10n_id_efaktur_coretax`
in both editions, non-admin users are denied on configuration models, the
Enterprise release tuple ends in `'e'` only at runtime (`web_enterprise/version.py`),
and the DBML converter's fixed `no action` relation marker is not derived from
Odoo `ondelete` (reference corrected).

| Case | Skill | Run | Live calls | Refused | Result |
|---|---|---|---|---|---|
| `addon-development-20-community-live-001` | odoo-addon-development | 1 | 7 | 0 | pass |
| `addon-development-20-enterprise-live-001` | odoo-addon-development | 1 | 7 | 0 | pass |
| `code-review-20-community-live-001` | odoo-code-review | 1 | 9 | 0 | pass |
| `code-review-20-enterprise-live-001` | odoo-code-review | 1 | 11 | 0 | pass |
| `code-tracing-20-community-live-001` | odoo-code-tracing | 1 | 11 | 0 | pass |
| `code-tracing-20-enterprise-live-001` | odoo-code-tracing | 1 | 11 | 0 | pass |
| `context-discovery-20-community-live-001` | odoo-context-discovery | 2 | 9 | 0 | pass |
| `context-discovery-20-enterprise-live-001` | odoo-context-discovery | 2 | 7 | 0 | pass |
| `data-model-diagram-20-community-live-001` | odoo-data-model-diagram | 2 | 10 | 0 | pass |
| `data-model-diagram-20-enterprise-live-001` | odoo-data-model-diagram | 2 | 8 | 0 | pass |
| `deployment-operations-20-community-live-001` | odoo-deployment-operations | 1 | 16 | 0 | pass |
| `deployment-operations-20-enterprise-live-001` | odoo-deployment-operations | 1 | 9 | 0 | pass |
| `functional-accounting-20-community-live-001` | odoo-functional-accounting | 1 | 12 | 0 | pass |
| `functional-accounting-20-enterprise-live-001` | odoo-functional-accounting | 1 | 10 | 0 | pass |
| `functional-inventory-20-community-live-001` | odoo-functional-inventory | 2 | 13 | 0 | pass |
| `functional-inventory-20-enterprise-live-001` | odoo-functional-inventory | 1 | 14 | 0 | pass |
| `functional-manufacturing-20-community-live-001` | odoo-functional-manufacturing | 1 | 12 | 0 | pass |
| `functional-manufacturing-20-enterprise-live-001` | odoo-functional-manufacturing | 1 | 12 | 0 | pass |
| `functional-pos-20-community-live-001` | odoo-functional-pos | 1 | 12 | 0 | pass |
| `functional-pos-20-enterprise-live-001` | odoo-functional-pos | 1 | 11 | 0 | pass |
| `functional-purchase-20-community-live-001` | odoo-functional-purchase | 1 | 10 | 0 | pass |
| `functional-purchase-20-enterprise-live-001` | odoo-functional-purchase | 1 | 18 | 0 | pass |
| `functional-sales-20-community-live-001` | odoo-functional-sales | 2 | 13 | 0 | pass |
| `functional-sales-20-enterprise-live-001` | odoo-functional-sales | 1 | 16 | 0 | pass |
| `indonesia-accounting-20-community-live-001` | odoo-indonesia-accounting | 1 | 12 | 0 | pass |
| `indonesia-accounting-20-enterprise-live-001` | odoo-indonesia-accounting | 1 | 19 | 0 | pass |
| `integration-design-20-community-live-001` | odoo-integration-design | 1 | 9 | 0 | pass |
| `integration-design-20-enterprise-live-001` | odoo-integration-design | 1 | 7 | 0 | pass |
| `live-context-20-community-live-001` | odoo-live-context | 2 | 8 | 0 | pass |
| `live-context-20-enterprise-live-001` | odoo-live-context | 2 | 12 | 0 | pass |
| `live-read-20-community-live-001` | odoo-live-read | 1 | 9 | 0 | pass |
| `live-read-20-enterprise-live-001` | odoo-live-read | 1 | 8 | 0 | pass |
| `oca-development-20-community-live-001` | odoo-oca-development | 1 | 5 | 0 | pass |
| `oca-development-20-enterprise-live-001` | odoo-oca-development | 1 | 6 | 0 | pass |
| `reporting-20-community-live-001` | odoo-reporting | 1 | 8 | 0 | pass |
| `reporting-20-enterprise-live-001` | odoo-reporting | 1 | 10 | 0 | pass |
| `security-audit-20-community-live-001` | odoo-security-audit | 1 | 8 | 0 | pass |
| `security-audit-20-enterprise-live-001` | odoo-security-audit | 1 | 14 | 0 | pass |
| `solution-design-20-community-live-001` | odoo-solution-design | 1 | 13 | 0 | pass |
| `solution-design-20-enterprise-live-001` | odoo-solution-design | 1 | 9 | 0 | pass |
| `testing-20-community-live-001` | odoo-testing | 1 | 7 | 0 | pass |
| `testing-20-enterprise-live-001` | odoo-testing | 1 | 7 | 0 | pass |
| `version-upgrade-20-community-live-001` | odoo-version-upgrade | 1 | 11 | 0 | pass |
| `version-upgrade-20-enterprise-live-001` | odoo-version-upgrade | 1 | 10 | 0 | pass |
| `website-portal-20-community-live-001` | odoo-website-portal | 1 | 12 | 0 | pass |
| `website-portal-20-enterprise-live-001` | odoo-website-portal | 1 | 9 | 0 | pass |


## Live mutation matrix on Odoo 20 (2026-10-25)

`odoo-live-mutation` claims no version cell because support is decided by the
shared capability contract. Its runtime path was nevertheless exercised on
disposable Odoo 20 Community and Enterprise databases over JSON-2/API key: all
five capabilities, exact replay, stale-update conflict, the boundary suite,
and no-sales denial pass in both cells, after two Odoo 20 fixes in the sibling
runtime repositories, now in milzamsz/odoo-rust-mcp#15 and
milzamsz/odoo-rust-mcp-agent#1 together with a receipt preflight and a
`denied` outcome for Odoo access errors. Details, branches, and residual risks are in
`docs/CROSS-REPO-MUTATION-BASELINE.md` (Odoo 20 addendum).

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
