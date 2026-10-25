#!/usr/bin/env python3
"""Validate dynamic_dashboard_ai_nexgen data XML before it is installed.

Usage: validate_dashboard_xml.py FILE.xml [FILE.xml ...]

Checks the rules the addon enforces at runtime (item types, grid bounds, data
source, SQL read-only rules, KPI configuration) plus layout overlap and the
dd_skip_auto_layout context. Exit code 1 when any error is found.
"""

from __future__ import annotations

import ast
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ITEM_TYPES = {
    "tile", "kpi", "scorecard", "bar", "barLine", "horizontalBar", "line", "area", "stepLine",
    "smoothedLine", "waterfall", "pie", "doughnut", "polarArea", "radar", "flower", "scatter",
    "radialBar", "gauge", "funnel", "pyramid", "pictorial", "bullet", "treemap", "sunburst",
    "forceDirected", "pack", "tree", "partition", "voronoiTreemap", "sankey", "chord",
    "chordDirected", "chordNonRibbon", "arcDiagram", "map", "mapPoints", "heatmap",
    "matrixHeatmap", "wordCloud", "venn", "candlestick", "ohlc", "timeline", "serpentine",
    "spiral", "list", "todo", "iframe", "odoo_view",
}
NO_SOURCE_TYPES = {"todo", "iframe", "odoo_view"}
TILE_ICONS = {
    "fa-bar-chart", "fa-line-chart", "fa-area-chart", "fa-pie-chart", "fa-dashboard",
    "fa-tachometer", "fa-money", "fa-usd", "fa-eur", "fa-shopping-cart", "fa-credit-card",
    "fa-truck", "fa-archive", "fa-calculator", "fa-users", "fa-user", "fa-building",
    "fa-briefcase", "fa-database", "fa-flask", "fa-list", "fa-check", "fa-star", "fa-heart",
    "fa-globe", "fa-calendar", "fa-clock-o", "fa-envelope", "fa-phone", "fa-tag", "fa-tags",
    "fa-cubes", "fa-cube", "fa-percent", "fa-signal", "fa-trophy", "fa-bolt", "fa-fire",
    "fa-leaf", "fa-home",
}
DATE_FILTERS = {
    "none", "today", "yesterday", "tomorrow", "this_week", "this_month", "this_quarter",
    "this_year", "next_week", "next_month", "next_quarter", "next_year", "week_to_date",
    "month_to_date", "year_to_date", "last_7_days", "last_30_days", "last_90_days",
    "last_week", "last_month", "last_quarter", "last_year", "past_until_now",
    "future_starting_now", "custom", "user_defined",
}
DATE_GRAINS = {"minute", "hour", "day", "week", "month", "quarter", "year"}
CALC_TYPES = {"custom", "sql", "api", "excel", "csv", "scrape", "sheets"}
# Same rule as the addon's _SQL_FORBIDDEN / _validate_sql_query.
SQL_FORBIDDEN = re.compile(
    r"\b(INSERT|UPDATE|DELETE|DROP|ALTER|CREATE|TRUNCATE|GRANT|REVOKE|COPY|"
    r"EXECUTE|EXEC|CALL|MERGE|REPLACE|ATTACH|DETACH|VACUUM|REINDEX|CLUSTER|"
    r"COMMENT|LISTEN|NOTIFY|LOAD|INTO\s+OUTFILE|INTO\s+DUMPFILE|"
    r"SET\s+ROLE|SET\s+SESSION|SECURITY\s+DEFINER)\b",
    re.IGNORECASE,
)
GRID = ("grid_x", "grid_y", "grid_w", "grid_h")


def sql_error(query: str) -> str | None:
    cleaned = re.sub(r"/\*.*?\*/", "", query, flags=re.DOTALL)
    cleaned = re.sub(r"--.*?$", "", cleaned, flags=re.MULTILINE).strip()
    body = cleaned.rstrip(";").strip()
    if not body:
        return "SQL query is empty"
    if ";" in body:
        return "SQL has more than one statement"
    if not re.match(r"^(WITH|SELECT)\b", body.lstrip("(").strip(), re.IGNORECASE):
        return "SQL must start with SELECT or WITH"
    match = SQL_FORBIDDEN.search(body)
    if match:
        return f"SQL contains forbidden keyword {match.group(0)!r} (the addon rejects it)"
    return None


