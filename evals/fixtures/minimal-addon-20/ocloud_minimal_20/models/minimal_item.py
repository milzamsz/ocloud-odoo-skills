from odoo import fields, models


class OCloudMinimalItem(models.Model):
    _name = "ocloud.minimal.item"
    _description = "OCloud Minimal Item"
    _order = "name, id"

    name = fields.Char(required=True, index=True)
    quantity = fields.Integer(default=0, required=True)
    active = fields.Boolean(default=True)

    # Odoo 20 ignores a `_sql_constraints` list; constraints are table objects.
    _quantity_nonnegative = models.Constraint(
        "CHECK(quantity >= 0)",
        "Quantity must be non-negative.",
    )
