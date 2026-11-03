# swarm-ai

[English](README.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [日本語](README_ja.md) · [Русский](README_ru.md) · [简体中文](README_zh.md) · [Français](README_fr.md) · [हिन्दी](README_hi.md) · [العربية](README_ar.md) · [বাংলা](README_bn.md) · [Português](README_pt.md)

![banner do swarm-ai](assets/banner.png)

**Um pequeno kit Python para experimentar a coordenação multiagente de LLMs.** Inclui exemplos de processamento paralelo de blocos, fluxos de trabalho com coordenador e agentes executores, estigmergia com SQLite, votação por maioria e roteamento para especialistas.

<p>
  <a href="https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml"><img src="https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml/badge.svg?branch=master" alt="Status da CI"></a>
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python 3.10+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="Licença MIT"></a>
</p>

O estado de coordenação é armazenado localmente. Chamadas à Anthropic, ao Claude CLI ou a outro provedor configurado podem enviar prompts e dados de solicitação a serviços externos. Consulte [fluxo de dados e limites](SECURITY.md) antes de usar dados sensíveis.

## Instalação

```bash
git clone https://github.com/ellmos-ai/swarm_ai.git
cd swarm_ai
python -m venv .venv
```

Ative o ambiente (`.venv\Scripts\Activate.ps1` no PowerShell ou `source .venv/bin/activate` no Linux/macOS) e instale o projeto:

```bash
python -m pip install -e .
swarm-consensus --help
```

O comando de ajuda não faz uma solicitação à API. Para a integração de provedores COMA, instale o extra opcional com `python -m pip install -e ".[providers]"`.

## Primeira execução

A execução de consenso ao vivo envia a pergunta à API configurada da Anthropic e pode gerar uma cobrança. Defina `ANTHROPIC_API_KEY` e informe um limite estimado de custo:

```bash
swarm-consensus --question "What is the capital of Australia?" --agents 3 --max-budget-usd 1
```

O limite é um teto estimado, positivo e finito definido pela ferramenta; a cobrança do provedor pode ser diferente. `--dry-run` estima uma solicitação sem chamar a API.

## Ferramentas CLI

- `swarm-consensus`: consulte workers independentes e agregue os resultados.
- `swarm-benchmark`: compare execuções sequenciais e paralelas; começa no modo de simulação.
- `swarm-translate`: traduza texto armazenado no banco de dados SQLite configurado.
- `swarm-summarize`: resuma trechos armazenados no SQLite.
- `swarm-stigmergy-init`: inicialize um banco de dados local de marcadores.

Use `--help` em cada comando para ver as opções. Consenso, tradução e sumarização exigem limites de custo estimados positivos e finitos em execuções ao vivo com provedor. `ClaudeRunner` aceita um limite opcional; os demais fluxos de provedor não compartilham um limite universal.

## Limites do runtime

- No consenso, `confidence` é o número de workers que deram a resposta vencedora dividido pelo total de resultados dos workers; `agreement_ratio` usa apenas respostas válidas. Nenhuma das duas é uma probabilidade calibrada, e a concordância não comprova a correção factual.
- Os bloqueios de equipe coordenam processos cooperantes por meio de arquivos de reserva criados atomicamente e registros de presença por participante. Eles não impedem gravações de processos que ignoram ou alteram o protocolo.
- O programa herda o ambiente e as permissões de quem o executa. `RunAsInvoker` não é uma sandbox do sistema operacional e não garante ausência de elevação de privilégios.
- Os alvos de tradução `de`, `en`, `es`, `zh`, `ja` e `ru` são idiomas de saída; isso não significa que a interface esteja localizada nesses seis idiomas. A ajuda da CLI mistura inglês e alemão; a GUI experimental em Tk tem rótulos em alemão.
- O arquivo de benchmark [`results/benchmark_20260306.json`](results/benchmark_20260306.json) registra uma única carga de trabalho histórica. Suas medições não preveem o desempenho geral.

Mais detalhes de implementação estão em [Arquitetura e coordenação](docs/ARCHITECTURE.md). As tarefas abertas atuais estão em [Tarefas abertas em `TODO.md`](TODO.md#offene-aufgaben).

## Informações do projeto e segurança

A versão `0.1.3` está declarada em `pyproject.toml`; esses metadados, por si só, não significam que o pacote foi lançado. O código-fonte deste repositório está licenciado sob [MIT](LICENSE). [`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md) lista algumas dependências declaradas e não constitui uma auditoria de dependências transitivas nem uma determinação geral de que o uso comercial é permitido.

Relate vulnerabilidades por meio de [GitHub Security Advisories](https://github.com/ellmos-ai/swarm_ai/security/advisories/new) ou de um endereço indicado em [`SECURITY.md`](SECURITY.md). O projeto não publica um SLA de tempo de resposta. Consulte o [workflow do GitHub Actions](https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml) ativo para ver o status atual da CI.

Consulte [`README_de.md`](README_de.md) para a visão geral em alemão, [`README_es.md`](README_es.md) para a visão geral em espanhol e [`CHANGELOG.md`](CHANGELOG.md) para o histórico datado do projeto.

## Projetos relacionados

- [COMA](https://github.com/ellmos-ai/coma) — uma ponte opcional entre o Spawner e os adaptadores de provedor, usada pelo Swarm quando o extra `providers` está instalado.
- [Roshambo](https://github.com/ellmos-ai/roshambo) — um kit separado para coordenar agentes iniciados de forma independente por meio de leases serializáveis e memória de resultados.
- [MarbleRun](https://github.com/ellmos-ai/marblerun) — um kit separado para configurar cadeias multiagente.
