# Ad Analysis - Terminal Velocity Sport

**Data source:** Metabase Campaign Analysis V1 dashboard
**Time window:** Feb 7 to May 6, 2026 (89 days = available ad data window)
**Status filter:** ENABLED only (active campaigns)

**Account-level snapshot:**
- Total ad spend: **$3,564**
- Total ad sales: **$3,553**
- **Account ROAS: 1.00 (break-even at the gross-revenue level, below break-even after COGS and fees)**
- Active campaigns: ~37
- Avg daily spend: ~$40/day

## Account Level

### Campaign Structure

| Metric | Value |
|--------|------:|
| Total active campaigns | ~37 |
| Product families with their own campaign suites | 7 (P0 mount, Skull mount, Flame mount, FAFO mount, Wing LED, USB 12V, Snoodle dog toy) |
| Campaigns with <$25 spend in 89 days | ~20 |
| Campaigns with $0 spend | ~10 |

> **Finding: Campaign structure is over-fragmented, not over-stuffed**
>
> **Problem:**
> - 37 campaigns active, but only ~10 spending more than $25 over 89 days. The rest are zombie campaigns generating impressions but no spend or activity.
> - Most product families have a full set of 5-6 campaigns (Auto/Close, Auto/Compliments, Auto/Product, Manual Broad, Manual Phrase, Manual Exact) regardless of whether the product is the hero. Even the SNOODLE dog toy (a $0-revenue SKU per Step 1) has 5 campaigns running.
> - Daily budgets are spread so thin that successful campaigns (e.g., Diamond Mount with USB/Manual Keyword/Phrase at 2.65 ROAS) only get $28 of spend over 89 days while broad-match campaigns with worse ROAS soak up most of the budget.
>
> **Solution:**
> - Consolidate to a single Auto campaign per active product (instead of three Auto sub-types per product).
> - Pause Snoodle, Bike Stem Mount, and other dead-product campaigns entirely.
> - Reallocate freed daily budget to the campaigns with proven ROAS > 1.5 that are currently starved (Diamond Mount Phrase 2.65, FAFO Manual Broad 1.67, FAFO Manual Phrase 1.80, Branded 3.60).
>
> **Impact:**
> - Snoodle campaigns: $2.38 wasted over 89 days (small in $ but indicates lack of campaign hygiene). Pausing reclaims attention bandwidth more than budget.
> - Phrase-match P0 campaign currently $28 over 89 days at 2.65 ROAS = $74 sales. At 10x budget ($280), assuming ROAS halves to a still-healthy ~1.5 due to bidding into broader queries, that's $420 in sales (vs $74 today). **Net incremental: ~$340 over 89 days from a single starved campaign.**

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|-------:|------:|------:|-----:|----:|----:|----:|
| Automatic | 2,190 | $1,224 | $1,512 | 1.24 | $20.72 | $0.56 | 3.33% |
| Manual | 3,427 | $2,299 | $1,973 | 0.86 | $17.62 | $0.67 | 3.27% |

> **Finding: Auto is outperforming Manual. The harvest-and-scale loop is broken.**
>
> **Problem:**
> - Auto campaigns return 1.24 ROAS. Manual returns 0.86 ROAS. The healthy pattern is the opposite (Manual should beat Auto because the seller has hand-picked the winning keywords).
> - Auto AOV is $20.72 vs Manual $17.62 - auto is finding higher-value buyers. This means Amazon's algorithm is matching the product to more relevant queries than the manual keyword list is.
> - **Auto is doing the discovery work. No one has harvested the winning search terms from Auto and scaled them in Manual exact campaigns.**
>
> **Solution:**
> - Mine the Auto campaign search-term reports for the top converters (Q719 search term report). Identify search terms with 3+ orders at ROAS > 1.5.
> - Launch Manual Exact campaigns for those terms with dedicated budgets and controlled bids.
> - Negate those harvested terms from Auto so spend isn't duplicated.
>
> **Impact:**
> - Current Manual ROAS 0.86 means every $1 of manual spend returns $0.86 in sales (loss). If Manual is brought to Auto's 1.24 ROAS via better keyword selection, current Manual sales of $1,973 become $2,851. **Net incremental: +$878 over 89 days at the same Manual budget.**

### Campaign Profitability

Unprofitable campaigns with meaningful click volume (>20 clicks, ROAS <1.5):

