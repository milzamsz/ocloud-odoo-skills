# Odoo 18 Community purchase evidence

Load only for confirmed Odoo 18.0 Community work.

## Verified scope

- `purchase/__manifest__.py` identifies the Purchase application and its security, RFQ/purchase views, bill-line matching views, vendor bill reports, configuration, and vendor/product integration.
- `purchase_stock` bridges purchase orders to receipts; Inventory still owns route, picking, return, and backorder detail.
- Bill-line matching and bill-to-PO helpers are CE purchase features. Describe the configured controls; do not call them universal “three-way matching” without stating quantity, price, and receipt policy.
- Creating a vendor bill from a purchase order is not the same as posting it. Purchase users may create bills without gaining posting rights; Accounting owns posting, tax, payment, and reconciliation.

## Evidence paths

Resolve paths relative to the verified Odoo source root:

- `addons/purchase/__manifest__.py`
- `addons/purchase/models/purchase_order.py`
- `addons/purchase/models/purchase_bill_line_match.py`
- `addons/purchase/views/purchase_views.xml`
- `addons/purchase/views/purchase_bill_line_match_views.xml`
- `addons/purchase/tests/test_access_rights.py`
- `addons/purchase_stock/__manifest__.py`

Inspect the target source before asserting field names, states, defaults, or installed capabilities. This reference does not claim Enterprise support.
## Matrix boundary

This remains the rich Odoo 18 Community baseline. Community evidence excludes Enterprise-only behavior. Source presence does not prove installation, configuration, authorization, or end-to-end behavior. Record exact target evidence and unresolved deltas.
