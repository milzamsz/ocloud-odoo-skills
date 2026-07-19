# Odoo 18 Community operations baseline

Use this reference only after confirming Odoo 18.0 Community and the actual
hosting topology.

- Recoverable state normally includes PostgreSQL data and the matching Odoo filestore. Also preserve the release identifier, addon set, dependency lock or image identifier, and required configuration without secret values.
- `db_name`, `dbfilter`, `data_dir`, addons paths, proxy settings, worker model, scheduled jobs, and external dependencies materially affect a runbook. Observe them from target evidence.
- A source or addon release can require a same-version module upgrade. Treat it as a database mutation: review migration implications, back up, test on a disposable restored copy, authorize exactly, and verify.
- Health requires more than a listening process: include database connectivity, registry startup, HTTP behavior, scheduled work, logs, and a scoped functional smoke test.
- Database and filestore restoration must use a consistent recovery point. Test restoration on an isolated target and record integrity and application-level evidence.
- Odoo commands and service controls vary by package, container, orchestrator, and hosting provider. Do not invent commands; use project and platform documentation.

This reference does not cover major-version migration. Compose
`odoo-version-upgrade` for that outcome. Enterprise and managed-hosting
features are advisory until verified against licensed source or provider
documentation.
## Matrix boundary

This remains the rich Odoo 18 Community baseline. Community evidence excludes Enterprise-only behavior. Source presence does not prove installation, configuration, authorization, or end-to-end behavior. Record exact target evidence and unresolved deltas.
