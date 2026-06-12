# Ad Analysis: Sapo All Natural

**Data window:** Jan 1, 2026 - Mar 31, 2026 (88 days of ad data)
**Total account spend:** $652.68 | Total ad sales: $1,268.42 | Account ROAS: 1.94

## Account Level

### Campaign Structure

36 enabled campaigns for 8 products. This is excessive. 17 of those campaigns are "Brands SP 1-17," which appear to be product-targeting campaigns with every product advertised across each one. Combined, these 17 campaigns spent $17.52 for $29.98 in sales over 3 months. They're generating essentially nothing and cluttering the account.

The core campaigns follow a clear pattern: each product has a "[Product] Master Ad SP" (manual) and a "[Product] Auto [Year]" (auto). This structure is reasonable for the manual/auto pairing, but the proliferation of inactive campaigns makes it harder to manage.

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|--------|-------|-------|------|-----|-----|-----|
| Automatic | 320 | $140.47 | $229.83 | 1.64 | $13.52 | $0.44 | 5.31% |
| Manual | 1,006 | $512.21 | $1,038.59 | 2.03 | $12.36 | $0.51 | 8.35% |

Manual drives 78% of spend at 2.03 ROAS, outperforming auto's 1.64 ROAS. Manual also converts at 8.35% vs auto's 5.31%. This is directionally healthy: manual is the primary driver, auto is the discovery channel. However, the auto ROAS is dragged down by one specific campaign (Calendula Auto 2025 at 0.29 ROAS), which is addressed under campaign profitability.

### Campaign Profitability

Unprofitable campaigns with meaningful spend (below 1.5x ROAS):

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| Calendula Master Ad SP | $194.13 | $209.79 | 1.08 | 372 | 20 |
| Trending Competitors | $84.93 | $79.42 | 0.94 | 144 | 8 |
| Calendula Auto 2025 | $68.88 | $19.98 | 0.29 | 146 | 2 |
| Eye Serum Master Ad SP | $14.95 | $0.00 | 0.00 | 17 | 0 |
| Vitamin C Master Ad SP | $16.21 | $0.00 | 0.00 | 19 | 0 |
| **Total unprofitable** | **$379.10** | | | | |

> **Finding: 58% of total ad spend is going to unprofitable campaigns**
>
> **Problem:**
> - $379 of $653 total spend (58%) is in campaigns below 1.5x ROAS
> - The Calendula Auto alone burned $69 for $20 in sales (0.29 ROAS, losing $49)
> - "Trending Competitors" campaign is spending $85 at 0.94 ROAS across multiple products
>
> **Solution:**
> - Pause Calendula Auto 2025 entirely. 146 clicks, 2 orders, 1.4% CVR means the traffic is not converting
> - Restructure Calendula Master Ad SP: the top search term "calendula soap" is spending $41 at 0.49 ROAS (see search term analysis below). Negate that term and reallocate
> - Evaluate "Trending Competitors" campaign targets. At 0.94 ROAS, the competitor targeting strategy is not working
>
> **Impact:**
> - $69 from Calendula Auto + $41 from "calendula soap" = $110 reallocated to Cucumber campaigns at 3.09 ROAS = ~$340 in additional sales
> - Net improvement: ~$310 in additional sales from the same ad budget

Top profitable campaigns (reallocation targets):

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| Cucumber Master Ad SP | $132.51 | $409.59 | 3.09 | 242 | 37 |
| Sapo Keywords for all products $.02 | $3.47 | $69.94 | 20.16 | 30 | 5 |
| Wrinkle Serum Master Ad SP | $18.14 | $129.93 | 7.16 | 23 | 6 |
| Night Cream Master Ad SP | $2.83 | $39.98 | 14.13 | 6 | 2 |

"Sapo Keywords for all products $.02" at 20.16 ROAS on $3.47 spend is extremely underfunded. This campaign is likely targeting branded "sapo" keywords at $0.02 bids, which would explain the high ROAS. It should be scaled to capture all branded search volume as a defense campaign.

### Targeting Strategy

**Keyword vs Product Targeting:**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|-------------------|--------|-------|-------|------|-----|-----|-----|
| Keyword Targeting | 994 | $467.12 | $948.73 | 2.03 | $12.82 | $0.47 | 7.44% |
| Product Targeting | 315 | $177.17 | $299.71 | 1.69 | $11.99 | $0.56 | 7.94% |

