# swarm-ai

[English](README.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [日本語](README_ja.md) · [Русский](README_ru.md) · [简体中文](README_zh.md) · [Français](README_fr.md) · [हिन्दी](README_hi.md) · [العربية](README_ar.md) · [বাংলা](README_bn.md) · [Português](README_pt.md)

![swarm-ai-Banner](assets/banner.png)

**Ein kleines Python-Toolkit zum Erproben von Koordination mit mehreren LLM-Agenten.** Es enthält Beispiele für parallele Chunk-Verarbeitung, Boss-/Worker-Abläufe, SQLite-Stigmergie, Mehrheitsabstimmung und Spezialisten-Routing.

<p>
  <a href="https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml"><img src="https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml/badge.svg?branch=master" alt="CI-Status"></a>
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python 3.10+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT-Lizenz"></a>
</p>

Koordinationsdaten werden lokal gespeichert. Aufrufe an Anthropic, Claude CLI oder einen anderen konfigurierten Provider können Prompts und Anfragedaten an externe Dienste übermitteln. Prüfe vor der Nutzung vertraulicher Inhalte den Abschnitt [Datenfluss und Grenzen](SECURITY.md).

## Installation

```bash
git clone https://github.com/ellmos-ai/swarm_ai.git
cd swarm_ai
python -m venv .venv
```

Aktiviere die Umgebung (`.venv\Scripts\Activate.ps1` in PowerShell oder `source .venv/bin/activate` unter Linux/macOS) und installiere das Projekt:

```bash
python -m pip install -e .
swarm-consensus --help
```

Der Aufruf `--help` sendet keine API-Anfrage. Für die COMA-Provider-Integration installiere das optionale Extra mit `python -m pip install -e ".[providers]"`.

## Erster Lauf

Ein Live-Konsenslauf sendet die Frage an die konfigurierte Anthropic-API und kann Kosten verursachen. Setze `ANTHROPIC_API_KEY` und gib eine Kostenschätzungsgrenze an:

```bash
swarm-consensus --question "Was ist die Hauptstadt von Australien?" --agents 3 --max-budget-usd 1
```

Die Grenze ist eine positive, endliche Schätzungsgrenze des Werkzeugs; die Provider-Abrechnung kann abweichen. `--dry-run` schätzt eine Anfrage, ohne die API aufzurufen.

## CLI-Werkzeuge

- `swarm-consensus`: unabhängige Antworten mehrerer Worker zusammenführen.
- `swarm-benchmark`: sequenzielle und parallele Abläufe vergleichen; startet im Dry-Run-Modus.
- `swarm-translate`: Texte aus der konfigurierten SQLite-Datenbank übersetzen.
- `swarm-summarize`: in SQLite gespeicherte Chunks zusammenfassen.
- `swarm-stigmergy-init`: eine lokale Marker-Datenbank einrichten.

`--help` zeigt die Optionen der jeweiligen Befehle. Konsens, Übersetzung und Zusammenfassung verlangen bei Live-Provider-Aufrufen positive, endliche Kostenschätzungsgrenzen. `ClaudeRunner` unterstützt eine optionale Grenze; andere Provider-Abläufe haben keine gemeinsame universelle Obergrenze.

## Laufzeitgrenzen

- `confidence` beim Konsens ist die Anzahl der Gewinnerstimmen geteilt durch alle Worker-Ergebnisse; `agreement_ratio` berücksichtigt nur gültige Antworten. Keiner der Werte ist eine kalibrierte Wahrscheinlichkeit, und Übereinstimmung beweist keine Richtigkeit.
- Team-Locks nutzen atomare Datei-Claims und getrennte Anwesenheitseinträge zur Koordination kooperierender Prozesse. Sie verhindern keine Schreibzugriffe von Prozessen, die das Verfahren ignorieren oder verändern.
- Das Programm übernimmt die Umgebung und Berechtigungen des aufrufenden Kontos. `RunAsInvoker` ist keine Betriebssystem-Sandbox und garantiert keine Ausführung ohne erhöhte Rechte.
- Die Übersetzungsziele `de`, `en`, `es`, `zh`, `ja` und `ru` sind Ausgabe-Sprachen und keine sechs lokalisierten UI-Sprachen. Die CLI-Hilfe ist englisch, einzelne Laufzeit-Fortschrittsmeldungen sind noch deutsch; die experimentelle Tk-GUI hat deutsche Beschriftungen.
- Die Benchmark-Datei [`results/benchmark_20260306.json`](results/benchmark_20260306.json) dokumentiert einen historischen Lauf mit einer bestimmten Arbeitslast. Die Messwerte sagen keine allgemeine Leistung voraus.

Mehr Implementierungsdetails stehen unter [Architektur und Koordination](docs/ARCHITECTURE.md). Aktuelle Aufgaben sind im Abschnitt [Offene Aufgaben in `TODO.md`](TODO.md#offene-aufgaben) aufgeführt.

## Projekt und Sicherheit

Die Paketmetadaten in `pyproject.toml` weisen Version `0.1.3` aus; daraus folgt keine Veröffentlichung des Pakets. Für den Quellcode dieses Repositorys gilt die [MIT-Lizenz](LICENSE). [`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md) nennt ausgewählte deklarierte Abhängigkeiten. Die Liste ist weder eine vollständige Prüfung transitiver Abhängigkeiten noch eine pauschale Aussage zur kommerziellen Nutzung.

Melde Schwachstellen über [GitHub Security Advisories](https://github.com/ellmos-ai/swarm_ai/security/advisories/new); die private Schwachstellenmeldung ist für dieses Repository aktiviert, und [`SECURITY.md`](SECURITY.md) nennt, was ein Bericht enthalten sollte. Das Projekt veröffentlicht keine Reaktionsfrist. Den aktuellen CI-Status zeigt der Live-[GitHub-Actions-Workflow](https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml).

Die englische Übersicht steht in [`README.md`](README.md), die spanische in [`README_es.md`](README_es.md) und die datierte Projekthistorie im [`CHANGELOG.md`](CHANGELOG.md).

## Verwandte Projekte

- [COMA](https://github.com/ellmos-ai/coma): eine optionale Provider-Brücke; mit installierter `providers`-Zusatzabhängigkeit nutzt Swarm die Spawner- und Adapter-API von COMA.
- [MarbleRun](https://github.com/ellmos-ai/marblerun): ein eigenständiges Toolkit zum Konfigurieren von Multi-Agent-Ketten.
- [clutch](https://github.com/ellmos-ai/clutch): stellt die Fähigkeit `routing.default` bereit, die dieses Modul in `ellmos-module.v2.json` als optional führt; swarm-ai ruft clutch nicht selbst auf.
- [lock-master](https://github.com/ellmos-ai/lock-master): das vollständige Datei-Lock-System (exklusive und Team-Locks mit Geltungsbereich und Ablauf); `tools/team_lock.py` ist hier nur ein kleines kooperatives Claim-Protokoll für Prozesse, die sich daran halten.
- [ellmos-scheduler](https://github.com/ellmos-ai/ellmos-scheduler): führt Cron- und Intervall-Jobs mit Leases und Laufbelegen aus; damit lassen sich Schwarmläufe zeitgesteuert starten.
- [compare-race](https://github.com/ellmos-ai/compare-race): schickt einen Prompt an mehrere Modelle und lässt ein Modell die Antworten bewerten — ein qualitativer Vergleich, während `swarm-consensus` gleiche Antworten zählt.
