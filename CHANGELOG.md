# Changelog

## After-care clarification — 2026-10-03

This dated clarification supersedes earlier documentation claims without rewriting their historical entries. The previous README matrices, badges, and audit text were not evidence of competitor behavior, zero network egress, calibrated consensus confidence, race-proof or unforgeable team locks, an operating-system sandbox, universal cost caps, transitive license clearance, or a vulnerability-response SLA. Do not treat those claims in the historical entries below as current guarantees. The recorded 2.54x benchmark belongs only to the specific run and success counts in `results/benchmark_20260306.json`; it is not a general performance claim. Version `0.1.3` is package metadata, not by itself evidence of a published package. One historical pilot error-path string was generalized for publication; the recorded experiment metrics are unchanged.

## [0.1.3] - 2026-09-16

### Added

- 18-Point Quick Navigation & Dual Anchor Parity: Upgraded English (`README.md`) and German (`README_de.md`) documentation navigation to the standardized 18-point architecture with dual HTML anchor tags (`#1-features` through `#18-changelog-contributing`), preserving full backward compatibility with legacy anchor targets. [G 2026-09-16]
- Target Personas & High-Intent SEO Discovery: Added dedicated persona mappings (`[PERSONA-01]` Local-First AI Engineers, `[PERSONA-02]` Reliability & Factuality Engineers, `[PERSONA-03]` Batch Processing Developers, `[PERSONA-04]` Multi-Agent System Architects) with context, pain points, swarm-ai solutions, and high-intent bilingual search queries. [G 2026-09-16]
- 10-Dimensions Comparative Matrix: Introduced comprehensive technical comparison matrix evaluating `swarm-ai` against LangChain/LangGraph, Microsoft AutoGen, CrewAI, and OpenAI Swarm across all 10 governance invariants (`INV-LOCAL-01` to `INV-SLA-10`). [G 2026-09-16]
- Third-Party License Audit & Non-Elevation Assurance: Audited `THIRD_PARTY_LICENSES.md` (Stand: 2026-09-16) confirming 100% permissive open-source licenses, zero copyleft, and standard unprivileged user space `RunAsInvoker` execution. [G 2026-09-16]
- Contract Test Suite Expansion: Expanded `tests/test_metadata.py` with tests for 18-point navigation, target personas, comparative matrix dimensions, and third-party license audit timestamps. [G 2026-09-16]
- Metadata, Version & Badge Synchronization: Harmonized version 0.1.3, audit date 2026-09-16, and verified test metrics across `pyproject.toml`, `README.md`, `README_de.md`, `llms.txt`, and `MARKETING-LOG.txt`. [G 2026-09-16]

## [0.1.2] - 2026-09-13

### Added

- All-Workflow Timeout Guardrails: Enforced explicit timeout limits across all GitHub Actions workflows (`timeout-minutes: 10` for `stale.yml`, `timeout-minutes: 15` for `codeql.yml`, and `timeout-minutes: 5` for `welcome.yml`), complementing the existing 15-minute limits on `ci.yml`. [G 2026-09-13]
- Multi-Host Cloud-Sync & Gitignore Hardening: Extended `.gitignore` defense patterns to shield against cross-device conflicts (`* (Kopie)*`, `* (Copy)*`, `*conflicted copy*`, `*-LAPTOP.*`, `*-LAPTOP-*`, `*-Mac Studio.*`, `.hypothesis/`). [G 2026-09-13]
- PEP 621 Standard License Declaration: Added `license-files = ["LICENSE"]` in `pyproject.toml` to comply with modern standard packaging metadata specifications. [G 2026-09-13]
- Import Organization & Ruff Ruleset Expansion: Added `"I"` (isort) to `[tool.ruff.lint]` select array and organized import blocks cleanly across `tools/` and `tests/`. [G 2026-09-13]
- Automated Contract Test Expansion: Added 3 new contract tests in `tests/test_metadata.py` (`test_pep621_license_files_contract`, `test_ruff_expanded_ruleset_and_isort_parity`, `test_workflows_presence_and_timeouts`) and expanded CI timeout validations, bringing test suite to 220 passed tests (100% green). [G 2026-09-13]
- Metadata & Badge Synchronization: Harmonized 220 passed test metrics and `2026-09-13` audit/check dates across `README.md`, `README_de.md`, `llms.txt`, and `MARKETING-LOG.txt`. [G 2026-09-13]

## [0.1.2] - 2026-09-12

### Added

