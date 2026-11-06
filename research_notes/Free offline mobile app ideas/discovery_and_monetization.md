# Discovery, Monetization and Platform Risk for Free, No-Backend iOS/Android Apps (as of Nov 2026)

Research scope note: ~21 tool calls. Many results in this space come from vendor/agency blogs with a commercial interest (ASO tools, tester-recruitment services, ad-mediation vendors); these are flagged. Items marked **[background, not verified this session]** are from the researcher's prior knowledge and should be checked before being stated as fact in the final report.

## 1. Discovery: how indie apps get downloads in 2025–2026

### Takeaway
Hard data on organic indie discovery is thin and mostly self-reported. The best-documented growth engine for small consumer apps in 2025–2026 is short-form video (TikTok/Reels, often multi-account or "faceless"), but the documented wins are almost all subscription apps, not free utilities. Apple Search Ads for Utilities are relatively cheap per tap (~$0.94–$1.23 US), which makes paid search a viable top-up only if each install earns more than a few dollars, which free/ad-supported utilities usually don't.

### Cited Findings
**Apple Search Ads (Apple Ads) costs**
- AppTweak 2026 benchmarks: Utilities cost per tap (CPT) is about **$1.23 in the US**, below the overall US median of **$1.91**. The global search-results median CPT is about **$0.92**. — [AppTweak Apple Ads benchmarks 2026](https://www.apptweak.com/en/aso-blog/apple-ads-benchmarks)
- RocketShip HQ (2026): "Utilities & Productivity" median CPT is **$0.94**, up 6% YoY, with an interquartile range of about **$0.48–$1.56**. — [RocketShip HQ](https://www.rocketshiphq.com/?p=5321)
- MobileAction: Utilities CPT was **$1.07 in 2024**, down from **$1.45 in 2023** (older data). — [MobileAction 2025 benchmark report – CPT](https://www.mobileaction.co/report/apple-search-ads-2025-benchmark-report/cost-per-tap/)
- SplitMetrics: the 2025 US Utilities tap-through rate is **11.3%**, and the average CPT across the top 15 categories is **$2.25** (2025). — [SplitMetrics Apple Ads cost](https://splitmetrics.com/blog/apple-search-ads-cost)

**Short-form video / TikTok (mostly self-reported founder interviews)**
- GlowUp: the founder told Starter Story the app reached about **2M users** and about **$800K in its first year** with **zero ad spend**, growing through TikTok. It was earning about $15K/month at the time of the interview. This is a secondary write-up of a self-reported interview. — [Stealwhatworks summary](https://stealwhatworks.com/blogs/news/apps-over-10k-month-through-tiktok)
- Vix (an AI manifestation app built by a non-coder) reached about **$30K/month** net subscription revenue within a year, using a **multi-account TikTok** strategy (self-reported). — [Stealwhatworks summary](https://stealwhatworks.com/blogs/news/apps-over-10k-month-through-tiktok)
- "Early": an app launched in late 2025 reportedly reached **$50K/month within 4 months** (self-reported, Starter Story). — [BigGo / Starter Story summary](https://finance.biggo.com/podcast/fbb0f4aa8eac0d9b); [Stealwhatworks](https://stealwhatworks.com/blogs/news/apps-over-10k-month-through-tiktok)
- Cal.ai is claimed to have reached **$1.5M MRR in 34 days** using only faceless TikTok explainer videos. This comes from a vendor blog, the source itself calls it exceptional, and it is unverified. — [ReelCarousel](https://www.reelcarousel.app/blog/faceless-tiktok-accounts-promoting-apps)
- Faceless app-promotion TikTok accounts are often run by affiliate or user-acquisition marketers paid per install or subscription, not by the developer. — [ReelCarousel](https://www.reelcarousel.app/blog/faceless-tiktok-accounts-promoting-apps)
- Lightreel (Aug 2026): the strongest consumer-app TikTok campaigns delayed the product reveal, and persistent creator personas outperformed one-off endorsements. — [Lightreel weekly report](https://www.lightreel.ai/blogs/consumer-apps-on-tiktok)
- For indie games, organic content from players and creators drove more views than studio posts, and paid TikTok is "a bad investment" for most indie games. — [PressKit field guide](https://presskit.gg/field-guides/tiktok-indie-game-marketing)
- A viral X claim of a solo founder at "$2M MRR in 10 months" with a Bible-scrolling app is an **unsourced social post**. Treat it with caution. — [X post](https://x.com/jacobrodri_/status/2115060267545731513)

**Reddit**
- An indie developer (Bills to Budget) testing Reddit ads saw **17,000+ impressions on day one** but only about **4 installs** attributed. The developer believed the ads boosted some App Store keyword rankings. — [Matt Corey Substack](https://mattcorey.substack.com/p/rethinking-my-indie-app-advertising)

**ASO case studies**
- No verified 2025–2026 indie case study of "100k organic downloads" turned up. A YouTube video titled "100K Downloads TWICE & $4K Revenue in 2 Months" (Sept 2025) exists, but its organic/paid split was not confirmed. — [YouTube](https://www.youtube.com/watch?v=Po44HS490Ik)
- An ASO-vendor case study shows an indie hyper-casual game at about **200 downloads after month 1**, reaching 1,000 in a week only after paid "keyword installs". — [ASO World](https://asoworld.com/case-studies/hyper-casual-game-case-study-how-a-new-entrant-gets-its-initial-1000-downloads-in-one-week/)
- A promotion vendor claims that DIY organic growth typically yields **100–1,000 downloads in 3–6 months**. This is a vendor claim with an interest in selling paid campaigns. — [Indie App Santa](https://indieappsanta.com/2025/11/21/10349/)

### Inferences
- Utility CPT of ~$1–1.25 and a typical tap-to-install conversion (commonly 40–60%, **[background, not verified this session]**) imply roughly $2–3 per install. Ad-supported or $2–5 one-time-unlock apps generally cannot recoup that, so for free no-backend apps Apple Ads is mainly useful for testing keywords, not for scaling.
- The documented TikTok successes are subscription, AI or lifestyle apps with a strong visual "hook". A plain utility needs a visually demonstrable output (a before/after, a widget on the home screen, a shareable image) to fit the format.
- Reddit works better as a launch and feedback channel than as paid acquisition.

### Gaps
- No primary data was found on Apple editorial ("App of the Day") or Google Play featuring uplift for indie apps in 2025–2026.
- No Product Hunt download outcomes for mobile apps were found.
- No verified r/iOSProgramming, r/androiddev or r/SideProject "X downloads in Y months" posts were retrieved this session. Searches returned vendor content instead, so a targeted Reddit search is still needed.
- No quantitative evidence was found on share loops (watermarked exports, widgets) for downloads, though widget-led virality is a known pattern, e.g. Locket Widget's #1 ranking in Jan 2022 **[background, not verified this session]**.

## 2. The 2025–2026 App Store flood and platform risk (Apple 4.3/4.2, Google Play testers, developer verification)

### Takeaway
App Store supply is exploding while demand is flat. Sensor Tower counted **235,800 new submissions in Q1 2026 (+84% YoY)**, and total downloads grew only about 2–3%. Apple rejected **371K+ submissions in 2025 for spam, copycats or misleading users**, and 4.3(a) targets near-identical template apps. On Android, new personal accounts still face the 12-testers/14-days gate, and developer verification for all apps (including sideloaded ones) starts in select countries on Sept 30, 2026 and goes global in 2027. A new simple utility now competes in a far more crowded field, and generic templates risk rejection.

### Cited Findings
**Submission surge**
- Sensor Tower: **235,800 new App Store submissions in Q1 2026, up 84% YoY**, attributed in reporting to vibe-coding tools such as Claude Code and Codex. — [The Next Web](https://thenextweb.com/news/vibe-coding-apple-app-store-surge-crackdown); [TweakTown](https://www.tweaktown.com/news/112818/vibe-coding-is-flooding-the-app-store-with-new-apps-on-track-for-record-submissions-in-2026/index.html)
- H1 2026 is estimated at about **560,000 new apps**, roughly double the prior year (NYT, July 20, 2026, citing Sensor Tower). Some outlets project more than **1 million new apps in 2026**, which would beat the 2016 record of about 890,000. — [pbxscience](https://pbxscience.com/app-store-new-app-submissions-may-surpass-one-million-this-year-as-ai-fuels-a-wave-of-junk-apps/); [TweakTown](https://www.tweaktown.com/news/112818/vibe-coding-is-flooding-the-app-store-with-new-apps-on-track-for-record-submissions-in-2026/index.html)
- In 2025, new apps appearing globally grew **30% to nearly 600,000** vs 2024 (The Information / Sensor Tower). Between 2016 and 2024, new submissions had *fallen* 46%. — [9to5Mac, Apr 6, 2026](https://9to5mac.com/2026/04/06/app-store-sees-84-surge-in-new-apps-as-ai-coding-tools-take-off/)
- **Downloads grew only about 3% in 2025 and about 2% in 2026 so far** (Sensor Tower), so supply is outpacing demand. — [TweakTown](https://www.tweaktown.com/news/112818/vibe-coding-is-flooding-the-app-store-with-new-apps-on-track-for-record-submissions-in-2026/index.html); [App Store vibe coding statistics](https://www.appetiteui.com/blog/app-store-vibe-coding-statistics)
- RevenueCat: monthly new *subscription* app launches reached **14,700 by January 2026, about 7x the January 2022 level**. Apps launched before 2020 still earn **69% of subscription revenue**. — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps-2026/)
- Users are reportedly tiring of vibe-coded apps (consumer press). — [Digital Trends](https://www.digitaltrends.com/phones/vibecoded-apps-are-flooding-apples-app-store-and-users-are-getting-sick-of-them/)

**Apple review**
- Apple says it processes **90% of submissions within 48 hours**. Over the 12 weeks before April 2026 it handled more than **200,000 submissions per week** with an average review time of **1.5 days**. Apple increasingly uses AI tools to assist human reviewers. Developers, including Elon Musk in March 2026, complained of delays. — [9to5Mac](https://9to5mac.com/2026/04/06/app-store-sees-84-surge-in-new-apps-as-ai-coding-tools-take-off/)
- In March 2026 Apple pulled or blocked updates to vibe-coding apps (Replit, Anything, Vibecode) for running code that changes app functionality after review. — [9to5Mac](https://9to5mac.com/2026/04/06/app-store-sees-84-surge-in-new-apps-as-ai-coding-tools-take-off/); [The Next Web](https://thenextweb.com/news/vibe-coding-apple-app-store-surge-crackdown)
- Apple's 2025 fraud report (May 2026) covers **9.1M submissions reviewed and 2M+ rejected** (1.2M new apps, about 800K updates), compared with 1.9M rejected in 2024. Of these, **371,000+ were flagged for copying other apps, spam or misleading users**, 22,000+ had hidden features, **443,000 failed for privacy violations**, about 59,000 were removed for bait-and-switch, **193,000 developer accounts were terminated** and 138,000+ enrollments were rejected. — [Apple Newsroom](https://www.apple.com/cm/newsroom/2026/05/the-app-store-stopped-over-2-point-2-billion-usd-in-fraudulent-transactions-in-2025/); [SecurityWeek](https://www.securityweek.com/apple-rejected-2-million-app-store-submissions-in-2025-for-security-and-fraud-prevention/); [heise](https://heise.de/-11304402)
- Apple's 4.3(a) rejection notices (April 2026 forum thread) name these triggers: the same source code or assets as other submitted apps, and "multiple similar apps using a repackaged app template". Apple says such apps share a "similar binary, metadata, and overall concept" with only minor differences. Each rejection gets one appeal to the App Review Board. — [Apple Developer Forums](https://developer.apple.com/forums/thread/822686); [Apple Developer Forums 4.3(a)](https://developer.apple.com/forums/thread/825522)
- An Oct 2026 guide argues that the claim "4.3 catches AI-built apps" is an inference. The guidelines mention "template" and "app generation service" only in 4.2.6. This is unverified. — [Newly guide](https://newly.app/guides/guideline-4-3-spam-rejection)

**Google Play**
- Google's Play Console help says personal developer accounts must run a **closed test with at least 12 opted-in testers for 14 continuous days** before applying for production access. This applies to personal accounts created after Nov 13, 2023; organization accounts are exempt. — [Google Play Console Help](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en-GB). The requirement was originally 20 testers and was lowered to 12 in Dec 2024 **[background, not verified this session]**.
- Some vendor blogs claim 2026 added tester-engagement checks; **no official confirmation was found**. — [Testers Community](https://www.testerscommunity.com/blog/google-play-closed-testing-requirements-2026)
- Android developer verification works like this:
  - Registration opened to all developers in March 2026.
  - User-facing enforcement begins in select countries (Brazil, Indonesia, Singapore, Thailand per earlier plans) on **Sept 30, 2026**, with global rollout in **2027**.
  - Installing apps from unverified developers will require an "advanced" sideloading flow (a 24-hour wait) or ADB.
  - Students and hobbyists get a lighter-requirement console.

  Sources: [Android Authority](https://www.androidauthority.com/android-sideloading-changes-timeline-3679204/); [Cybernews](https://cybernews.com/security/google-test-sideloading-unverified-android-apps/); [9to5Google](https://9to5google.com/2025/08/25/android-apps-developer-verification/)

### Inferences
- With download demand flat and supply up 84–100%, the median new simple utility's organic search share is shrinking. Generic "flashlight/QR/unit converter" ideas face hundreds of fresh near-clones per month.
- 4.3(a) risk mostly bites developers who ship several similar apps from one template. A single, distinct app is low-risk; an "app factory" strategy is high-risk.
- The Play 12-tester gate adds about 2+ weeks and a recruitment problem to every new personal-account developer's first launch. Developer verification makes Play Store distribution even more dominant on Android, since sideloading becomes friction-heavy.

### Gaps
- Apple has not published 4.2 (minimum functionality) rejection counts specifically.
- No hard data was found on how ranking difficulty for new utilities changed between 2024 and 2026 (e.g. median keyword rank achieved), only supply and demand totals.
- Other 2025–2026 Play policy changes (target API level deadlines, etc.) were not researched this session.

## 3. Monetization with zero backend (one-time IAP, tips, ads, paid upfront)

### Takeaway
Freemium apps convert only about 2% of downloads to paid, while hard paywalls convert about 11%. Revenue per install within two weeks is $0.27 (freemium) vs $2.32 (hard paywall). The middle class of apps is shrinking: the median one-year-old subscription app earns tens of dollars per month, and only 17% of new apps reach $1K MRR within two years. One-time unlocks are server-free on iOS via StoreKit 2. Ad revenue for utilities is low (banner eCPM of about $0.20–0.80 globally), and no reliable ARPDAU benchmark for utilities was found.

### Cited Findings
**RevenueCat State of Subscription Apps 2026 (Part 1 released Mar 12, 2026; 115K+ apps, $16B+ revenue)**
- Conversion and early revenue by model:

| Metric | Hard paywall | Freemium |
|---|---|---|
| User-to-subscriber conversion | **11%** | **2%** |
| One-year retention of converted users | 27% | 28% |
| Revenue per install, first 2 weeks | **$2.32** | **$0.27** |

  — [PPC Land summary of RevenueCat SOSA 2026](https://ppc.land/the-app-middle-class-is-dying-and-revenuecats-data-shows-exactly-how-fast/)
- Revenue one year after launch:
  - Average monthly revenue is about **$72**.
  - The top 10% earn **$2,500+/month** and the top quartile at least **$429/month**.
  - The middle 50% earn **$16–$429/month**.
  - Top-quartile revenue by category: Productivity $1,250, Gaming $552.

  — [PPC Land](https://ppc.land/the-app-middle-class-is-dying-and-revenuecats-data-shows-exactly-how-fast/)
- New apps reaching **$1K MRR within two years** fell from 19% to **17%**, and those reaching **$10K MRR** fell from 5.3% to **4.6%**. The top 10% of apps grew MRR 306% YoY while the bottom 25% fell 33%. — [PPC Land](https://ppc.land/the-app-middle-class-is-dying-and-revenuecats-data-shows-exactly-how-fast/); [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps-2026/)
- Utilities' median **download-to-trial (D30) is 6.5%**, among the high performers. Utilities monetization is "highly variable", and Month-1 LTV per payer sits in the middle tier (exact figures are behind the PDF). — [RevenueCat SOSA 2026 – Utilities](https://www.revenuecat.com/state-of-subscription-apps-2026-utilities/)
- Freemium median D35 download-to-paid is **2.1%** vs **10.7%** for hard paywall. Note that this blog's figures differ slightly from the PPC Land summary. — [BuildMVPFast](https://www.buildmvpfast.com/blog/hard-paywall-vs-free-trial-revenuecat-indie-app-2026)
- Part 2 (cancellations): only **5% of users who cancel an annual plan ever reactivate**, and monthly subscribers return about 4x as often. — [lavx news](https://news.lavx.hu/article/annual-app-subscribers-almost-never-return-after-canceling-new-revenuecat-report-shows)

**One-time unlock / lifetime**
- Adapty indie-segment medians (2026), cited by a developer: hard paywall **12.11%** conversion vs freemium+subscription **2.18%**. The same developer cites a Utilities download-to-trial of 24% (Adapty), which conflicts with RevenueCat's 6.5%, likely because of a different definition or sample. — [dev.to (snake_sun), May 2026](https://dev.to/snake_sun/why-i-picked-one-time-iap-over-subscription-for-4-indie-ios-apps-storekit-2-2026-data-1nk6)
- That developer's one-time vs subscription model:
  - At $2.99 one-time the developer keeps **$2.09** per sale.
  - Modeled revenue per 1,000 downloads is about **$251** one-time vs **$152** subscription.
  - The model uses the hard-paywall conversion rate, so it is optimistic for freemium. No actual results are reported yet.
  - The StoreKit 2 IAP code is about **90 lines per app** using `Transaction.currentEntitlements` and verified transactions, with no server component.

  — [dev.to](https://dev.to/snake_sun/why-i-picked-one-time-iap-over-subscription-for-4-indie-ios-apps-storekit-2-2026-data-1nk6)
- About one app in four offers a lifetime option, and lifetime appears on 5–18% of paywalls depending on category. A guide suggests pricing lifetime at about 2–3x the annual price, or 5–12x when it sits alongside a subscription (citing RevenueCat). — [note.com yss_dev](https://note.com/yss_dev/n/n5b747b0e885e?hl=en)
- Real freemium-unlock example: the game Gasketball converted **0.67%** of free players to the paid unlock, against a goal of 2%. — [Wikipedia: Gasketball](https://en.wikipedia.org/wiki/Gasketball)
- Free-to-paid conversion is typically **1–5%**, with top games at 4–8% (secondary source). For indie desktop tools it is 0.5–3%. — [dev.to (kerfiq)](https://dev.to/kerfiq/why-my-indie-tool-has-no-free-tier-no-trial-no-demo-and-the-buy-once-ltv-math-13aa)

**Ads**
- Global average AdMob banner eCPM is **$0.20–$0.80**. A US impression can be worth 5–15x one from a low-income country, and an app with 80% Tier-1 traffic earns about 3x an identical app with 20% Tier-1 traffic. Utility apps get fewer sessions, which limits impressions. — [Playwire](https://www.playwire.com/blog/admob-ecpm-benchmarks-what-publishers-should-expect); [appsfinboard](https://appsfinboard-landing-page.pages.dev/blog/admob-revenue-optimization-guide/)
- Utility apps sit in the low-to-mid eCPM range, behind finance and gaming. — [MonetizeMore](https://www.monetizemore.com/blog/how-much-ad-revenue-can-apps-generate/)
- US rewarded video eCPM is about **$13–$30** depending on source, but the best country/format table is **game-only Q2 2024** data (older). — [Playio](https://blog.playio.co/mobile-game-ecpm-benchmarks-2026)
- AdMob's in-account "Trends and benchmarks" report (opt-in) compares an app against anonymized category peers, and is the most reliable source for real numbers. — [Google AdMob Help](https://support.google.com/admob/topic/14662126?hl=en)

### Inferences
- For a free no-backend utility, a one-time "Pro" unlock at $2.99–$4.99 converting 1–3% of downloads yields roughly **$20–$100 per 1,000 downloads** after Apple/Google's 15% small-business cut. The 15% small-business programme rate is **[background, not verified this session]**. Reaching $1K/month therefore takes roughly 10K–50K downloads per month, which is consistent with RevenueCat's finding that only about 17% of new apps reach $1K MRR in two years.
- Ads on a low-session utility with mostly non-Tier-1 traffic plausibly yield well under $1 per 1,000 daily sessions from banners. Ads only matter at large DAU, and they undercut "privacy/no-ads" positioning.
- StoreKit 2 transactions are JWS-signed and verifiable on-device, so a pro unlock needs no server. Google Play Billing can also run client-only, but Google recommends server-side verification, so client-only is weaker against piracy **[background, not verified this session]**.

### Gaps
- No RevenueCat or AppMagic figures were found on **lifetime/one-time purchase revenue share** or on tip-jar performance.
- No credible utility-specific **ad revenue per DAU (ARPDAU)** benchmark for 2026 was found.
- No 2025–2026 data was found on **paid-upfront** app performance (share of revenue, conversion).
- The full Utilities numbers (trial-to-paid, RPI) are in RevenueCat's gated PDF.

## 4. Unavoidable costs

### Takeaway
Costs are fixed and low: the Apple Developer Program at $99/yr and a $25 one-time Google Play registration **[background, not verified this session]**. Add ongoing OS-update maintenance and Play's tester requirement, which costs time rather than money. Store commission on sales still applies.

### Cited Findings
- Apple keeps 30% of a $2.99 sale ($2.09 net) at the standard rate. Subscriptions drop to 15% in year 2. — [dev.to](https://dev.to/snake_sun/why-i-picked-one-time-iap-over-subscription-for-4-indie-ios-apps-storekit-2-2026-data-1nk6)
- A one-time buyer pays once, but the obligation to support the app and keep it updated for new OS versions is permanent. — [note.com yss_dev](https://note.com/yss_dev/n/n5b747b0e885e?hl=en)
- Recruiting 12 testers for 14 days is a de facto cost for new personal Play accounts. A cottage industry of paid tester services has emerged (the many vendor results are evidence of this). — [Google Play Console Help](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en-GB); [Testers Community](https://www.testerscommunity.com/blog/google-play-closed-testing-requirements-2026)

### Inferences
- Other costs:
  - Apple Developer Program at $99/yr and Google Play at $25 once **[background, not verified this session]**.
  - The 15% Small Business Program rate on both stores for developers earning under $1M/yr **[background]**.
  - Free crash reporting (Firebase Crashlytics free tier; Xcode Organizer and Play Console vitals are built in) **[background]**.
  - A Mac for iOS builds **[background]**.
  - A hosted privacy-policy URL (required by both stores), which can be static/free **[background]**.

### Gaps
- Store fees and Small Business Program terms were not re-verified on official pages this session.

## 5. App traits that correlate with organic growth; privacy-first positioning

### Takeaway
No rigorous data was found linking specific traits (widgets, daily use, shareable outputs, privacy positioning) to organic growth. The evidence is anecdotal. The best-supported points are structural. Supply is flooding generic categories, so niche distinctiveness matters, and the apps that demonstrably grew without ad spend had a visual hook suited to short-form video. "No ads, no tracking, no account" is a very common positioning, but no outcome data shows it wins on its own.

### Cited Findings
- Privacy positioning is widespread: AlternativeTo lists hundreds of pages of "No Tracking" apps, and new free apps such as FeedOff market "no subscription, no account, no tracking". No download outcomes were published for them. — [AlternativeTo No Tracking](https://alternativeto.net/feature/no-tracking/?p=5); [FeedOff](https://feedoff.app/)
- Apple failed **443,000 submissions for privacy violations in 2025**, so privacy is an active review focus. — [Apple Newsroom](https://www.apple.com/cm/newsroom/2026/05/the-app-store-stopped-over-2-point-2-billion-usd-in-fraudulent-transactions-in-2025/)
- Apps launched before 2020 still earn 69% of subscription revenue, and the top 10% grew 306% while the median grew about 5%. Incumbency and network effects dominate. — [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps-2026/)
- Organic TikTok growth came from apps with visual or identity hooks (GlowUp, Vix). For indie games, player- and creator-generated content beat studio posts, which suggests outputs users want to share drive reach. — [Stealwhatworks](https://stealwhatworks.com/blogs/news/apps-over-10k-month-through-tiktok); [PressKit](https://presskit.gg/field-guides/tiktok-indie-game-marketing)
- Distinct purpose, niche and functionality are what avoid 4.3 rejections. — [Apple Developer Forums](https://developer.apple.com/forums/thread/822686)

### Inferences
- Widgets, Live Activities and shareable images act as free distribution because they appear in front of other people (home-screen screenshots, social posts). This is a commonly cited indie pattern, but **no quantitative source was found this session**.
- Seasonal or event-driven niches (tax season, holidays, sports seasons, exams) produce keyword-volume spikes that a small app can rank for temporarily. This is plausible, but unverified here.

### Gaps
- No study was found that quantifies widget presence, daily-use frequency or a privacy-first claim against download growth.
- No AppTweak, Appfigures or Sensor Tower analysis of privacy-label effects on conversion was found.

---

### (a) Criteria that predict whether a free no-backend app can get downloads (synthesized from the evidence above)
1. **Clear, distinct niche with real search demand.** The app targets a specific keyword cluster or community, not a generic utility category flooded by near-clones. This is supported by supply up 84–100% vs downloads up 2–3%, and by 4.3(a) "similar concept" rejections.
2. **A visually demonstrable "hook" for short-form video.** The value can be shown in a 5–15 second clip (before/after, satisfying output, widget on the home screen). All the documented zero-ad-spend growth stories ran on TikTok.
3. **Built-in exposure loops.** Outputs that users share (images, exports with subtle branding), or a home-screen or lock-screen widget others see. This is anecdotal, but it is the only free distribution that scales without a backend.
4. **Repeat or daily use.** Repeat usage supports retention, review accumulation and ad impressions. Playwire notes low-session utilities monetize poorly with ads.
5. **Monetization that tolerates a ~2% conversion rate.** A one-time unlock at $3–10 with a meaningful pro feature, or a hard paywall where justified. Revenue per 1,000 downloads is in the tens of dollars for freemium, so the idea needs a path to 10K+ downloads per month to matter.
6. **Not dependent on paid UA economics.** Utility installs via Apple Ads cost about $2–3, which exceeds the lifetime value of most free utilities, so the idea must win organically.
7. **Low 4.3/4.2 and policy risk.** Original functionality beyond what iOS/Android ship natively, no runtime code changing behavior, and privacy-compliant (443K privacy rejections in 2025).
8. **A reachable community or seasonal spike.** A subreddit, forum or hobby group where a launch post is welcome, or a calendar-driven search spike that a new app can rank for briefly.

### (b) Specific app opportunities with strong evidence
- **None found with strong, verifiable evidence for the free/no-backend profile.** The verified growth stories (GlowUp, Vix, "Early", Cal.ai) are subscription apps, many AI-powered and therefore needing a backend, and their figures are self-reported.
- Weak signals only:
  - "Digital wellbeing / anti-feed" apps marketed as no-account, no-tracking (e.g. FeedOff) exist and are free, but no traction data was found.
  - Faith and devotional content apps showed viral claims (the Bible-scroll app, unverified X post).
  - Countdown, event and simple single-purpose iOS utilities with one-time unlocks are being tried by indies (the dev.to author's NewDaysUntil, AltitudeNow, AutoChoice), with no results published yet.
