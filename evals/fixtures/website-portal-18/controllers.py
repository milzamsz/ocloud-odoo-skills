# Synthetic, non-installable fixture. Defects are intentional.
from odoo import http
from odoo.http import request


class WarrantyPortal(http.Controller):
    @http.route(["/my/warranty/<int:claim_id>"], type="http", auth="user", website=True)
    def warranty_claim(self, claim_id, **kw):
        partner = request.env.user.partner_id
        claim = request.env["warranty.claim"].sudo().search(
            [("id", "=", claim_id), ("partner_id", "=", partner.id)], limit=1
        )
        return request.render("warranty_portal.claim_page", {"claim": claim})
