# swarm-ai

[English](README.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [日本語](README_ja.md) · [Русский](README_ru.md)

![banner de swarm-ai](assets/banner.png)

**Un pequeño conjunto de herramientas de Python para experimentar con la coordinación multiagente con LLM.** Incluye ejemplos de procesamiento paralelo de fragmentos, flujos de trabajo jefe/trabajador, estigmergia con SQLite, votación por mayoría y enrutamiento a especialistas.

<p>
  <a href="https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml"><img src="https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml/badge.svg?branch=master" alt="Estado de CI"></a>
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python 3.10+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="Licencia MIT"></a>
</p>

El estado de coordinación se almacena localmente. Las llamadas a Anthropic, Claude CLI u otro proveedor configurado pueden enviar prompts y datos de solicitudes a servicios externos. Consulta [flujo de datos y límites](SECURITY.md) antes de usar datos sensibles.

## Instalación

```bash
git clone https://github.com/ellmos-ai/swarm_ai.git
cd swarm_ai
python -m venv .venv
```

Activa el entorno (`.venv\Scripts\Activate.ps1` en PowerShell o `source .venv/bin/activate` en Linux/macOS) y luego instala el proyecto:

```bash
python -m pip install -e .
swarm-consensus --help
```

El comando de ayuda no realiza una llamada a la API. Para integrar el proveedor COMA, instala el extra opcional con `python -m pip install -e ".[providers]"`.

## Primer uso

Una ejecución de consenso en vivo envía la pregunta a la API de Anthropic configurada y puede generar un coste. Define `ANTHROPIC_API_KEY` y establece un límite de coste estimado:

```bash
swarm-consensus --question "What is the capital of Australia?" --agents 3 --max-budget-usd 1
```

El límite es un umbral de estimación positivo y finito que aplica la herramienta; la facturación del proveedor puede diferir. `--dry-run` estima una solicitud sin llamar a la API.

## Herramientas de CLI

- `swarm-consensus`: consulta a trabajadores independientes y agrega sus resultados.
- `swarm-benchmark`: compara ejecuciones secuenciales y paralelas; comienza en modo dry-run.
- `swarm-translate`: traduce texto almacenado en la base de datos SQLite configurada.
- `swarm-summarize`: resume fragmentos almacenados en SQLite.
- `swarm-stigmergy-init`: inicializa una base de datos local de marcadores.

Consulta `--help` de cada comando para ver sus opciones. El consenso, la traducción y el resumen requieren límites de coste estimado positivos y finitos en las ejecuciones en vivo con proveedores. `ClaudeRunner` admite un límite opcional; los demás flujos de proveedores no comparten un límite universal.

## Límites de ejecución

- En el consenso, `confidence` es el número de votos del ganador dividido entre todos los resultados de los trabajadores; `agreement_ratio` se calcula solo con las respuestas válidas. Ninguno de los dos valores es una probabilidad calibrada, y la concordancia no demuestra que los datos sean correctos.
- Los bloqueos de equipo usan reclamaciones atómicas de archivos y registros de asistencia por participante para coordinar procesos que cooperan. No impiden escrituras de procesos que ignoren o modifiquen el protocolo.
- El programa hereda el entorno y los permisos del proceso que lo invoca. `RunAsInvoker` no es un entorno aislado del sistema operativo ni garantiza que el programa no se ejecute con privilegios elevados.
- Los idiomas de destino de la traducción `de`, `en`, `es`, `zh`, `ja` y `ru` son idiomas de salida, no seis idiomas de una interfaz localizada. La ayuda de CLI combina inglés y alemán; la GUI experimental de Tk tiene etiquetas en alemán.
- El archivo de benchmark [`results/benchmark_20260306.json`](results/benchmark_20260306.json) registra una carga de trabajo histórica. Sus mediciones no predicen el rendimiento general.

Encontrarás más detalles de implementación en [Arquitectura y coordinación](docs/ARCHITECTURE.md). Las tareas abiertas actuales están en [Tareas abiertas de `TODO.md`](TODO.md#offene-aufgaben).

## Información del proyecto y seguridad

`pyproject.toml` declara la versión `0.1.3`; esos metadatos por sí solos no implican que se haya publicado un paquete. El código fuente de este repositorio está bajo la [licencia MIT](LICENSE). [`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md) enumera algunas dependencias declaradas; no es una auditoría de dependencias transitivas ni una determinación general sobre el uso comercial.

Informa de vulnerabilidades mediante [GitHub Security Advisories](https://github.com/ellmos-ai/swarm_ai/security/advisories/new) o a una dirección indicada en [`SECURITY.md`](SECURITY.md). El proyecto no publica un SLA de tiempo de respuesta. Consulta el [flujo de trabajo de GitHub Actions](https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml) en vivo para ver el estado actual de CI.

Consulta [`README_de.md`](README_de.md) para la descripción general en alemán, [`README.md`](README.md) para la versión en inglés y [`CHANGELOG.md`](CHANGELOG.md) para el historial fechado del proyecto.

## Proyectos relacionados

- [COMA](https://github.com/ellmos-ai/coma) — un puente opcional de proveedor Spawner/adaptador que Swarm usa cuando está instalado el extra `providers`.
- [Roshambo](https://github.com/ellmos-ai/roshambo) — un conjunto de herramientas independiente para coordinar agentes iniciados por separado mediante leases serializables y memoria de resultados.
- [MarbleRun](https://github.com/ellmos-ai/marblerun) — un conjunto de herramientas independiente para configurar cadenas multiagente.
