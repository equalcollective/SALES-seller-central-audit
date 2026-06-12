# Ad Analysis - MINT Tools

Window: 2026-01-26 to 2026-04-24 (~13 weeks, the full ad data availability for this seller).

Account totals: 144 enabled campaigns, $43,014 total spend, $158,327 total sales, account ROAS 3.68. Manual review confirms many findings the user predicted - there are several material misallocations.

## Account Level

### Campaign Structure

The account has **144 enabled campaigns** running simultaneously. Naming is well-organized by product (CI = curling iron, CW = curling wand, WAV = waver, RCI = revamp curling iron, BDB = blackbird hair dryer, CRMP = crimper, etc.). Campaign count alone isn't the problem; the issue surfaces inside specific campaigns where many keywords compete for one budget. The most spend-heavy P0 campaigns are auto campaigns (catch-all) which dilute spend across whatever Amazon decides to target. This shows up as the auto vs manual issue (next section). No single campaign is grossly overstuffed in a way that warrants a dedicated finding here.

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|--------|-------|-------|------|-----|-----|-----|
| Automatic | 22,608 | $27,562 | $99,599 | 3.61 | $94.59 | $1.22 | 4.66% |
| Manual | 9,189 | $15,452 | $58,728 | 3.80 | $99.04 | $1.68 | 6.45% |

> **Finding: Auto campaigns are running 64% of total ad spend, which is the inverse of the healthy pattern.**
>
> **Problem:**
> - Auto: $27,562 spend (64% of total) at ROAS 3.61, CVR 4.66%
> - Manual: $15,452 spend (36%) at ROAS 3.80, CVR **6.45%**
> - Manual converts 38% better than auto, yet gets half the budget
> - Auto is meant for discovery (small slice). The healthy split is roughly Manual 70% / Auto 30%
>
> **Solution:**
> - Mine auto-campaign search terms for converting queries (Q717 already shows clear winners like "long barrel curling iron 1.5 inch" at ROAS 5.85, "1 1/4 inch curling iron" at ROAS 4.25)
> - Move winning terms into dedicated manual campaigns with controlled bids and budget
> - Negate harvested terms from auto so spend doesn't double-count
>
> **Impact:** If we shift $10,000 from auto to manual at the current ROAS gap (3.61 → 3.80) the immediate ROAS lift is small, but the structural lift is much bigger because manual lets us bid up Top of Search (which has ROAS 3.70 vs Product Pages at 1.31 - see placement section). Realistic 90-day impact: account ROAS 3.65 → 4.0+, with $20-30K incremental sales at the same total ad budget.

### Campaign Profitability

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| RCI1 - SP - EX - 1 inch curling iron | $850 | $1,000 | 1.18 | 313 | 10 |
| RCI15 - SP - EX - HV - 1 | $394 | $510 | 1.29 | 149 | 5 |
| BDB - SP - PH (2) | $320 | $340 | 1.06 | 275 | 5 |
| CI125 - SP - EX - HV - 1 | $150 | $0 | 0.00 | 59 | 0 |
| KAZ40 - SP - AUTO - 2 - B0CHTXM2TN | $117 | $70 | 0.60 | 94 | 1 |
| CW1 - SP - EX - HV - 1 - B0CXQ837DR | $51 | $0 | 0.00 | 38 | 0 |
| BDB - SP - PH (4) | $46 | $0 | 0.00 | 46 | 0 |
| CW125 - SP - BR - 1 - B0CXQ7K11T | $41 | $0 | 0.00 | 35 | 0 |
| BDB - SP - EX (2) | $40 | $0 | 0.00 | 31 | 0 |
| **Total wasted** | **$2,009** | **$1,919** | | | |

> **Problem:** 9 campaigns with meaningful click volume (30+ clicks) are running below 1.5x ROAS. Combined waste: $2,009 over ~90 days. Most are exact-match campaigns (the match type that should have the BEST ROAS), and most are on the new 2026 REVAMP curling iron (RCI*) which is launching with poor conversion.
>
> **Solution:** Pause the four campaigns with 0 sales (CI125 EX, CW1 EX, BDB PH 4, CW125 BR, BDB EX 2). Restructure the RCI exact-match campaigns - either bid down significantly or pause until the REVAMP listing has more reviews and converts better.
>
> **Impact:** Reallocating $2,000 to the highest-ROAS campaigns (e.g., the WAV phrase campaign at ROAS 8.80, "MINT_Curling Wand" at 8.80) would generate ~$16,000 in sales vs the current $1,919. Net swing: ~$14K in 90 days, $56K annualized.

