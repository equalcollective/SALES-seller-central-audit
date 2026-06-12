# Ad Analysis - Scary Peeper Inc.

**Data window:** 2026-01-22 to 2026-04-20 (last 90 days, full ad data availability)
**Total account ad spend:** $1,914 | **Total account ad sales:** $17,003 | **Account ROAS:** 8.89

**Important caveat:** Ad data coverage is ~90 days only. We cannot see what happened during Halloween 2025 (Sep-Oct). Findings reflect current/recent behavior, not historical peak-season strategy.

## Account Level

### Campaign Structure

The account has 6 campaigns over the 90-day window, but only **1 is currently ENABLED**. Nearly all spend went to paused razor blade campaigns.

| Campaign | Status | Advertised Product Line | Spend | Sales | ROAS | Clicks |
|----------|--------|------------------------|-------|-------|------|--------|
| Harry 8-pack 2/10/2026 | PAUSED | Razor Blade 8ct | $617 | $6,658 | 10.80 | 1,527 |
| Harry 12-pack 2/10/2026 | PAUSED | Razor Blade 12ct | $541 | $5,828 | 10.77 | 1,381 |
| Harry 4-pack 02/10/2026 | PAUSED | Razor Blade 4ct | $492 | $2,745 | 5.58 | 1,470 |
| B0GHGSWRG7 \| Auto \| $20/day | PAUSED | Razor Blade auto | $239 | $1,630 | 6.83 | 785 |
| SP - Phrase - Top Selling Products | ENABLED | Scary Peeper (5 SKUs) | $26 | $142 | 5.38 | 98 |
| Harry 4 Count 01/08/2026 | - | Razor Blade 4ct | $0 | $0 | - | 0 |

> **Finding: The Scary Peeper Halloween brand has essentially no advertising infrastructure.**
>
> **Problem:**
> - Only one Halloween-related campaign is active: "SP - Phrase - Top Selling Products" with $26 spend over 90 days and just **2 phrase keywords** covering **5 different Scary Peeper products** simultaneously
> - That means the signature brand is getting less than $10/month in ad investment
> - Four razor blade campaigns drove ~99% of the account's ad activity in this window, and all are now paused
> - No auto campaigns, no exact match campaigns, no product targeting campaigns exist for the Halloween portfolio
> - The single active campaign bundles 5 products (B00F4HRW50 Peeping Tom, B012U6OSZO Giggle, B01LXND0HR Lenticular Clown, B073X583YZ Hitchhiker, B07V6JVJPZ), so no individual product can be scaled independently. Budget is spread too thin for any one product to gain meaningful traction.
>
> **Solution:**
> - Build a Scary Peeper Halloween ad stack from scratch before Halloween 2026 preseason (August launch window)
> - Minimum viable structure per hero product: 1 auto campaign (discovery), 1 manual exact match campaign (proven converters), 1 manual phrase campaign (discovery + defense), 1 product targeting campaign (competitor ASINs and own-brand defense)
> - Split the currently-bundled phrase campaign into individual campaigns per product. Each SKU needs its own budget and bid control
> - Use the 4 paused razor blade campaigns as the template — the structure there (close-match, substitutes, loose-match, complements on autos; tight manual campaigns with one product per campaign) was producing 5.6-10.8 ROAS before being paused
>
> **Impact:**
> - The brand has proven PPC competence on razor blades (10.8 ROAS). Applying that same discipline to the Halloween portfolio during the Sep-Oct peak, with Tier 1 + Tier 2 SQP blockers as the target keyword list, is the single highest-leverage change available.
> - Rough impact estimate: a 2-3% impression share lift on Tier 2 during Halloween preseason (Aug-Oct 2026) at market conversion rates maps to roughly $50K-100K of incremental Halloween revenue (see SQP Analysis for the full funnel math).

### Auto vs Manual Split

With 4 of 6 campaigns paused, the 90-day account-wide view shows:

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|--------|-------|-------|------|-----|-----|-----|
| Automatic | 785 | $239 | $1,630 | 6.83 | $18.52 | $0.30 | 11.21% |
| Manual (Keyword+Product) | 4,476 | $1,675 | $15,373 | 9.18 | $27.79 | $0.37 | 12.53% |

Manual outperforms auto (9.18 vs 6.83 ROAS), which is the healthy pattern. Manual is driving 87% of spend and 90% of sales. The harvest-and-scale loop has clearly been running — the razor blade manual campaigns (close-match, substitutes, loose-match targets) show that when this team operates, they operate well. This is not an "auto-on-autopilot" account.

