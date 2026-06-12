# Ad Analysis - Abokichi Inc.

## Context: Near-Zero Active Advertising

Abokichi has done minimal Amazon PPC. Across Jan 1 - May 15, 2026, total ad spend is approximately **$147.56** with **5 ad-attributed orders** and $97.45 in ad sales. There are **no currently-active campaigns** with meaningful spend. Historical (now-paused) campaigns from 2023 do exist and provide a useful baseline.

Per CLAUDE.md, when the seller has effectively not advertised, Step 4 pivots from "optimize what's running" to "what does the data reveal, and what's the ad-launch strategy." The seller's CVR and CTR signals are still informative on the small budget that has been spent.

## Historical Campaign Performance (Paused)

| Campaign | Status | Impressions | Clicks | Spend | Sales | Orders | ROAS | ACOS |
|----------|--------|-------------|--------|-------|-------|--------|------|------|
| 20230424- AUTO | PAUSED | 82,968 | 366 | $273.67 | $802.58 | 40 | **2.93** | 34% |
| 20230901 - Manual - Keyword | PAUSED | 55,230 | 187 | $371.88 | $228.88 | 12 | 0.62 | 162% |

**Reading these:**
- The 2023 **Auto campaign was profitable** (2.93 ROAS, 34% ACoS, 40 orders) and provided a clean source of impression growth. Pausing it removed a working channel.
- The 2023 **Manual Keyword campaign was not profitable** (0.62 ROAS, 162% ACoS) and lost ~$143 net.
- Net of both: the seller spent $645 to make $1,031, a blended 1.60 ROAS. Not great, not terrible. The Auto was carrying the Manual.

Note: spend totals shown for the Jan-May 2026 window only capture spend that fell in that window; the 2023 campaigns ran earlier.

## Account-Level Analysis (Jan 1 - May 15, 2026)

### Campaign Structure

Only paused 2023 campaigns and a small set of current micro-test campaigns. No restructuring needed because there is essentially nothing live to restructure. The 2023 Auto campaign is the model to copy when relaunching.

### Auto vs Manual Split

The Auto vs Manual split tool returned no data for the recent window (campaigns are largely off). The relevant comparison is the historical paused-campaign data above. Auto outperformed Manual by ~5x ROAS in the seller's own history. **This is consistent with the SQP finding that the brand wins on long-tail Japanese-specific queries that auto campaigns naturally surface.**

### Campaign Profitability

There are no currently-profitable enabled campaigns at meaningful spend. The historical Manual Keyword campaign (0.62 ROAS) was unprofitable. The historical Auto campaign (2.93 ROAS) was profitable.

> **Finding: The proven-profitable Auto campaign has been paused for over 2 years.**
>
> **Problem:**
> - In 2023, the 20230424-AUTO campaign generated 40 orders at 2.93 ROAS on $274 spend.
> - It has been paused since then.
> - Total 2026 YTD ad spend across all efforts is $147.56 (5 ad orders).
>
> **Solution:**
> - Restart the Auto campaign at a small daily budget ($10-15/day) with a 30-day learning window.
> - Use it as the discovery layer for long-tail queries.
>
> **Impact:**
> - If the campaign returns to its historical 2.93 ROAS at $10/day budget, that's $300/mo spend producing ~$880/mo ad sales (45+ orders).
> - This alone would 2x the brand's current monthly revenue.

### Targeting Strategy

**Keyword vs Product Targeting (Jan 1 - May 15, 2026):**

| Targeting Strategy | Impressions | Clicks | CTR | Spend | Sales | Orders | ROAS | CVR |
|--------------------|-------------|--------|-----|-------|-------|--------|------|-----|
| Keyword Targeting | 29,296 | 111 | 0.38% | $141.63 | $155.92 | 8 | 1.10 | 7.2% |
| Product Targeting | 3,821 | 10 | 0.26% | $5.93 | $77.96 | 3 | **13.15** | **30%** |

Caveat: Product Targeting has a tiny sample (10 clicks, 3 orders). The 13x ROAS is not yet stable. But the directional signal (defensive/competitor-ASIN targeting converts well for this product) is consistent with SQP findings: when shoppers are already looking at a relevant Asian condiment, the Japanese-miso differentiator works.