- CI Workflow Timeout Guardrails & Verbose Reporting: Added `timeout-minutes: 15` execution limits to `tests`, `anthropic-compat`, and `security` jobs in `.github/workflows/ci.yml` and standardized test execution to `python -m pytest -ra -v`. [G 2026-09-12]
- Multi-Host Cloud-Sync & Canonical Lock Defense: Hardened `.gitignore` against multi-host conflict files (`*-WORKSTATION*`, `*-WORKSTATION-LG*`, `*-ASUS-GEI*`, `* (kopie)*`, `* (copy)*`, `*.orig`, `*.rej`), canonical lock system entries (`uv.lock`, `!package-lock.json`), and build/cache outputs (`.mypy_cache/`, `.tox/`, `.turbo/`, `.coverage.*`). [G 2026-09-12]
- PEP 621 Standard URLs: Registered `"LLM Ready" = "https://github.com/ellmos-ai/swarm_ai/blob/master/llms.txt"` in `pyproject.toml` `[project.urls]` for autonomous LLM agent discoverability. [G 2026-09-12]
- Expanded Ruff Ruleset & Code Hygiene: Expanded `[tool.ruff.lint]` in `pyproject.toml` to `["E4", "E7", "E9", "F", "W", "B", "SIM", "C4", "RUF"]` and performed code cleanup across `tools/` and `tests/` (`strict=True` in `zip()`, set comprehension in `benchmark.py`, loop variable renaming in `generate_banners.py`, `contextlib.suppress` in `team_lock.py` and `translate_swarm.py`, and assertion coverage in `test_consensus.py`). [G 2026-09-12]
- Automated Contract Test Expansion: Added 4 new contract tests in `tests/test_metadata.py` (`test_ci_timeout_minutes_guardrail`, `test_pep621_llm_ready_contract`, `test_extended_gitignore_multi_host_and_lock_defense`, and `test_changelog_recent_pfad_a_entry`), bringing test suite to 217 passed tests (100% green). [G 2026-09-12]
- Metadata & Badge Synchronization: Harmonized version 0.1.2, release date 2026-09-12, and 217 passed test badge metrics across `pyproject.toml`, `README.md`, `README_de.md`, `llms.txt`, and `MARKETING-LOG.txt`. [G 2026-09-12]

## [0.1.1] - 2026-09-11

### Added

- Discoverability, Visual Architecture & Design (Pfad B): Modernized bilingual documentation architecture (`README.md` & `README_de.md`) with standardized Shields.io badge array (version 0.1.1, CI passing, 213 passed tests | 100% green, platforms, Local-First zero-egress, RunAsInvoker non-elevation, security SLA, third-party audited 100% permissive, marketing log active, Ruff, ellmos-ai, open-bricks, LLM-Ready llms.txt, last-checked 2026-09-11, license MIT), 15-point Schnellnavigation with exact mutual anchor parity including `#third-party-licenses--transparency` / `#drittanbieter-lizenzen--transparenz`, dual Mermaid diagrams (5-layer flowchart TB & autonumbered sequenceDiagram), 10 Governance & Runtime Invariants table (`INV-LOCAL-01` to `INV-SLA-10`), and 16-repository ecosystem matrix across `ellmos-ai`, `dev-bricks`, `file-bricks`, `doc-bricks`, and `open-bricks`. [G 2026-09-11]
- Third-Party License Inventory: Created and audited comprehensive `THIRD_PARTY_LICENSES.md` (Stand: 2026-09-11) documenting Anthropic SDK, COMA, pytest, Ruff, Bandit, and Python Standard Library licenses with 100% permissive open-source licenses, zero copyleft (GPL/AGPL), unprivileged user mode `RunAsInvoker` non-elevation assurance, and fail-closed evidence acceptance. [G 2026-09-11]
- Marketing & Discoverability Audit: Added and hardened repository-level `MARKETING-LOG.txt` (Audit Date: 2026-09-11, Status: ACTIVE / PFAD B DISCOVERABILITY HARDENED) documenting 4 user personas, competitive differentiation matrix vs. CrewAI, LangGraph, AutoGen, and OpenAI Swarm, search index terms (EN/DE), and 10 architectural invariants. [G 2026-09-11]
- Packaging & PEP 621 Standard URLs: Synchronized `pyproject.toml` version to 0.1.1, added `addopts = "-ra -v"` to `[tool.pytest.ini_options]`, and registered URLs for Third-Party Licenses, Marketing Log, Documentation, Security, Parent Organization, and Umbrella Ecosystem. [G 2026-09-11]
- Gitignore Hardening: Hardened `.gitignore` against multi-host cloud-sync conflicts (`*-conflict-*`, `*.sync-temp-*`, `*-ASUS-GEI.*`, `*-WORKSTATION-LG.*`) and multi-agent lock files (`LOCK`, `LOCK.*`, `*.lock`, `LOCK.permissions.json`). [G 2026-09-11]
- Automated Contract Test Expansion: Extended contract test suite in `tests/test_metadata.py` with 15-point navigation anchor parity, third-party licenses RunAsInvoker & audit date assertions, and badge matrix completeness, bringing test suite to 213 passed tests (100% green). [G 2026-09-11]
- Context & Verification Parity: Updated `llms.txt` with Last-checked date `2026-09-11`, version 0.1.1, 10 governance invariants, and 213 verified tests. [G 2026-09-11]

