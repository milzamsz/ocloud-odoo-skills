# Odoo 18 Community POS baseline

Use this reference only after confirming Odoo 18.0 Community.

## Verified scope

- Standard scope is grounded in the `point_of_sale` addon and its declared CE dependencies.
- Keep configuration, session, order, order line, payment, and payment method as distinct objects.
- A POS configuration connects products, pricelists, taxes, payment methods, and a stock location to browser-based selling sessions.
- Treat the session as the operating control boundary: opening state, orders and payments, cash movements where configured, and closing control.
- Payment amounts received from the client are recomputed server-side. Do not treat a terminal receipt alone as proof that Odoo recorded or reconciled the payment.
- Orders may be captured during connectivity loss, but offline limits and reconnection behavior depend on loaded data, browser state, devices, and payment integrations. Test the target setup.
- Paid orders can create stock pickings and, when invoiced, accounting moves. Hand route/valuation depth to Inventory and journal posting/reconciliation to Accounting.
- Refund, lot/serial, fiscal, hardware, restaurant, and payment-provider requirements must be verified against installed CE addons and the target source.

## Evidence paths

Resolve paths relative to the verified Odoo source root:

- `addons/point_of_sale/__manifest__.py`
- `addons/point_of_sale/models/pos_config.py`
- `addons/point_of_sale/models/pos_session.py`
- `addons/point_of_sale/models/pos_order.py`
- `addons/point_of_sale/models/pos_payment.py`
- `addons/point_of_sale/models/stock_picking.py`
- `addons/point_of_sale/tests/test_frontend.py`

Enterprise capabilities are outside this skill's support claim. Label them advisory until licensed target-source evidence is available.
## Matrix boundary

This remains the rich Odoo 18 Community baseline. Community evidence excludes Enterprise-only behavior. Source presence does not prove installation, configuration, authorization, or end-to-end behavior. Record exact target evidence and unresolved deltas.
