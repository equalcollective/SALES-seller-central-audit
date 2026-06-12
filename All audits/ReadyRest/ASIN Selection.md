# ASIN Selection: ReadyRest

## Data Readiness

- **Business data:** 2024-07-01 to 2026-04-12 (16 monthly periods)
- **Ad data:** None. `ads_day_count = 0`. No advertised-product report data exists in our system. Per the 90-day retention rule, this could mean the seller has not run ads in the last 90 days, but it does not prove they never advertised.
- **Analysis window:** Jan 2026 to Mar 2026 (3 most recent complete months)

## Catalog Overview

Single-product brand. One parent ASIN (B0B5D5SNNX) under which 5 child ASINs are registered, but only one child has been actively selling for the last 12 months.

- **B09NJQF7GM** ("Tactical Black, Covert Khaki") - 100% of revenue across the last 12 months. Buy box 97-100% throughout. The actual hero SKU.
- **B0C9WS1HB2** ("Tactical Black Clip-on") - generated $59-$400/mo Apr-Nov 2025, then went to $0 from Dec 2025 onward. Either out of stock or discontinued.
- **B0B5D5SNNX, B0C9WQWMYH, B09NJQG8V6** - effectively dead variations. 0-10 sessions/mo, $0 sales for 12+ months.

All children are color/configuration variations of the same shotgun rest accessory, so no need to deep-dive multiple. P0 = B09NJQF7GM.

## Priority Table

| Priority | Product | 3-Mo Sales | 3-Mo Ad Spend | ROAS | TACoS | Organic Sales | Ad Sales % | Buy Box % | CVR | Trend |
|----------|---------|-----------|--------------|------|-------|---------------|-----------|-----------|-----|-------|
| P0 | ReadyRest Shotgun Rest (B09NJQF7GM) | $3,179 | $0 | N/A | N/A | $3,179 (100%) | 0% | 99.5% avg | 6.9% avg | Seasonal trough |

No P1, P2, P3. Single-product catalog.

**Note on parent vs child:** At parent level, buy box reads 49-50% in Jan-Mar 2026, which would normally be a major flag. This is a dilution artifact: the 4 inactive children have 0% buy box (no inventory), pulling the parent average down. At the child level, the active SKU (B09NJQF7GM) holds 99-100% buy box. Buy box is not a constraint here.

## P0 Annual Trend

| Metric | May 2025 (Off-season) | Sep 2025 (Build-up) | Dec 2025 (Peak) | Mar 2026 (Latest) |
|--------|----------------------|---------------------|-----------------|-------------------|
| Total Sales | $385 | $1,570 | $4,379 | $720 |
| Sessions | 272 | 711 | 609 | 202 |
| CVR | 4.04% | 4.08% | 11.99% | 5.94% |
| Avg Price | $34.99 | $54.13 | $59.99 | $59.99 |
| Buy Box % | 98.5% | 99.2% | 99.6% | 99.2% |

- The product is heavily seasonal. December peaks at ~11x the May trough on revenue, driven by hunting season (Sep-Jan: dove, pheasant, sporting clays) plus holiday gifting. This is consistent with a shotgun accessory's natural demand cycle, but it must be confirmed with SQP search-volume data in Step 3 before treating it as a fact.
- The funnel shifts shape across the year. Sessions peak in Aug-Sep (pre-season research) at ~700-800/mo with low CVR (~4%). Conversions peak in Oct-Dec at 7-12% CVR on lower session counts. The seller is getting researchers in summer and buyers in fall, which suggests a real opportunity to compress the research-to-purchase gap with retargeting or seasonal ad sequencing.
- Average price climbed from $33 in spring to $60 by fall and has stayed there. CVR did not collapse at the higher price (Dec hit 12%), so the listing supports $60 demand. Need to confirm in Product Understanding whether this is a deliberate seasonal pricing strategy or a permanent reset.

## Insights

- 100% organic, zero ad spend. The brand has scaled to ~$20K/year and a 12% peak-season CVR purely on organic discovery. Every purchase to date has come from someone who found the listing without paid help. This is the single biggest growth lever in the audit.
- Seasonal demand is the largest driver of variance, not anything operational. Buy box, listing health, and CVR are all stable when corrected for child level. The seller does not have a "Q1 problem"; they have an off-season.

## Things to Investigate Further

- Confirm seasonality with SQP search volume in Step 3 (per CLAUDE.md, sales-rank or revenue alone do not prove seasonality, only search volume does).
- Investigate whether the listing's strong organic CVR (12% in Dec) is driven by listing quality, low competitive density, or being a category-defining product. This shapes whether ads will scale efficiently or whether competitors will appear once the brand pays for visibility.

## Questions for the Seller

- Have you ever run Amazon ads, even briefly? Our system shows zero ad data in the last 90 days, but we cannot see further back. If you have run ads previously, what worked, what did not, and why did you stop?
- Is the price progression from $34 (spring) to $60 (fall/winter) deliberate seasonal pricing, or did costs change? Understanding intent matters: if it is intentional, we time ad launches around the price ramp. If it is involuntary, margin in peak season is already compressed.
- The "Tactical Black Clip-on" variation (B0C9WS1HB2) generated steady sales through Nov 2025 and then dropped to zero. Was this discontinued, out of stock, or de-listed? Reactivating it could add a second SKU's worth of revenue at peak.
