# Third-Party Components and License Notices

The source code in this repository is offered under the terms in [`LICENSE`](LICENSE). Third-party packages have their own license terms, notices, and transitive dependencies; the repository license does not replace them.

This page records selected dependencies declared directly by this project. It is not a complete inventory of transitive packages or bundled files, and it is not a legal or commercial-use determination. Check the package metadata and license notices for the exact versions you install.

## Runtime dependencies

| Component | How it is declared or used | Upstream information |
|---|---|---|
| `anthropic` | Required Python dependency in `pyproject.toml` and `requirements.txt` | [anthropic-sdk-python](https://github.com/anthropics/anthropic-sdk-python) |
| Python standard library | Used by the application, including `sqlite3`, `pathlib`, `json`, `subprocess`, and `argparse` | [Python](https://www.python.org/) |
| `coma` | Optional `providers` extra; installed from the source repository below | [ellmos-ai/coma](https://github.com/ellmos-ai/coma) |

## Development and CI tools

| Component | Use in this repository | Upstream information |
|---|---|---|
| `pytest` | Test runner | [pytest](https://pytest.org/) |
| `ruff` | Lint checks | [Ruff](https://github.com/astral-sh/ruff) |
| `bandit` | High-severity static scan in CI | [Bandit](https://github.com/PyCQA/bandit) |
| `setuptools` | Build backend, minimum version declared in `pyproject.toml` | [setuptools](https://github.com/pypa/setuptools) |

No transitive dependency license audit or blanket permissive-license claim is made here. No conclusion about commercial use of third-party packages is made by this inventory.
