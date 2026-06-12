# Beauticone Trends - Ad Analysis

**Window:** 2026-01-22 to 2026-04-20 (89 days, full available window).
**Filter:** ENABLED campaigns for account-level blockers unless noted. Some account-level tables (keyword vs product, match type, placement) include paused campaigns because those queries do not expose a status filter.
**Account ad spend (enabled, 89d):** $6,128 // $8,897 sales // ROAS 1.45 // 25 active campaigns

## Account Level

### Campaign Structure

Campaign structure is healthy and not overstuffed. Naming convention is systematic: `SO | {Product} | {ASIN} | SPM | {Theme} | {Match Type}`. Each campaign groups a small set of related targets. No single campaign has dozens of keywords fighting for one budget.

No action needed on structure. Move on.

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|--------|-------|-------|------|-----|-----|-----|
| Manual targeting | 7,320 | $6,128.49 | $8,897.06 | 1.45 | $7.42 | $0.84 | 16.38% |
| Automatic | 0 | $0 | $0 | - | - | - | - |

> **Problem:** The account is running 100% manual, 0% auto. There is no discovery loop in place. Auto campaigns exist precisely to let Amazon's algorithm surface high-intent search terms the advertiser has not yet thought of, which are then harvested into manual exact campaigns. Without this loop, the account is only ever bidding on the keywords the team already knows about. Any emerging or long-tail converting term is invisible.
>
> **Solution:** Launch a small auto campaign per hero product (start with P0 Straight Razors and P2 Pumice Stone) with a low daily budget (~$10-15/day) and Broad/Close/Loose/Substitutes enabled. Review search term reports weekly and harvest converting terms into new manual exact campaigns.
>
> **Impact:** Expect 10-20% lift in P0 ad-attributed sales within 4-6 weeks as the harvesting loop begins feeding new exact campaigns. Hard to quantify precisely in advance, but the structural gap is clear.

### Campaign Profitability

Threshold: ROAS below 1.5x is unprofitable (default margin assumption). Meaningful-spend campaigns ($100+ spend) below threshold:

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| SO \| Straight Razor \| B0F839C7CT \| PT \| Top Competitors \| Exact | $2,282.64 | $2,991.34 | 1.31 | 2,409 | 387 |
| SO \| Pumice Stone \| B0FT8N1KC8 \| SK \| pumice stone for feet \| Exact | $1,543.97 | $2,231.15 | 1.45 | 1,483 | 326 |
| SO \| Hair Cutting Scissors \| B0FPRCTCK8 \| PT \| Converting ASINs | $400.66 | $425.60 | 1.06 | 506 | 44 |
| SO \| Straight Razor \| B0F839C7CT \| GTEX BS3 | $360.12 | $442.30 | 1.23 | 449 | 58 |
| **Total below-threshold spend** | **$4,587.39** | **$6,090.39** | **1.33** | | |

> **Problem:** 75% of enabled ad spend is below the 1.5x ROAS profitability threshold. The single largest underperformer is the P0 "PT Top Competitors" campaign at $2,283 spend (37% of account) running at 1.31 ROAS. At 16% CVR and 387 orders it is volume-rich, but each sale loses margin.
>
> **Solution:** Do not pause the P0 PT campaign outright; it is driving the majority of P0 volume. Instead: (a) lower bids on the lowest-converting ASIN targets inside it to reduce CPC (current CPC is $0.95), (b) negate ASIN targets with 30+ clicks and zero orders, (c) reallocate a portion of the saved spend to the high-ROAS Scavenger Broad campaign ($148 spend at 2.13 ROAS) and the currently non-existent Tier 1 SK Exact campaign (see product-level section).
>
> **Impact:** A 10-15% bid reduction on PT Top Competitors at current volume preserves ~90% of orders while cutting spend by ~$250/month. Redeploying that spend to the 2.13 ROAS Broad Scavenger campaign adds ~$500 in sales/month at the same ad cost. Net: roughly +$2,000 in annualized P0 ad sales from reallocation alone, before any campaign additions.

The second-largest below-threshold campaign, P2 Pumice Stone "pumice stone for feet Exact," is borderline (1.45 ROAS) and is on a fast-growing product. Tightening bids here is secondary.

### Targeting Strategy

**Keyword vs Product Targeting (includes paused campaigns):**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|-------------------|--------|-------|-------|------|-----|-----|-----|
| Keyword Targeting | 7,255 | $5,724.07 | $7,236.59 | 1.26 | $7.59 | $0.79 | 13.15% |
| Product Targeting | 9,141 | $7,207.44 | $8,464.05 | 1.17 | $7.66 | $0.79 | 12.09% |

