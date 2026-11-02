# swarm-ai

[English](README.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [日本語](README_ja.md) · [Русский](README_ru.md) · [简体中文](README_zh.md) · [Français](README_fr.md) · [हिन्दी](README_hi.md) · [العربية](README_ar.md) · [বাংলা](README_bn.md) · [Português](README_pt.md)

![Bannière swarm-ai](assets/banner.png)

**Une petite boîte à outils Python pour expérimenter la coordination de LLM multi-agents.** Elle comprend des exemples de traitement parallèle de fragments, de flux de travail maître/exécutants, de stigmergie avec SQLite, de vote majoritaire et de routage vers des spécialistes.

<p>
  <a href="https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml"><img src="https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml/badge.svg?branch=master" alt="État de la CI"></a>
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Version Python 3.10+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="Licence MIT"></a>
</p>

L’état de coordination est stocké localement. Les appels à Anthropic, à Claude CLI ou à un autre fournisseur configuré peuvent transmettre des prompts et des données de requête à des services externes. Consultez [flux des données et limites](SECURITY.md) avant d’utiliser des données sensibles.

## Installation

```bash
git clone https://github.com/ellmos-ai/swarm_ai.git
cd swarm_ai
python -m venv .venv
```

Activez l’environnement (`.venv\Scripts\Activate.ps1` dans PowerShell ou `source .venv/bin/activate` sous Linux/macOS), puis installez le projet :

```bash
python -m pip install -e .
swarm-consensus --help
```

La commande d’aide n’effectue aucune requête API. Pour intégrer le fournisseur COMA, installez l’option facultative avec `python -m pip install -e ".[providers]"`.

## Première exécution

Un consensus en direct envoie la question à l’API Anthropic configurée et peut entraîner des frais. Définissez `ANTHROPIC_API_KEY` et indiquez une limite de coût estimé :

```bash
swarm-consensus --question "What is the capital of Australia?" --agents 3 --max-budget-usd 1
```

Cette limite constitue, dans l’outil, une borne d’estimation positive et finie ; la facturation du fournisseur peut différer. `--dry-run` estime une requête sans appeler l’API.

## Outils CLI

- `swarm-consensus` : interroger des agents indépendants et agréger leurs résultats.
- `swarm-benchmark` : comparer des exécutions séquentielles et parallèles ; démarre en mode simulation.
- `swarm-translate` : traduire du texte stocké dans la base de données SQLite configurée.
- `swarm-summarize` : résumer des fragments stockés dans SQLite.
- `swarm-stigmergy-init` : initialiser une base de données locale de marqueurs.

Utilisez `--help` de chaque commande pour connaître les options. Le consensus, la traduction et le résumé nécessitent des limites de coût estimé positives et finies pour les exécutions en direct avec un fournisseur. `ClaudeRunner` prend en charge une limite facultative ; les autres flux liés aux fournisseurs ne partagent pas de limite universelle.

## Limites d’exécution

- Pour le consensus, `confidence` correspond au nombre de résultats en faveur du gagnant divisé par le nombre total de résultats des agents ; `agreement_ratio` ne tient compte que des réponses valides. Ni l’une ni l’autre n’est une probabilité calibrée, et l’accord ne garantit pas l’exactitude factuelle.
- Les verrous d’équipe s’appuient sur des fichiers de réservation créés atomiquement et des registres de présence par participant pour coordonner les processus coopérants. Ces verrous sont coopératifs, ne sont pas imposés par le système d’exploitation et n’empêchent pas les écritures de processus qui ignorent ou modifient le protocole.
- Le programme hérite de l’environnement et des autorisations de son appelant. `RunAsInvoker` ne constitue pas un bac à sable du système d’exploitation et ne garantit pas l’absence d’élévation de privilèges.
- Les cibles de traduction `de`, `en`, `es`, `zh`, `ja` et `ru` sont des langues de sortie, pas six langues d’interface localisées. L’aide du CLI mêle l’anglais et l’allemand ; l’IHM expérimentale en Tk utilise des libellés allemands.
- Le fichier de benchmark [`results/benchmark_20260306.json`](results/benchmark_20260306.json) consigne une charge de travail historique. Ses mesures ne permettent pas de prédire les performances générales.

Vous trouverez davantage de détails sur l’implémentation dans [Architecture et coordination](docs/ARCHITECTURE.md). Les tâches actuellement ouvertes figurent sous [Tâches ouvertes dans `TODO.md`](TODO.md#offene-aufgaben).

## Informations sur le projet et la sécurité

La version `0.1.3` est déclarée dans `pyproject.toml` ; ces métadonnées seules ne signifient pas qu’un paquet a été publié. Le code source de ce dépôt est sous licence [MIT](LICENSE). [`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md) répertorie une sélection de dépendances déclarées et ne constitue ni un audit des dépendances transitives ni une conclusion générale sur l’autorisation d’un usage commercial.

Signalez les vulnérabilités via [GitHub Security Advisories](https://github.com/ellmos-ai/swarm_ai/security/advisories/new) ou à une adresse indiquée dans [`SECURITY.md`](SECURITY.md). Le projet ne publie aucun SLA sur les délais de réponse. Consultez le [workflow GitHub Actions](https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml) en direct pour connaître l’état actuel de la CI.

Voir [`README_de.md`](README_de.md) pour la présentation allemande, [`README_es.md`](README_es.md) pour la présentation espagnole et [`CHANGELOG.md`](CHANGELOG.md) pour l’historique daté du projet.

## Projets associés

- [COMA](https://github.com/ellmos-ai/coma) — une passerelle facultative entre Spawner et les adaptateurs de fournisseurs, utilisée par Swarm lorsque l’option `providers` est installée.
- [Roshambo](https://github.com/ellmos-ai/roshambo) — une boîte à outils distincte pour coordonner des agents lancés indépendamment à l’aide de baux sérialisables et d’une mémoire des résultats.
- [MarbleRun](https://github.com/ellmos-ai/marblerun) — une boîte à outils distincte pour configurer des chaînes multi-agents.
