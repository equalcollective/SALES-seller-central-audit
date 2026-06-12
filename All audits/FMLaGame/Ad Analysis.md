# Step 4: Ad Analysis - FMLaGame (P0: B0CTXKBB6X)

## Window and Constraints

- **Date range:** 2026-01-26 to 2026-04-24 (89 days, full ads-data window)
- **Constraint: Sponsored Display NOT allowed** per seller. SD-based recommendations (defensive SD on own listing, etc.) are excluded from this analysis.
- **Constraint: Profit-first.** Recommendations are evaluated against unit economics, not topline.

**Break-even unit economics (per Brian's intake notes):**

| Item | Amount |
|------|--------|
| Retail price | $19.95 |
| Referral fee (~15%, Toys & Games) | -$2.99 |
| FBA fees (small standard est.) | -$3.50 |
| Landed COGS (mid of $4-5) | -$4.50 |
| **Contribution before ads** | **$8.96 (45%)** |
| **Break-even ROAS** | **2.23** |

Current account ROAS is 0.66. **Every dollar of ad spend is currently destroying margin.** Over the 89-day window: $856 spent, $568 in ad sales, contribution from those sales = $255, net ad cash burn = -$601 (~ -$2,463/year run rate).

This frames every recommendation below: with the listing converting at 1% (vs ~8% industry per Step 3), no amount of PPC optimization can reach 2.23 ROAS. **The listing fix from Step 2 has to come first.** The PPC actions in this section are about stopping the bleed, not scaling.

## Account Level

### Campaign Structure

The account has 5 active campaigns, all targeting the single ASIN B0CTXKBB6X. Campaign naming convention ("SO | FML | B0CTXKBB6X | SPM | ...") indicates Sophie Society set up the manual campaigns. The auto campaign is named "FML Auto - Sellozo" suggesting Sellozo (a PPC management platform) is the executor.

| Campaign | Type | Spend | Sales | ROAS | Clicks | Orders | CTR | CVR |
|----------|------|-------|-------|------|--------|--------|-----|-----|
| FML Auto - Sellozo | Auto | $267.26 | $209.44 | 0.78 | 1,762 | 14 | 0.90% | 0.79% |
| SO Adult Card Games SKW (Exact, TOS 60%) | Manual Exact | $472.52 | $309.18 | 0.65 | 1,578 | 20 | 1.20% | 1.27% |
| SO All Suggested Low Bid (Exact, ROS 50% / PP 80% / AU 70%) | Manual Exact | $73.90 | $49.87 | 0.67 | 294 | 3 | 1.29% | 1.02% |
| SO Funny Card Games SKW (Exact, ROS 400%) | Manual Exact | $37.13 | $0.00 | 0.00 | 55 | 0 | 2.39% | 0.00% |
| SO PT Would you rather (Exact, AU 100 / TOS 80% / ROS 30%) | Product Targeting | $5.17 | $0.00 | 0.00 | 19 | 0 | 3.01% | 0.00% |

Campaigns are not overstuffed (3-5 keywords each, mostly 1-2 active targets). Structure is clean. The issue is not structure - it's bid placement modifiers and the unit economics underneath.

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|--------|-------|-------|------|-----|-----|-----|
| Automatic | 1,762 | $267.26 | $209.44 | 0.78 | $14.96 | $0.15 | 0.79% |
| Manual | 1,946 | $588.72 | $359.05 | 0.61 | $15.61 | $0.30 | 1.18% |

> **Finding: Auto is outperforming Manual on ROAS, despite being meant only for discovery.**
>
> **Problem:**
> - Auto ROAS 0.78 vs Manual ROAS 0.61 (auto is 27% more efficient)
> - Manual CPC is 2x auto CPC ($0.30 vs $0.15) - you are paying twice as much per click for worse efficiency.
> - Manual CVR is higher (1.18% vs 0.79%) but the bid premium more than wipes it out.
>
> **What this tells us:** Sellozo's auto bidding is finding clicks at a much lower cost than the manually-targeted exact keywords. This typically happens when manual bid prices are set too high (Sophie Society's TOS 60% / PP 80% modifiers may be over-bidding) and when winning auto search terms haven't been harvested into manual.
>
> **Solution:**
> - Reduce manual exact bids to bring CPC closer to the $0.15 auto level. Even a small drop ($0.30 -> $0.20) on the "Adult Card Games SKW" campaign saves ~$160 over a 90-day window at the same click volume.
> - Mine the auto search term report for terms not yet in manual exact campaigns and harvest them.
>
> **Impact:** Bringing manual CPC from $0.30 to $0.20 on the same click volume (~1,946 clicks/quarter) saves ~$195/quarter in spend at unchanged sales. That alone moves blended ROAS from 0.66 to ~0.86. Still below break-even, but stops $195/quarter of the bleed.