**Match Type Breakdown:**

| Match Type | Impressions | Clicks | CTR | Spend | Sales | Orders | ROAS | ACOS |
|------------|-------------|--------|-----|-------|-------|--------|------|------|
| BROAD | 4,735 | 20 | 0.42% | $40.80 | $38.98 | 2 | 0.96 | 105% |
| PHRASE | 4,329 | 16 | 0.37% | $37.03 | $0 | 0 | 0 | — |
| EXACT | 42 | 0 | 0% | $0 | $0 | 0 | — | — |

> **Finding: Phrase Match is burning budget on zero conversions; Exact Match is unused.**
>
> **Problem:**
> - PHRASE: $37 spent, 16 clicks, 0 orders. ROAS 0.
> - EXACT: 42 impressions, 0 clicks. Essentially untested.
>
> **Solution:**
> - Pause all Phrase Match keywords.
> - Build Exact Match keyword targeting on the Tier 1 winners (japanese chili oil, miso chili oil, miso chili crisp, chili miso, garlic miso, rayu japanese chili oil, gluten free miso, tekka miso condiment).
> - Move converting search terms from auto/broad into Exact Match for tight bid control.
>
> **Impact:**
> - Recovers ~$37/mo of wasted Phrase spend.
> - Exact Match on Tier 1 high-CTR queries should convert at brand's documented 5-7% CTR (above industry) and 9-12% CVR (near industry).

### Placement Performance

| Placement | Impressions | Clicks | CTR | Spend | Sales | Orders | ROAS | CVR |
|-----------|-------------|--------|-----|-------|-------|--------|------|-----|
| **Top of Search** | 1,735 | 31 | **1.79%** | $53.70 | $58.47 | 3 | **1.09** | **9.7%** |
| Rest of Search | 17,189 | 57 | 0.33% | $54.85 | $19.49 | 1 | 0.36 | 1.8% |
| Product Pages | 11,781 | 28 | 0.24% | $38.30 | $19.49 | 1 | 0.51 | 3.6% |
| Off Amazon | 2,223 | 5 | 0.22% | $0.71 | $0 | 0 | 0 | 0% |

> **Finding: Top of Search is the only profitable placement; everything else is sub-1.0 ROAS.**
>
> **Problem:**
> - Top of Search ROAS: 1.09. CVR 9.7%. CTR 1.79% (5-8x other placements).
> - Rest of Search ROAS: 0.36. CVR 1.75%. 64% of all spend went to non-Top-of-Search placements.
> - Product Pages ROAS: 0.51. CVR 3.57%.
>
> **Solution:**
> - In Campaign Manager, set Top of Search bid modifier to +200-300% (vs. current default).
> - Reduce Product Pages and Rest of Search bid modifiers toward 0% (let the auction floor decide).
> - Reallocate the saved budget into Top of Search bid ceilings.
>
> **Impact:**
> - Roughly 64% of current spend ($147) is producing 33% of orders. Shifting toward Top of Search at current ratios moves the blended ROAS from 0.66 to ~1.0+.
> - On a relaunch budget of $300/mo, ~$200 redirected to Top of Search at 1.09 ROAS = ~$218/mo sales vs ~$66/mo from other placements at 0.4-0.5 ROAS.

## Product-Level Analysis (P0)

### P0 Campaign Map

There are no currently-enabled campaigns specifically targeting P0 (OKAZU Mild Chili Miso Oil) with meaningful spend. The micro-test spending of the last 5 months mostly fell on broad chili oil queries via legacy auto/broad campaigns.

### Blocker-Specific Findings

#### Impression Share Blocker: Tier 1 Bidding (Japanese Chili Miso Oil queries)

Section 3 identified **impression share as the primary blocker on Tier 1**, where the brand has 2.5x above-industry CTR but only 1-5% impression share against a 16-18% cap. The PPC lever is bidding directly on these 14 Tier 1 keywords.

Looking at search-term-level data for the queries that DID get spend (Jan-May 2026):

