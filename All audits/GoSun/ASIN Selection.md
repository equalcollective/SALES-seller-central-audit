# Step 1: ASIN Selection - GoSun

## Data Readiness

- **Business data:** 2024-07-01 to 2026-04-19 (full coverage)
- **Ad data:** None. `ads_day_count = 0`. The seller is either not running Amazon Ads or the data is not ingested. Per Aryan, no ads are currently running, so this audit will treat the account as fully organic and the PPC launch becomes a major growth lever.
- **Analysis window:** Last 3 complete months (Jan, Feb, Mar 2026)

## Catalog Overview

GoSun is a solar-powered camping/outdoor cooking brand with 23 parents on Amazon. The catalog spans:
- **Solar cooking (core):** Sport Solar Oven, Fusion, Go Portable Stove, Solar BBQ, Solar Oven Kits
- **Cooling:** Chill cooler, Chillest 12V refrigerator
- **Power:** Foldable solar panels, 100W solar panel
- **Other:** Solar table, water purifier, electric boat, coffee maker, flatware, carrying case

Of 23 parents, only **8 generated any sales** in the last 3 months. The top 4 products = ~87% of revenue.

## Priority Table

| Priority | Product | 3-Mo Sales | Sessions | CVR | Buy Box % | Avg Price | Trend |
|----------|---------|-----------|----------|-----|-----------|-----------|-------|
| **P0** | GoSun Sport Solar Oven (B00KLKJB72) | $8,321 | 4,675 | 1.19% | 98.4% | ~$216 | Mixed, strong Mar surge |
| **P1** | Portable Solar Oven Kit, 1-2 Meals (B0CSWVM2W3) | $7,135 | 4,432 | 3.86% | 90.7% | ~$42 | Growing |
| **P2** | GoSun Go Portable Camping Stove (B07CJP52D6) | $5,413 | 29,771 | 0.18% | 98.6% | ~$119 | Sales growing, CVR catastrophic |
| **P3** | GoSun Fusion Solar Oven (B07WRF6PN4) | $3,312 | 3,346 | 0.41% | 98.9% | ~$356 | Mar-only spike |

**Other notable products (below P3):**
- **Portable Solar Oven Kit duplicate (B0DNRBHHF3):** $1,580 / 3 mo. Identical listing title to P1 (B0CSWVM2W3). Two listings selling the same SKU is splitting traffic and rankings.
- **Solar Oven Portable Stove / Go PRO (B0BRQY4KR4):** $1,299 / 3 mo, declining ($783 → $258 → $258).
- **GoSun Breeze (B0CT5DQCJH):** $790 / 3 mo, tiny but high CVR (4-16%) on very low sessions.
- **Solar Barbecue (B082QF6WG9):** Mostly dormant, $329 in Mar only.
- **Cooling/power/water/boat lines:** All zero or near-zero sales over 3 months despite buy box being available. The catalog has 14+ products that are effectively dead weight on Amazon.

## P0 Annual Trend (B00KLKJB72: Sport Solar Oven)

| Metric | Apr 2025 | Jun 2025 (peak) | Aug 2025 (trough) | Oct 2025 (anomaly) | Feb 2026 | Mar 2026 |
|--------|---------|-----------------|-------------------|---------------------|----------|----------|
| Total Sales | $2,358 | $4,794 | $275 | $1,631 | $1,346 | $4,995 |
| Sessions | 1,340 | 1,814 | 1,268 | 6,589 | 2,534 | 1,084 |
| CVR % | 1.12% | 1.38% | 0.16% | 0.15% | 0.24% | 2.58% |
| Buy Box % | 99.2% | 99.4% | 89.6% | 99.96% | 99.7% | 97.6% |
| Avg Price | $157 | $192 | $138 | $163 | $224 | $178 |

- **Solar season expected pattern is summer-peak, but Jun 2025 was the peak then it cratered in Aug (sales fell 90% to $275, buy box dropped to 89.6%).** Something specific went wrong in August, most likely a stockout or pricing/MAP event combined with a buy box dip. Worth confirming with the seller.
- **CVR has been chronically below 1.5% all year** at AOV $138-$275. The product gets steady traffic (1K-2.5K sessions/mo baseline) but converts poorly. Mar 2026 is the first month above 2% in 12 months, a clear inflection or one-off worth watching.
- **Oct 2025 and Feb 2026 had session spikes (6,589 and 2,534) with collapsing CVR** (0.15% and 0.24%). Pattern is consistent with a low-intent traffic event, likely external referral, viral social moment, or category browsing wave. Sales did not move with the traffic, meaning the product page is not capturing that audience.

