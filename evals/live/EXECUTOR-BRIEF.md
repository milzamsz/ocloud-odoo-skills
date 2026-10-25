# Live skill evaluation brief

You are an Agent Skills client executing one live outcome evaluation.

- Repository (read-only, never modify): <repo>
- Your case: the `id` given in your task, in `evals/outcome/cases.yaml`. Read its request, fixture, required_findings, prohibited_actions.
- Skill: `skills/<skill>/SKILL.md`. Follow it exactly. Load only the Odoo 20 reference for your edition (`references/odoo-20-community.md` or `references/odoo-20-enterprise.md`) plus the conditional references the skill names for this request.
- Fixture: read `evals/fixtures/domain-eval-20` (README and source).
- Live target: a running Odoo 20.0 server for your edition, seeded with realistic data (customers, a confirmed and delivered and invoiced sale order, a draft sale order, a confirmed purchase order, a confirmed manufacturing order, a POS config, a second company with the Indonesian chart, a project, the fixture's `ocloud.eval.note` model). Query it ONLY through this read-only proxy:

      <harness-dir>/odoo20q.py <ce|ee> <your_case_id> <model> <method> '<json kwargs>'

  Allowed methods: search_read, search_count, read, read_group (Odoo 20 kwargs: domain, groupby, aggregates), fields_get, name_search, search. One extra read-only call returns the live server version: `odoo20q.py <cell> <case_id> _server version_info '{}'` (wraps Odoo's `/web/webclient/version_info`). Example:
      odoo20q.py ce <case_id> sale.order search_read '{"domain": [["state","=","sale"]], "fields": ["name","state","amount_total"], "limit": 5}'
  Every call is logged under your case id. ATTEMPTING ANY OTHER METHOD (for example check_access_rights, has_group, write, create, or any made-up name) IS A PROHIBITED ACTION THAT FAILS YOUR CASE, even though the proxy refuses it; prove access by a bounded read instead. Never try other methods, never read files under the proxy's keys/ directory, never contact the server any other way. The evaluator user is a non-admin internal user; access denials are real Odoo 20 behavior worth reporting.
- Local Odoo 20 source for path:line citations (read-only; quote identifiers only, never copy blocks): Community `$ODOO_DEV_ROOT/environments/odoo20ce/odoo`; Enterprise addons `$ODOO_DEV_ROOT/libraries/odoo-enterprise/odoo_20.0+e.20261008/odoo-20.0+e.20261008/odoo`.
- Do not run Odoo, odoo-bin, databases, or anything that writes outside your artifact path.

Produce the skill's required output artifact from its `assets/` template, grounded in live queries, the fixture, the reference, and source. Cite each live query as `model.method(...) -> observed result`. Mark genuine unknowns as Unknown. Write it to:

    <results-dir>/eval-live/<case_id>.md

Reply with only: the output path, the reference files you loaded, the number of live queries you made, and any skill instruction you could not follow and why.
