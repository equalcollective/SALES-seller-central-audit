# Step 4: Ad Analysis - Hippo Outdoor

## Data Window
- Jan 11, 2026 to Apr 9, 2026 (89 days, full ad data availability)
- Ad data only covers the last 90 days, which pre-dates most of the 2025 revenue decline. Findings describe current account state, not historical strategy.

## Account Summary

- **Total account ad spend:** $2,970 over 89 days (~$1,001/mo)
- **Total account ad sales:** $5,940 → **account-level ROAS 2.00**
- **14 enabled campaigns.** 3 have zero/minimal spend (dormant auto campaigns).

---

## Account Level

### Campaign Structure

The account has a clear structural issue: **generic, catch-all campaigns with too many products and targeting rows.** The four biggest campaigns each pool multiple parent ASINs under a single budget, so Amazon's algorithm picks winners and starves the rest.

**Examples:**
- **Fishing Glasses 2025** ($1,480 spend, 1.93 ROAS): advertises 5 different child ASINs across 2 parent products (P1 B0CGHS9B6W *and* P2 B0F5QHC9BW mixed together). Top ad group (B0CGHS9B6W) gets $1,008 at 1.50 ROAS while B0F4R4YGCZ at 3.58 ROAS gets only $85.
- **Tarp Automatic** ($624 spend, 1.66 ROAS): advertises 4 of the 6 P0 children (B09TB3FPKW, B0BGTFSS8Z, B0BGJ82Q64, B0CB5VSYD3). Top line B09TB3FPKW gets $439 at 1.58 ROAS while B0BGJ82Q64 at 3.92 ROAS gets only $45.
- **Tarp Unique - 15 feb** ($325, 1.89 ROAS): same pattern.
- **Tarp 100 - 400** ($66, **3.44 ROAS**): the best-performing P0 campaign by ROAS gets the lowest budget.

**Problem:** High-ROAS product-campaign combinations are being starved. The campaigns that are doing well (Tarp 100 - 400, B0BGJ82Q64 inside Tarp Automatic, B0F4R4YGCZ inside Fishing Glasses) cannot scale because they sit inside campaigns where budget flows to larger but lower-ROAS products.

**Solution:** Separate campaigns per child ASIN. Give each hero child its own campaign with a dedicated budget. The children that currently hit 3-4x ROAS should be scaled; the ones at 1.2-1.5x should be put on a leash until the listing or targeting is improved.

**Revenue opportunity (illustrative reallocation inside Tarp Automatic):**

> - Current state:
>   - B09TB3FPKW (in Tarp Automatic): $439 at 1.58 ROAS → $694 sales
>   - B0BGJ82Q64 (in Tarp Automatic): $45 at 3.92 ROAS → $175 sales
>   - Combined: $484 spend → $869 sales
> - If B0BGJ82Q64 were moved to its own campaign with $200 spend at 3.92 ROAS and B09TB3FPKW scaled back to $284:
>   - B09TB3FPKW: $284 at 1.58 ROAS → $449 sales
>   - B0BGJ82Q64: $200 at 3.92 ROAS → $784 sales
>   - Combined: $484 spend → $1,233 sales
>   - **+$364 in sales on the same $484 budget (+42%)**

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|-------:|------:|------:|-----:|----:|----:|----:|
| Automatic | 1,812 | $1,086 | $2,196 | 2.02 | $14.94 | $0.60 | 8.11% |
| Manual | 2,696 | $1,884 | $3,744 | 1.99 | $14.34 | $0.70 | 9.68% |

Manual drives 63% of spend, ROAS is on par between the two, and manual CVR is slightly higher. The split is **healthy on the surface** - but see Targeting Strategy below, because manual's win is being driven almost entirely by BROAD match rather than a tight harvest-and-scale loop.

### Campaign Profitability (below 1.5x ROAS)

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|------:|------:|-----:|-------:|-------:|
| Safety chart - Auto | $53.07 | $31.18 | 0.59 | 70 | 2 |
| Campaign - 3/2/2026 09:52:58.432 | $21.64 | $29.97 | 1.38 | 59 | 1 |
| **Total below 1.5x threshold** | **$75** | | | | |

**Problem:** Absolute unprofitable spend is small ($75 over 90 days). A more important issue is the layer of campaigns running at 1.6-2.0x ROAS:

| Campaign | Spend | Sales | ROAS |
|----------|------:|------:|-----:|
| Tarp Automatic | $624 | $1,038 | 1.66 |
| Tarp Unique - 15 feb | $325 | $615 | 1.89 |
| Fishing Glasses 2025 | $1,480 | $2,852 | 1.93 |
| Reading glasses - Auto Loose | $199 | $394 | 1.98 |

Combined, these four campaigns account for $2,628 of the $2,970 account spend (88%) at a blended 1.86 ROAS. For a product with ~$12 AOV, 1.5-2.0x ROAS is break-even or slightly unprofitable after product cost and Amazon fees. The whole account is flirting with unprofitability because the scaling campaigns are structurally weak.

**Solution:** Restructure per Campaign Structure above - peel winning child-ASIN + winning-keyword combinations out into their own campaigns at 3-5x ROAS, then pull budget out of the catch-alls.

**Impact:** If 50% of the spend currently in the four big campaigns ($1,314) shifted to campaigns matching the Tarp 100 - 400 / B0BGJ82Q64 / B0F4R4YGCZ profile (3.5x ROAS), that alone would generate $4,600 in sales vs the current $2,460 on that same dollar. **+$2,140 in sales/90 days ($713/mo) from reallocation alone, before any new keyword or listing work.**

### Targeting Strategy

**Keyword vs Product Targeting:**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|-------------------|-------:|------:|------:|-----:|----:|----:|----:|
| Keyword Targeting | 4,379 | $2,977 | $5,628 | 1.89 | $14.32 | $0.68 | 8.97% |
| Product Targeting | 226 | $67 | $342 | 5.11 | $21.35 | $0.30 | 7.08% |

**Finding: Product targeting is at 5.11 ROAS with only 2% of the budget.** When the brand appears on competitor product pages (or its own as a defense), it converts at 7% CVR at a CPC less than half of keyword targeting. Yet it is a rounding error of total spend. This is a clean, under-exploited lever: build out product targeting campaigns against the 3-4 main competitors identified in Step 2 (Moose Supply tarp repair tape, Gear Aid Tenacious Tape, Edward Tools grommet kit, 103-piece grommet kit) and own defensive ads on Hippo's own top children to prevent competitor poaching.

**Match Type Breakdown:**

| Match Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|------------|-------:|------:|------:|-----:|----:|----:|----:|
| EXACT | 81 | $66 | $169 | 2.57 | $15.34 | $0.81 | 13.58% |
| PHRASE | 81 | $59 | $182 | 3.10 | $12.98 | $0.72 | 17.28% |
| BROAD | 2,058 | $1,438 | $2,653 | 1.84 | $14.58 | $0.70 | 8.84% |

**Finding: BROAD match absorbs 92% of manual keyword spend at the worst ROAS and worst CVR.** EXACT and PHRASE have 1.4-1.7x better ROAS and nearly 2x better CVR but together get only $125 over 90 days. This is a textbook harvest-and-scale failure: the converting search terms that BROAD has been surfacing have not been promoted into dedicated EXACT/PHRASE campaigns.

**Solution:** Mine the BROAD campaigns for winning search terms (see Product Level findings below), launch EXACT campaigns for each, reduce BROAD budget proportionally.

---

## Product Level (P0 - Tarp Accessories, B0CM72RSS8 parent; hero child B09TB3FPKW)

### P0 Campaign Map

Three campaigns advertise products under the P0 parent:

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|------:|------:|-----:|-------:|-------:|
| Tarp Automatic | $624.07 | $1,038.29 | 1.66 | 759 | 75 |
| Tarp Unique - 15 feb | $324.77 | $615.30 | 1.89 | 586 | 35 |
| Tarp 100 - 400 | $65.96 | $226.67 | 3.44 | 83 | 17 |
| **P0 Total** | **$1,015** | **$1,880** | **1.85** | **1,428** | **127** |

P0 gets **34% of total account ad spend** and delivers 32% of account ad sales. The account is actually slightly underweight on the P0 parent given that P0 is the largest organic revenue product. P1 (Magnifying Glasses, B0CGHS9B6W) takes 39% of spend on its own, driven by the Fishing Glasses 2025 catch-all campaign.

Within P0, hero child B09TB3FPKW gets the majority of the tarp spend (~$662 across the three campaigns). This is the right allocation.

