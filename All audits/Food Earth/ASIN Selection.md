# Food Earth — ASIN Selection

## Data Readiness

- **Business data:** 2024-07-01 to 2026-05-03
- **Ad data:** 2026-02-15 to 2026-05-14 (89 days, just over the 70-day threshold)
- **Analysis window:** Feb-Apr 2026 (3 complete months)
- **Caveat:** Feb ad spend reflects only Feb 15-28 (half month), so February ad metrics are artificially low. Real ramp begins March.

## Catalog Context

- 46 parent ASINs / 65 children. Long tail of single-child parents, most with zero or near-zero sales.
- Only 4 parents have meaningful 3-month revenue. The next tier drops below $325 / 3-mo.
- Latest month (Apr 2026) account-level: $10,013 sales, $3,002 ad spend, blended ROAS 0.93, TACoS 30.0%. Confirms Bilal's call comment: "to get 10K in sales, you're spending 6K in ads." Our data shows $3K in ad spend on Seller Central, suggesting the additional spend may be off-Amazon or includes other Amazon fees.

## Priority Table

| Priority | Product | 3-Mo Sales | 3-Mo Ad Spend | ROAS | TACoS | Organic Sales | Ad Sales % | Buy Box % | CVR | Trend |
|----------|---------|-----------|--------------|------|-------|---------------|-----------|-----------|-----|-------|
| **P0** | Ready to Eat Indian Cuisine Bundle (B0GX9VV9ST) | $14,455 | $2,399 | 1.22 | 16.6% | $11,521 | 20.3% | 79.3% | 6.0% | Growing |
| **P1** | Indian Simmer Sauce (B0GMP7GG3S) | $7,958 | $819 | 1.84 | 10.3% | $6,449 | 19.0% | 83.0% | 7.1% | Growing |
| **P2** | Hug in a Bowl Soup, Five Lentil Coconut (B0FCBXWGF2) | $2,231 | $850 | 1.19 | 38.1% | $1,220 | 45.3% | 98.7% | 6.3% | Flat |
| **P3** | Hong Kong Noodle (B0GY96D8CX) | $926 | $1,361 | 0.48 | 147% | $279 | 69.9% | 99.7% | 6.3% | New launch, burning |

**Note on excluded parents:** All other parents are below $325 / 3-mo. Several have ad spend but negligible sales (A Perfect Marriage Soup, Lentil & Quinoa Soup, multiple Dip/Chutney parents). They will be addressed at an account level in Ad Analysis (campaign profitability) rather than treated as focus ASINs.

## P0 Parent Structure: Critical Flag

The parent B0GX9VV9ST ("Ready to Eat Indian Cuisine Bundle") groups **9 distinct meal products** under a single parent. These are not true variants (color/size) — they are different recipes that solve different customer needs:

| Child ASIN | Variant | 3-Mo Sales | 3-Mo Ad Spend | CVR (latest) | Buy Box (latest) |
|------------|---------|-----------|--------------|-------------|------------------|
| B0D8Q9MMT9 | Six Flavor Variety Pack | **$5,333** | $30 | 6.2% | 97.6% |
| B086WPJGXQ | Vegetable Biryani | $4,017 | $2,362 | 6.5% | 98.2% |
| B086VQ7HM7 | Split Lentil Curry w/ Steamed Rice | $1,328 | $0 | 15.0% | 88.8% |
| B0CLBLZWR7 | Trio Pack (Bombay Lentil, Five Lentil, Madras Coconut) | $1,152 | $4 | 4.8% | 98.3% |
| B0CLBMXQS3 | Trio Pack (Split Lentil, Chickpeas, Veg Biryani) | $936 | $2 | 5.2% | 98.7% |
| B0CQM1D7BK | Five Lentil Curry w/ Turmeric Rice | $882 | $0 | 15.6% | 97.1% |
| B0CQLZPYPT | Madras Coconut Curry w/ Turmeric Rice | $571 | $0 | 12.7% | **83.0%** |
| B0CQLYTFPK | Bombay Lentil Curry w/ Turmeric Rice | $168 | $1 | 0% | 56.1% |
| B086VPCC7N | Chickpeas Curry w/ Steamed Rice (Pack of 6) | $71 | $0 | 0.8% | **14.3%** |

