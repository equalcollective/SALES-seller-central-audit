# Step 4: Ad Analysis - NutriGardens

**Date range:** Feb 6 - May 5 2026 (89 days, full ad data window).

**Account headline:** $1,843 total ad spend / $9,647 ad sales / **ROAS 5.24** across 22 campaigns.

## Account-Level Analysis

### Campaign Structure

Campaign count is high (22 campaigns) for a 2-product catalog, and 12 of them are "SI -" prefixed inactive/zombie campaigns spending under $10 each (likely artifacts from a prior agency setup). The structure isn't overstuffed in the classic sense (most active campaigns have 11-16 targets, which is reasonable for broad discovery), but there is meaningful cleanup work to consolidate scope.

The two highest-spend manual campaigns ("Exact - Isolation - Conversions - RS400" and "Exact - Isolation - Conversions - VitaSpinach", $525 and $465 respectively, 11 targets each) carry the workhorse exact-match traffic, but at modest ROAS (3.84 and 2.75). Splitting them by intent (Tier 1 hero terms separated from broader supplement terms) is a candidate for a Week 2-3 optimization.

Action: clean up the 12 zombie "SI -" campaigns, then split the two workhorse exact campaigns by tier.

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|--------|-------|-------|------|-----|-----|-----|
| Automatic | 226 | $180.26 | $3,337.00 | **18.51** | $55.62 | $0.80 | 26.55% |
| Manual | 768 | $1,625.12 | $6,270.45 | 3.86 | $50.57 | $2.12 | 16.15% |

