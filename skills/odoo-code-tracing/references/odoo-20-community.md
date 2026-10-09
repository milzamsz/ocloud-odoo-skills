# Odoo 20 Community tracing evidence

Supported cell: 20.0 Community (source-evidence-only experimental). Consult `odoo-20-ce-source` and the specific official 20.0 developer page needed for the traced API; the registered documentation index alone is not behavioral proof. Matrix fixture: `evals/fixtures/version-matrix-20-community`. The local source tree has no Git provenance; record a reproducible fingerprint before citing it, never invent an upstream commit.

- Verify the exact controller, ORM hook, XML wiring, or frontend registration in the 20.0 source before drawing an edge; do not assume 18/19 APIs, OCA 20, Enterprise 20, or installed optional modules.
- Record source-confirmed edges with path and line, and classify dynamic or inaccessible links as unknown. Separate source-level possibility from observed runtime behavior.
- Identify caller identity, company/security boundary, elevation, and side effects; require a disposable Odoo 20 runtime check before claiming execution, measured performance, or effective access.
