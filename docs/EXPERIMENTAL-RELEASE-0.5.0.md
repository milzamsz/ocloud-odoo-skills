# Experimental Release 0.5.0

## Scope

This release candidate packages the eight Phase 1 OCloud Odoo skills and four
Hermes bundles. It is intended for controlled evaluation, not autonomous
production operation.

## Supported evidence baseline

- Odoo 18.0 Community is the primary verified source baseline.
- Odoo 17.0 and 19.0 are secondary, version-bound references.
- Enterprise guidance is advisory and must be checked against licensed source;
  no Enterprise code is distributed.

## Install smoke test

After publishing the repository, use a disposable Hermes profile:

```bash
hermes skills tap add milzamsz/ocloud-odoo-skills
hermes skills search odoo
hermes skills install milzamsz/ocloud-odoo-skills/odoo-context-discovery
```

Then copy or symlink one file from `bundles/` into
`~/.hermes/skill-bundles/`, reload bundles, and confirm every named member is
installed. Bundle files group existing skills; they do not install members.

## Release gates

- `make validate`
- `make lint`
- `make test`
- `make package-check`
- Manual trigger/outcome records for each skill
- Human Odoo review
- Root MIT `LICENSE` is present
- Clean-profile Hermes tap smoke test after a remote is published

## Known limitations

- Model-based trigger and outcome execution remains a documented manual
  protocol; no provider credentials are stored in this repository.
- Local OCA 18.0 checkout coverage is incomplete.
- Live Odoo mutation remains outside this repository and requires controlled
  integration through the plugin/MCP layer.

## Local verification

On 2026-07-19, Hermes Agent 0.18.2 loaded all four bundle files in a disposable
profile and listed the expected 2/5/4/5 member counts. Tap search and skill
installation remain publication-time gates because this checkout has no remote.

The eight-skill manual evaluation and review results are recorded in
[EVALUATION-SUMMARY-0.5.0.md](EVALUATION-SUMMARY-0.5.0.md). They support an
experimental release; the listed stable-promotion blockers remain open.