## [0.1.0] - 2026-09-08

### Added

- Technical Hygiene & CI Matrix Hardening: Expanded GitHub Actions CI test matrix (`.github/workflows/ci.yml`) to test Python 3.10, 3.11, 3.12, and 3.13 across Ubuntu, Windows, and macOS with pip caching enabled (`cache: 'pip'`). [G 2026-09-08]
- Gitignore Hardening: Added extended sync conflict and temporary file patterns (`*-CONFLIT-*`, `*.tmp`, `*.bak`, `.coverage`, `htmlcov/`) to `.gitignore`. [G 2026-09-08]
- Canonical Remote Parity: Synchronized repository URLs across `pyproject.toml`, `SECURITY.md`, `README.md`, `README_de.md`, and `llms.txt` with the canonical GitHub remote (`ellmos-ai/swarm_ai`). [G 2026-09-08]
- Automated Contract Test Hardening: Extended `tests/test_metadata.py` with multi-Python CI matrix checks (3.10-3.13), gitignore conflict patterns, Ruff configuration contract validation, and changelog release hygiene tests (13/13 contract tests passed, 204 total tests passed, 100% green). [G 2026-09-08]
- Context Synchronization: Synchronized `llms.txt` to `2026-09-08` with verified test metrics and canonical remote endpoints. [G 2026-09-08]

## [0.1.0] - 2026-08-25

### Added

- Discoverability, README-Design & Badges: Structured Quick Navigation / Schnellnavigation (14 jump anchors) with bilingual parity across `README.md` and `README_de.md`. [G 2026-08-25]
- Capabilities & Invariants Matrix: Added bilingual Table of Core Capabilities & Security Invariants covering 10 fundamental architecture guarantees (100% Local-First & Zero-Egress, Parallel Chunks, Boss/Worker, Stigmergy, Consensus, Specialist Routing, Team Locks, Fail-Closed Budgeting, Unprivileged User Mode, Multi-OS CI). [G 2026-08-25]
- Sibling Tools & Ecosystem Expansion: Comprehensive 16-repository ecosystem table across `ellmos-ai`, `dev-bricks`, `file-bricks`, `doc-bricks`, and `open-bricks` (coma, clutch, MarbleRun, policy-registry, system-explorer, sqlite-transit-sync, workflowhooker, memoryhooker, ellmos-filecommander-mcp, ellmos-codecommander-mcp, ellmos-controlcenter-mcp, DevCenter, CodeBox, ProFiler, DokuZen, open-bricks). [G 2026-08-25]
- CI Concurrency Control: Hardened `.github/workflows/ci.yml` with GitHub Actions `concurrency` group and `cancel-in-progress: true` to prevent redundant parallel workflow runs. [G 2026-08-25]
- PEP 621 Standard Metadaten: Added POSIX Linux, Microsoft Windows, MacOS, Topic Security and Topic Distributed Computing classifiers and `[project.urls]` for Parent Organization (`ellmos-ai`) and Umbrella Ecosystem (`open-bricks`) in `pyproject.toml`. [G 2026-08-25]
- Dual-Language Security SLA & Contacts: Hardened `SECURITY.md` with explicit 48-hour Initial Response SLA, 5-day triage commitment, and official security contacts (`security@ellmos.ai`, `security@open-bricks.org`, `support@lukasgeiger.com`, `lukas@open-bricks.org`). [G 2026-08-25]
- Repository Hygiene & Gitignore: Added synchronization conflict patterns (`*.sync-conflict-*`, `*.conflict`) and lockfiles (`LOCK*.txt`) to `.gitignore`. [G 2026-08-25]
- Automated Contract Tests: Extended `tests/test_metadata.py` with 4 new contract test functions verifying CI concurrency, ecosystem URLs, supported versions & 48h SLA, README quick navigation, capabilities table, sibling matrix, and gitignore hygiene (11/11 passed, 201 total tests passed, 1 skipped). [G 2026-08-25]
- Machine-Readable Context: Synchronized `llms.txt` timestamp (`2026-08-25`), version `0.1.0`, and verified test suite metrics. [G 2026-08-25]

