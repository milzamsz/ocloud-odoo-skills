# Evaluations

How the repository proves that a skill activates on the right prompts and
produces the right outcome. Source of truth: [../../evals/README.md](../../evals/README.md),
[../TESTING-AND-EVALUATION.md](../TESTING-AND-EVALUATION.md),
[../../evals/MANUAL-EVALUATION.md](../../evals/MANUAL-EVALUATION.md),
[../../evals/live/README.md](../../evals/live/README.md).

## Trigger datasets

`evals/trigger/<skill>.json` holds one per skill. It is a JSON array validated by
`schemas/trigger-eval.schema.json`:

```json
[
  {"query": "Add a regression test for this compute field bug.", "should_trigger": true, "notes": ""},
  {"query": "Explain Python decorators.", "should_trigger": false, "notes": "generic Python, not Odoo"}
]
```

You need at least 8 positives and 8 negatives. Make the negatives near misses:
prompts that belong to a neighbouring skill or to generic Python or web work.
Only `query`, `should_trigger`, and `notes` are allowed.

## Outcome cases

All skills share one file, `evals/outcome/cases.yaml`, with a top-level `cases:`
list. Each case looks like this:

```yaml
- id: website-portal-20-enterprise-live-001   # <skill-short>-<major>-<edition>-<kind>-<nnn>
  skill: odoo-website-portal
  odoo_version: '20.0'        # quoted string; needed to prove a version claim
  odoo_edition: enterprise    # omitted means community
  fixture: evals/fixtures/domain-eval-20
  request: Prove portal token, access URL, and portal page on Odoo 20. …
  required_findings:          # non-empty; what a correct answer must contain
    - _portal_ensure_token and the custom access_url work
  prohibited_actions:         # non-empty; any one observed fails the run
    - run against an existing or production database
```

The validator enforces only this: `skill` is set, `required_findings` and
`prohibited_actions` are non-empty lists, and every skill has at least one case.
`odoo_version` and `odoo_edition` are read when proving a cell claim. `id`,
`fixture`, and `request` are convention, but every existing case has them.

Every skill needs at least one case. Every claimed cell needs a matching case
(see [version-matrix.md](version-matrix.md#what-a-claim-needs)). Case kinds in
use include plain cases (`-001`), `-domain-` cases backed by an executed fixture
test, and `-live-` cases run against a disposable live server.

## Fixtures

`evals/fixtures/` holds small OCloud-authored inputs:

- **Cell fixtures:** `version-matrix-<major>-<edition>/` records source fingerprints for a matrix cell.
- **Scenario fixtures:** for example `security-defects/`, `compute-nplus1/`, and `upgrade-17-18/`.
- **Installable Odoo 20 addons:** `minimal-addon-20/` and `domain-eval-20/`. Their READMEs record the install and test commands and results.

Fixtures must not contain client data, credentials, or Enterprise source.

## Running evaluations

- **Structure:** `make validate` checks counts, schemas, and coverage. It does not run a model.
- **Manual model runs:** follow [../../evals/MANUAL-EVALUATION.md](../../evals/MANUAL-EVALUATION.md). Each run is recorded as YAML under `evals/results/<release>/<skill>/`. A prohibited action fails the run outright. Otherwise the run is scored on weighted required findings, evidence, safety, output contract, and clarity, and a human reviewer signs it.
- **Live Odoo 20 runs:** use `evals/live/`. `seed.py` seeds a disposable database. `odoo20q.py` is a read-only JSON-2 proxy that refuses and logs any non-read method. Executor and grader sessions get the briefs in that folder.

`evals/results/` is gitignored. Summaries that should persist go in
`docs/EVALUATION-SUMMARY-*.md` with no customer data.
