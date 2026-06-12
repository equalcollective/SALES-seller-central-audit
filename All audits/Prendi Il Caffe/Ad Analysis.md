# Ad Analysis - Prendi Il Caffe

## Period: 2026-02-02 to 2026-05-02 (90 days)

**Account totals across all campaigns:**
- 46 campaigns, $3,916 total spend, $10,303 total sales, 140 orders, 3,227 clicks
- Account ROAS: 2.63x | Account TACoS (based on $30K+ catalog sales): ~13%

Ad spend started Feb 2026, so this 90-day window covers the entire history of paid advertising on this account.

## Account-Level Findings

### Campaign Structure

> **Finding: 46 campaigns, many overlapping the same products, with overstuffed manual campaigns and dead duplicates.**
>
> **Problem:**
> - 46 campaigns for a 25-parent catalog. Multiple campaigns advertise the same hero product. Example: the Spinel Ciao Espresso Machine (P0, B0DQLQYRXM) is being advertised by **6 different campaigns** simultaneously: Campaign - 11/13/2025, Ciao 03/2026, Ciao 03/2026 Manual, Ciao M, Espresso machine, Emachine. They are competing with each other for the same impressions.
> - 8 manual campaigns have 10+ targets crammed into one campaign. The worst offenders are NEW_SELECTION: B0GNTBMPDX (27 targets, $26 spend), Ciao M (19 targets, $93 spend), Can manual (18 targets, $156 spend, ROAS 1.16x), Tenerelli Manual (17 targets, $39 spend, 0 orders).
> - One auto campaign, "Campaign - 11/13/2025 15:51:55.420," carries $2,098 in spend (54% of total account spend) and produces 3.17x ROAS. It is the lifeblood of the account, and at the same time it advertises a mix of high-AOV machines and low-AOV pods with no budget separation.
>
> **Solution:**
> - Consolidate: one auto discovery campaign per product family (Machine / ESE pods / Aluminum capsules / Ground coffee / Bean coffee / Adjacencies). Currently the seller is running multiple autos on the same products.
> - Restructure manual campaigns: 3-5 keywords per campaign, one match type per campaign, one target ASIN family. The seller has multiple campaigns named after the same product (Ciao 03/2026, Ciao 03/2026 Manual, Ciao M, Emachine) - these need to be merged into one well-structured campaign per product.
> - Pause and delete the test/dead campaigns: today prendi, Auto Dec, Campaign - 11/29/2024, Campaign - 2/26/2026 (all $0 spend).
>
> **Impact:** Most concrete near-term win is freeing budget from the wasted manual campaigns and pushing it through the auto + the few high-ROAS manuals. See Campaign Profitability section below for the math.

### Auto vs Manual Split

The standard Q703 report only captures a narrow slice of campaigns, but the campaign-level data confirms the picture:

| Targeting Type | Approx Spend | Approx Sales | ROAS | Notes |
|----------------|--------------|--------------|------|-------|
| Automatic (heavy: Campaign 11/13 + smaller autos) | ~$2,400 | ~$8,200 | ~3.4x | Includes the single $2,098 mega-auto |
| Manual / Product Targeting | ~$1,500 | ~$2,100 | ~1.4x | Mostly underperforming |

> **Finding: Auto is doing all the work, manual is mostly burning budget.**
>
> **Problem:** The big auto campaign (Campaign - 11/13/2025) does 3.17x ROAS at $2,098 spend. The manual campaigns are scattered across the catalog, mostly underspending and underperforming. The classic "harvest-and-scale" loop is broken: no one has identified the winning search terms inside the auto and graduated them into dedicated manual campaigns. The manuals that do exist look like guesses, not data-driven harvests.
>
> **Solution:** Pull the search term report from the big auto campaign (Campaign - 11/13/2025), identify the converting search terms, and rebuild manual exact-match campaigns around them. Then negate those terms from the auto so spend isn't duplicated.
>
> **Impact:** Manual campaigns built from harvested search terms typically achieve 30-50% better ROAS than the auto they came from, because bid control and budget are tighter. If the auto's $2,098 spend at 3.17x ROAS were partially harvested (say 30% of it, $630) and rebuilt into manuals at 4.5x ROAS, that's an extra $830 in sales from the same spend.

