from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    x_approval_code = fields.Char(string="Approval Code", store=True)
    x_related_partner_email = fields.Char(related="partner_id.email", store=False)
