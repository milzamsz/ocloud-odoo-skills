# Odoo 18 Community tracing evidence

Supported cell: 18.0 Community. Consult the checked-out Odoo 18 Community source and registered sources `odoo-18-ce-source` and `odoo-18-developer` before claiming framework behavior. This reference is a trace procedure, not a claim that any optional addon is installed.

- For backend entry points, inspect the target addon manifest, Python model/controller code, XML actions/data records, and inherited parent implementation before drawing an edge.
- For computed fields, distinguish declaration/dependencies from actual read-time or recompute timing; static code alone cannot prove an invocation count.
- For frontend paths, inspect the declared asset bundle, registry entry, template event, and server endpoint; unknown loaded assets remain unknown.
- For security, identify route authentication, ORM user, ACL and record-rule checks, company context, and each elevation boundary; do not infer access solely from a UI group or a call to `sudo()`.
- Run a disposable-environment test only with explicit database authorization. An unexecuted trace remains source-level evidence.
