#!/usr/bin/env python3
"""Read-only Odoo 20 JSON-2 proxy for skill evaluations.

Usage: odoo20q.py <ce|ee|ce-meta|ee-meta> <case_id> <model> <method> '<json kwargs>'
Only read methods are forwarded; every call (allowed or refused) is logged.
"""
import json, sys, urllib.request, urllib.error, pathlib, datetime
ROOT = pathlib.Path(__file__).resolve().parent
READ_METHODS = {"search_read", "search_count", "read", "read_group", "fields_get", "name_search", "search"}
PORTS = {"ce": 28069, "ee": 28070, "ce-meta": 28069, "ee-meta": 28070}
def main():
    if len(sys.argv) != 6:
        print(__doc__); return 2
    cell, case, model, method, raw = sys.argv[1:]
    log = ROOT / "logs" / f"{case}.jsonl"
    entry = {"ts": datetime.datetime.now(datetime.timezone.utc).isoformat(), "cell": cell, "model": model, "method": method}
    if model == "_server" and method == "version_info" and cell in PORTS:
        req = urllib.request.Request(f"http://127.0.0.1:{PORTS[cell]}/web/webclient/version_info",
                                     data=json.dumps({"jsonrpc": "2.0", "method": "call", "params": {}}).encode(),
                                     headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode()
        entry.update({"kwargs": {}, "status": 200, "bytes": len(body)})
        log.open("a").write(json.dumps(entry) + "\n")
        print(json.dumps({"status": 200, "result": json.loads(body).get("result")}, indent=1)); return 0
    if cell not in PORTS or method not in READ_METHODS or not model.replace(".", "").replace("_", "").isalnum():
        entry["refused"] = True
        log.open("a").write(json.dumps(entry) + "\n")
        print(json.dumps({"error": "refused: only read methods on a valid model are allowed", "allowed": sorted(READ_METHODS)})); return 3
    try:
        kwargs = json.loads(raw or "{}")
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"invalid JSON kwargs: {exc}"})); return 4
    key = (ROOT / "keys" / f"{cell}.key").read_text().strip()
    req = urllib.request.Request(f"http://127.0.0.1:{PORTS[cell]}/json/2/{model}/{method}", data=json.dumps(kwargs).encode(),
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            status, body = resp.status, resp.read().decode()
    except urllib.error.HTTPError as exc:
        status, body = exc.code, exc.read().decode()
    entry.update({"kwargs": kwargs, "status": status, "bytes": len(body)})
    log.open("a").write(json.dumps(entry) + "\n")
    print(json.dumps({"status": status, "result": json.loads(body) if body.startswith(("[", "{")) else body}, indent=1)[:20000])
    return 0
if __name__ == "__main__":
    sys.exit(main())
