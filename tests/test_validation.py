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
    validate_version_claims,
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


def test_skill_version_claims_have_complete_evidence():
    skill_dirs = sorted(path for path in (ROOT / "skills").iterdir() if path.is_dir())
    errors = validate_version_claims(skill_dirs)
    assert not errors, "\n".join(errors)


def test_editions_by_version_can_claim_community_without_enterprise_for_new_release():
    from scripts.validate_repository import iter_version_edition_pairs

    metadata = {
        "versions": ["17.0", "18.0", "20.0"],
        "editions": ["community", "enterprise"],
        "editions_by_version": {
            "17.0": ["community", "enterprise"],
            "18.0": ["community", "enterprise"],
            "20.0": ["community"],
        },
    }

    assert list(iter_version_edition_pairs(metadata)) == [
        ("17.0", "community"),
        ("17.0", "enterprise"),
        ("18.0", "community"),
        ("18.0", "enterprise"),
        ("20.0", "community"),
    ]


def test_edition_claims_without_version_map_keep_legacy_cross_product():
    from scripts.validate_repository import iter_version_edition_pairs

    metadata = {"versions": ["18.0", "19.0"], "editions": ["community", "enterprise"]}

    assert list(iter_version_edition_pairs(metadata)) == [
        ("18.0", "community"),
        ("18.0", "enterprise"),
        ("19.0", "community"),
        ("19.0", "enterprise"),
    ]


def test_editions_by_version_omits_unlisted_edition_pairs():
    from scripts.validate_repository import iter_version_edition_pairs

    metadata = {
        "versions": ["20.0"],
        "editions": ["community", "enterprise"],
        "editions_by_version": {"20.0": ["community"]},
    }

    assert list(iter_version_edition_pairs(metadata)) == [("20.0", "community")]
    assert ("20.0", "enterprise") not in list(iter_version_edition_pairs(metadata))
