# Odoo 18 Community inventory evidence

Load only for confirmed Odoo 18.0 Community work.

## Verified scope

- `stock/__manifest__.py` identifies the Inventory application and its security, warehouses, locations, routes/rules, operation types, moves, move lines, quants, lots, packages, replenishment, returns, backorders, counts, and reports.
- `stock` tests provide target-version evidence for warehouse, flow, route, replenishment, return, inventory, and multi-company behavior.
- `sale_stock` and `purchase_stock` are handoff evidence for sales deliveries and purchase receipts. They do not transfer ownership of commercial policy to Inventory.
- Keep picking, stock move, move line, and quant distinct. Quants represent quantity by location and dimensions such as lot, package, or owner.
- Valuation consequences must be flagged, then delegated to Accounting. Inspect `stock_account` only as a valuation-impact boundary; do not invent costing method, accounts, or journal entries here.

## Evidence paths

Resolve paths relative to the verified Odoo source root:

- `addons/stock/__manifest__.py`
- `addons/stock/models/stock_warehouse.py`
- `addons/stock/models/stock_rule.py`
- `addons/stock/models/stock_picking.py`
- `addons/stock/models/stock_move.py`
- `addons/stock/models/stock_quant.py`
- `addons/stock/tests/test_stock_flow.py`
- `addons/stock/tests/test_multicompany.py`
- `addons/stock_account/__manifest__.py`

Inspect the target source before asserting field names, states, defaults, or installed capabilities. This reference does not claim Enterprise support.
## Matrix boundary

This remains the rich Odoo 18 Community baseline. Community evidence excludes Enterprise-only behavior. Source presence does not prove installation, configuration, authorization, or end-to-end behavior. Record exact target evidence and unresolved deltas.