| Search Term | Impressions | Clicks | CTR | Spend | Sales | ROAS |
|-------------|-------------|--------|-----|-------|-------|------|
| japanese chili oil | 21 | 2 | 9.52% | $4.20 | $0 | 0 |
| crispy chili oil | 16 | 1 | 6.25% | $2.15 | $19.49 | **9.07** |
| ramen chili | 5 | 1 | 20% | $1.12 | $19.49 | **17.40** |
| garlic miso | 7 | 1 | 14.29% | $1.66 | $0 | 0 |
| spicy miso paste | 1 | 1 | 100% | $0.60 | $0 | 0 |
| chilli miso | 2 | 1 | 50% | $0.55 | $0 | 0 |
| ozaku chili miso | 2 | 1 | 50% | $0.55 | $0 | 0 |

> **Finding: Tier 1 keywords are barely funded but the two that did convert generated 9-17x ROAS.**
>
> **Problem:**
> - "crispy chili oil" returned 9.07 ROAS on $2.15 spend (1 order).
> - "ramen chili" returned 17.40 ROAS on $1.12 spend (1 order).
> - "japanese chili oil" got 2 clicks, no orders - but only 21 impressions total. The sample is too small to evaluate.
> - Tier 1 spending across all 14 keywords totals well under $20 across 5 months.
>
> **Solution:**
> - Build a dedicated **Manual Exact Match campaign** for the Tier 1 keyword list (japanese chili oil, miso chili oil, miso chili crisp, chili miso, garlic miso, rayu japanese chili oil, miso oil, japanese chili crisp, chilli oil japanese, gluten free miso, spicy miso, spicy miso paste, garlic miso, tekka miso condiment).
> - Start at suggested bid + 20% to win impression share.
> - Top of Search bid modifier +200%.
> - Daily budget $15/day across the campaign (~$450/mo).
>
> **Impact:**
> - Combined Tier 1 query volume is ~1,500/mo. At a 16-18% impression share cap with 2 ranking products, max ~250/mo brand impressions.
> - At brand's documented 5.8% CTR and 9.7% CVR (Top of Search), 250 impressions → 14 clicks → 1-2 conversions/mo from this campaign at $19/AOV = $19-38/mo at the cap (small but high-quality).
> - More importantly: this is the highest-intent traffic that builds review velocity and BSR momentum. Indirect benefit is larger than direct sales.

#### CTR Blocker: Tier 2 Mismatch (Don't fight this)

Section 3 identified **CTR as the primary blocker on Tier 2** (broad chili crisp / chili oil / miso paste queries) because the Japanese-miso product doesn't match Sichuan-style chili crisp search intent. The current ad data confirms this:

| Search Term | Impressions | Clicks | CTR | Spend | Sales | ROAS |
|-------------|-------------|--------|-----|-------|-------|------|
| chili oil | 352 | 4 | 1.14% | $6.47 | $0 | 0 |
| chili crisp oil | 109 | 3 | 2.75% | $5.01 | $0 | 0 |
| chilli oil | 121 | 2 | 1.65% | $4.50 | $0 | 0 |
| chili crisp | 107 | 1 | 0.93% | $1.12 | $0 | 0 |
| miso paste | 15 | 1 | 6.67% | $0.60 | $0 | 0 |

Combined Tier 2 spend: ~$18. Combined Tier 2 orders: 0.

> **Finding: Broad chili oil/crisp keywords have eaten 100%+ of their spend with zero conversions.**
>
> **Problem:**
> - $18 spent across the 5 main Tier 2 keywords. 0 orders.
> - Confirms SQP finding: the product visually doesn't match what these searchers want.
>
> **Solution:**
> - Pause "chili oil", "chili crisp", "chilli oil", "chili crisp oil" as standalone keyword targets.
> - Move them to negative keywords on Auto campaigns to prevent the auto from re-discovering them.
> - Allow Auto to keep harvesting other long-tail Japanese-specific variants.
>
> **Impact:**
> - Recovers ~$18-30/mo at relaunch budget that would otherwise be wasted on these broad terms.

#### CVR Blocker: Irrelevant Auto Spillover (Product Targeting as lever)

