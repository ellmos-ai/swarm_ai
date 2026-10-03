"""Repository configuration integrity checks."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_ci_workflow_covers_supported_matrix_and_concurrency():
    ci_text = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    for operating_system in ("ubuntu-latest", "windows-latest", "macos-latest"):
        assert operating_system in ci_text
    for version in ("3.10", "3.11", "3.12", "3.13"):
        assert f'"{version}"' in ci_text
    assert "concurrency:" in ci_text
    assert "cancel-in-progress: true" in ci_text


def test_ci_timeout_minutes_guardrail():
    ci_text = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    assert "timeout-minutes: 15" in ci_text
    assert "python -m pytest -ra -v" in ci_text

    stale_text = (ROOT / ".github" / "workflows" / "stale.yml").read_text(encoding="utf-8")
    assert "timeout-minutes: 10" in stale_text

    codeql_text = (ROOT / ".github" / "workflows" / "codeql.yml").read_text(encoding="utf-8")
    assert "timeout-minutes: 15" in codeql_text

    welcome_text = (ROOT / ".github" / "workflows" / "welcome.yml").read_text(encoding="utf-8")
    assert "timeout-minutes: 5" in welcome_text


def test_workflows_presence_and_timeouts():
    workflows_dir = ROOT / ".github" / "workflows"
    for workflow in ("ci.yml", "stale.yml", "codeql.yml", "welcome.yml"):
        assert (workflows_dir / workflow).is_file()


def test_gitignore_multi_host_conflict_and_lock_defense():
    gitignore_text = (ROOT / ".gitignore").read_text(encoding="utf-8")
    required_patterns = [
        "*-WORKSTATION*",
        "*-WORKSTATION-LG*",
        "*-ASUS-GEI*",
        "*-LAPTOP.*",
        "*-LAPTOP-*",
        "*-Mac Studio.*",
        "* (kopie)*",
        "* (Kopie)*",
        "* (copy)*",
        "* (Copy)*",
        "*conflicted copy*",
        "*.orig",
        "*.rej",
        "LOCK",
        "LOCK.*",
        "*.lock",
        "LOCK*.txt",
        "LOCK.permissions.json",
        "uv.lock",
        "!package-lock.json",
        ".hypothesis/",
        ".mypy_cache/",
        ".tox/",
        ".turbo/",
        ".coverage.*",
    ]
    for pattern in required_patterns:
        assert pattern in gitignore_text, f"Pattern '{pattern}' missing from .gitignore"


def test_ruff_configuration_parity():
    pyproject_text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    assert "[tool.ruff]" in pyproject_text
    assert 'target-version = "py310"' in pyproject_text
    for rule in ("E4", "E7", "E9", "F", "W", "I", "B", "SIM", "C4", "RUF"):
        assert f'"{rule}"' in pyproject_text


def test_pep621_license_files_contract():
    pyproject_text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    assert 'license-files = ["LICENSE"]' in pyproject_text
    assert (ROOT / "LICENSE").is_file()


def test_pep621_classifiers_and_urls_parity():
    pyproject_text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    for python_version in ("3.10", "3.11", "3.12", "3.13"):
        assert f"Programming Language :: Python :: {python_version}" in pyproject_text
    for operating_system in (
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
    ):
        assert operating_system in pyproject_text
    assert '"Bug Tracker" = ' in pyproject_text
    assert '"LLM Ready" = ' in pyproject_text


def test_utf8_integrity_across_markdown():
    markdown_files = list(ROOT.glob("*.md")) + list((ROOT / "konzepte").glob("*.md"))
    for markdown_file in markdown_files:
        content = markdown_file.read_text(encoding="utf-8")
        assert "\ufffd" not in content, f"Replacement character detected in {markdown_file}"
