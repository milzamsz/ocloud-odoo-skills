# Odoo 18 Community Data Model Diagram Fixture

This clean-room fixture represents a bounded `sale.order` diagram request. It
contains source-only `x_approval_code`, `live-metadata.json` shaped like the
read-only MCP payload, a one-to-many inverse, a many-to-many tag relation, and
absent relation-target metadata for `crm.tag`. `model-graph.json` is the
normalized converter input.

Expected behavior:

- produce logical DBML rather than physical PostgreSQL claims;
- retain source/live evidence in notes;
- generate a labelled `crm.tag` stub and synthetic logical many-to-many bridge;
- report `sale.order.line` as the inverse of `sale.order.order_line`; and
- avoid record reads, credentials, or mutation.
