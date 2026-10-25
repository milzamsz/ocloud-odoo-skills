# Live Odoo 20 skill evaluation harness

Reproduces the live outcome evaluation recorded in
`docs/EVALUATION-SUMMARY-ODOO-20.md` (cases `*-20-{community,enterprise}-live-001`).

- `seed.py`: run inside `odoo-bin shell` on a fresh database that has the
  `domain-eval-20` fixture installed (plus `web_enterprise` and
  `account_accountant` for Enterprise). Seeds realistic records and a non-admin
  evaluator user, and prints an `rpc`-scoped API key (`KEY=...`). Store it as
  `keys/<cell>.key` with mode 600; never commit it.
- `odoo20q.py`: read-only JSON-2 proxy. Forwards only `search_read`,
  `search_count`, `read`, `read_group`, `fields_get`, `name_search`, `search`,
  plus a version call (`_server version_info`), logs every call per case under
  `logs/`, and refuses everything else (refusals are logged and fail the case).
  Cells `ce`/`ee` use the non-admin evaluator; `ce-meta`/`ee-meta` use a second
  evaluator that also holds the Access Rights group.
- `logsummary.py`: per-case call, refusal, and status summary for graders.
- `EXECUTOR-BRIEF.md`, `GRADER-BRIEF.md`: the exact briefs given to the
  executor and grader sessions (`<repo>`, `<harness-dir>`, `<results-dir>`, and
  `$ODOO_DEV_ROOT` are placeholders).

Serve each database on a dedicated port with `--workers=0` and `--db-filter`,
and drop the databases and keys afterwards. Results and logs belong in the
gitignored `evals/results/` directory.