### Keyword vs Product Targeting

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|-------------------|--------|-------|-------|------|-----|-----|-----|
| Keyword Targeting | 3,013 | $1,091 | $10,472 | 9.60 | $26.05 | $0.36 | 13.34% |
| Product Targeting | 2,248 | $823 | $6,531 | 7.94 | $25.12 | $0.37 | 11.57% |

Healthy split. Keyword targeting has a slight edge (9.60 vs 7.94 ROAS) but both are above the 1.5x profitability threshold by a wide margin. No reallocation needed.

### Match Type Breakdown

Only PHRASE appears in the last-90-day data for currently-trackable campaigns. The paused razor blade campaigns operated on auto-targeting rather than match-type-classified keywords, and the only active manual campaign is PHRASE-only.

| Match Type | Clicks | Spend | Sales | ROAS | CVR |
|------------|--------|-------|-------|------|-----|
| EXACT | 0 | $0 | $0 | - | - |
| PHRASE | 98 | $26 | $142 | 5.38 | 5.10% |
| BROAD | 0 | $0 | $0 | - | - |

> **Finding: No exact match campaigns exist.**
>
> **Problem:** Exact match is where the proven converting keywords live. Without any EXACT campaigns in the account, there is no place to harvest and scale winning search terms from phrase/broad/auto. The "SP - Phrase - Top Selling Products" campaign holds two converting keywords ("scary peeper window prank" ROAS 5.50, "scary face for window" ROAS 5.19) that should be in an EXACT campaign with dedicated bids.
>
> **Solution:** Create EXACT match campaigns for the Tier 1 keywords from the SQP analysis, starting with the two that already converted in the phrase campaign. Add the other four Tier 1 keywords ("peeping tom window prank", "window peeper", "halloween window peeper", "scary face window prank", "scary face window cling") as the next wave.
>
> **Impact:** Exact match lets you set bids per keyword and typically delivers 30-50% better CVR than phrase on the same query. More importantly, it enables budget discipline: you can give your highest-ROAS keywords the spend they deserve instead of splitting budget across five products and two phrase terms.

### Campaign Profitability

All 5 campaigns with meaningful spend are profitable (ROAS 5.38-10.80, all well above 1.5x). No wasted-spend pause candidates. The problem is not that spend is being wasted; it is that the overall spend is too small and over-concentrated on a product line (razor blades) that has been paused.

## Product Level (P0)

### P0 Campaign Map

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| SP - Phrase - Top Selling Products (shared with 4 other SKUs) | $10.21 | $63.97 | 6.27 | 40 | ~2 |

- P0 ad spend as % of account ad spend: 0.53%
- P0 ad spend as % of Halloween-brand ad spend: 39%
- Total P0 90-day ad budget: $10.21. Ten dollars. Across three months.

### Blocker-Specific Findings

#### Impression Share Blocker: Keyword Spend vs. Tier 1 / Tier 2 Queries

The SQP analysis identified impression share as the primary blocker on both Tier 1 (partial, at 19.7% of ~24-27% cap) and Tier 2 (near-zero, at 0.16%). The PPC lever is straightforward: bid on those keywords. Here is what the ad data shows for the tagged queries.

| Search Term | Tier | Current Ad Spend | Clicks | Orders | ROAS | In Active Campaign? |
|-------------|------|------------------|--------|--------|------|--------------------|
| scary peeper window prank | Branded | $16.36 | 65 | 3 | 5.50 | Yes (phrase) |
| scary face for window | Tier 1 | $10.02 | 33 | 2 | 5.19 | Yes (phrase) |
| peeping tom window prank | Tier 1 | $0 | 0 | 0 | - | **No** |
| window peeper | Tier 1 | $0 | 0 | 0 | - | **No** |
| halloween window peeper | Tier 1 | $0 | 0 | 0 | - | **No** |
| scary face window prank | Tier 1 | $0 | 0 | 0 | - | **No** |
| scary face window cling | Tier 1 | $0 | 0 | 0 | - | **No** |
| halloween jump scare | Tier 2 | $0 | 0 | 0 | - | **No** |
| halloween prank | Tier 2 | $0 | 0 | 0 | - | **No** |
| scary halloween decorations | Tier 2 | $0 | 0 | 0 | - | **No** |
| scary halloween mask | Tier 2 | $0 | 0 | 0 | - | **No** |

