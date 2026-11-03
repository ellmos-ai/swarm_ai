# swarm-ai

[English](README.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [日本語](README_ja.md) · [Русский](README_ru.md) · [简体中文](README_zh.md) · [Français](README_fr.md) · [हिन्दी](README_hi.md) · [العربية](README_ar.md) · [বাংলা](README_bn.md) · [Português](README_pt.md)

![swarm-ai バナー](assets/banner.png)

**複数のLLMエージェントによる協調を試すための小さなPythonツールキットです。** 並列チャンク処理、ボス／ワーカー方式のワークフロー、SQLiteを使ったスティグマジー、多数決、専門エージェントへの振り分けの例を含みます。

<p>
  <a href="https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml"><img src="https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml/badge.svg?branch=master" alt="CIの状態"></a>
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python 3.10+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MITライセンス"></a>
</p>

協調状態はローカルに保存されます。Anthropic、Claude CLI、またはその他の設定済みプロバイダーへの呼び出しでは、プロンプトやリクエストデータが外部サービスに送信される場合があります。機密情報を入力する前に、[データフローと制限事項](SECURITY.md)を確認してください。

## インストール

```bash
git clone https://github.com/ellmos-ai/swarm_ai.git
cd swarm_ai
python -m venv .venv
```

仮想環境（PowerShellでは`.venv\Scripts\Activate.ps1`、Linux/macOSでは`source .venv/bin/activate`）を有効にしてから、プロジェクトをインストールします。

```bash
python -m pip install -e .
swarm-consensus --help
```

ヘルプコマンドはAPIリクエストを行いません。COMAプロバイダー連携を使うには、任意の追加機能を`python -m pip install -e ".[providers]"`でインストールしてください。

## 初回実行

実際にコンセンサスを実行すると、質問が設定済みのAnthropic APIに送信され、料金が発生する場合があります。`ANTHROPIC_API_KEY`を設定し、推定費用の上限を指定してください。

```bash
swarm-consensus --question "What is the capital of Australia?" --agents 3 --max-budget-usd 1
```

この上限は、ツールに指定する正の有限な費用見積もり値です。実際のプロバイダー請求額は異なる場合があります。`--dry-run`はAPIを呼び出さずにリクエストを見積もります。

## CLIツール

- `swarm-consensus`: 独立したワーカーに質問し、回答を集約します。
- `swarm-benchmark`: 逐次実行と並列実行を比較します。初期状態ではドライランで開始します。
- `swarm-translate`: 設定済みのSQLiteデータベースに保存されたテキストを翻訳します。
- `swarm-summarize`: SQLiteに保存されたチャンクを要約します。
- `swarm-stigmergy-init`: ローカルのマーカーデータベースを初期化します。

各コマンドのオプションは`--help`で確認できます。プロバイダーを実際に呼び出すコンセンサス、翻訳、要約では、正の有限な推定費用上限が必要です。`ClaudeRunner`には任意の上限を設定できますが、他のプロバイダーフローに共通の単一上限はありません。

## 実行時の境界

- コンセンサスの`confidence`は、勝者の票数を全ワーカーの結果数で割った値です。`agreement_ratio`の計算対象は有効な回答だけです。どちらも確率として較正されておらず、回答の一致は事実の正しさを証明しません。
- チームロックは、アトミックなファイル確保と参加者ごとの出席記録を使い、協調に参加するプロセス同士を調整します。この手順を無視または変更するプロセスによる書き込みは防げません。
- プログラムは呼び出し元の環境と権限を引き継ぎます。`RunAsInvoker`はOSのサンドボックスではなく、昇格されないことも保証しません。
- 翻訳先の`de`、`en`、`es`、`zh`、`ja`、`ru`は出力言語であり、UIが6言語にローカライズされているという意味ではありません。CLIのヘルプは英語とドイツ語が混在し、実験的なTk GUIのラベルはドイツ語です。
- ベンチマークファイル[`results/benchmark_20260306.json`](results/benchmark_20260306.json)が記録しているのは、過去の1つのワークロードです。その測定値から一般的な性能を予測することはできません。

実装の詳しい説明は[アーキテクチャと協調](docs/ARCHITECTURE.md)にあります。現在の未完了タスクは[`TODO.md`の未完了タスク](TODO.md#offene-aufgaben)に記載されています。

## プロジェクトとセキュリティ

バージョン`0.1.3`は`pyproject.toml`で宣言されていますが、そのメタデータだけではパッケージの公開を意味しません。このリポジトリのソースコードは[MITライセンス](LICENSE)で提供されています。[`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md)には一部の宣言済み依存関係が記載されていますが、推移的依存関係の監査ではなく、商用利用を一律に判断するものでもありません。

脆弱性は[GitHub Security Advisories](https://github.com/ellmos-ai/swarm_ai/security/advisories/new)、または[`SECURITY.md`](SECURITY.md)に記載された連絡先へ報告してください。プロジェクトは応答時間のSLAを公表していません。現在のCI状況は[GitHub Actionsのワークフロー](https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml)で確認してください。

ドイツ語の概要は[`README_de.md`](README_de.md)、スペイン語の概要は[`README_es.md`](README_es.md)をご覧ください。日付順のプロジェクト履歴は[`CHANGELOG.md`](CHANGELOG.md)にあります。

## 関連プロジェクト

- [COMA](https://github.com/ellmos-ai/coma) — 任意で使えるSpawner／adapterプロバイダーブリッジです。`providers`追加機能をインストールすると、Swarmから利用できます。
- [Roshambo](https://github.com/ellmos-ai/roshambo) — シリアライズ可能なリースと結果メモリーを使い、独立して起動したエージェントを連携させる別個のツールキットです。
- [MarbleRun](https://github.com/ellmos-ai/marblerun) — 複数エージェントのチェーンを設定するための別個のツールキットです。