The Auto campaign in 2023 was profitable BUT current data shows the auto/broad targeting is also catching irrelevant queries:

| Wasted Search Term | Impressions | Clicks | Spend | Note |
|--------------------|-------------|--------|-------|------|
| ramen | 159 | 2 | $2.18 | Too broad |
| prik nam mun chili oil | 20 | 1 | $3.63 | Thai chili oil, wrong intent |
| sesame oil | 4 | 1 | $1.12 | Cooking oil, wrong intent |
| soy sauce | 2 | 1 | $0.89 | Wrong product |
| japanese mayo | 6 | 1 | $0.60 | Wrong product |
| japanese couple | 3 | 1 | $0.23 | Random (auto bug) |
| food recipies | 6 | 1 | $0.16 | Random (auto bug) |
| homemade spices | 3 | 1 | $0.16 | Wrong product |
| hotpot soup bases | 1 | 1 | $1.97 | Wrong product |

> **Finding: Auto targeting catches a long tail of irrelevant queries. These need to be negated as the auto restarts.**
>
> **Problem:**
> - Even at micro-budget, the auto has picked up "soy sauce", "japanese mayo", "japanese couple", "food recipies", "hotpot soup bases" as search terms.
> - Total wasted: ~$15 in this small window.
>
> **Solution:**
> - At auto restart, add a negative keyword list including: ramen, soy sauce, mayo, japanese mayo, hotpot, recipies, sesame oil (alone), japanese curry cube, prik nam mun, layu, lao gan ma.
> - Negative-ASIN-target competitor brand pages where Abokichi's CVR is unproven.
>
> **Impact:**
> - Saves estimated 10-15% of auto spend that goes to irrelevant search terms.
> - Tightens the discovery loop so the auto surfaces additional Japanese-specific long tail.

#### Product Targeting (Defensive + Competitor)

Product Targeting in the current window has tiny sample but exceptional ROAS: 13.15 ROAS, 30% CVR, 3 orders on $5.93 spend.

> **Finding: Product Targeting (likely competitor/category-ASIN targeting) converts at 13x but is underfunded.**
>
> **Problem:**
> - 3,821 impressions, 10 clicks, 3 orders in the 5-month window.
> - Spend was only $5.93 - barely tested.
>
> **Solution:**
> - Build a Sponsored Products **Product Targeting campaign** that targets:
>   1. Own ASINs (defensive against competitors poaching browsers on Abokichi product pages).
>   2. Competitor chili oil / chili crisp ASINs where Abokichi's "Japanese miso" angle is a clear differentiator (S&B Layu, premium chili crisps, Momofuku).
>   3. Adjacent Japanese pantry ASINs (ramen kits, premium miso, Japanese cooking guides).
> - Cap daily at $5-10 to start.
>
> **Impact:**
> - At brand's small-sample 30% CVR on PAT: $10/day → ~$15-25/day sales (1.5-2.5 ROAS conservatively).
> - Even if ROAS settles at 2-3x once volume scales, this is high-margin growth.

## Insights and Open Questions (Step 4)

**Insights:**
- The brand is functionally not advertising. The previous Auto campaign (2.93 ROAS, 40 orders) was paused and never replaced. There is a clear, proven playbook to restart from.
- Top of Search is the only profitable placement (1.09 ROAS, 9.7% CVR). The 64% of current spend going to Rest of Search and Product Pages is producing 33% of orders.
- Product Targeting converts at 30% CVR / 13x ROAS in a small sample - this is the strongest untapped lever after Tier 1 keyword targeting.
- Phrase Match has burned $37 on 0 conversions; Exact Match has been essentially untested.

**Questions for the Seller:**
- "The 2023 Auto campaign was profitable at 2.93 ROAS and was paused. Do you remember why it was paused? Was there a margin/COGS reason, an inventory constraint, or something else? We'd want to know before we restart it."
- "What's the unit cost / contribution margin per OKAZU jar at $19.49 retail? We want to set ROAS targets that protect margin, not just produce top-line sales."
- "Are you open to a small Product Targeting / defensive campaign on your own ASINs and on adjacent Japanese-pantry competitors? It's the highest-converting tactic in your current data but the volume has been minimal."