### Campaign Profitability

Campaigns below 1.5x ROAS with meaningful spend (≥$30) over the 90-day window:

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| Ciao 03/2026 | $302.27 | $359.00 | 1.19x | 264 | 1 |
| Beans | $165.86 | $165.33 | 1.00x | 73 | 4 |
| Can manual | $155.74 | $180.67 | 1.16x | 100 | 12 |
| Ciao 03/2026 Manual | $154.57 | $0.00 | 0.00x | 137 | 0 |
| Napoli Beans | $46.62 | $28.99 | 0.62x | 17 | 1 |
| Pods Manual | $43.46 | $0.00 | 0.00x | 12 | 0 |
| Decaf Manual | $39.64 | $70.00 | 1.77x (borderline) | 8 | 2 |
| Espresso machine | $38.80 | $0.00 | 0.00x | 42 | 0 |
| Tenerelli Manual | $38.54 | $0.00 | 0.00x | 37 | 0 |
| esp machine | $32.18 | $0.00 | 0.00x | 44 | 0 |
| **Total wasted (excl. Decaf Manual)** | **~$978** | **~$733** | **0.75x** | | |

> **Problem:** $978 of the past 90 days' spend (25% of the entire $3,916 ad budget) went to campaigns producing below break-even sales. The Ciao 03/2026 Manual campaign alone burned $154 with 137 clicks and zero orders, an alarming signal because that traffic is being driven to the P0 listing and failing to convert.
>
> **Solution:** Pause the unprofitable campaigns. Reallocate that budget to the proven winners: Capsules Automatic (9.26x), Decaf Automatic (3.84x), and the Campaign - 11/13/2025 auto (3.17x).
>
> **Impact:** $978 reallocated to the 11/13 auto at 3.17x ROAS would produce ~$3,100 in additional sales. Net improvement: ~$2,300 in sales from the same total ad spend.

### Targeting Strategy

**Keyword vs Product Targeting:**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|-------------------|--------|-------|-------|------|-----|-----|-----|
| Keyword Targeting | 1,968 | $2,424 | $7,370 | 3.04x | $75.98 | $1.23 | 4.93% |
| Product Targeting | 1,259 | $1,492 | $2,933 | 1.97x | $68.22 | $1.19 | 3.42% |

> **Finding: Product targeting is bleeding spend at sub-2x ROAS.**
>
> **Problem:** Product targeting takes 38% of the budget ($1,492) at 1.97x ROAS, well below the 3.04x ROAS keyword targeting delivers. The lower CVR (3.42% vs 4.93%) confirms that product-targeting traffic is less qualified.
>
> **Solution:** Audit the product targeting campaigns. Most likely the brand is targeting competitor ASINs without enough relevance, or is running broad category targeting that doesn't convert. Pause the lowest-ROAS product targets and reallocate to keyword campaigns. The healthy product targeting plays are: own-ASIN defensive targeting (Sponsored Display on Prendi's own listings to prevent competitor poaching) and targeting specific high-relevance competitor ASINs.
>
> **Impact:** Cutting $700 of the worst product targeting (assuming the bottom half ROAS averages 1.2x) and reallocating to keyword targeting at 3.04x ROAS adds ~$1,300 in sales at the same spend.

**Match Type Breakdown:**

| Match Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|------------|--------|-------|-------|------|-----|-----|-----|
| EXACT | 124 | $166.69 | $390.96 | 2.35x | $39.10 | $1.34 | 8.06% |
| BROAD | 83 | $147.42 | $70.00 | 0.47x | $35.00 | $1.78 | 2.41% |
| PHRASE | 54 | $87.76 | $0.00 | 0.00x | $0.00 | $1.63 | 0.00% |

