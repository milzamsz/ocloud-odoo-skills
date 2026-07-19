#!/usr/bin/env python3
"""Validate OCloud Odoo Skills repository structure and metadata."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
MIN_TRIGGER_CASES_PER_CLASS = 8
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
DANGEROUS_PATTERNS = {
    "broad recursive deletion": re.compile(r"rm\s+-rf\s+/(?:\s|$)"),
    "curl piped to shell": re.compile(r"curl[^\n|]*\|\s*(?:ba)?sh"),
    "wget piped to shell": re.compile(r"wget[^\n|]*\|\s*(?:ba)?sh"),
    "database drop": re.compile(r"\bDROP\s+DATABASE\b", re.IGNORECASE),
}


def parse_skill(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("missing YAML frontmatter")
    data = yaml.safe_load(match.group(1)) or {}
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a mapping")
    return data, text[match.end():]


def validate_links(skill_dir: Path, body: str) -> list[str]:
    errors: list[str] = []
    for target in LINK_RE.findall(body):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        clean = target.split("#", 1)[0]
        if not clean:
            continue
        resolved = (skill_dir / clean).resolve()
        try:
            resolved.relative_to(skill_dir.resolve())
        except ValueError:
            errors.append(f"reference escapes skill directory: {target}")
            continue
        if not resolved.exists():
            errors.append(f"missing referenced file: {target}")
    return errors


def validate_skill(skill_dir: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    path = skill_dir / "SKILL.md"
    if not path.exists():
        return ["missing SKILL.md"], warnings
    try:
        meta, body = parse_skill(path)
    except Exception as exc:  # noqa: BLE001
        return [str(exc)], warnings
    name = meta.get("name")
    description = meta.get("description")
    if not isinstance(name, str) or not NAME_RE.fullmatch(name):
        errors.append("invalid or missing name")
    elif name != skill_dir.name:
        errors.append(f"name {name!r} does not match directory {skill_dir.name!r}")
    if not isinstance(description, str) or not description.strip():
        errors.append("missing description")
    elif len(description) > 1024:
        errors.append("description exceeds 1024 characters")
    elif "Use this skill when" not in description:
        warnings.append("description should state 'Use this skill when'")
    lines = body.count("\n") + 1
    words = len(body.split())
    if lines > 500:
        warnings.append(f"SKILL.md body has {lines} lines; recommended maximum is 500")
    if words > 7000:
        warnings.append(f"SKILL.md body has {words} words; inspect token budget")
    errors.extend(validate_links(skill_dir, body))
    for label, pattern in DANGEROUS_PATTERNS.items():
        if pattern.search(path.read_text(encoding="utf-8")):
            warnings.append(f"dangerous pattern requires review: {label}")
    trigger = ROOT / "evals" / "trigger" / f"{skill_dir.name}.json"
    if not trigger.exists():
        warnings.append("missing trigger evaluation file")
    return errors, warnings


def validate_trigger_files() -> list[str]:
    errors: list[str] = []
    schema = json.loads((ROOT / "schemas" / "trigger-eval.schema.json").read_text())
    validator = Draft202012Validator(schema)
    for path in sorted((ROOT / "evals" / "trigger").glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
            continue
        for error in validator.iter_errors(data):
            errors.append(f"{path.relative_to(ROOT)}: {error.message}")
        positives = sum(1 for row in data if row.get("should_trigger") is True)
        negatives = sum(1 for row in data if row.get("should_trigger") is False)
        if positives < MIN_TRIGGER_CASES_PER_CLASS or negatives < MIN_TRIGGER_CASES_PER_CLASS:
            errors.append(
                f"{path.relative_to(ROOT)}: need at least "
                f"{MIN_TRIGGER_CASES_PER_CLASS} positive and "
                f"{MIN_TRIGGER_CASES_PER_CLASS} negative cases "
                f"(found {positives} positive, {negatives} negative)"
            )
    return errors


def validate_outcome_cases(skill_names: set[str]) -> list[str]:
    errors: list[str] = []
    path = ROOT / "evals" / "outcome" / "cases.yaml"
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as exc:
        return [f"{path.relative_to(ROOT)}: invalid YAML: {exc}"]
    cases = data.get("cases") if isinstance(data, dict) else None
    if not isinstance(cases, list):
        return [f"{path.relative_to(ROOT)}: cases must be a list"]

    covered: set[str] = set()
    for index, case in enumerate(cases):
        label = f"{path.relative_to(ROOT)}: case {index + 1}"
        if not isinstance(case, dict):
            errors.append(f"{label} must be a mapping")
            continue
        skill = case.get("skill")
        if isinstance(skill, str):
            covered.add(skill)
        else:
            errors.append(f"{label} has no skill")
        for field in ("required_findings", "prohibited_actions"):
            value = case.get(field)
            if not isinstance(value, list) or not value:
                errors.append(f"{label} {field} must be a non-empty list")

    missing = sorted(skill_names - covered)
    if missing:
        errors.append(f"{path.relative_to(ROOT)}: skills without outcome cases: {missing}")
    return errors


def validate_sources() -> list[str]:
    errors: list[str] = []
    registry_path = ROOT / "sources" / "SOURCES.yaml"
    schema_path = ROOT / "schemas" / "source-registry.schema.json"
    try:
        data = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, yaml.YAMLError) as exc:
        return [f"{registry_path.relative_to(ROOT)}: cannot load registry/schema: {exc}"]
    for error in Draft202012Validator(schema).iter_errors(data):
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        errors.append(f"{registry_path.relative_to(ROOT)}:{location}: {error.message}")
    if isinstance(data, dict):
        registry_review = data.get("review_date")
        for index, source in enumerate(data.get("sources", [])):
            if isinstance(source, dict) and not (source.get("last_reviewed") or registry_review):
                errors.append(
                    f"{registry_path.relative_to(ROOT)}:sources.{index}: "
                    "last_reviewed is required when registry review_date is absent"
                )
    return errors


def validate_bundles(skill_names: set[str]) -> list[str]:
    errors: list[str] = []
    for path in sorted((ROOT / "bundles").glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if not isinstance(data, dict):
            errors.append(f"{path.relative_to(ROOT)}: bundle must be a mapping")
            continue
        members = data.get("skills")
        if not isinstance(members, list) or not members:
            errors.append(f"{path.relative_to(ROOT)}: bundle skills must be non-empty")
            continue
        missing = [name for name in members if name not in skill_names]
        if missing:
            errors.append(f"{path.relative_to(ROOT)}: missing skills {missing}")
    return errors


def main() -> int:
    all_errors: list[str] = []
    all_warnings: list[str] = []
    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir() and not p.name.startswith((".", "_")))
    names = {p.name for p in skill_dirs}
    for skill_dir in skill_dirs:
        errors, warnings = validate_skill(skill_dir)
        all_errors.extend(f"{skill_dir.name}: {item}" for item in errors)
        all_warnings.extend(f"{skill_dir.name}: {item}" for item in warnings)
    all_errors.extend(validate_trigger_files())
    all_errors.extend(validate_outcome_cases(names))
    all_errors.extend(validate_sources())
    all_errors.extend(validate_bundles(names))
    for item in all_warnings:
        print(f"WARNING: {item}")
    for item in all_errors:
        print(f"ERROR: {item}")
    print(f"Validated {len(skill_dirs)} skills, {len(all_warnings)} warnings, {len(all_errors)} errors.")
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
