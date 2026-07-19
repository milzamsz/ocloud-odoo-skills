# Review Checklist

Use this after confirming the target Odoo version, edition, requirement, diff,
and repository instructions.

## Correctness and lifecycle

- Verify manifest dependencies, data order, hooks, assets, license, and external
  dependencies.
- Trace create/write/unlink, constraints, state transitions, compute
  dependencies, inverse/search methods, and behavior on multi-record sets.
- Check installation, upgrade, existing-data, uninstall, scheduled-job, and
  integration failure paths.
- Treat a missing `@api.depends` as both a correctness and recomputation risk;
  do not reduce it to style.

## Security and tenancy

- Map each persistent model to intentional ACLs and record rules.
- Review company-dependent fields, `company_id`, `check_company`, allowed
  companies, and negative cross-company cases.
- Trace every `sudo()`, public method, controller, SQL statement, HTML sink,
  attachment, and file operation. Load `odoo-security-audit` for material
  findings.
- Authentication is not record authorization. Confirm access to each selected
  record before any elevation or mutation.

## UI, data, and upgradeability

- Check stable XML inheritance selectors, groups, visibility, external IDs,
  `noupdate`, reports, escaping, frontend assets, and target-version syntax.
- Flag copied core code, core modifications, model/field/XML-ID renames without
  migration, and stored-field semantic changes.

## Evidence and tests

- Cite the exact file and symbol or line. Mark the finding Confirmed, Inferred,
  Assumed, or Unknown.
- Explain business impact, smallest safe remediation, and a verification that
  would fail before the fix.
- Require negative access and company tests, batch/query tests where material,
  and state/migration tests where relevant.
- Do not invent runtime behavior from static evidence or inflate formatting
  preferences above defects.