> **Finding: Broad and phrase match are not paying their way.**
>
> **Problem:** Broad match has $147 spend at 0.47x ROAS (it costs more than it earns). Phrase match has $88 spend with literally zero sales over 90 days. Combined, that's $235 in spend producing $70 in sales. Exact match is the only match type pulling its weight.
>
> **Solution:** Pause broad and phrase match campaigns until a search-term harvest has been done. Restart broad/phrase only as discovery layers around proven exact-match keywords, with tight bid caps.
>
> **Impact:** $235 reallocated from broad/phrase to exact match at 2.35x ROAS would produce ~$550 in sales vs the current $70. ~$480 in incremental sales from the same spend.

### Placement

| Placement | Spend | Sales | ROAS | CTR | CVR | Orders |
|-----------|-------|-------|------|-----|-----|--------|
| Top of Search | $1,708 | $5,035 | 2.95x | 1.61% | 5.53% | 58 |
| Rest of Search | $846 | $2,765 | 3.27x | 0.48% | 6.64% | 50 |
| Product Pages | $1,354 | $2,502 | 1.85x | 0.27% | 2.28% | 32 |
| Off Amazon | $4 | $0 | 0.00x | 0.29% | 0.00% | 0 |

> **Finding: Product Pages placement is the weakest, but it gets 35% of the budget.**
>
> **Problem:** Product Pages placement (Sponsored Product placements on other product detail pages, plus Sponsored Display targeting product pages) is taking $1,354 of spend (35% of total) at 1.85x ROAS, while Top of Search delivers 2.95x ROAS with 5x higher CTR (1.61% vs 0.27%). The CVR gap is also stark: 2.28% on Product Pages vs 5.53% on Top of Search.
>
> **Solution:** Reduce Product Pages bid modifiers across all campaigns. Increase Top of Search modifiers (start at +25% and tune up if Top of Search ROAS holds). Rest of Search has the highest ROAS (3.27x) and is already efficient, push it more cautiously.
>
> **Impact:** Even a partial shift of $500 from Product Pages to Top of Search would lift sales by ~$550 ($500 × 2.95 - $500 × 1.85 = $550 in incremental sales at the same spend).

---

## Product-Level Findings (P0: Spinel Ciao Espresso Coffee Machine)

### P0 Campaign Map

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| Campaign - 11/13/2025 (auto, all products) | $590.68 (P0 share) | $2,136 | 3.62x | 519 | 6 |
| Ciao 03/2026 | $302.27 | $359 | 1.19x | 264 | 1 |
| Ciao 03/2026 Manual | $154.57 | $0 | 0.00x | 137 | 0 |
| Ciao M | $92.97 | $359 | 3.86x | 97 | 1 |
| Espresso machine | $30.21 | $0 | 0.00x | 32 | 0 |
| Emachine | $4.04 | $0 | 0.00x | 8 | 0 |
| **P0 Total** | **$1,174.74** | **$2,854** | **2.43x** | **1,057** | **8** |

P0 takes 30% of total account ad spend. The P0 listing converts at 0.76% on ad clicks (8 orders / 1,057 clicks). This is low even for an espresso machine, where 1-2% is the norm. The Step 2 listing findings (no A+ content, no video, low review count, missing key search terms in the title) are the root cause.

### Blocker Analysis

> **Primary blocker for P0: CVR (listing-side), with impression share as secondary.**
>
> **Problem (CVR):**
> - 1,057 P0 ad clicks produced 8 orders. That's 0.76% CVR on paid traffic.
> - The biggest waste is Ciao 03/2026 Manual: $154.57 spent, 137 clicks, 0 orders. Buyers see the ad, click, land on the listing, and leave. The listing is failing to close.
> - This pattern is consistent with the listing gaps identified in Step 2: no A+ content, no video, low review count (under 10), main image with a heavy watermark, title missing high-intent terms (ESE, 44mm, Made in Italy).
>
> **Solution (CVR fix first, then PPC scale):** The listing has to be fixed before more ad budget is poured into P0. The fastest CVR levers, in order of impact:
> 1. Build and publish A+ content telling the Italian heritage / Spinel manufacturing story
> 2. Add a 30-60 second product video (brewing demonstration)
> 3. Rewrite the title to include ESE, 44mm, Made in Italy
> 4. Launch Vine to push reviews above the 50-review credibility threshold
> 5. Reconsider the main image watermark
>
> **Impact:** If the listing changes lift P0 ad CVR from 0.76% to 2% (still conservative for a $350 machine with a clear value prop), at the current 1,057 P0 ad clicks per quarter the math is:
> - Current: 8 orders at $360 AOV = $2,854 sales on $1,175 spend (2.43x ROAS)
> - After: 21 orders at $360 AOV = $7,560 sales on $1,175 spend (6.43x ROAS)
> - Incremental: $4,700 in sales from listing fixes alone, before any ad spend increase.

