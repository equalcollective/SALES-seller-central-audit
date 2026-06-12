# Ad Analysis - Abokichi Inc. (Canada)

## Important: Date Window & Frame

Ad data window: **Feb 20 – May 19, 2026** (89 days). Ads launched in Feb 2026 after no spend in 2025, so this is the entire ad history. CA ad spend over 90 days is **~$6.3K** vs the US storefront's **~$147 YTD 2026** - the CA account is actively managed, ramped, and profitable. The framing in this section is **scale & allocation**, not "the seller isn't advertising" (which was the US frame).

## Account Level

### Campaign Structure

**4 ENABLED campaigns**, all Manual:

| Campaign | Product | Spend | Sales | ROAS | ACoS | Orders | CPC | CTR | CVR |
|----------|---------|-------|-------|------|------|--------|-----|-----|-----|
| Spicy Chili Miso - Manual | B07JGJXTK8 (P0 Spicy Single) | $4,783 | $15,827 | 3.31 | 30.2% | 771 | $0.93 | 1.31% | 15.0% |
| Chili Miso - Manual Jun2025 | B07JWCDC4D (P1 Mild) + B088YNXZ4B (Mild 2-pack) | $1,073 | $4,677 | 4.36 | 22.9% | 197 | $0.76 | 0.56% | 13.9% |
| [CurryMiso] CA-KW-Jun022025 | B07JGJXYHP (P3 Curry) | $223 | $710 | 3.19 | 31.4% | 31 | $0.75 | 0.55% | 10.4% |
| Campaign with presets - B07MCYB2VV | B07MCYB2VV (P2 Variety Pack) | $55 | $1,860 | **34.12** | 2.93% | 47 | $0.24 | 2.10% | 20.4% |
| **Total** |  | **$6,133** | **$23,074** | **3.76** | **26.6%** | 1,046 | | | |

**Observations:**
- All 4 campaigns are profitable (above 1.5x ROAS). Account-level ROAS 3.76 is healthy.
- One campaign per ASIN family, no overstuffed campaigns. Structure is clean.
- **No campaign overstuffing problem** — this is unlike many sellers we audit.
- The Variety Pack campaign at **34.12 ROAS on $55 spend** is the most extreme under-funded campaign in the account. Same hero-pattern we noted in Step 1: the SKU does $5-7K/mo organically, gets virtually no PPC, and where PPC was tested it returns ~$34 for every $1 spent.

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|--------|-------|-------|------|-----|-----|-----|
| Automatic | – | – | – | – | – | – | – |
| Manual | 7,067 | $6,133 | $23,074 | 3.76 | $22.06 | $0.87 | 14.80% |

**100% manual, 0% auto.**

> **Finding: The account is running 100% manual with no Auto campaign for discovery.**
>
> **Problem:**
> - All 4 enabled campaigns are Manual.
> - Without Auto, the algorithm has no place to surface emerging high-intent search terms for harvesting into Manual.
> - The targeting-level data shows the P0 Manual campaign already converts at 25-46% CVR on the 5 Tier 1 keywords it does include (e.g., "spicy chili miso" 46% CVR, "chili miso" 33%, "spicy miso" 44%). The hypothesis that there are *more* of these Tier 1 long-tail variants Amazon could surface for the brand is strong.
>
> **Solution:**
> - Launch a single Auto campaign for the chili miso oil hero line at $10-15/day with a tight negative-keyword list (lao gan ma, lee kum kee, umami, chilli crunch oil, japanese curry - all of which have spent in Manual and returned zero).
> - Set a 30-day learning window; pull the converting search terms into the existing Manual Exact campaign.
>
> **Impact:**
> - At a conservative 3.0 ROAS on $300/mo Auto spend, the campaign produces ~$900/mo in incremental sales while feeding a perpetual stream of new converting Exact targets into Manual.
> - Even more importantly, the search-term harvest creates a 6-12 month compounding edge as new long-tail Tier 1 variants get scaled.

