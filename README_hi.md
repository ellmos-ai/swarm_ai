# swarm-ai

[English](README.md) · [Deutsch](README_de.md) · [Español](README_es.md) · [日本語](README_ja.md) · [Русский](README_ru.md) · [简体中文](README_zh.md) · [Français](README_fr.md) · [हिन्दी](README_hi.md) · [العربية](README_ar.md) · [বাংলা](README_bn.md) · [Português](README_pt.md)

![swarm-ai बैनर](assets/banner.png)

**बहु-एजेंट LLM समन्वय के प्रयोगों के लिए एक छोटा Python टूलकिट।** इसमें समानांतर खंड-प्रसंस्करण, बॉस/वर्कर कार्यप्रवाह, SQLite-आधारित स्टिग्मर्जी, बहुमत मतदान और विशेषज्ञ रूटिंग के उदाहरण शामिल हैं।

<p>
  <a href="https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml"><img src="https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml/badge.svg?branch=master" alt="CI की स्थिति"></a>
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python 3.10+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT लाइसेंस"></a>
</p>

समन्वय की स्थिति स्थानीय रूप से संग्रहीत होती है। Anthropic, Claude CLI या किसी अन्य कॉन्फ़िगर किए गए प्रोवाइडर को किए गए कॉल प्रॉम्प्ट और अनुरोध डेटा बाहरी सेवाओं को भेज सकते हैं। संवेदनशील इनपुट इस्तेमाल करने से पहले [डेटा प्रवाह और सीमाएँ](SECURITY.md) देखें।

## इंस्टॉल करें

```bash
git clone https://github.com/ellmos-ai/swarm_ai.git
cd swarm_ai
python -m venv .venv
```

परिवेश सक्रिय करें (`.venv\Scripts\Activate.ps1` को PowerShell में या `source .venv/bin/activate` को Linux/macOS पर), फिर प्रोजेक्ट इंस्टॉल करें:

```bash
python -m pip install -e .
swarm-consensus --help
```

हेल्प कमांड कोई API अनुरोध नहीं करता। COMA प्रोवाइडर इंटीग्रेशन के लिए वैकल्पिक एक्स्ट्रा `python -m pip install -e ".[providers]"` से इंस्टॉल करें।

## पहली बार चलाना

लाइव कंसेंसस प्रश्न को कॉन्फ़िगर किए गए Anthropic API को भेजता है और शुल्क लग सकता है। `ANTHROPIC_API_KEY` सेट करें और अनुमानित लागत-सीमा दें:

```bash
swarm-consensus --question "What is the capital of Australia?" --agents 3 --max-budget-usd 1
```

यह सीमा टूल में धनात्मक और परिमित अनुमानित लागत-सीमा है; प्रोवाइडर की बिलिंग इससे अलग हो सकती है। `--dry-run` API को कॉल किए बिना अनुरोध का अनुमान देता है।

## CLI उपकरण

- `swarm-consensus`: स्वतंत्र वर्करों से प्रश्न पूछें और उनके परिणामों का समेकन करें।
- `swarm-benchmark`: क्रमिक और समानांतर निष्पादनों की तुलना करें; यह dry-run मोड से शुरू होता है।
- `swarm-translate`: कॉन्फ़िगर किए गए SQLite डेटाबेस में संग्रहीत पाठ का अनुवाद करें।
- `swarm-summarize`: SQLite में संग्रहीत खंडों का सारांश बनाएं।
- `swarm-stigmergy-init`: स्थानीय मार्कर डेटाबेस को आरंभ करें।

विकल्पों के लिए प्रत्येक कमांड का `--help` देखें। लाइव प्रोवाइडर रन के लिए कंसेंसस, अनुवाद और सारांश-निर्माण में धनात्मक और परिमित अनुमानित लागत-सीमाएँ आवश्यक हैं। `ClaudeRunner` वैकल्पिक सीमा का समर्थन करता है; अन्य प्रोवाइडर प्रवाहों में कोई एक साझा सार्वभौमिक सीमा नहीं है।

## रनटाइम सीमाएँ

