# swarm-ai

[English](README.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [日本語](README_ja.md) · [Русский](README_ru.md) · [简体中文](README_zh.md) · [Français](README_fr.md) · [हिन्दी](README_hi.md) · [العربية](README_ar.md) · [বাংলা](README_bn.md) · [Português](README_pt.md)

![لافتة swarm-ai](assets/banner.png)

**مجموعة أدوات Python صغيرة للتجريب في تنسيق نماذج اللغة الكبيرة متعددة الوكلاء.** تتضمن أمثلة لمعالجة المقاطع بالتوازي، وسير العمل بنمط المدير/العامل، والتنسيق غير المباشر المستند إلى SQLite، والتصويت بالأغلبية، والتوجيه إلى المتخصصين.

<p>
  <a href="https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml"><img src="https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml/badge.svg?branch=master" alt="حالة CI"></a>
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python 3.10+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="ترخيص MIT"></a>
</p>

تُخزَّن حالة التنسيق محليًا. قد ترسل الطلبات الموجّهة إلى Anthropic أو Claude CLI أو مزوّد مُعدّ آخر، بما فيها المطالبات وبيانات الطلب، إلى خدمات خارجية. راجع [تدفق البيانات والحدود](SECURITY.md) قبل استخدام مدخلات حساسة.

## التثبيت

```bash
git clone https://github.com/ellmos-ai/swarm_ai.git
cd swarm_ai
python -m venv .venv
```

فعّل البيئة (`.venv\Scripts\Activate.ps1` في PowerShell أو `source .venv/bin/activate` على Linux/macOS)، ثم ثبّت المشروع:

```bash
python -m pip install -e .
swarm-consensus --help
```

لا يرسل أمر المساعدة طلبًا إلى API. لتكامل مزوّدي COMA، ثبّت الإضافة الاختيارية باستخدام `python -m pip install -e ".[providers]"`.

## التشغيل الأول

يرسل تشغيل الإجماع المباشر السؤال إلى Anthropic API المُعدّة وقد تترتب عليه تكلفة. عيّن `ANTHROPIC_API_KEY` وقدّم حدًا تقديريًا للتكلفة:

```bash
swarm-consensus --question "What is the capital of Australia?" --agents 3 --max-budget-usd 1
```

الحد سقف تقديري موجب ومنتهٍ داخل الأداة؛ وقد تختلف فوترة المزوّد. يقدّر `--dry-run` الطلب دون الاتصال بـ API.

## أدوات CLI

- `swarm-consensus`: استشر عمّالًا مستقلين واجمع نتائجهم.
- `swarm-benchmark`: قارن بين التشغيلين المتسلسل والمتوازي؛ ويبدأ في وضع التشغيل التجريبي.
- `swarm-translate`: ترجم نصًا مخزنًا في قاعدة بيانات SQLite المُعدّة.
- `swarm-summarize`: لخّص المقاطع المخزنة في SQLite.
- `swarm-stigmergy-init`: هيّئ قاعدة بيانات محلية للعلامات.

استخدم `--help` لكل أمر للاطّلاع على الخيارات. يتطلب الإجماع والترجمة والتلخيص حدودًا تقديرية موجبة ومنتهية عند التشغيل المباشر عبر المزوّد. يدعم `ClaudeRunner` حدًا اختياريًا؛ أما تدفقات المزوّدين الأخرى فلا تشترك في حدّ موحّد.

## حدود التشغيل

- في الإجماع، تمثل `confidence` عدد نتائج الإجابة الفائزة مقسومًا على جميع نتائج العاملين؛ أما `agreement_ratio` فيستخدم الإجابات الصالحة فقط. ولا يمثّل أيٌّ منهما احتمالًا معايرًا، كما أن الاتفاق لا يثبت صحة الوقائع.
- تستخدم أقفال الفريق مطالبات ملفّية تُنشأ بصورة ذرّية وسجلات حضور لكل مشارك لتنسيق العمليات المتعاونة. لكنها لا تمنع الكتابة من عمليات تتجاهل البروتوكول أو تعدّله.
- يرث البرنامج بيئة المستدعي وصلاحياته. إن `RunAsInvoker` ليس عزلًا على مستوى نظام التشغيل ولا يضمن عدم الارتقاء بالصلاحيات.
- أهداف الترجمة `de` و`en` و`es` و`zh` و`ja` و`ru` هي لغات للمخرجات، ولا يعني ذلك أن واجهة المستخدم موطّنة بهذه اللغات الست. تمزج مساعدة CLI بين الإنجليزية والألمانية؛ وتحمل واجهة Tk التجريبية تسميات ألمانية.
- يسجّل ملف المقارنة [`results/benchmark_20260306.json`](results/benchmark_20260306.json) عبء عمل تاريخيًا واحدًا. ولا تتنبأ قياساته بالأداء العام.

ترد تفاصيل تنفيذ إضافية في [البنية والتنسيق](docs/ARCHITECTURE.md). وترد المهام المفتوحة الحالية ضمن [المهام المفتوحة في `TODO.md`](TODO.md#offene-aufgaben).

## معلومات المشروع والأمان

الإصدار `0.1.3` مُعلن في `pyproject.toml`؛ وهذه البيانات الوصفية وحدها لا تعني إصدار الحزمة. مصدر هذا المستودع مرخّص بموجب [MIT](LICENSE). يسرد [`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md) مجموعة مختارة من التبعيات المعلنة، ولا يُعدّ تدقيقًا للتبعيات العابرة أو حكمًا عامًا بشأن الاستخدام التجاري.

أبلغ عن الثغرات عبر [إشعارات الأمان من GitHub](https://github.com/ellmos-ai/swarm_ai/security/advisories/new) أو عنوان مدرج في [`SECURITY.md`](SECURITY.md). لا ينشر المشروع اتفاقية مستوى خدمة لزمن الاستجابة. راجع [سير عمل GitHub Actions](https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml) المباشر لمعرفة حالة CI الحالية.

راجع [`README_de.md`](README_de.md) للاطلاع على النظرة العامة بالألمانية، و[`README_es.md`](README_es.md) للنظرة العامة بالإسبانية، و[`CHANGELOG.md`](CHANGELOG.md) لسجل المشروع المؤرّخ.

## مشاريع ذات صلة

- [COMA](https://github.com/ellmos-ai/coma) — جسر اختياري للمزوّدين يربط Spawner بمحوّل ويستخدمه Swarm عند تثبيت الإضافة `providers`.
- [Roshambo](https://github.com/ellmos-ai/roshambo) — مجموعة أدوات منفصلة لتنسيق وكلاء يُطلَقون بشكل مستقل عبر حجوزات مؤقتة قابلة للتسلسل وذاكرة للنتائج.
- [MarbleRun](https://github.com/ellmos-ai/marblerun) — مجموعة أدوات منفصلة لإعداد سلاسل متعددة الوكلاء.