### Campaign Profitability

All 4 enabled campaigns are above 1.5x ROAS. **No profitability cleanup needed.** This is unusual — most CA-equivalent accounts have at least one bleeder. Moving on.

### Targeting Strategy

**Keyword vs Product Targeting:**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|--------------------|--------|-------|-------|------|-----|-----|-----|
| Keyword Targeting | 7,178 | $6,275 | $23,230 | 3.70 | $22.04 | $0.87 | 14.68% |
| Product Targeting | 10 | $5.93 | $77.96 | **13.15** | $25.99 | $0.59 | **30.00%** |

> **Finding: Product Targeting is essentially zero ($6 spend over 90 days) despite 13x ROAS in the small sample available.**
>
> **Problem:**
> - 99.9% of ad spend goes to Keyword Targeting.
> - The micro-sample of Product Targeting shows 30% CVR and 13x ROAS.
> - The brand has clear competitive-defense and competitor-attack ASINs available (Fly By Jing, Lao Gan Ma, Momofuku, S&B La-Yu on CA where present).
>
> **Solution:**
> - Build a Sponsored Products Product Targeting campaign with three target groups:
>   1. **Own ASINs (defense)** — bid on Abokichi's own listings so competitors can't poach browsers.
>   2. **Adjacent Japanese pantry ASINs** — premium miso pastes, ramen kits.
>   3. **Competitor chili oil / chili crisp ASINs** where Abokichi's Japanese-miso angle is a clear differentiator.
> - Cap daily at $10-15 to start, scale on ROAS.
>
> **Impact:**
> - At a conservative 3-5x ROAS once volume scales, $300-450/mo of Product Targeting spend produces $1,000-2,250/mo in incremental sales, with the additional value of defensive moat-building.

**Match Type Breakdown:**

| Match Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|------------|--------|-------|-------|------|-----|-----|-----|
| EXACT | 1,863 | $1,715 | $6,606 | **3.85** | $20.65 | $0.92 | **17.18%** |
| PHRASE | 1,624 | $1,505 | $5,197 | 3.45 | $21.30 | $0.93 | 15.02% |
| BROAD | 3,616 | $2,991 | $11,309 | 3.78 | $23.37 | $0.83 | 13.38% |

Match type performance is healthy across the board (all 3 above 1.5x). Exact has the best CVR (17.18%) and ROAS (3.85), as expected. Broad gets the lion's share of spend ($2,991, ~49%) - typical for a brand that's still discovering its converting keyword universe.

The pattern is fine but suggests another harvest-and-scale opportunity: the Broad-converting search terms should be migrated to Exact bids. Step 4f below shows specific candidates.

### Account-Wide Placement Distribution

| Placement | Impressions | Clicks | CTR | Spend | Sales | ROAS | CVR |
|-----------|-------------|--------|-----|-------|-------|------|-----|
| **Top of Search** | 64,697 | 4,575 | **7.07%** | $4,693 | $11,987 | 2.55 | 11.87% |
| Rest of Search | 203,074 | 1,062 | 0.52% | $526 | $1,574 | **2.99** | 6.97% |
| Product Pages | 470,416 | 1,543 | 0.33% | $1,059 | $1,303 | **1.23** | 3.82% |
| Off Amazon | 2,551 | 5 | 0.20% | $0.71 | $0 | 0 | 0% |

> **Finding: Product Pages placement is barely profitable (1.23 ROAS) and consumes 17% of spend.**
>
> **Problem:**
> - Product Pages: $1,059 spent over 90 days, $1,303 in sales, 1.23 ROAS - barely break-even, below the 1.5 profitability floor.
> - Top of Search converts at 11.87% CVR (3x the Product Pages CVR of 3.82%) but is capped on impressions.
>
> **Solution:**
> - Reduce Product Pages bid modifier toward 0% on the P0 campaigns.
> - Increase Top of Search bid modifier (currently presumably +0%) to +50-100% to win more premium impressions.
>
> **Impact:**
> - Shifting ~$700/mo from Product Pages (1.23 ROAS) to Top of Search (2.55 ROAS) at the same total budget produces roughly $1,800/mo of additional sales (~$900/mo Product Pages would have made vs ~$1,800/mo at Top of Search ROAS).