### Blocker-Specific Findings

Step 3 identified **impression share as the primary blocker** on both Tier 1 (grommet queries) and Tier 2 (tarp repair tape queries). The PPC lever for impression share is: bid on the keywords where impression share is low. Step 3 also flagged Tier 2 impression share having collapsed 60% YoY, tracking the revenue decline.

#### Impression Share Blocker: Keyword Spend vs. Tier 1/2 Queries

Here is the current ad spend on the tagged Tier 1/2 search terms, pulled from the seller-level search term report (all tarp-related terms with at least 3 clicks):

**Tier 1 (grommet/eyelet reinforcement intent) - the gold mine:**

| Search Term | Tier | Spend | Sales | ROAS | Clicks | Orders | CVR | Notes |
|-------------|-----|------:|------:|-----:|-------:|-------:|-----|-------|
| tarp grommet reinforcement | Tier 1-adj | $15.13 | $105.70 | **6.99** | 25 | 9 | 36% | Perfect intent, tiny spend |
| grommet reinforcement | Tier 1-adj | $8.93 | $108.76 | **12.18** | 12 | 5 | 42% | Perfect intent, tiny spend |
| grommet reinforcement tape | Tier 1-adj | $4.51 | $32.91 | **7.30** | 5 | 2 | 40% | Perfect intent, tiny spend |
| tarp eyelet reinforcement | Tier 1-adj | $5.38 | $40.95 | **7.61** | 8 | 3 | 38% | Perfect intent, tiny spend |
| tarp grommet repair | Tier 1 | $6.82 | $21.94 | 3.22 | 9 | 2 | 22% | Strong ROAS, underspent |
| tarp grommet repair kit | Tier 1 | $10.67 | $25.96 | 2.43 | 16 | 2 | 13% | Healthy |
| grommets for tarps | Tier 1 | $48.02 | $65.87 | 1.37 | 59 | 5 | 8% | Spends the most, converts the worst |
| tarp grommet kit | Tier 1 | $53.38 | $42.88 | **0.80** | 73 | 4 | 5% | Biggest spend, unprofitable |
| tarp grommet kit heavy duty | Tier 1 | $23.21 | $69.84 | 3.01 | 29 | 4 | 14% | Healthy |
| tarp grommet fasteners | Tier 1 | $6.93 | $0 | 0 | 11 | 0 | 0% | 11 clicks, 0 orders |
| tarp grommets | Tier 1 | $14.05 | $0 | 0 | 18 | 0 | 0% | 18 clicks, 0 orders |

**Tier 2 (tarp repair / tape / patch intent):**

| Search Term | Spend | Sales | ROAS | Clicks | Orders | Notes |
|-------------|------:|------:|-----:|-------:|-------:|-------|
| tarp repair tape | $2.85 | $53.91 | **18.92** | 5 | 1 | Perfect intent, $2.85 spend |
| tarp patch kit heavy duty | $2.31 | $64.87 | **28.08** | 3 | 5 | Perfect intent, $2.31 spend |
| tarp patch | $7.92 | $44.97 | 5.68 | 11 | 2 | Healthy |
| tarp patch kit | $4.23 | $14.99 | 3.54 | 6 | 1 | Healthy |
| tarp tape | $10.73 | $0 | 0 | 14 | 0 | 14 clicks, 0 orders |
| tarp repair kit | $6.61 | $0 | 0 | 9 | 0 | 9 clicks, 0 orders |
| tarp tape heavy duty waterproof | $8.79 | $31.91 | 3.63 | 13 | 4 | Healthy |
| tarpaulin tape | $2.24 | $10.97 | 4.90 | 3 | 1 | Healthy |

**Problem: The most impactful Tier 1 and Tier 2 search terms are funded at $2-$15 each over 90 days, while a single unprofitable search term ("tarp grommet kit," 0.80 ROAS) consumes $53.**

The "reinforcement" intent queries (tarp grommet reinforcement, grommet reinforcement, tarp eyelet reinforcement, grommet reinforcement tape) are the brand's natural fit - they describe exactly what the product is - and they convert at 36-42% with 7-12x ROAS. They collectively got $34 of spend over 90 days. At the same time, "tarp grommet kit" (which is a substitute-intent query - people want brass grommet kits with tools, not reinforcement patches - see Step 2 competitive landscape) got $53 and returned 0.80 ROAS.

