from markupsafe import Markup

from odoo import fields, models


class FixtureDocument(models.Model):
    _name = "fixture.security.document"

    name = fields.Char(required=True)
    company_id = fields.Many2one("res.company", required=True)
    owner_id = fields.Many2one("res.users")
    body = fields.Html()
    line_count = fields.Integer(compute="_compute_line_count")

    def action_approve_for_fixture(self, document_id):
        document = self.browse(document_id).sudo()
        document.write({"name": "Approved"})
        return document.name

    def find_by_name_for_fixture(self, term):
        self.env.cr.execute(
            f"SELECT id FROM fixture_security_document WHERE name = '{term}'"
        )
        return self.browse(row[0] for row in self.env.cr.fetchall())

    def render_notice_for_fixture(self, message):
        return Markup(f"<strong>{message}</strong>")

    def _compute_line_count(self):
        for document in self:
            document.line_count = self.env["fixture.security.line"].search_count(
                [("document_id", "=", document.id)]
            )
