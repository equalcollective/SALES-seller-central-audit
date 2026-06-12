# Ad Analysis - Celebration Stadium

**Analysis period:** December 27, 2025 to March 25, 2026 (89 days of ad data)
**Total account ad spend:** $4,533 | **Total ad sales:** $14,429 | **Account ROAS:** 3.18

## Account-Level Analysis

### Campaign Structure

36 campaigns total. Many are well-structured with descriptive naming conventions (product, targeting type, match type, ASIN). However, 8 campaigns for White Candles (B0G7KQQBXG) are running with $0 spend and $0 sales, a dead product consuming campaign slots. Additionally, the account has too many campaigns for the product count: 43 campaign-product combinations for a 3-product catalog suggests over-segmentation.

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|--------|-------|-------|------|-----|-----|-----|
| Automatic | 3,011 | $3,192 | $9,316 | 2.92 | $63.38 | $1.06 | 4.88% |
| Manual | 1,286 | $1,341 | $5,113 | 3.81 | $70.04 | $1.04 | 5.68% |

> **Finding: Auto campaigns are oversized at 70% of spend while underperforming Manual**
>
> **Problem:**
> - Auto drives 70% of spend ($3,192) but achieves lower ROAS (2.92 vs 3.81) and lower CVR (4.88% vs 5.68%)
> - A single catch-all auto campaign ("SP - Auto - Catch All - Top 5 ASINs") consumes $2,506 (55% of total account spend)
>
> **Solution:**
> - Mine the auto campaign search terms for top converters and move them into dedicated manual exact/phrase campaigns
> - Reduce the auto catch-all daily budget to prevent it from consuming the majority of account spend
> - Negate converted terms from auto to avoid duplicate spend
>
> **Impact:**
> - Manual campaigns at 3.81 ROAS vs Auto at 2.92 ROAS means every $100 shifted from auto to manual (at its current ROAS) yields $89 more in sales from the same spend

### Campaign Profitability

Campaigns below 1.5x ROAS with meaningful spend:

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| SP - ASIN - COMP - Exact - Tall Gold Candles | $66 | $80 | 1.21 | 84 | 2 |
| SP - KW - Broad Mod - Tall Gold Candles | $37 | $40 | 1.08 | 40 | 1 |
| **Total wasted** | **$103** | | | | |

Most campaigns are above the 1.5 threshold. The unprofitable campaigns are small. The bigger issue is the auto catch-all consuming disproportionate budget (covered above).

### Targeting Strategy

**Keyword vs Product Targeting:**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|-------------------|--------|-------|-------|------|-----|-----|-----|
| Keyword Targeting | 5,210 | $4,820 | $12,411 | 2.57 | $65.67 | $0.93 | 3.63% |
| Product Targeting | 1,832 | $1,796 | $3,650 | 2.03 | $68.86 | $0.98 | 2.89% |

Keyword targeting outperforms product targeting on both ROAS (2.57 vs 2.03) and CVR (3.63% vs 2.89%). Product targeting is still profitable but should be monitored.

**Match Type Breakdown:**

| Match Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|------------|--------|-------|-------|------|-----|-----|-----|
| BROAD | 1,579 | $1,608 | $2,465 | 1.53 | $68.47 | $1.02 | 2.28% |
| PHRASE | 1,005 | $886 | $2,481 | 2.80 | $72.98 | $0.88 | 3.38% |
| EXACT | 101 | $96 | $329 | 3.42 | $54.81 | $0.95 | 5.94% |

> **Finding: Broad match is barely profitable and Exact match is underfunded**
>
> **Problem:**
> - Broad match consumes $1,608 (the largest match type by spend) at 1.53 ROAS (borderline profitable) with only 2.28% CVR
> - Exact match has the best ROAS (3.42) and CVR (5.94%) but receives only $96 in spend, 6% of what Broad gets
> - This indicates the harvest-and-scale loop is not happening: winning terms from Broad/Phrase are not being graduated to Exact campaigns
>
> **Solution:**
> - Identify top-performing search terms from Broad/Phrase and create Exact match campaigns for them
> - Reduce Broad match budgets, particularly on the candle holder campaigns where the terms are too broad to convert
>
> **Impact:**
> - Exact match at 3.42 ROAS vs Broad at 1.53 ROAS. Shifting $500 from Broad to Exact would yield ~$945 more in sales

