# OpenUpgrade Workflow

## Planning and analysis (read-only)

1. Pin source and target Odoo, Enterprise (when licensed), OCA, vendor, and
   custom revisions.
2. Inventory installed modules and map each to target coverage: migrated,
   native replacement, custom script, archive, or blocker.
3. Compare source/target models, fields, constraints, XML IDs, configuration,
   and semantics. An apparent rename needs evidence; matching labels are not
   enough.
4. Define pre-, schema/data-, and post-migration operations, assertions, and
   reconciliation evidence before execution.

## Execution boundary

Analysis does not authorize execution. Run OpenUpgrade only after explicit
approval on a disposable database and matching filestore copy, with a verified
backup and disabled outbound effects. Never use the sole database copy.

For authorized rehearsals:

- capture exact revisions, configuration, commands, logs, and run duration;
- fail loudly if expected source columns, XML IDs, or record counts differ;
- preserve stable external references with an explicit XML-ID rename mapping;
- preserve values during field renames before old schema is removed;
- make repeated trials disposable and migration steps idempotent where the
  framework expects reruns;
- separate compatibility/migration commits from feature changes.

Technical startup is only an intermediate checkpoint. Complete functional,
security, performance, inventory, and accounting reconciliation before a
go/no-go decision.
