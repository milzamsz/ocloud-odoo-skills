#!/usr/bin/env python3
"""Convert a bounded logical Odoo model graph into drawDB-importable DBML."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


TYPE_MAP = {
    "binary": "BLOB",
    "boolean": "BOOLEAN",
    "char": "VARCHAR",
    "date": "DATE",
    "datetime": "TIMESTAMP",
    "float": "FLOAT",
    "html": "TEXT",
    "image": "BLOB",
    "integer": "BIGINT",
    "json": "JSON",
    "many2one": "BIGINT",
    "many2one_reference": "VARCHAR",
    "monetary": "DECIMAL",
    "properties": "JSON",
    "reference": "VARCHAR",
    "selection": "VARCHAR",
    "text": "TEXT",
}


def quote(value: str) -> str:
    """Quote an identifier for DBML without guessing whether it is safe."""
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def note(value: str) -> str:
    return "'" + value.replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ") + "'"


def require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")
    return value.strip()


def list_of_strings(value: Any, label: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"{label} must be an array of strings")
    return [item for item in value if item]


def validate_graph(data: Any) -> tuple[str, list[dict[str, Any]]]:
    if not isinstance(data, dict):
        raise ValueError("model graph must be a JSON object")
    title = require_string(data.get("title"), "title")
    models = data.get("models")
    if not isinstance(models, list) or not models:
        raise ValueError("models must be a non-empty array")

    names: set[str] = set()
    for model in models:
        if not isinstance(model, dict):
            raise ValueError("each model must be an object")
        model_name = require_string(model.get("name"), "model name")
        if model_name in names:
            raise ValueError(f"duplicate model: {model_name}")
        names.add(model_name)
        fields = model.get("fields", [])
        if not isinstance(fields, list):
            raise ValueError(f"fields for {model_name} must be an array")
        field_names: set[str] = set()
        for field in fields:
            if not isinstance(field, dict):
                raise ValueError(f"field in {model_name} must be an object")
            field_name = require_string(field.get("name"), f"field name in {model_name}")
            require_string(field.get("type"), f"type for {model_name}.{field_name}")
            if field_name in field_names:
                raise ValueError(f"duplicate field: {model_name}.{field_name}")
            field_names.add(field_name)
    return title, models


def field_note(field: dict[str, Any]) -> str:
    parts: list[str] = []
    label = field.get("label")
    if isinstance(label, str) and label:
        parts.append(label)
    for key in ("required", "readonly", "store", "compute", "related", "index"):
        if key in field and field[key] is not None:
            parts.append(f"{key}={str(field[key]).lower()}")
    selection = field.get("selection")
    if isinstance(selection, list) and selection:
        parts.append("selection=" + ", ".join(str(item) for item in selection))
    evidence = list_of_strings(field.get("evidence"), "field evidence")
    if evidence:
        parts.append("evidence=" + ",".join(evidence))
    return "; ".join(parts)


def model_note(model: dict[str, Any], stub: bool = False) -> str:
    parts: list[str] = []
    label = model.get("label")
    if isinstance(label, str) and label:
        parts.append(label)
    if stub:
        parts.append("stub: related model metadata unavailable")
    for key in ("module", "auto", "table"):
        if key in model and model[key] is not None:
            parts.append(f"{key}={model[key]}")
    inherits = list_of_strings(model.get("inherits"), "model inherits")
    if inherits:
        parts.append("inherits=" + ", ".join(inherits))
    delegates = model.get("delegates")
    if isinstance(delegates, dict) and delegates:
        parts.append("delegates=" + ", ".join(f"{key}->{value}" for key, value in delegates.items()))
    evidence = list_of_strings(model.get("evidence"), "model evidence")
    if evidence:
        parts.append("evidence=" + ",".join(evidence))
    return "; ".join(parts)


def field_type(field: dict[str, Any]) -> str:
    return TYPE_MAP.get(str(field["type"]).lower(), "VARCHAR")


def bridge_name(model_name: str, field_name: str) -> str:
    cleaned = "".join(char if char.isalnum() else "_" for char in model_name)
    return f"logical_m2m__{cleaned}__{field_name}"


def column_name(model_name: str, suffix: str) -> str:
    cleaned = "".join(char if char.isalnum() else "_" for char in model_name).strip("_")
    return f"{cleaned}_{suffix}" if cleaned else suffix


def render(data: Any) -> str:
    title, input_models = validate_graph(data)
    models = {model["name"]: {**model, "fields": list(model.get("fields", []))} for model in input_models}
    stubs: set[str] = set()

    for model in list(models.values()):
        for field in model["fields"]:
            if str(field["type"]).lower() in {"many2one", "many2many"}:
                relation = field.get("relation")
                if isinstance(relation, str) and relation and relation not in models:
                    models[relation] = {"name": relation, "fields": [{"name": "id", "type": "integer"}]}
                    stubs.add(relation)

    blocks = [f"Project {quote(title)} {{\n}}"]
    references: list[str] = []
    bridges: list[dict[str, str]] = []

    for model_name in sorted(models):
        model = models[model_name]
        fields = model["fields"]
        if not any(field["name"] == "id" for field in fields):
            fields = [{"name": "id", "type": "integer"}, *fields]
        lines: list[str] = []
        one_to_many: list[str] = []
        for field in sorted(fields, key=lambda item: (item["name"] != "id", item["name"])):
            kind = str(field["type"]).lower()
            if kind == "one2many":
                one_to_many.append(field["name"])
                continue
            if kind == "many2many":
                relation = field.get("relation")
                if isinstance(relation, str) and relation:
                    bridges.append({"source": model_name, "field": field["name"], "target": relation})
                continue
            settings: list[str] = []
            if field["name"] == "id":
                settings.append("pk")
            annotation = field_note(field)
            if annotation:
                settings.append(f"note: {note(annotation)}")
            suffix = f" [ {', '.join(settings)} ]" if settings else ""
            lines.append(f"\t{quote(field['name'])} {field_type(field)}{suffix}")
            if kind == "many2one" and isinstance(field.get("relation"), str) and field["relation"]:
                references.append(
                    f"Ref {{\n\t{quote(model_name)}.{quote(field['name'])} > "
                    f"{quote(field['relation'])}.{quote('id')} [delete: no action, update: no action]\n}}"
                )
        annotation = model_note(model, model_name in stubs)
        if one_to_many:
            annotation = "; ".join(part for part in (annotation, "one2many=" + ", ".join(one_to_many)) if part)
        if annotation:
            lines.append(f"\tNote: {note(annotation)}")
        blocks.append(f"Table {quote(model_name)} {{\n" + "\n".join(lines) + "\n}")

    for bridge in sorted(bridges, key=lambda item: (item["source"], item["field"])):
        name = bridge_name(bridge["source"], bridge["field"])
        source_column = column_name(bridge["source"], "id")
        target_column = column_name(bridge["target"], "id")
        if source_column == target_column:
            source_column, target_column = "source_id", "target_id"
        blocks.append(
            f"Table {quote(name)} {{\n"
            f"\t{quote(source_column)} BIGINT [note: 'logical many2many source']\n"
            f"\t{quote(target_column)} BIGINT [note: 'logical many2many target']\n"
            f"\tNote: 'synthetic logical bridge for {bridge['source']}.{bridge['field']}; not a physical join-table claim'\n"
            "}"
        )
        references.extend(
            [
                f"Ref {{\n\t{quote(name)}.{quote(source_column)} > {quote(bridge['source'])}.{quote('id')} [delete: no action, update: no action]\n}}",
                f"Ref {{\n\t{quote(name)}.{quote(target_column)} > {quote(bridge['target'])}.{quote('id')} [delete: no action, update: no action]\n}}",
            ]
        )
    return "\n\n".join([*blocks, *references]) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="Canonical model graph JSON")
    parser.add_argument("--output", type=Path, required=True, help="Destination DBML file")
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        args.output.write_text(render(data), encoding="utf-8")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