## Unreleased

### Added

- Technical Hygiene, Security & Metadata Parity: Added PEP 621 Standard Classifiers (Python 3.10-3.13, OS Independent, AI topic) and expanded project URLs (Documentation, Bug Tracker, Changelog, Security) in `pyproject.toml`. [G 2026-08-21]
- Comprehensive Bilingual Security Policy: Replaced minimal policy with dual-language (EN/DE) `SECURITY.md` detailing supported versions, local-first & zero-egress architecture guarantees, fail-closed budgeting, and direct security contact endpoints. [G 2026-08-21]
- Automated Test Suite Extensions: Extended `tests/test_metadata.py` with PEP 621 classifiers/URLs contract tests, bilingual security policy validation, and CI workflow parity assertions (7/7 passed, 196 total tests). [G 2026-08-21]
- Synchronized `llms.txt` Last-checked timestamp to `2026-08-21` and updated verification metrics. [G 2026-08-21]

- Discoverability, Badges & Metadata Parity: synchronized README.md and README_de.md with interactive Mermaid system architecture & consensus sequence diagrams, 100% accurate test badges (193 passed, 1 skipped), LLM-Ready tags, and an extensive sibling tools matrix across ellmos-ai, dev-bricks, and open-bricks. [G 2026-08-16]
- Implemented automated metadata, manifest and UTF-8 parity test suite in `tests/test_metadata.py` (4/4 passed). [G 2026-08-16]
- Configured unified `[tool.ruff]` and `[tool.ruff.lint]` in `pyproject.toml` targeting Python 3.10. [G 2026-08-16]
- Synchronized `llms.txt` with latest ecosystem links, test statistics and verified discovery keywords. [G 2026-08-16]

- Defined the `ellmos-swarm-ai` PEP-621 packaging contract with stable CLI
  entry-points, package data inclusion, PEP-440 versioning, and a gated
  TestPyPI/PyPI readback checklist in `PYPI_RELEASE.md`.
- Extended `tools/benchmark.py` with explicit model pricing, token-cost
  estimates, reproducibility metadata, and versioned dry-run/live JSON exports.
- `konzepte/matruschka-verfahren.md` (Version 1.3): Kernregel 4 „Exklusive
  Schreibbereiche bei paralleler Arbeit" — disjunkte Schreibbereiche oder eigene
  Kopie für Helfer, Schreibverbote immer mit Begründung, und Messen zählt als
  Nutzung des Bereichs. Mit Belegfall vom 2026-08-02. [C 2026-08-02]
- Alt-Datenbanken: `summarize_chunks.py --init-db` übernimmt Laufprotokolle aus
  der abgelösten Tabelle `epstein_runs` idempotent nach `parallel_chunks_runs`
  (`initialize_schema(migrate_legacy=True)` liefert die Anzahl übernommener
  Läufe). **Gewählt wurde die Datenmigration statt eines Kompatibilitäts-Views:**
  Der kanonische Tabellenname bleibt `parallel_chunks_runs` (umbenannt am
  2026-06-17), und ein View könnte eine in der Alt-Datenbank real existierende
  Tabelle gleichen Namens ohnehin nicht überlagern. Ohne Migration legte
  `initialize_schema` daneben eine leere Tabelle an — die Altläufe blieben auf
  der Platte, wären aber für jede Abfrage unsichtbar. Die Legacy-Tabelle wird
  nicht verändert und nicht gelöscht; der Abgleich zählt je
  (`started_at`, `llm_model`)-Gruppe, damit auch zwei echte Altläufe mit
  identischem Zeitstempel und Modell erhalten bleiben. [C 2026-08-02]