| Campaign | Product | Spend | Sales | ROAS | Clicks | Orders |
|----------|---------|------:|------:|-----:|-------:|-------:|
| Wing LED/manual keyword/Broad | P2 (LED Wings) | $584 | $227 | 0.39 | 978 | 12 |
| Wing LED / Manual/ Phrase | P2 (LED Wings) | $217 | $124 | 0.57 | 386 | 6 |
| All Products /Auto Catchall Campaign | Multi-product | $484 | $452 | 0.93 | 1,243 | 26 |
| Diamond Mount with USB/Manual Keyword/Broad | P0 mount | $501 | $483 | 0.97 | 635 | 21 |
| USB12V/Auto/Close | USB charger | $84 | $45 | 0.53 | 120 | 3 |
| USB 12V/Manual keyword/Broad | USB charger | $69 | $30 | 0.43 | 108 | 1 |
| Wing LED/ Manual Keyword/Exact | P2 (LED Wings) | $68 | $39 | 0.57 | 119 | 2 |
| Wing Led/Auto/Product | P2 (LED Wings) | $82 | $78 | 0.96 | 201 | 3 |
| **Total wasted spend** | | **$2,089** | **$1,478** | | | |

> **Finding: $2,089 (59% of total ad spend) is going to campaigns running at break-even or below**
>
> **Problem:**
> - $2,089 of $3,564 total ad spend (59%) is in campaigns below 1.5 ROAS. Combined ROAS on this bucket: 0.71.
> - The single biggest leak is the **Wing LED product family (P2 from Step 1)**: $951 spent across 4 campaigns, total ad sales $468, total ROAS 0.49. This is the LED Projection Wings - it has lost approximately $483 of margin-equivalent spend over 89 days assuming generous breakeven.
> - The Auto Catchall campaign sprays budget across all products including dead SKUs (Snoodle dog toy, bicycle stem-pieces).
>
> **Solution:**
> - **Pause Wing LED manual campaigns** (Broad, Exact, Phrase). Keep one Auto/Close test campaign at low budget to learn whether the issue is keywords or the listing.
> - **Pause USB 12V Auto/Close and Manual/Broad** ($153 spent, $75 sales, ROAS 0.49). Keep USB 12V Manual/Exact only ($1.25 spend, 11.89 ROAS = real signal at tiny scale).
> - **Restructure Diamond Mount with USB/Manual Keyword/Broad.** This is P0 broad match at 0.97 ROAS. Pause it as-is and rebuild with tighter keywords harvested from Auto.
>
> **Impact:**
> - Pausing the Wing LED Broad/Phrase/Exact campaigns alone saves **$869 of spend over 89 days at the loss of $390 of ad sales** = **net +$479 to gross margin** (and that's before reallocating).
> - Reallocate the saved $869 to FAFO Mount (P3) at its current 1.7-1.8 ROAS = **+$1,478 in incremental sales** over 89 days vs the current state.

### Targeting Strategy

**Keyword vs Product Targeting:**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|-------------------|-------:|------:|------:|-----:|----:|----:|----:|
| Keyword Targeting | 4,466 | $3,099 | $3,061 | 0.99 | $18.78 | $0.69 | 3.65% |
| Product Targeting | 1,204 | $465 | $492 | 1.06 | $18.22 | $0.39 | 2.24% |

Product Targeting performs marginally better at ROAS 1.06 vs 0.99 and at much lower CPC ($0.39 vs $0.69). It's only 13% of spend. Modest reallocation opportunity, but not a primary lever.

**Match Type Breakdown:**

| Match Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|------------|-------:|------:|------:|-----:|----:|----:|----:|
| BROAD | 2,421 | $1,701 | $1,415 | 0.83 | $17.47 | $0.70 | 3.35% |
| PHRASE | 637 | $411 | $402 | 0.98 | $16.76 | $0.65 | 3.77% |
| EXACT | 212 | $139 | $131 | 0.94 | $16.38 | $0.66 | 3.77% |

> **Finding: Broad match dominates spend at the worst ROAS**
>
> **Problem:**
> - 75% of manual keyword spend is going to BROAD match at 0.83 ROAS. PHRASE and EXACT each have better ROAS but get small slices of budget.
> - **EXACT match has only $139 of spend over 89 days.** This is the harvest-and-scale loop again: even when the seller knows which terms convert (and they have an Exact campaign for each product), almost no money is going there.
>
> **Solution:**
> - Apply the same harvest logic from the Auto vs Manual finding: mine Broad and Phrase search-term reports for converting terms, move them into EXACT campaigns with dedicated budgets.
> - Reduce Broad bids on the worst converters (Wing LED Broad already flagged for pause).
>
> **Impact:** Folded into the campaign profitability impact above (Wing LED pause + reallocation).

## Product Level (P0 - Motorcycle Cell Phone Mount with Dual USB-C)

### P0 Campaign Map

| Campaign | Product Family | Spend | Sales | ROAS | Clicks | Orders |
|----------|---------------|------:|------:|-----:|-------:|-------:|
| Diamond Mount With USB/ Auto/close | P0 | $603 | $948 | 1.57 | 728 | 39 |
| Diamond Mount with USB/Manual Keyword/Broad | P0 | $501 | $483 | 0.97 | 635 | 21 |
| All Products Auto Catchall (P0 portion only) | P0 (cross-product) | $63 | $70 | 1.11 | 162 | 3 |
| Diamond Mount with USB/Manual Keyword/Phrase | P0 | $28 | $74 | 2.65 | 36 | 3 |
| Diamond Mount with USB/Manual keyword/exact | P0 | $18 | $23 | 1.28 | 24 | 1 |
| Terminal Velocity Sport / Manual / Keyword All Products (P0 portion) | P0 (branded) | $4 | $23 | 5.51 | 5 | 1 |
| Diamond Mount with USB/ Auto/Compliments | P0 | $0.46 | $0 | 0.00 | 1 | 0 |
| **P0 total** | | **~$1,218** | **~$1,621** | **1.33** | **1,591** | **68** |

**P0 represents 53% of trailing 3-month revenue but only 34% of trailing 90-day ad spend ($1,218 / $3,564).** Under-invested relative to its profit potential.

**Important observation:** Only the **Orange variant (B0CWKTJM9Q)** is being advertised actively. Black (B0DJCR293K), Blue (B0DPWRFNCH), and Yellow (B0DJNS3QS7) collectively received less than $10 of spend over 89 days. Three of four colorways are not being scaled even though all share the same parent listing, ratings, and reviews.

### Blocker-Specific Findings

#### Impression Share Blocker: Keyword Spend vs. Tier 1/2/3 Queries

Section 4 (SQP Analysis) identified impression share as the primary blocker on P0 across all tiers (Tier 1: 0.94%, Tier 2: 0.10%, Tier 3: 0.11%). The PPC lever for impression share is to bid into the keywords where the brand needs more visibility.

The current allocation tells a clear story: the seller is bidding on Tier 2 broad terms (where CVR is 1.0%) instead of concentrating on Tier 1 (where the product fits the intent and CTR already wins).

> **Finding: P0 ad spend is concentrated in the wrong tier**
>
> **Problem:**
> - The Manual Keyword Broad campaign for P0 ($501 spend, 0.97 ROAS, 635 clicks) is the largest manual-keyword bet. It is almost certainly catching Tier 2 "motorcycle phone mount" generic queries, which has 1.0% brand CVR per SQP data, not the Tier 1 "motorcycle phone mount with charger" queries.
> - The Manual Phrase campaign for P0 ($28 spend, 2.65 ROAS) - which is presumably catching tighter intent - is getting **18x less spend** than the broad campaign that is losing money.
> - Auto/close on P0 returns 1.57 ROAS = Amazon's algorithm is finding more profitable customers than the manual keyword list is.
>
> **Solution:**
> 1. **Pause** Diamond Mount with USB/Manual Keyword/Broad ($501 spend at 0.97 ROAS).
> 2. **Mine** the Auto/close campaign for its top-converting search terms (which average 1.57 ROAS).
> 3. **Launch** a tight Manual/Exact campaign with the harvested terms targeting Tier 1 keywords ("motorcycle phone mount with charger", "motorcycle phone charger", "motorcycle usb charger") at a dedicated ~$300/90-day budget.
> 4. **Negate** Tier 1 terms from the Auto/close so they don't compete with the new Manual/Exact campaign.
> 5. **Add ads for the other 3 P0 color variants** (Black, Blue, Yellow). Currently zero spend on three variants of the hero product.
>
> **Impact:**
> - Reallocating the $501 from the unprofitable Broad campaign at 0.97 ROAS into Tier 1 Manual Exact at expected 1.8-2.5 ROAS (between current Phrase 2.65 and Auto/close 1.57) = **+$400 to $750 in incremental sales** over 89 days at the same P0 budget.
> - Scaling P0 Phrase from $28 to $250 at 2.0 ROAS (assuming some efficiency loss as it scales) = additional **+$430 in sales** over 89 days.
> - Activating ads for the other 3 P0 colorways at modest budgets ($150 each over 89 days at expected 1.3 ROAS) = additional **~$585 in sales** over 89 days.
> - **Combined P0 impression-share play: +$1,400 to +$1,750 in incremental sales over 89 days, before any CVR fix.**

#### CVR Secondary Blocker

From SQP: brand CVR is 4x below industry on Tier 1 (2.1% vs 8.2%) and 11x below on Tier 2 (1.0% vs 11.0%). PPC levers for CVR are placement targeting and reducing wasted spend on non-converting search terms.

For this audit, the placement-level breakdown wasn't pulled because the data window is short (89 days) and most P0 spend goes to two campaigns. The bigger CVR fix is on the listing side (Step 2e: rewrite/move bullet 6 caveats, add comparison module, fix title typo). The PPC contribution is to ensure spend goes to placements that convert and to terms that match the product's actual fit.

**Solution (CVR):** Sequence the listing fixes BEFORE scaling P0 spend aggressively. Step 2e identifies the concrete changes. Once CVR improves on the PDP, the impression-share scaling plan above can be pushed harder without burning budget.

## Insights

- **The account is at break-even on ads** (ROAS 1.00). After COGS and Amazon fees, this is a net loss on advertising. The current pattern is "ads turned on, but no optimization loop". Even small structural changes (auto-to-manual harvest, pausing Wing LED) materially improve net profit.
- **Wing LED (P2) is the single biggest leak**: ~$967 spent for $467 in ad sales. Three months of consistent below-1.0 ROAS across 4 campaigns is enough data to act on. Per Step 2/3 analysis on the LED Wings product (not deep-dived in this audit), the product likely has a structural CVR issue (1.49% on a category where 5-6% is typical) that needs addressing before any spend should resume.
- **P3 (FAFO Mount) is the most efficient product in the catalog** at 1.7-1.8 ROAS across all campaigns, but receives only 3% of total ad spend ($104). Every dollar redirected from Wing LED to FAFO Mount roughly triples its revenue output.
- **The branded defense campaign is working as designed**: "Terminal Velocity Sport / Manual / Keyword All Products / All Types" - $27 spend at 3.60 ROAS. Small share of budget, well-positioned protective campaign. Per CLAUDE.md, branded spend should stay under 5% of total - currently at <1%, leave it alone.
- **Three of four P0 color variants are unadvertised**. The seller is leaving organic ranking and incremental sales on the table on Black, Blue, and Yellow.
- **The Auto Catchall campaign is doing too much**: it's running ads for the dead SNOODLE dog toy, for bicycle stem-pieces with zero sales, for the bleeding-money Wing LED, and for the P0 phone mount all under one campaign. Should be split.

## Things to Investigate

- **Top search terms inside Auto/close for the Diamond Mount With USB campaign.** This is where Amazon's algorithm has been finding the 1.57-ROAS customers. The exact terms that are converting will reveal the right Tier 1 / Tier 2 mix and inform the new Manual Exact campaign keyword list. Pull Q717/Q719 for this campaign as the next data point.
- **Search-term level analysis for the Wing LED Manual Broad campaign.** Before fully pausing it, look at whether ANY search terms in there have ROAS > 1.0. If a small subset is profitable, harvest those; pause the rest.
- **Placement breakdown for Diamond Mount With USB campaigns.** If Top of Search is driving most of the conversions at higher CVR than Rest of Search or Product Pages, increase Top of Search bid modifier when scaling.

## Questions for the Seller

- The Wing LED (American Eagle Projection Wings) product has been on negative ROAS ads for 89 days. Was there a specific campaign strategy goal (brand awareness, new product launch push), or has it been on autopilot? We want to confirm before recommending a pause.
- You have one ASIN advertised for the Diamond Mount With USB family (Orange / B0CWKTJM9Q). The Black, Blue, and Yellow variants of the same product are not being advertised. Was this an intentional concentration decision (color preference data), or has it been overlooked?
- The Snoodle dog toy has 5 active ad campaigns running but $0 sales. Is this product still in-scope, or has it been deprioritized? We want to fully pause the campaigns if so.
