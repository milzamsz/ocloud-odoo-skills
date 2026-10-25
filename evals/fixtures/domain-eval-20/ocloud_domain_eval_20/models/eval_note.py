from odoo import fields, models


class OCloudEvalNote(models.Model):
    _name = "ocloud.eval.note"
    _description = "OCloud Evaluation Note"
    _inherit = ["portal.mixin"]

    name = fields.Char(required=True)
    partner_id = fields.Many2one("res.partner", required=True)
    score = fields.Integer(default=0)

    _score_nonnegative = models.Constraint("CHECK(score >= 0)", "Score must be non-negative.")

    def _compute_access_url(self):
        super()._compute_access_url()
        for note in self:
            note.access_url = f"/my/eval-notes/{note.id}"
