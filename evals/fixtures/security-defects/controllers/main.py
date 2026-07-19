from odoo import http
from odoo.http import request


class FixtureSecurityController(http.Controller):
    @http.route(
        "/fixture/security/approve",
        type="http",
        auth="public",
        methods=["POST"],
        csrf=False,
    )
    def approve_for_fixture(self, document_id, **kwargs):
        document = request.env["fixture.security.document"].sudo().browse(
            int(document_id)
        )
        document.write({"name": "Approved by route"})
        return document.name
