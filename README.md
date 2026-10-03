# swarm-ai

[English](README.md) · [Deutsch](README_de.md)

![swarm-ai banner](assets/banner.png)

**A small Python toolkit for experimenting with multi-agent LLM coordination.** It includes examples for parallel chunk processing, boss/worker workflows, SQLite-backed stigmergy, majority voting, and specialist routing.

<p>
  <a href="https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml"><img src="https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml/badge.svg?branch=master" alt="CI status"></a>
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python 3.10+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT license"></a>
</p>

Coordination state is stored locally. Calls to Anthropic, Claude CLI, or another configured provider can send prompts and request data to external services. See [data flow and limits](SECURITY.md) before using sensitive inputs.

## Install

```bash
git clone https://github.com/ellmos-ai/swarm_ai.git
cd swarm_ai
python -m venv .venv
```

Activate the environment (`.venv\Scripts\Activate.ps1` in PowerShell or `source .venv/bin/activate` on Linux/macOS), then install the project:

```bash
python -m pip install -e .
swarm-consensus --help
```

The help command does not make an API request. For COMA provider integration, install the optional extra with `python -m pip install -e ".[providers]"`.

## First run

Live consensus sends the question to the configured Anthropic API and can incur a charge. Set `ANTHROPIC_API_KEY` and provide an estimated cost cap:

```bash
swarm-consensus --question "What is the capital of Australia?" --agents 3 --max-budget-usd 1
```

The cap is a positive finite estimate boundary in the tool; provider billing may differ. `--dry-run` estimates a request without calling the API.

## CLI tools

- `swarm-consensus`: ask independent workers and aggregate their results.
- `swarm-benchmark`: compare sequential and parallel runs; starts in dry-run mode.
- `swarm-translate`: translate text stored in the configured SQLite database.
- `swarm-summarize`: summarize chunks stored in SQLite.
- `swarm-stigmergy-init`: initialize a local marker database.

Use each command's `--help` for options. Consensus, translation, and summarization require positive finite estimated-cost caps for live provider runs. `ClaudeRunner` supports an optional cap; other provider flows do not share one universal cap.

## Runtime boundaries

- Consensus `confidence` is the winner count divided by all worker results; `agreement_ratio` uses valid answers only. Neither is a calibrated probability, and agreement does not establish factual correctness.
- Team locks use atomic file claims and per-participant attendance records to coordinate cooperating processes. They do not prevent writes from processes that ignore or edit the protocol.
- The program inherits the caller's environment and permissions. `RunAsInvoker` is not an operating-system sandbox and does not guarantee non-elevation.
- Translation targets `de`, `en`, `es`, `zh`, `ja`, and `ru` are output languages, not six localized UI languages. CLI help mixes English and German; the experimental Tk GUI has German labels.
- The benchmark file [`results/benchmark_20260306.json`](results/benchmark_20260306.json) records one historical workload. Its measurements do not predict general performance.

More implementation detail is in [Architecture and coordination](docs/ARCHITECTURE.md). Current open tasks are under [Offene Aufgaben in `TODO.md`](TODO.md#offene-aufgaben).

## Project and security information

Version `0.1.3` is declared in `pyproject.toml`; that metadata alone does not imply a package release. This repository's source is licensed under [MIT](LICENSE). [`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md) lists selected declared dependencies and is not a transitive dependency audit or a blanket commercial-use determination.

Report vulnerabilities through [GitHub Security Advisories](https://github.com/ellmos-ai/swarm_ai/security/advisories/new) or an address listed in [`SECURITY.md`](SECURITY.md). The project does not publish a response-time SLA. Consult the live [GitHub Actions workflow](https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml) for current CI status.

See [`README_de.md`](README_de.md) for the German overview and [`CHANGELOG.md`](CHANGELOG.md) for dated project history.
