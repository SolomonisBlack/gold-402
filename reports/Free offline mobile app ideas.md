# Free Offline Apps Spread Through Communities, Not Search

The free, no-backend apps a solo founder can actually get downloaded in late 2026 are mostly not the famous "hated utility" categories like phone cleaners, PDF editors and scanners. They are niche tools that spread from person to person or through tight-knit communities, and each charges a single honest one-time unlock of $5–$10. I scored 16 candidates against a discovery rubric built from the research. The top 10 are: a padel and pickleball social organizer, a hands-free crochet/knitting pattern tracker, an offline lecture-to-flashcards recorder, a period tracker that keeps all data on the phone, a one-tap baby tracker, an on-device food logger, an offline prayer-times app, an instrument tuner with practice log, a disc golf scorecard, and a free AAC (augmentative and alternative communication) board. **The five best bets are the first five.** The economics decide it. Freemium apps convert about **2%** of downloads to paid, so a $5.99 unlock earns roughly **$100 per 1,000 downloads, about ten cents per download**. A paid utility install through Apple Ads costs roughly $2–3. Meanwhile App Store submissions rose **84%** while downloads grew only **2–3%**. Only apps whose users recruit other users can win without a marketing budget. Expectations should be modest. Reaching $1,000 a month takes about 10,000 downloads a month, and only **17%** of new apps reach $1K monthly revenue within two years. The research found **no verified case** of a hobby utility reaching 100,000 downloads through a community, so treat this as a portfolio of cheap options with explicit kill criteria, not a sure thing. Some costs are unavoidable even with no servers: Apple's $99/year developer fee, Google's $25 one-time registration (both from background knowledge, not re-verified in this research), a Mac for iOS builds, OS-update maintenance, and Google Play's 12-tester, 14-day closed test.

## A free download earns about ten cents, so paid installs never pay back

