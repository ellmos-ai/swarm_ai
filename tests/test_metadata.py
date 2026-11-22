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


def test_ruff_configuration_has_a_single_effective_source():
    """ruff prefers ruff.toml over pyproject.toml.

    This test used to require an expanded rule set in pyproject.toml. That
    block was shadowed by ruff.toml and never ran, so the test protected a
    dead configuration. It now enforces one effective source.
    """
    pyproject_text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    assert "[tool.ruff" not in pyproject_text, "a second ruff config would be ignored"
    ruff_text = (ROOT / "ruff.toml").read_text(encoding="utf-8")
    assert 'target-version = "py310"' in ruff_text
    assert 'select = ["E4", "E7", "E9", "F"]' in ruff_text


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


def test_security_reporting_uses_only_the_enabled_advisory_channel():
    """SECURITY.md once listed four e-mail addresses that could not receive mail.

    Two domains did not resolve and one had no mail exchanger, so every report
    sent there was silently lost. The only supported channel is GitHub's
    private vulnerability reporting; no README may point readers at addresses.
    """
    import re

    advisory = "https://github.com/ellmos-ai/swarm_ai/security/advisories/new"
    security = (ROOT / "SECURITY.md").read_text(encoding="utf-8")
    assert security.count(advisory) == 2  # English and German section
    listed = re.findall(r"`[^`\s]+@[^`\s]+\.[a-z]{2,}`", security)
    assert listed == [], f"SECURITY.md lists e-mail addresses again: {listed}"
    for readme in sorted(ROOT.glob("README*.md")):
        text = readme.read_text(encoding="utf-8")
        assert advisory in text, f"{readme.name} lost the advisory link"
        assert "@ellmos.ai" not in text and "@open-bricks.org" not in text


def test_cli_help_of_every_entry_point_is_english():
    """The README promises English CLI help; this used to be German in four tools."""
    import re
    import subprocess
    import sys

    german = re.compile(r"[äöüÄÖÜß]|\b(und|nicht|für|Anzahl|Ausgabe|Nur|anzeigen)\b")
    for module in ("benchmark", "consensus_swarm", "translate_swarm", "summarize_chunks", "stigmergy_init"):
        out = subprocess.run(
            [sys.executable, "-m", f"tools.{module}", "--help"],
            cwd=ROOT, capture_output=True, text=True, encoding="utf-8", timeout=60, check=True,
        ).stdout
        hits = sorted({m.group(0) for m in german.finditer(out)})
        assert hits == [], f"tools.{module} --help still contains German: {hits}"
