# Ad Analysis - The Restroom Kit

**Important context:** All campaigns are currently paused. The seller ran ads from Jan 12 - Mar 21, 2026 (69 days), then stopped entirely. All findings below describe "here's what was happening before you stopped," not "here's what's broken right now." The campaigns were managed by an external tool (AsteroidX/Amazify).

**Date range:** January 12 - March 21, 2026
**Total spend:** $2,251 | **Total sales:** $4,632 | **Overall ROAS:** 2.06

## Account Level

### Campaign Structure

**Finding: Overstuffed manual campaign with budget starvation**

**Problem:**
- The primary manual campaign ("[AsteroidX] 1001 $ B079LX5T6R $ REMA") has 20 keyword and product targets in a single campaign
- Only 3 of the 20 targets spend meaningfully. The top target ("travel toilet seat covers") consumes 62% of the campaign budget ($335 of $542), starving the other 19 targets

| Targeting | Match Type | Spend | Sales | ROAS | Clicks | Orders |
|-----------|-----------|-------|-------|------|--------|--------|
| travel toilet seat covers | EXACT | $335.24 | $584.78 | 1.74 | 380 | 21 |
| travel toilet paper to go packs | EXACT | $91.95 | $389.85 | 4.24 | 201 | 15 |
| travel size toilet paper | EXACT | $78.54 | $204.91 | 2.61 | 124 | 9 |
| asin="b000jlfbao" | Product | $15.36 | $55.98 | 3.64 | 56 | 2 |
| asin="b07fl97fn4" | Product | $7.12 | $0.00 | 0.00 | 16 | 0 |
| 15 other targets | Various | $14.04 | $55.98 | 3.99 | 30 | 1 |

**Revenue Opportunity:** Move "travel toilet paper to go packs" to a separate campaign and increase spend. Impact:

- Current:
  - travel toilet seat covers: Spend = $335, Sales = $585 (1.74 ROAS)
  - travel toilet paper to go packs: Spend = $92, Sales = $390 (4.24 ROAS)
- After restructuring (swap spend levels):
  - travel toilet seat covers: Spend = $92, Sales = $160 (at its 1.74 ROAS)
  - travel toilet paper to go packs: Spend = $335, Sales = $1,420 (at its 4.24 ROAS)
- Impact: +$605 in sales from the same total spend

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|--------|-------|-------|------|-----|-----|-----|
| Automatic | 1,734 | $1,535 | $2,930 | 1.91 | $27.57 | $0.89 | 6.0% |
| Manual | 1,017 | $716 | $1,702 | 2.38 | $28.39 | $0.70 | 7.1% |

**Finding: Auto is consuming 68% of total ad spend**

**Problem:**
- The auto campaign alone spent $1,535 (68% of total spend) vs $716 in manual campaigns (32%)
- Auto ROAS (1.91) is lower than manual ROAS (2.38)
- Auto CPC ($0.89) is higher than manual CPC ($0.70)

**What this tells us:** The account is relying on Amazon's algorithm to find customers instead of actively targeting the keywords that convert. The auto campaign has clearly found winning search terms (103 orders from close-match), but no one took the next step of harvesting those terms into manual campaigns with dedicated budgets and controlled bids.

**Solution:** Mine the auto campaign's converting search terms, launch manual exact campaigns for the top converters, negate those terms from auto so spend isn't duplicated.

**Impact:** Manual campaigns achieve 24% better ROAS (2.38 vs 1.91) and 22% lower CPC ($0.70 vs $0.89). Moving the top auto search terms to manual and scaling them should improve ROAS while increasing total sales.

### Campaign Profitability

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| Amazify Auto (Travel Kit) | $33.64 | $11.99 | 0.36 | 45 | 1 |
| Campaign with presets (B079LXXKP3) | $48.92 | $27.99 | 0.57 | 33 | 1 |
| Business Customers - SP-EX - Test | $11.81 | $0.00 | 0.00 | 15 | 0 |
| **Total wasted** | **$94.37** | | | | |

**Problem:** 3 campaigns ran below 1.5x ROAS, spending a combined $94 over 69 days. The Business Customers campaign generated zero sales from 15 clicks, and the Amazify Auto campaign generated $12 from $34 spent.

**Solution:** Pause these campaigns (already done) and reallocate budget to the REMA manual campaign's best-performing keywords.