The split is roughly even. Both are below 1.5x ROAS, which reflects the overall account profitability problem rather than a specific strategy mismatch. Keyword targeting converts slightly better (13.15% vs 12.09%), consistent with intent quality.

**Match Type Breakdown (includes paused campaigns):**

| Match Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|------------|--------|-------|-------|------|-----|-----|-----|
| EXACT | 3,161 | $3,038.59 | $4,039.85 | 1.33 | $7.05 | $0.96 | 18.13% |
| BROAD | 2,216 | $1,350.29 | $1,703.20 | 1.26 | $8.56 | $0.61 | 8.98% |
| PHRASE | 190 | $109.18 | $146.70 | 1.34 | $8.15 | $0.57 | 9.47% |

Exact match dominates keyword spend (~68%) with by-far the best CVR (18%). This is a healthy pattern. Broad has lower CVR (9%) as expected but cheap CPCs are keeping ROAS acceptable. Phrase is underutilized at only $109 spend. Not a pressing issue, but there is room to add phrase variants of the winning exact keywords.

## Product Level (P0: Straight Razors for Men)

### P0 Campaign Map

All enabled campaigns targeting the Straight Razors parent (B0F839C7CT + B0FKD87MTR child ASINs):

| Campaign | Spend | Sales | ROAS | Clicks | Orders | CVR |
|----------|-------|-------|------|--------|--------|-----|
| B0F839C7CT \| PT \| Top Competitors \| Exact | $2,282.64 | $2,991.34 | 1.31 | 2,409 | 387 | 16.1% |
| B0F839C7CT \| GTEX BS3 | $360.12 | $442.30 | 1.23 | 449 | 58 | 12.9% |
| B0FKD87MTR \| Broad \| Scavenger | $149.35 | $362.72 | 2.43 | 505 | 48 | 9.5% |
| B0F839C7CT \| Broad \| Scavenger | $148.40 | $316.58 | 2.13 | 434 | 41 | 9.4% |
| B0FKD87MTR \| Converting Keywords | $77.49 | $161.84 | 2.09 | 143 | 23 | 16.1% |
| Other (Exact/Phrase Scavengers, small spend) | $29.32 | $29.80 | 1.02 | 96 | 4 | 4.2% |
| **P0 Total** | **$3,047.32** | **$4,304.58** | **1.41** | **4,036** | **561** | **13.9%** |

P0 consumes ~50% of total account ad spend. P0 ROAS (1.41) is slightly below account overall (1.45) and below the 1.5x threshold.

**Key structural observation:** P0 has no dedicated SK (Sponsored Products Keyword) campaign on Tier 1 search terms. By contrast, P2 (Pumice Stone) has a dedicated "SK | pumice stone for feet | Exact" campaign spending $1,544 over 90 days. The hero product is missing the equivalent of that campaign. See the Impression Share Blocker section below.

### Impression Share Blocker: Keyword Spend vs. Tier 1 Queries

Section 4 of SQP Analysis identified impression share as the primary Tier 1 blocker. Brand is at 2.97% impression share vs a ~9% cap. The PPC lever is bidding on the keywords where visibility is low. Here is current Tier 1 keyword-level spend across all P0 campaigns:

| Tier 1 Search Term | SQP Volume/mo | Ad Spend (90d) | Ad Sales | ROAS | Clicks | Orders | Ad CVR |
|-------------------|---------------|----------------|----------|------|--------|--------|--------|
| straight razor | 102K | $147 | $215 | 1.46 | 241 | 27 | 11.2% |
| straight razors for men | 35K | $157 | $113 | 0.72 | 193 | 15 | 7.8% |
| single blade razor | 43K | $13 | $21 | 1.61 | 22 | 3 | 13.6% |
| single blade razors for men | 15K | $21 | $29 | 1.37 | 38 | 4 | 10.5% |
| straight edge razor | 14K | $26 | $58 | 2.25 | 39 | 8 | 20.5% |
| barber razor | 12K | $195 | $196 | 1.01 | 252 | 27 | 10.7% |
| navajas para barbero | 12K | $23 | $22 | 0.96 | 41 | 3 | 7.3% |
| **Tier 1 total (search-term level)** | **~233K** | **$582** | **$654** | **1.12** | **826** | **87** | **10.5%** |

High-efficiency Tier 1 variants currently underfunded:
- "straight edge razor" - $26 spend, 2.25 ROAS, 20.5% CVR
- "barber razors" (plural) - $39 spend, 1.78 ROAS
- "mens straight razor" - $8 spend, 2.83 ROAS
- "beard straight razor" - $10 spend, 2.76 ROAS