### Targeting Strategy

**Keyword vs Product Targeting:**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|-------------------|--------|-------|-------|------|-----|-----|-----|
| Keyword Targeting | 30,785 | $45,374 | $147,319 | 3.25 | $93.36 | $1.47 | 5.13% |
| Product Targeting | 5,339 | $6,411 | $35,018 | **5.46** | $109.43 | $1.20 | 5.99% |

> **Finding: Product Targeting is 68% more efficient than Keyword Targeting but receives only 12% of spend.**
>
> **Problem:** Product targeting (placing your ad on competitor product pages or category pages) runs at ROAS 5.46 vs 3.25 on keyword targeting - a 68% efficiency advantage. AOV is also higher ($109 vs $93). Yet only 12% of ad budget goes to product targeting.
>
> **Solution:** Build out product targeting campaigns. Two specific plays:
> 1. **Defensive product targeting:** Run Sponsored Product ads on MINT's own listings to capture customers landing on the page (prevents competitor poaching, especially given the 75% buy box on P0)
> 2. **Offensive product targeting:** Bid on competitor curling iron ASINs (Bio Ionic, Hot Tools, T3 entry-level models) - SQP already shows MINT poaches Bio Ionic searchers organically (2.3% impression share on "bio ionic long barrel curling iron 1.25"); product targeting can scale that pattern
>
> **Impact:** Shifting $5,000 from keyword to product targeting at current ROAS levels = $27,300 in sales (at 5.46 ROAS) vs $16,250 (at 3.25 ROAS) = **+$11,050 in 90 days**. Annualized: ~$45K.

**Match Type Breakdown:**

| Match Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|------------|--------|-------|-------|------|-----|-----|-----|
| EXACT | 2,521 | $5,141 | $10,503 | **2.04** | $96.35 | $2.04 | **4.32%** |
| PHRASE | 5,291 | $9,256 | $35,137 | 3.80 | $98.15 | $1.75 | 6.77% |
| BROAD | 5,108 | $8,785 | $34,962 | 3.98 | $98.48 | $1.72 | 6.95% |

> **Finding: Exact match underperforms phrase and broad - the inverse of the healthy pattern.**
>
> **Problem:** Exact match should have the highest ROAS (most targeted, most refined). Instead, EXACT runs at ROAS 2.04 vs 3.80 (PHRASE) and 3.98 (BROAD). CPC on exact is also the highest ($2.04). CVR on exact is 4.32% vs 6.77-6.95% on phrase and broad.
>
> **What this tells us:** The exact-match keywords currently being targeted are wrong. Either:
> 1. The seller picked exact keywords without looking at search term data (guessed at keywords vs harvested), OR
> 2. The harvest-and-scale loop isn't running - winning terms from broad/phrase haven't been moved to exact yet, AND/OR
> 3. The exact campaigns are bidding on terms that are too generic (e.g., "curling iron" exact match - confirmed in search term data, "curling iron" exact has $460 spend at 0.98 ROAS)
>
> **Solution:**
> - Pause or significantly reduce bids on under-performing exact campaigns. Specifically: "curling iron" exact (head term, no intent), generic single-size exacts that are competing with the brand's own broad/phrase campaigns
> - Run the harvest loop monthly: pull last 30 days of broad/phrase winners (>3x ROAS, 20+ clicks), promote to exact in dedicated campaigns
> - Use Step 4f search terms below as the starting list for harvested keywords
>
> **Impact:** If exact match ROAS rises from 2.04 to even 3.5 (still below phrase/broad), the same $5,141 in spend would generate $18,000 vs $10,500 = **+$7,500 in 90 days**.

## Product Level (P0 = Curling Irons B07RM2VQ77)

### P0 Campaign Map

P0 (Curling Irons B07RM2VQ77 + 3 children) is being advertised across **20+ campaigns** totaling $14,859 spend over the 90-day window. That's 35% of the entire account's ad spend going to the hero product, which is appropriate.