### Placement Performance

| Placement | Spend | Sales | ROAS | CTR | CVR | Clicks | Orders |
|-----------|-------|-------|------|-----|-----|--------|--------|
| Top of Search | $2,479 | $9,474 | 3.82 | 2.51% | 6.98% | 2,034 | 142 |
| Rest of Search | $2,211 | $3,609 | 1.63 | 0.48% | 2.12% | 2,590 | 55 |
| Product Pages | $1,801 | $2,888 | 1.60 | 0.29% | 2.36% | 1,862 | 44 |
| Off Amazon | $115 | $90 | 0.78 | 0.30% | 0.18% | 546 | 1 |

Top of Search is overwhelmingly the best placement: 3.82 ROAS, 2.51% CTR, 6.98% CVR. It generates 59% of total ad sales from 37% of spend. Rest of Search and Product Pages are borderline at 1.6 ROAS. Off Amazon is unprofitable and should be excluded.

## Product-Level Analysis (P0: Candle Holder)

### P0 Campaign Map

| Product | Spend | Sales | ROAS | Clicks | Orders | % of Account Spend |
|---------|-------|-------|------|--------|--------|-------------------|
| P0 - Candle Holder | $4,066 | $6,351 | 1.56 | 4,579 | 73 | 61% |
| P1 - Gold Candles | $2,206 | $6,787 | 3.08 | 1,889 | 127 | 33% |
| Other (Tray, bundles) | $344 | $2,922 | 8.49 | 569 | 42 | 5% |

> **Finding: P0 (Candle Holder) consumes 61% of ad spend at 1.56 ROAS, barely above profitability**
>
> **Problem:**
> - P0 spends $4,066 and generates $6,351 in ad sales at 1.56 ROAS. At a 1.5 profitability threshold, this is borderline. Every dollar of P0 ad spend returns ~$0.06 in profit after product costs (assuming 1.5 break-even).
> - P1 (Gold Candles) spends $2,206 at 3.08 ROAS, generating $1 of profit for every $1 spent (after COGS).
> - The account is allocating 2x more budget to the product that returns 2x less.
>
> **Solution:**
> - Reduce P0 candle holder ad spend to only the campaigns/terms that are genuinely profitable (see search term analysis below)
> - Reallocate freed budget to P1 (Gold Candles) campaigns where ROAS is strong
>
> **Impact:**
> - Shifting $1,000 from P0 campaigns (1.56 ROAS) to P1 campaigns (3.08 ROAS) would increase total ad sales by ~$1,520 with the same spend

### Impression Share Blocker: Search Term Spend vs Tier 1 Queries

Section 3 (SQP) identified impression share as the primary blocker on Tier 1 candle holder queries (1.73% of ~8-9% max). The PPC lever would be to bid on those keywords. Here is what the ad data shows:

| Search Term | Tier | Spend | Sales | ROAS | Clicks | Orders |
|-------------|------|-------|-------|------|--------|--------|
| birthday candle holder | Tier 1 | $137 | $0 | 0.00 | 109 | 0 |
| birthday candle holder cake | Tier 1 | $82 | $0 | 0.00 | 86 | 0 |
| birthday candle holders for cake | Tier 1 | $23 | $0 | 0.00 | 31 | 0 |
| number candle holder | Adjacent | $51 | $0 | 0.00 | 33 | 0 |
| number candle holder set | Adjacent | $48 | $0 | 0.00 | 43 | 0 |
| number candle holders | Adjacent | $33 | $0 | 0.00 | 45 | 0 |
| reusable birthday candles | Adjacent | $77 | $0 | 0.00 | 44 | 0 |
| candle holder | Tier 1 | $28 | $0 | 0.00 | 26 | 0 |
| 60th birthday decorations | Tier 3 | $47 | $90 | 1.91 | 38 | 1 |
| 50th birthday decorations | Tier 3 | $39 | $0 | 0.00 | 30 | 0 |
| 70th birthday decorations | Tier 2 | $32 | $0 | 0.00 | 33 | 0 |
| 80th birthday decorations for women | Tier 2 | $19 | $0 | 0.00 | 18 | 0 |
| sparkler candles | Adjacent | $27 | $0 | 0.00 | 29 | 0 |
| cake sparklers | Adjacent | $22 | $0 | 0.00 | 26 | 0 |
| **Total wasted on non-converting candle holder terms** | | **$665** | **$90** | | | |