The constraint is no longer building the app. It is getting it found. Sensor Tower counted **235,800 new App Store submissions in Q1 2026, up 84% year over year**, a surge that press coverage attributes to AI coding tools such as Claude Code and Codex ([The Next Web](https://thenextweb.com/news/vibe-coding-apple-app-store-surge-crackdown)). H1 2026 is estimated at about 560,000 new apps, and some outlets project more than a million for the year ([pbxscience](https://pbxscience.com/app-store-new-app-submissions-may-surpass-one-million-this-year-as-ai-fuels-a-wave-of-junk-apps/)). Downloads, however, grew only **about 3% in 2025 and about 2% so far in 2026** ([TweakTown](https://www.tweaktown.com/news/112818/vibe-coding-is-flooding-the-app-store-with-new-apps-on-track-for-record-submissions-in-2026/index.html)). Apps launched before 2020 still earn **69% of subscription revenue** ([RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps-2026/)). An AI-built app is cheap for everyone to make, so code is not a moat. Distribution is.

Monetization benchmarks set the ceiling. RevenueCat's 2026 data across 115,000+ apps shows freemium converting **2%** of users to paid, against **11%** for hard paywalls. First-two-week revenue per install is **$0.27** for freemium and **$2.32** for hard paywalls ([PPC Land summary of RevenueCat](https://ppc.land/the-app-middle-class-is-dying-and-revenuecats-data-shows-exactly-how-fast/)). The median app earns little. One year after launch, average monthly revenue is about **$72**, the middle half of apps earn $16–$429 a month, and only **17%** of new apps reach $1K a month within two years ([PPC Land](https://ppc.land/the-app-middle-class-is-dying-and-revenuecats-data-shows-exactly-how-fast/)).

With no backend, a one-time unlock is the natural model. StoreKit 2 verifies purchases on the device in about 90 lines of code with no server ([dev.to](https://dev.to/snake_sun/why-i-picked-one-time-iap-over-subscription-for-4-indie-ios-apps-storekit-2-2026-data-1nk6)). One-time pricing also fits only because inference is free. A one-time license fails when every use costs money, as with cloud LLM calls ([RevenueCat 2026 benchmarks](https://www.revenuecat.com/blog/growth/subscription-app-trends-benchmarks-2026.md)). The table below shows revenue per 1,000 downloads at 2% conversion, after a 15% store commission. The 15% Small Business Program rate is background knowledge; at the standard 30%, a $2.99 sale nets $2.09 ([dev.to](https://dev.to/snake_sun/why-i-picked-one-time-iap-over-subscription-for-4-indie-ios-apps-storekit-2-2026-data-1nk6)).

| One-time price | Net per 1,000 downloads at 2% | Downloads per month needed for $1K/month |
|---|---|---|
| $2.99 | ~$51 | ~19,700 |
| $4.99 | ~$85 | ~11,800 |
| $5.99 | ~$102 | ~9,800 |
| $7.99 | ~$136 | ~7,400 |
| $9.99 | ~$170 | ~5,900 |

These figures assume freemium-style 2% conversion, which is optimistic. One freemium game converted only **0.67%** against a 2% goal ([Wikipedia: Gasketball](https://en.wikipedia.org/wiki/Gasketball)). The economics rule out paid acquisition. Utilities cost **$0.94–$1.23 per tap** in Apple Ads ([RocketShip HQ](https://www.rocketshiphq.com/?p=5321); [AppTweak](https://www.apptweak.com/en/aso-blog/apple-ads-benchmarks)). With a typical 40–60% tap-to-install rate (background knowledge), that comes to about **$2–3 per install**, against roughly $0.05–$0.17 earned per download. That is a 10–30x loss on every paid install, so Apple Ads can only be used to test keywords.

Ads do little better. Global AdMob banner eCPMs run **$0.20–$0.80**, utilities sit in the low-to-mid range, and low session counts limit impressions ([Playwire](https://www.playwire.com/blog/admob-ecpm-benchmarks-what-publishers-should-expect); [MonetizeMore](https://www.monetizemore.com/blog/how-much-ad-revenue-can-apps-generate/)). Ad SDKs also break the "no tracking" promise that is the main selling point for most of these apps. No benchmark exists for tip jars, which is a research gap. Tips belong only where charging would undermine the mission.

The evidence on free discovery is thin, so this report states its confidence plainly. The documented zero-ad-spend growth stories are subscription or AI apps with self-reported numbers, such as GlowUp's claimed 2M users through TikTok ([Stealwhatworks](https://stealwhatworks.com/blogs/news/apps-over-10k-month-through-tiktok)). Their shared trait is a visual hook that works in short-form video. Reddit works better as a launch channel than as paid acquisition. One price-tracking app got **1,000 downloads in its first week** from an r/androidapps post ([Indie Hustle](https://indiehustle.beehiiv.com/p/hitting-80-000-downloads-for-his-price-tracking-app)), while one indie developer's Reddit ads produced 17,000 impressions and about **4 installs** ([Matt Corey](https://mattcorey.substack.com/p/rethinking-my-indie-app-advertising)). A vendor claims DIY organic growth usually yields 100–1,000 downloads in 3–6 months ([Indie App Santa](https://indieappsanta.com/2025/11/21/10349/)). That source sells paid promotion, but the figure is a useful pessimistic baseline.

**Platform policy shapes what is safe to ship.** In 2025 Apple rejected **371,000+ submissions for copying, spam or misleading users** and **443,000 for privacy violations**, and terminated **193,000 developer accounts** ([Apple Newsroom](https://www.apple.com/cm/newsroom/2026/05/the-app-store-stopped-over-2-point-2-billion-usd-in-fraudulent-transactions-in-2025/)). Guideline 4.3(a) rejections cite "multiple similar apps using a repackaged app template" ([Apple Developer Forums](https://developer.apple.com/forums/thread/822686)). WWDC 2026 reportedly added a stricter clone and spam cleanup policy; that source is a search summary and was not fetched ([iDrop News](https://www.idropnews.com/news/app-store-subscription-suites-spam-rules/265140)). Since October 2026, Guideline 2.5.19 bans hidden or undocumented features ([9to5Mac](https://9to5mac.com/2026/10/16/apples-new-app-store-rules-crack-down-on-ai-nudification-and-bait-and-switch-apps/)). In April 2026 Apple pulled Cal AI over a deceptive paywall ([TechCrunch](https://techcrunch.com/2026/04/21/apples-cal-ai-crackdown-signals-its-still-policing-the-app-store/)). A single, distinct app with a clearly priced one-time unlock sits on the safe side of every one of these rules. A factory of lookalike apps does not.

On Android, new personal accounts must run a **closed test with 12 testers for 14 days** before production ([Google Play Console Help](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en-GB)). Developer verification starts enforcement in select countries from Sept 30, 2026 and goes global in 2027 ([Android Authority](https://www.androidauthority.com/android-sideloading-changes-timeline-3679204/)).

**The remaining unavoidable costs are small.** None of them are servers:

| Cost | Amount | Status |
|---|---|---|
| Apple Developer Program | $99/year | Background knowledge, not re-verified |
| Google Play registration | $25 one-time | Background knowledge, not re-verified |
| Mac for iOS builds | Hardware you may already own | Background knowledge |
| Privacy-policy page (required by both stores) | Free if static | Background knowledge |
| Store commission on each sale | 15% small business / 30% standard | 15% is background; 30% example cited above |
| OS-update maintenance | Time, permanently, even after one-time sales | [note.com](https://note.com/yss_dev/n/n5b747b0e885e?hl=en) |
| Play's 12-tester recruitment | Time | Cited above |

## Ten ideas scored on a 22-point discovery rubric

Each candidate is scored 0–2 on ten criteria, eight of them taken from the discovery research plus two feasibility checks.

| Code | Criterion | What a 2 means |
|---|---|---|
| D (×2) | Demand and an open position | Large proven demand and incumbents who leave a clear opening |
| H | Short-video hook | Value visible in a ten-second clip |
| X | Exposure loop | Normal use puts the app in front of non-users (shared image, QR code, bracket) |
| R | Repeat use | Daily or weekly |
| M | Monetization survives ~2% conversion | Proven willingness to pay and an obvious pro feature |
| O | Organic channel | Wins without paid installs |
| P | Low policy risk | Low 4.3 clone risk, low 4.2 risk and low privacy risk |
| C | Reachable community or seasonal spike | A named community and a calendar spike |
| F | No-backend feasibility on mainstream phones | The core works on all phones, not only AI-tier devices |
| K | Not killed by OS built-ins | Neither iOS nor Android ships the feature |

Demand is double-weighted because audience size caps downloads, which gives a maximum of 22. Ties are broken by monetization, then feasibility, then audience size. The scores are my judgments from the notes' evidence, not measured data. No keyword-volume data was obtained for any category.

| # | App idea | D×2 | H | X | R | M | O | P | C | F | K | **Total** | Best model | Key audience / incumbent signal |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Padel + pickleball social organizer and scorer | 4 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | **20** | Free + $5.99 one-time | 19.4M–40M padel players; 24.3M US pickleball players (+22.8%) |
| 2 | Hands-free crochet/knit PDF pattern tracker | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | **17** | Free + $4.99 one-time | r/crochet ~2.0M, r/knitting ~626k |
| 3 | Offline lecture recorder → summary → flashcards | 4 | 2 | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | **17** | Free + $4.99 one-time | "Offline" rival Inscribe still charges $9.99/mo |
| 4 | Period tracker with all data kept on the phone | 4 | 1 | 0 | 2 | 2 | 1 | 1 | 1 | 2 | 1 | **15** | Free core + $7.99 one-time | Flo 81M MAU; 84% of reviewed apps share data |
| 5 | One-tap baby tracker | 2 | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | **15** | Free + $9.99 one-time | Huckleberry $9.99–$14.99/mo |
| 6 | On-device photo/barcode food logger | 4 | 2 | 1 | 2 | 2 | 1 | 0 | 1 | 0 | 2 | **15** | Free + $9.99 one-time | Cal AI $30M+ annual revenue |
| 7 | Offline prayer times + Qibla, no tracking | 2 | 0 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | **15** | Free + $2.99 widgets + tip jar | Muslim Pro data-selling scandal |
| 8 | Chromatic tuner + metronome + practice log | 2 | 1 | 0 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | **14** | Free tuner + $3.99 practice pack | Tuners charging $5.99/week |
| 9 | Disc golf scorecard you own | 0 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | **14** | Free + $4.99 stats | UDisc 2M+ users, Pro $29.99/yr backlash |
| 10 | Free AAC core-word communication board | 2 | 1 | 1 | 2 | 0 | 2 | 1 | 1 | 2 | 2 | **14** | Free + tip jar | Proloquo2Go $249.99; no free full-featured app found |

Evidence for each row, beyond the top five covered in the next section:

- **#1 and #9:** [SFIA](https://sfia.org/research/u-s-pickleball-participation/); [Padel Addict](https://www.padeladdict.com/en/padel-is-experiencing-unstoppable-growth-more-than-58000-courts-worldwide-and-19-4-million-players/); [UDisc Growth Report 2026](https://udisc.com/disc-golf-growth-report/2026).
- **#6:** [TechCrunch](https://techcrunch.com/2026/03/02/myfitnesspal-has-acquired-cal-ai-the-viral-calorie-app-built-by-teens/).
- **#7:** [Vice](https://www.vice.com/en/article/muslim-app-location-data-salaat-first/).
- **#8:** [justuseapp](https://justuseapp.com/en/app/1545753207/guitar-tuner-chords-tabs/reviews).
- **#10:** [AppPricingLab](https://apppricinglab.com/app/apple/308368164).

Three things stand out in the scoring.

**Exposure loops decide the top of the table.** The padel organizer wins because every social night it runs shows standings to 8–16 players, not because it has the biggest market.

**On-device AI is better as an upgrade than as the core.** The food logger has the biggest money pool and the best hook. But its core feature, photo-to-nutrition, needs iOS 27 on an Apple Intelligence iPhone or a recent Gemini Nano flagship, and no benchmark shows on-device food recognition is accurate. So it scores zero on feasibility and on policy risk. The lecture app ranks higher because its core, transcription, works broadly, and only its AI layer is limited to high-end devices.

**The rubric deliberately ranks some apps below the size of their market.** Disc golf scores well on community but zero on demand, because UDisc's free tier already offers unlimited scoring. The prayer-times app has the strongest daily-use pattern but no visual hook. AAC is the most important app socially, but it should not be monetized beyond tips.

## Five best bets: build scope, revenue math and kill criteria

### 1. A padel and pickleball organizer turns every social night into an ad

**The audience is large and growing fast.** Padel had **19.4M players and 58,334 courts at end of 2025**, with courts up **16%** year on year ([Padel Addict](https://www.padeladdict.com/en/padel-is-experiencing-unstoppable-growth-more-than-58000-courts-worldwide-and-19-4-million-players/)). The FIP counts 40M players under a broader definition, with registered players up **30.5%** ([SGI Europe](https://www.sgieurope.com/trends/padel-is-in-constant-growth-around-the-world-says-latest-fip-report/118582.article)). US pickleball reached **24.3M players in 2025, up 22.8%** and up 479% over five years ([SFIA](https://sfia.org/research/u-s-pickleball-participation/)).

**The incumbents' pain is fragmentation and paywalled history.** Rally keeps only the **last 5 games** free and puts history behind "Pickleball Plus". PickleLogic charges **$6.99** and PickleballTrkr **$5.99** up front, and the field is full of 2023–2026 indie scorers with too few ratings to display ([Rally](https://apps.apple.com/app/id6780994931); [Pickleball Score Tracker](https://apps.apple.com/us/app/id6449199491?l=en-us)). Padel-specific tools looked thinner still; multi-sport scorers cover padel only generically ([App Store](https://apps.apple.com/app/id1254911810)).

**The free version wins because the customer is the organizer and the players are the audience.** The gap no solo scorer fills is the social event. That means Americano and Mexicano round-robins for padel, which rotate partners and compute standings, and open-play paddle-stack queues for pickleball courts.

**The v1 scope needs no AI and runs on every device.** It includes:
- Correct scoring engines: padel golden point/advantage and tie-breaks; pickleball side-out, rally and modified rally.
- A rotation generator for 4–32 players with court assignment.
- A standings image to share.
- QR-code handoff of an event between phones, with no server.
- On-device voice score call-outs.
- Apple Watch and Wear OS scoring.
- Localized listings in Spanish, Italian, French, Swedish and Portuguese.

**Ship both sports in one app.** Two near-identical template apps invite a 4.3(a) rejection.

**Monetization: a $5.99 one-time "Organizer Pro" unlock.** It covers unlimited saved events and seasons, player stats and ratings, watch scoring and custom formats. Unlimited score history stays free, which answers Rally's limit directly. At 2% this yields about **$102 per 1,000 downloads**. Organizers probably convert above the average, but that is unmeasured.

**Download channels:**
- Club organizers and coaches.
- WhatsApp and Facebook groups.
- r/Pickleball, with about **139k** members ([GummySearch](https://gummysearch.com/r/Pickleball)).
- Court bulletin boards.
- The standings image itself, posted to group chats after every session.

**A club also solves Play's 12-tester requirement in a single evening.**

**Risks:**
- The pickleball scorer market is crowded.
- Booking platforms could add organizer features. This is my inference, not something the notes show.
- Outdoor pickleball is seasonal in the northern hemisphere, though padel is played indoors year-round in Europe.

**Kill criterion:** stop after 90 days if fewer than half of 10 seeded organizers run a third event, or if the app has fewer than 1,000 downloads.

**Confidence:** high on the audience, low on download forecasts.

### 2. A hands-free pattern tracker serves 2.6 million engaged crafters

**The audience is big, engaged and easy to reach.** r/crochet has about **2.0M** members and r/knitting about **626k** ([GummySearch r/crochet](https://gummysearch.com/r/crochet); [r/knitting](https://gummysearch.com/r/knitting)).

**The incumbents are dated or monetize aggressively.** Simple row counters are saturated, and the pain is monetization. Stitch Keeper's maker built it because they were "fed up with row counter apps full of ads and subscriptions" and sells it for a one-time **$4.99** ([Product Hunt](https://www.producthunt.com/products/stitch-keeper)). At least one major counter uses monthly and yearly subscriptions ([App Store](https://apps.apple.com/app/id6478523765)). The real gap is a pattern tracker rather than a counter. Ravelry has **no official app** ([Ravelry](https://www.ravelry.com/about/apps)). The long-standing tracker knitCompanion is older ([knitCompanion](https://apps.apple.com/app/id1058142783)). Ravelry's 2020 redesign left some users unable to use the site, which created a segment that cares about accessibility ([CraftGossip](https://knitting.craftgossip.com/classic-ravelry-is-gone-now-what/2021/04/02)).

**There is a realistic benchmark.** StitchTally, released in November 2024, has reached about **16K installs** by a third-party estimate ([AppGoblin](https://www.appgoblin.info/apps/6738016114)). That is roughly what a decent indie entry achieves here.

**The v1 scope needs no AI, so the core works on every device.** It includes:
- Import of the user's own PDF patterns.
- A row-highlighter bar that moves with the counter.
- Multiple linked counters (row, repeat, increase).
- Hands-free increments by voice ("next row", "undo"), headphone button or Watch.
- Full VoiceOver support.
- A photo project log and yarn stash.

**On-device tech:** voice commands use Apple's on-device speech stack (SpeechAnalyzer, iOS 26+) and ML Kit's basic GenAI speech recognition on Android 12+ ([Gigazine](https://www.gigazine.net/gsc_news/en/20260714-apple-speech-analyzer-benchmark/); [ML Kit](https://developers.google.com/ml-kit/genai/speech-recognition/android)). On Apple Intelligence iPhones, the Foundation Models framework could optionally explain abbreviations like "sc2tog".

**Monetization: free for two active projects, with a $4.99 one-time unlock.** The unlock covers unlimited projects, Watch and voice. That is about **$85 per 1,000 downloads**.

**Download channels:**
- r/crochet and r/knitting launch posts.
- The curated Ravelry apps directory.
- Pattern-designer partnerships.
- Short videos of hands-free counting mid-stitch, which is a strong visual hook.

Winter holiday gift-making is a likely seasonal peak, but no Google Trends data confirmed it.

**Risks:**
- Saturation, which gives this pick only a 1 on policy risk.
- Copyright. Only ever open user-imported files, and never add pattern sharing.

**Kill criterion:** stop if there are fewer than 1,000 downloads 60 days after both subreddit posts, a Ravelry listing and ten short videos, or if conversion is below 1% after 3,000 downloads.

**Confidence:** moderate.

### 3. A free lecture recorder undercuts $9.99-a-month "offline" transcribers

**On-device speech recognition now matches cloud quality, yet apps still charge subscriptions for it.** Apple's SpeechAnalyzer scored a **2.12% word error rate** on LibriSpeech test-clean, against **3.74% for Whisper Small**, and ran about 3x faster ([Gigazine](https://www.gigazine.net/gsc_news/en/20260714-apple-speech-analyzer-benchmark/)). On long conversational audio it matches mid-tier Whisper at twice the speed ([Argmax](https://www.argmaxinc.com/blog/apple-and-argmax)). Even so, the "offline-first" Inscribe charges **$3.99/week, $9.99/month or $29.99 for unlimited** ([App Store](https://apps.apple.com/app/id6754086711)). The market treats on-device processing as a privacy feature inside paid apps. "On-device, therefore free" is still an open position.

**Recording alone is not enough of a wedge.** Voice Memos and Pixel Recorder already cover recording. My background knowledge, not verified this session, is that Apple's Notes app now transcribes too. So the wedge is the study loop: lecture to summary to flashcards to spaced review.

**On-device tech:** iOS 27's Foundation Models framework provides an **8,192-token context**, guided generation with @Generable for structured flashcards, and Spotlight-backed fully local RAG for "ask your lectures" ([WWDC26 session 241](https://developer.apple.com/videos/play/wwdc2026/241/)). An hour-long transcript has to be summarized in chunks.

**Device coverage is the main caveat.**
- On iOS, summaries and flashcards need an Apple Intelligence iPhone: A17 Pro or newer with 8GB RAM, which means iPhone 15 Pro or later ([techpp](https://techpp.com/2026/04/01/apple-intelligence-supported-devices/)). About **450M** such iPhones had shipped by Q1 2026 ([Counterpoint](https://counterpointresearch.com/en/insights/apple-has-shipped-over-450-million-apple-intelligence-capable-iphones)). The notes estimate that is roughly 30% or less of active iPhones, from an unsourced denominator.
- On Android, Gemini Nano runs only on flagship tiers, only in the foreground and under per-app quotas ([ML Kit GenAI](https://developers.google.com/ml-kit/genai)). One unsourced estimate puts the newest Nano tier at 1–3% of devices ([NineTwoThree](https://www.ninetwothree.co/blog/gemini-nano-4-device-support)).
- The Android alternative is to bundle Gemma 4 E2B, a download of about 1.5GB ([Android Authority](https://www.androidauthority.com/gemma-4-ai-edge-gallery-3656199/)).
- Apple's free Private Cloud Compute tier, offered to small-business apps under 2M downloads, could back non-AI devices at zero cost. It runs on Apple's servers, though, which breaks a strict "everything on-device" claim ([WWDC26 session 241](https://developer.apple.com/videos/play/wwdc2026/241/)).

**The v1 scope is iOS-first.** It covers background recording, transcription, search, and AI summaries and flashcards on capable devices, with a review widget and CSV/Markdown export for Anki. Android follows later with transcription first.

**Monetization: recording, transcripts and summaries stay free; a $4.99 one-time Pro unlock adds the study tools.** Pro covers flashcards with spaced repetition, export, multi-course organization and local Q&A. That is about **$85 per 1,000 downloads**.

**Download channels:**
- Short video showing a lecture turning into flashcards in ten seconds.
- Student communities (subreddit sizes were not collected).
- The August–September and January semester starts. These spikes are an inference, not measured.

**Risks:**
- One-star reviews from users on unsupported phones. State the device requirement plainly; quietly hiding features by device also sits badly with 2.5.19's rules.
- AI summary errors.
- Recording-consent rules at some universities and in some jurisdictions (background knowledge).

**Kill criterion:** move the app to maintenance mode if the August–September 2027 back-to-school push yields fewer than 5,000 downloads, or if the rating falls below 4.3.

**Confidence:** moderate on the technology, low on demand, since no keyword or Otter pricing data was retrieved.

### 4. A period tracker that never phones home answers an 84% data-sharing problem

**The demand is huge, and the incumbents' pain is privacy rather than price.** Flo has **81M monthly active users** ([The Star / Mozilla](https://www.the-star.co.ke/news/world/2026-07-19-how-period-trackers-share-your-private-details)) and a 2021 FTC settlement over sharing data with marketers ([Pharmacy Times](https://pharmacytimes.com/view/post-roe-how-safe-are-period-tracking-smartphone-apps-)). ORCHA found **84% of 25 women's health apps share data with third parties**, and **only one** kept all sensitive data on the device ([ORCHA](https://us.orchahealth.com/84-of-25-womens-health-period-tracker-apps-share-data-with-third-parties/)). Mozilla's top-rated app, Euki, earned that rating precisely because it stores data locally. The press rewards exactly this architecture, and privacy research recurs: Privacy International in 2025 and Mozilla in July 2026 ([Privacy International](https://privacyinternational.org/sites/default/files/2025-05/Period%20tracking%20apps%20research%2020245%20for%206%20May.pdf)).

**The free version wins because having no backend is the product.** Cycle prediction is simple math, so no AI is needed, and the app works on every device. Apple Health's cycle tracking is a partial built-in on iOS (background knowledge). Android has no strong local-only default, so Android deserves equal launch weight.

**The v1 scope:**
- Logging, predictions, reminders and symptoms.
- A home-screen widget.
- An app lock.
- A user-controlled encrypted export and backup file, because losing a phone must not mean losing years of data.
- No analytics or ad SDKs, so the iOS "Data Not Collected" label is truthful.

**Monetization: free forever for everything privacy-related, with a $7.99 one-time unlock for extras.** The unlock covers insights and charts, a PDF report for the doctor, Watch support and themes. Never paywall the lock or the export. That yields about **$136 per 1,000 downloads**. Ads are ruled out because they contradict the pitch.

**Download channels:**
- Privacy press cycles: Mozilla Privacy Not Included, ORCHA, Privacy International.
- r/privacy and "No Tracking" app directories ([AlternativeTo](https://alternativeto.net/feature/no-tracking/?p=5)).
- Short video explaining where period data goes.

**Risks:**
- A high trust bar.
- Apple's privacy enforcement, with 443K rejections in 2025.
- Never market predictions as contraception. Regulatory exposure there is background knowledge.
- "No tracking" claims are everywhere and have no proven effect on outcomes on their own.
- The honest competitors, Euki and Drip, are free FOSS apps, so the edge has to come from polish and design.

**Kill criterion:** stop if the rating falls below 4.5 or the app has fewer than 3,000 downloads after six months.

**Confidence:** high on demand and pain, moderate on whether a newcomer can break through.

### 5. A one-tap baby log counters $14.99-a-month Huckleberry

**The incumbent charges premium subscription prices.** Huckleberry Plus costs **$9.99/month** and Premium **$14.99/month**, behind a soft paywall with a trial ([Adapty](https://adapty.io/paywall-library/huckleberry/)). Across baby trackers the top complaint is that "the best features sit behind a subscription". One parent said logging "got to be a chore so we stopped" ([Unstar](https://unstar.app/blog/huckleberry-baby-tracker-sprout-glow-baby-daybook-baby-tracker-apps-ranked-2026); [Reddit snapshot](https://reddit.sentinel-team.org/posts/1qr7kw2/snapshots/2026-01-31T00%3A11%3A22.226577Z)).

**The free version wins on speed and privacy at 3am.** That means no account, one-tap logging, and a one-time price that is less than a single month of Premium.

**The v1 scope covers several logs and quick-access surfaces:**
- Feed timers for left/right, bottle, diaper, sleep and pumping logs.
- Lock-screen timers, widgets and a Watch app.
- Optional voice logging ("4-ounce bottle at 3:10") through Foundation Models on Apple Intelligence iPhones only.

**Two-parent sync is the hard part.** On iOS, CloudKit shared zones are Apple-hosted and cost the developer nothing within quotas (background knowledge). Couples who use different platforms need file or local-network handoff.

**Monetization: free logging forever, with a $9.99 one-time unlock.** The unlock covers charts, pediatrician PDF reports and caregiver sharing, for about **$170 per 1,000 downloads**. One-time pricing suits a product used intensively for about a year.

**Download channels:**
- Parenting groups and registry checklists.
- Word of mouth.
- Cross-promotion from the period tracker's pregnancy mode.

**Risks:**
- A growing crowd of free challengers (Sofi, Pipkin, SleepSpot) ([Pipkin](https://www.producthunt.com/p/pipkin)).
- Constant churn as babies age out. This is my inference.
- Sync complexity across platforms.

**Kill criterion:** stop if the app has fewer than 2,000 downloads in four months, or if fewer than half of new users are still logging on day three.

**Confidence:** moderate. The category is proven, but the field is getting crowded.

## The biggest money pools are the worst places to launch free

The ideas that just missed the top 10, or were rejected, show why sheer category revenue misleads. **The iOS photo and storage cleaner (13/22) is the first alternate.** It is the largest on-device-capable pool. Consumers spent nearly **$40M** on cleaners in one month ([Appfigures](https://appfigures.com/resources/this-week-in-apps/20250606)), and Cleanup is estimated at **$14M/month**, #1 in iOS Utilities as of November 2026 ([GetAppNiche](https://getappniche.com/top-grossing-ios-apps/utilities)). But about **1,500** cleaners compete, the leaders grow by buying Apple Ads on thousands of keywords, the category is a prime target for Apple's clone cleanup, more than 95% of its revenue is on iOS only, and Appfigures itself calls cleanup "a feature Apple can easily sherlock" ([Appfigures](https://appfigures.com/resources/this-week-in-apps/20250606)). A founder who wants one high-variance bet should build it as a swipe-triage cleaner with on-device video compression and a "freed 9GB" share card, and accept that organic search will be brutal.

**Two more categories have the same demand-without-discovery problem.**
- **Scanner plus PDF toolkit (13/22).** Incumbents genuinely hate their users, with $9.99 weekly plans and trial traps ([PDF Editor listing](https://apps.apple.com/us/app/pdf-editor/id6596751792)). But the category is won through paid search and has no exposure loop, and the Notes, Files, Drive and Preview built-ins cover the basics.
- **Universal TV remote.** It has an estimated **$2M/month** leader, but it fragments across TV protocols and no complaint evidence was gathered.

**Other categories fail on a specific weakness:**

| Rejected idea | Why it was rejected |
|---|---|
| Vehicle fuel and maintenance log (13/22) | Sound but hook-less |
| On-device plant ID | Faces free Visual Look Up and Seek, and its accuracy would lag cloud leaders |
| White-noise apps | Partly replaced by iOS Background Sounds ([iDrop News](https://www.idropnews.com/apps/popular-iphone-app-alternatives-2026/246739/9/)) |
| Private AI journal | Gated to AI-tier devices, and Apple Journal partly covers it |
| Offline general-purpose chatbot | Small models lag frontier quality, need a 1.5GB download, and Google's free AI Edge Gallery already exists |
| MTG life counters | Strong free incumbents, plus IP risk from card art ([Lifetap](https://apps.apple.com/us/app/id1508241754)) |
| Board-game scorekeepers | Indie entrants show trivial traction, about 200 installs in one case ([AppGoblin](https://appgoblin.info/apps/com.martiferret.scoreboard)) |
| Clones of existing games | Excluded outright as an IP risk |

**OS built-ins kill a set of utilities outright, unless a founder finds a sharp wedge:** QR scanners (Which? tells users to use the camera instead) ([Which?](https://www.which.co.uk/news/article/qr-codes-are-still-being-hijacked-to-set-subscription-traps-and-scams-alyxt1h5FrBD)), standalone translators, flashlights, compasses, levels, calculators, voice recorders, file managers and 2FA authenticators.

## Launch order: crafts in winter, courts in spring, campuses in August

The launch sequence should follow seasons and the time needed to get a signal, not the ranking.

| When | App | Why this timing |
|---|---|---|
| December 2026 | Crochet/knit pattern tracker | Smallest build with no AI, matches the likely winter crafting peak, and tests the one-time-unlock thesis with a community that is ready for launch posts |
| February–March 2027 | Padel + pickleball organizer | Recruit Play's 12 testers from one club in December, then launch before the northern spring season |
| Spring 2027 soft launch, August–September 2027 main push | Lecture-to-flashcards (iOS-first) | Buys a semester to fix summary quality before the biggest student spike |
| Q2 2027 | Period tracker | Android weighted equally with iOS; time the launch to a privacy-report news cycle |
| Q3 2027 | Baby tracker | A pregnancy mode in the period tracker hands users straight to it |

Two portfolio rules matter as much as the order. First, **use one brand promise everywhere**: free core, works offline, no account, one fair price. Each app gets an offline "more apps" screen, which makes cross-promotion free. Second, **make every app genuinely distinct in concept, metadata and assets**. Shared internal libraries are fine, but Apple's 4.3(a) language targets repackaged templates, and an account termination would take down the whole portfolio at once.

## Conclusion

Free AI-built apps have reversed the old indie equation. Building is close to free for everyone, so the scarce asset is a user who brings the next user. That favors apps used in a group, such as an organizer, a shared scorecard or a caregiver log, over apps used alone, however large their category's revenue. The second shift is that on-device AI works best as the paid tier, not the core. iOS 27 and Gemini Nano make "on-device, therefore free" newly credible, but coverage still excludes most phones, so the core should run on classic APIs and the AI layer should be what justifies the unlock. Third, Apple's 2026 crackdown on deceptive paywalls and clones turns an honest one-time price into a competitive advantage rather than a sacrifice.

The prudent reading of the evidence is to treat each app as a cheap option. Each has a defined launch channel and a kill date, because the research shows the median outcome is tens of dollars a month. The upside comes from the one or two apps whose communities adopt them.
