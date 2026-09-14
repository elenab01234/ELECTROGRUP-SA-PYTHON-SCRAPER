"""Consistency tests for CODE_OF_CONDUCT.md."""

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
CODE_OF_CONDUCT_PATH = ROOT / "CODE_OF_CONDUCT.md"

REQUIRED_SECTIONS = [
    "## Our Pledge",
    "## Our Standards",
    "## Scope",
    "## Enforcement Responsibilities",
    "## Enforcement",
    "## Attribution",
]


def _code_of_conduct() -> str:
    return CODE_OF_CONDUCT_PATH.read_text(encoding="utf-8")


def test_code_of_conduct_required_sections():
    coc = _code_of_conduct()
    missing = [s for s in REQUIRED_SECTIONS if s not in coc]
    assert not missing, f"CODE_OF_CONDUCT.md missing required sections: {missing}"


def test_code_of_conduct_has_contributor_covenant():
    coc = _code_of_conduct()
    assert "Contributor Covenant" in coc, "CODE_OF_CONDUCT.md must reference Contributor Covenant"