**Impact:** $94 reallocated to "travel toilet paper to go packs" at its 4.24 ROAS would generate $399 in additional sales.

### Targeting Strategy

**Keyword vs Product Targeting:**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|-------------------|--------|-------|-------|------|-----|-----|-----|
| Keyword Targeting | 2,659 | $2,216 | $4,564 | 2.06 | $27.73 | $0.83 | 6.2% |
| Product Targeting | 92 | $35 | $68 | 1.95 | $22.66 | $0.38 | 3.3% |

Keyword targeting dominates (98% of spend). Product targeting is minimal and underperforming. No reallocation needed here.

**Match Type Breakdown:**

| Match Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|------------|--------|-------|-------|------|-----|-----|-----|
| EXACT | 834 | $604 | $1,438 | 2.38 | $27.39 | $0.72 | 6.5% |
| PHRASE | 81 | $60 | $168 | 2.80 | $27.99 | $0.74 | 7.4% |
| BROAD | 33 | $49 | $28 | 0.57 | $27.99 | $1.48 | 3.0% |

Exact match has the best ROAS (2.38) and CVR (6.5%). Phrase match is performing well at 2.80 ROAS with small volume. Broad match is losing money (0.57 ROAS, $1.48 CPC, 3.0% CVR). The broad campaign should be paused or heavily negated.

## Product Level (P0)

### P0 Campaign Map

All campaigns advertise P0 children (12-pack and 3-pack variants). 100% of ad spend goes to P0.

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| Auto (B079LX5T6R - 12 Pack) | $1,501 | $2,918 | 1.94 | 1,704 | 103 |
| REMA Manual (B079LX5T6R - 12 Pack) | $542 | $1,292 | 2.38 | 807 | 48 |
| SP-PH Research (B079LX5T6R) | $60 | $168 | 2.80 | 81 | 6 |
| REMA Manual (B079LXXKP3 - 3 Pack) | $39 | $191 | 4.85 | 41 | 7 |
| Others (5 campaigns) | $109 | $63 | 0.58 | 118 | 4 |
| **Total P0** | **$2,251** | **$4,632** | **2.06** | **2,751** | **168** |

P0 ad spend = 100% of total account ad spend. No other products are being advertised.

### Impression Share Blocker: Keyword Spend vs. Tier 1/2 Queries

Section 4 (SQP) identified impression share as the primary blocker on both Tier 1 (2.47% of ~8-9% max) and Tier 2 (0.86% of ~8-9% max). The PPC lever is bidding on the keywords where impression share is low. Here's what the ad data shows:

**Tier 1 Keywords in Ad Data:**

| Search Term | Tier | Spend | Sales | ROAS | Clicks | Orders | CVR |
|-------------|------|-------|-------|------|--------|--------|-----|
| travel toilet paper | Tier 1 | $115.69 | $168.94 | 1.46 | 127 | 5 | 3.9% |
| travel toilet paper to go packs | Tier 1 | $94.14 | $333.87 | 3.55 | 182 | 13 | 7.1% |
| travel size toilet paper | Tier 1 | $67.01 | $164.93 | 2.46 | 104 | 7 | 6.7% |
| compact toilet paper | Tier 1 | $31.85 | $138.94 | 4.36 | 31 | 4 | 12.9% |
| portable toilet paper | Tier 1 | $14.79 | $0.00 | 0.00 | 17 | 0 | 0.0% |
| toilet paper on the go | Tier 1 | $3.80 | $0.00 | 0.00 | 5 | 0 | 0.0% |

**Tier 2 Keywords in Ad Data:**

| Search Term | Tier | Spend | Sales | ROAS | Clicks | Orders | CVR |
|-------------|------|-------|-------|------|--------|--------|-----|
| travel toilet seat covers | Tier 2 | $299.76 | $444.83 | 1.48 | 342 | 16 | 4.7% |
| toilet seat cover | Tier 2 | $13.94 | $27.99 | 2.01 | 16 | 1 | 6.2% |
| disposable toilet seat covers | Tier 2 | $6.97 | $27.99 | 4.02 | 9 | 1 | 11.1% |
| toilet seat covers disposable | Tier 2 | $5.37 | $0.00 | 0.00 | 6 | 0 | 0.0% |
| travel toilet seat cover | Tier 2 | $4.17 | $27.99 | 6.71 | 4 | 1 | 25.0% |
| restroom kit (branded) | - | $5.19 | $0.00 | 0.00 | 6 | 0 | 0.0% |

