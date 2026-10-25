"""HTTP evidence: JSON-2 bearer API and portal page access on Odoo 20."""

from datetime import datetime, timedelta
from http import HTTPStatus

from odoo.tests import HttpCase, tagged
from odoo.tests.common import new_test_user

CT_JSON = {"Content-Type": "application/json; charset=utf-8"}


@tagged("-at_install", "post_install")
class TestHttpEvidence(HttpCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = new_test_user(cls.env, login="eval_api", groups="base.group_user,base.group_allow_export")
        cls.key = cls.user.with_user(cls.user).env["res.users.apikeys"]._generate(
            scope="rpc", name="eval", expiration_date=datetime.now() + timedelta(hours=1)
        )

    # odoo-integration-design, odoo-live-context, odoo-live-read, odoo-security-audit
    def test_json2_requires_bearer_and_reads(self):
        anonymous = self.url_open("/json/2/res.partner/search_read", data='{"domain": [], "fields": ["name"], "limit": 1}', headers=CT_JSON)
        self.assertIn(anonymous.status_code, (HTTPStatus.UNAUTHORIZED, HTTPStatus.FORBIDDEN))
        res = self.url_open(
            "/json/2/res.partner/search_read",
            data='{"domain": [], "fields": ["name"], "limit": 1}',
            headers={**CT_JSON, "Authorization": f"Bearer {self.key}"},
        )
        self.assertEqual(res.status_code, HTTPStatus.OK, res.text)
        body = res.json()
        self.assertIsInstance(body, list)
        self.assertEqual(len(body), 1)
        self.assertIn("name", body[0])

    # odoo-website-portal
    def test_portal_home_for_portal_user(self):
        new_test_user(self.env, login="eval_portal_http", password="eval_portal_http", groups="base.group_portal")
        self.authenticate("eval_portal_http", "eval_portal_http")
        res = self.url_open("/my")
        self.assertEqual(res.status_code, HTTPStatus.OK)
        res = self.url_open("/my/eval-notes/999999")
        self.assertIn(res.status_code, (HTTPStatus.NOT_FOUND, HTTPStatus.FORBIDDEN, HTTPStatus.SEE_OTHER, HTTPStatus.FOUND))
