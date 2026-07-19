# OpenUpgrade Boundary

OpenUpgrade applies to major-version database analysis and migration. A normal
addon version bump, same-series data migration, or OCA port is not
automatically an OpenUpgrade task.

- Use OpenUpgrade repositories and documentation to inspect coverage, analysis,
  and migration APIs for the exact source/target series.
- Keep addon porting commits separate from database migration scripts and
  unrelated features.
- Treat analysis and planning as read-only. Do not run a migration unless the
  user explicitly authorizes mutation on a disposable database and filestore
  copy with a verified backup.
- Never experiment on the only database copy or present registry startup as
  migration completion.
- Re-author clean-room fixture examples. Before adapting third-party migration
  code, verify repository and file licenses, attribution needs, assumptions,
  framework version, and target schema.
- Hand major-version reconciliation to `odoo-version-upgrade`; OCA contribution
  readiness alone does not prove migrated business data is correct.