**Finding: Spend is misallocated across tiers**

**Problem:**
- "travel toilet seat covers" alone consumed $300 (13% of total ad budget) at a poor 1.48 ROAS. This is the single largest non-auto search term by spend.
- Meanwhile, high-ROAS terms like "travel toilet paper to go packs" (3.55 ROAS), "compact toilet paper" (4.36 ROAS), and "travel size toilet paper" (2.46 ROAS) are underfunded.
- Tier 2 keywords beyond "travel toilet seat covers" received almost no spend. "travel toilet kit," "public bathroom kit," "emergency bathroom kit," and "public restroom kit" are all absent from the search term report, meaning zero ad dollars went to these relevant terms.

**Solution:**
1. Create dedicated manual exact campaigns with 3-5 keywords each, separated by tier
2. Tier 1 campaign: "travel toilet paper to go packs," "travel size toilet paper," "compact toilet paper" (proven converters)
3. Tier 2 campaign: "travel toilet kit," "public bathroom kit," "emergency bathroom kit," "public restroom kit" (untapped keywords with strong intent match)
4. Reduce spend on "travel toilet seat covers" or move to its own campaign with a lower budget
5. Set Top of Search bid modifiers (see placement data below)

### CTR/CVR Blocker: Placement Distribution

SQP showed above-industry CTR on Tier 1 (2.92% vs 2.63%) but below-industry CVR (3.58% vs 9.44%). The placement data reveals why the overall CVR is low despite the listing being strong:

| Placement | Spend | Sales | ROAS | CTR | CVR | Spend Share |
|-----------|-------|-------|------|-----|-----|-------------|
| Top of Search | $395 | $1,394 | **3.53** | **9.25%** | **12.1%** | 17.5% |
| Rest of Search | $1,115 | $2,028 | 1.82 | 1.09% | 5.2% | 49.5% |
| Product Pages | $738 | $1,210 | 1.64 | 0.86% | 5.0% | 32.8% |

**Finding: Top of Search dramatically outperforms but gets only 17.5% of spend**

**Problem:**
- Top of Search ROAS (3.53) is nearly 2x Rest of Search (1.82) and Product Pages (1.64)
- Top of Search CVR (12.1%) is over 2x the other placements (~5%)
- Top of Search CTR (9.25%) is 8-10x higher than other placements
- Yet only 17.5% of spend goes to Top of Search, while 82.5% goes to lower-performing placements

**Solution:** Increase the Top of Search bid modifier across all campaigns. This shifts more impressions to the premium placement where the listing converts at 12.1% CVR. The listing's strong images and A+ content perform best when the customer sees the product at the top of search results.

**Impact:** If spend were shifted to a 30/35/35 split (TOS/ROS/PP from the current 17.5/49.5/33):
- Current: ($395 × 3.53) + ($1,115 × 1.82) + ($738 × 1.64) = $1,394 + $2,029 + $1,210 = $4,633
- Revised: ($675 × 3.53) + ($788 × 1.82) + ($788 × 1.64) = $2,383 + $1,434 + $1,292 = $5,109
- Impact: +$476 in sales from the same $2,251 total spend, ROAS improves from 2.06 to 2.27

## Insights

- The seller's first advertising attempt was managed by AsteroidX/Amazify automation, which created an auto-heavy, overstuffed campaign structure. 67% of spend went to a single auto campaign, and the only manual campaign had 20 targets competing for one budget. This is the primary reason the ad experiment "failed" and was abandoned.
- Top of Search placement converts at 12.1% CVR and 3.53 ROAS, 2x better than other placements. A properly structured campaign with Top of Search bid modifiers would have achieved significantly better overall ROAS, potentially changing the seller's decision to stop advertising.
- "Travel toilet paper to go packs" is the standout keyword: 4.24 ROAS in the manual campaign, 3.55 ROAS as a search term, 7.1% CVR. This should be the anchor keyword for the first manual campaign.

## Things to Investigate Further

## Questions for the Seller

- The campaigns were set up through AsteroidX/Amazify automation. Was this a self-service tool, or did someone manage the campaigns for you? Understanding this helps us gauge how much PPC experience you've had and what expectations to set.