| Top P0 Campaigns (by spend) | Spend | Sales | ROAS | Clicks | Orders |
|------------------------------|-------|-------|------|--------|--------|
| CI15 - SP - AUTO - ALL | $3,235 | $7,841 | 2.42 | 1,809 | 84 |
| CI125 - AUTO - ALL | $1,540 | $4,507 | 2.93 | 1,072 | 47 |
| CI15 - SP - BR - AL - B07Q7GF2YS | $1,489 | $6,128 | 4.12 | 661 | 66 |
| CI1 - SP - PH - HV - high likelihood 25 | $1,098 | $3,304 | 3.01 | 511 | 34 |
| CI125 - PH - Branded - B07Q8KY243 | $833 | $6,541 | 7.85 | 295 | 66 |
| CI15 - SP - BR - MKW - 1 - B07Q7GF2YS | $652 | $3,204 | 4.92 | 252 | 33 |
| CI1 - SP - MKW - LV2 - BR - 1 | $616 | $1,150 | 1.87 | 350 | 12 |
| CI1 - SP - AUTO - ALL | $477 | $638 | 1.34 | 273 | 7 |
| CI125 - SP - AUTO | $374 | $2,389 | 6.40 | 215 | 23 |
| CI1 - SP - MKW - LV3 - EX - 1 | $298 | $210 | **0.70** | 104 | 2 |
| **P0 totals (B07RM2VQ77)** | **$11,500+** | **$36,000+** | **3.13 avg** | | |

Plus another ~$2,706 spent on the 2026 REVAMP (RCI*) campaigns at ROAS 1.18-1.95 (mostly losing).

P0 ROAS is 3.13 average, just above the account average of 3.68 but not great for the hero product. The auto campaigns (CI15-AUTO-ALL, CI125-AUTO-ALL, CI1-AUTO-ALL) are absorbing $5,250 at ROAS 1.34-2.93 - significantly below the manual broad campaigns on the same product (4.12-4.92 ROAS).

### Blocker-Specific Findings

#### CVR Blocker: Placement Distribution

Step 3 identified CVR as the immediate blocker (3.71% vs 13.10% industry on Tier 1). One PPC lever for CVR is shifting spend toward placements that convert better. Here's the data:

| Placement | Spend | Sales | ROAS | CTR | CVR |
|-----------|-------|-------|------|-----|-----|
| Top of Search | $13,054 | $48,291 | **3.70** | **5.18%** | **5.59%** |
| Rest of Search | $21,717 | $42,628 | 1.96 | 0.41% | 3.07% |
| Product Pages | $16,870 | $22,167 | **1.31** | 0.19% | 1.96% |
| Off Amazon | $119 | $94 | 0.80 | 0.34% | 0.26% |

> **Finding: Top of Search has 2.8x the ROAS of Product Pages but receives less spend.**
>
> **Problem:**
> - Top of Search: ROAS 3.70, CTR 5.18%, CVR 5.59% - the premium placement, performing as expected
> - Product Pages: ROAS **1.31** (unprofitable), CTR 0.19%, CVR 1.96% - bleeding budget
> - Currently 30% of spend on Top of Search vs 39% on Product Pages
> - Product Pages alone is wasting roughly $3,500-4,000 over 90 days at sub-1.5x ROAS
>
> **Solution:**
> - Increase Top of Search bid modifier by 50-100% on top P0 campaigns (especially CI15-AUTO and CI125-AUTO which collectively spent $4,775)
> - Reduce or zero out Product Pages bid modifier on campaigns where it's running at sub-2x ROAS (most of them)
> - Re-allocate the Product Pages spend toward Top of Search and to the high-ROAS manual campaigns flagged earlier
>
> **Impact:** Shifting $5,000 from Product Pages (ROAS 1.31) to Top of Search (ROAS 3.70):
> - Lose: $5,000 × 1.31 = $6,550 in sales
> - Gain: $5,000 × 3.70 = $18,500 in sales
> - **Net gain: $11,950 in 90 days. Annualized: ~$48K.**
>
> Note: This won't fix the underlying CVR vs industry gap (which is mostly the buy box issue from Step 2). It will redirect existing spend to a placement that already converts better. The buy box fix from Step 1 is what closes the gap to industry CVR.

#### Impression Share Blocker (Secondary): Tier 1 Search Term Spend

Step 3 also flagged impression share as the long-term ceiling on Tier 1 (0.76% vs 30%+ cap). The PPC lever is bidding on the Tier 1 keywords. The data shows the seller IS bidding on the right terms - the issue is conversion, not coverage:

