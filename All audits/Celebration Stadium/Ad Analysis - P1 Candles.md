# Ad Analysis - Celebration Stadium (P1: 100 Tall Gold Birthday Candles)

**Analysis period:** December 27, 2025 to March 25, 2026 (89 days of ad data)
**Note:** Account-level analysis (campaign structure, auto vs manual, profitability, targeting strategy) was covered in the P0 Ad Analysis and applies to the full account. This file focuses exclusively on P1 product-level findings.

## P1 Campaign Map

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| SP - Auto - Catch All - Top 5 ASINs | $1,117 | $4,889 | 4.37 | 832 | 86 |
| SP - SKW - Broad - gold birthday candles | $307 | $602 | 1.96 | 191 | 12 |
| SP - KW - Phrase - Gold Candles | $111 | $199 | 1.79 | 53 | 5 |
| SP - SQP - KW - Broad - Tall Gold Candles MAG 2 | $65 | $170 | 2.60 | 52 | 3 |
| SP - ASIN - COMP - Exact - Tall Gold Candles | $66 | $80 | 1.21 | 84 | 2 |
| SP - KW - Phrase - Gold Birthday Candle (Scavenger) | $59 | $40 | 0.68 | 75 | 1 |
| SP - SQP - KW - Broad - Tall Gold Candles MAG 3 | $49 | $0 | 0.00 | 56 | 0 |
| SP - KW - Broad Mod - Tall Gold Candles MAG 2 | $37 | $40 | 1.08 | 40 | 1 |
| SP - SQP - KW - Phrase - Tall Gold Candles MAG 2 | $36 | $0 | 0.00 | 37 | 0 |
| SP - Auto - Substitutes - Gold Candles | $35 | $80 | 2.26 | 51 | 2 |
| SP - STR - KW - Exact - Tall Gold Candles MAG 2 | $30 | $159 | 5.24 | 30 | 3 |
| SP - KW - Phrase - Tall Gold Candles MAG 1 | $30 | $210 | 6.95 | 37 | 4 |
| All other P1 campaigns (20+) | $164 | $319 | 1.95 | 224 | 8 |
| **P1 Total** | **$2,206** | **$6,787** | **3.08** | **1,862** | **127** |

P1 consumes 33% of total account ad spend ($2,206 of $6,606) but generates 47% of ad sales ($6,787 of $14,429). The auto catch-all alone drives 72% of P1 ad revenue.

**Critical observation:** There are 30+ campaigns targeting P1, but a single auto catch-all generates more sales ($4,889) than all manual campaigns combined ($1,898). This is the clearest signal that the harvest-and-scale loop has not happened.

## Impression Share Blocker: Search Term Spend vs Tier 1/2 Queries

Section 3 (SQP) identified impression share as the primary blocker on Tier 1 (1.26% of ~8-9% max) with above-industry CVR. The PPC lever is bidding on the queries where impression share is low. Here is what the ad data shows:

### Auto Catch-All: The Hidden Gold Mine

The auto campaign has already discovered the winning search terms. Here are the top performers:

| Search Term | Tier | Spend | Sales | ROAS | Clicks | Orders |
|-------------|------|-------|-------|------|--------|--------|
| birthday candles | P1 Tier 2 | $149 | $742 | 4.98 | 78 | 16 |
| gold birthday candles | P1 Tier 1 | $49 | $867 | 17.69 | 26 | 13 |
| gold candles | Adjacent | $17 | $355 | 21.09 | 11 | 4 |
| slow burning birthday candles | P1 Tier 3 | $9 | $180 | 19.51 | 4 | 2 |
| candle birthday | Adjacent | $9 | $40 | 4.58 | 6 | 1 |
| **Total converting** | | **$233** | **$2,183** | **9.37** | **125** | **36** |

And the top wasted spend in the same campaign:

| Search Term | Spend | Sales | Clicks | Orders | Issue |
|-------------|-------|-------|--------|--------|-------|
| b00b51budo (ASIN) | $78 | $0 | 68 | 0 | Non-converting competitor ASIN |
| b08x6lyl5v (ASIN) | $59 | $0 | 40 | 0 | Non-converting competitor ASIN |
| b00hw59wku (ASIN) | $52 | $0 | 38 | 0 | Non-converting competitor ASIN |
| number candle holder set | $28 | $0 | 16 | 0 | Wrong product intent |
| birthday candles for cake | $23 | $0 | 10 | 0 | Non-converting |
| 60th birthday decorations | $16 | $0 | 6 | 0 | Milestone decoration (not capturable) |
| 50th birthday decorations | $15 | $0 | 8 | 0 | Milestone decoration (not capturable) |
| tall birthday candles | $14 | $0 | 7 | 0 | Non-converting |
| sparkler candles | $10 | $0 | 9 | 0 | Different product type |
| firework candles for cake | $10 | $0 | 7 | 0 | Different product type |
| **Total wasted** | **$305** | **$0** | **209** | **0** | |

> **Finding: $305 wasted on non-converting terms in the auto campaign, while $233 on converting terms generates $2,183 in sales**
>
> **Problem:**
> - The auto catch-all has found the winning formula: "birthday candles" at 4.98 ROAS (16 orders) and "gold birthday candles" at 17.69 ROAS (13 orders)
> - But these winners share budget with $188 in completely wasted ASIN targeting (b00b51budo, b08x6lyl5v, b00hw59wku: combined 146 clicks, zero orders) and $117 in non-converting keyword terms
> - The winners are being starved of budget because the auto campaign's daily budget is split across all targets including the losers
>
> **Solution:**
> - Harvest: Create dedicated manual exact campaigns for "birthday candles" and "gold birthday candles" with their own budgets
> - Negate: Add these terms as negative exact matches in the auto campaign to avoid duplicate spend
> - Clean: Negate the 3 wasted ASINs (b00b51budo, b08x6lyl5v, b00hw59wku) and irrelevant keyword terms from auto
> - Expand: Create a "birthday candles bulk" campaign targeting B2B queries identified in SQP (2,366/mo search volume, 54 brand clicks, currently no dedicated campaign)
>
> **Impact:**
> - "gold birthday candles" currently generates $867 from just $49 spend (17.69 ROAS). Scaling to $200/month in a dedicated campaign, even at a conservative 10x ROAS, would yield $2,000/month in additional sales
> - "birthday candles" at 4.98 ROAS generates $742 from $149 spend. Scaling to $400/month at 4x ROAS would yield $1,600/month in additional sales
> - Negating $305 in wasted auto spend frees that budget for the winning terms
> - Combined potential: $3,600+/month in incremental ad sales from reallocating within the existing budget, before any budget increase

### Manual Campaigns: Wrong Keywords

The manual campaigns are almost entirely targeting "tall gold candles" variations:

| Campaign Group | Spend | Sales | ROAS | Clicks | Orders |
|----------------|-------|-------|------|--------|--------|
| "Gold birthday candles" (Broad/Phrase) | $307 | $602 | 1.96 | 191 | 12 |
| "Gold Candles" (Phrase) | $111 | $199 | 1.79 | 53 | 5 |
| "Tall Gold Candles" (all variations) | $280 | $579 | 2.07 | 272 | 11 |
| ASIN Comp - Tall Gold Candles | $66 | $80 | 1.21 | 84 | 2 |
| "Gold Birthday Candle" Scavenger | $59 | $40 | 0.68 | 75 | 1 |
| Other manual campaigns | $166 | $399 | 2.40 | 187 | 6 |

