# ASIN Selection - Hardless NG

## Data Readiness Note

Hardless NG has **no business reports connected** (0 periods of Seller Central sales, sessions, CVR, buy box, organic split). This audit is built from the three sources that are available:

- **Advertising data** (Metabase): Feb 15 to May 14, 2026 (89 days)
- **SQP** (Brand Analytics): Oct 2024 to Apr 2026
- **Keepa / product data** (Metabase): full catalog snapshot, rating and rank history

The catalog table below is therefore built from **ad investment + Keepa proxies**, not from business-report sales. Cells that require business reports are marked "No data." This is a teaser-grade audit designed to show the prospect we already understand their account. The business-report layer is what we would connect on the call to size the exact revenue impact.

## Catalog Overview

5 parent ASINs, 9 children. The catalog splits into three product lines plus accessories:

1. **Whole House Water Filter / Salt-Free Conditioner** (parent B0CQ5PB1J4, 5 variants: NG4 and NG4L, 3/4" and 1" inlets). The flagship system. Carries ~99% of all ad spend.
2. **Replacement Cartridges** (B0CRHXXCZT for NG4, 6-month; B0CRHZDQP8 for NG4L, 8-month). The recurring-revenue refills.
3. **Under-Sink Water Filter** (B0CVLB56YJ). A separate drinking-water product. Not advertised.
4. **Metal Filter Mount** (B0FCDRZ9M4). Accessory. Not advertised.

## Priority Table

Ranked by ad investment and strategic role (sales rank by revenue is not available without business reports). 3-month window is the ad window (Feb 15 to May 14, 2026).

| Priority | Product | 3-Mo Ad Spend | Ad Sales | ROAS | Orders | Rating | Sales Rank (subcat) | Notes |
|----------|---------|--------------|----------|------|--------|--------|---------------------|-------|
| P0 | Whole House Water Filter (B0CQ5PB1J4, NG4 / NG4L) | $7,739 | $13,921 | 1.80 | 38 | 4.0 | ~#100-185 in Whole House Water Treatment Systems | The hero system, 99% of ad spend |
| P1 | Replacement Cartridge NG4L (B0CRHZDQP8, 8-mo) | $23 | $1,421 | 62.3 | 9 | 4.1 | No data | Recurring refill, barely advertised, prints at 62x |
| P2 | Replacement Cartridge NG4 (B0CRHXXCZT, 6-mo) | $53 | $1,446 | 27.3 | 9 | 4.4 | No data | Recurring refill, prints at 27x |
| P3 | Under-Sink Water Filter (B0CVLB56YJ) | $0 | $0 | n/a | 0 | 4.6 | No data | Separate drinking-water product, no ads, highest rating |

Business-report columns (Total Sales, Organic Sales, Ad Sales %, Buy Box %, organic CVR, Trend) are **not available** and left out of the table rather than guessed.

**Not prioritized:** Metal Filter Mount (B0FCDRZ9M4). Accessory with no ad spend and no standalone demand. Skip.

## P0 Selection Rationale

P0 is the **Whole House Water Filter (B0CQ5PB1J4)** with no contest:

- It absorbs ~99% of account ad spend ($7,739 of $7,811).
- It is the brand's identity product (the salt-free softener alternative) and the system the cartridges (P1, P2) refill.
- Its sub-category sales rank has been stable and strong (roughly #100 to #185 in Whole House Water Treatment Systems through the ad window), indicating consistent underlying demand.

The cartridges (P1, P2) are strategically important as recurring revenue and show extremely high ROAS on tiny spend, but they are downstream of the system itself. Growing P0 grows the cartridge annuity automatically.

## Observations Carried Forward

- **P0 (Whole House Water Filter) is almost the entire ad story.** Any growth lever found in Steps 3 and 4 should be evaluated against P0 first.
- **P1/P2 (Replacement Cartridges) are under-advertised relative to their ROAS.** 27x to 62x ROAS on under $80 combined spend suggests an untapped, low-risk recurring-revenue lever. Worth a small dedicated campaign once P0 is stabilized.
- **The NG4 (hard water) vs NG4L (extra hard water) variants behave very differently in ads.** The NG4 lines bleed, the NG4L lines convert. This is investigated in Step 4.

## Questions for the Seller

- Business reports are not connected to our system. Connecting Seller Central (or sharing a Business Report export) is the one missing piece. It would let us size exact revenue, organic vs ad split, buy box, and true conversion rate. Is that something you can grant access to before the call?
