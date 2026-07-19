# Odoo 18 Community manufacturing baseline

Use this reference only after confirming Odoo 18.0 Community.

## Verified scope

- Standard scope is grounded in the `mrp` addon and its declared CE dependencies.
- Bills of materials define components and can define operations and by-products; manufacturing orders control demand, consumption, production, and completion.
- Confirming an MO plans and reserves components according to stock rules; marking done consumes components and produces finished goods. Planned, reserved, consumed, and produced quantities remain distinct.
- Work centers and operations may represent execution steps and duration or capacity inputs. They are not mandatory for every manufacturing flow; confirm installed modules and configuration before promising scheduling behavior.
- Partial completion can close an order or create a manufacturing backorder. Inspect the target backorder wizard and tests before asserting default behavior.
- Lots and serials depend on product tracking and stock configuration; require evidence for component and finished-product traceability.
- Stock moves are operational records. Costing and journal-entry behavior depend on inventory and accounting configuration. Inspect `mrp_account` only as a valuation-impact boundary and delegate debit/credit, posting, and reconciliation to Accounting.
- Verify subcontracting, maintenance, quality, PLM, advanced planning, and edition-specific requests against installed target addons.

## Evidence paths

Resolve paths relative to the verified Odoo source root:

- `addons/mrp/__manifest__.py`
- `addons/mrp/models/mrp_bom.py`
- `addons/mrp/models/mrp_production.py`
- `addons/mrp/models/mrp_workorder.py`
- `addons/mrp/models/mrp_workcenter.py`
- `addons/mrp/wizard/mrp_production_backorder.py`
- `addons/mrp_account/__manifest__.py`

Enterprise capabilities are outside this skill's support claim. Label them advisory until licensed target-source evidence is available.
## Matrix boundary

This remains the rich Odoo 18 Community baseline. Community evidence excludes Enterprise-only behavior. Source presence does not prove installation, configuration, authorization, or end-to-end behavior. Record exact target evidence and unresolved deltas.
