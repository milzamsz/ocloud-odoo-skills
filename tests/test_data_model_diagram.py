import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "odoo-data-model-diagram" / "scripts" / "model_graph_to_dbml.py"
FIXTURE = ROOT / "evals" / "fixtures" / "data-model-diagram-18"
SKILL = ROOT / "skills" / "odoo-data-model-diagram" / "SKILL.md"
DRAWDB_DIR = Path("/home/milzam/Workspace/tools/drawdb")


def test_model_graph_converter_generates_stable_logical_dbml(tmp_path):
    output = tmp_path / "diagram.dbml"
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--input", str(FIXTURE / "model-graph.json"), "--output", str(output)],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert output.read_text(encoding="utf-8") == (FIXTURE / "expected.dbml").read_text(encoding="utf-8")

    invalid = tmp_path / "invalid.json"
    invalid.write_text('{"title": "bad", "models": [{"name": "x", "fields": [{"name": "id"}]}]}', encoding="utf-8")
    failure = subprocess.run(
        [sys.executable, str(SCRIPT), "--input", str(invalid), "--output", str(output)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert failure.returncode == 1
    assert "type for x.id" in failure.stderr


def test_skill_names_only_metadata_tools_and_drawdb_boundaries():
    skill = SKILL.read_text(encoding="utf-8")

    assert "odoo_list_models" in skill
    assert "odoo_get_model_metadata" in skill
    assert "odoo_check_access" in skill
    assert "odoo_search_read" in skill
    assert "odoo_read" in skill
    assert "odoo_execute" in skill
    assert "odoo_create" in skill
    assert "odoo_write" in skill or "odoo_update" in skill
    assert "one relation hop" in skill or "one-hop" in skill
    assert "30 models" in skill
    assert "physical PostgreSQL" in skill
    assert "business records" in skill


def test_converter_renders_relation_stub_and_skips_one2many_column(tmp_path):
    graph = {
        "title": "Edge cases",
        "roots": ["x.parent"],
        "models": [
            {
                "name": "x.parent",
                "fields": [
                    {"name": "id", "type": "integer"},
                    {"name": "child_ids", "type": "one2many", "relation": "x.child", "inverse": "parent_id"},
                    {"name": "tag_ids", "type": "many2many", "relation": "x.tag"},
                ],
            },
        ],
    }
    input_path = tmp_path / "graph.json"
    output_path = tmp_path / "diagram.dbml"
    input_path.write_text(json.dumps(graph), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--input", str(input_path), "--output", str(output_path)],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    dbml = output_path.read_text(encoding="utf-8")
    assert 'Table "x.tag"' in dbml
    assert "stub: related model metadata unavailable" in dbml
    assert "logical_m2m__x_parent__tag_ids" in dbml
    assert '"child_ids"' not in dbml
    assert "one2many=child_ids" in dbml


@pytest.mark.skipif(
    shutil.which("node") is None or not (DRAWDB_DIR / "node_modules" / "@dbml" / "core").is_dir(),
    reason="local drawDB checkout with @dbml/core is required for DBML parser verification",
)
def test_expected_dbml_parses_in_drawdb():
    script = (
        "const fs=require('fs');const {Parser}=require('@dbml/core');"
        f"const src=fs.readFileSync({str(FIXTURE / 'expected.dbml')!r},'utf8');"
        "const schema=new Parser().parse(src,'dbmlv2').schemas[0];"
        "if(schema.tables.length!==6||schema.refs.length!==5)process.exit(1);"
        "console.log('tables='+schema.tables.length+' refs='+schema.refs.length);"
    )
    result = subprocess.run(
        ["node", "-e", script],
        capture_output=True,
        text=True,
        check=False,
        cwd=DRAWDB_DIR,
    )

    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "tables=6 refs=5"