### Targeting Strategy

**Keyword vs Product Targeting:**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|-------------------|--------|-------|-------|------|-----|-----|-----|
| Keyword Targeting | 3,552 | $839.63 | $558.52 | 0.67 | $15.51 | $0.24 | 1.01% |
| Product Targeting | 156 | $16.35 | $9.97 | 0.61 | $9.97 | $0.10 | 0.64% |

98% of spend is keyword targeting. Product targeting is barely active ($16 in 89 days, 1 order). The "PT Would you rather" campaign was an attempt to target competitor ASINs but has zero conversions on 19 clicks. Not a meaningful play right now.

**Match Type Breakdown:**

| Match Type | Clicks | Spend | Sales | ROAS | CVR |
|------------|--------|-------|-------|------|-----|
| EXACT | 1,927 | $583.55 | $359.05 | 0.62 | 1.19% |

> **Finding: 100% exact match. No Broad or Phrase campaigns running.**
>
> Broad and phrase match aren't strictly required, but they're how you discover converting search terms outside the auto campaign. With only auto + exact, the harvest pipeline is half-built: auto finds something, but a broad/phrase variant of an exact target would catch the same patterns under tighter bid control.
>
> Not a top-priority fix given the larger CVR issue, but worth noting for the longer-term ad strategy.

### Campaign Profitability

Every active campaign is below 1.5x ROAS. The break-even threshold is 2.23. **Zero of 5 campaigns are profitable.**

| Campaign | Spend | Sales | ROAS | Status |
|----------|-------|-------|------|--------|
| FML Auto - Sellozo | $267.26 | $209.44 | 0.78 | Best of the bunch, still unprofitable |
| Adult Card Games SKW | $472.52 | $309.18 | 0.65 | Largest spender, unprofitable |
| All Suggested Low Bid | $73.90 | $49.87 | 0.67 | Unprofitable |
| Funny Card Games SKW | $37.13 | $0.00 | 0.00 | Pure waste, 55 clicks 0 orders |
| PT Would you rather | $5.17 | $0.00 | 0.00 | Pure waste, 19 clicks 0 orders |

> **Finding: Two campaigns are pure waste, the rest are unprofitable but converting.**
>
> **Problem:** Combined, "Funny Card Games SKW" and "PT Would you rather" have spent $42.30 over 89 days with 74 clicks and 0 orders. They are statistically meaningful (>20 clicks each) and clearly not converting.
>
> **Solution:** Pause both immediately.
>
> **Impact:** Saves ~$170/year in unambiguously wasted spend. Small in absolute terms but trivially actionable - this is a same-day fix.

## Product Level (P0)

### P0 Campaign Map

Single ASIN account: 100% of ad spend goes to P0. Mapping is identical to the campaign list above. Total P0 ad spend over 89 days: $855.98. Total P0 ad sales: $568.49.

### Blocker-Specific Findings

