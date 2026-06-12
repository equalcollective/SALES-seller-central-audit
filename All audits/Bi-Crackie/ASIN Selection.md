# ASIN Selection - Bi-Crackie

## Data Readiness

- Business data: 2024-07-01 to 2026-04-12 (latest complete month: March 2026)
- Ad data: **none available in the system** (`ads_day_count: 0`). Per the ~90-day window, this means no ads have been running in the last 90 days. Historical ad activity is unknown and must be confirmed with the seller.
- Catalog: 1 parent ASIN (B0D86S4HNF) with 5 child variants of the same product (BICRACKIE Stand-Up Crack Weeding Tool).

Selection window: Jan 2026 to Mar 2026 (last 3 complete months). However, this product is strongly seasonal (peak May to July). The 12-month rolling view is used to confirm priority order, since Q1 is the off-season trough and would distort rankings.

## Catalog Note: Single-Product Brand

All four selling SKUs (B0C9KWVCTY, B0D868RNVJ, B0D86DYYC6, B0D86DVNYH) are variants of the same BICRACKIE weeding tool. They share product identity, customer, brand, and competitive landscape. The differences are color/size SKU variations and one bundle:

- B0C9KWVCTY: BICRACKIE Weeding Tool (original, the parent listing's main face)
- B0D868RNVJ: Purple Paver Weeder (color and use-case variant for paver cracks)
- B0D86DYYC6: Original & Paver Weeder Set (bundle of the two)
- B0D86DVNYH: BICRACKIE Junior (smaller version)
- B0D86S4HNF: parent ASIN (no independent traffic, rolled into B0C9KWVCTY)

Step 2 to Step 4 will deep-dive on the parent listing as a single product, with B0C9KWVCTY as the canonical child for SQP and ad analysis.

## Priority Table (3-Month: Jan to Mar 2026)

| Priority | Product | 3-Mo Sales | 3-Mo Ad Spend | ROAS | TACoS | Organic Sales | Ad Sales % | Buy Box % | CVR | Trend |
|----------|---------|-----------|--------------|------|-------|---------------|-----------|-----------|-----|-------|
| P0 | BICRACKIE Weeding Tool (original, B0C9KWVCTY) | $179.96 | n/a | n/a | n/a | $179.96 | 0% | 98.1% | 2.26% | Seasonal (off-season trough) |
| P1 | Purple Paver Weeder (B0D868RNVJ) | $269.94 | n/a | n/a | n/a | $269.94 | 0% | 100% | 7.32% | Seasonal (off-season trough) |
| P2 | Original & Paver Weeder Set (B0D86DYYC6) | $79.99 | n/a | n/a | n/a | $79.99 | 0% | 100% | 2.78% | Seasonal (off-season trough) |
| P3 | BICRACKIE Junior (B0D86DVNYH) | $0 | n/a | n/a | n/a | $0 | 0% | 100% | 0% | Dead |

### Priority Logic

P0 vs P1: In Q1 2026 alone, P1 (Purple Paver) outsold P0 in revenue ($270 vs $180) and crushed it on CVR (7.3% vs 2.3%). However, on the 12-month rolling view (Apr 2025 to Mar 2026), P0 has higher total revenue ($3,959 vs $3,329) and ~40% more sessions (2,470 vs 1,748). P0 is also the parent listing's primary face. P0 stays as the hero, but the Purple Paver's CVR strength is a notable signal for Step 2 / Step 3.

P3 (BICRACKIE Junior) is functionally dead: 600+ sessions across the trailing 12 months and only 1 unit sold. Will not be deep-dived in later steps.

## Annual Trend (Account Level, P0 represents most of revenue)

Single-product brand with clear seasonality. Account-level monthly sales:

| Metric | Mar 2025 (peak ramp) | Jun 2025 (peak) | Aug 2025 (drop) | Mar 2026 (current) |
|--------|---------------------|-----------------|-----------------|--------------------|
| Total Sales | $1,205 | $2,150 | $390 | $305 |
| Sessions | 729 | 1,268 | 263 | 181 |
| CVR | 3.57% | 3.86% | 3.04% | 3.31% |
| Buy Box % | 99.79% | 99.74% | 99.38% | 100.0% |

- The brand has clear spring/summer seasonality (Mar to Jul) consistent with a weeding tool. Peak month June 2025 was 5x the trough month. April to July is the right window for active intervention. The audit is happening at a perfect moment, peak season is starting.
- **Year-over-year decline from peak:** Mar 2025 ($1,205) vs Mar 2026 ($305) is a 75% YoY decline at the same point in the seasonal cycle. Sessions also fell from 729 to 181 (-75%). This is significant. Either the brand has lost organic visibility, the listing has degraded, or ads were running last spring and are not now (ads_day_count is 0 today, but we don't know what was running 12 months ago).
- **Anomalous August 2025 drop:** sales fell 75% from July ($1,535) to August ($390), with sessions dropping 67% (795 to 263). Hard to attribute from data alone. Possible causes: stock-out, inventory issue, ad pause, or listing suppression. Question for the seller.
- **December 2025 buy box dip:** dropped to 73.6% account-wide for one month (vs 95-99% otherwise). On a private-label single-seller listing, this typically points to a MAP or pricing event triggering buy box suppression. Will check with the seller.

## Insights

- **The brand is effectively a one-product business.** All meaningful revenue ties to the BICRACKIE weeding tool. Growth strategy = grow this one product. There is no portfolio rebalancing lever.
- **No ads currently running.** With 0 ad spend over the last 90 days, all current sales are organic. For a seasonal product entering peak season, this is the single biggest unlocked lever, ad spend at this moment of the year compounds.
- **P3 (BICRACKIE Junior) is dead.** 600+ sessions across the year and 1 unit sold across that window means the variant either fails to convert (likely listing/product-fit issue at the variant level) or is mis-positioned. Not a focus, but worth flagging as a discontinue/relaunch question.

## Things to Investigate Further

- **YoY decline (Mar 2025 to Mar 2026, -75%) at same seasonal point.** Need to dig into SQP to see whether brand impression share has eroded, and check whether the seller was running ads last spring.
- **P1 (Purple Paver) Q1 CVR of 7.3% vs P0 CVR of 2.3%.** Why does the same tool with a different color/positioning convert 3x better when shown? This may have implications for which child to push hardest in peak season.

## Questions for the Seller

- Sales dropped 75% from July 2025 ($1,535) to August 2025 ($390), with sessions falling 67%. Was this a stock-out, inventory issue, ad pause, or something else?
- Buy box fell to 73.6% account-wide in December 2025 (otherwise 95-99% all year). On a private-label single-seller listing this typically points to a price/MAP event. Was there a price change or pricing rule that may have triggered buy box suppression?
- Have you run Sponsored Products / Sponsored Brands / Sponsored Display ads in the last 12 months? If yes, what was the rough monthly spend and which products did you advertise? (We have no ad data in the system; advertised product reports cover ~90 days, so we cannot see further back without your input.)
- BICRACKIE Junior (smaller version) accumulated 600+ sessions over the trailing 12 months and sold 1 unit. Is this variant being intentionally maintained, and is there a reason it converts so poorly compared to the original?
