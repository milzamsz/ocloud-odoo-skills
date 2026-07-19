from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.validate_repository import (  # noqa: E402
    MIN_TRIGGER_CASES_PER_CLASS,
    NAME_RE,
    parse_skill,
    validate_outcome_cases,
    validate_sources,
    validate_trigger_files,
)



def test_all_skill_names_match_directories():
    for skill_dir in (ROOT / "skills").iterdir():
        if not skill_dir.is_dir():
            continue
        meta, _ = parse_skill(skill_dir / "SKILL.md")
        assert meta["name"] == skill_dir.name
        assert NAME_RE.fullmatch(meta["name"])


def test_all_phase_one_skills_have_trigger_evals():
    for skill_dir in (ROOT / "skills").iterdir():
        if skill_dir.is_dir():
            assert (ROOT / "evals" / "trigger" / f"{skill_dir.name}.json").exists()


def test_evaluation_data_meets_release_contract():
    trigger_errors = validate_trigger_files()
    assert all(
        f"need at least {MIN_TRIGGER_CASES_PER_CLASS} positive" not in error
        for error in trigger_errors
    ), "\n".join(trigger_errors)

    skill_names = {path.name for path in (ROOT / "skills").iterdir() if path.is_dir()}
    outcome_errors = validate_outcome_cases(skill_names)
    assert not outcome_errors, "\n".join(outcome_errors)


def test_source_registry_matches_policy():
    errors = validate_sources()
    assert not errors, "\n".join(errors)
