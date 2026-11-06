# Self-Hosted and One-Time-License Software as SaaS Alternatives (Market Scan, Nov 2026)

Scope note: research done 2026-11-06. Most evidence is from 2025–2026. Older items are labeled. Many sources are vendor or competitor blogs with a commercial interest (flagged inline). Items from prior knowledge that I did not re-verify in this session appear only under Inferences or Gaps and are marked "unverified".

## 1. Which forced migrations, vendor exits and pricing shocks (2025–2026) are leaving customers stranded?

### Takeaway
The biggest live forced migration is Atlassian Data Center's end of life (sales end March 2028, read-only March 2029), which hits regulated and on-prem-only orgs that cannot move to cloud. Next come Broadcom/VMware (around 90% of customers weighing alternatives), Plex's lifetime price tripling to $749.99 (July 2026), Gmail dropping POP3/Gmailify, and Heroku moving to maintenance-only. Synology's 2025 drive lock-in shock was largely reversed, so that opening has mostly closed.

### Cited Findings
**Atlassian Data Center**
- Atlassian DC end of life for affected products is March 28, 2029. After that date, DC licenses and Marketplace app licenses expire and instances become read-only — [Schneider IT](https://www.schneider.im/atlassian-data-center-end-of-life/); [Jimi Wikman](https://jimiwikman.se/writings/my-articles/atlassian/atlassian-data-center-is-officially-ending-on-march-28-2029-r258). Two sources (Idalko, Medium) give March 30, 2029 instead, so check Atlassian's official page — [Idalko](https://idalko.com/?p=16003); [Medium](https://medium.com/@martyhenderson/the-end-of-on-prem-atlassian-is-retiring-data-center-992fde5eb69d)
- Interim milestone: March 2028 is the end of license sales and Marketplace app purchases for existing customers, which limits expansion before the final date — [Easy8 FAQ](https://www.easy8.com/resources/faq/atlassian-data-center-going-away); [Seibert](https://us.seibert.group/go/data-center-eol)
- Bitbucket DC is reportedly excluded, with a dual cloud/DC license — [Schneider IT](https://www.schneider.im/lu/atlassian-data-center-end-of-life/)
- Competing vendors are already marketing on-prem replacements: Easy Redmine, ONES.com (pitched as a Confluence alternative with "on-premise feature parity"), and Tuleap (French, open-source ALM). These are vendor blogs — [Easy Redmine](https://www.easyredmine.com/atlassian-data-center-alternatives); [ONES](https://ones.com/blog/?p=1068353); [Tuleap](https://www.tuleap.org/agile/tuleap-the-best-jira-alternative)

**Broadcom / VMware**
- A Rimini Street / Unisphere Research 2026 survey reports that 90% of respondents are weighing alternatives because of licensing costs. Sample size is reported as 269 or 300 depending on the source — [Ecosistema Startup](https://ecosistemastartup.com/?p=115092)
- A Virtified Loop survey (April 2026, 450 IT professionals) found 48% plan to shrink their VMware footprint by 2028, and about a quarter said finding suitable alternatives was their biggest hurdle — [Pulse.bot summary](https://www.pulse.bot/ma/news/48-of-vmware-customers-plan-to-reduce-usage-as-competitors-gain-ground-2f6c9886-c70f-45e1-ab1b-34099192aa52/)
- Gartner forecasts that by 2028, 70% of enterprise VMware customers will move 50% of their virtual workloads to alternatives — [cloudmagazin](https://www.cloudmagazin.com/en/2026/03/18/vmware-broadcom-kostenfalle-2026-alternativen-proxmox-nutanix/)
- Proxmox is the most-cited destination, but the evidence for it is anecdotal or from vendor blogs — [cloudnews.tech](https://cloudnews.tech/broadcoms-vmware-price-hikes-are-pushing-customers-toward-proxmox/); [Richweb](https://www.richweb.com/news/vmware-to-proxmox-in-2026/)

**Plex (media servers)**
- Plex Lifetime Pass went from $119.99 to $249.99 on April 29, 2025, its first rise in over a decade. Monthly and annual plans went to $6.99 and $69.99 — [NASCompares](https://nascompares.com/2025/04/18/plex-price-increases-the-rise-of-jellyfin-and-now-what/)
- Lifetime for new buyers went from $249.99 to $749.99 on July 1, 2026. Existing lifetime holders keep their benefits — [AppleInsider](https://appleinsider.com/articles/26/06/27/psa-lifetime-plex-plan-goes-from-24999-to-a-painful-74999-on-july-1); [HotHardware](https://hothardware.com/news/plex-lifetime-pass-skyrockets-to-750)
- Commentators framed the hike as a push toward Jellyfin. I found no measured Jellyfin adoption figures — [Linuxiac](https://linuxiac.com/plex-lifetime-pass-jumps-to-750-jellyfin-responds-with-0-price-increase/)

**Google**
- Gmail is retiring Gmailify and POP3 fetching of external accounts. Most outlets say January 2026 — [TechRepublic](https://www.techrepublic.com/article/news-gmail-ends-gmailify-pop3/); [heise](https://heise.de/-10709020); [PCWorld](https://www.pcworld.com/article/2928100/gmail-users-watch-out-these-2-features-are-being-killed-next-year.html). One source says new users lost access after Q1 2026 and existing users keep it until January 2027, so the timing is conflicting — [Canal26](https://www.canal26.com/tecnologia/2026/02/19/google-retrasa-el-cierre-de-gmail-que-funciones-desapareceran-este-2026-y-como-evitar-perder-tu-correo/)

**Heroku**
- Heroku moved to a "sustaining engineering" model in February 2026: security patches only, no new features. These are competitor blogs, and I found no primary Salesforce notice — [Encore](https://encore.dev/resources/end-of-heroku); [selfhost.dev](https://selfhost.dev/the-10-best-heroku-alternatives-in-2026/)
- The free tier ended November 28, 2022 (older) — [TechTarget](https://www.techtarget.com/it-infrastructure/news/252524336/Heroku-to-end-free-tiers-creating-platform-void-for-devs)

**Synology (shock reversed)**
- In October 2025, DSM 7.3 restored support for unverified third-party HDDs and SSDs on 2025 Plus, Value and J models. Reports said NAS sales fell after the lock-in. M.2/NVMe drives still need validation for some features — [Neowin](https://www.neowin.net/news/synology-backtracks-on-policy-that-allegedly-turned-buyers-away-from-its-nas-devices/); [Guru3D](https://guru3d.com/story/synology-reverses-policy-banning-thirdparty-hdds-after-nas-sales-plummet/); [Techzine](https://www.techzine.eu/news/devices/135275/synology-lifts-artificial-restrictions-on-third-party-storage)

**Creative apps (paid apps going free or subscription)**
- Canva relaunched Affinity as a free all-in-one app (photo, vector, layout). It needs a free Canva account, and AI features are paid — [Neowin](https://www.neowin.net/software/canva-relaunches-affinity-as-a-free-all-in-one-creative-app/); [TipRanks/The Fly](https://www.tipranks.com/news/the-fly/canva-introduces-all-new-affinity-now-completely-free-thefly)
- Apple announced "Creator Studio" in January 2026, a subscription bundle including Pixelmator Pro, Final Cut Pro and Logic Pro, reportedly $12.99/month or $129/year. Pricing comes from thin sources — [toolradar](https://toolradar.com/compare/affinity-by-canva-vs-pixelmator-pro); [iphoneblog.de](https://beta.iphoneblog.de/tag/photoshop/)

### Inferences
- Atlassian DC is the highest-value stranded segment: B2B budgets, a hard deadline, and a hard constraint (data cannot leave the premises). A forced decision window of 2026–2029 is ideal timing for a product launched now. The March 2028 end of sales is the real trigger, because customers who need seat expansions after that date must move.
- Plex's $749.99 lifetime and the media-server boom (see section 3) leave many price-sensitive users moving to Jellyfin, which is free. The paid opportunity is around Jellyfin (clients, migration, setup), not in another server.
- VMware's stranded customers are mostly mid-market IT teams. A solo founder cannot replace a hypervisor, but tooling around Proxmox migration and operations fits the "a quarter say finding alternatives is the biggest hurdle" signal.
- Unverified prior knowledge, worth checking: Microsoft Exchange Server 2016/2019 reached end of support on Oct 14, 2025 (replaced by Exchange Server Subscription Edition); Skype shut down in May 2025; Microsoft Publisher retires in October 2026. All of these push SMBs toward either M365 or self-hosted mail and collaboration.

### Gaps
- No primary Atlassian announcement was fetched (one source returned 403). No count of DC customers was found.
- No Proxmox-specific migration survey and no measured Jellyfin user growth.
- Microsoft retirements (Exchange, Publisher, SharePoint Server) and other 2025–2026 Google shutdowns were not verified in this session.

## 2. Does the "Once" / one-time-license model work, and at what scale?

### Takeaway
The headline 2026 evidence is negative for one-time-fee self-hosted web apps. DHH wrote in March 2026 that ONCE "didn't work": Campfire only recouped its investment, and 37signals open-sourced Campfire, Writebook and Fizzy. Tailwind Plus ($299 lifetime) saw revenue fall about 80% as AI cut docs traffic, followed by layoffs and a Shopify deal. Affinity went free. One-time pricing works best for (a) desktop or BYOK apps with no server cost, (b) supporter-style licenses on popular OSS (Immich), and (c) B2B products with a sharp, urgent need.

### Cited Findings
- **Campfire launch:** in February 2024 (older), DHH said Campfire sold more than $250K in roughly its first week at about $299 — [Build Your SaaS podcast](https://saas.transistor.fm/episodes/is-once-going-to-disrupt-the-indie-saas-world); [onepage-research profile](https://onepage-research.sliplane.app/products/37signals)
- **DHH, "ONCE (Again)", March 16, 2026:** the original plan "sought to sell self-hostable web apps for a one-time fee" and it didn't work. "We recouped the investment on Campfire, our chat app, but that was it." The market "didn't seem to want to pay for self-hosted web apps in a one-off way." They released Campfire, Writebook and Fizzy as free, permissively licensed open source, and are now building a free ONCE application server that runs many apps on one machine. DHH noted that the per-app dedicated box or VM was "cumbersome and costly to maintain" — [DHH, HEY World](https://world.hey.com/dhh/once-again-3e99f755)
- **Campfire open source:** Campfire went MIT on August 21, 2025. Fizzy uses an "O'Saasy" license that bars competing SaaS — [Wikipedia: 37signals](https://en.wikipedia.org/wiki/37signals); [Korben](https://korben.info/en/once-open-source-self-hosted-platform-37signals.html)
- **Writebook:** Writebook was free from launch in 2024 (older) — [Dave Swift review](https://daveswift.com/writebook/)
- **Tailwind Plus:** sold as one-time $299 (individual) / $979 (team). In January 2026, Adam Wathan disclosed revenue down about 80% and docs traffic down 40% since early 2023, attributed to AI, and 75% of the engineering team was laid off — [DevClass](https://www.devclass.com/2026/01/08/tailwind-labs-lays-off-75-percent-of-its-engineers-thanks-to-brutal-impact-of-ai/); [eWeek](https://www.eweek.com/news/tailwind-labs-lays-off-engineers-due-to-ai/). Critics argued that lifetime pricing meant "every dollar required a brand-new buyer" — [Leanware](https://www.leanware.co/insights/tailwind-ai-crisis)
- **Tailwind and Shopify:** on September 9, 2026, Tailwind Labs announced it is joining Shopify. One source says Tailwind Plus closed to new customers; the deal structure is unclear — [Beri](https://www.beri.net/article/shopify-tailwind-labs-acquisition-ai-agents-open-source-funding-model); [Runtimewire](https://runtimewire.com/article/tailwind-labs-joining-shopify-undefined-deal)
- **Immich:** sells a voluntary "supporter" lifetime license at $24.99 per user or $99 per server, from 2024 (older). No sales volume is published — [Immich blog](https://v1.109.0.archive.immich.app/blog/2024/immich-licensing)
- **Coolify:** self-reported funding of about $15K+ MRR from hosted services, about $4.5K/month from GitHub Sponsors and about $1.2K/month from Open Collective. This is undated and self-reported — [coollabsio GitHub](https://github.com/coollabsio); [Open Collective](https://opencollective.com/coollabsio)
- **Affinity:** formerly a one-time-license Serif product, now free under Canva — [Neowin](https://www.neowin.net/amp/canva-relaunches-affinity-as-a-free-all-in-one-creative-app/)
- **BYOK desktop counter-example:** one founder moved a subscription web app to a one-time-purchase desktop app with bring-your-own-keys, removing server and API costs. It was reportedly an "$80,000 cash flow asset in six months" at a 93% margin. Self-reported, and the founder's name differs between sources — [Starter Story via pages.dev](https://app-dev-and-marketing.pages.dev/my-app-failed-then-i-changed-one-thing-and-made-80k); [Rosetta](https://rosetta.to/u/starterstory/my-app-failed-then-i-changed-one-thing-and-made-80k)
- **Critique of pay-once:** an HN commenter argued that subscriptions fund maintenance and that setup and maintenance effort is self-hosting's main obstacle — [HN Q&A mirror](https://ask.live.com.de/34041962)

### Inferences
- The ONCE failure is specific: a generic web app category (chat, books) competing with free OSS and with cheap SaaS, with a per-app VM install burden. It does not show that all pay-once fails. The cited successes are either desktop or local with zero marginal cost, or B2B with acute need.
- AI coding agents cut both ways. They make a solo v1 feasible in 1–3 months, but they also make it cheap for others to clone a pay-once web app as free OSS. They also erode docs- and SEO-driven discovery (the Tailwind lesson). Defensibility has to come from deadlines, migration fidelity, data or format know-how, or distribution, not from the code itself.
- A hybrid model looks most viable: a one-time license that includes 12 months of updates, plus optional paid renewal for updates. This is the Sketch / JetBrains-perpetual-fallback style; noted.lol also suggests paid major upgrades.
- Unverified prior knowledge: Sublime Text sells a $99 license with 3 years of updates. Obsidian made its $50/user/year commercial license optional in early 2025. Paperless-ngx is donation-funded only. Plausible sells cloud SaaS and offers a free AGPL "Community Edition" for self-hosting, with no paid self-host license.

### Gaps
- No unit-sales or cumulative-revenue data for Campfire beyond the launch week. No revenue data for Plausible self-hosted, Umami, Immich licenses, Nextcloud Enterprise, Sketch, Things or Panic apps.
- No audited revenue figure for any indie self-hosted one-time-license product in 2025–2026.

## 3. What do r/selfhosted and adjacent communities signal about demand and gaps?

### Takeaway
The community is large and growing (the selfh.st 2025 survey had 4,081 responses), but what it asks for is polish and integration, not new categories. Recurring requests are lighter alternatives to Nextcloud, OIDC/SSO everywhere, native mobile clients, better Jellyfin clients, a simple Active Directory alternative, Microsoft 365 backup, and infrastructure visibility. Media servers and photos (Immich) are the fastest-growing segments.

### Cited Findings
- The selfh.st 2025 Self-Host User Survey drew 4,081 responses (published Nov 21, 2025). The raw data is on GitHub (selfhst/cdn `2025-results.json`); the charts were not readable in this session — [selfh.st](https://selfh.st/survey/2025-results/)
- A separate 2025 community survey (850+ respondents) found 98.3% container adoption, and the media-server share rose from 40.2% (2024) to 55.9% (2025) — [deployn survey](https://selfhosted-survey-2025.deployn.de)
- The "State of Self-Hosting 2026" report (AI-compiled by a self-hosting publisher, so a weak source) covers 370 apps in 93 categories. It finds about 60% of apps need under 256 MB of RAM. Its most-covered categories are Media Servers, Note Taking & Knowledge, and Reverse Proxy & SSL. It calls photo management (Immich) fast-growing, and names mobile-app polish and 1–5 hours/month of maintenance as pain points — [dev.to / selfhosting.sh](https://dev.to/selfhostingsh/state-of-self-hosting-2026-data-from-315-apps-and-1165-articles-3jcl)
- Requests in "what's missing" threads (mostly 2025, one February 2026 snapshot):
  - Nextcloud is "big and pain to manage" for basic file sync
  - "Biggest thing missing from so many projects is oidc support"
  - A Lidarr alternative for playlists and single tracks
  - Native mobile apps rather than PWAs
  - App and container lifecycle and network visualization
  - Better Jellyfin clients (Tizen, Jellyseerr integration)
  - A free self-hosted Active Directory alternative
  - A self-hosted Microsoft 365 backup tool (the one in use is archived)
  
  Sources: [r/selfhosted Jan 2025 mirror](https://redlib.hbubli.cc/r/selfhosted/comments/1ibmbxq/what_solution_is_missing_in_your_selfhosted_setup); [Feb 2026 snapshot](https://reddit.sentinel-team.org/subreddits/selfhosted/snapshots/2026-02-13T03%3A31%3A05.320637Z); [r/selfhosted Apr 2025](https://lr.in.psf.lt/r/selfhosted/comments/1jqc698/hot_take_whats_the_one_selfhosted_tool_this/ml5xfeu)
- On the monetization mood: noted.lol (October 2026) says that "a reasonably priced lifetime license can be quite appealing". It argues subscriptions are justified for hosted services but weak for software on the user's own hardware, and it suggests one-time purchases with paid major upgrades. RustDesk is cited as a free-plus-paid self-hosted example — [noted.lol](https://noted.lol/free-self-hosted-software-subscriptions/)
- Developers report that users "actively resent" adding even a $3/month subscription — [IndieHackers](https://www.indiehackers.com/post/1dd70ff8f6)

### Inferences
- The self-hosted hobbyist market prefers free OSS and pays mainly for supporter licenses, clients and hardware. Paying buyers are more likely to be small businesses, prosumers and IT teams who want "it just works" with SSO, backups and a mobile client.
- The requests that line up with money are Microsoft 365 backup, an AD/SSO replacement and infrastructure visibility, because businesses have those needs.

### Gaps
- No current r/selfhosted subscriber count or growth curve was found. No 2026 HN "what would you pay once for" thread was located. awesome-selfhosted was not analyzed for gaps.
- The selfh.st 2025 numeric breakdowns (willingness to pay, top apps) were not extracted.

## 4. Is the digital sovereignty / "buy European" movement creating demand, and in which categories?

### Takeaway
Yes, and it is concentrated in public-sector office, email and collaboration (Microsoft Exchange/Outlook, SharePoint and Office replaced by open-source email, Nextcloud, LibreOffice and openDesk). The EU Commission issued a tech-sovereignty package in June 2026. Adoption lags rhetoric: about 83% of EU cloud and software spend still went to US firms in 2024.

### Cited Findings
- The European Commission presented a technological-sovereignty package on June 3, 2026, covering semiconductors, AI, cloud and open-source software — [Swissquote](https://www.swissquote.com/en-ch/private/inspire/swissquote-magazine/the-data-war/europes-quest-for-digital-sovereignty)
- About €330B (83%) of roughly €400B in European cloud and software spend went to US companies in 2024 — [Swissquote](https://www.swissquote.com/en-ch/private/inspire/swissquote-magazine/the-data-war/europes-quest-for-digital-sovereignty)
- The Tuta-commissioned "State of Digital Sovereignty 2026" (1,818 IT decision-makers in Germany, France and the Nordics) found 40% of German IT leaders actively implementing European software, up from 20% in 2025. Tuta is a vendor — [Tuta](https://tuta.com/blog/digital-sovereignty-study)
- Schleswig-Holstein is the first German state to fully move email from Exchange/Outlook to open source: 40,000 accounts and 100M emails. It plans to replace SharePoint with Nextcloud and Office with LibreOffice, with estimated savings of €15M/year. About 20% of workstations still need Word and Excel — [WinFuture](https://winfuture.de/news,154283.html); [Cybernews DE](https://cybernews.com/de/tech/schleswig-holstein-verbannt-microsoft-dienste/)
- Hamburg's parliament passed a motion on May 6, 2026 to assess replacing Microsoft 365 with openDesk. A study found openDesk cannot yet fully replace Microsoft (gaps in notifications, data exchange and security features) — [Cybernews](https://cybernews.com/tech/hamburg-microsoft-opendesk/)
- An Austrian ministry (BMWET) moved from Microsoft to Nextcloud (October 2025). The ICC is reportedly switching to openDesk, but that is a single unverified report — [Gigazine](https://gigazine.net/gsc_news/en/20251031-austria-bmwet-nextcloud)
- Barriers include high switching costs, integration issues and limited European-scale alternatives. Defense planners prefer "sovereign configurations" of US tech — [BISI](https://bisi.org.uk/reports/european-tech-sovereignty-and-the-security-risks-of-decoupling); [The Good Lobby](https://thegoodlobby.eu/why-arent-europeans-switching-to-european-digital-alternatives/)
- Atlassian DC alternatives are pitched specifically to EU orgs that need data control (Tuleap, European sovereign cloud) — [Tuleap](https://www.tuleap.org/agile/tuleap-the-best-jira-alternative); [Easy Redmine](https://www.easyredmine.com/blog/jira-end-data-center)

### Inferences
- Large public-sector deals go to integrators and big OSS vendors (Nextcloud, Open-Xchange, openDesk/ZenDiS), not solo founders. The solo-founder angle is the gaps those stacks leave: migration and import tools (Exchange/SharePoint/Confluence to OSS), compliance and backup add-ons, and polished niche apps for EU SMBs and Mittelstand firms that want "EU-hosted or on-prem" checkbox compliance.
- An EU-based founder has a marketing edge ("made in EU, runs on your server").

### Gaps
- I found no hard data on SMB (as opposed to public-sector) adoption of sovereign tools, and no category-level spending shift data.

## 5. What are the pricing benchmarks for one-time licenses?

### Takeaway
Consumer and prosumer one-time licenses cluster at $25–$300. Supporter licenses run about $25 per user or $99 per server. Developer and UI products run $299–$979. Lifetime deals (LTDs) run $49–$299. B2B on-prem replacements are typically per-server or per-seat with annual maintenance, but I found little public pricing data.

### Cited Findings
- Campfire (ONCE): about $299 one-time (2024) — [onepage-research](https://onepage-research.sliplane.app/products/37signals); [Dave Swift](https://daveswift.com/writebook/)
- Immich supporter: $24.99 per user / $99 per server — [Immich](https://v1.109.0.archive.immich.app/blog/2024/immich-licensing)
- Tailwind Plus: $299 individual / $979 team (lifetime) — [Leanware](https://www.leanware.co/insights/tailwind-ai-crisis)
- Plex Lifetime: $119.99, then $249.99 (April 2025), then $749.99 (July 2026). Annual is $69.99 — [AppleInsider](https://appleinsider.com/articles/26/06/27/psa-lifetime-plex-plan-goes-from-24999-to-a-painful-74999-on-july-1); [NASCompares](https://nascompares.com/2025/04/18/plex-price-increases-the-rise-of-jellyfin-and-now-what/)
- Typical LTD pricing is $49–$299. AppSumo leaves the founder about 60% of revenue, versus about 97% through a merchant-of-record platform. VAT and sales tax still apply — [Fungies](https://fungies.io/how-to-run-saas-lifetime-deal-2026.md)
- Founder posts: "$29 once vs competitors' $144/year" and "$49 once for my desktop app" — [dev.to](https://dev.to/rafay_korai_cb5d79a6a13fa/i-charge-29-once-for-software-that-competitors-charge-144year-for-heres-why-44hf); [IndieHackers](https://www.indiehackers.com/post/why-im-charging-49-once-instead-of-a-subscription-for-my-desktop-app-aabcd91ddb)
- Revenue anecdotes (all self-reported): about $65K from LTDs in 3 days and then about $20K/month — [Starter Story summary](https://stationlm.com/analysis/6afd7437-ff2f-4ce3-84a7-6397c4ec3eb8); 50 pre-sold LTDs for about $20K — [stormy.ai](https://stormy.ai/blog/saas-pricing-strategy-lifetime-deal-bootstrap-revenue)
- Some self-hosted vendors sell a one-time fee that includes 1 year of updates and support, with a discounted renewal — [noted.lol](https://noted.lol/free-self-hosted-software-subscriptions/); [DashboardFox](https://dashboardfox.com/pricing)

### Inferences
- Suggested price points for a solo founder:
  - Consumer or prosumer tool: $29–$79 once.
  - Prosumer or homelab "pro" license: $49–$149, plus about 40–50% for a major-version upgrade.
  - SMB or IT on-prem tool: $499–$2,500 per server once, plus 20–25%/year optional maintenance.
- Atlassian or VMware exit tools can be priced against the cost of the alternative (Atlassian Cloud Enterprise, consultants), which supports four-figure prices.

### Gaps
- No verified public pricing for B2B on-prem wiki or ALM replacements (Easy Redmine, ONES on-prem). No real upgrade-pricing data from Sketch, Things or Panic in 2025–2026.

## 6. Which categories are saturated with free OSS, and which lack a polished, payable product?

### Takeaway
Saturated (hard to charge for): media servers (Jellyfin), photos (Immich), document management (Paperless-ngx), PaaS / Heroku replacements (Coolify, Dokku, now DHH's free ONCE server), analytics (Plausible CE, Umami), chat (Campfire is now MIT), wikis (BookStack and others), and reverse proxy and SSO building blocks. Under-served: migration and import tooling for forced exits, SaaS backup (M365/Google), simple SMB identity, native mobile and TV clients for OSS servers, and lightweight "one job done well" replacements for heavy suites (Nextcloud).

### Cited Findings
- Heavily covered and free categories: Media Servers, Note Taking & Knowledge, and Reverse Proxy & SSL top coverage. Jellyfin, BookStack and Navidrome are the most-referenced apps — [selfhosting.sh report](https://dev.to/selfhostingsh/state-of-self-hosting-2026-data-from-315-apps-and-1165-articles-3jcl)
- PaaS: Coolify is free and OSS with a hosted tier — [coollabsio](https://github.com/coollabsio). DHH is shipping a free ONCE server for many apps on one box — [DHH](https://world.hey.com/dhh/once-again-3e99f755)
- Campfire, Writebook and Fizzy are free and open source — [DHH](https://world.hey.com/dhh/once-again-3e99f755)
- Gaps named by users: mobile apps lag, OIDC is missing, Nextcloud is too heavy, there is no simple AD alternative, the Microsoft 365 backup tool is archived, and Jellyfin clients are weak — [r/selfhosted mirror](https://redlib.hbubli.cc/r/selfhosted/comments/1ibmbxq/what_solution_is_missing_in_your_selfhosted_setup); [selfhosting.sh report](https://dev.to/selfhostingsh/state-of-self-hosting-2026-data-from-315-apps-and-1165-articles-3jcl)
- openDesk has functional gaps (notifications, data exchange, security features) — [Cybernews](https://cybernews.com/tech/hamburg-microsoft-opendesk/)
- About a quarter of VMware leavers cite finding alternatives as the top hurdle — [Pulse.bot](https://www.pulse.bot/ma/news/48-of-vmware-customers-plan-to-reduce-usage-as-competitors-gain-ground-2f6c9886-c70f-45e1-ab1b-34099192aa52/)

### Inferences
- Rule of thumb: do not build "another X server" where X already has a 30K+ star OSS leader. Build the paid edge around it: importers, clients, backup, compliance, or a one-command appliance for non-technical SMBs.

### Gaps
- No GitHub star-trend dataset was pulled in this session to quantify saturation by category.

## 7. Concrete product opportunities (6–10) and the ranked top-4 shortlist

### Takeaway
The best openings attach to a deadline or a stranded population (Atlassian DC, Plex lifetime, Gmail POP, VMware) or to a business-grade gap in free OSS (M365/Workspace backup, SMB identity). Generic pay-once web apps are a weak bet, given the evidence from ONCE, Tailwind and Affinity.

### Cited Findings
- Supporting evidence is cited in sections 1–6. Key anchors:
  - Atlassian DC: sales end March 2028, read-only March 28, 2029 — [Schneider IT](https://www.schneider.im/atlassian-data-center-end-of-life/); [Easy8](https://www.easy8.com/resources/faq/atlassian-data-center-going-away)
  - Microsoft 365 backup tool gap — [r/selfhosted mirror](https://redlib.hbubli.cc/r/selfhosted/comments/1ibmbxq/what_solution_is_missing_in_your_selfhosted_setup)
  - Plex $749.99 lifetime — [AppleInsider](https://appleinsider.com/articles/26/06/27/psa-lifetime-plex-plan-goes-from-24999-to-a-painful-74999-on-july-1)
  - Media-server share at 55.9% — [deployn](https://selfhosted-survey-2025.deployn.de)
  - Gmail POP/Gmailify retirement — [TechRepublic](https://www.techrepublic.com/article/news-gmail-ends-gmailify-pop3/)
  - VMware: 90% weighing alternatives — [Ecosistema Startup](https://ecosistemastartup.com/?p=115092)
  - Schleswig-Holstein moving off Exchange and SharePoint — [WinFuture](https://winfuture.de/news,154283.html)
  - BYOK desktop pay-once success — [Starter Story](https://app-dev-and-marketing.pages.dev/my-app-failed-then-i-changed-one-thing-and-made-80k)

### Inferences
**Candidate opportunities (9).** All are inferences built from the findings above, not validated with customers.

1. **Confluence (and Jira) Data Center exit kit.**
   - What: a self-hosted, high-fidelity Confluence importer. It converts page trees, macros, attachments, permissions and page history into an existing OSS wiki (BookStack, Outline, Docmost, Wiki.js) or a thin branded wiki. Sold as a per-instance one-time license.
   - Buyers: regulated and EU DC customers facing March 2028 / March 2029.
   - Price: $990–$4,900 per instance once, plus optional support.
2. **Self-hosted Microsoft 365 / Google Workspace backup appliance.**
   - What: a Docker appliance that backs up mail, OneDrive/SharePoint and Drive to local or S3/EU storage, with restore and search UI.
   - Why: a cited community gap (the existing tool is archived), plus sovereignty and ransomware drivers.
   - Price: $299–$999 per tenant once, plus a yearly update plan.
3. **Plex-to-Jellyfin "switch kit".**
   - What: migrates users, watch history, collections, ratings and playlists, then gives a guided setup.
   - Optional upsell: a polished paid TV or mobile client (Tizen, webOS, Apple TV).
   - Price: $19–$49 once.
4. **Proxmox SMB operations add-on for VMware leavers.**
   - What: a migration-readiness scanner (vCenter inventory mapped to Proxmox), a VM conversion runbook, and a multi-node dashboard with backup verification and chargeback reports.
   - Price: per node or per cluster, one-time.
5. **Gmail POP/Gmailify replacement.**
   - What: a small self-hosted container or desktop app that polls POP3/IMAP accounts and injects mail into Gmail via API, keeping labels and spam filtering.
   - Price: $19–$39 once.
   - Caveat: the window is uncertain because the retirement timing conflicts between sources.
6. **Simple SMB directory and SSO ("AD for 5–50 people").**
   - What: an opinionated, one-command LDAP and OIDC server with device onboarding docs and a friendly admin UI.
   - Competes with free Authentik, Kanidm and LLDAP (prior knowledge, unverified), so it must win on simplicity.
   - Price: $299–$799 once.
7. **Lightweight file sync / share ("Nextcloud without the suite").**
   - What: a single binary with a mobile app, sold as a pro license.
   - Moderate demand signal, but crowded by Seafile and Syncthing (unverified).
8. **Exchange/SharePoint-to-OSS migration tools for EU SMBs and municipalities.**
   - What: tools that follow the Schleswig-Holstein-style moves, for example SharePoint document libraries and permissions into Nextcloud. Sold as per-migration one-time licenses.
9. **BYOK local-first desktop apps sold once.**
   - Examples: meeting transcription, document Q&A, or a research assistant using the user's API keys or local models.
   - This dodges server costs, matching the cited $80K case. It competes with many AI apps, so a vertical niche is needed.

**Ranked top-4 shortlist**

**#1 Confluence Data Center exit kit (importer + self-hosted wiki target, one-time per-instance license).** This is the only opportunity with a hard, vendor-imposed deadline: license sales end March 2028 and instances go read-only March 28/30, 2029. It hits buyers with real budgets who often cannot use the cloud by policy or regulation, especially in the EU, where sovereignty pressure is rising. The pain is migration fidelity, which free OSS wikis generally do not solve well. That is the kind of format-parsing work (Confluence storage XML, macros, attachments, permissions) that AI coding agents speed up. A v1 targeting one destination (for example BookStack or Outline) plus a dry-run fidelity report is feasible in 1–3 months. A four-figure one-time price is defensible against the cost of Atlassian Cloud Enterprise or consultants. Risks: incumbent vendors (Easy Redmine, ONES, Tuleap) are courting the same buyers, and enterprise sales cycles are slow. Mitigate by selling self-serve to mid-size teams and partnering with Atlassian-exit consultancies.

**#2 Self-hosted Microsoft 365 / Google Workspace backup appliance.** Self-hosters explicitly flag this gap (the tool they relied on is archived). It aligns with three demand drivers: sovereignty (keep a copy on EU or on-prem storage), ransomware and compliance, and the broader EU move away from Microsoft, where hybrid periods require backups. Buyers are SMBs and MSPs with budget, the need recurs, and a one-time license plus an optional yearly update plan fits the "runs on my hardware" preference the community voices. The Graph and Gmail APIs are well documented, so a v1 (mail + OneDrive/Drive backup to S3/local, with restore) is feasible in 1–3 months. Risk: commercial SaaS backup vendors exist, so the wedge is "self-hosted, one-time, data never leaves you."

**#3 Plex-to-Jellyfin switch kit (migration + polished client upsell).** The stranded population is large and freshly angry: lifetime went from $119.99 to $249.99 in 2025 and then to $749.99 in July 2026, and media servers are now about 56% of self-hosters' setups. Jellyfin is free, so the money is in reducing switching cost (moving users, watch state, collections, playlists) and in client polish, where users repeatedly complain (TV and mobile apps). Small one-time prices ($19–$49) match the consumer segment, and Reddit plus YouTube homelab channels make distribution cheap. A v1 migrator can be built in weeks. Risks: a free OSS migration script could undercut it, so bundle it with guided setup, a hardware-transcoding config wizard and a client to keep it worth paying for. Plex may also soften pricing.

**#4 Proxmox operations and migration add-on for SMB VMware leavers.** Around 90% of VMware customers are weighing alternatives, about a quarter say finding an alternative is the hardest part, and Proxmox is the most-cited SMB destination. That makes "make Proxmox feel enterprise-ready" a payable layer: a vCenter inventory and readiness scanner, guided VM conversion, a multi-cluster dashboard, and backup-verification and capacity reports. IT teams pay one-time per-node licenses more readily than hobbyists, and the tool sits next to (not against) free Proxmox. A scanner and report v1 is quick to build and doubles as lead generation. Risk: Proxmox's own management tooling and established MSPs may cover this. Validate with r/sysadmin and r/Proxmox before committing. (Honorable mention as a fast, small-ticket experiment: the Gmail POP/Gmailify replacement in opportunity #5.)

### Gaps
- None of the opportunities has been validated with customer interviews, keyword volume or competitor revenue data. Run a 2-week landing-page and pre-sale test for #1–#3 before building.