> **Finding: The auto/manual split is inverted. Auto is generating 35% of revenue with 10% of spend at ROAS 18.51, while manual is running at ROAS 3.86.**
>
> **Problem:**
> - Auto's ROAS is 4.8x higher than manual's. CVR is 26.5% vs 16.1%. CPC is one-third manual's.
> - Auto's hero ("Automatic Campaign - 11/28/2025") alone did $2,678 in sales on $147 spend (ROAS 18.21). That's a single campaign outperforming the rest of the account.
> - This pattern means Amazon's algorithm has found converting search terms inside auto that have never been harvested into dedicated manual campaigns. The high-converting traffic is being subsidized by limited auto budget instead of being scaled in manual.
>
> **Solution:**
> - Mine the auto campaign search term reports, identify the top 5-10 converters, and launch dedicated manual exact campaigns with controlled bids.
> - Negate those terms from auto so spend isn't duplicated.
> - Scale auto budget moderately in parallel (it's leaving money on the table at $180 over 3 months).
>
> **Impact:**
> - Conservative case: doubling auto spend (to ~$360 over 3 months) at half its current ROAS efficiency (~ROAS 9) adds $1,440 in incremental sales.
> - The bigger lever is moving the top converting auto search terms to manual exact at ROAS 8-10. Expected uplift: $3,000-5,000 additional sales over the next 3 months at the current ad budget.

### Campaign Profitability

Unprofitable or borderline-unprofitable campaigns (below ~1.5x ROAS with meaningful spend):

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| Campaign with presets - B0C6QJM2MG | $31.26 | $39.95 | 1.28 | 8 | 1 |
| SI - SP - red spinach - BA kws - broad | $365.24 | $619.25 | 1.70 | 72 | 14 |
| PT - Exact - VitaSpinach | $40.58 | $79.90 | 1.97 | 35 | 2 |
| **Total** | **$437.08** | **$739.10** | | | |

> **Finding: ~$437 of spend over the 89-day window is going to campaigns below or near the 1.5x ROAS floor.**
>
> **Problem:**
> - "SI - SP - red spinach - BA kws - broad" is the biggest drag: $365 in spend for $619 in sales (ROAS 1.70). This is a broad-match keyword campaign that has not been refined - it's catching irrelevant traffic.
> - "PT - Exact - VitaSpinach" (product targeting on competitor ASINs) hasn't converted well.
> - "Campaign with presets" is an Amazon default auto campaign that is being out-performed by the better-built "Auto - Discovery - VitaSpinach" (ROAS 23.17 on $26 spend).
>
> **Solution:**
> - Pause "Campaign with presets - B0C6QJM2MG" (the better Auto - Discovery campaign is already in place).
> - For "SI - SP - red spinach - BA kws - broad": negate non-converting search terms (see Search Term section below), then re-evaluate. If still under-performing after 2 weeks, pause.
> - Re-evaluate "PT - Exact - VitaSpinach" targets - product targeting on the wrong competitor ASINs is the most likely cause.
>
> **Impact:**
> - $437 reallocated to the auto hero ("Automatic Campaign - 11/28/2025") at its current 18.2 ROAS = ~$7,950 in additional sales. Realistically with diminishing returns at 50% efficiency: **~$4,000 additional sales over a 3-month window** from the same total ad budget.

### Targeting Strategy

**Keyword vs Product Targeting:**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|-------------------|--------|-------|-------|------|-----|-----|-----|
| Keyword Targeting | 922 | $1,768.41 | $9,187.90 | 5.20 | $52.50 | $1.92 | 18.98% |
| Product Targeting | 81 | $74.35 | $459.50 | 6.18 | $45.95 | $0.92 | 12.35% |

Product targeting is a tiny share of spend (4%) with marginally better ROAS but worse CVR. Not a material lever right now. Note for later: if VitaSpinach's "PT - Exact" campaign is restructured, product targeting could be tested more aggressively against the established beet-root brands (Force Factor, KOS, Snap, ONNIT) where defensive PT can poach price-comparison shoppers.

**Match Type Breakdown:**

| Match Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|------------|--------|-------|-------|------|-----|-----|-----|
| EXACT | 600 | $1,148.82 | $4,532.30 | 3.95 | $50.92 | $1.91 | 14.83% |
| BROAD | 120 | $445.33 | $1,458.45 | 3.27 | $50.29 | $3.71 | 24.17% |
| PHRASE | 6 | $7.42 | $119.85 | 16.15 | $39.95 | $1.24 | 50.00% |

> **Finding: Exact match is the dominant spend but only marginally outperforms broad on ROAS (3.95 vs 3.27). Broad converts at a higher rate (24% CVR) but at 1.9x the CPC, eroding ROAS.**
>
> The classic "harvest-and-scale" pattern says broad should be a discovery channel feeding exact. Here, broad's high CVR signals that broad is finding good search terms, but they aren't being moved to exact match (where bidding could be tighter and CPC lower). The same root cause as auto vs manual: harvesting isn't happening.

### Placement Performance (where ads appear)

| Placement | Impressions | Clicks | CTR | Spend | Sales | ROAS | CVR |
|-----------|------------|--------|-----|-------|-------|------|-----|
| Top of Search | 6,407 | 722 | **11.27%** | $1,034.84 | $7,529.45 | **7.28** | 20.22% |
| Rest of Search | 12,673 | 113 | 0.89% | $197.71 | $799.25 | 4.04 | 12.39% |
| Product Pages | 71,568 | 167 | **0.23%** | $607.68 | $1,318.70 | **2.17** | 14.97% |

> **Finding: Top of Search is dramatically better at every funnel stage, but Product Pages is burning a third of spend at ROAS 2.17.**
>
> **Problem:**
> - Top of Search CTR is 11.27%, Product Pages CTR is 0.23%. That's a 49x gap. ToS is also the highest-converting placement (CVR 20.2%) and the highest-ROAS (7.28).
> - Product Pages absorbs $607 (33% of total spend) but generates only $1,319 in sales (14% of total sales). At ROAS 2.17, it's marginally profitable but is the wrong place to put incremental spend.
> - ToS impressions are tiny relative to Product Pages (6,407 vs 71,568, an 11x gap). The placement bid modifiers are skewed away from where the conversion is happening.
>
> **Solution:**
> - Increase Top of Search bid modifier (likely +50% to +100%) on the high-spend P0 campaigns to shift impression share toward ToS.
> - Reduce Product Pages bid adjustment to zero or near-zero on campaigns where ToS is converting (we're not using product pages strategically for ASIN defense; this spend is incidental).
> - The auto campaigns are likely contributing most of the Product Pages exposure (auto targets close/loose/substitute/complement product ASINs by default).
>
> **Impact:**
> - Shifting $300 from Product Pages (ROAS 2.17) to Top of Search (ROAS 7.28) generates $1,533 in additional sales over the same 89-day window at the same total budget.
> - This is a near-deterministic move because the ROAS differential is large and consistent across campaigns.

## Product-Level Analysis (P0 - RS400)

### P0 Campaign Map

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| Exact - Isolation - Conversions - RS400 | $525.43 | $2,015.25 | 3.84 | 233 | 33 |
| Automatic Campaign - 11/28/2025 | $147.07 | $2,677.75 | **18.21** | 153 | 45 |
| Broad - Discovery - RS400 | $23.48 | $579.50 | **24.68** | 23 | 9 |
| PT - Exact - RS400 | $20.35 | $119.90 | 5.89 | 16 | 2 |
| Exact - Staging - RS400 | $17.24 | $199.80 | 11.59 | 12 | 4 |
| Exact - Isolation - RS400 | $7.60 | $119.90 | 15.78 | 4 | 1 |
| Auto - Discovery - RS400 | $7.33 | $59.95 | 8.18 | 15 | 1 |
| **RS400 Total** | **$748.50** | **$5,772.05** | **7.71** | 456 | 95 |

P0 absorbs 41% of total ad spend ($748 of $1,843) and generates 60% of ad sales ($5,772 of $9,647). RS400 punches well above its budget share. Auto campaigns plus the "Broad - Discovery" are the high-ROAS leaders at 18-25 ROAS, but combined they spend only $178. The "Exact - Isolation - Conversions" workhorse takes 70% of P0's spend at the lowest ROAS in the P0 set.

### Impression Share Blocker: Tier 1 Keyword Spend

Section 4 (SQP) identified **impression share as the primary blocker on Tier 1** (6.3% vs ~16-18% catalog-adjusted cap). The PPC lever is bidding on the keywords where impression share is low. Here is the spend per Tier 1 search term (89 days):

| Search Term | Tier | Spend | Sales | ROAS | Clicks | Orders | CVR |
|-------------|------|-------|-------|------|--------|--------|-----|
| red spinach extract | T1 | $369.77 | $1,995.05 | 5.40 | 191 | 37 | 19.4% |
| red spinach supplement | T1 | $202.40 | $359.60 | 1.78 | 78 | 8 | 10.3% |
| red spinach | T1 | $140.67 | $1,178.75 | **8.38** | 141 | 25 | 17.7% |
| red spinach powder | T1 | $59.24 | $119.85 | 2.02 | 27 | 2 | 7.4% |
| red spinach extract powder | T1 | $24.98 | $239.75 | **9.60** | 19 | 5 | 26.3% |
| red spinach extract capsules | T1 | $6.25 | $59.95 | 9.59 | 4 | 1 | 25.0% |
| best red spinach supplement | T1 | $3.56 | $39.95 | 11.22 | 3 | 1 | 33.3% |
| 400mg nitrate | T1 | $6.79 | $0.00 | 0.00 | 5 | 0 | 0% |
| red spinach supplements | T1 | $9.74 | $0.00 | 0.00 | 5 | 0 | 0% |
| red spinach nitric oxide supplement | T1 | $7.09 | $0.00 | 0.00 | 4 | 0 | 0% |

> **Finding: Tier 1 keywords are massively underfunded relative to their ROAS, except for "red spinach extract" which is the only one getting real budget.**
>
> **Problem:**
> - "red spinach" at ROAS 8.38 with $141 spend - this should be ~3x the budget. Clear scaling opportunity.
> - "red spinach extract powder" at ROAS 9.60 with $25 spend - dramatically underfunded.
> - "best red spinach supplement" and "red spinach extract capsules" both above 9x ROAS on under $10 spend each.
> - "red spinach supplement" at ROAS 1.78 needs a different look - it's the only Tier 1 term losing money. CVR is 10.3% (still acceptable), but CPC is $2.59 which is high. Bidding too aggressively.
>
> **Solution:**
> - Increase bids on "red spinach", "red spinach extract powder", "red spinach extract capsules" (intent mismatch with our powder product, but converted - format-agnostic shoppers), and "best red spinach supplement" (high-intent).
> - For "red spinach supplement": reduce bid to bring CPC under $1.80 and re-evaluate.
> - Add "400mg nitrate" and "red spinach supplements" as targets in dedicated campaigns - they have brand impressions but are not converting yet, likely a listing/CVR signal worth watching as scale grows.
>
> **Impact:**
> - "red spinach" alone: doubling spend to $280 at ROAS 7 (slight efficiency loss from 8.38) = $1,960 sales, $782 incremental over the current $1,179.
> - "red spinach extract powder" doubling to $50 at ROAS 8 = $400 sales, $160 incremental.
> - Combined across the under-funded T1 winners: **~$1,500-2,000 incremental sales over 89 days** with disciplined bid increases.
> - This directly addresses the impression share blocker. Tier 1 impression share rising from 6.3% toward the ~16% adjusted cap means proportionally more purchase share (currently 27.4% at 6.3% impression share - room for substantial upside).

### Wasted Search Term Spend (Negate List)

Across the account, ~$200 of spend over 89 days went to search terms with 0 orders. These should be added as negative keywords:

| Search Term | Spend | Clicks | Reason |
|-------------|-------|--------|--------|
| spinach | $36.18 | 5 | Vegetable intent (industry ATC rate 89%, not supplement) |
| spinach supplement | $28.87 | 6 | Too broad, intent unclear |
| spinach powder organic | $26.20 | 4 | Vegetable-leaning intent |
| nitric oxide powder | $22.90 | 7 | Tier 2 test, didn't convert at brand's price |
| organic spinach powder | $18.41 | 3 | Vegetable-leaning |
| beet it sport nitrate 400 shot | $16.01 | 6 | Competitor brand product (Beet It Sport) |
| beetroot supplement | $12.00 | 4 | Tier 2 test, didn't convert |
| oxystorm ruby spinach extract | $9.30 | 10 | Competitor variant, 10 clicks no conversion is a quality signal |

> **Solution:** Add the top 6 as exact-match negatives across all P0/VitaSpinach campaigns. Add "spinach" alone as a phrase negative on broad/auto campaigns to block vegetable intent.
>
> **Impact:** ~$170 saved over the next 89 days. Modest dollar amount, but the more important impact is cleaner data on Tier 2/competitor terms once they're isolated.

## Insights

- **The single biggest finding is auto outperforming manual by 4.8x ROAS, with the auto hero ("Automatic Campaign - 11/28/2025") doing $2,678 in sales on $147 spend.** The harvest-and-scale loop has not been closed. Mining auto's search terms into dedicated manual campaigns is the highest-impact Week 1 action.
- **Top of Search is the right placement, but the bid modifiers are skewed.** ToS converts at ROAS 7.28 with $1,035 spend, Product Pages converts at ROAS 2.17 with $608 spend. Shifting $300 of Product Pages budget to ToS is near-deterministic upside.
- **Tier 1 keywords (P0) are converting at 8-10 ROAS but receiving low spend across the board, except "red spinach extract".** This is the direct PPC lever for the impression share blocker identified in Section 4 (SQP).
- **Branded spend on RS400 is healthy and not bloated.** "rs400" related terms are getting $44 combined spend at ROAS 23-39. This is appropriate defensive branded coverage. Not a growth lever, but no fix needed.

## Things to Investigate

- **Auto campaign search term report (granular).** Need to know exactly which terms inside "Automatic Campaign - 11/28/2025" are driving the 18 ROAS so we can isolate and scale them. Will be the first action in Week 1.
- **Why VitaSpinach gets 60% of ad spend at half the ROAS of RS400.** This is more of a capital allocation question already covered in Step 1, but the ad data confirms the issue and amplifies it.

## Questions for the Seller

- Are you currently the one managing these campaigns, or is there an agency / freelancer involved? The "SI -" prefixed campaigns look like prior agency artifacts that haven't been cleaned up. Want to confirm before we propose pausing.
- The auto campaign from Nov 28 2025 is your highest performer by ROAS. Was that intentionally set up alongside the RS400 launch, and do you know what search terms are converting inside it.