Keyword targeting outperforms product targeting on ROAS (2.03 vs 1.69) while spending less per click ($0.47 vs $0.56). Both have similar CVR (~7.5-8%). No major reallocation needed, but the product targeting (primarily the "Trending Competitors" campaign) is pulling the average down.

**Match Type Breakdown:**

| Match Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|------------|--------|-------|-------|------|-----|-----|-----|
| EXACT | 254 | $134.92 | $199.80 | 1.48 | $10.52 | $0.53 | 7.48% |
| PHRASE | 224 | $103.30 | $359.73 | 3.48 | $14.39 | $0.46 | 11.16% |
| BROAD | 209 | $87.85 | $99.40 | 1.13 | $9.94 | $0.42 | 4.78% |

> **Finding: Exact match is underperforming phrase match**
>
> **Problem:**
> - Phrase match achieves 3.48 ROAS with 11.16% CVR
> - Exact match achieves only 1.48 ROAS with 7.48% CVR, despite getting the most spend ($135)
> - This is backwards. Exact should be the highest-performing match type because it targets the most specific queries
>
> **What this tells us:** The exact keywords in the manual campaigns are not the right keywords. Phrase match is finding better converting search terms through its broader matching, but those winners have never been harvested into dedicated exact match campaigns. The harvest-and-scale loop is broken.
>
> **Solution:** Mine the top-converting search terms from phrase match campaigns. Move the winners into new exact match campaigns with dedicated budgets. Negate those terms from phrase to prevent duplicate spend.
>
> **Impact:** If the $135 in exact match spend were redirected to terms with phrase match's 3.48 ROAS performance, it would generate $470 in sales vs the current $200. A $270 increase from the same spend.

## Product Level (P0: Face Cleansers)

### P0 Campaign Map

| Campaign | Product | Spend | Sales | ROAS | Clicks | Orders |
|----------|---------|-------|-------|------|--------|--------|
| Calendula Master Ad SP | Calendula | $191.18 | $209.79 | 1.10 | 366 | 20 |
| Cucumber Master Ad SP | Cucumber | $131.90 | $409.59 | 3.11 | 241 | 37 |
| Calendula Auto 2025 | Calendula | $68.38 | $9.99 | 0.15 | 145 | 2 |
| Cucumber Auto 072923 | Cucumber | $41.26 | $99.91 | 2.42 | 90 | 10 |
| Trending Competitors (P0 share) | Both | $38.13 | $69.43 | 1.82 | 66 | - |
| Sapo Keywords (P0 share) | Cucumber | $0.84 | $39.96 | 47.57 | 7 | - |
| **Total P0** | | **$471.69** | **$838.67** | **1.78** | **915** | **69+** |

P0 gets 72% of total account ad spend ($472 of $653). Within P0:
- **Cucumber: $174 spend, $549 sales, 3.16 ROAS** (profitable, scalable)
- **Calendula: $260 spend, $220 sales, 0.85 ROAS** (unprofitable, burning cash)

Calendula consumes 55% of P0 ad budget but generates only 26% of P0 ad sales. This is the single biggest misallocation in the account.

### Impression Share Blocker: Keyword Spend vs. Tier 1/2 Queries

Section 4 (SQP) identified impression share as the primary blocker on Tier 1 (3.55% of ~8-9% max) and near-zero on Tier 2. The PPC lever is bidding on the keywords where impression share is low. Here's what the search term data shows:

**Tier 1 queries (cucumber/calendula face wash/cleanser):**

| Search Term | Spend (3mo) | Sales | ROAS | Clicks | Orders |
|-------------|------------|-------|------|--------|--------|
| cucumber face wash | $11.77 | $89.41 | 7.60 | 20 | 8 |
| calendula face wash | $4.62 | $0.00 | 0.00 | 8 | 0 |
| aloe vera face wash | $2.38 | $19.98 | 8.39 | 4 | 1 |
| natural face wash | $1.98 | $0.00 | 0.00 | 4 | 0 |
| face wash | $7.20 | $9.99 | 1.39 | 12 | 1 |
| facial cleanser | $6.39 | $0.00 | 0.00 | 12 | 0 |

**"Cucumber face wash" is the standout.** 7.60 ROAS, 40% CVR (8 orders from 20 clicks). But it's only getting $11.77 in spend over 3 months. That's $3.92/month on the hero query that converts at 7.6x. This is the most underfunded keyword in the account.

**Meanwhile, the Calendula campaigns are spending on irrelevant terms:**