- `konzepte/schwarm-operationen.md`: frühere Bezeichnung des Musters
  („Epstein-Muster", bis Juni 2026) als Herkunftsnotiz aufgenommen — der Name
  wird nirgends mehr ausgewertet, bleibt aber dokumentiert, damit ältere Notizen
  und Datenbanken zuordenbar sind. [C 2026-08-02]
- `konzepte/matruschka-verfahren.md`: Matruschka-Verfahren (Synonym:
  Subsidiaritätsprinzip) als Querschnittsverfahren für kaskadierte
  Helfer-Delegation mit Aktivitäts-Limits je Ebene (Limits = gleichzeitige
  Aktivität statt Bestand; Vorhalten + kontextbezogenes Wiederverwenden;
  Delegation nur abwärts). Verweis in `konzepte/schwarm-operationen.md`
  (Version 1.2). [C 2026-08-01]

### Fixed

- Technical Hygiene & Maintenance: fixed 38 ruff lint issues across experiment scripts (unused imports, extraneous f-strings, boolean/None comparisons), added noqa E402 import guards in dungeon_template.py, updated llms.txt Last-checked timestamp to 2026-08-04 and verified test suite count (182 passed, 1 skipped). [G 2026-08-04]
- Handled optional COMA provider test dependency gracefully with `pytest.importorskip` in `test_runner.py`. [G 2026-07-30]
- Restored the empirically supported Anthropic SDK floor to 0.40.0 and added
  minimum/latest SDK contract tests across Python 3.10 and 3.13.
- Installed the declared COMA provider dependency in full CI so provider
  runner tests execute instead of failing during import.
- Added a clear `ValueError` for `ClaudeRunner.run_parallel()` dict items that omit the required `prompt` key.
- Made `ClaudeRunner` read-only by default and restrictive even with an empty tool set.
- Corrected consensus confidence under partial failures and validated classification/boolean responses.
- Made consensus pricing model-aware instead of silently applying Haiku prices to overrides.
- Added atomic standalone stigmergy storage and fixed `evaporate(0)` deleting a record.
- Implemented translation source-language handling, identity-based result mapping, and serialized writes.
- Added standalone DB initialization, limits, and cross-process claims for chunk summarization.
- Added mandatory live limits and conservative cost ceilings for benchmarks, translation, and summarization.
- Cost ceilings include every configured retry, not only the first API attempt.
- Added pre-API translation claims to prevent concurrent runs paying for the same rows.
- Made team resource claims atomic across processes and attendance lossless.
- Serialized claim/release transitions and hashed attendance tokens to prevent path escape and release races.
- Made stigmergy evaporation reserve its SQLite writer transaction before reading.
- Corrected the benchmark working directory and duplicate dungeon result keys.
- Made historical experiment launchers fail closed and protected dungeon fixtures from accidental overwrite.
- Separated Claude CLI tool visibility from pre-approval, denied MCP tools by default, and disabled session persistence.
- Required finite live budgets for consensus and rejected NaN/infinite caps across every paid tool.
- Counted exact JSON escaping and translation identities in conservative cost bounds.
- Closed every SQLite handle, rejected concurrent summary overwrites, and preserved translation placeholders.
- Made consensus ties explicit instead of selecting a completion-order winner.
- Kept expired team claims non-stealable and removed partial claim files after failed writes.
- Made legacy stigmergy migration select the newest valid duplicate deterministically.
- Removed user-memory mutation from historical experiments and required strict modes, fixture markers, and total-run budgets.
- Restricted write-capable experiments to pre-approved built-in file tools in Claude safe mode.

### Security

- Removed legacy permission bypass flags and hardcoded personal targets from executable experiments.
- Pinned GitHub Actions by commit SHA and added CodeQL, Dependabot, Bandit, and `SECURITY.md`.

### Documentation

- Synchronized `llms.txt`, `RELEASE_GATE.md`, and test suite verification to 2026-08-03 (172 passed, 1 skipped). Integrated open-bricks ecosystem & Pytest badges and GFM Callout box for `llms.txt` in English & German READMEs. Fixed unused `import time` in `tools/render_previews.py` (ruff 100% clean). [G 2026-08-03]
- Synchronized `llms.txt`, `RELEASE_GATE.md`, and test suite verification to 2026-07-30 (170 passed, 4 skipped for optional COMA backend). [G 2026-07-30]
- Synchronized `llms.txt`, `RELEASE_GATE.md`, and verification metadata to the 2026-07-27 test run (167 passed).
- Added PEP 621 compliant `pyproject.toml` with pytest `pythonpath` and `testpaths` configuration.
- Synchronized `llms.txt`, `RELEASE_GATE.md`, and verification metadata to the 2026-07-26 test run (167 passed).
- Synchronized `llms.txt`, `RELEASE_GATE.md`, and verification metadata to the 2026-07-25 test run (166 passed).
- Added `konzepte/team-lock-verfahren.md` and README references for the coordination guardrail used during shared-file swarm work.
- Synchronized release-gate and `llms.txt` verification metadata to the 2026-07-10 test run.
- Updated verification metadata to the 2026-07-15 FABLE review (166 tests).
- Added clearer discovery context and search phrases to `README.md` and `README_de.md`.
- Standardized `llms.txt` with `Last-checked`, audience, search phrases, keywords, and disambiguation notes.
