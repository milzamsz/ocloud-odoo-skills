import json
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "odoo-process-flowchart"
BUILD = SKILL / "scripts" / "build.mjs"
EXAMPLE = SKILL / "assets" / "example-purchase-approval.json"

pytestmark = pytest.mark.skipif(shutil.which("node") is None, reason="node not installed")


def build(src, out):
    return subprocess.run(["node", str(BUILD), str(src), str(out)], capture_output=True, text=True, check=False)


def test_example_builds(tmp_path):
    result = build(EXAMPLE, tmp_path / "site")
    assert result.returncode == 0, result.stderr
    assert (tmp_path / "site" / "index.html").exists()
    js = (tmp_path / "site" / "process.js").read_text(encoding="utf-8")
    assert js.startswith("window.PROCESS = ")
    assert json.loads(js[len("window.PROCESS = "):].rstrip().rstrip(";"))["steps"][0]["id"] == "map"


@pytest.mark.parametrize(
    ("mutate", "message"),
    [
        (lambda d: d["edges"].append({"from": "1", "to": "nope", "d": "M0 0"}), "unknown node nope"),
        (lambda d: d["steps"].append(dict(d["steps"][1])), "duplicate step ids"),
        (lambda d: d["nodes"][0].update(y=5000), "centre outside every lane"),
        (lambda d: d["steps"][1].update(focus=["ghost"]), "unknown focus node ghost"),
        (lambda d: d.update(sections={"X": "missing"}), "unknown step missing"),
    ],
)
def test_structural_errors_are_rejected(tmp_path, mutate, message):
    data = json.loads(EXAMPLE.read_text(encoding="utf-8"))
    mutate(data)
    src = tmp_path / "bad.json"
    src.write_text(json.dumps(data), encoding="utf-8")
    result = build(src, tmp_path / "site")
    assert result.returncode == 1
    assert message in result.stderr
    assert not (tmp_path / "site").exists()