Step 3 (SQP) identified **CVR (post-click conversion)** as the primary blocker on Tier 1, with the funnel breaking specifically between click and add-to-cart (Brand ATC rate 9.7% vs industry 32.8%). Per CLAUDE.md, the PPC levers for CVR blockers are: (1) better placements (especially Top of Search), (2) Sponsored Display defensive ads - **blocked: SD not allowed**, (3) removing wasted spend on irrelevant targets/search terms.

#### CVR Blocker: Placement Distribution

> **Connecting to Step 3:** SQP showed Tier 1 brand CTR at 1.84x industry, then a collapse at ATC rate (30% of industry). The brand wins clicks; the PDP loses them. One of the few PPC levers that can change which clicks the brand pays for is shifting placement bids toward Top of Search, where presentation is most prominent and shoppers convert at a higher rate.

| Placement | Spend | Sales | ROAS | CTR | CVR | Spend Share |
|-----------|-------|-------|------|-----|-----|-------------|
| **Top of Search** | $20.08 | $9.97 | 0.50 | **12.59%** | **1.89%** | 2.3% |
| Rest of Search | $225.73 | $69.82 | 0.31 | 2.11% | 0.36% | 26.4% |
| Product Pages | $608.03 | $249.35 | 0.41 | 0.86% | 0.59% | 71.0% |
| Off Amazon | $0.05 | $0.00 | 0.00 | 0.12% | 0.00% | 0.0% |

> **Finding: The placement with the best CTR and CVR is getting 2.3% of spend.**
>
> **Problem:**
> - Top of Search has 12.59% CTR (vs 2.11% Rest of Search, 0.86% Product Pages) and 1.89% CVR (vs 0.36% Rest of Search, 0.59% Product Pages). It is by far the highest-converting placement.
> - Despite that, only $20 of $856 (2.3%) of spend reaches Top of Search.
> - Sophie Society's bid modifiers explain it: the largest campaign uses TOS 60% but the "All Suggested Low Bid" campaign uses ROS 50% / PP 80% (under-modifies TOS, over-modifies Product Pages), and "Funny Card Games SKW" uses ROS 400% (heavily biased to Rest of Search). The bidding logic is intentionally pushing spend AWAY from the best-converting placement.
> - **Caveat:** TOS only has 53 clicks and 1 order in this window, so the CVR estimate is uncertain. The CTR signal (12.59% on 421 impressions) is more reliable - the bigger problem is the brand barely shows up at TOS at all.
>
> **Solution:**
> - Increase the TOS bid modifier on "Adult Card Games SKW" from 60% to ~150-200%, while reducing the PP modifier on "All Suggested Low Bid" from 80% to ~30-40%. This redirects spend toward the placement that converts.
> - Pair this with bid floor reductions on Rest of Search (which has 26% of spend at 0.31 ROAS - it is wasting budget) and Product Pages (71% of spend at 0.41 ROAS).
>
> **Impact:** Even shifting only $200 of the $608 Product Pages budget to TOS at TOS's converted-out economics (1.89% CVR, $0.38 CPC) generates roughly the same number of orders (~10) at higher AOV and better placement quality, but is unlikely to flip the campaign profitable until listing CVR improves. The honest framing for the call: this is a hygiene fix that arrests bleed, not a profitability fix.

#### CVR Blocker: Wasted Targeting

Targets with meaningful spend (>$3) and zero conversions over 89 days, sorted by spend:

| Campaign | Targeting | Match Type | Spend | Clicks | Orders | CVR |
|----------|-----------|------------|-------|--------|--------|-----|
| Funny Card Games SKW | funny card games | EXACT | $37.13 | 55 | 0 | 0% |
| Auto - Sellozo | substitutes | (Auto) | $11.18 | 137 | 1 | 0.73% |
| All Suggested Low Bid | party card game | EXACT | $10.16 | 23 | 0 | 0% |
| All Suggested Low Bid | go fucl yourself card game | EXACT | $7.70 | 29 | 0 | 0% |
| PT Would you rather | asin "B0BRT58L5W" | (PT) | $5.15 | 18 | 0 | 0% |
| All Suggested Low Bid | adult games dirty | EXACT | $4.93 | 20 | 0 | 0% |
| All Suggested Low Bid | drinking card games | EXACT | $4.67 | 21 | 0 | 0% |
| All Suggested Low Bid | bachelorette party games | EXACT | $3.90 | 21 | 0 | 0% |
| Auto - Sellozo | close-match | (Auto) | $3.53 | 33 | 0 | 0% |
| **Total wasted** | | | **$88.35** | **357** | **1** | |

> **Finding: $88 of clear-zero-conversion spend over 89 days, plus $5 in tiny PT and other waste.**
>
> **Problem:** Nine targets with meaningful click volume (>15 clicks each, 357 clicks total) and 0 or near-0 conversions. These are signaling intent the listing isn't fulfilling.
>
> **Solution:**
> 1. Pause "Funny Card Games SKW" and "PT Would you rather" entire campaigns (already covered above).
> 2. Negate "party card game", "go fucl yourself card game", "adult games dirty", "drinking card games", "bachelorette party games" from "All Suggested Low Bid" campaign.
> 3. Add negative match for "close-match" and "substitutes" auto-targeting types if Sellozo allows it - they're spending $14 with 1 order across 170 clicks.
>
> **Impact:** Saves ~$360/year in wasted spend. Combined with the campaign-level pauses above, total annual savings is ~$530. Modest but immediate.

#### CVR Blocker: Irrelevant Search Terms (from Auto)

The auto campaign is pulling traffic from search terms that suggest the wrong intent. Over 89 days, the most expensive zero-conversion search terms with >5 clicks each:

| Search Term | Clicks | Spend | CTR | Why it's misaligned |
|-------------|--------|-------|-----|---------------------|
| funny card games | 27 | $18.43 | 4.82% | Generic - too broad, low purchase intent |
| party card games | 17 | $6.95 | 4.26% | Generic - low intent |
| cards against humanity | 33 | $5.29 | 2.42% | CAH searchers want CAH; FMLaGame can't out-trust the incumbent |
| go fucl yourself card game | 17 | $4.20 | 2.43% | Searching for a different specific game |
| adult games dirty | 16 | $3.88 | 3.43% | "Dirty" = sexual; FMLaGame is irreverent but not sexual |
| drinking card games | 12 | $2.54 | 3.03% | Different sub-category (drinking games) |
| adult card game (singular) | 9 | $2.48 | 4.48% | Mostly redundant with plural exact, low yield |
| party games | 14 | $2.30 | 1.80% | Too broad |
| bachelorette party games | 14 | $2.24 | 1.88% | Specific occasion mismatch |
| do or drink | 12 | $2.01 | 8.05% | Different specific game (drinking) |
| sex games | 8 | $1.31 | 11.43% | NSFW intent mismatch |
| family games | 5 | $0.77 | 33.33% | Family-friendly intent; this is 18+ |
| jenga game for adults | 6 | $1.00 | 30.00% | Different category entirely |
| truth or dare card game for adults | 9 | $1.43 | 6.62% | Different mechanic |
| adult monopoly game naughty | 10 | $1.78 | 5.15% | Different game |
| **Total** | **209** | **$56.61** | | |

> **Finding: ~$57 in misaligned search-term traffic over 89 days. Negate list is straightforward.**
>
> **Problem:** Auto campaign is appearing on searches for unrelated games (jenga, monopoly, drinking games, "do or drink", "truth or dare") and irrelevant categories (sex games, family games, bachelorette games). These shoppers don't want this product, and the listing fails to convert them.
>
> **Solution:** Add the 15 search terms above as exact-match negatives in the auto campaign.
>
> **Impact:** Saves ~$230/year. Cumulative with the prior recommendations: ~$760/year in eliminated waste, blended ROAS lifts from 0.66 to ~0.78. Still below break-even, but represents 12% of current spend reclaimed.