> **Finding: The account is not bidding on the keywords where impression share is the blocker.**
>
> **Problem:**
> - Of 6 Tier 1 keywords identified in the SQP analysis, only **1** is being bid on ("scary face for window", $10 spend over 90 days)
> - Of 4 Tier 2 keywords, **0** are being bid on
> - The one Tier 1 keyword that is live shows 5.19 ROAS on $10 spend — the keyword converts, it is just starved for budget
> - The one branded keyword that is live ("scary peeper window prank") also converts at 5.50 ROAS — Scary Peeper is literally running ads on their own brand name and it works, but no defensive branded campaign exists beyond this one
>
> **Solution:**
> - Launch one EXACT match campaign with the 6 Tier 1 keywords. Dedicated budget of $20-40/day during preseason (Aug-Oct) plus $5-10/day in off-season
> - Launch one PHRASE match campaign with the 4 Tier 2 keywords. Dedicated budget of $30-50/day during preseason to buy visibility on the larger addressable market
> - Create a branded defense EXACT campaign (2-3% of total budget) covering "scary peeper", "scary peeper window prank", "scary peeper hitchhiker", "scary peeper giggle" and other brand variations
> - Do not do this in isolation. Fix the P0 listing issues first (brand registry error, Spanish bullet, short video, keyword-stuffed title — from Product Understanding) so the incremental traffic converts at the brand's typical rate
>
> **Impact:**
> - Tier 1: Currently at 19.7% impression share vs ~24-27% cap. Moving to cap recovers the remaining ~5% impression share. At the market's existing conversion rates and the brand's 45% purchase share, rough math: $1,580/mo market × remaining 5% impression share × 0.45 purchase share = ~$35/mo incremental from Tier 1 during off-season, scaling to ~$700/mo during Halloween peak
> - Tier 2: Currently at 0.16% impression share vs ~24-27% cap. Getting to even 5% impression share during preseason (a modest goal) at market conversion norms maps to roughly 250 incremental cart adds/month during Sep-Oct. At ~$20 AOV and typical cart-to-purchase rate, that is ~$2,500-5,000/month in incremental Halloween revenue for P0 alone. Since multiple Scary Peeper SKUs rank on Tier 2 queries, the benefit extends across the whole Halloween portfolio

## Insights

- **The brand has proven they can run ads well (razor blades at 5.6-10.8 ROAS), but they are not applying that capability to the Scary Peeper Halloween portfolio.** The 90-day view shows the core brand getting $26 in ads across 5 products. This is not a competence problem; it is an allocation problem.
- **The ENABLED phrase campaign proves Tier 1 keywords convert at positive ROAS with zero optimization.** "Scary peeper window prank" converted at 5.50 ROAS and "scary face for window" at 5.19 ROAS on tiny spend — these are buy-more-of-it signals, not reassess-the-strategy signals.
- **All four paused razor blade campaigns had good ROAS (5.58-10.80) when they ran.** They were not paused because they failed. Understanding why they were paused is a key seller question because it shapes whether razor blades should be scaled back up, reallocated to Halloween, or treated as a legitimately stopped experiment.
- **Tier 3 is rightly ignored by the current ad strategy.** No budget is being wasted on "halloween decorations outdoor" or similar broad queries. This is the correct decision given the scale of competition there.

## Things to Investigate Further

- **What is the Halloween 2025 ad history?** The 90-day window starts Jan 22, 2026, so we cannot see what ran in Sep-Oct 2025. If meaningful Halloween preseason ads ran last year and were turned off in November, we should replicate that playbook earlier and larger in 2026. If no Halloween ads ran at all in 2025, then this is a greenfield buildout and the 8-week plan should plan for 2-3 months of ramp.
- **Placement data on the ENABLED phrase campaign.** Is the $26 being spent on Top of Search, Rest of Search, or Product Pages? With only 98 clicks, placement analysis would be statistically thin, but worth a glance before the call.

## Questions for the Seller

- **Why were all four razor blade campaigns paused?** They were running at 5.6-10.8 ROAS — strong performance. Common reasons: inventory constraint, margin problem, strategic pivot, or a specific account issue. The reason determines whether to relaunch them, redirect budget to Halloween, or something else.
- **Did the Scary Peeper Halloween portfolio run ads during Sep-Oct 2025?** Ad data only covers the last 90 days so we cannot see it directly, but the answer shapes how aggressively we can scale ad investment for Halloween 2026.
- **Is there a reason the "SP - Phrase - Top Selling Products" campaign was built as a single bundled campaign across 5 products rather than per-product campaigns?** If there is a historical rationale (budget discipline, testing, etc.), that changes how we approach restructuring it.