> **Problem (Impression Share):**
> - The Ciao 03/2026 campaign generated 264 clicks at 0.70% CTR and converted 1 order on $302 spend. The product is showing up but not closing.
> - The Espresso machine and Emachine campaigns are tiny ($30 and $4). The brand is not actively bidding to win the core "ese pod espresso machine" or "italian espresso machine" queries.
>
> **Solution:** After the listing is fixed, build a dedicated exact-match manual campaign targeting the high-intent ESE queries: "ese pod espresso machine," "ese espresso machine," "44mm pod espresso machine," "italian espresso machine made in italy." Bid aggressively on Top of Search placements.
>
> **Impact (sequenced):** Once CVR is fixed, scaling impression share on Tier 1 queries should produce 2-3x the current P0 sales. Without the listing fix first, more impression share just multiplies wasted spend.

### Wasted P0 Targets

Two specific P0 campaigns to pause immediately:

| Campaign | Spend | Clicks | Orders | Reason to Pause |
|----------|-------|--------|--------|-----------------|
| Ciao 03/2026 Manual | $154.57 | 137 | 0 | 0 orders over 90 days, 137 clicks confirms statistical significance |
| Espresso machine | $30.21 | 32 | 0 | 0 orders, but small spend |
| Emachine | $4.04 | 8 | 0 | Tiny, likely a leftover test |

Pause these, reallocate to the well-performing P0 paths (Ciao M and the broader 11/13 auto), and pair with the listing fix above.

---

## Insights

- **The single biggest issue at the account level is campaign sprawl.** 46 campaigns is far too many for a brand still under $30K/month in revenue. The seller (or whoever set this up) keeps creating new campaigns rather than optimizing existing ones. Consolidating to 12-15 well-structured campaigns is a Week 1 priority.
- **P0 has decent visibility but the listing is failing to convert.** 1,057 P0 ad clicks in 90 days at 0.76% CVR is a strong signal that the listing is the bottleneck, not traffic. The listing fixes from Step 2 (A+, video, reviews, title) should sequence before more P0 ad spend.
- **Capsules Automatic and Decaf Automatic are punching above their weight.** $245 combined spend, 26 orders, 5.7x average ROAS. These two campaigns are the closest the account has to a working "harvest-ready" auto setup. Mining their search terms is the highest-leverage Week 2 task.
- **Branded defense is working but barely active.** The "Brand" campaign has $1.87 spend, 102x ROAS, 3 orders. The brand should run a slightly larger branded defense (~$30-50/month) to protect against competitor bidding on Prendi searches.

## Things to Investigate Further

- **Which search terms are driving the big 11/13/2025 auto campaign's $6,660 in sales?** Pull the search term report for that one campaign in Week 1. The winners become the manual campaign keywords for Weeks 2-4. This is the highest-leverage data pull in the entire engagement.
- **Are any of the duplicate P0 campaigns (Ciao M, Ciao 03/2026, Ciao 03/2026 Manual, Emachine, Espresso machine) bidding on the same keywords?** If so, they're competing with each other and inflating CPCs. Worth a search term audit on each.

## Questions for the Seller

- **Who has been managing the ads since February 2026 launch, and what's the campaign creation logic?** Hypothesis: campaigns were spun up ad-hoc (per product launch, per ASIN test) without a consolidated structure plan, which explains the 46-campaign sprawl.
- **What's the current monthly ad budget target?** This shapes the action plan: total spend over 90 days was $3,916 (~$1,300/month). If the goal is $3K-5K/month, the path is consolidate first, then scale. If the seller wants to push to $10K+/month, the listing fixes have to come first or the ROAS will collapse at scale.
