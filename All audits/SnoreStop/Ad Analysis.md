# Ad Analysis - SnoreStop USA

**Data window:** 2026-01-18 to 2026-04-16 (90 days, matching full ad data availability)

**Important context:** Seller Analytics ad data is available from 2026-01-18 onward. This does not mean ads only started on that date - it is the retention window of the advertised product report. Historical ad strategy is a question for the seller.

## Account-Level Findings

### Campaign Structure

**Finding: One broad-match campaign absorbs 96% of all ad spend. High-ROAS exact and narrow-match keywords are starved of budget.**

**Problem:**
- 4 campaigns running. `M-G: All products - Broad Match` alone accounts for $808 of the $842 total ad spend (96%).
- Inside that one campaign, the broad match `+snore` keyword eats $694 (86%) of the campaign's budget at ROAS 1.86 - barely profitable.
- Narrow, high-ROAS targets sit inside the same campaign with trivial budget:

| Campaign | Targeting | Match Type | Spend | Sales | ROAS | Clicks | Orders |
|----------|-----------|-----------|-------|-------|------|--------|--------|
| M-G: All products - Broad Match | `+snore` | BROAD | $694.28 | $1,289.22 | 1.86 | 612 | 88 |
| M-G: All products - Broad Match | `anti snore tablets for pets` | BROAD | $14.05 | $66.63 | 4.74 | 16 | 5 |
| M-G: All products - Broad Match | `snore stop dogs` | EXACT | $13.09 | $100.59 | 7.68 | 13 | 4 |
| M-G: All products - Broad Match | `dog snoring relief` | BROAD | $12.23 | $14.99 | 1.23 | 12 | 1 |
| M-G: All products - Broad Match | `+anti +snoring` | BROAD | $10.32 | $14.99 | 1.45 | 10 | 1 |
| M-G: Pet chewable tablets | (exact keywords) | EXACT | $9.95 | $74.95 | **7.53** | 11 | 4 |

- Also, all three top-converting search terms identified in Step 3 (`anti snoring for dogs`, `stop dog snoring`, `dog snoring relief`) are being captured via broad match on `+snore` instead of being isolated into their own exact-match campaigns.

**Solution:**
- Restructure so each proven keyword gets its own exact-match campaign with dedicated budget. Start with the 3-5 highest-ROAS search terms (see Product-Level section).
- Narrow `+snore` into a specific pet-intent phrase target (e.g. `+snore +dog` or `+pet +snore`) to stop paying for human-snoring clicks leaked by the broad match.
- Fund the existing `M-G: Pet chewable tablets` exact campaign properly. At ROAS 7.53 it is carrying almost zero spend.

**Impact:**
- Current: `+snore` broad delivers 88 orders at ROAS 1.86 on $694 spend. `snore stop dogs` exact delivers 4 orders at ROAS 7.68 on $13 spend.
- If $100 is shifted from `+snore` broad to `snore stop dogs` exact (or to a new exact-match campaign on a proven search term like `stop dog snoring` at ROAS 4.05), that $100 of ad spend generates approximately $400 in sales instead of approximately $186. Net gain of roughly $215 in sales for the same $100 of ad budget. Scale this across the top 3-5 proven terms and the effect compounds.

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|--------|-------|-------|------|-----|-----|-----|
| Automatic | 35 | $23.28 | $10.83 | 0.47 | $10.83 | $0.67 | 2.86% |
| Manual | 732 | $818.82 | $1,647.15 | 2.01 | $15.11 | $1.12 | 14.89% |

Manual drives 97% of spend and sales at a healthy 2.01x ROAS. The auto campaign is tiny and unprofitable (1 order on 35 clicks).

**Finding: Auto is currently vestigial, not a discovery engine.**

**Problem:** At $23 spent in 90 days, the auto campaign is too small to discover anything meaningful. It is generating a single order at negative ROAS.

**Solution:** Either pause it entirely or give it a real budget (e.g. $100-200/month) with the explicit purpose of mining new converting search terms. Currently it is the worst of both worlds: too small to discover, not small enough to ignore.

