"""Opt-in end-to-end test against a configured live Odoo MCP instance.

This test is skipped unless ``OCLOUD_ODOO_E2E_INSTANCE`` is set, because it
requires a reachable, authorised, read-only Odoo instance. It never hard-codes a
client instance name, host, or credential: the instance identifier comes from
the environment and the endpoint defaults to the local MCP server.

It exercises the same contract as ``skills/odoo-data-model-diagram``:

* only the read-only metadata allowlist is used
  (``odoo_list_models``, ``odoo_get_model_metadata``,
  ``odoo_check_access`` with ``operation=read``);
* the bundled converter turns live metadata into drawDB-importable DBML;
* the generated DBML parses with the drawDB ``@dbml/core`` parser when the
  local drawDB checkout is available.

Run it explicitly with, for example::

    OCLOUD_ODOO_E2E_INSTANCE=my-instance pytest -q tests/test_data_model_diagram_live.py
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "odoo-data-model-diagram" / "scripts" / "model_graph_to_dbml.py"
DRAWDB_DIR = Path("/home/milzam/Workspace/tools/drawdb")

INSTANCE = os.environ.get("OCLOUD_ODOO_E2E_INSTANCE")
ENDPOINT = os.environ.get("OCLOUD_ODOO_MCP_ENDPOINT", "http://127.0.0.1:8787/mcp")

# Bounded root set: one workflow root plus its direct relation targets.
ROOTS = ["sale.order", "sale.order.line", "stock.picking", "sale.workflow.process"]

ALLOWED_TOOLS = {"odoo_list_models", "odoo_get_model_metadata", "odoo_check_access"}
DENIED_TOOLS = {
    "odoo_read",
    "odoo_search_read",
    "odoo_count",
    "odoo_name_search",
    "odoo_name_get",
    "odoo_read_group",
    "odoo_default_get",
    "odoo_onchange",
    "odoo_generate_report",
    "odoo_execute",
    "odoo_execute_capability",
    "odoo_create",
    "odoo_create_batch",
    "odoo_update",
    "odoo_delete",
    "odoo_copy",
    "odoo_workflow_action",
}

pytestmark = pytest.mark.skipif(
    not INSTANCE,
    reason="set OCLOUD_ODOO_E2E_INSTANCE to run the live read-only metadata test",
)


class McpClient:
    """Minimal JSON-RPC client for the local Odoo MCP endpoint."""

    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint
        self.session_id: str | None = None
        self._next_id = 0

    def _rpc(self, method: str, params: dict | None = None) -> dict:
        self._next_id += 1
        payload: dict = {"jsonrpc": "2.0", "id": self._next_id, "method": method}
        if params is not None:
            payload["params"] = params
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
        }
        if self.session_id:
            headers["mcp-session-id"] = self.session_id
        request = urllib.request.Request(
            self.endpoint,
            data=json.dumps(payload).encode("utf-8"),
            headers=headers,
            method="POST",
        )
        with urllib.request.urlopen(request, timeout=60) as response:
            if not self.session_id:
                self.session_id = response.headers.get("mcp-session-id")
            body = response.read().decode("utf-8")
        for line in body.splitlines():
            line = line.strip()
            if line.startswith("data:"):
                line = line[len("data:") :].strip()
            if line.startswith("{"):
                return json.loads(line)
        raise AssertionError(f"no JSON payload in MCP response: {body[:200]}")

    def initialize(self) -> None:
        self._rpc(
            "initialize",
            {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "ocloud-diagram-e2e", "version": "0.1.0"},
            },
        )

    def call_tool(self, name: str, arguments: dict) -> dict:
        assert name in ALLOWED_TOOLS, f"tool {name!r} is outside the read-only allowlist"
        result = self._rpc("tools/call", {"name": name, "arguments": arguments})
        assert "error" not in result, f"{name} failed: {result.get('error')}"
        content = result["result"].get("content", [])
        text = "".join(part.get("text", "") for part in content if part.get("type") == "text")
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {"raw": text}


def build_graph(client: McpClient) -> dict:
    """Turn live metadata for the bounded roots into a canonical model graph."""
    fields_by_model = {}
    for model in ROOTS:
        access = client.call_tool(
            "odoo_check_access",
            {"instance": INSTANCE, "model": model, "operation": "read"},
        )
        assert access.get("has_access") is True, f"no read access to {model}"
        payload = client.call_tool(
            "odoo_get_model_metadata", {"instance": INSTANCE, "model": model}
        )
        fields_by_model[model] = payload["model"]["fields"]

    graph = {"title": "Live read-only Odoo model diagram", "roots": [ROOTS[0]], "models": []}
    for model in ROOTS:
        fields = fields_by_model[model]
        entry = {
            "name": model,
            "evidence": ["live"],
            "fields": [
                {
                    "name": name,
                    "type": spec["type"],
                    **({"relation": spec["relation"]} if spec.get("relation") else {}),
                    "evidence": ["live"],
                }
                for name, spec in sorted(fields.items())
                if spec.get("type") in {"many2one", "char", "boolean", "integer", "selection", "date"}
            ],
        }
        graph["models"].append(entry)
    return graph


def test_live_metadata_allowlist_excludes_mutation_and_record_tools():
    """The test harness itself must never reference a denylisted tool."""
    import re
    from collections import Counter

    source = Path(__file__).read_text(encoding="utf-8")
    # Match whole quoted tokens so `odoo_read` is not confused with
    # `odoo_read_group`, and `odoo_execute` not with `odoo_execute_capability`.
    counts = Counter(re.findall(r'"([a-z_]+)"', source))
    for tool in DENIED_TOOLS:
        assert tool not in ALLOWED_TOOLS
        assert counts[tool] == 1, f"{tool} is referenced outside the denylist declaration"


def test_live_metadata_generates_drawdb_parseable_dbml(tmp_path):
    client = McpClient(ENDPOINT)
    client.initialize()

    listing = client.call_tool(
        "odoo_list_models",
        {"instance": INSTANCE, "domain": [["model", "in", ROOTS]], "limit": 50},
    )
    present = {row["model"] for row in listing.get("models", [])}
    assert present, f"none of the bounded roots exist on {INSTANCE}"

    graph = build_graph(client)
    graph_path = tmp_path / "model-graph.json"
    graph_path.write_text(json.dumps(graph, indent=2, sort_keys=True), encoding="utf-8")

    dbml_path = tmp_path / "diagram.dbml"
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--input", str(graph_path), "--output", str(dbml_path)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr

    dbml = dbml_path.read_text(encoding="utf-8")
    assert dbml.startswith("Project "), dbml[:80]
    for model in ROOTS:
        assert f'Table "{model}"' in dbml

    if shutil.which("node") is None or not (DRAWDB_DIR / "node_modules" / "@dbml" / "core").is_dir():
        pytest.skip("local drawDB checkout with @dbml/core is required for parser verification")

    script = (
        "const fs=require('fs');const {Parser}=require('@dbml/core');"
        f"const src=fs.readFileSync({str(dbml_path)!r},'utf8');"
        "const s=new Parser().parse(src,'dbmlv2').schemas[0];"
        "console.log('tables='+s.tables.length+' refs='+s.refs.length);"
    )
    parsed = subprocess.run(
        ["node", "-e", script], capture_output=True, text=True, check=False, cwd=DRAWDB_DIR
    )
    assert parsed.returncode == 0, parsed.stderr
    assert parsed.stdout.strip().startswith("tables=")
