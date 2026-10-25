# dynamic-dashboard-20 fixture

Synthetic OCloud-authored data XML for the NexGen `dynamic_dashboard_ai_nexgen`
addon (20.0.1.0.15) on Odoo 20.0 Community. It covers an ORM tile with period
comparison, a count tile, a KPI with a target and its board item, a monthly bar
chart, a pie with a segment colour, a SQL item restricted by group, and a global
many2one filter, on a non-overlapping 12-column grid.

Used by `tests/test_dynamic_dashboard_xml.py` (validator) and installed in a
throwaway addon on a disposable Odoo 20 Community database to confirm the records
load (see `docs/EVALUATION-SUMMARY-ODOO-20.md`). No client data.