> **Problem: The hero ASIN is not bidding meaningfully on its own hero keywords.** Total P0 keyword-level spend on Tier 1 terms is ~$582 over 90 days (~$6.50/day). The largest Tier 1 volume query "straight razor" (102K monthly searches) gets $1.63/day in spend. This is the direct mechanical cause of the 2.97% impression share on Tier 1. P0 is winning through Product Targeting (going after competitor ASIN detail pages), not through keyword visibility on search.
>
> **Solution:**
> 1. Launch a dedicated **SO | Straight Razor | B0F839C7CT | SPM | SK | Tier 1 | Exact** campaign with the 7 Tier 1 keywords above, each as a separate exact-match target. Start at $30-40/day. Use the Pumice Stone SK campaign as the template.
> 2. Within 2 weeks, scale the SK Tier 1 budget to $60-80/day based on early ROAS. These keywords already convert at 10-20% on minimal spend.
> 3. Investigate the underperformance of "straight razors for men" (0.72 ROAS on $157 spend). Most likely cause is bad placement (appearing mostly on Product Pages where CVR is 10% vs Top of Search where it is 16%). Add a +50% Top of Search bid modifier on this campaign and retest.
> 4. Negate: "professional straight razor" ($79 spend at 0.44 ROAS), "magnetic straight razor" ($10 at 0 ROAS, wrong product), "porta navajas para barbero" ($9 at 0 ROAS, searching for a razor HOLDER).
>
> **Impact:** Tripling P0 Tier 1 keyword spend (from $6.50/day to ~$20/day) at the current blended Tier 1 ROAS of 1.12 is not the base case; the base case is scaling the underfunded high-ROAS variants (2.25-2.85 ROAS) which have clear room to grow. Conservative projection: moving Tier 1 spend from $582 to $1,800 over 90 days at a blended 1.6 ROAS adds roughly $2,880 in ad sales/quarter. At a category-realistic 3% CVR lift from better placements on "straight razors for men" alone, add another ~$700. Combined quarterly incremental sales from the Tier 1 PPC fix: **~$3,500-$4,500**.

### Secondary: CTR on Tier 1

From SQP, brand CTR on Tier 1 is 2.12% vs industry 2.31% (near parity, not a primary blocker). Placement data confirms the diagnostic: Top of Search CTR is 8.64% vs 0.59% on Product Pages. If P0 were getting more Top of Search share, CTR would improve on its own. This is a second-order effect of the impression-share fix above, not a separate problem.

## Insights

- **P0 is the 50% ad-spend product but has no dedicated Tier 1 keyword exact campaign.** This is the single biggest structural mistake in the account. The P2 Pumice Stone has exactly this kind of campaign and it drives 326 orders/quarter (on its own) from one dedicated SK exact campaign. The P0 equivalent is missing.
- **Product Targeting is doing the heavy lifting on P0 but at 1.31 ROAS.** Going after competitor detail pages with exact ASIN targets gets volume (387 orders/quarter) but the spend efficiency is suffering. A small Tier 1 keyword campaign would produce higher-quality clicks at similar or better ROAS.
- **Top of Search placement massively outperforms Product Pages for this account** (16.4% CVR, 8.64% CTR vs 10.5% CVR, 0.59% CTR). Yet 27% of spend is on Product Pages. Shifting placement mix toward Top of Search via bid modifiers is a cross-product lever, not just P0.
- **No auto campaigns are running.** The account has no mechanism for discovering new converting search terms. Every keyword in the account is one someone manually chose. This is both a quality ceiling and a reason P0's Tier 1 impression share is stuck.

## Things to Investigate Further

- **Why was the Marble variant's PT Top Competitors campaign paused?** Q726 shows it ran $1,356 spend at 0.99 ROAS. Paused campaigns do not show in Q699 ENABLED, but the historical spend is significant. Worth understanding when and why this was paused, because the All Black variant's equivalent PT campaign is still running at 1.31 ROAS (similar profile).
- **Does the Tier 1 impression share collapse (Oct 2025 to Mar 2026, per SQP) coincide with ad spend being pulled back?** Our ad data window only starts Jan 22, 2026, so we cannot directly see Oct-Dec 2025 ad activity. Worth asking the seller.

## Questions for the Seller

- The account has zero auto campaigns. Is that a deliberate strategy, or was the auto campaign turned off at some point?
- On the All Black variant, the PT Top Competitors campaign is the dominant revenue driver but sits below profitability. What is the actual product cost basis, so we can recalculate the break-even ROAS threshold precisely?
- The Marble variant's main PT campaign appears to be paused. When and why was it paused, and is there a plan to restart it?
