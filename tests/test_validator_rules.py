"""Rules added to the validator: description prefix, metadata enums, local paths, secrets."""

import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.validate_repository import (  # noqa: E402
    expand_braces,
    scan_skill_files,
    validate_local_paths,
    validate_skill,
    validate_wiki,
)

FRONTMATTER = textwrap.dedent(
    """\
    ---
    name: {name}
    description: {description}
    metadata:
      status: {status}
      risk: {risk}
    ---
    """
)


def make_skill(tmp_path: Path, **overrides) -> Path:
    fields = {
        "name": "odoo-sample",
        "description": "Use this skill when testing the validator.",
        "status": "experimental",
        "risk": "advisory",
        "body": "Read `references/odoo-18-community.md` after confirming Odoo 18.\n",
        "refs": ["odoo-18-community.md"],
    }
    fields.update(overrides)
    skill = tmp_path / fields["name"]
    (skill / "references").mkdir(parents=True)
    for ref in fields["refs"]:
        (skill / "references" / ref).write_text("# ref\n", encoding="utf-8")
    (skill / "SKILL.md").write_text(FRONTMATTER.format(**fields) + fields["body"], encoding="utf-8")
    return skill


def test_expand_braces_handles_nested_options():
    assert expand_braces("odoo-{17,18}-{community,enterprise}.md") == [
        "odoo-17-community.md",
        "odoo-17-enterprise.md",
        "odoo-18-community.md",
        "odoo-18-enterprise.md",
    ]
    assert expand_braces("plain.md") == ["plain.md"]


def test_valid_skill_has_no_errors(tmp_path):
    errors, warnings = validate_skill(make_skill(tmp_path))
    assert errors == []
    assert warnings == ["missing trigger evaluation file"]


def test_description_must_start_with_trigger_phrase(tmp_path):
    skill = make_skill(tmp_path, description="Helps with Odoo. Use this skill when unsure.")
    errors, _ = validate_skill(skill)
    assert any("must start with" in e for e in errors)


def test_metadata_enums_are_enforced(tmp_path):
    skill = make_skill(tmp_path, status="beta", risk="high")
    errors, _ = validate_skill(skill)
    assert any("metadata.status" in e for e in errors)
    assert any("metadata.risk" in e for e in errors)


def test_backtick_reference_must_exist_and_orphans_warn(tmp_path):
    skill = make_skill(
        tmp_path,
        body="Read `references/odoo-{18,19}-community.md` after discovery.\n",
        refs=["odoo-18-community.md", "unused.md"],
    )
    errors, warnings = validate_local_paths(skill, (skill / "SKILL.md").read_text())
    assert errors == ["missing referenced file: references/odoo-19-community.md"]
    assert warnings == ["packaged file never loaded by SKILL.md: references/unused.md"]


def test_secret_literals_are_errors_and_repo_paths_warn(tmp_path):
    skill = make_skill(tmp_path)
    (skill / "references" / "odoo-18-community.md").write_text(
        "admin_passwd = 'hunter22'\nSee `evals/fixtures/x` for the fixture.\n", encoding="utf-8"
    )
    errors, warnings = scan_skill_files(skill)
    assert errors == ["references/odoo-18-community.md: possible hardcoded password"]
    assert warnings == [
        "references/odoo-18-community.md: repository path not shipped with the skill: evals/fixtures/x"
    ]


def test_wiki_flags_broken_links_and_missing_catalog_rows(tmp_path):
    wiki = tmp_path / "docs" / "wiki"
    wiki.mkdir(parents=True)
    (wiki / "index.md").write_text("[ok](skill-catalog.md) [web](https://x.org) [bad](gone.md)\n")
    (wiki / "skill-catalog.md").write_text("| `odoo-a` | outcome |\n")
    (tmp_path / "llms.txt").write_text("- [Index](docs/wiki/index.md#top)\n")
    errors = validate_wiki({"odoo-a", "odoo-b"}, root=tmp_path)
    assert errors == [
        "docs/wiki/index.md: broken link gone.md",
        "docs/wiki/skill-catalog.md: skills without a row: ['odoo-b']",
    ]