**Implications for Step 2 (Product Understanding):**
- The hero child for deep-dive is the **Six Flavor Variety Pack (B0D8Q9MMT9)** — highest revenue, near-zero ads, healthy CVR, near-100% buy box. The variety pack is the natural entry product for new customers and the brand's largest organic engine.
- **Misallocation flag:** ~98% of P0 ad spend is going to a single child (Vegetable Biryani, ROAS 1.0-1.2). The actual revenue leader (Variety Pack) gets almost no ad support despite a healthier CVR. This is a major lever in Ad Analysis.
- Two children have severe child-level buy box problems: **B086VPCC7N (Chickpeas Curry, BB 14.3%)** and **B0CQLYTFPK (Bombay Lentil, BB 56.1%)**. Per the call, this is a private-label brand with no third-party sellers, so likely MAP/pricing related. Worth flagging.

## P0 Annual Trend (Parent B0GX9VV9ST)

| Metric | Sep 2025 | Dec 2025 | Feb 2026 | Apr 2026 |
|--------|---------|----------|----------|----------|
| Total Sales | $3,103 | $3,242 | $4,217 | $5,010 |
| Sessions | 1,714 | **3,748** | 2,977 | 2,616 |
| CVR | 6.18% | **3.20%** | 5.21% | 6.50% |
| Buy Box % | 84.08% | **58.24%** | 73.85% | 81.33% |

- **The story is buy box, not ads.** From Sep to Dec 2025, buy box collapsed from 84% to 58%. Sessions more than doubled in Q4 (likely holiday + gifting traffic), but CVR halved because the brand couldn't convert visitors when it wasn't holding the buy box. Sales stayed flat at ~$3k despite the traffic surge.
- **Recovery preceded the ad ramp.** Buy box began recovering in Feb 2026 (74%) before any meaningful ad spend was deployed. The current growth (Feb $4.2k -> Apr $5.0k) is largely a buy box recovery story, not an ad performance story. The ads (starting March at $1.1k/month) added ~$1.3k/month in ad sales but came at TACoS of 21%.
- **Same pattern in P1 (Simmer Sauce):** Buy box jumped from 71% (Feb) to 89% (Mar/Apr), correlating with that product's 50% sales growth. The buy box recovery is account-wide.

## Insights

- **The agency's hypothesis (CPC is the blocker) is unconfirmed and likely incomplete.** The bigger driver of recent growth is the buy box recovery from Oct-Jan lows, not the ad ramp. Without understanding why buy box dropped and whether it's now stable, scaling ad spend is risky.
- **P0 ad spend is concentrated on the wrong child.** Vegetable Biryani (B086WPJGXQ) absorbs ~98% of the P0 parent's ad budget at ROAS 1.0-1.2, while the Six Flavor Variety Pack (B0D8Q9MMT9, the actual revenue leader with healthier CVR) gets essentially no ad support. Reallocating spend is an immediate, low-risk lever.
- **P3 Hong Kong Noodle is a budget leak.** 147% TACoS on $926 of revenue means ~$1,000 / 3-mo lost to a product that has not found product-market fit yet. Either the launch needs more time with reduced spend, or the spend should be paused entirely until the product is ready to scale.
- **P2 Hug in a Bowl Soup is over-dependent on ads.** 45% of sales come from ads, ROAS 1.19. Without ads the product would be doing ~$400/mo. The Feb-to-Apr trend shows ad spend grew 7x while organic sales declined.

## Things to Investigate Further

- **Why did P0 buy box collapse Oct-Dec 2025?** No third-party sellers on the listing (per Bilal). Likely candidates: MAP-violating price changes by the seller themselves (possibly via promos/coupons), pricing alerts from Amazon vs. external retailer prices (Walmart, DTC, Instacart), or a stockout / FBA replenishment issue. To assess in Step 2 via Keepa price history.
- **Are the two child-level buy box problems (Chickpeas Curry at 14%, Bombay Lentil at 56%) MAP-related?** Both are pack-of-6 single-flavor SKUs. If MAP is the root cause, the fix is centralized pricing across channels rather than per-listing intervention.
- **Was Q4 2025 traffic spike actual demand or low-quality traffic?** Sessions doubled while CVR halved. Worth verifying in Step 3 (SQP) whether this was relevant search traffic (real holiday demand for Indian food) or off-target placements / lookups.

## Questions for the Seller

- Buy box for the Ready-to-Eat Bundle dropped to 58% from October through January and recovered to 80%+ by March. Was there a pricing change, an Amazon price-match issue with Walmart / DTC / Instacart, or a stockout during that window?
- The Six Flavor Variety Pack is your highest-revenue child but receives almost no ad spend, while ~98% of the bundle parent's ad budget goes to Vegetable Biryani at ROAS ~1.0. Was this an intentional strategy, or was the agency just running what was already set up?
- Hong Kong Noodle launched in March with $1.4k of ad spend over 2 months returning $647 (ROAS 0.48, TACoS 147%). Is this a deliberate launch investment with a runway you're willing to absorb, or are you unaware of the loss rate?
