# Ad Analysis: ReadyRest

## Overview

ReadyRest has **zero ad data** in our system (Step 1 confirmed `ads_day_count = 0`). Per the 90-day retention rule, this could mean the seller has run no ads in the last 90 days, or has never advertised on Amazon at all. Either way, there are no campaigns, search terms, placements, or budgets to audit. The actual seller question (have you ever advertised, and if so when did you stop and why) is open in the Questions for the Seller bucket.

This section reframes Step 4 as: given the SQP findings, what should PPC look like for ReadyRest? Every recommendation here ties back to a specific blocker identified in [SQP Analysis](./SQP%20Analysis.md).

## The Opportunity, Reframed

From SQP, the picture is unusually clean for a single-product brand:

- **Tier 1 ("shotgun rest"):** Brand impression share 2.5% of an ~8-9% cap. Brand CTR is 5x industry, ATC is at industry, CVR is above industry. The listing converts excellently when shoppers see it. The only thing missing is impressions.
- **Tier 2 (use-case accessory queries):** $109K/mo market with proven brand traction across multiple keywords annually. Shotgun holster generated 14 brand purchases over the last 12 months (second-best converter after Tier 1). Upland hunting gear, dove hunting gear, skeet shooting accessories, and bird hunting accessories all show meaningful cart-adds. The volume-weighted CVR is below industry, but that's an average dragged down by traffic on weaker tail queries - the right play is to test the full set in PPC and prune by ACoS, not exclude upfront.
- **Tier 3 (general activity queries):** Below-industry CVR; not worth PPC budget.

PPC for this brand is not a campaign-structure-optimization problem (there are no campaigns to optimize). It is a clean-slate launch where the question is: **"Where should the first dollar go, and what does the next 90 days of ramp-up look like?"**

## Recommended Campaign Structure (Day 1 Plan)

### Campaign 1: Branded Defense (small, defensive)

**Goal:** Stop competitors from bidding on "ready rest", "readyrest", and brand-variant queries to poach the brand's own customers.

**Budget:** 2-3% of total ad budget. From CLAUDE.md: branded ads are not a growth lever; this is purely protective.

| Keyword | Match Type | Notes |
|---------|-----------|-------|
| ready rest | Exact | 197 vol Dec, 222 vol Nov, smaller off-season |
| readyrest | Exact | Variant spelling |
| ready rest shotgun rest | Exact | Long-tail brand-product pair |
| readyrest shotgun rest | Exact | Variant |

Bidding should be moderate, not aggressive. The goal is to win the Top of Search slot on the brand's own name, not to outbid for vanity.

### Campaign 2: Tier 1 Hero - "shotgun rest" (PRIMARY GROWTH CAMPAIGN)

**Goal:** Close the gap between the brand's 2.5% impression share and the ~8-9% cap on the single most relevant keyword in the brand's universe.

| Keyword | Match Type | Avg Monthly Volume | Brand Currently |
|---------|-----------|-------------------|-----------------|
| shotgun rest | Exact | 190 | 2.48% imp share |
| shotgun rest | Phrase | (overlapping volume) | - |

**Bid strategy:** Aggressive on Top of Search bid modifier. From CLAUDE.md domain knowledge: Top of Search converts better, and on a niche, low-competition query, ToS bids may be cheaper than expected. The product is at $59.99 with proven 7%+ CVR on this query; per-click economics support a strong opening bid.

**Per-click economics on Tier 1 (sanity check):**
- Brand CVR on Tier 1 (12-month): 6.98%
- AOV: $59.99
- Implied per-click revenue: $59.99 x 6.98% = $4.19 per click
- Break-even CPC at 100% margin: $4.19. Real margin (after COGS, FBA fees) on a $60 aluminum product is likely 30-50%, so break-even CPC is $1.25-$2.10. There is meaningful headroom.

**Budget:** $5-10/day initial. Volume is low; budget unlikely to fully spend in the first weeks.

### Campaign 3: Tier 2 Full Set (test, then prune)

**Goal:** Capture Tier 2 demand. Annual data shows real brand traction across the full set, not just the rest-adjacent queries. Launch wide, prune by ACoS.

