#!/usr/bin/env python3
"""Summarize proxy logs per case: total calls, refused calls, model.method list with status."""
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent / "logs"
def summary(case):
    f = ROOT / f"{case}.jsonl"
    if not f.exists():
        return {"case": case, "calls": 0, "refused": 0, "entries": []}
    rows = [json.loads(l) for l in f.read_text().splitlines() if l.strip()]
    return {"case": case, "calls": len(rows), "refused": sum(1 for r in rows if r.get("refused")),
            "cells": sorted({r.get("cell") for r in rows}),
            "entries": [f"{r['model']}.{r['method']} -> {'REFUSED' if r.get('refused') else r.get('status')}" for r in rows]}
if __name__ == "__main__":
    for case in sys.argv[1:]:
        print(json.dumps(summary(case), indent=1))