## Product Level (P0)

### P0 Campaign Map

| Campaign | Spend | Sales | ROAS | Clicks | Orders | CPC | CTR | CVR |
|----------|-------|-------|------|--------|--------|-----|-----|-----|
| Spicy Chili Miso - Manual | $4,783 | $15,827 | 3.31 | 5,125 | 771 | $0.93 | 1.31% | 15.04% |
| 20230424- AUTO (legacy, low spend) | $50 | $97 | 1.95 | 58 | 5 | $0.86 | 0.36% | 8.62% |
| 20230901 - Manual - Keyword (legacy) | $63 | $39 | 0.62 | 29 | 2 | $2.18 | 0.42% | 6.90% |

Total P0 (B07JGJXTK8) ad spend: ~$4,896 (~80% of total account spend, appropriate given P0 represents ~57% of total chili miso oil revenue).

The two 2023 legacy campaigns are tiny but the Manual-Keyword one is running at 0.62 ROAS — should be paused or restructured. Spend is small ($63) so this is a hygiene item, not a major lever.

### Blocker-Specific Findings

#### Impression Share Blocker: Tier 1 Keyword Bidding

Section 4 of the SQP analysis identified **impression share as the primary Tier 1 blocker**. Brand impression share on Tier 1 is 3.9% (Apr 2026) vs a 24-27% cap (3 children rank). The PPC lever is to bid on Tier 1 keywords.

Current spend distribution on Tier 1 keywords inside the P0 campaign (top entries by ROAS):

| Tier 1 Keyword | Match Type | Spend | Sales | ROAS | CVR | Clicks |
|----------------|------------|-------|-------|------|-----|--------|
| miso chili oil | EXACT | $0.78 | $151.43 | **194.14** | 41.18% | 17 |
| spicy miso chili oil | BROAD | $0.06 | $18.99 | 316.50 | 100% | 1 |
| spicy miso | PHRASE | $0.51 | $113.94 | **223.41** | 100% | 2 |
| spicy chili miso | BROAD | $2.71 | $260.95 | **96.29** | 46.15% | 26 |
| chili miso | EXACT | $3.63 | $266.91 | **73.53** | 33.33% | 30 |
| spicy miso | EXACT | $2.86 | $73.99 | 25.87 | 44.44% | 9 |
| miso chili oil | PHRASE | $17.78 | $218.93 | 12.31 | 25.00% | 36 |
| crispy chili oil | EXACT | $10.71 | $76.96 | 7.19 | 30.77% | 13 |

Tier 1 total spend in P0 campaign: **~$40** over 90 days, producing ~$1,180 in sales (ROAS ~29x).

> **Finding: The Tier 1 keywords where Abokichi has a near-perfect product-intent match are getting trivial spend ($40 over 3 months) at extreme ROAS (12-300x).**
>
> **Problem:**
> - "chili miso" EXACT: 33% CVR, 73x ROAS, $3.63 total spend over 90 days.
> - "spicy miso" PHRASE: 100% CVR (small sample), 223x ROAS.
> - "miso chili oil" EXACT: 41% CVR, 194x ROAS, $0.78 spend.
> - All 8 Tier 1 brand-fit keywords combined have eaten **less than $40** while the broader-intent chili crisp / chili oil keywords have eaten $3,000+.
>
> **Solution:**
> - Create a dedicated Manual Exact Match campaign for the 14 Tier 1 keywords (from SQP Step 3).
> - Suggested bid +30-50% to win impression share at the cap.
> - Top of Search bid modifier +100%.
> - Daily budget $25-40/day for this CA-scale account.
>
> **Impact:**
> - At even a conservative blended 10x ROAS (vs the current 12-300x small-sample), $800/mo of dedicated Tier 1 spend would produce ~$8,000/mo in incremental sales.
> - Just as importantly, this drives organic ranking and review velocity on Tier 1, which is where Abokichi's defensible niche lives.

