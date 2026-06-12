# Ad Analysis: Goal Crazy

**Data window:** Dec 25, 2025 to Mar 23, 2026 (~90 days)
**Total account spend:** $503.25 | **Total account sales:** $2,599.80 | **Account ROAS:** 5.17

## Account Level

### Campaign Structure

The account has only 3 campaigns:

| Campaign | Type | Spend | Sales | ROAS | Clicks | Orders | CVR |
|----------|------|-------|-------|------|--------|--------|-----|
| Booster All ASINs | Auto | $265.08 | $365.40 | 1.38 | 726 | 11 | 1.52% |
| Branded KWs | Manual | $216.73 | $2,234.40 | 10.31 | 229 | 69 | 30.13% |
| Pro all | Manual | $21.44 | $0.00 | 0.00 | 10 | 0 | 0.00% |

**Finding: The account has zero non-branded manual campaigns.**

**Problem:**
- The only manual campaign ("Branded KWs") targets branded keywords: "goal crazy planner" (exact), "goal crazy" (phrase + exact), "goalcrazy" (phrase)
- "Pro all" targets branded misspellings ("crazy goals planner," "goalcrazy planner") with $21 spent and 0 orders
- There are NO manual campaigns targeting Tier 1 keywords (goal planner, goal journal, goal setting planner) or Tier 2 keywords (undated planner, productivity planner)
- This is the direct cause of the 0.42% impression share on Tier 1 and 0.01% on Tier 2 identified in the SQP analysis

**Solution:**
- Launch dedicated manual campaigns for Tier 1 keywords (3-5 keywords each, exact and phrase match)
- Launch dedicated manual campaigns for Tier 2 keywords
- Pause "Pro all" ($21 wasted on branded misspellings that the phrase match in "Branded KWs" already captures)

**Impact:**
- The entire Tier 1 market ($33K/mo) and Tier 2 market ($116K/mo) are currently untapped by PPC. Even capturing 2-3% purchase share on Tier 1 through targeted manual campaigns would represent meaningful revenue growth from a standing start of near zero.

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|--------|-------|-------|------|-----|-----|-----|
| Automatic | 726 | $265.08 | $365.40 | 1.38 | $33.22 | $0.37 | 1.52% |
| Manual | 239 | $238.17 | $2,234.40 | 9.38 | $32.38 | $1.00 | 28.87% |

**Finding: Manual massively outperforms auto, but manual is 100% branded keywords.**

**Problem:**
- Manual ROAS (9.38) is 6.8x auto ROAS (1.38), but this comparison is misleading. Manual is entirely branded search ("goal crazy planner"), which inherently converts at 30% because those customers already know the brand. Auto is the only campaign discovering non-branded customers, and it's running at a loss.
- The auto campaign is generating 726 clicks across 238 unique search terms, meaning the budget is spread extremely thin. Most search terms get 1-2 clicks, far too few to learn or optimize.
- The harvest-and-scale loop is not happening: auto is finding search terms, but no one is extracting the winners into targeted manual campaigns.

**Solution:**
- Mine the auto campaign search terms for non-branded converters (e.g., "daily planner" generated 1 order at 5.33 ROAS)
- Move winning terms into new manual exact campaigns with dedicated budgets
- Negate branded terms from auto (auto is spending on "goal crazy planner" variants that the manual campaign already covers)
- Add negative targeting for clearly irrelevant terms

### Campaign Profitability

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| Booster All ASINs | $265.08 | $365.40 | 1.38 | 726 | 11 |
| Pro all | $21.44 | $0.00 | 0.00 | 10 | 0 |
| **Total unprofitable** | **$286.52** | | | | |

**Problem:** $287 of the $503 total spend (57%) is going to unprofitable campaigns. The auto campaign is running at 1.38 ROAS (below the 1.5x profitability threshold), and "Pro all" is completely dead.

**Solution:** Pause "Pro all" immediately. Optimize the auto campaign by negating branded terms (already covered by manual) and irrelevant search terms. Reallocate the freed budget to new non-branded manual campaigns.

**Impact:** $287 reallocated to campaigns matching "Branded KWs" performance (10.31 ROAS) would generate ~$2,960 in sales. Even at a conservative 3-4x ROAS for non-branded campaigns, $287 would generate $860-$1,148 in additional sales vs. the current $365 from auto. Net improvement: $495-$783 in additional sales from the same budget.

### Targeting Strategy

**Keyword vs Product Targeting:**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|-------------------|--------|-------|-------|------|-----|-----|-----|
| Keyword Targeting | 928 | $491.50 | $2,570.85 | 5.23 | $32.54 | $0.53 | 8.51% |
| Product Targeting | 37 | $11.75 | $28.95 | 2.46 | $28.95 | $0.32 | 2.70% |

Product targeting is negligible ($12 spend), coming only from the auto campaign's "substitutes" and "complements" targeting. Keyword targeting drives 98% of spend and sales.

**Match Type Breakdown:**

| Match Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|------------|--------|-------|-------|------|-----|-----|-----|
| EXACT | 182 | $143.13 | $1,613.40 | 11.27 | $32.93 | $0.79 | 26.92% |
| PHRASE | 57 | $95.04 | $621.00 | 6.53 | $31.05 | $1.67 | 35.09% |

Both match types are performing well, but this is entirely branded keywords. There is no BROAD match at all. The absence of broad match campaigns means there is no keyword discovery happening through manual campaigns, only through auto.

## Product Level (P0)

### P0 Campaign Map

All 3 campaigns advertise P0 (Undated Planner 2025/2026). There are no other products in the account, so P0 = 100% of ad spend.