| Keyword | Match Type | Avg Monthly Volume | Annual Brand Cart-Adds | Notes |
|---------|-----------|-------------------|------------------------|-------|
| shotgun holster | Exact | ~1,400 | 43 (14 purchases) | Highest-converting Tier 2 keyword, prioritize |
| shotgun accessories | Exact + Phrase | ~37,000 | high volume | Broad anchor |
| trap shooting accessories | Exact | ~6,000 | 26 cart-adds class | - |
| skeet shooting accessories | Exact | ~4,500 | 26 | - |
| sporting clays accessories | Exact | ~5,000 | - | - |
| bird hunting accessories | Exact | ~2,500 | 19 | - |
| upland hunting gear | Exact | ~5,500 | 31 | Strong Tier 2 traction |
| upland hunting accessories | Exact | ~900 | 2 | Lower volume |
| dove hunting gear | Exact | ~13,000 (peak) | 29 | Strong |
| pheasant hunting gear | Exact | ~6,000 | varies | Strong in fall |
| pheasant hunting accessories | Exact | ~1,500 | varies | - |

**Bid strategy:** Conservative initial bids across the full set. Exact match first. The brand's CTR is above industry on Tier 2, so clicks come; the question per keyword is whether they convert. Apply a tight ACoS gate: pause any keyword that does not deliver under 40% ACoS by end of Week 4. Scale up the keywords that do.

**Budget:** $10-15/day combined initial, scaling per keyword as ACoS data comes in.

### Campaign 4 (deferred): Sponsored Brands Video

**Goal:** Make use of the existing 49-second product video to capture "what is this thing?" curiosity on Tier 2 queries. The product's value prop is hard to grasp from a static image, and video addresses that.

**Defer to Week 4-5 of ramp:** Launch only after Campaigns 1-3 have produced 30 days of clean data. SBV typically requires Brand Store, which is a Step 2 listing-quality opportunity (not yet built).

## Campaigns Explicitly NOT Recommended

The following keywords look attractive on volume but should not be targeted:

| Keyword | Vol/mo | Why Not |
|---------|--------|---------|
| shooting rest | 31,000 | Refers to rifle bench rests for sighting in / target shooting, not the same product |
| shotgun sling | 30,000 | A carry strap, not a rest. Wrong product. |
| shotgun shell holder | 32,000 | Ammo storage, not a rest. Wrong product. |
| hunting accessories | 812,000 | Far too broad; CVR will be near zero |
| pheasant hunting (Tier 3) | varies | Activity-research, below-industry CVR confirmed |
| dove hunting (Tier 3) | up to 30,000 | Same as above |

These are common mistakes a new advertiser would make on volume alone. The SQP data confirms each of them is intent-mismatched.

## Expected 90-Day Trajectory

This is a back-of-envelope projection, not a guarantee. Assumptions: aggressive Tier 1 bid wins ToS placement; Tier 2 aligned subset converts at 60-70% of organic CVR (intent-filtered).

| Period | Focus | Expected Monthly Lift in P0 Revenue |
|--------|-------|-------------------------------------|
| Weeks 1-2 | Branded Defense + Tier 1 launch | +$200-400/mo from Tier 1 incremental impressions |
| Weeks 3-4 | Add full Tier 2 set, optimize bids by ACoS | +$500-1,500/mo combined |
| Weeks 5-8 | Scale Tier 1 toward 5-7% impression share, scale Tier 2 winners (esp. shotgun holster), prune underperformers | +$1,500-3,500/mo combined |
| Weeks 9-12 | Add Sponsored Brands Video on Brand Store, retarget cart-abandoners | +$2,500-5,500/mo combined |

Off-season caveat: April-July is the seasonal trough across the entire market (SQP confirms this). The dollar lift in Q2 will be smaller in absolute terms; the goal during off-season is to ramp the campaigns, optimize bids, and have them at scale by Aug-Sep when the next hunting season begins. The real revenue payoff is positioning for the Aug-Dec season, where the SQP search-volume curve lifts 2-3x.

## Findings (Existing Account)

There are no findings on the existing account because there is no existing account. The pre-call question to the seller is whether ads have ever run; if yes, what was attempted and why it stopped.