**Impact:** Pausing recaptures $23 of unprofitable spend. Scaling it intentionally for discovery is a medium-term opportunity if the account is willing to accept short-term unprofitability to harvest new keywords.

### Campaign Profitability

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| A-G: All (Auto) | $23.28 | $10.83 | 0.47 | 35 | 1 |
| M-G: All products - Broad Match | $808.05 | $1,572.20 | 1.95 | 720 | 105 |
| M-G: Pet chewable tablets | $9.95 | $74.95 | 7.53 | 11 | 4 |
| M-G: Pet spray | $0.82 | $0.00 | 0.00 | 1 | 0 |

The large broad-match campaign is at ROAS 1.95, which is *marginally* profitable but below the 1.5x safety buffer when you isolate what's going to the spray product specifically. Breaking this campaign apart by advertised product reveals the real leak:

| Advertised Product | Campaign | Spend | Sales | ROAS | Clicks | Orders |
|--------------------|----------|-------|-------|------|--------|--------|
| P0 (Tablets, B004GW338E) | M-G: All products - Broad Match | $680.01 | $1,479.75 | 2.18 | 593 | 98 |
| P1 (Spray, B000FL43XY) | M-G: All products - Broad Match | $128.04 | $92.45 | **0.72** | 127 | 7 |
| P1 (Spray, B000FL43XY) | A-G: All | $14.13 | $10.83 | 0.77 | 21 | 1 |

**Finding: The Spray product (P1) is burning budget inside the shared broad-match campaign.**

**Problem:** $142 spent advertising the spray in 90 days returned $103 in sales. ACoS 139% - the ad cost exceeds the product revenue before accounting for product cost.

**Solution:** Stop advertising the spray through the shared broad-match campaign. Either pause spray ads entirely, or move the spray into its own dedicated small-budget exact-match campaign on clearly pet-specific spray queries (e.g. `dog snoring spray`, `nasal spray for dogs`) so performance can be monitored in isolation.

**Impact:** $142 of unprofitable spend recovered per 90 days. Reallocated to the tablets broad-match campaign at its 2.18 ROAS, that $142 would generate approximately $310 in sales instead of $103. Net gain: roughly $207 in sales per 90 days (about $70/month).

### Targeting Strategy

**Keyword vs Product Targeting:**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|-------------------|--------|-------|-------|------|-----|-----|-----|
| Keyword Targeting | 738 | $823.12 | $1,647.15 | 2.00 | $15.11 | $1.12 | 14.77% |
| Product Targeting | 29 | $18.98 | $10.83 | 0.57 | $10.83 | $0.65 | 3.45% |

Product targeting is a tiny, unprofitable experiment - 29 clicks and 1 order in 90 days. Not enough volume to draw conclusions, but nothing suggests it should be scaled without restructuring.

**Match Type Breakdown:**

| Match Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|------------|--------|-------|-------|------|-----|-----|-----|
| EXACT | 68 | $71.42 | $250.49 | **3.51** | $19.27 | $1.05 | 19.12% |
| BROAD | 664 | $747.40 | $1,396.66 | 1.87 | $14.55 | $1.13 | 14.46% |
| PHRASE | 0 | $0.00 | $0.00 | n/a | n/a | n/a | n/a |

**Finding: Exact match is 1.9x more profitable than broad, but receives only 9% of spend.**

**Problem:** Exact match has ROAS 3.51 vs broad at 1.87, yet broad eats $747 and exact eats only $71 over 90 days. Phrase match is not being used at all. This is the same harvest-and-scale problem as the campaign structure issue - proven winners are not being isolated and funded.

**Solution:** Move budget from broad to exact. For every proven search term from Q719 with ROAS above 2.5 and 5+ orders, launch a dedicated exact-match campaign. Also introduce phrase match for the same terms as a middle layer to capture natural variations.

**Impact:** Shifting $200 from broad to exact campaigns on the top-ROAS search terms would generate approximately $700 in sales instead of $374 at broad's ROAS. Net gain: $326 in sales per 90 days from the same total ad budget.

