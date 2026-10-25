# Run inside `odoo-bin shell`. Seeds realistic data and an evaluation reader; prints KEY=.
from datetime import datetime, timedelta
from odoo import fields
U = env['res.users']; fld = 'group_ids' if 'group_ids' in U._fields else 'groups_id'
def g(x):
    r = env.ref(x, raise_if_not_found=False); return r.id if r else None
company = env.company
partner = env['res.partner'].create({'name': 'Live Customer', 'email': 'customer@example.com'})
vendor = env['res.partner'].create({'name': 'Live Vendor'})
prod = env['product.product'].create({'name': 'Live Widget', 'type': 'consu', 'is_storable': True, 'list_price': 120.0, 'standard_price': 70.0})
comp = env['product.product'].create({'name': 'Live Component', 'type': 'consu', 'is_storable': True, 'standard_price': 15.0})
wh = env['stock.warehouse'].search([('company_id', '=', company.id)], limit=1)
env['stock.quant']._update_available_quantity(prod, wh.lot_stock_id, 20)
env['stock.quant']._update_available_quantity(comp, wh.lot_stock_id, 50)
so = env['sale.order'].create({'partner_id': partner.id, 'order_line': [(0, 0, {'product_id': prod.id, 'product_uom_qty': 3})]})
so.action_confirm()
for m in so.picking_ids.move_ids:
    m.quantity = m.product_uom_qty; m.picked = True
so.picking_ids.button_validate()
inv = so._create_invoices(); inv.action_post()
env['sale.order'].create({'partner_id': partner.id, 'order_line': [(0, 0, {'product_id': prod.id, 'product_uom_qty': 1})]})
po = env['purchase.order'].create({'partner_id': vendor.id, 'order_line': [(0, 0, {'product_id': comp.id, 'product_qty': 10, 'price_unit': 14.0})]})
po.button_confirm()
bom = env['mrp.bom'].create({'product_tmpl_id': prod.product_tmpl_id.id, 'product_qty': 1, 'bom_line_ids': [(0, 0, {'product_id': comp.id, 'product_qty': 2})]})
mo = env['mrp.production'].create({'product_id': prod.id, 'product_qty': 2, 'bom_id': bom.id}); mo.action_confirm()
env['pos.config'].create({'name': 'Live POS'})
idco = env['res.company'].create({'name': 'Live ID Co', 'country_id': env.ref('base.id').id})
env['account.chart.template'].try_loading('id', idco, install_demo=False)
env['project.project'].create({'name': 'Live Project', 'allow_timesheets': True})
env['ocloud.eval.note'].create({'name': 'Live note', 'partner_id': partner.id})
groups = [x for x in map(g, ['base.group_user', 'base.group_allow_export', 'sales_team.group_sale_salesman_all_leads', 'purchase.group_purchase_user', 'stock.group_stock_user', 'account.group_account_readonly', 'mrp.group_mrp_user', 'point_of_sale.group_pos_user', 'project.group_project_user']) if x]
reader = U.create({'name': 'Skill Evaluator', 'login': 'skill_evaluator', fld: [(6, 0, groups)], 'company_ids': [(6, 0, [company.id, idco.id])], 'company_id': company.id})
key = reader.with_user(reader).env['res.users.apikeys']._generate(scope='rpc', name='skill-eval', expiration_date=datetime.now() + timedelta(hours=8))
env.cr.commit()
print('KEY=' + key)
