# Gotchas

Traps that earlier changes hit. Check this page before you finish.

## Repository

- **Skills install one at a time.** A link from a skill to `../../docs/…` or
  to another skill fails validation. A backticked repository path such as
  `evals/…` inside a skill warns. Put what the skill needs in its own `references/`.
- **The validator only sees what `SKILL.md` names.** A reference file that
  `SKILL.md` never mentions is a warning, and the agent never loads it.
- **Brace paths are expanded.** `references/odoo-{19,20}-community.md` must
  resolve for every option.
- **`odoo_version` in outcome cases is a string.** Write `'20.0'`, not `20.0`.
  A missing `odoo_edition` means `community`, so Enterprise claims need it set.
- **`evals/results/` is gitignored.** Put durable summaries in `docs/EVALUATION-SUMMARY-*.md`.
- **Historical documents are records, not rules.** Release summaries in `docs/`
  describe the state at that release. See [repo-map.md](repo-map.md).
  For example, the "Runtime posture" paragraph in
  [../PHASE-3-SKILL-BOUNDARIES.md](../PHASE-3-SKILL-BOUNDARIES.md) predates the
  Odoo 17 to 20 mutation contract cells. The shared contract decides support.
- **Counts appear in several places.** These are `README.md`, `MANIFEST.md`,
  `CHANGELOG.md`, and this wiki. Recount from the tree instead of copying a number.
- **Separate change types.** `AGENTS.md` asks for bug fixes, behavior changes,
  reference updates, evaluation changes, version support, and formatting in
  separate changes.

## Odoo 20

- `ir.model.access.csv` no longer loads. Use `security/ir.access.csv`.
- `_sql_constraints` disappears silently, with only a warning. Use `models.Constraint`.
- A manifest `license: MIT` is rejected on module update. Use a selection value such as `Other OSI approved licence`.
- `read_group` takes `(domain, groupby, aggregates)`. A legacy `fields` argument answers 422 over JSON-2.
- JSON-2 lives in the `rpc` addon at `/json/2/`, not in `web` at `/json/1/`.
- Non-admin users get 403 on technical models. Prove access with `fields_get` and a bounded business read.
- Only the runtime version endpoint shows the Enterprise suffix. The source `release.py` never does.

## Local Odoo environments

These apply when running fixtures against the local Odoo source trees. They are
outside the repository, under an `odoo-dev/environments/odoo<major><ce|ee>` workspace.

- Run with `env -u PYTHONPATH` so another tree's packages do not leak in.
- Package-installed trees use `venv/bin/odoo`. Others use `odoo/odoo-bin`. Some
  configs send output to a log file instead of the console, so read the log for test summaries.
- Use only disposable databases. Drop them afterwards, and never commit API keys from `evals/live/` runs.