## Product-Level Analysis (P0 - SnoreStop for Pets 20 Chewable Tablets)

### P0 Campaign Map

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| M-G: All products - Broad Match | $680.01 | $1,479.75 | 2.18 | 593 | 98 |
| M-G: Pet chewable tablets (Exact) | $9.95 | $74.95 | 7.53 | 11 | 4 |
| A-G: All (Auto) | $9.15 | $0.00 | 0.00 | 14 | 0 |
| **Total P0** | **$699.11** | **$1,554.70** | **2.22** | **618** | **102** |

P0 absorbs 83% of total account ad spend. The P0-level ROAS of 2.22 is healthy. 99% of P0 spend flows through the single broad-match campaign - the dedicated `M-G: Pet chewable tablets` exact campaign (ROAS 7.53) has essentially no budget.

### P0 Blocker Context from Step 3

**There is no traditional PPC blocker to solve for P0.** Step 3 established that on Tier 1 (pet snoring) queries:
- Impression share is 14.5%, already near the ~17% adjusted cap for 2 products
- CTR at 5.63% is 3x industry
- CVR at 8.0% beats industry (5.5%)

Tier 2 (pet nasal/breathing) had 0 purchases in 3 months - it is not convertible for the tablets product and should not be scaled into.

The P0 PPC opportunity is therefore **internal efficiency**, not unlocking new demand. Three concrete levers follow.

### PPC Lever 1: Shift Placement Budget to Top of Search

**Problem:** Placement spend is misallocated.

| Placement | Spend | Sales | ROAS | CTR | CVR |
|-----------|-------|-------|------|-----|-----|
| Top of Search | $550.28 | $1,434.78 | **2.61** | 13.78% | 17.28% |
| Product Pages | $104.58 | $182.39 | 1.74 | 0.04% | 13.68% |
| Rest of Search | $180.95 | $40.81 | **0.23** | 1.03% | 2.65% |
| Off Amazon | $2.48 | $0.00 | 0.00 | 0.59% | 0.00% |

Top of Search delivers $1,435 in sales (82% of total) at ROAS 2.61 and CVR 17.28%. Rest of Search burns $181 at ROAS 0.23 (CVR 2.65%) - essentially wasted spend. 

**Solution:** Increase the Top of Search bid modifier so more impressions route there. Reduce or remove modifiers on Rest of Search so less budget flows to low-converting mid-results placements.

**Impact:** Shifting $150 from Rest of Search to Top of Search would convert at 2.61 ROAS instead of 0.23. That is approximately $392 in sales instead of $35. Net gain of roughly $357 in sales per 90 days on the same ad budget.

### PPC Lever 2: Harvest Proven Search Terms into Exact-Match Campaigns

**Problem:** The highest-converting search terms on P0 are trapped inside the broad-match campaign, sharing budget with a single `+snore` keyword that has 3x weaker ROAS.

Top converting search terms on P0 over 90 days:

| Search Term | Spend | Sales | ROAS | Clicks | Orders |
|-------------|-------|-------|------|--------|--------|
| stop dog snoring | $33.32 | $134.91 | **4.05** | 37 | 9 |
| anti snoring for dogs | $34.02 | $119.92 | **3.52** | 39 | 8 |
| snore stopper for dogs | $54.68 | $125.81 | 2.30 | 65 | 9 |
| snorestop for dogs | $6.21 | $59.96 | **9.66** | 5 | 4 |
| dog snore stop | $9.55 | $55.80 | **5.84** | 11 | 4 |
| dog snoring relief | $45.48 | $85.78 | 1.89 | 30 | 6 |

**Solution:** Launch dedicated exact-match campaigns for `stop dog snoring`, `anti snoring for dogs`, and `dog snore stop` with their own budgets. These already prove themselves in broad - the isolation simply lets them scale without cannibalizing the umbrella campaign.

**Impact:** Together the top 3 terms (`stop dog snoring`, `anti snoring for dogs`, `dog snore stop`) did $311 in sales at a blended ROAS of 4.22 on $77 of spend. Tripling budget on these three terms (to roughly $230) at similar ROAS would yield approximately $970 in sales - a net gain of $660 over 90 days, or ~$220/month.

