# Step 1: ASIN Selection - Periodic Audio

## Data Readiness

- **Business data:** Available Jul 2024 to May 2026 (monthly, plus recent weekly). Good coverage.
- **Ad data:** None. `ads_day_count = 0` in Seller Analytics, and Metabase Q698 (full multi-year campaign history) is empty across ENABLED, PAUSED, and ARCHIVED. Periodic Audio has no record of ever running Amazon PPC. Confirmed with Aryan: they are not running ads. All ad-dependent columns below are N/A and sales are 100% organic.
- **Selection window:** Last 3 complete months (Mar to May 2026), consistent with the workflow. Since there is no ad data, the window is driven by business data only.

## Catalog

Periodic Audio has only 3 ASINs in this Amazon account, each a single-child parent. The account is effectively a single live product.

| Priority | Product | ASIN | 3-Mo Sales (Mar-May 26) | Ad Spend | ROAS / TACoS | Organic Sales | Ad Sales % | Buy Box % (child) | CVR | Trend |
|----------|---------|------|------|------|------|------|------|------|------|------|
| P0 | Rhodium USB-C DAC/Amp | B0929D9T57 | $833 (17 units) | $0 | N/A | $833 (100%) | 0% | 94-96% | ~4.4% | Flat, down YoY |
| P1 | Neon Bluetooth 5.2 Receiver | B0CDNZJ6MH | $0 (0 units) | $0 | N/A | $0 | 0% | 94-100% | 0% | Dormant |
| P2 | (unnamed accessory) | B0CDFN278W | $0 | $0 | N/A | $0 | 0% | N/A | N/A | Dead |

No P3 (only 3 ASINs exist).

**Notes on non-prioritized products:**
- **P1 (Neon BT Receiver):** Priced $59. Sells in small bursts (last sales were Oct-Dec 2025, ~1-2 units/mo; zero in 2026 so far). ~15-28 sessions/mo with near-zero conversion. Real product but commercially dormant on Amazon.
- **P2 (B0CDFN278W):** Priced ~$9.95. One unit ever sold (Dec 2024). No Keepa product snapshot exists for it (no title/brand ingested). Effectively dead.

**Buy box note:** The parent/account-level "total" buy box reads ~63-66%, but that is the FBM-aggregation dilution artifact, not a real issue. At the child level the Rhodium holds 94-98% buy box. Buy box is healthy and is not a constraint.

## P0 Selection

P0 is unambiguously the **Rhodium USB-C DAC/Amp (B0929D9T57)**. It is the only product with meaningful, consistent sales (roughly 99% of account revenue) and the only one with a complete product record.

## P0 Annual Trend (Rhodium DAC)

| Metric | Jul 2025 | Dec 2025 | Mar 2026 | May 2026 |
|--------|----------|----------|----------|----------|
| Total Sales | $196 | $686 | $196 | $343 |
| Sessions | 244 | 226 | 136 | 128 |
| CVR | 1.6% | 6.2% | 2.9% | 5.5% |
| Buy Box % (child) | 93% | 97% | 95% | 96% |

- **Trajectory:** Revenue bounces in a $100-700/mo band with a clear December holiday peak. The product is not growing; it is coasting. Trailing 12-month account sales are about $4,200 (~$346/mo).
- **Sessions are declining.** Traffic has roughly halved over the year, from ~240-300 sessions/mo in mid-2025 to ~128-145/mo now. Sales held up only because CVR and price stayed steady, masking a real and ongoing loss of visibility.
- **CVR is low and volatile (2-6%)** on a $49 audiophile accessory, consistent with thin, mostly branded traffic and a 4.0-star rating.

## Insights

- P0 (Rhodium DAC) is essentially the entire business on Amazon. The other two ASINs are dormant or dead, so all growth analysis focuses on the Rhodium.
- Declining sessions on a flat-revenue product point to an eroding top of funnel, not a conversion or pricing event. This is the thread to pull in SQP.

## Questions for the Seller

- The brand's core catalog (the element-named IEMs, plus other DACs like Nickel and BlueDAC) is not on this Amazon account, only 3 accessory SKUs are. Are those sold through a different channel, discontinued, or is there an opportunity to bring the full line to Amazon? This is the single biggest growth question for the account.
- Sessions have roughly halved over 12 months while price held at $49. Is this a deliberate pullback (focusing on the DTC site) or unmanaged decay?
