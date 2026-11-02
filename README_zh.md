# swarm-ai

[English](README.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [日本語](README_ja.md) · [Русский](README_ru.md) · [简体中文](README_zh.md) · [Français](README_fr.md) · [हिन्दी](README_hi.md) · [العربية](README_ar.md) · [বাংলা](README_bn.md) · [Português](README_pt.md)

![swarm-ai 横幅](assets/banner.png)

**一个用于试验多智能体 LLM 协作的小型 Python 工具包。**其中包含并行分块处理、主管/工作者工作流、由 SQLite 支持的痕迹协作、多数投票和专家路由示例。

<p>
  <a href="https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml"><img src="https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml/badge.svg?branch=master" alt="CI 状态"></a>
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python 3.10+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT 许可证"></a>
</p>

协作状态存储在本地。调用 Anthropic、Claude CLI 或其他已配置的提供方时，提示词和请求数据可能会发送到外部服务。使用敏感输入前，请参阅[数据流与限制](SECURITY.md)。

## 安装

```bash
git clone https://github.com/ellmos-ai/swarm_ai.git
cd swarm_ai
python -m venv .venv
```

激活环境（在 PowerShell 中运行 `.venv\Scripts\Activate.ps1`，或在 Linux/macOS 上运行 `source .venv/bin/activate`），然后安装项目：

```bash
python -m pip install -e .
swarm-consensus --help
```

帮助命令不会发出 API 请求。要集成 COMA 提供方，请使用 `python -m pip install -e ".[providers]"` 安装可选扩展。

## 首次运行

实时共识会将问题发送到已配置的 Anthropic API，并可能产生费用。请设置 `ANTHROPIC_API_KEY` 并提供一个估算费用上限：

```bash
swarm-consensus --question "What is the capital of Australia?" --agents 3 --max-budget-usd 1
```

工具要求该估算上限为正且有限；提供方的实际计费金额可能不同。`--dry-run` 会估算请求，但不会调用 API。

## CLI 工具

- `swarm-consensus`：向互相独立的工作者提问并汇总其结果。
- `swarm-benchmark`：比较顺序运行和并行运行；默认以 dry-run 模式启动。
- `swarm-translate`：翻译存储在已配置 SQLite 数据库中的文本。
- `swarm-summarize`：汇总存储在 SQLite 中的文本块。
- `swarm-stigmergy-init`：初始化本地标记数据库。

使用各命令的 `--help` 查看选项。实时运行提供方时，共识、翻译和摘要功能都要求设置正且有限的估算费用上限。`ClaudeRunner` 支持可选上限；其他提供方流程没有共用的统一上限。

## 运行时边界

- 共识结果中的 `confidence` 是支持胜出答案的结果数除以所有工作者结果数；`agreement_ratio` 仅以有效答案为分母。二者都不是经过校准的概率，一致性也不能证明答案在事实上正确。
- 团队锁通过原子化的文件认领和每位参与者的出席记录来协调遵守协议的进程。它们无法阻止忽略或修改该协议的进程写入。
- 程序继承调用者的环境和权限。`RunAsInvoker` 不是操作系统沙箱，也不保证程序不会以提升的权限运行。
- 翻译目标 `de`、`en`、`es`、`zh`、`ja` 和 `ru` 是输出语言，并不代表界面有六种本地化语言。CLI 帮助混用英语和德语；实验性的 Tk GUI 使用德语标签。
- 基准测试文件 [`results/benchmark_20260306.json`](results/benchmark_20260306.json) 记录了一次历史工作负载。其测量结果无法预测一般情况下的性能。

更多实现细节请见[架构与协作](docs/ARCHITECTURE.md)。当前未完成的任务见 [`TODO.md` 中的未完成任务](TODO.md#offene-aufgaben)。

## 项目与安全信息

`pyproject.toml` 中声明的版本为 `0.1.3`；仅有这项元数据并不意味着该软件包已发布。本仓库的源代码采用 [MIT](LICENSE) 许可。[`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md) 列出部分已声明依赖项；它不构成传递依赖审计，也不构成对商业用途的一概认定。

请通过 [GitHub Security Advisories](https://github.com/ellmos-ai/swarm_ai/security/advisories/new) 或 [`SECURITY.md`](SECURITY.md) 中列出的地址报告漏洞。该项目没有公布响应时间 SLA。请查看实时的 [GitHub Actions 工作流](https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml) 了解当前 CI 状态。

参阅 [`README_de.md`](README_de.md) 查看德语概览，参阅 [`README_es.md`](README_es.md) 查看西班牙语概览；项目的历史变更记录见 [`CHANGELOG.md`](CHANGELOG.md)。

## 相关项目

- [COMA](https://github.com/ellmos-ai/coma) — 一个可选的 Spawner/adapter 提供方桥接层；安装 `providers` 扩展后，Swarm 会使用它。
- [Roshambo](https://github.com/ellmos-ai/roshambo) — 一个独立工具包，通过可序列化租约和结果记忆来协调独立启动的智能体。
- [MarbleRun](https://github.com/ellmos-ai/marblerun) — 一个用于配置多智能体链的独立工具包。
