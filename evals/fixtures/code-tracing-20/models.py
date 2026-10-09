from odoo import fields, models


class TraceOrder(models.Model):
    _name = "x.trace.order"
    _description = "Synthetic Odoo 20 trace fixture, not an installed addon"

    name = fields.Char()

    def action_confirm(self):
        self._mark_confirmed()
        return {"type": "ir.actions.act_window_close"}

    def _mark_confirmed(self):
        self.write({"name": "Confirmed"})