**This is the most important finding in the entire audit.** The brand has spent $137 on "birthday candle holder" (the exact Tier 1 hero query) with 109 clicks and **zero orders**. The other candle holder terms show the same pattern: spend, clicks, no conversions.

This proves that the impression share blocker identified in SQP cannot be solved through PPC alone. The product gets shown, gets clicked, but does not convert on these queries. The likely reasons:

1. **Price mismatch:** Shoppers searching "birthday candle holder" expect a simple, cheap product ($10-20). The Celebration Stadium at ~$90 is 5-9x the expected price.
2. **Product mismatch:** "Number candle holder" queries (3 of the top wasted terms) show that many shoppers want a holder for number-shaped candles, not a grandstand for 100 candles. These are completely different products.
3. **Intent mismatch:** The product solves a niche problem (milestone birthday with 50-100 individual candles) that most "birthday candle holder" searchers don't have.

**Increasing PPC spend on Tier 1 candle holder queries would increase waste, not sales.** The $665 already spent on non-converting candle holder search terms should be negated and the budget reallocated.

### Profitable P0 Search Terms

The candle holder does convert on a small set of terms:

| Search Term | Type | Spend | Sales | ROAS | Clicks | Orders |
|-------------|------|-------|-------|------|--------|--------|
| celebration stadium | Branded | $27 | $405 | 15.23 | 33 | 6 |
| b0c2wq8g64 | Self-ASIN | $19 | $745 | 39.97 | 25 | 10 |

The candle holder converts on branded queries and self-ASIN targeting, not on non-branded category queries. This aligns perfectly with the SQP finding that branded searches drive the product's sales.

### Profitable Candle (P1) Search Terms

For comparison, the candle search terms convert well:

| Search Term | Spend | Sales | ROAS | Clicks | Orders |
|-------------|-------|-------|------|--------|--------|
| birthday candles | $232 | $941 | 4.06 | 169 | 20 |
| gold birthday candles | $84 | $957 | 11.37 | 56 | 14 |
| gold candles | $45 | $435 | 9.60 | 25 | 6 |
| gold candles birthday | $20 | $40 | 2.02 | 10 | 1 |
| birthday candles gold | $18 | $40 | 2.14 | 8 | 1 |

These are the terms where the brand should concentrate budget. The candles match the search intent, are competitively priced, and convert.

## Insights

- **The candle holder's PPC spend is a capital misallocation.** $4,066 (61% of account) goes to P0 at 1.56 ROAS while P1 (candles) gets $2,206 (33%) at 3.08 ROAS. The candle holder's non-branded search terms generate zero conversions. The only P0 terms that convert are branded ("celebration stadium") and self-ASIN targeting.
- **The candle holder cannot be grown through Amazon search PPC.** The $665 wasted on non-converting candle holder search terms proves that the product does not convert on generic category queries. The market is too small, the price is too high relative to shopper expectations, and the product concept is too niche for generic search discovery.
- **Top of Search placement is the account's strength.** 3.82 ROAS, 6.98% CVR, 2.51% CTR. The account should increase Top of Search bid modifiers to concentrate more spend in this placement.
- **Candle (P1) campaigns are the growth engine.** "Birthday candles" and "gold birthday candles" generate strong ROAS (4-11x) with clear room to scale.

## Questions for the Seller

- Are you aware that the candle holder ad campaigns are spending $4,066 with only 1.56 ROAS over the past 90 days? Would you be open to significantly reducing candle holder ad spend and reallocating to the candles, where ROAS is 3.08?
