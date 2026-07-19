from odoo import fields, models


class UpgradeSample(models.Model):
    _name = "oca.upgrade.sample"
    _description = "Clean-room Upgrade Sample"

    name = fields.Char(required=True)
    legacy_reference = fields.Char(index=True)
