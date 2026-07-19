from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'
    sale_count_bad = fields.Integer(compute='_compute_sale_count_bad')

    def _compute_sale_count_bad(self):
        for partner in self:
            partner.sale_count_bad = self.env['sale.order'].search_count([('partner_id', '=', partner.id)])
