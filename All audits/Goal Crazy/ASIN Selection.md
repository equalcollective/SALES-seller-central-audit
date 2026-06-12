# ASIN Selection: Goal Crazy

## Data Readiness

- **Business data:** Jul 2024 to Mar 15, 2026
- **Ad data:** 89 days (Dec 25, 2025 to Mar 23, 2026)
- **Analysis window:** Dec 2025 to Feb 2026 (3 complete months)
- **Note:** Ad data only exists from late Dec 2025. The brand had zero ad spend from Mar to Nov 2025, running entirely on organic sales.

## Catalog Overview

Goal Crazy has 3 parent ASINs but only one is active:

| Parent ASIN | Product | 3-Mo Sales | 3-Mo Units | Status |
|------------|---------|-----------|-----------|--------|
| B085TN9RTW | Undated Planner 2025 2026 | $8,959.95 | 332 | Active (6 children) |
| B091FYBJH9 | Habit Cards | $0 | 0 | Dead |
| B0B8JS5B7J | Undated Planner 2024 2025 | $0 | 0 | Dead (predecessor, replaced by 2025/2026 version) |

## Priority Table

| Priority | Product | 3-Mo Sales | 3-Mo Ad Spend | ROAS | TACoS | Organic Sales | Ad Sales % | Buy Box % | CVR | Trend |
|----------|---------|-----------|--------------|------|-------|---------------|-----------|-----------|-----|-------|
| P0 | Undated Planner 2025 2026 | $8,960 | $424 | 5.06 | 4.7% | $6,815 | 24.0% | 94.4% avg | 10.1% avg | Declining (seasonal) |

No P1, P2, or P3. Habit Cards and the older planner have zero sales across all 3 months.

## P0 Annual Trend

| Metric | Mar 2025 | Jun 2025 | Sep 2025 | Dec 2025 (Peak) | Jan 2026 | Feb 2026 |
|--------|----------|----------|----------|----------------|----------|----------|
| Total Sales | $3,509 | $3,495 | $3,727 | $5,008 | $2,868 | $1,083 |
| Sessions | 1,343 | 1,095 | 1,318 | 1,162 | 1,241 | 412 |
| CVR | 9.0% | 9.1% | 9.5% | 17.3% | 8.1% | 7.5% |
| Buy Box % | 99.6% | 99.6% | 83.0% | 100.0% | 83.2% | 100.0% |
| Ad Spend | $0 | $0 | $0 | $75 | $254 | $94 |

- **Strong seasonal peak in December.** Sales nearly doubled ($5K) driven by a CVR spike to 17.3%, likely from New Year resolution / gift-giving demand for planners. This is the clearest seasonality signal in the data.
- **Consistent organic base of $2.5K-$3.7K/mo through Mar-Nov 2025 with zero ad spend.** The product has real organic demand and does not depend on ads to generate sales. This is a strong foundation.
- **Buy box dropped from ~99-100% to ~83% starting August 2025.** It has toggled between 83% and 100% since. When buy box is at 83%, roughly 1 in 6 sessions is being lost to another seller, directly suppressing CVR and sales. This is a recurring issue, not a one-time event.
- **Feb 2026 shows a sharp traffic decline (412 sessions vs. 891-2,154 range in prior months).** This is likely seasonal (post-New Year planner demand drops), but the magnitude is worth investigating.

## Insights

- **Single-product brand.** All revenue comes from one planner listing with 6 color variations. Habit Cards is dead. The older planner version has been fully replaced. This means the audit is entirely about maximizing the P0 ASIN.
- **The brand was 100% organic until December 2025.** They only started running ads ~3 months ago. This creates a clear growth opportunity: the product already converts well organically, and ads are a new, largely untapped lever.
- **TACoS is healthy at 4.7%.** Even with the recent ad ramp-up, ads account for only ~24% of total sales. The organic base is strong.

## Things to Investigate Further

- **Buy box instability (83% in Aug-Nov, Jan).** Is there a competitor or another seller on this listing winning the buy box ~17% of the time? This directly impacts CVR and is a constraint on growth. Need to check via Keepa/Metabase in Product Understanding.
- **Feb 2026 traffic collapse (412 sessions).** Is this purely seasonal for the planner category, or has organic ranking dropped? Compare to prior-year Feb if data allows.
- **Ad strategy effectiveness.** The brand tripled ad spend from Dec ($75) to Jan ($254), but ROAS dropped from 8.44 to 4.43. Need to assess whether the ad scaling was efficient or whether spend was wasted.

## Questions for the Seller

- **What changed in August 2025 that caused buy box to drop from ~100% to ~83%?** Was a new seller authorized on the listing, or did an unauthorized reseller appear? The buy box has been unstable since (83% in Aug, Sep, Oct, Nov, Jan; 100% in Dec, Feb).
