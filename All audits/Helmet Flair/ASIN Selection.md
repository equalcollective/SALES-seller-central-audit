# Step 1: ASIN Selection - Helmet Flair

## Data Readiness

- **Business data:** 2024-07-01 to 2026-05-10 (good, ~22 months)
- **Ad data:** 2026-02-21 to 2026-05-20 only (~90 days, the standard advertised-product report window). February ad data is partial (ads ramped mid-month: Feb ad spend was $925 across the account vs $3.7k in March), so the clean ad months are March and April 2026.
- **Selection window:** Feb-Apr 2026 (3 months), noting Feb ad figures are understated.

## Catalog Overview

Helmet Flair sells novelty helmet accessories (devil horns, cat ears, unicorn horns, banana, corn cob) that attach to bike, motorcycle, ski, and airsoft helmets. Two product lines:

- **MagNeatOhz** - magnetic and interchangeable attachments. The premium line, ~$30-35 price point. This is where nearly all the revenue sits.
- **Softeez** - foam peel-and-stick attachments. The budget line, ~$15-20 price point. Small revenue, and the data shows attribution problems (see Data Quality Notes).

All products are private label, made in USA, sold only by Helmet Flair.

## Priority Table (Feb-Apr 2026)

| Priority | Product | 3-Mo Sales | 3-Mo Ad Spend | ROAS | TACoS | Organic Sales | Ad Sales % | Buy Box % | CVR | Trend |
|----------|---------|-----------|--------------|------|-------|---------------|-----------|-----------|-----|-------|
| P0 | Cat Ears (MagNeatOhz) - B08Q1PMMTQ | $18,454 | $2,147 | 4.30 | 11.6% | $9,212 | 50.1% | ~80% | ~4.9% | Growing |
| P1 | Large Devil Horns (MagNeatOhz) - B08Q1NJK7G | $17,370 | $2,354 | 3.86 | 13.6% | $8,293 | 52.3% | ~85.6% | ~4.3% | Growing (fastest) |
| P2 | Small Devil Horns (MagNeatOhz) - B08KPHDFDB | $12,652 | $1,371 | 3.99 | 10.8% | $7,185 | 43.2% | ~85.7% | ~5.1% | Growing |
| P3 | Extra Nubbins - B0C3NCJSGV | $957 | $52 | 7.93 | 5.4% | $548 | 42.7% | ~100% | ~14% | Growing |

**Products not prioritized:**
- The Softeez foam line (Cat Ears B0BXZ2SF4Q ~$1,400, Devil Horns B0BXY6CGTZ ~$1,100) and the two Unicorn Horn parents (~$350-600 each) are all small (<$500/mo each) and several are declining. They are budget variants of the hero SKUs, not independent growth drivers.
- Banana (B08HFF37DD): ~$290/mo, low CVR (1.7-3.4%), flat-to-declining. Niche novelty item.
- Corn Cob (B0DXQTNNKK): newest SKU, near-zero sales (1-2 units/mo). Essentially a soft launch.

## P0 Selection Rationale

Cat Ears (B08Q1PMMTQ) and Large Devil Horns (B08Q1NJK7G) are nearly tied. Cat Ears wins P0 on:
- Highest trailing 3-month sales ($18,454 vs $17,370) and highest annual peak (May 2025: $11,219 vs $10,939).
- Best blended ROAS (4.30) and lowest TACoS (11.6%) of the hero SKUs.

Large Devil Horns is a very close P1 and is actually growing fastest (Feb $4,054 to Apr $7,060, +74%). Both hero SKUs are strong, and SQP/Ad analysis may reinforce going deep on both. For this audit, P0 deep-dive is Cat Ears.

## P0 Annual Trend (Cat Ears - B08Q1PMMTQ)

| Metric | May 2025 (peak) | Nov 2025 (trough) | Feb 2026 | Apr 2026 (latest) |
|--------|-----------------|-------------------|----------|-------------------|
| Total Sales | $11,219 | $4,963 | $5,347 | $6,640 |
| Sessions | 6,385 | 2,518 | 2,969 | 4,122 |
| CVR | 5.09% | 5.68% | 5.19% | 4.66% |

- **Strong seasonal pattern.** Sales peaked in May/June 2025 ($11.2k), declined through summer and fall to a $4-5k trough around Nov 2025 and Jan 2026, and are now climbing back as spring returns. The account-level pattern is identical (May 2025 peak $34k, Jan 2026 trough $13k). This points to spring/summer seasonality (helmet/riding season), to be verified against SQP search volume in Step 3. We are now entering peak season, which makes the next 8-12 weeks the highest-leverage window to scale.
- **Sessions track sales (demand-driven), CVR is stable and healthy (~5%).** The decline was a traffic story, not a conversion story. CVR has held in the 4.7-5.7% range all year (the Dec 7.8% spike was a holiday price promo at $29.80 vs the usual $34.50). Conversion is not the problem; visibility is.

## Insights

- **The catalog is highly concentrated and seasonal.** The three MagNeatOhz hero SKUs (Cat Ears, Large Devil Horns, Small Devil Horns) drive ~85% of revenue, all follow the same spring-peak seasonal curve, and all are growing into the current peak. Effort focused on these three compounds.

## Things to Investigate Further

- **Seasonality confirmation.** Verify the spring/summer demand pattern against SQP 12-month search volume in Step 3 before treating it as fact. If confirmed, the action plan should front-load ad scaling now.
- **Ad scaling headroom.** Ad spend roughly 4x'd from Feb to Mar across the account ($925 to $3,719) while ROAS held at ~4. Step 4 should determine whether there is room to scale further into peak season at acceptable ROAS.

## Questions for the Seller

- **Ad data only goes back to Feb 21, 2026.** Were you advertising before February, and if so, what was the historical strategy and budget? (We can only see the last ~90 days of ad data, so we need this context rather than assuming ads started in February.)

## Data Quality Notes

- **`get_metrics` parent filter does not work.** Passing a `parent_asin` to `get_metrics` returns account-level totals, not the parent. All parent-level annual trends in this audit were pulled via `get_pivot_table` (aggregation_level=parent) instead.
- **Ad attribution is duplicated/cross-attributed on the tail SKUs.** The Softeez Cat Ears parent (B0BXZ2SF4Q) shows the exact same ad spend ($978.64) and ad sales ($4,178.95) as the MagNeatOhz Cat Ears (B08Q1PMMTQ), producing impossible negative organic sales (-$3,880). The same duplication appears on Softeez Devil Horns (B0BXY6CGTZ) and across the two Unicorn parents. This does not affect the three hero SKUs, whose ad data is clean, but the tail-SKU ad figures should not be trusted.
