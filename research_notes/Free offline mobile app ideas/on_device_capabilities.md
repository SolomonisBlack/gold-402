# On-device capabilities for free, zero-server-cost iOS and Android apps (as of November 2026)

Scope note: research done 2026-11-06 with about 22 tool calls. Some items come from secondary blogs, and I've labeled those. Facts marked "[background, unverified this session]" are from pre-2026 general knowledge and were not re-checked against a source. The report writer should treat them as context, not citable facts.

## 1. Apple: Foundation Models framework and adjacent on-device frameworks (iOS 26 to iOS 27)

### Takeaway
iOS 27 (WWDC26) rebuilt Apple's on-device LLM. It now has an 8,192-token context (up from 4,096), image input, built-in Vision OCR and barcode tools, Spotlight-backed local RAG, and agentic "Dynamic Profiles". Guided generation (@Generable) and tool calling carry over from iOS 26. All of it runs free with no API key. Apple also added a free tier of its much larger Private Cloud Compute (PCC) model for small developers, plus a new Core AI framework for running your own models on-device. The catch is device coverage: only Apple Intelligence-capable iPhones (iPhone 15 Pro and later) can use it.

### Cited Findings
**Foundation Models (FM): iOS 27 / WWDC26**
- Apple calls the on-device model "rebuilt from the ground up" and says it is "more intelligent; better at logic and tool calling". The session code shows `SystemLanguageModel().contextSize` returning 8192. Context-size and token-count APIs arrived in iOS 26.4. — [Apple WWDC26 session 241](https://developer.apple.com/videos/play/wwdc2026/241/)
- Conflict: an Apple WWDC26 Group Lab answer, as summarized by the search tool, said the on-device window stays at 4,096 tokens shared between input and output. The session 241 code shows 8,192. The session is the more authoritative primary source. — [WWDC26 Group Lab](https://developer.apple.com/videos/play/wwdc2026/8121/) vs [session 241](https://developer.apple.com/videos/play/wwdc2026/241/)
- Image input: the on-device model now accepts image attachments (UIImage, CGImage, pixel buffers, file URLs). Images can be any size or aspect ratio, but larger images cost more tokens and add latency. — [Apple WWDC26 session 241](https://developer.apple.com/videos/play/wwdc2026/241/)
- System tools: `OCRTool` (structured text extraction from images) and `BarcodeReaderTool` are both backed by Vision and run on-device. A Spotlight search tool enables "fully local Retrieval-Augmented Generation". — [Apple WWDC26 session 241](https://developer.apple.com/videos/play/wwdc2026/241/); [Apple WWDC26 iOS guide](https://developer.apple.com/wwdc26/guides/ios/)
- Guardrails: iOS 26.4 reduced false positives, and Apple says more improvements are coming in iOS 27. — [Apple WWDC26 session 241](https://developer.apple.com/videos/play/wwdc2026/241/)
- New `LanguageModel` protocol: a session can be backed by the system model, PCC, Claude or Gemini (via partner Swift packages from Anthropic and Google), or open-sourced `CoreAILanguageModel` and `MLXLanguageModel` for running local models. — [Apple WWDC26 session 241](https://developer.apple.com/videos/play/wwdc2026/241/)
- Dynamic Profiles let an app swap instructions, tools and model (for example, on-device to PCC) within one session while keeping context. There is also a new Evaluations framework, an `fm` CLI on macOS 27, and a Python SDK. Apple says the core FM framework is being open-sourced. — [Apple WWDC26 session 241](https://developer.apple.com/videos/play/wwdc2026/241/)
- PCC model terms: 32K-token context, adjustable reasoning level, no API keys. It is free ("no cloud API cost") for apps in the App Store Small Business Program with fewer than 2 million total first-time downloads. End users get daily PCC access, with higher limits for iCloud+ subscribers. It requires an entitlement. — [Apple WWDC26 session 241](https://developer.apple.com/videos/play/wwdc2026/241/); [Apple WWDC26 iOS guide](https://developer.apple.com/wwdc26/guides/ios/)
- Core AI (new in iOS 27) is "a new framework built directly into the OS". It lets apps "load, specialize, and run AI models entirely on-device... with zero server dependencies and zero token costs", with ahead-of-time compilation, memory control, and support from compact vision models up to large generative ones. — [Apple WWDC26 iOS guide](https://developer.apple.com/wwdc26/guides/ios/)
- Other iOS 27 additions: the Music Understanding framework analyzes audio "across six dimensions on your device". App Intents entity schemas feed the Spotlight semantic index so Siri can surface app content. Widgets can now be customized via App Intents. — [Apple WWDC26 iOS guide](https://developer.apple.com/wwdc26/guides/ios/)
- Secondary sources disagree on model size. The 2025 figure is about 3B parameters. Some 2026 blogs claim a newer "AFM 3 Core Advanced" with about 20B total and 1–4B active parameters. That claim is unverified. — [Search summary incl. infinum](https://infinum.com/blog/apple-on-device-ai/), [lavx news](https://news.lavx.hu/article/apple-s-third-generation-foundation-models-five-ai-engines-on-device-and-in-google-s-cloud)

**Model limits (design intent)**
- Apple stated in 2025 that because of its reduced size, the on-device model "isn't intended to implement a world-knowledge chat". It targets extraction, summarization, image understanding and reasoning. — [InfoQ / Apple 2025 material via search](https://www.infoq.com/news/2025/07/apple-foundation-models-ios26)
- A developer's view: "For complex reasoning, long documents, or open-ended conversations, you still need the cloud." — [Etnetera blog](https://flow.etnetera.cz/blog/on-device-ai-with-apple-foundation-models-what-i-learned-building-with-it)
- TechCrunch (Oct 2025): "Apple's models are small compared with leading models from OpenAI, Anthropic, Google, or Meta", so early adopters mostly shipped quality-of-life features. Developers use the models "without worrying about any inference cost". — [TechCrunch](https://www.techcrunch.com/2025/10/03/how-developers-are-using-apples-local-ai-models-with-ios-26/)

**Speech (SpeechAnalyzer, iOS 26+)**
- Inscribe developer benchmark (July 2026): SpeechAnalyzer had a 2.12% word error rate (WER) on LibriSpeech test-clean, against 3.74% for Whisper Small and 7.88% for Whisper Tiny. On test-other, the figures were 4.56% vs 7.95%. It was also about 3x faster. — [Gigazine](https://www.gigazine.net/gsc_news/en/20260714-apple-speech-analyzer-benchmark/)
- Argmax (June 2025, M4 Mac mini, long-form conversational audio): Apple "matches the speed and accuracy of mid-tier OpenAI Whisper models". The error rate was 14.0 for SpeechAnalyzer vs 12.8 for Whisper small.en, but SpeechAnalyzer was about 2x faster (speed factor 70 vs 35). Its model is a system download, not preinstalled. — [Argmax](https://www.argmaxinc.com/blog/apple-and-argmax)

**Translation framework**
- `translationPresentation` requires iOS 17.4+. Programmatic `TranslationSession` / `translationTask` requires iOS 18+. It runs locally with no API key and no network call once the language is installed. Batch translation is supported. The first use of a language pair downloads assets. It is SwiftUI-only and doesn't run in the Simulator. — [Blake Crosley](https://blakecrosley.com/blog/apple-translation-framework-on-device)
- On quality, the same source calls it "good, not the best available" and recommends cloud translation for legal or medical content. It suggests wrapping FM calls with translation to make English-only features multilingual. — [Blake Crosley](https://blakecrosley.com/blog/apple-translation-framework-on-device)

**Vision**
- Vision has a `RecognizeDocumentsRequest` with supported recognition languages, added in iOS 26 for structured document recognition. — [Apple docs](https://developer.apple.com/documentation/vision/recognizedocumentsrequest/supportedrecognitionlanguages.md); [Kodeco](https://www.kodeco.com/ios/programs/apple-intelligence/apple-ai-models/49307523-vision-framework/04-unveiling-new-vision-framework-features-in-ios-18-ios-26/05)

### Inferences
- iOS 27 FM can now do basic multimodal "photo in, structured JSON out" with no server. Examples include identifying a meal, reading a label, or parsing a receipt using @Generable plus OCRTool. Before iOS 27, that needed a cloud vision LLM. This is the biggest new unlock for free apps.
- With 8K context, a long transcript (over roughly 45–60 minutes of speech) still has to be chunked and summarized in stages. That is my estimate, not sourced.
- The PCC free tier is technically Apple's server, not on-device. It costs the developer nothing up to 2M downloads, so it can serve as a "hard query" fallback without breaking a zero-cost model. It may break a strict "no server" or privacy pitch, and the daily per-user caps are not quantified.
- [background, unverified this session] Long-standing free on-device Apple frameworks also enable zero-cost apps. These include VisionKit document camera, Live Text, subject lifting (iOS 16+), Vision body and hand pose, SoundAnalysis (built-in classifier of about 300 sounds), ARKit plus LiDAR depth (Pro models only), HealthKit, Live Activities, and widgets.

### Gaps
- Number of languages FM supports on iOS 27, and whether the image-input on-device model runs on all Apple Intelligence devices.
- Quantified PCC per-user daily limits.
- I found no public numbers on the image-understanding quality of the new on-device model.
- Whether SpeechAnalyzer works on iPhones without Apple Intelligence wasn't confirmed this session. I believe it runs on iOS 26 devices broadly, but that is unverified.
- The number of languages Translation supports.

## 2. Android: Gemini Nano / ML Kit GenAI, classic ML Kit, and open models on phones

### Takeaway
Android now has a broad free on-device GenAI stack through ML Kit GenAI on AICore. It covers a general `GenerativeModel` (multimodal prompts, structured output, tool declarations), `AgentRunner`, speech recognition and translation, TTS, summarization, proofreading, rewriting, image description, and embeddings. Coverage is limited to flagship and upper-mid-range phones, with per-app quotas and a foreground-only rule. Bundling open models (Gemma 4 E2B at about 1.5GB) through Play AI packs works on more devices. It costs download size and brings variable speed.

### Cited Findings
- ML Kit GenAI APIs: direct model access via `GenerativeModel`, supporting text or typed structured output from text-only or multimodal prompts, multi-turn chat and tool declarations. Also `AgentRunner` for multi-step tool calling, speech recognition, speech translation, text-to-speech, image description, summarization, proofreading, rewriting, and text/image embeddings. — [Google ML Kit GenAI overview](https://developers.google.com/ml-kit/genai)
- The APIs run on-device with "No additional server cost incurred for each API call". AICore enforces a per-app inference quota (`ErrorCode.BUSY`) and a long-duration battery quota (`PER_APP_BATTERY_USE_QUOTA_EXCEEDED`). Inference works only when the app is the top foreground app, and background use returns `BACKGROUND_USE_BLOCKED`. — [Google ML Kit GenAI overview](https://developers.google.com/ml-kit/genai)
- Device tiers:
  - nano-v4: Pixel 11 series and Galaxy Z Flip8/Fold8.
  - nano-v3: Pixel 9 and 10, Galaxy S26, plus many Honor, OnePlus, OPPO, Sony and vivo devices.
  - nano-v2: a wider set, including Galaxy Z Fold7, Xiaomi 15/17, OnePlus 13 and Motorola Razr Ultra 2025.
  — [Google ML Kit GenAI overview](https://developers.google.com/ml-kit/genai) (as summarized by search tool)
- The Prompt API (custom Gemini Nano prompting) went alpha in October 2025. — [Android Developers Blog](https://android-developers.googleblog.com/2025/10/ml-kit-genai-prompt-api-alpha-release.html)
- GenAI Speech Recognition comes in two modes. Basic works on API 31+ (Android 12+). Advanced needs Pixel 10/11 or Gemini Nano devices on Snapdragon SM8750+, Dimensity MT6991/6993/6995, or some Exynos chips. — [ML Kit GenAI Speech Recognition](https://developers.google.com/ml-kit/genai/speech-recognition/android) (via search summary)
- Coverage share: one unsourced estimate (June 2026 blog) puts Nano-4-capable devices at about 1–3% of the active Android install base. I found no official install-base figure. — [NineTwoThree blog](https://www.ninetwothree.co/blog/gemini-nano-4-device-support)
- AICore storage: Google keeps old and new models for three days during updates, which inflates storage use (May 2026 report). — [Gadget Hacks](https://android.gadgethacks.com/news/why-is-android-aicore-using-so-much-storage-explained/)
- Open models: Google AI Edge Gallery is on Google Play and the App Store (Android 12+, iOS 17+) and is free and open source (Apache 2.0). Gemma 4 E2B is "designed for mid-range smartphones" and runs in under 1.5GB of RAM, with about a 1.5GB download. E4B targets flagships. Features include chat with thinking mode, Ask Image, Audio Scribe, and Mobile Actions via FunctionGemma 270M. — [Android Authority](https://www.androidauthority.com/gemma-4-ai-edge-gallery-3656199/); [pasqualepillitteri.it](https://pasqualepillitteri.it/en/news/795/google-ai-edge-gallery-gemma-4-offline)
- Speed (older Gemma 3n, anecdotal): E4B on a 2022 Galaxy Z Fold 4 managed about 7 tok/s decode on CPU and about 8 on GPU. A Pixel 4a was much slower. Blog claims of 60–70 tok/s look optimistic. Gemma 3 1B was 529MB, and Google guidance is at least 4GB of RAM. — [Hacker News thread](https://news.ycombinator.com/item?id=44044199); [Google Developers Blog](https://developers.googleblog.com/es/gemma-3-on-mobile-and-web-with-google-ai-edge)
- Distribution: Play for On-device AI (beta) "AI packs" can each be up to 1.5GB compressed. An app bundle's maximum cumulative size is 4GB. Packs contain models only, no code. It works with LiteRT and MediaPipe and needs AGP 8.8+. — [Android Developers: Play for On-device AI](https://developer.android.com/google/play/on-device-ai)
- A developer case study describes shipping a 584MB Gemma model through Google Play. — [ProAndroidDev](https://proandroiddev.com/shipping-a-584-mb-gemma-model-through-google-play-b4df1825c6b8)

### Inferences
- A cross-platform free app should treat platform GenAI (FM / Gemini Nano) as an enhancement. For the broadest reach, it can fall back to classic ML Kit, Vision APIs, or a bundled small model. On Android, a 1–1.5GB Gemma E2B pack reaches many more devices than Gemini Nano, but it brings a heavy first download and slower decode.
- The foreground-only rule and quotas on Android rule out background batch jobs, such as overnight photo-library tagging, on Gemini Nano.
- [background, unverified this session] Classic ML Kit (text recognition v2, barcode, document scanner, subject segmentation, on-device translation of about 50+ languages, face/pose/selfie segmentation) runs on most Android devices via Google Play services at no cost. MediaPipe LLM Inference, llama.cpp, MLC LLM and ExecuTorch are the main runtimes for bundling Llama, Qwen and Phi models.

### Gaps
- No official percentage of active Android devices with Gemini Nano or AICore.
- Battery-drain measurements for sustained on-device LLM use on phones were not found.
- Current GA vs beta status of each ML Kit GenAI API (the overview page doesn't state it).
- Input token limits for Gemini Nano via ML Kit.

## 3. Shipped apps built on these capabilities and how they've done

### Takeaway
Apple's showcase apps mostly use FM for modest add-on features (tagging, summaries, prompts) inside existing apps. I found no breakout standalone free app built purely on on-device AI with disclosed download numbers. Offline transcription apps built on SpeechAnalyzer and Whisper exist, but they still charge subscriptions even with no inference cost, which leaves room for a free competitor.

### Cited Findings
- Apple's September 2025 newsroom post highlighted SmartGym, Stoic and VLLO among FM adopters. — [Apple Newsroom](https://www.apple.com/newsroom/2025/09/apples-foundation-models-framework-unlocks-new-intelligent-app-experiences/)
- TechCrunch's list of FM adopters and their uses:
  - Lil Artist: kids' stories.
  - MoneyCoach: spending insights and auto-categorization.
  - LookUp: example sentences and etymology.
  - Tasks: tags, recurring-task detection, and offline speech-to-tasks.
  - Day One: summaries, titles, and prompts.
  - Crouton: recipe tags and step splitting.
  - Signeasy: contract summaries.
  - Dark Noise: soundscape from a text description.
  - Lights Out: F1 commentary summaries.
  - CardPointers: Q&A about the user's credit cards.
  - SmartGym: workout text to structured sets.
  - Stoic: mood-based prompts.
  - SwingVision: form feedback from racquet-sports video.
  - Zoho: summarize and translate.
  - Stuff: voice to tasks.
  - Also Daylish, Capture, Lumy, Guitar Wiz and TrainFitness.
  — [TechCrunch](https://www.techcrunch.com/2025/10/03/how-developers-are-using-apples-local-ai-models-with-ios-26/)
- Inscribe: AI Chat & Documents is an "offline-first" iOS 26+ app for transcribing and querying documents, images, audio and video. It is free with in-app purchases: $3.99/week, $9.99/month and $29.99 "Unlimited". After its benchmark, it switched its auto engine to prefer SpeechAnalyzer for supported languages and Whisper for others. A competitor's blog claims it was renamed Lyonesse in 2026, which is unverified. — [App Store listing](https://apps.apple.com/app/id6754086711); [Gigazine](https://www.gigazine.net/gsc_news/en/20260714-apple-speech-analyzer-benchmark/); [Weesper blog](https://weesperneonflow.ai/es/blog/2026-09-25-inscribe-lyonesse-vs-weesper-transcribe-2026/)
- Google AI Edge Gallery, Google's own free open-source showcase for offline Gemma 4, is now on both app stores. — [Android Authority](https://www.androidauthority.com/gemma-4-ai-edge-gallery-3656199/)

### Inferences
- The market pattern so far is that "on-device" works as a privacy feature inside paid apps. "On-device, therefore free" is still an open position.

### Gaps
- No download, rating or revenue figures were found for FM-showcase apps, Inscribe, PocketPal, Locally AI, or other offline-LLM apps. Searches for PocketPal and Locally AI returned nothing useful.
- I found no reporting of App Store review rejections specific to FM or on-device model apps.

## 4. Server-cost-heavy subscription categories and on-device quality vs cloud

### Takeaway
Big subscription businesses sit on tasks that on-device stacks now partly cover. Cal AI made $30–50M a year from calorie-from-photo, and PictureThis earned about $13M a month in 2022 from plant ID. Transcription and translation are closest to cloud parity. Photo-to-nutrition, fine-grained species ID, homework math, and open-ended chat remain clearly weaker on-device.

### Cited Findings
- Cal AI: MyFitnessPal acquired it in March 2026, saying it had over $30M in annual revenue. Cal AI projected $50M in 2026 revenue. It is subscription-priced (commonly cited at $9.99/month or $29.99/year) and was spending over $1M a month on ads by January 2026, per a third-party source. — [TechCrunch](https://techcrunch.com/2026/03/02/myfitnesspal-has-acquired-cal-ai-the-viral-calorie-app-built-by-teens/); [Forbes](https://www.forbes.com/sites/zoyahasan/2026/03/06/this-u30-kept-launching-apps-until-one-worked-then-sold-it-to-myfitnesspal/); [Superframeworks](https://superframeworks.com/case-study/cal-ai)
- PictureThis: Appfigures estimated over $13M net revenue in May 2022 (seasonal). The average in-app price is $37.66 (AppTail). I found no reliable 2025–26 figure. — [Appfigures](https://appfigures.com/resources/insights/20220610/amp?f=3); [AppTail](https://apptail.io/app/picturethis-plant-identifier-kqm/singapore)
- Transcription quality: SpeechAnalyzer roughly matches or beats Whisper Small on read speech and roughly matches mid-tier Whisper on conversational speech (see section 1). — [Gigazine](https://www.gigazine.net/gsc_news/en/20260714-apple-speech-analyzer-benchmark/); [Argmax](https://www.argmaxinc.com/blog/apple-and-argmax)
- Translation quality: Apple's is "good, not the best available". — [Blake Crosley](https://blakecrosley.com/blog/apple-translation-framework-on-device)
- LLM quality: the on-device model isn't meant for world-knowledge chat, and the PCC model falls short of GPT-4o and Qwen-3-235B, per a 2025 summary. — [InfoQ](https://www.infoq.com/news/2025/07/apple-foundation-models-ios26); [search summary](https://venturebeat.com/ai/what-we-know-about-apples-on-device-ai)

### Inferences
- Quality ranking, from closest to cloud to furthest:
  1. Transcription and OCR/document scanning: near parity.
  2. Text translation: good.
  3. Summarization, extraction, categorization and structured output: good for short inputs.
  4. Image description and food recognition: plausible but unbenchmarked.
  5. Species ID: needs a specialized classifier, not a general small LLM.
  6. Math and homework reasoning, and open-ended chat: clearly weaker than cloud.
- For calorie-from-photo, a free on-device app can identify foods and log them. Portion and calorie estimates will be rough, though cloud apps are also widely criticized for this (unsourced).

### Gaps
- Otter.ai, Photomath, Remini, Gauth, and translator-app subscription prices and revenues were not retrieved.
- I found no head-to-head benchmarks of on-device vs cloud for food recognition, plant ID or homework solving.

## 5. Constraints: device coverage, app size, review

### Takeaway
Coverage is the binding constraint. Apple Intelligence needs an A17 Pro or newer with 8GB+ RAM. About 450M capable iPhones had shipped by Q1 2026, but no reliable share of the active base exists. Android Gemini Nano coverage is a flagship minority. App size limits allow bundled models of 1–1.5GB per pack on Android.

### Cited Findings
- Apple Intelligence requires an A17 Pro or newer and at least 8GB RAM: iPhone 15 Pro/Pro Max, the iPhone 16 family and later. — [Counterpoint / search summary](https://counterpointresearch.com/en/insights/apple-has-shipped-over-450-million-apple-intelligence-capable-iphones); [techpp](https://techpp.com/2026/04/01/apple-intelligence-supported-devices/)
- Counterpoint: over 450M Apple Intelligence-capable iPhones shipped cumulatively through Q1 2026 (published June 8, 2026). It gives no installed-base percentage. — [Counterpoint Research](https://counterpointresearch.com/en/insights/apple-has-shipped-over-450-million-apple-intelligence-capable-iphones)
- iOS 27 supports every iPhone that ran iOS 26, but its AI features are limited to newer models. — [Technobezz](https://www.technobezz.com/news/apple-confirms-ios-27-for-all-iphones-running-ios-26-but-limits-ai-features-to-newer-models)
- Apple Intelligence storage: up to 14GB free for iPhone 17 Pro/Pro Max/Air and 8GB on other supported iPhones, per Apple's support doc as reported in September 2026. Reports conflict over a 12GB-RAM tier for some Siri features. — [MacObserver](https://macobserver.com/news/ios-27-apple-intelligence-requires-14gb-on-some-new-iphones-8gb-on-others); [eWeek](https://www.eweek.com/news/iphone-17-apple-intelligence-siri-ai-12gb/); [Tom's Guide](https://www.tomsguide.com/phones/iphones/your-phone-may-run-ios-27-but-only-these-devices-run-everything-siri-ai-can-do)
- Siri AI features reportedly won't launch in the EU or China at iOS 27 launch (secondary). — [DEV Community](https://dev.to/hariharanjagan/whats-new-in-apples-foundation-models-framework-at-wwdc-2026-5227)
- Android: AI packs are up to 1.5GB each, the bundle is capped at 4GB total, and packs are models only. — [Android Developers](https://developer.android.com/google/play/on-device-ai)
- Android Gemini Nano runs only in the foreground and under quotas. — [ML Kit GenAI](https://developers.google.com/ml-kit/genai)

### Inferences
- Rough Apple coverage: if the active iPhone base is about 1.4–1.5B (my assumption, unsourced), 450M+ capable units shipped means roughly 30% or less of active iPhones could use FM as of Q1 2026. It is likely higher by November 2026 after the iPhone 17 cycle, but shipped is not the same as active, and this needs a real denominator.
- Apps should be designed so the core value works through broadly available APIs (Vision OCR, Translation, SpeechAnalyzer, ML Kit), with the LLM layer as an upgrade on capable devices.

### Gaps
- Active iPhone installed base and Apple Intelligence share. I found no reliable figure.
- App Store size or review policies specific to bundling LLM weights. Apple's limits (Background Assets, the 4GB app size) weren't verified this session.
- On-device generation availability in China and the EU for third-party FM apps.

## 6. Ranked top 8 app ideas enabled by on-device capabilities

### Takeaway
The best free on-device opportunities pair a near-cloud-quality capability (speech, OCR, translation, structured extraction) with an incumbent that charges a subscription mainly to cover inference. Ideas that depend on harder reasoning or fine-grained vision rank lower.

### Cited Findings
- Incumbent pricing and evidence: Cal AI has $30–50M in revenue at about $9.99/month ([TechCrunch](https://techcrunch.com/2026/03/02/myfitnesspal-has-acquired-cal-ai-the-viral-calorie-app-built-by-teens/)). Inscribe charges up to $9.99/month even for offline transcription ([App Store](https://apps.apple.com/app/id6754086711)). PictureThis made over $13M a month in 2022 ([Appfigures](https://appfigures.com/resources/insights/20220610/amp?f=3)). The capabilities are cited in sections 1–2.

### Inferences (ranked ideas)
1. **Free offline meeting and lecture recorder with transcript, summary and action items.** On iOS this uses SpeechAnalyzer, plus FM chunked summarization with @Generable action items and Spotlight local RAG to "ask your recordings". On Android it uses ML Kit GenAI speech recognition and summarization, or a bundled Whisper or Gemma model. It undercuts subscription transcribers such as Otter-style apps (pricing not retrieved) and even "offline" apps like Inscribe that still charge $9.99/month. Speech accuracy is roughly Whisper-Small class, which makes it the most cloud-competitive capability. Coverage caveat: transcription likely works broadly on iOS 26+ (unverified), while summaries need an Apple Intelligence iPhone (15 Pro or later). On Android, Advanced speech recognition needs 2025+ flagship chips, and Gemini Nano inference is foreground-only.
2. **Free photo-to-food logger.** It uses iOS 27 FM image input with @Generable nutrition structs, plus OCRTool and BarcodeReaderTool for packaged foods. On Android it uses ML Kit `GenerativeModel` multimodal prompts and ML Kit barcode. It undercuts Cal AI ($30–50M a year at about $9.99/month, now owned by MyFitnessPal) and MyFitnessPal Premium. This is the biggest revenue pool, but quality is the risk. No benchmarks exist for the on-device model's food recognition, and portion and calorie estimation will be rough. The barcode, label-OCR and food-database path is reliable, but it needs a bundled nutrition database (for example, an offline Open Food Facts subset; licensing to be checked). Coverage caveat: image input needs iOS 27 on Apple Intelligence iPhones only, and Gemini Nano multimodal needs nano-v3/v4 flagships.
3. **Free offline conversation translator and camera translator for travel.** It uses the Apple Translation framework (iOS 18+, free, offline after language download) with SpeechAnalyzer and Vision OCR. Android uses ML Kit translation plus ML Kit GenAI speech translation. It undercuts subscription translator and "AI interpreter" apps. Coverage is the broadest of any idea, since Translation doesn't need Apple Intelligence, and quality is "good, not the best". The caveat is that the first download of each language pair needs a network connection, and the market is crowded with free Google and Apple Translate.
4. **Free scan-and-understand document assistant for contracts, bills and letters.** It covers scanning, OCR, plain-language summaries, key dates to reminders, and "what am I signing" Q&A. On iOS it uses VisionKit or RecognizeDocumentsRequest with FM and local Spotlight RAG; on Android it uses the ML Kit document scanner with GenAI summarization. It undercuts CamScanner and Adobe Scan premium tiers and AI-PDF subscription apps (Signeasy already ships FM contract summaries). The caveat is that 8K context means multi-page documents must be chunked. Summaries need AI-capable devices, while scanning works everywhere.
5. **Free private AI journal or mood coach.** FM generates prompts, summaries, weekly reflections, and HealthKit-correlated insights (sleep vs mood), with Live Activities and widgets for daily check-ins. On Android, Gemini Nano or bundled Gemma does the same. It undercuts AI-journaling subscriptions; Stoic and Day One already gate similar features. On-device is a real advantage here because people are reluctant to send journal content to servers. The task (short-text generation) fits small models well. Coverage is limited to AI-capable devices.
6. **Free receipt and expense tracker with automatic categorization.** It uses OCRTool or Vision for receipts, with FM @Generable for merchant, amount, category and splitting. ML Kit text recognition and Gemini Nano do the same on Android. MoneyCoach proves the categorization use case. It undercuts subscription budgeting and receipt apps. Extraction and classification are well within on-device quality. The caveat is that bank syncing needs servers or aggregators, so this must stay manual or scan-based.
7. **Free offline study helper.** It turns a photo of notes or a textbook page into flashcards, quizzes and plain-language explanations, using Vision OCR, FM @Generable quiz items and spaced repetition, with widgets for reviews. It undercuts Quizlet Plus-style and AI-homework subscriptions (pricing not retrieved). Generating flashcards from provided text is a strength of small models. Solving math or giving authoritative answers is a weakness, so it should be positioned around "learn from your material", not "solve my homework". The optional PCC fallback is free under 2M downloads but uses Apple's servers. Coverage is limited to AI-capable devices.
8. **Free offline general AI assistant with bundled open models.** It runs Gemma 4 E2B (about 1.5GB, under 1.5GB RAM) via LiteRT, MediaPipe or llama.cpp, delivered through Play AI packs. On iOS it uses the system FM model or MLX or Core AI with an open model. It undercuts ChatGPT, Gemini and Claude subscriptions for casual or offline use. This idea ranks last because quality falls well short of frontier models and the space is already filled with free cloud tiers and Google's own free AI Edge Gallery. Decode speeds on mid-range phones can be under 10 tok/s, and the first download is 1.5GB. It reaches many more Android devices than Gemini Nano, though.

Honorable mentions:
- **Plant, insect and mushroom ID:** a bundled Core ML or LiteRT species classifier inside the size limits, versus PictureThis's large subscription revenue. Accuracy depends on licensing a good open species model, and I found no data on that.
- **Voice-to-tasks / brain-dump organizer:** already shipped by Stuff and Tasks.
- **Workout coach from text logs:** SmartGym.
- **LiDAR room measurement:** Pro iPhones only.

### Gaps
- Incumbent pricing and revenue for transcription (Otter), homework (Photomath/Gauth), scanning (CamScanner) and journaling apps was not retrieved. The report writer should not quote figures for these.
- How users respond to "free forever" on-device apps, and whether free apps can sustain themselves through ads or tips, wasn't researched.