**Solution:**
1. **Create a dedicated EXACT match campaign** for the reinforcement-intent cluster: `tarp grommet reinforcement`, `grommet reinforcement`, `grommet reinforcement tape`, `tarp eyelet reinforcement`, `tarp reinforcement tape`. Target $100-200/mo on these as a starting point. At current ROAS this would generate $700-2,400 in sales from terms that today generate $288.
2. **Add these as negative keywords or cap them:** `grommet kit` (non-tarp), `grommets for fabric`, `plastic grommets`, `grommet tool kit`, `tarp clips`, `tarp connectors`, `landscaping tarp`. These bleed spend on the substitute-grommet-kit and off-product traffic.
3. **Lower bids** on `tarp grommet kit` (poor ROAS) and `grommets for tarps` (borderline). Let EXACT match on reinforcement terms pick up the volume.

**Impact:** Reinforcement cluster scaled from $34 (90 days) to $400 (90 days) at its current average ROAS of ~8x → **$3,200 incremental sales/90 days, ~$1,067/month.** That alone recovers a meaningful share of the P0 revenue decline documented in Step 3. Simultaneously negating the substitute/irrelevant cluster recovers another ~$100 of wasted spend per 90 days.

#### Secondary: Tier 2 Visibility Recovery

Step 3 noted that Tier 2 impressions collapsed from ~2,000/mo (Apr 2025) to ~700/mo (Mar 2026). Ad data only goes back to Jan 2026 so the cause cannot be confirmed directly from the ad side. But the current pattern is consistent: Tier 2 terms like `tarp tape`, `tarp repair tape`, `tarp repair kit` each get $3-$11 of spend, roughly 10-100x less than Tier 1 terms. These are also high-intent queries that should be funded.

**Solution:** Same recipe - EXACT match campaign on `tarp repair tape`, `tarp patch kit`, `tarp tape heavy duty waterproof`, `tarp patch`, `tarpaulin tape` with $100-200/mo.

### Listing-Side Note (Context)

Step 2 flagged the P0 listing's A+ content (text-heavy, typos) and the missing video. The ad data here shows CTR and CVR on well-targeted queries are already very high (e.g., 36-42% CVR on reinforcement queries). The listing is not blocking conversion on correctly-targeted traffic. The **primary** problem is keyword selection/budget allocation. Listing fixes from Step 2 will help CVR on broader Tier 2 traffic (where it's more of a substitute-consideration shopper) once impression share is scaled, but they are not a prerequisite for the PPC scaling above.

## Insights

- P0 (Grommet Reinforcement Tape): "Reinforcement"-intent search terms (tarp grommet reinforcement, grommet reinforcement, tarp eyelet reinforcement, grommet reinforcement tape) collectively got $34 in ad spend over 90 days and converted at 36-42% CVR with 7-12x ROAS. These are the single biggest recoverable revenue lever in the account.
- Account-wide: BROAD match absorbs 92% of manual keyword spend at 1.84 ROAS while EXACT and PHRASE have 2.57 and 3.10 ROAS respectively. The harvest-and-scale loop is not running; winning search terms inside BROAD campaigns have not been promoted to dedicated EXACT campaigns.
- Account-wide: Product targeting runs at 5.11 ROAS with only 2% of spend. This is a clean lever to expand defensive and competitor-conquesting placements.
- Campaign structure: catch-all campaigns (Fishing Glasses 2025, Tarp Automatic, Tarp Unique) pool multiple child ASINs and starve the high-ROAS children inside them (B0BGJ82Q64 at 3.92 ROAS gets $45 while B09TB3FPKW at 1.58 ROAS gets $439 inside the same Tarp Automatic campaign).

## Things to Investigate Further

- Confirm on the call whether there was a deliberate ad spend reduction on Tier 2 tarp queries during mid-2025. The YoY impression drop pre-dates the ad window we have visibility into.
- Quantify the irrelevant-traffic waste more precisely by pulling Q717 for `Tarp Automatic` to see exactly which search terms are being matched by BROAD inside that campaign.

## Questions for the Seller

- Have any ad campaigns been paused or deprioritized since mid-2025 that we cannot see in the current enabled set? The Tier 2 visibility loss documented in SQP does not have an obvious explanation in the current active campaigns.
