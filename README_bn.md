# swarm-ai

[English](README.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [日本語](README_ja.md) · [Русский](README_ru.md) · [简体中文](README_zh.md) · [Français](README_fr.md) · [हिन्दी](README_hi.md) · [العربية](README_ar.md) · [বাংলা](README_bn.md) · [Português](README_pt.md)

![swarm-ai ব্যানার](assets/banner.png)

**বহু-এজেন্ট LLM সমন্বয় নিয়ে পরীক্ষা করার জন্য একটি ছোট Python টুলকিট।** এতে সমান্তরাল খণ্ড প্রক্রিয়াকরণ, বস/ওয়ার্কার কর্মপ্রবাহ, SQLite-ভিত্তিক স্টিগমার্জি, সংখ্যাগরিষ্ঠ ভোটদান এবং বিশেষজ্ঞ রাউটিংয়ের উদাহরণ রয়েছে।

<p>
  <a href="https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml"><img src="https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml/badge.svg?branch=master" alt="CI-এর অবস্থা"></a>
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python 3.10+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT লাইসেন্স"></a>
</p>

সমন্বয়ের অবস্থা স্থানীয়ভাবে সংরক্ষিত হয়। Anthropic, Claude CLI বা অন্য কোনো কনফিগার করা প্রোভাইডারে করা কল প্রম্পট ও অনুরোধের ডেটা বাহ্যিক পরিষেবায় পাঠাতে পারে। সংবেদনশীল ইনপুট ব্যবহারের আগে [ডেটা প্রবাহ ও সীমাবদ্ধতা](SECURITY.md) দেখুন।

## ইনস্টল করুন

```bash
git clone https://github.com/ellmos-ai/swarm_ai.git
cd swarm_ai
python -m venv .venv
```

পরিবেশটি সক্রিয় করুন (`.venv\Scripts\Activate.ps1` PowerShell-এ অথবা `source .venv/bin/activate` Linux/macOS-এ), তারপর প্রকল্পটি ইনস্টল করুন:

```bash
python -m pip install -e .
swarm-consensus --help
```

সহায়তা কমান্ডটি কোনো API অনুরোধ করে না। COMA প্রোভাইডার ইন্টিগ্রেশনের জন্য ঐচ্ছিক এক্সট্রাটি `python -m pip install -e ".[providers]"` দিয়ে ইনস্টল করুন।

## প্রথমবার চালানো

লাইভ কনসেনসাস প্রশ্নটি কনফিগার করা Anthropic API-তে পাঠায় এবং এতে খরচ হতে পারে। `ANTHROPIC_API_KEY` সেট করুন এবং আনুমানিক খরচের সীমা দিন:

```bash
swarm-consensus --question "What is the capital of Australia?" --agents 3 --max-budget-usd 1
```

টুলে নির্ধারিত সীমাটি একটি ধনাত্মক ও সসীম আনুমানিক খরচসীমা; প্রোভাইডারের বিল আলাদা হতে পারে। `--dry-run` API-তে কল না করেই অনুরোধের খরচ অনুমান করে।

## CLI সরঞ্জাম

- `swarm-consensus`: স্বাধীন ওয়ার্কারদের প্রশ্ন করে তাদের ফলাফল একত্র করুন।
- `swarm-benchmark`: ধারাবাহিক ও সমান্তরাল রান তুলনা করে; এটি dry-run মোডে শুরু হয়।
- `swarm-translate`: কনফিগার করা SQLite ডেটাবেসে থাকা লেখা অনুবাদ করে।
- `swarm-summarize`: SQLite-তে সঞ্চিত খণ্ডগুলির সারসংক্ষেপ তৈরি করে।
- `swarm-stigmergy-init`: স্থানীয় মার্কার ডেটাবেস আরম্ভ করে।

বিকল্পের জন্য প্রতিটি কমান্ডের `--help` ব্যবহার করুন। লাইভ প্রোভাইডার রানগুলিতে কনসেনসাস, অনুবাদ ও সারাংশ তৈরির জন্য ধনাত্মক ও সসীম আনুমানিক খরচসীমা আবশ্যক। `ClaudeRunner` ঐচ্ছিক সীমা সমর্থন করে; অন্য প্রোভাইডার প্রবাহগুলিতে সবার জন্য একক সাধারণ সীমা নেই।

## রানটাইম সীমাবদ্ধতা

- কনসেনসাসে `confidence` হলো সব ওয়ার্কার ফলাফলের মোট সংখ্যা দিয়ে ভাগ করা বিজয়ী ফলাফলের সংখ্যা; `agreement_ratio` হিসাব করতে শুধু বৈধ উত্তর ব্যবহার করা হয়। কোনোটিই ক্যালিব্রেট করা সম্ভাব্যতা নয়, আর মতৈক্য তথ্যের সত্যতা প্রমাণ করে না।
- দলীয় লকগুলো অ্যাটমিক ফাইল-দাবি এবং অংশগ্রহণকারী-প্রতি উপস্থিতির নথি ব্যবহার করে সহযোগী প্রক্রিয়াগুলোর মধ্যে সমন্বয় করে। প্রোটোকল উপেক্ষা বা সম্পাদনা করে এমন প্রক্রিয়ার লেখা এগুলো আটকায় না।
- প্রোগ্রামটি কলকারীর পরিবেশ ও অনুমতিসমূহ উত্তরাধিকারসূত্রে পায়। `RunAsInvoker` অপারেটিং-সিস্টেম স্যান্ডবক্স নয় এবং এটি উচ্চতর অনুমতি ছাড়া চলার নিশ্চয়তা দেয় না।
- অনুবাদের লক্ষ্য `de`, `en`, `es`, `zh`, `ja` ও `ru` হলো আউটপুট ভাষা, ছয়টি স্থানীয়কৃত UI ভাষা নয়। CLI সহায়তায় ইংরেজি ও জার্মান মিশে আছে; পরীক্ষামূলক Tk GUI-তে জার্মান লেবেল রয়েছে।
- বেঞ্চমার্ক ফাইল [`results/benchmark_20260306.json`](results/benchmark_20260306.json) একটি ঐতিহাসিক কাজের চাপ নথিভুক্ত করে। এর পরিমাপ সাধারণ কর্মদক্ষতার পূর্বাভাস দেয় না।

বাস্তবায়ন সম্পর্কে আরও বিস্তারিত [স্থাপত্য ও সমন্বয়](docs/ARCHITECTURE.md)-এ আছে। বর্তমান খোলা কাজগুলি [`TODO.md`-এর খোলা কাজ](TODO.md#offene-aufgaben)-এ রয়েছে।

## প্রকল্প ও নিরাপত্তার তথ্য

`0.1.3` সংস্করণটি `pyproject.toml`-এ ঘোষিত; শুধু এই মেটাডেটা প্যাকেজ প্রকাশিত হয়েছে এমন বোঝায় না। এই রিপোজিটরির সোর্স [MIT](LICENSE) লাইসেন্সের অধীনে। [`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md)-এ বেছে নেওয়া কিছু ঘোষিত নির্ভরতার তালিকা আছে; এটি পারগমনশীল নির্ভরতার নিরীক্ষা বা বাণিজ্যিক ব্যবহারের সার্বিক অনুমোদন নয়।

দুর্বলতার খবর [GitHub Security Advisories](https://github.com/ellmos-ai/swarm_ai/security/advisories/new)-এ জানান, অথবা [`SECURITY.md`](SECURITY.md)-এ দেওয়া কোনো ঠিকানায় পাঠান। প্রকল্পটি সাড়া দেওয়ার সময়সীমা SLA হিসেবে প্রকাশ করে না। বর্তমান CI অবস্থা জানতে সরাসরি [GitHub Actions কর্মপ্রবাহ](https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml) দেখুন।

জার্মান সারাংশের জন্য [`README_de.md`](README_de.md), স্প্যানিশ সারাংশের জন্য [`README_es.md`](README_es.md), এবং তারিখ-সহ প্রকল্পের ইতিহাসের জন্য [`CHANGELOG.md`](CHANGELOG.md) দেখুন।

## সংশ্লিষ্ট প্রকল্প

- [COMA](https://github.com/ellmos-ai/coma) — Swarm-এ `providers` এক্সট্রা ইনস্টল থাকলে ব্যবহৃত ঐচ্ছিক Spawner/adapter প্রোভাইডার সেতু।
- [Roshambo](https://github.com/ellmos-ai/roshambo) — স্বতন্ত্রভাবে চালু করা এজেন্টদের সমন্বয়ে সিরিয়ালাইজ করা যায় এমন লিজ ও ফলাফল-স্মৃতি ব্যবহারের পৃথক টুলকিট।
- [MarbleRun](https://github.com/ellmos-ai/marblerun) — বহু-এজেন্ট চেইন কনফিগার করার পৃথক টুলকিট।