#### Hidden Win: One Target Is Already Profitable

The single profitable target across the entire account, hidden inside "All Suggested Low Bid":

| Target | Spend | Sales | ROAS | Clicks | Orders | CVR |
|--------|-------|-------|------|--------|--------|-----|
| adult games for game night (Exact) | $6.69 | $19.95 | **2.98** | 49 | 1 | 2.04% |

The matching search term shows ROAS 3.92 ($5.09 spend, $19.95 sales). Both are above the 2.23 break-even.

> **Finding: "adult games for game night" is the only profitable target in the account, and it has $6.69 in lifetime spend.**
>
> **Problem:** This target is buried in the "All Suggested Low Bid" campaign with 14 other keywords and a low bid floor (50% ROS / 80% PP modifier). It's not getting room to scale. With only 1 order on 49 clicks the data is thin, but the CTR (1.72%) and ROAS (2.98) are both well above account average and above break-even.
>
> **Solution:** Carve out "adult games for game night" into its own dedicated SP exact campaign with a higher daily budget and TOS-biased bidding. Test scaling to 10x current spend ($60-80/quarter) to see whether the ROAS holds at higher click volumes.
>
> **Impact:** If ROAS holds at 2.5+ as spend scales, a $300/quarter dedicated campaign on this term would generate ~$750/quarter in sales at break-even or better economics. This is the single most actionable PPC opportunity in the account.

## Insights

- **The PPC architecture isn't broken; the unit economics are.** Sophie Society set up a clean structure (named campaigns, exact match, auto for discovery, TOS modifiers). The structure works. What's broken is that the listing converts at 1% when industry is 8%, so even good keyword bids lose money. The PPC actions in this audit save ~$760/year in waste, but reaching profitability requires the listing fix from Step 2 to land first.
- **The TOS placement signal is genuinely strong (12.6% CTR vs 0.86% Product Pages).** Even with thin volume, this confirms what Step 3 SQP showed: the listing wins the click battle when it shows up prominently. The leverage is real but capped by the broken PDP downstream. After listing fixes, TOS bid scaling becomes the next major lever.
- **One target is already profitable ("adult games for game night" at ROAS 2.98).** It's buried in a 14-keyword campaign at a low bid floor. Carving it out is the single highest-leverage PPC action available right now.
- **Sponsored Display being off-limits is a real constraint.** SD defensive (own-listing retargeting) is the textbook answer for cart-to-purchase rate fixes when CVR is the blocker. With SD ruled out, the listing-side fixes carry more of the load. The action plan in the final audit should reflect that.

## Things to Investigate Further

- The 89-day ad window means we cannot see what Sophie Society was doing during the Dec 2024 viral peak or the Dec 2025 holiday window. If the strategy then was different from now (different placements, broader/phrase match, off-Amazon-driven traffic absorbing into branded campaigns), there's no way to reconstruct it from data. Worth asking the seller directly.
- TOS click data is thin (53 clicks in 89 days). The 12.6% CTR signal is reliable but the CVR estimate (1.89%) is not. After increasing TOS bid modifiers, monitor weekly to confirm the CVR holds at scale.

## Questions for the Seller

- Sophie Society named the manual campaigns and Sellozo runs the auto. Is the current ad setup something you've actively reviewed in the last 90 days, or is it on autopilot? (Hypothesis: the campaigns were set up by Sophie Society, then handed off to Sellozo, with no one currently owning the bid modifier logic - this would explain why TOS is starved despite being the best-converting placement.)
- Are you open to materially reducing ad spend in the off-season (May-Sep) while listing fixes are implemented, then re-scaling for Q4 2026? (Hypothesis: the cleanest path to profit-first execution is to stop bleeding ~$2.5K/year on ads that lose money on every sale, fix the PDP, and re-engage with proper unit economics for the holiday push.)