## Insights

- **The account is entirely organic.** No ad spend, no ROAS, no PPC infrastructure. Combined with $14K-$18K monthly revenue across 23 parents, this is a textbook low-base-rate account where launching a structured PPC program is the single largest near-term lever.
- **P2 (GoSun Go Portable Camping Stove) is the single biggest CVR unlock in the catalog.** It pulled 29,771 sessions in 3 months at 0.18% blended CVR. Even moving CVR to a category-baseline 2% would multiply units 11x, taking quarterly revenue from $5K to $50K+ on that ASIN alone, before any traffic increase. Why traffic is so high while conversion is so low is the question that drives the rest of the audit.
- **P0 (Sport Solar Oven) and P1 (Portable Solar Oven Kit 1-2 Meals) live in different price tiers and serve different buyers.** P0 is a $178-$248 premium oven; P1 is a $41 entry kit converting at 5%. The catalog effectively has a strong entry-level product (P1) and a strong premium product (P0), but no clear mid-tier merchandising path between them.
- **B0CSWVM2W3 (P1) and B0DNRBHHF3 share the exact same listing title.** They appear to be two listings for the same product. P1 (B0CSWVM2W3) is converting at ~4% with $7K in sales, while B0DNRBHHF3 converts at 1-2% with $1.5K. Combined demand sits across two listings, which fragments reviews, ranking, and ad efficiency. Consolidating or redirecting one to the other is a quick win.
- **14 of 23 parents are effectively dead on Amazon** (zero or near-zero sales over 3 months). The cooler line (B09JB3FBTN, B0BDTBRY4J, B0BN6XH6RH), solar panels (B09WKRTB6M, B0BQ8NWX1B), water purifiers (B08GF2HQVQ, B0BQTFS9TP), tables (B08CM8295B, B0BSNVXBSX), and the boat (B0CKF8L4LT) are all listed but not selling. These are catalog hygiene problems, not growth problems, and not worth focusing the audit on.

## Things to Investigate Further

- **P2 (GoSun Go Portable Camping Stove) traffic-CVR mismatch.** Why is this product getting 10K+ sessions/month at 0.2% CVR? Is the traffic mismatched (irrelevant queries), is the listing broken on conversion (price, image, reviews), or is the product not what searchers want? Step 2 (Product Understanding) and Step 3 (Datadive keyword analysis) should answer this.
- **P0 (Sport Solar Oven) Aug 2025 dip.** Sales fell 90% in one month; buy box dropped from ~99% to 89.6%. Likely a stockout or MAP/pricing event. Check Keepa price/sales rank history to confirm.
- **B0CSWVM2W3 vs B0DNRBHHF3 duplicate listing.** Are these intentional (e.g., different bundles) or a merch/catalog mistake? Compare images, bullets, A+ in Step 2 and decide whether to merge or repurpose one.
- **Feb 2026 traffic spike across the account.** Total sessions hit 20,953 in Feb (highest of the year) but CVR was 0.32%. Was this an external referral, social viral moment, or a price drop on the listing? If we can identify the source, it informs whether to amplify or fix it.

## Questions for the Seller

- "P2 (GoSun Go Portable Camping Stove) gets ~10K Amazon sessions per month but converts at 0.2%. Is this a known issue? Have you seen the same pattern, and have you tried anything to fix it?"
- "Sport Solar Oven sales dropped 90% in August 2025 and the buy box hit 89%. Was that a stockout, a price change, or something else?"
- "Two listings (B0CSWVM2W3 and B0DNRBHHF3) carry the same Portable Solar Oven Kit title. Is this intentional, and which one is the primary?"
- "Is there a reason ads have not been running on Amazon? Budget, prior agency experience, or something else?"
- "There are 14 parent ASINs with effectively zero Amazon sales (coolers, solar panels, water purifiers, tables, boat, accessories). Are these channels we should think about activating, or are they intentionally deprioritized for Amazon?"
