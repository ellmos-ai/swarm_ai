# Security Policy / Sicherheitsrichtlinie

[English](#english) | [Deutsch](#deutsch)

---

<a name="english"></a>
## English

### Supported versions

This repository currently declares version `0.1.3` in `pyproject.toml`. That source version alone does not identify a published package or promise a response or support period. Report issues against the current repository state and include the commit or version you use.

### Data flow and execution

Coordination data such as SQLite marker and chunk state is stored locally by the tools. Calls to Anthropic, Claude CLI, COMA-connected providers, or other configured services can send prompts and related request data outside the machine. Review the selected provider's data handling rules before sending sensitive content.

The program runs with the permissions and environment of its caller. The Windows `RunAsInvoker` compatibility mechanism does not create an operating-system sandbox and does not guarantee that a process is non-elevated. Team-lock files are a cooperative coordination protocol, not a security boundary.

Some commands require positive finite estimated-cost caps: consensus, translation, and summarization accept such caps, and `ClaudeRunner` supports an optional cap. These controls do not form one universal limit across every provider or workflow; estimates can differ from billed charges.

### Reporting a vulnerability

Please avoid public issue details while a vulnerability is unresolved. Submit a private report through [GitHub Security Advisories](https://github.com/ellmos-ai/swarm_ai/security/advisories/new), or contact a maintainer at one of these addresses:

- `security@ellmos.ai`
- `security@open-bricks.org`
- `support@lukasgeiger.com`
- `lukas@open-bricks.org`

Include the affected component, a concise description, reproduction steps, and potential impact. Do not include API keys, passwords, or private production data. The project does not publish a response-time or remediation SLA.

---

<a name="deutsch"></a>
## Deutsch

### Unterstützte Versionen

Dieses Repository weist in `pyproject.toml` die Version `0.1.3` aus. Diese Quellcode-Version allein sagt nichts über eine veröffentlichte Paketversion aus und begründet keine Support- oder Reaktionsfrist. Melden Sie Probleme zum aktuellen Repository-Stand und nennen Sie den verwendeten Commit oder die Version.

### Datenfluss und Ausführung

Koordinationsdaten wie SQLite-Marker und Chunk-Zustand werden von den Werkzeugen lokal gespeichert. Aufrufe an Anthropic, Claude CLI, über COMA verbundene Provider oder andere konfigurierte Dienste können Prompts und zugehörige Anfragedaten an externe Systeme senden. Prüfen Sie vor der Übermittlung vertraulicher Inhalte die Datenschutzregeln des gewählten Providers.

Das Programm läuft mit den Berechtigungen und der Umgebung des aufrufenden Kontos. Der Windows-Kompatibilitätsmechanismus `RunAsInvoker` erzeugt keine Betriebssystem-Sandbox und garantiert nicht, dass ein Prozess ohne erhöhte Rechte läuft. Team-Lock-Dateien bilden ein kooperatives Koordinationsverfahren und keine Sicherheitsgrenze.

Einige Befehle verlangen positive, endliche Kostenschätzungsgrenzen: Konsens, Übersetzung und Zusammenfassung akzeptieren solche Grenzen; `ClaudeRunner` unterstützt eine optionale Grenze. Diese Kontrollen bilden keine universelle Obergrenze für alle Provider oder Abläufe. Schätzungen können von den abgerechneten Kosten abweichen.

### Schwachstelle melden

Bitte veröffentlichen Sie Details zu einer ungelösten Schwachstelle nicht in einem öffentlichen Issue. Senden Sie einen vertraulichen Bericht über [GitHub Security Advisories](https://github.com/ellmos-ai/swarm_ai/security/advisories/new) oder kontaktieren Sie die Maintainer unter einer dieser Adressen:

- `security@ellmos.ai`
- `security@open-bricks.org`
- `support@lukasgeiger.com`
- `lukas@open-bricks.org`

Nennen Sie die betroffene Komponente, eine kurze Beschreibung, Reproduktionsschritte und mögliche Auswirkungen. Fügen Sie keine API-Schlüssel, Passwörter oder vertraulichen Produktionsdaten bei. Das Projekt veröffentlicht keine Reaktions- oder Behebungsfrist.
