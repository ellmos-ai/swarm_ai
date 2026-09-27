"""Metadata and manifest parity tests for ellmos-ai/swarm-ai."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_manifest_and_pyproject_version_parity():
    pyproject_text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    version_match = re.search(r'^version = "([^"]+)"', pyproject_text, re.MULTILINE)
    assert version_match, "version not found in pyproject.toml"
    pyproject_version = version_match.group(1)

    manifest_path = ROOT / "ellmos-module.v2.json"
    assert manifest_path.exists(), "ellmos-module.v2.json must exist"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    assert manifest["package"] == "ellmos-swarm-ai"
    assert manifest["id"] == "swarm_ai"
    assert pyproject_version == "0.1.3"


def test_cli_entrypoints_parity():
    pyproject_text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")

    expected_tools = [
        ("tools/consensus_swarm.py", "swarm-consensus"),
        ("tools/benchmark.py", "swarm-benchmark"),
        ("tools/translate_swarm.py", "swarm-translate"),
        ("tools/summarize_chunks.py", "swarm-summarize"),
        ("tools/stigmergy_init.py", "swarm-stigmergy-init"),
    ]

    for rel_path, entrypoint in expected_tools:
        tool_file = ROOT / rel_path
        assert tool_file.exists(), f"Expected tool file {rel_path} must exist"
        assert entrypoint in pyproject_text, f"Entrypoint {entrypoint} must be in pyproject.toml"


def test_llms_txt_and_documentation_parity():
    llms_txt = (ROOT / "llms.txt").read_text(encoding="utf-8")
    readme_en = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_de = (ROOT / "README_de.md").read_text(encoding="utf-8")

    assert (
        "https://github.com/ellmos-ai/swarm_ai" in llms_txt
        or "https://github.com/ellmos-ai/swarm-ai" in llms_txt
    )
    assert (
        "https://github.com/ellmos-ai/swarm_ai" in readme_en
        or "https://github.com/ellmos-ai/swarm-ai" in readme_en
    )
    assert (
        "https://github.com/ellmos-ai/swarm_ai" in readme_de
        or "https://github.com/ellmos-ai/swarm-ai" in readme_de
    )

    # Verify key patterns documented
    patterns = [
        "tools/consensus_swarm.py",
        "tools/stigmergy_api.py",
        "tools/translate_swarm.py",
        "tools/summarize_chunks.py",
        "tools/runner.py",
    ]
    for pattern in patterns:
        assert pattern in llms_txt, f"Pattern {pattern} must be mentioned in llms.txt"
        assert (ROOT / pattern).exists(), f"File {pattern} must exist"


def test_utf8_integrity_across_markdown():
    md_files = list(ROOT.glob("*.md")) + list((ROOT / "konzepte").glob("*.md"))
    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8")
        assert "\ufffd" not in content, f"Replacement character detected in {md_file}"


def test_pep621_classifiers_and_urls_parity():
    pyproject_text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    assert "Programming Language :: Python :: 3" in pyproject_text
    assert "Programming Language :: Python :: 3.10" in pyproject_text
    assert "Programming Language :: Python :: 3.11" in pyproject_text
    assert "Programming Language :: Python :: 3.12" in pyproject_text
    assert "Programming Language :: Python :: 3.13" in pyproject_text
    assert "Operating System :: OS Independent" in pyproject_text
    assert "Operating System :: POSIX :: Linux" in pyproject_text
    assert "Operating System :: Microsoft :: Windows" in pyproject_text
    assert "Operating System :: MacOS" in pyproject_text
    assert "Topic :: Security" in pyproject_text
    assert "Topic :: System :: Distributed Computing" in pyproject_text
    assert "Documentation = " in pyproject_text
    assert '"Bug Tracker" = ' in pyproject_text
    assert "Changelog = " in pyproject_text
    assert "Security = " in pyproject_text
    assert '"Parent Organization" = "https://github.com/ellmos-ai"' in pyproject_text
    assert '"Umbrella Ecosystem" = "https://github.com/open-bricks"' in pyproject_text
    assert '"LLM Ready" = ' in pyproject_text


def test_security_policy_bilingual_parity():
    security_md = ROOT / "SECURITY.md"
    assert security_md.exists(), "SECURITY.md must exist"
    content = security_md.read_text(encoding="utf-8")
    assert "# Security Policy / Sicherheitsrichtlinie" in content
    assert "## English" in content
    assert "## Deutsch" in content
    assert "### Supported Versions" in content
    assert "### Unterstützte Versionen" in content
    assert "`0.1.x`" in content
    assert "48 hours" in content
    assert "48 Stunden" in content
    assert "security@ellmos.ai" in content
    assert "security@open-bricks.org" in content
    assert "support@lukasgeiger.com" in content
    assert "lukas@open-bricks.org" in content
    assert "Zero-Egress" in content


def test_ci_workflow_parity():
    ci_path = ROOT / ".github" / "workflows" / "ci.yml"
    assert ci_path.exists(), "ci.yml must exist"
    ci_text = ci_path.read_text(encoding="utf-8")
    assert "ubuntu-latest" in ci_text
    assert "windows-latest" in ci_text
    assert "macos-latest" in ci_text
    assert "3.10" in ci_text
    assert "3.11" in ci_text
    assert "3.12" in ci_text
    assert "3.13" in ci_text
    assert "concurrency:" in ci_text
    assert "cancel-in-progress: true" in ci_text


def test_readme_quick_navigation_and_bilingual_parity():
    readme_en = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_de = (ROOT / "README_de.md").read_text(encoding="utf-8")

    assert "## Quick Navigation" in readme_en
    assert "## Schnellnavigation" in readme_de

    en_anchors = [
        "#1-features",
        "#2-architecture",
        "#3-target-personas",
        "#4-comparative-matrix",
        "#5-mermaid-diagrams",
        "#6-governance-invariants",
        "#7-coordination-patterns",
        "#8-team-locks",
        "#9-coma-providers",
        "#10-installation",
        "#11-quick-start",
        "#12-benchmarks",
        "#13-repository-layout",
        "#14-project-status",
        "#15-sibling-ecosystem",
        "#16-third-party-licenses",
        "#17-security-policy",
        "#18-changelog-contributing",
    ]
    for anchor in en_anchors:
        assert anchor in readme_en, f"Anchor {anchor} must exist in README.md"

    de_anchors = [
        "#1-merkmale",
        "#2-architektur",
        "#3-zielgruppen",
        "#4-vergleichsmatrix",
        "#5-mermaid-diagramme",
        "#6-governance-invarianten",
        "#7-koordinationsmuster",
        "#8-team-locks",
        "#9-coma-provider",
        "#10-installation",
        "#11-schnellstart",
        "#12-benchmarks",
        "#13-repository-struktur",
        "#14-projektstatus",
        "#15-geschwister-tools",
        "#16-drittanbieter-lizenzen",
        "#17-sicherheit",
        "#18-aenderungsprotokoll-mitwirken",
    ]
    for anchor in de_anchors:
        assert anchor in readme_de, f"Anchor {anchor} must exist in README_de.md"


def test_core_capabilities_and_security_invariants_table():
    readme_en = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_de = (ROOT / "README_de.md").read_text(encoding="utf-8")

    assert (
        "## 6. Governance & Runtime Invariants" in readme_en
        or "## Core Capabilities & Security Invariants" in readme_en
    )
    assert (
        "## 6. Governance & Laufzeit-Invarianten" in readme_de
        or "## Kernfähigkeiten & Sicherheitsinvarianten" in readme_de
    )

    capabilities = [
        "100% Local-First & Zero-Egress",
        "Parallel Chunks Pattern",
        "Boss / Worker Hierarchy",
        "Stigmergy & Pheromone Store",
        "Consensus & Majority Vote",
        "Specialist Routing",
        "Team Lock Guardrail",
        "Fail-Closed Budgeting",
        "Unprivileged User Mode",
        "Multi-OS CI Smoke Integrity",
    ]
    for cap in capabilities:
        assert cap in readme_en, f"Capability '{cap}' must be present in README.md"

    german_caps = [
        "100% Local-First & Zero-Egress",
        "Parallel-Chunks-Muster",
        "Boss-/Worker-Hierarchie",
        "Stigmergie & Pheromonspeicher",
        "Konsens & Mehrheitsentscheid",
        "Spezialisten-Routing",
        "Team-Lock-Guardrail",
        "Fail-Closed Budget-Schutz",
        "Unprivilegierter User-Mode",
        "Multi-OS CI-Smoke-Integrität",
    ]
    for cap in german_caps:
        assert cap in readme_de, f"German capability '{cap}' must be present in README_de.md"


def test_governance_invariants_table_parity():
    readme_en = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_de = (ROOT / "README_de.md").read_text(encoding="utf-8")

    invariants = [
        "INV-LOCAL-01",
        "INV-CHUNKS-02",
        "INV-HIERARCH-03",
        "INV-STORE-04",
        "INV-VOTE-05",
        "INV-ROUTER-06",
        "INV-LOCK-07",
        "INV-BUDGET-08",
        "INV-RUNAS-09",
        "INV-SLA-10",
    ]
    for inv in invariants:
        assert inv in readme_en, f"Invariant '{inv}' must be present in README.md"
        assert inv in readme_de, f"Invariant '{inv}' must be present in README_de.md"


def test_sibling_tools_and_ecosystem_matrix():
    readme_en = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_de = (ROOT / "README_de.md").read_text(encoding="utf-8")

    siblings = [
        "coma",
        "clutch",
        "MarbleRun",
        "policy-registry",
        "system-explorer",
        "sqlite-transit-sync",
        "workflowhooker",
        "memoryhooker",
        "ellmos-filecommander-mcp",
        "ellmos-codecommander-mcp",
        "ellmos-controlcenter-mcp",
        "DevCenter",
        "CodeBox",
        "ProFiler",
        "DokuZen",
        "open-bricks",
    ]
    for tool in siblings:
        assert tool in readme_en, f"Sibling '{tool}' must be listed in README.md"
        assert tool in readme_de, f"Sibling '{tool}' must be listed in README_de.md"


def test_third_party_licenses_inventory():
    licenses_file = ROOT / "THIRD_PARTY_LICENSES.md"
    assert licenses_file.exists(), "THIRD_PARTY_LICENSES.md must exist"
    content = licenses_file.read_text(encoding="utf-8")
    assert "anthropic" in content
    assert "coma" in content
    assert "pytest" in content
    assert "ruff" in content
    assert "bandit" in content
    assert "MIT License" in content


def test_marketing_log_exists():
    marketing_log = ROOT / "MARKETING-LOG.txt"
    assert marketing_log.exists(), "MARKETING-LOG.txt must exist"
    content = marketing_log.read_text(encoding="utf-8")
    assert "DISCOVERABILITY & MARKETING LOG" in content
    assert "swarm-ai" in content
    assert "INV-LOCAL-01" in content


def test_pyproject_pytest_ini_and_urls():
    pyproject_text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    assert '[tool.pytest.ini_options]' in pyproject_text
    assert 'addopts = "-ra -v"' in pyproject_text
    assert '"Third-Party Licenses" = ' in pyproject_text
    assert '"Marketing Log" = ' in pyproject_text


def test_mermaid_diagrams_parity():
    readme_en = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_de = (ROOT / "README_de.md").read_text(encoding="utf-8")

    assert "flowchart TB" in readme_en
    assert "sequenceDiagram" in readme_en
    assert "flowchart TB" in readme_de
    assert "sequenceDiagram" in readme_de


def test_gitignore_hygiene_patterns():
    gitignore_text = (ROOT / ".gitignore").read_text(encoding="utf-8")
    assert "*.sync-conflict-*" in gitignore_text
    assert "*.conflict" in gitignore_text
    assert "*-CONFLIT-*" in gitignore_text
    assert "*-conflict-*" in gitignore_text
    assert "LOCK" in gitignore_text
    assert "LOCK.*" in gitignore_text
    assert "*.lock" in gitignore_text
    assert "LOCK*.txt" in gitignore_text
    assert "LOCK.permissions.json" in gitignore_text
    assert ".ruff_cache/" in gitignore_text


def test_ruff_configuration_parity():
    pyproject_text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    assert "[tool.ruff]" in pyproject_text
    assert 'target-version = "py310"' in pyproject_text
    assert "select = " in pyproject_text


def test_changelog_hygiene_and_latest_entry():
    changelog_text = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert "2026-09-11" in changelog_text
    assert "## [0.1.1] - 2026-09-11" in changelog_text
    assert "\ufffd" not in changelog_text


def test_bilingual_readme_navigation_anchor_sections():
    readme_en = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_de = (ROOT / "README_de.md").read_text(encoding="utf-8")

    en_headings = [
        "## 1. Features & System Overview",
        "## 2. System Architecture & Workflow Lifecycle",
        "## 3. Target Personas & SEO Discovery",
        "## 4. Comparative Matrix vs. Alternatives",
        "## 5. Dual Mermaid Architecture & Lifecycle Diagrams",
        "## 6. Governance & Runtime Invariants",
        "## 7. 5 Swarm Coordination Patterns",
        "## 8. Coordination Guardrail: Team Locks",
        "## 9. Provider Routing: COMA Bridge (Codex, Agy, Kimi)",
        "## 10. Installation & Setup",
        "## 11. Quick Start & CLI Entrypoints",
        "## 12. Benchmarks & Performance Metrics",
        "## 13. Repository Layout & File Structure",
        "## 14. Project Status & Verification",
        "## 15. Sibling Tools & Ecosystem",
        "## 16. Third-Party Licenses & Transparency",
        "## 17. Security Policy & Privacy SLAs",
        "## 18. Changelog, Roadmap & Contributing",
    ]
    for h in en_headings:
        assert h in readme_en, f"Heading '{h}' must exist in README.md"

    de_headings = [
        "## 1. Merkmale & Systemüberblick",
        "## 2. Systemarchitektur & Workflow-Lebenszyklus",
        "## 3. Zielgruppen & SEO-Auffindbarkeit",
        "## 4. Vergleichsmatrix gegenüber Alternativen",
        "## 5. Duale Mermaid-Architektur & Lebenszyklus-Diagramme",
        "## 6. Governance & Laufzeit-Invarianten",
        "## 7. 5 Schwarm-Koordinationsmuster",
        "## 8. Koordinations-Guardrail: Team-Locks",
        "## 9. Provider-Routing: COMA-Bridge (Codex, Agy, Kimi)",
        "## 10. Installation & Setup",
        "## 11. Schnellstart & CLI-Einstiegspunkte",
        "## 12. Benchmarks & Leistungsmetriken",
        "## 13. Repository-Struktur & Verzeichnis-Layout",
        "## 14. Projektstatus & Verifikation",
        "## 15. Geschwister-Tools & Ökosystem",
        "## 16. Drittanbieter-Lizenzen & Transparenz",
        "## 17. Sicherheitsrichtlinie & Datenschutz-SLAs",
        "## 18. Änderungsprotokoll, Roadmap & Mitwirken",
    ]
    for h in de_headings:
        assert h in readme_de, f"Heading '{h}' must exist in README_de.md"


def test_marketing_log_contract_and_invariants():
    marketing_log = (ROOT / "MARKETING-LOG.txt").read_text(encoding="utf-8")
    assert "Audit Date: 2026-09-16" in marketing_log
    assert "Status: ACTIVE" in marketing_log
    assert "Active Version: 0.1.3" in marketing_log
    assert "2. TARGET PERSONAS & AUDIENCE MAPPING" in marketing_log
    assert "3. ARCHITECTURAL INVARIANTS & GOVERNANCE" in marketing_log
    assert "9. DISCOVERABILITY, DESIGN & GOVERNANCE AUDIT (2026-09-16)" in marketing_log

    invariants = [
        "INV-LOCAL-01",
        "INV-RUNAS-02",
        "INV-BUDGET-03",
        "INV-STORE-04",
        "INV-CHUNKS-05",
        "INV-HIERARCH-06",
        "INV-VOTE-07",
        "INV-ROUTER-08",
        "INV-LOCK-09",
        "INV-SLA-10",
    ]
    for inv in invariants:
        assert inv in marketing_log, f"Invariant {inv} must exist in MARKETING-LOG.txt"


def test_readme_badge_matrix_parity():
    readme_en = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_de = (ROOT / "README_de.md").read_text(encoding="utf-8")

    assert "version-0.1.3-blue" in readme_en
    assert "version-0.1.3-blue" in readme_de

    assert "CI-passing-brightgreen" in readme_en
    assert "CI-passing-brightgreen" in readme_de

    assert "tests-22" in readme_en
    assert "tests-22" in readme_de

    assert "third--party-audited" in readme_en
    assert "drittanbieter-gepr" in readme_de

    assert "marketing--log-active" in readme_en
    assert "marketing--log-aktiv" in readme_de

    assert "last--checked-2026--09--16-blue" in readme_en
    assert "letzte--pr%C3%BCfung-2026--09--16-blue" in readme_de


def test_third_party_licenses_audit_and_non_elevation():
    licenses_text = (ROOT / "THIRD_PARTY_LICENSES.md").read_text(encoding="utf-8")
    assert "- **Audit Date:** 2026-09-16" in licenses_text
    assert "RunAsInvoker Non-Elevation" in licenses_text
    assert "Fail-Closed Evidence Acceptance" in licenses_text
    assert "No copyleft (GPL / AGPL)" in licenses_text


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


def test_pep621_llm_ready_contract():
    pyproject_text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    assert '"LLM Ready" = "https://github.com/ellmos-ai/swarm_ai/blob/master/llms.txt"' in pyproject_text
    assert (ROOT / "llms.txt").exists()


def test_extended_gitignore_multi_host_and_lock_defense():
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


def test_pep621_license_files_contract():
    pyproject_text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    assert 'license-files = ["LICENSE"]' in pyproject_text
    assert (ROOT / "LICENSE").exists()


def test_ruff_expanded_ruleset_and_isort_parity():
    pyproject_text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    for rule in ["E4", "E7", "E9", "F", "W", "I", "B", "SIM", "C4", "RUF"]:
        assert f'"{rule}"' in pyproject_text


def test_workflows_presence_and_timeouts():
    workflows_dir = ROOT / ".github" / "workflows"
    assert (workflows_dir / "ci.yml").exists()
    assert (workflows_dir / "stale.yml").exists()
    assert (workflows_dir / "codeql.yml").exists()
    assert (workflows_dir / "welcome.yml").exists()


def test_changelog_recent_pfad_a_entry():
    changelog_text = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert "## [0.1.2] - 2026-09-12" in changelog_text or "## [0.1.2] - 2026-09-13" in changelog_text
    assert "timeout-minutes" in changelog_text
    assert "Multi-Host Cloud-Sync & Canonical Lock Defense" in changelog_text
    assert "PEP 621 Standard URLs" in changelog_text


def test_changelog_recent_pfad_b_entry():
    changelog_text = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert "## [0.1.3] - 2026-09-16" in changelog_text
    assert "18-Point Quick Navigation & Dual Anchor Parity" in changelog_text
    assert "Target Personas & High-Intent SEO Discovery" in changelog_text
    assert "10-Dimensions Comparative Matrix" in changelog_text
    assert "Third-Party License Audit & Non-Elevation Assurance" in changelog_text


def test_target_personas_and_high_intent_seo_queries():
    readme_en = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_de = (ROOT / "README_de.md").read_text(encoding="utf-8")

    personas = ["[PERSONA-01]", "[PERSONA-02]", "[PERSONA-03]", "[PERSONA-04]"]
    for p in personas:
        assert p in readme_en, f"Persona {p} must be present in README.md"
        assert p in readme_de, f"Persona {p} must be present in README_de.md"

    assert "Local-First AI Engineers & Multi-Agent Researchers" in readme_en
    assert "Reliability & Factuality Engineers" in readme_en
    assert "Batch Processing & Document Pipeline Developers" in readme_en
    assert "Collaborative Multi-Agent System Architects" in readme_en

    assert "Local-First KI-Ingenieure & Multi-Agenten-Forscher" in readme_de
    assert "Zuverlässigkeits- & Faktizitäts-Ingenieure" in readme_de
    assert (
        "Batch-Verarbeitungs- & Dokumenten-Pipeline-Entwickler" in readme_de
        or "Batch-Processing- & Dokumenten-Pipeline-Entwickler" in readme_de
    )
    assert "Architekten kollaborativer Multi-Agenten-Systeme" in readme_de


def test_comparative_matrix_ten_dimensions_parity():
    readme_en = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_de = (ROOT / "README_de.md").read_text(encoding="utf-8")

    alternatives = [
        "swarm-ai",
        "LangChain",
        "AutoGen",
        "CrewAI",
        "OpenAI Swarm",
    ]
    for alt in alternatives:
        assert alt in readme_en, f"Alternative {alt} must be present in README.md"
        assert alt in readme_de, f"Alternative {alt} must be present in README_de.md"

    invariants = [
        "INV-LOCAL-01",
        "INV-CHUNKS-02",
        "INV-HIERARCH-03",
        "INV-STORE-04",
        "INV-VOTE-05",
        "INV-ROUTER-06",
        "INV-LOCK-07",
        "INV-BUDGET-08",
        "INV-RUNAS-09",
        "INV-SLA-10",
    ]
    for inv in invariants:
        assert inv in readme_en, f"Invariant {inv} must be present in README.md comparative matrix"
        assert inv in readme_de, f"Invariant {inv} must be present in README_de.md comparative matrix"


def test_dual_mermaid_diagrams_structure_and_autonumber():
    readme_en = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_de = (ROOT / "README_de.md").read_text(encoding="utf-8")

    for doc in [readme_en, readme_de]:
        assert "flowchart TB" in doc
        assert "sequenceDiagram" in doc
        assert "autonumber" in doc
        assert "subgraph Coordination" in doc
        assert "SQLite Pheromone / Chunk DB" in doc or "Store" in doc
