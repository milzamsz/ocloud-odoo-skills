#!/usr/bin/env python3
"""Check that each tap skill is self-contained for distribution."""
import json
from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def main() -> int:
    errors: list[str] = []
    skill_names = {
        path.name
        for path in (ROOT / "skills").iterdir()
        if path.is_dir() and not path.name.startswith((".", "_"))
    }
    for skill in sorted((ROOT / "skills").iterdir()):
        if not skill.is_dir() or skill.name.startswith((".", "_")):
            continue
        text = (skill / "SKILL.md").read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            path = (skill / target.split("#", 1)[0]).resolve()
            try:
                path.relative_to(skill.resolve())
            except ValueError:
                errors.append(f"{skill.name}: non-local resource {target}")
        if not (ROOT / "evals" / "trigger" / f"{skill.name}.json").exists():
            errors.append(f"{skill.name}: trigger evaluation missing")

    tap = json.loads((ROOT / "skills.sh.json").read_text(encoding="utf-8"))
    tap_names = {
        name
        for grouping in tap.get("groupings", [])
        for name in grouping.get("skills", [])
    }
    if tap_names != skill_names:
        errors.append(
            "skills.sh.json: skill set differs from skills/ "
            f"(missing={sorted(skill_names - tap_names)}, extra={sorted(tap_names - skill_names)})"
        )

    for bundle_path in sorted((ROOT / "bundles").glob("*.yaml")):
        bundle = yaml.safe_load(bundle_path.read_text(encoding="utf-8"))
        members = bundle.get("skills", [])
        missing = sorted(set(members) - skill_names)
        if missing:
            errors.append(f"{bundle_path.name}: unknown members {missing}")
        if not members:
            errors.append(f"{bundle_path.name}: no skill members")
    if errors:
        print("\n".join(f"ERROR: {item}" for item in errors))
        return 1
    print("Package check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
