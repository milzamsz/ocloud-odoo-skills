from odoo import fields, models

class SecretRecord(models.Model):
    _name = 'fixture.secret.record'
    name = fields.Char(required=True)
    company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company)
