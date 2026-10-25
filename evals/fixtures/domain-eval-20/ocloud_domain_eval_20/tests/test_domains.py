"""Executable Odoo 20 evidence per OCloud skill domain. Each test names the skills it backs."""

import logging

from psycopg2 import IntegrityError

from odoo import release
from odoo.exceptions import AccessError, ValidationError
from odoo.tests import TransactionCase
from odoo.tests.common import new_test_user

_logger = logging.getLogger(__name__)


class TestDomains(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = cls.env.company
        cls.partner = cls.env["res.partner"].create({"name": "Eval Customer"})
        cls.vendor = cls.env["res.partner"].create({"name": "Eval Vendor"})
        cls.product = cls.env["product.product"].create(
            {"name": "Eval Product", "type": "consu", "is_storable": True, "list_price": 100.0, "standard_price": 60.0}
        )
        cls.component = cls.env["product.product"].create(
            {"name": "Eval Component", "type": "consu", "is_storable": True, "standard_price": 10.0}
        )
        cls.warehouse = cls.env["stock.warehouse"].search([("company_id", "=", cls.company.id)], limit=1)

    # odoo-context-discovery, odoo-solution-design
    def test_release_and_edition_markers(self):
        self.assertEqual(release.version_info[0], 20)
        modules = self.env["ir.module.module"]
        web_enterprise = modules.search([("name", "=", "web_enterprise")], limit=1)
        installed = {
            m.name: m.state for m in modules.search([("name", "in", ["web_enterprise", "account_accountant", "l10n_id_efaktur"])])
        }
        _logger.info("EVAL edition markers: %s", installed or "none present (Community)")
        if web_enterprise and web_enterprise.state == "installed":
            self.assertEqual(installed.get("account_accountant"), "installed")

    # odoo-addon-development, odoo-testing, odoo-security-audit
    def test_access_csv_constraint_and_portal_rule(self):
        user = new_test_user(self.env, login="eval_internal")
        note = self.env["ocloud.eval.note"].with_user(user).create({"name": "n1", "partner_id": self.partner.id})
        self.assertTrue(note.id)
        with self.assertRaises((IntegrityError, ValidationError)), self.cr.savepoint():
            self.env["ocloud.eval.note"].with_user(user).create({"name": "bad", "partner_id": self.partner.id, "score": -1})
        portal_user = new_test_user(self.env, login="eval_portal", groups="base.group_portal")
        other = self.env["ocloud.eval.note"].create({"name": "other", "partner_id": self.vendor.id})
        own = self.env["ocloud.eval.note"].create({"name": "own", "partner_id": portal_user.partner_id.id})
        self.assertEqual(own.with_user(portal_user).read(["name"])[0]["name"], "own")
        with self.assertRaises(AccessError):
            other.with_user(portal_user).read(["name"])
        # access rows live in ir.access, not ir.model.access
        self.assertFalse("ir.model.access" in self.env.registry)
        rows = self.env["ir.access"].search([("model_id.model", "=", "ocloud.eval.note")])
        self.assertEqual(set(rows.mapped("operation")), {"crud", "r"})

    # odoo-functional-sales, odoo-functional-inventory, odoo-code-tracing
    def test_sales_order_to_cash(self):
        so = self.env["sale.order"].create(
            {"partner_id": self.partner.id, "order_line": [(0, 0, {"product_id": self.product.id, "product_uom_qty": 2})]}
        )
        so.action_confirm()
        self.assertEqual(so.state, "sale")
        picking = so.picking_ids
        self.assertEqual(len(picking), 1, "confirming the order created exactly one delivery")
        self.env["stock.quant"]._update_available_quantity(self.product, self.warehouse.lot_stock_id, 5)
        picking.action_assign()
        for move in picking.move_ids:
            move.quantity = move.product_uom_qty
            move.picked = True
        picking.button_validate()
        self.assertEqual(picking.state, "done")
        self.assertEqual(self.product.with_context(location=self.warehouse.lot_stock_id.id).qty_available, 3)
        invoice = so._create_invoices()
        invoice.action_post()
        self.assertEqual(invoice.state, "posted")
        self.assertEqual(invoice.move_type, "out_invoice")
        self.assertAlmostEqual(invoice.amount_untaxed, 200.0)

    # odoo-functional-purchase
    def test_purchase_to_pay(self):
        po = self.env["purchase.order"].create(
            {"partner_id": self.vendor.id, "order_line": [(0, 0, {"product_id": self.product.id, "product_qty": 3, "price_unit": 50.0})]}
        )
        po.button_confirm()
        self.assertEqual(po.state, "purchase")
        receipt = po.picking_ids
        self.assertEqual(len(receipt), 1)
        for move in receipt.move_ids:
            move.quantity = move.product_uom_qty
            move.picked = True
        receipt.button_validate()
        self.assertEqual(receipt.state, "done")
        po.action_create_invoice()
        bill = po.invoice_ids
        self.assertEqual(bill.move_type, "in_invoice")
        bill.invoice_date = fields_today(self.env)
        bill.action_post()
        self.assertEqual(bill.state, "posted")
        self.assertAlmostEqual(bill.amount_untaxed, 150.0)

    # odoo-functional-accounting
    def test_invoice_payment_and_reconciliation(self):
        invoice = self.env["account.move"].create(
            {
                "move_type": "out_invoice",
                "partner_id": self.partner.id,
                "invoice_line_ids": [(0, 0, {"product_id": self.product.id, "quantity": 1, "price_unit": 100.0})],
            }
        )
        invoice.action_post()
        receivable = invoice.line_ids.filtered(lambda line: line.account_id.account_type == "asset_receivable")
        self.assertEqual(len(receivable), 1)
        self.assertAlmostEqual(receivable.debit, invoice.amount_total)
        wizard = self.env["account.payment.register"].with_context(
            active_model="account.move", active_ids=invoice.ids
        ).create({})
        wizard.action_create_payments()
        self.assertIn(invoice.payment_state, ("paid", "in_payment"))
        self.assertTrue(receivable.reconciled or invoice.payment_state == "in_payment")

    # odoo-indonesia-accounting
    def test_indonesian_chart_loads(self):
        company = self.env["res.company"].create({"name": "Eval ID Co", "country_id": self.env.ref("base.id").id})
        self.env["account.chart.template"].try_loading("id", company, install_demo=False)
        accounts = self.env["account.account"].with_company(company).search([("company_ids", "in", company.id)])
        self.assertGreater(len(accounts), 50)
        taxes = self.env["account.tax"].with_company(company).search([("company_id", "=", company.id)])
        self.assertTrue(taxes, "the Indonesian template installs taxes")
        self.assertEqual(company.currency_id.name, "IDR")

    # odoo-functional-pos
    def test_pos_session_open_and_close(self):
        config = self.env["pos.config"].create({"name": "Eval POS"})
        config.with_user(self.env.user).open_ui()
        session = config.current_session_id
        self.assertEqual(session.state, "opening_control")
        session.set_opening_control(0, "")
        self.assertEqual(session.state, "opened")
        session.close_session_from_ui()
        self.assertEqual(session.state, "closed")

    # odoo-functional-manufacturing
    def test_manufacturing_order(self):
        bom = self.env["mrp.bom"].create(
            {
                "product_tmpl_id": self.product.product_tmpl_id.id,
                "product_qty": 1,
                "bom_line_ids": [(0, 0, {"product_id": self.component.id, "product_qty": 2})],
            }
        )
        self.env["stock.quant"]._update_available_quantity(self.component, self.warehouse.lot_stock_id, 10)
        mo = self.env["mrp.production"].create({"product_id": self.product.id, "product_qty": 1, "bom_id": bom.id})
        mo.action_confirm()
        mo.action_assign()
        mo.qty_producing = 1
        mo.button_mark_done()
        self.assertEqual(mo.state, "done")
        self.assertEqual(self.component.with_context(location=self.warehouse.lot_stock_id.id).qty_available, 8)

    # odoo-reporting
    def test_report_renders_html(self):
        so = self.env["sale.order"].create({"partner_id": self.partner.id})
        html = self.env["ir.actions.report"]._render_qweb_html("sale.report_saleorder", [so.id])[0]
        self.assertIn(so.name.encode(), html)

    # odoo-website-portal
    def test_portal_mixin_token_and_url(self):
        note = self.env["ocloud.eval.note"].create({"name": "portal", "partner_id": self.partner.id})
        token = note._portal_ensure_token()
        self.assertTrue(token)
        self.assertEqual(note.access_url, f"/my/eval-notes/{note.id}")
        self.assertTrue(self.env["website"].search([], limit=1))

    # odoo-data-model-diagram, odoo-live-context, odoo-live-read
    def test_metadata_and_bounded_reads(self):
        fields_meta = self.env["ir.model.fields"].search_read(
            [("model", "=", "sale.order"), ("name", "in", ["partner_id", "order_line"])], ["name", "ttype", "relation"]
        )
        self.assertEqual({f["name"]: f["relation"] for f in fields_meta}, {"partner_id": "res.partner", "order_line": "sale.order.line"})
        self.env["sale.order"].create({"partner_id": self.partner.id})
        # Odoo 20 orders read_group arguments as (domain, groupby, aggregates).
        groups = self.env["sale.order"]._read_group([("partner_id", "=", self.partner.id)], ["state"], ["amount_total:sum"])
        self.assertEqual(groups[0][0], "draft")
        rows = self.env["sale.order"].search_read([("partner_id", "=", self.partner.id)], ["name", "state"], limit=5)
        self.assertLessEqual(len(rows), 5)

    # odoo-solution-design (automation and mail options), odoo-integration-design
    def test_server_action_automation_and_mail_template(self):
        model = self.env["ir.model"]._get("res.partner")
        action = self.env["ir.actions.server"].create(
            {"name": "Eval set ref", "model_id": model.id, "state": "code", "code": "record.write({'ref': 'EVAL'})"}
        )
        action.with_context(active_model="res.partner", active_id=self.partner.id).run()
        self.assertEqual(self.partner.ref, "EVAL")
        triggers = dict(self.env["base.automation"]._fields["trigger"].selection)
        self.assertIn("on_create_or_write", triggers)
        template = self.env["mail.template"].create(
            {"name": "Eval", "model_id": model.id, "subject": "Hello {{ object.name }}"}
        )
        rendered = template._render_field("subject", self.partner.ids)[self.partner.id]
        self.assertEqual(rendered, "Hello Eval Customer")

    # project and timesheet (gap noted in coverage review)
    def test_project_task_timesheet(self):
        project = self.env["project.project"].create({"name": "Eval Project", "allow_timesheets": True})
        task = self.env["project.task"].create({"name": "Eval Task", "project_id": project.id})
        line = self.env["account.analytic.line"].create(
            {"name": "work", "project_id": project.id, "task_id": task.id, "unit_amount": 2.0, "employee_id": self._employee().id}
        )
        self.assertEqual(line.task_id, task)
        self.assertAlmostEqual(task.effective_hours, 2.0)

    def _employee(self):
        return self.env["hr.employee"].create({"name": "Eval Employee", "user_id": self.env.user.id})


def fields_today(env):
    from odoo import fields

    return fields.Date.context_today(env["res.partner"])


class TestMultiCompanyCurrency(TransactionCase):
    """odoo-security-audit, odoo-functional-accounting, odoo-functional-sales: company and currency boundaries."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company_a = cls.env.company
        cls.company_b = cls.env["res.company"].create({"name": "Eval Company B"})
        cls.user_b = new_test_user(
            cls.env, login="eval_user_b", groups="base.group_user,sales_team.group_sale_salesman",
            company_id=cls.company_b.id, company_ids=[(6, 0, [cls.company_b.id])],
        )
        cls.partner = cls.env["res.partner"].create({"name": "Eval MC Partner"})
        cls.product = cls.env["product.product"].create({"name": "Eval MC Product", "type": "consu", "list_price": 10.0})

    def test_company_record_rule_isolates_sale_orders(self):
        so_a = self.env["sale.order"].create({"partner_id": self.partner.id, "company_id": self.company_a.id})
        visible = self.env["sale.order"].with_user(self.user_b).search([("id", "=", so_a.id)])
        self.assertFalse(visible, "a user limited to company B must not see company A orders")
        with self.assertRaises(AccessError):
            so_a.with_user(self.user_b).read(["name"])
        so_b = self.env["sale.order"].with_user(self.user_b).with_company(self.company_b).create(
            {"partner_id": self.partner.id}
        )
        self.assertEqual(so_b.company_id, self.company_b)

    def test_foreign_currency_invoice_converts_to_company_currency(self):
        usd = self.env.ref("base.USD")
        company_currency = self.company_a.currency_id
        if usd == company_currency:
            usd = self.env.ref("base.EUR")
        usd.active = True
        self.env["res.currency.rate"].create(
            {"currency_id": usd.id, "company_id": self.company_a.id, "rate": 2.0, "name": fields_today(self.env)}
        )
        invoice = self.env["account.move"].create(
            {
                "move_type": "out_invoice",
                "partner_id": self.partner.id,
                "currency_id": usd.id,
                "invoice_date": fields_today(self.env),
                "invoice_line_ids": [(0, 0, {"product_id": self.product.id, "quantity": 1, "price_unit": 100.0, "tax_ids": [(5, 0, 0)]})],
            }
        )
        invoice.action_post()
        self.assertEqual(invoice.currency_id, usd)
        self.assertAlmostEqual(invoice.amount_total, 100.0)
        receivable = invoice.line_ids.filtered(lambda line: line.account_id.account_type == "asset_receivable")
        self.assertAlmostEqual(receivable.amount_currency, 100.0)
        self.assertAlmostEqual(receivable.balance, 50.0, msg="rate 2.0 converts 100 USD to 50 in company currency")