| Campaign | Child ASIN | Spend | Sales | ROAS | Clicks | Orders |
|----------|-----------|-------|-------|------|--------|--------|
| Branded KWs | B07QNSB373 (Black) | $139.50 | $1,671.30 | 11.98 | 174 | 51 |
| Booster All ASINs | B07WG38CWZ (Navy) | $172.65 | $243.60 | 1.41 | 465 | 7 |
| Booster All ASINs | B07QNSB373 (Black) | $92.43 | $121.80 | 1.32 | 261 | 4 |
| Branded KWs | B07WG38CWZ (Navy) | $30.70 | $162.75 | 5.30 | 21 | 5 |
| Branded KWs | B09LQZFBFJ (Forest Green) | $25.60 | $173.70 | 6.79 | 14 | 6 |
| Pro all | B07QNSB373 (Black) | $17.46 | $0.00 | 0.00 | 8 | 0 |
| Branded KWs | B07WDYBLWB (Rose Gold) | $14.14 | $104.85 | 7.42 | 14 | 3 |
| Branded KWs | B09LQYYJQM (Brown) | $6.79 | $121.80 | 17.94 | 6 | 4 |

### Impression Share Blocker: No Targeted Spend on Tier 1/2 Keywords

Section 3 (SQP) identified impression share as the primary blocker across all tiers (0.42% on Tier 1, 0.01% on Tier 2). The PPC lever is bidding on the keywords where impression share is low. Here's what the ad data shows:

**Tier 1 keyword spend from search terms (auto campaign discovery only):**

| Search Term | Tier | Spend | Sales | ROAS | Clicks | Orders |
|-------------|------|-------|-------|------|--------|--------|
| goal planner | Tier 1 | $2.43 | $0.00 | 0.00 | 6 | 0 |
| goal journal | Tier 1 | $0.41 | $0.00 | 0.00 | 1 | 0 |
| goal setting planner | Tier 1 | $0.41 | $0.00 | 0.00 | 1 | 0 |
| goal setting | Tier 1 | $0.41 | $0.00 | 0.00 | 1 | 0 |
| 90 day goal planner journal | Tier 1 | $0.41 | $0.00 | 0.00 | 1 | 0 |
| **Total Tier 1** | | **$4.07** | **$0.00** | | **10** | **0** |

| Search Term | Tier | Spend | Sales | ROAS | Clicks | Orders |
|-------------|------|-------|-------|------|--------|--------|
| undated daily planner | Tier 2 | $2.05 | $0.00 | 0.00 | 5 | 0 |
| productivity planner 2026 | Tier 2 | $1.23 | $0.00 | 0.00 | 3 | 0 |
| undated planner | Tier 2 | $0.82 | $0.00 | 0.00 | 2 | 0 |
| undated weekly planner | Tier 2 | $0.48 | $0.00 | 0.00 | 2 | 0 |
| **Total Tier 2** | | **$4.58** | **$0.00** | | **12** | **0** |

**Finding: Total spend on Tier 1 + Tier 2 keywords over 90 days is $8.65 (22 clicks, 0 orders).**

This confirms the SQP finding. The brand is not participating in its own market through PPC. The auto campaign occasionally surfaces these terms (1-6 clicks each), but the sample is far too small to draw any conclusions about whether these keywords can convert. Zero orders from 22 clicks is not a signal of poor conversion; it's a signal of insufficient data.

For context, the "Branded KWs" campaign spent $217 on branded terms and generated 69 orders. The auto campaign spent $265 and generated 11 orders (mostly on incidental branded matches). The actual non-branded spend that reached Tier 1/Tier 2 keywords was $8.65, or 1.7% of total ad spend.

### Placement Opportunity

| Placement | Spend | Sales | ROAS | CTR | CVR | Orders |
|-----------|-------|-------|------|-----|-----|--------|
| Top of Search | $155.41 | $1,955.85 | 12.59 | 13.14% | 22.99% | 60 |
| Rest of Search | $198.28 | $516.15 | 2.60 | 1.37% | 3.65% | 16 |
| Product Pages | $145.34 | $127.80 | 0.88 | 0.26% | 1.58% | 4 |
| Off Amazon | $1.28 | $0.00 | 0.00 | 0.24% | 0.00% | 0 |

Top of Search dominates: 12.59 ROAS, 13.14% CTR, 22.99% CVR. This is heavily influenced by branded traffic (branded keywords naturally appear at the top of search), but it also signals that when this product appears in premium placement, it converts very well.

Product Pages placement is unprofitable (0.88 ROAS) and should be deprioritized. When new non-branded campaigns are launched, Top of Search bid modifiers should be set high from the start to capture the premium placement advantage.

## Insights

- **P0 (Undated Planner) has zero PPC presence on its market keywords.** The entire $503 ad spend over 90 days goes to either branded defense ($217 at 10.31 ROAS) or an unoptimized auto campaign ($265 at 1.38 ROAS). Only $8.65 reached Tier 1/Tier 2 keywords, and that was incidental auto traffic, not intentional targeting. This is the single largest opportunity in the account.
- **The branded campaign is well-run and validates the product's conversion ability.** At 30% CVR and 10.31 ROAS on branded keywords, the product converts when shoppers find it. The challenge is entirely about visibility, not conversion.
- **The auto campaign's budget is being burned without structure.** 726 clicks across 238 search terms means an average of 3 clicks per term, which is not enough to optimize anything. The auto campaign needs negatives (branded terms, irrelevant terms) and a smaller scope to focus learning on fewer, more relevant terms.

## Questions for the Seller

- **Has the brand intentionally avoided non-branded keyword targeting, or is this a knowledge/resource gap?** The account structure suggests someone who knows Amazon basics (they set up a branded campaign and an auto campaign) but hasn't taken the next step of building non-branded manual campaigns. Understanding whether this was a deliberate choice (e.g., budget constraints, fear of low ROAS) or simply never attempted will help frame the action plan on the call.