#### Spend Allocation Problem: Broad Category Keywords

Where the P0 spend currently goes (top 10 spenders, descending):

| Keyword | Match | Spend | Sales | ROAS | CVR |
|---------|-------|-------|-------|------|-----|
| chili crisp | BROAD | $924 | $2,470 | 2.67 | 13.89% |
| chili | PHRASE | $824 | $2,768 | 3.36 | 15.91% |
| chili oil | EXACT | $550 | $2,292 | 4.17 | 20.28% |
| chilli oil | EXACT | $456 | $1,694 | 3.71 | 16.20% |
| miso | BROAD | $440 | $666 | **1.51** | 11.58% |
| chilli crisp | BROAD | $422 | $1,338 | 3.17 | 13.55% |
| chili | BROAD | $281 | $698 | 2.48 | 12.77% |
| chili oil | BROAD | $216 | $871 | 4.03 | 15.50% |
| miso | PHRASE | $203 | $750 | 3.70 | 19.32% |
| chilli oil | PHRASE | $85 | $266 | 3.14 | 13.73% |

Observations:
- **"miso" BROAD: $440 spend at 1.51 ROAS** is the marginal target. It is right at the unprofitability threshold and given the SQP finding that Tier 2 conversion is structurally weak, this spend is unlikely to improve.
- **"chili" PHRASE: $824 spend, 3.36 ROAS, 15.91% CVR** — surprisingly profitable. But "chili" is a category-level term; this is converting because CA shoppers searching "chili" on a smaller marketplace are more likely to land on Abokichi than US shoppers. The CA-specific market dynamic is at work here.
- **"chili oil" EXACT: $550 at 4.17 ROAS, 20% CVR** — strong. Keep as is.

> **Finding: $440 is being spent monthly-equivalent on "miso" BROAD at near-unprofitable 1.51 ROAS.**
>
> **Problem:** "miso" BROAD captures a lot of impression but converts poorly because the searcher wants culinary miso paste, not a chili miso oil. Same Tier 2 intent-mismatch problem flagged in SQP Step 3.
>
> **Solution:** Move "miso" BROAD to PHRASE (already running at 3.70 ROAS, 19% CVR) and let the long-tail variations compete. Negative-match "miso paste", "white miso", "red miso", "miso ramen broth" in the campaign.
>
> **Impact:** Recovers ~$147/mo of marginal spend; redirects to Tier 1 dedicated campaign. Net: same total spend, materially higher ROAS.

#### Negative Keyword Candidates (P0 campaign)

Targets with meaningful spend and zero conversion:

| Target | Match | Spend | Clicks | Orders |
|--------|-------|-------|--------|--------|
| umami | PHRASE | $13.32 | 16 | 0 |
| chilli crunch oil | EXACT | $11.88 | 16 | 0 |
| lao gan ma | PHRASE+BROAD | $7.06 | 6 | 0 |
| japanese chili | BROAD | $0.44 | 1 | 0 |
| lee kum kee | EXACT | $1.30 | 4 | 0 |
| chili garlic oil | BROAD | $4.83 | 5 | 0 |
| japanese spice | PHRASE | $1.94 | 2 | 0 |

> **Finding: ~$41 of P0 spend on targets that have never converted.**
>
> **Solution:** Add these to negative keyword exact list across all campaigns. Total recovery is small but compounds when the new Auto campaign launches (these would otherwise re-emerge).

## Beyond P0: Variety Pack Underspending

The Variety Pack campaign deserves explicit callout:

| Metric | Variety Pack Campaign |
|--------|------------------------|
| Spend (90d) | $55 |
| Sales (90d) | $1,860 |
| ROAS | **34.12** |
| CVR | 20.35% |
| Orders | 47 |

> **Finding: The Variety Pack (B07MCYB2VV) earns $34 for every $1 of PPC spend and is funded with $55/quarter.**
>
> **Problem:** The Variety Pack does $5-7K of organic sales per month (per Step 1) and has 9 months of accumulated PPC test data showing it converts at 20% with extreme efficiency. It's running on autopilot at $0.61 per day.
>
> **Solution:** Either (a) scale the Variety Pack campaign to $10-15/day with the existing structure, or (b) build a dedicated keyword campaign targeting "japanese chili oil gift set", "miso oil variety", "japanese condiment gift" — gift / variety / sampler-intent terms that aren't in the current Tier 1.
>
> **Impact:** Conservatively, scaling to $300/mo at half the current ROAS (call it 15x) generates $4,500/mo of incremental sales. The actual upside is likely higher because the Variety Pack also has no video (Step 2 listing fix would add CVR on top of PPC).

## Key Observations from Step 4

**Insights:**
- **CA ads are well-managed and profitable, just under-allocated.** All 4 enabled campaigns above 1.5 ROAS, no campaign structure problems, no auto-vs-manual harvest gap *within* what's running. The work is allocation, not cleanup.
- **The Tier 1 brand-fit keyword campaign is the single biggest unspent opportunity.** $40 of spend over 90 days on 8 Tier 1 keywords returned $1,180 in sales at 12-300x ROAS. A dedicated $800/mo campaign on the 14 Tier 1 keywords (per Step 3) is the highest-conviction action in this audit.
- **Product Targeting is unfunded.** $5.93 in 90 days. The 13x ROAS in the micro-sample is consistent with the Step 3 finding that Abokichi converts well when the buyer is already in the category. Both defense (own ASINs) and offense (competitor ASINs) are viable.
- **Product Pages placement is the only sub-1.5 ROAS issue in the account.** $1,059 spent at 1.23 ROAS. Cut bid modifier to zero.
- **Variety Pack is doing $34 ROAS on $0.61/day spend.** Scaling is a directly testable hypothesis with a clear control (current micro-test) and a clear upside path.
- **No Auto campaign means no continuous keyword discovery.** The existing converting Tier 1 keywords were found manually; there are likely more long-tail variants Amazon would surface with a small Auto budget.

**Things to Investigate:**
- Why ads launched only in Feb 2026 with no prior CA spend. This affects how aggressively to recommend scaling — if there's a deliberate margin or cash-flow constraint, the velocity of the proposed Tier 1 ramp and Product Targeting launch needs to be paced accordingly.
- The legacy 2023 "20230424- AUTO" and "20230901 - Manual - Keyword" campaigns are still enabled at sub-2 ROAS. Whether to pause or repurpose them.

**Questions for the Seller:**
- "Tier 1 brand-fit keywords (chili miso, spicy miso, miso chili oil) are converting at 25-46% CVR and 12-300x ROAS in your existing P0 campaign but each one is getting under $20 of spend per 90 days. Is there a deliberate reason these aren't scaled, or has the keyword harvest just not been a priority yet?"
- "Product Targeting (Sponsored Products at the ASIN level, both defensive on your own ASINs and offensive on competitor ASINs) has effectively zero spend on the CA account. Has this been tested before and rejected, or is it just untouched?"
- "Are the two legacy 2023 CA campaigns (20230424-AUTO, 20230901-Manual-Keyword) still active by intent or by oversight? Both are at sub-2 ROAS and trickling spend."
- "What's the unit COGS / contribution margin on the Spicy single at $19.99 retail? At current 3.31 ROAS on P0 we want to confirm what the break-even ROAS floor actually is so we can set bid targets correctly."