| Search Term | Campaign | Spend | Sales | ROAS | Clicks |
|-------------|----------|-------|-------|------|--------|
| calendula soap | Calendula campaigns | $40.75 | $19.98 | 0.49 | 75 |
| jabon de calendula | Calendula campaigns | $11.26 | $0.00 | 0.00 | 21 |
| calendula cream | Calendula campaigns | $10.59 | $0.00 | 0.00 | 21 |
| calendula (generic) | Calendula campaigns | $2.90 | $0.00 | 0.00 | 5 |

$65 is going to "calendula soap," "jabon de calendula," and "calendula cream," which are not face cleanser queries. "Calendula soap" is a bar soap search. "Calendula cream" is a moisturizer search. These should be negated immediately.

> **Finding: P0's hero keyword gets $12 in 3 months while $65 goes to irrelevant calendula terms**
>
> **Problem:**
> - "Cucumber face wash" converts at 7.60 ROAS but gets $3.92/mo in ad spend
> - SQP shows 3.55% impression share on Tier 1, with ~$2K/mo addressable market
> - Meanwhile, $65 is spent on non-cleanser calendula queries (soap, cream, generic) with 0.31 ROAS combined
>
> **Solution:**
> - Negate "calendula soap," "calendula cream," "jabon de calendula" from Calendula campaigns
> - Create a dedicated exact match campaign for "cucumber face wash" with $5-10/day budget
> - Add "cucumber face cleanser," "calendula face cleanser," "natural face cleanser" as phrase match targets
>
> **Impact:**
> - $65 saved from irrelevant terms, reallocated to "cucumber face wash" at 7.60 ROAS = ~$494 in additional sales over 3 months
> - Impression share on Tier 1 should increase from 3.55% toward the 8-9% cap, driving proportional revenue growth

### Placement Optimization

| Placement | Impressions | Clicks | Spend | Sales | ROAS | CTR | CVR |
|-----------|-------------|--------|-------|-------|------|-----|-----|
| Top of Search | 3,463 | 67 | $31.88 | $299.77 | **9.40** | 1.93% | **31.34%** |
| Rest of Search | 81,986 | 519 | $255.45 | $489.55 | 1.92 | 0.63% | 7.71% |
| Product Pages | 1,216,199 | 698 | $352.41 | $459.12 | 1.30 | 0.06% | 5.44% |

> **Finding: Top of Search converts at 31% but gets only 5% of spend**
>
> **Problem:**
> - Top of Search: 9.40 ROAS, 31.34% CVR, 1.93% CTR
> - Product Pages: 1.30 ROAS, 5.44% CVR, 0.06% CTR
> - Product Pages gets $352 (54% of spend) while Top of Search gets $32 (5%)
> - For every dollar spent on Top of Search, the brand gets $9.40 back. For Product Pages, $1.30.
>
> **Solution:**
> - Increase Top of Search bid modifier to 50-100% on P0 campaigns to shift more impressions to the premium placement
> - Consider reducing Product Page bids on campaigns with consistently poor ROAS there
>
> **Impact:**
> - If $100 of Product Pages spend were shifted to Top of Search: Product Pages would lose $130 in sales, but Top of Search would gain $940 in sales. Net gain: $810 from the same spend.
> - Even a modest shift (moving $50 from Product Pages to Top of Search) nets ~$405 in incremental sales.

## Insights

- **The Calendula cleanser ad strategy is the account's biggest problem.** $260 in spend at 0.85 ROAS, with $65 going to irrelevant search terms (calendula soap, cream). This isn't just low ROAS; it's actively taking budget away from the profitable Cucumber campaigns.
- **Top of Search placement is severely underutilized.** 31% CVR at 9.4 ROAS, yet it receives only 5% of total spend. This is the fastest lever to pull: increase Top of Search bid modifiers and the account immediately generates more revenue from the same budget.
- **"Sapo Keywords for all products $.02" is a hidden gem.** 20.16 ROAS on $3.47 spend. This branded keyword campaign captures high-intent branded searches at near-zero cost. It should be scaled with slightly higher bids to capture all branded volume.

## Things to Investigate Further

(None remaining. All investigation items from earlier steps have been addressed through the data pulls.)

## Questions for the Seller

- **Is the Calendula cleanser a strategically important product?** The ad data shows it underperforming Cucumber by every metric: 0.85 vs 3.16 ROAS, 10% vs 29% CVR, 4.2 vs 4.5 stars. If the seller has a strong reason to keep investing in Calendula ads (e.g., higher margin, building the variant), the strategy needs to change significantly. If not, the budget should shift to Cucumber.