> **Finding: Manual campaigns target "tall gold candles" but the product converts on "birthday candles" and "gold birthday candles"**
>
> **Problem:**
> - $280 is spread across multiple "tall gold candles" campaigns at 2.07 ROAS, borderline profitable
> - "Gold Birthday Candle" Scavenger at $59 and 0.68 ROAS is unprofitable
> - Meanwhile, the keyword "birthday candles" (the #1 converter in auto at 4.98 ROAS) has NO dedicated manual campaign
> - The keyword "birthday candles bulk" (B2B-relevant, 2,366/mo search volume) has NO campaign at all
>
> **Solution:**
> - Pause "Gold Birthday Candle" Scavenger campaign ($59 wasted at 0.68 ROAS)
> - Reduce budget on the lowest-performing "Tall Gold Candles" campaigns (MAG 3 at $49/$0, Phrase MAG 2 at $36/$0)
> - Create new exact/phrase campaigns for: "birthday candles," "gold birthday candles," "birthday candles bulk," "gold candles"
>
> **Impact:**
> - Pausing unprofitable campaigns frees ~$144 (Scavenger + zero-sales Tall Gold campaigns)
> - Redirecting to "birthday candles" at auto's demonstrated 4.98 ROAS: $144 * 4.98 = $717 in additional sales

### Seller-Level Search Term Analysis: P1 Converting vs Non-Converting

Across ALL campaigns (auto + manual), here are the P1-relevant search terms by performance:

**Converting:**

| Search Term | Tier | Spend | Sales | ROAS | Clicks | Orders |
|-------------|------|-------|-------|------|--------|--------|
| birthday candles | P1 Tier 2 | $232 | $941 | 4.06 | 169 | 20 |
| gold birthday candles | P1 Tier 1 | $84 | $957 | 11.37 | 56 | 14 |
| gold candles | Adjacent | $45 | $435 | 9.60 | 25 | 6 |
| gold candles birthday | P1 Tier 1 | $20 | $40 | 2.02 | 10 | 1 |
| birthday candles gold | P1 Tier 1 | $18 | $40 | 2.14 | 8 | 1 |
| **Total** | | **$399** | **$2,412** | **6.05** | **268** | **42** |

**Not converting (candle-relevant terms only):**

| Search Term | Spend | Sales | Clicks | Orders |
|-------------|-------|-------|--------|--------|
| birthday candles for cake | $62 | $40 | 57 | 1 |
| tall birthday candles | $24 | $0 | 14 | 0 |
| celebration stadium gold birthday candles | $28 | $0 | 10 | 0 |
| sparkler candles | $27 | $0 | 29 | 0 |
| cake candles | $25 | $0 | 18 | 0 |
| candles for cake | $21 | $0 | 19 | 0 |
| **Total** | **$187** | **$40** | **147** | **1** |

The pattern is consistent: "birthday candles" and "gold birthday candles" convert well. "Tall," "cake candles," "sparkler," and other adjacent terms do not. The manual campaign keyword strategy should align with this reality.

## Insights

- **The auto catch-all has already solved the keyword discovery problem.** "Birthday candles" (4.98 ROAS, 16 orders) and "gold birthday candles" (17.69 ROAS, 13 orders) are proven winners sitting inside a catch-all campaign. The next step is extracting these into dedicated campaigns where they can be scaled with controlled budgets and bids.
- **The manual campaign keyword strategy is misaligned.** 30+ campaigns target variations of "tall gold candles," which converts at 2.07 ROAS across all variations. Meanwhile, the mega keyword "birthday candles" (155K monthly searches, 4.06 ROAS at seller level) has zero dedicated manual campaigns.
- **$305 in wasted auto spend and $144 in unprofitable manual campaigns can be immediately reallocated.** Combined $449 redirected to proven keywords at demonstrated ROAS would generate ~$1,500-2,200 in incremental sales.
- **B2B-specific queries ("birthday candles bulk" at 2,366/mo) are completely untargeted.** This is the most natural expansion for a product whose growth is driven by B2B bulk purchasing.

## Questions for the Seller

- The auto catch-all campaign drives 72% of P1 ad revenue. Is this by design, or has the manual campaign strategy not been updated since the account was originally structured? Understanding the intent helps determine whether to restructure aggressively or incrementally.
