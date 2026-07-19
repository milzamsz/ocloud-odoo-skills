# Odoo 18 Community sales evidence

Load only for confirmed Odoo 18.0 Community work.

## Verified scope

- `sale/__manifest__.py` identifies the Sales module and its dependencies, security, quotation/order views, invoice integration, pricelist-related product behavior, reports, and configuration.
- `sale_management/__manifest__.py` extends the Sales application; inspect it when `sale_management` is installed.
- `crm/__manifest__.py` is the evidence boundary for leads, opportunities, and sales teams.
- `sale_crm` bridges CRM opportunities to quotations/orders; do not treat CRM as part of base `sale`.
- `sale_stock` bridges confirmed sales to delivery operations; Inventory still owns route and picking detail.
- Quotation confirmation and invoice creation are distinct actions. Line invoiceability depends on order state, ordered/delivered/invoiced quantities, and the product invoice policy; inspect `sale.order` / `sale.order.line` before asserting when an order is invoice-ready.

## Evidence paths

Resolve paths relative to the verified Odoo source root:

- `addons/sale/__manifest__.py`
- `addons/sale/models/sale_order.py`
- `addons/sale/models/sale_order_line.py`
- `addons/sale/views/sale_order_views.xml`
- `addons/sale_management/__manifest__.py`
- `addons/crm/__manifest__.py`
- `addons/sale_crm/__manifest__.py`
- `addons/sale_stock/__manifest__.py`

Inspect the target source before asserting field names, states, defaults, or installed capabilities. This reference does not claim Enterprise support.