def field_values(record: ET.Element) -> dict[str, ET.Element]:
    return {f.get("name"): f for f in record.findall("field")}


def text(field: ET.Element | None) -> str | None:
    if field is None:
        return None
    value = field.get("eval") if field.get("eval") is not None else (field.text or "")
    return value.strip()


def is_set(field: ET.Element | None) -> bool:
    if field is None:
        return False
    return bool(field.get("ref") or field.get("search") or text(field))


def validate(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        return [f"{path}: not well-formed XML: {exc}"], []
    if root.tag != "odoo":
        errors.append(f"{path}: root element must be <odoo>")
    records = root.iter("record")
    dashboards: set[str] = set()
    layout: dict[str, list[tuple[str, int, int, int, int]]] = {}
    noupdate = root.get("noupdate") in ("1", "True", "true") or any(
        d.get("noupdate") in ("1", "True", "true") for d in root.iter("data")
    )
    if not noupdate:
        warnings.append(f"{path}: no noupdate=\"1\"; module updates will overwrite user edits")

    for record in records:
        model, xid = record.get("model"), record.get("id") or "<no id>"
        fields = field_values(record)
        where = f"{path.name}:{xid}"

        if model == "dynamic.dashboard":
            dashboards.add(xid)
            if not is_set(fields.get("name")):
                errors.append(f"{where}: dashboard needs a name")

        elif model == "dynamic.dashboard.item":
            item_type = text(fields.get("item_type")) or "tile"
            calc = text(fields.get("data_calculation_type")) or "custom"
            dashboard = fields.get("dashboard_id")
            if dashboard is None or not dashboard.get("ref"):
                errors.append(f"{where}: dashboard_id must be set with ref=")
            if item_type not in ITEM_TYPES:
                errors.append(f"{where}: unknown item_type {item_type!r}")
            if calc not in CALC_TYPES:
                errors.append(f"{where}: unknown data_calculation_type {calc!r}")
            icon = text(fields.get("tile_icon"))
            if icon and icon not in TILE_ICONS:
                errors.append(f"{where}: unknown tile_icon {icon!r}")
            has_kpi = is_set(fields.get("kpi_id")) or is_set(fields.get("analysis_id"))

            if calc == "custom" and item_type not in NO_SOURCE_TYPES and not has_kpi:
                if not is_set(fields.get("model_id")):
                    errors.append(f"{where}: Odoo-model item needs model_id")
                data_type = text(fields.get("data_type")) or "sum"
                if data_type in ("sum", "average") and item_type != "list" and not is_set(
                    fields.get("measure_field_ids")
                ):
                    errors.append(f"{where}: data_type {data_type!r} needs measure_field_ids")
            if calc == "sql":
                query = text(fields.get("query"))
                problem = sql_error(query or "")
                if problem:
                    errors.append(f"{where}: {problem}")
                if not is_set(fields.get("allowed_group_ids")):
                    errors.append(f"{where}: SQL item bypasses record rules; set allowed_group_ids")
                if query and "company_id" in query and not re.search(
                    r"\{company_id\}|%COMPANY_ID%", query
                ):
                    warnings.append(f"{where}: SQL filters company_id without {{company_id}}")
                elif query and "company_id" not in query:
                    warnings.append(f"{where}: SQL has no company filter; confirm the tables are not company-owned")
            if calc in ("api", "excel", "csv", "scrape", "sheets"):
                warnings.append(f"{where}: data_calculation_type {calc!r} needs a connection or file; not covered by this skill")

            domain = text(fields.get("domain"))
            if domain:
                try:
                    if not isinstance(ast.literal_eval(domain), list):
                        errors.append(f"{where}: domain must be a list")
                except (ValueError, SyntaxError):
                    warnings.append(f"{where}: domain is not a plain literal; check it evaluates on the server")
            date_filter = text(fields.get("date_filter_selection"))
            if date_filter and date_filter not in DATE_FILTERS:
                errors.append(f"{where}: unknown date_filter_selection {date_filter!r}")
            if date_filter and date_filter != "none" and calc == "custom" and not has_kpi and not is_set(
                fields.get("date_filter_field_id")
            ):
                errors.append(f"{where}: date_filter_selection needs date_filter_field_id")
            if date_filter == "custom" and not (
                is_set(fields.get("item_start_date")) and is_set(fields.get("item_end_date"))
            ):
                errors.append(f"{where}: custom date filter needs item_start_date and item_end_date")
            for grain_field in ("group_by_date_type", "sub_group_by_date_type"):
                grain = text(fields.get(grain_field))
                if grain and grain not in DATE_GRAINS:
                    errors.append(f"{where}: unknown {grain_field} {grain!r}")

            grid = [text(fields.get(name)) for name in GRID]
            if any(value is not None for value in grid):
                if "dd_skip_auto_layout" not in (record.get("context") or ""):
                    errors.append(
                        f"{where}: grid set without context=\"{{'dd_skip_auto_layout': True}}\"; the addon will replace it"
                    )
                try:
                    x, y, w, h = (int(value) for value in grid)
                except (TypeError, ValueError):
                    errors.append(f"{where}: grid_x, grid_y, grid_w, grid_h must all be integers")
                else:
                    if x < 0 or y < 0 or h < 1 or not 1 <= w <= 12 or x + w > 12:
                        errors.append(f"{where}: grid ({x},{y},{w},{h}) outside the 12-column board")
                    if dashboard is not None and dashboard.get("ref"):
                        layout.setdefault(dashboard.get("ref"), []).append((xid, x, y, w, h))
            else:
                warnings.append(f"{where}: no grid; the addon will place the item automatically")

        elif model == "dynamic.dashboard.kpi":
            mode = text(fields.get("computation_mode")) or "model"
            aggregation = text(fields.get("aggregation")) or "sum"
            if mode == "model":
                if not is_set(fields.get("model_id")):
                    errors.append(f"{where}: KPI in model mode needs model_id")
                if aggregation in ("sum", "average"):
                    # Addon 20.0.1.0.15 calls read_group with the pre-Odoo-20 argument order here.
                    errors.append(
                        f"{where}: KPI aggregation {aggregation!r} fails on Odoo 20 with addon 20.0.1.0.15; "
                        "use a count KPI or a tile with target lines"
                    )
            elif mode == "formula" and not is_set(fields.get("formula")):
                errors.append(f"{where}: KPI in formula mode needs formula")
            elif mode not in ("model", "formula", "children"):
                errors.append(f"{where}: unknown computation_mode {mode!r}")

        for name, field in fields.items():
            search = field.get("search")
            if search and name in {
                "measure_field_ids", "measure_field_2_ids", "group_by_field_id",
                "sub_group_by_field_id", "sort_by_field_id", "list_view_field_ids",
                "date_filter_field_id", "measure_field_id", "filter_field_id",
            } and "'model'" not in search:
                errors.append(f"{where}: {name} search must include ('model', '=', ...) to pick one model's field")

    for dashboard, items in layout.items():
        for i, (a, ax, ay, aw, ah) in enumerate(items):
            for b, bx, by, bw, bh in items[i + 1:]:
                if ax < bx + bw and bx < ax + aw and ay < by + bh and by < ay + ah:
                    errors.append(f"{path.name}: items {a} and {b} overlap on {dashboard}")
    return errors, warnings


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__.strip().splitlines()[2], file=sys.stderr)
        return 2
    total_errors = 0
    for name in argv:
        path = Path(name)
        if path.suffix.lower() != ".xml" or not path.is_file():
            print(f"ERROR: {name}: not an existing .xml file")
            total_errors += 1
            continue
        errors, warnings = validate(path)
        for message in errors:
            print(f"ERROR: {message}")
        for message in warnings:
            print(f"WARNING: {message}")
        total_errors += len(errors)
        print(f"{path.name}: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