| Search Term | Tier | Spend | Sales | ROAS | Clicks | Orders |
|-------------|------|-------|-------|------|--------|--------|
| long barrel curling iron | Tier 1 | $791 | $1,168 | 1.48 | 370 | 12 |
| 1.5 inch curling iron | Tier 1 | $676 | $1,455 | 2.15 | 306 | 16 |
| 1 inch curling iron | Tier 1 | $595 | $798 | 1.34 | 237 | 8 |
| curling iron 1 1/2 inch | Tier 1 | $497 | $960 | 1.93 | 284 | 10 |
| 1 1/2 inch curling iron | Tier 1 | $398 | $675 | 1.70 | 155 | 7 |
| long barrel curling iron 1.25 | Tier 1 | $271 | $570 | 2.10 | 121 | 6 |
| long barrel curling iron 1.5 inch | Tier 1 | $191 | $1,120 | **5.85** | 77 | 12 |
| 1 1/4 inch curling iron | Tier 1 | $137 | $580 | **4.25** | 67 | 6 |
| 1.25 inch curling iron | Tier 1 | $162 | $375 | 2.32 | 83 | 4 |

> **Finding: Tier 1 keywords are funded but converting at 1.3-2.3 ROAS. The PPC isn't the blocker on Tier 1 visibility - the listing's CVR is the blocker (per Step 3). The ad data confirms: even with right keywords + meaningful spend, conversion is poor.**
>
> A few specific terms (long barrel 1.5 inch, 1 1/4 inch curling iron) ARE converting at 4-6x ROAS. These are the harvest-and-scale candidates - move to dedicated exact-match campaigns with higher bids.
>
> **Solution path:** Don't scale Tier 1 spend until the buy box and CVR are fixed (Step 1 + listing-side actions). Once those land, return and 2-3x the spend on the long-barrel + sized variant terms.
>
> **Impact at full unlock:** Tier 1 represents a $22M/year market, MINT is at <1% share. If the seller can get to industry CVR (13.10%) at even 2x current impression share (1.5% from 0.76%), Tier 1 contribution would roughly triple. But this is contingent on the buy box and listing fixes; PPC alone won't deliver it.

#### Wasted Spend on Irrelevant Search Terms

| Search Term | Spend | Sales | ROAS | Note |
|-------------|-------|-------|------|------|
| beach waver | $248 | $189 | **0.76** | Bidding on Beach Waver competitor brand - they don't switch. Negate. |
| curling iron (head term) | $460 | $450 | **0.98** | Pure head term, no intent qualifier. Money-losing. Negate or move to Tier 2 manual exact only. |
| 1 inch curling wand | $137 | $98 | **0.72** | Wrong product (wand, not iron). Negate from iron campaigns. |
| 1 inch curling wand long barrel | $134 | $98 | **0.73** | Same. Negate. |

Combined immediate negation savings: ~$979 over 90 days = ~$3,900/year reallocated to profitable terms.

## Insights

- **The biggest single ad lever is placement reallocation.** Top of Search ROAS 3.70 vs Product Pages ROAS 1.31 with 39% of spend on the worse placement = ~$48K/year recoverable just by shifting bid modifiers. This is independent of any listing change.
- **The auto campaigns are doing the heavy lifting because the harvest loop isn't running.** $27.5K of $43K total spend is in auto. If the seller's agency or in-house team had been mining auto search terms monthly and promoting to manual, this ratio would have flipped by now.
- **Product targeting is dramatically under-deployed.** 5.46x ROAS at 12% of budget is the most surprising finding - virtually no other lever in the audit has this kind of efficiency gap.

## Things to Investigate

- **The 2026 REVAMP curling iron is being heavily ad-supported but converting poorly** ($2,706 spent, ROAS ~1.4 average). The product is 4 months old with low review count, so this might be expected - but at this ROAS the seller is essentially paying to acquire reviews. Worth checking ROI math against the implied review acquisition cost.
- **Why is "BDB" (Blackbird Dryer) running 4 separate campaigns at 0 sales?** The hair dryer (B07Q5QM81X) generates organic sales each month - the ad campaigns specifically are dead. Likely setup error.

## Questions for the Seller

- Are you currently running the auto-to-manual harvest loop? If yes, when was it last done and what tooling? The 64% auto / 36% manual split suggests it's been a while.
- Top of Search bid modifier on the curling iron campaigns - what's it currently set to? The data implies it's either off or low. We'd recommend pushing to 75-100%.