### PPC Lever 3: Negate Irrelevant Search Terms (Humans and Dog Beds)

**Problem:** The broad-match campaign is leaking spend to search terms where the product cannot convert. These fall into two buckets:

Human-intent queries (P0 is a pet product, cannot convert):

| Search Term | Spend | Clicks | Orders |
|-------------|-------|--------|--------|
| snoring solution | $15.11 | 9 | 0 |
| anti snoring devices | $9.09 | 5 | 0 |
| how to stop snoring while sleeping | $3.70 | 2 | 0 |
| anti snoring | $3.68 | 2 | 0 |
| anti snore device | $3.63 | 2 | 0 |
| z3 pro anti snoring device | $3.60 | 2 | 0 |
| anti snoring mouthpiece | $2.99 | 2 | 0 |
| how to stop snoring | $2.32 | 4 | 0 |

Product-mismatch queries (customer wants a bed/furniture, not a supplement):

| Search Term | Spend | Clicks | Orders |
|-------------|-------|--------|--------|
| anti snoring dog bed | $5.55 | 3 | 0 |
| bed for snoring dog | $3.44 | 2 | 0 |

Plus low-ROAS relevant terms that could also be negated or rebid downward:

| Search Term | Spend | Clicks | Orders | ROAS |
|-------------|-------|--------|--------|------|
| anti snore for dogs | $22.29 | 17 | 1 | 0.67 |
| dog snoring | $17.45 | 13 | 1 | 0.86 |

**Solution:** Add the human-intent and bed-related terms as negative keywords at the campaign or ad group level. Lower bids (do not fully negate) on `anti snore for dogs` and `dog snoring` since they are semantically relevant but underperforming at the current bid.

**Impact:** Roughly $53 of clearly wasted spend recovered per 90 days ($210/year). Plus approximately $40 of underperforming spend reallocated, for a total of ~$93 that can be redirected to the top-3 exact terms at 4.22 ROAS, generating roughly $390 in sales instead of $18. Net gain: ~$370 per 90 days.

## Insights

- **P0 ad ROAS (2.22) beats the full-account ROAS (1.97) because the spray weighs it down.** Separating the spray into its own profitable-only campaign or pausing it would lift headline account ROAS without any new spend.
- **The `snore stop dogs` exact keyword at ROAS 7.68 on just $13 spend is the single clearest unlock in the account.** This is a branded-adjacent keyword where the brand wins without question. It should carry 3-5x more budget.
- **The top-of-search placement is already doing the heavy lifting (65% of spend, 82% of sales).** This confirms the listing converts when it reaches high-intent shoppers. The main thing holding performance back at the placement level is the drag from Rest of Search, not a Top of Search shortfall.
- **About $50-60 per 90 days is leaking to human-snoring queries** (snoring solution, anti snoring devices, etc.). This is a direct result of the broad `+snore` match type and will continue until those terms are negated.

## Things to Investigate Further

- **Historical ad activity before 2026-01-18.** Our data window is limited to the last 90 days. If the seller has been running similar campaigns for a year, the wasted spend figures compound significantly. Worth asking them for a 12-month spend view.
- **Whether the spray product justifies any ad budget at all.** P1 (Spray) has been running at ROAS 0.72 for 90 days. The question is whether this is a structural pricing issue (AOV $13 on a $10.83 product is too low to cover CPC) or whether the spray needs its own listing improvements before ad spend can make sense.

## Questions for the Seller

- **How long have these campaigns been running?** Our ad data starts 2026-01-18. If these campaigns are 6-12 months old, the overstuffed broad-match structure has likely been leaking ~$40-60/month in wasted human-query spend since day one, and the `Pet chewable tablets` exact campaign has been sitting underfunded that entire time.
- **Is there a reason the spray is being advertised?** At ROAS 0.72 it loses money on every order. We would recommend pausing spray ads and testing a dedicated small-budget exact-match campaign only if there is a strategic reason to keep it visible.
