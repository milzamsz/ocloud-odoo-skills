import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "odoo-dynamic-dashboard" / "scripts" / "validate_dashboard_xml.py"
FIXTURE = ROOT / "evals" / "fixtures" / "dynamic-dashboard-20" / "dashboard_invoicing.xml"


def run(*paths):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *map(str, paths)], capture_output=True, text=True, check=False
    )


def item(body, xid="item_x", context=True):
    ctx = " context=\"{'dd_skip_auto_layout': True}\"" if context else ""
    return f'<record id="{xid}" model="dynamic.dashboard.item"{ctx}>{body}</record>'


def write(tmp_path, *records):
    path = tmp_path / "dash.xml"
    path.write_text(
        '<odoo noupdate="1"><record id="d" model="dynamic.dashboard"><field name="name">D</field></record>'
        + "".join(records)
        + "</odoo>",
        encoding="utf-8",
    )
    return path


BASE = (
    '<field name="dashboard_id" ref="d"/><field name="item_type">tile</field>'
    "<field name=\"model_id\" search=\"[('model', '=', 'res.partner')]\"/>"
    '<field name="data_type">count</field>'
)


def grid(x, y, w, h):
    return "".join(f'<field name="grid_{k}">{v}</field>' for k, v in zip("xywh", (x, y, w, h)))


def test_fixture_is_valid():
    result = run(FIXTURE)
    assert result.returncode == 0, result.stdout
    assert "0 error(s)" in result.stdout


def test_overlap_grid_and_auto_layout_are_errors(tmp_path):
    path = write(
        tmp_path,
        item(BASE + grid(0, 0, 6, 2), "a"),
        item(BASE + grid(3, 1, 6, 2), "b"),
        item(BASE + grid(10, 0, 4, 2), "c"),
        item(BASE + grid(0, 4, 3, 2), "d", context=False),
    )
    out = run(path).stdout
    assert "items a and b overlap" in out
    assert "c: grid (10,0,4,2) outside" in out
    assert "d: grid set without context" in out


def test_sql_rules_match_the_addon(tmp_path):
    def sql(query, xid, groups=True):
        group = '<field name="allowed_group_ids" eval="[(6, 0, [ref(\'base.group_system\')])]"/>' if groups else ""
        return item(
            '<field name="dashboard_id" ref="d"/><field name="item_type">bar</field>'
            '<field name="data_calculation_type">sql</field>'
            f'<field name="query"><![CDATA[{query}]]></field>{group}',
            xid,
            context=False,
        )

    path = write(
        tmp_path,
        sql("SELECT 1 AS value WHERE company_id = {company_id}", "ok"),
        sql("DELETE FROM res_partner", "delete"),
        sql("SELECT 1; SELECT 2", "two"),
        sql("SELECT replace(name, 'a', 'b') FROM res_partner", "fn"),
        sql("SELECT 1 AS value", "nogroup", groups=False),
    )
    out = run(path).stdout
    assert "delete: SQL must start with SELECT or WITH" in out
    assert "two: SQL has more than one statement" in out
    assert "fn: SQL contains forbidden keyword 'replace'" in out
    assert "nogroup: SQL item bypasses record rules" in out
    assert "ERROR: dash.xml:ok" not in out


def test_measure_type_and_kpi_checks(tmp_path):
    path = write(
        tmp_path,
        item(
            '<field name="dashboard_id" ref="d"/><field name="item_type">pizza</field>'
            "<field name=\"model_id\" search=\"[('model', '=', 'res.partner')]\"/>"
            '<field name="data_type">sum</field>',
            "m",
            context=False,
        ),
        '<record id="k" model="dynamic.dashboard.kpi"><field name="name">K</field>'
        '<field name="computation_mode">formula</field></record>',
        '<record id="ks" model="dynamic.dashboard.kpi"><field name="name">S</field>'
        "<field name=\"model_id\" search=\"[('model', '=', 'res.partner')]\"/>"
        '<field name="aggregation">sum</field></record>',
    )
    out = run(path).stdout
    assert "m: unknown item_type 'pizza'" in out
    assert "m: data_type 'sum' needs measure_field_ids" in out
    assert "k: KPI in formula mode needs formula" in out
    assert "ks: KPI aggregation 'sum' fails on Odoo 20" in out


def test_rejects_non_xml_input(tmp_path):
    other = tmp_path / "dash.txt"
    other.write_text("x", encoding="utf-8")
    result = run(other)
    assert result.returncode == 1
    assert "not an existing .xml file" in result.stdout