- कंसेंसस में `confidence` सभी वर्कर परिणामों की कुल संख्या से विभाजित विजेता के परिणामों की संख्या है; `agreement_ratio` केवल मान्य उत्तरों का उपयोग करता है। इनमें से कोई भी कैलिब्रेट की गई प्रायिकता नहीं है, और सहमति तथ्यात्मक शुद्धता सिद्ध नहीं करती।
- टीम लॉक परमाण्विक फ़ाइल-दावों और प्रति-प्रतिभागी उपस्थिति अभिलेखों का उपयोग करके सहयोग करने वाली प्रक्रियाओं के बीच समन्वय करते हैं। वे उन प्रक्रियाओं के लेखन को नहीं रोकते जो प्रोटोकॉल की अनदेखी करती हैं या उसमें बदलाव करती हैं।
- प्रोग्राम कॉलर का परिवेश और अनुमतियाँ विरासत में लेता है। `RunAsInvoker` ऑपरेटिंग-सिस्टम सैंडबॉक्स नहीं है और यह गारंटी नहीं देता कि प्रोग्राम उच्चतर अधिकारों के बिना चलेगा।
- अनुवाद के लक्ष्य `de`, `en`, `es`, `zh`, `ja` और `ru` आउटपुट भाषाएँ हैं, छह स्थानीयकृत UI भाषाएँ नहीं। CLI हेल्प में अंग्रेज़ी और जर्मन मिला हुआ है; प्रयोगात्मक Tk GUI के लेबल जर्मन में हैं।
- बेंचमार्क फ़ाइल [`results/benchmark_20260306.json`](results/benchmark_20260306.json) एक ऐतिहासिक कार्यभार दर्ज करती है। इसके मापन सामान्य प्रदर्शन का अनुमान नहीं बताते।

कार्यान्वयन का अधिक विवरण [वास्तुकला और समन्वय](docs/ARCHITECTURE.md) में है। मौजूदा खुले कार्य [`TODO.md` में खुले कार्य](TODO.md#offene-aufgaben) के अंतर्गत हैं।

## परियोजना और सुरक्षा की जानकारी

संस्करण `0.1.3` की घोषणा `pyproject.toml` में है; केवल यह मेटाडेटा पैकेज रिलीज़ होने का संकेत नहीं देता। इस रिपॉज़िटरी का स्रोत [MIT](LICENSE) लाइसेंस के तहत है। [`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md) कुछ घोषित निर्भरताओं की सूची देता है; यह पारगामी निर्भरता-जाँच या व्यावसायिक उपयोग की सार्वभौमिक मंज़ूरी नहीं है।

कमज़ोरियों की सूचना [GitHub Security Advisories](https://github.com/ellmos-ai/swarm_ai/security/advisories/new) के माध्यम से दें या [`SECURITY.md`](SECURITY.md) में दिए गए किसी पते पर भेजें। परियोजना प्रतिक्रिया-समय SLA प्रकाशित नहीं करती। CI की मौजूदा स्थिति के लिए लाइव [GitHub Actions वर्कफ़्लो](https://github.com/ellmos-ai/swarm_ai/actions/workflows/ci.yml) देखें।

जर्मन परिचय के लिए [`README_de.md`](README_de.md), स्पैनिश परिचय के लिए [`README_es.md`](README_es.md), और तारीख़वार परियोजना इतिहास के लिए [`CHANGELOG.md`](CHANGELOG.md) देखें।

## संबंधित परियोजनाएँ

- [COMA](https://github.com/ellmos-ai/coma) — Swarm में `providers` एक्स्ट्रा इंस्टॉल होने पर इस्तेमाल होने वाला वैकल्पिक Spawner/adapter प्रोवाइडर ब्रिज।
- [Roshambo](https://github.com/ellmos-ai/roshambo) — स्वतंत्र रूप से शुरू किए गए एजेंटों के समन्वय के लिए सीरियलाइज़ किए जा सकने वाले लीज़ और परिणाम-स्मृति वाला अलग टूलकिट।
- [MarbleRun](https://github.com/ellmos-ai/marblerun) — बहु-एजेंट श्रृंखलाएँ कॉन्फ़िगर करने के लिए अलग टूलकिट।
