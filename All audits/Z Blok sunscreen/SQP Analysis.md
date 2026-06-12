# SQP Analysis - P0 (Z Blok Lip Balm & SPF 30 Sunscreen)

## Tagging Rationale

- **Tier 1 (Hero):** Direct SPF-lip-balm intent. Queries where the customer is explicitly searching for a lip balm with SPF, and the product is the literal answer to the search. Queries: `spf lip balm`, `lip balm spf`, `lip sunscreen`, `sunscreen lip balm`.
- **Tier 2 (Competitor conquest):** Customers searching by competitor brand in the SPF-lip-balm space who would buy Z Blok if they saw it. Only one high-volume query of this type in the data: `sun bum lip balm` (Sun Bum is the mainstream SPF lip balm leader).
- **Tier 3 (Broad/adjacent):** The mass-market `lip balm` query. Z Blok can show but most searchers do not want SPF specifically. Included to size the adjacent demand, not as a primary growth target.
- **Branded:** `z blok`, `z blok lip balm`. Used for sizing brand equity, not as a growth lever per CLAUDE.md branded-keyword principle.

**Note on excluded queries:** The broader sunscreen queries (`sunscreen`, `mineral sunscreen`, `zinc oxide sunscreen`, `sunscreen stick`, etc.) are not P0-relevant because P0 is a lip balm, not a body/face sunscreen. Those queries are relevant to the other ASINs in the Z Blok catalog (P1, P2, P3) and should be tagged separately when those products are audited.

### Catalog Overlap Check

P0 is the only Z Blok product that is a lip balm. The other three parents (4 oz Sunscreen, Stick Sunscreen, 2 oz Sunscreen) are body/face sunscreens and would not rank for the Tier 1 lip-specific queries. Impression share cap stays at **~8-9% (1 product ranking)** across all three tiers. No adjustment needed.

## Market Sizing (12 months, Apr 2025 - Mar 2026)

| Tier | Monthly Search Volume | Monthly Add to Carts (Market) | Monthly Purchases (Market) | Est. Market Size ($/mo) |
|------|----------------------|-------------------------------|---------------------------|------------------------|
| Tier 1 | 112,934 | 28,466 | 11,365 | ~$227,700 |
| Tier 2 | 17,783 | 5,241 | 2,292 | ~$26,200 |
| Tier 3 | 581,778 | 96,142 | 34,459 | ~$480,700 |
| **Total P0-relevant** | **712,495** | **129,849** | **48,116** | **~$734,600** |

*Estimated using $8 for Tier 1 (SPF lip balm avg), $5 for Tier 2 (Sun Bum is ~$4-5), $5 for Tier 3 (broad lip balm mix). Z Blok's own 3-pack is $12.80 at $4.27/stick.*

**Seasonality:** Tier 1 search volume peaks June-July at ~210K/mo and troughs November-December at ~60K/mo. That is a 3.5x swing. The seller's own P0 revenue cycle (Jul 2025 peak $13.2K, Nov 2025 trough $4.2K, also a 3.1x swing) matches this SQP pattern almost exactly. This confirms Z Blok's revenue swings are market-demand driven, not brand-specific. The business is entering the recovery phase of the cycle now (Mar 2026 Tier 1 search volume 137K, up from 58K in Dec), and peak summer is 3 months away.

## Market Share and Potential (3 months, Jan-Mar 2026)

| Tier | Impression Share | Click Share | Cart Share | Purchase Share | Trend |
|------|-----------------|-------------|------------|----------------|-------|
| Tier 1 | 0.34% | 0.14% | 0.05% | 0.06% | Flat, share declining as market grows |
| Tier 2 | 0.06% (Feb only) | 0% | 0% | 0% | Negligible |
| Tier 3 | 0.003% | 0.005% | 0.006% | 0.009% | Flat, negligible |

Against the ~8-9% impression-share ceiling for a single product ranking, Z Blok is capturing roughly **4% of its theoretical maximum on Tier 1** (0.34% / 8% cap). On Tier 2 and Tier 3, share is effectively zero.

On Tier 1 specifically, Z Blok's impression share *declined* Jan (0.43%) > Feb (0.35%) > Mar (0.29%) even though total market volume grew sharply. Competitors are absorbing the seasonal volume increase while Z Blok is not.

## Blockers & Growth Path

| Tier | Impression Share | CTR (Brand vs Industry) | CVR (Brand vs Industry) | Primary Blocker | Growth Path |
|------|-----------------|------------------------|------------------------|-----------------|-------------|
| Tier 1 | 0.34% of ~8-9% max (Blocker) | 1.07% vs 2.69% (Blocker) | 6.87% vs 15.22% (Blocker) | **Impression Share + CTR + ATC** | Fix listing first (CTR + ATC levers), then scale PPC for impression share |
| Tier 2 | 0.06% (Blocker, data thin) | Insufficient data | Insufficient data | Impression Share (low priority) | Small competitor-conquest campaign after Tier 1 is unlocked |
| Tier 3 | 0.003% | N/A (intent mismatch) | N/A | Intent mismatch (broad lip balm intent, not SPF) | Do not pursue at scale. Skip. |

**Tier 1 detail:**

The funnel is broken at every stage, and each stage maps to a separate fix.

- **Impression share (0.34% vs ~8-9% cap):** Z Blok shows up in only 1 of every ~300 search results for SPF lip balm queries. Below the 3% "low impression share" threshold by a factor of ~10. The ceiling is effectively untouched.
- **CTR (1.07% vs industry 2.69%, 60% below industry):** Of the rare times Z Blok does show up, searchers click at less than half the industry rate. This is a search-results-card problem: main image, title, price, star rating, reviews, coupon.
- **ATC rate (14.5% vs industry 37.9%, 62% below industry):** Of the rare clicks that do happen, only 1 in 7 adds to cart vs 1 in 3 for the industry. This is a product-detail-page problem: bullets (empty), A+ (absent), video (absent), images (3 total, 1 is unrelated stock art).
- **Cart-to-Purchase (47.4% vs industry 40.2%):** This is the one stage Z Blok is **above** industry. When a shopper actually makes it to the cart, they complete the purchase more reliably than the benchmark. The brand, rating, and price are doing their job once the shopper has committed.

**Interpretation:** This is the "Low impression share + poor CVR + fixable listing" pattern from CLAUDE.md. The listing gaps identified in Step 2 (no bullets, no A+, no video, 34-char title, 3 images) are the direct cause of the CTR and ATC gaps. The sequence must be listing fixes first, because scaling PPC on a leaky funnel is paying for clicks at 15% ATC instead of 38% ATC. Once the listing is fixed and the funnel tightens up, the impression-share opportunity is enormous. With 97% of the Tier 1 ceiling untouched, even a 2x gain on impression share (from 0.34% to 0.7%) plus listing-driven improvements in CTR and ATC could materially scale revenue into the summer peak.

## Insights

- P0 (Lip Balm & SPF 30) is operating at roughly 4% of its Tier 1 impression-share ceiling. The Tier 1 market is 28,466 cart adds and 11,365 purchases per month, $227K in monthly market size, and Z Blok is capturing ~7 purchases of that per month. The gap is the opportunity.
- Z Blok's seasonality is real and market-driven, not brand-specific. SQP Tier 1 search volume follows the same June-peak, December-trough cycle as the seller's own revenue. We are currently 2-3 months away from peak, which is the best possible timing window for listing and PPC fixes to land before demand rises.
- The one funnel stage where Z Blok beats industry is cart-to-purchase (47% vs 40%). That tells us the product itself converts when it is properly surfaced. The problem is not product-market fit; it is visibility and listing presentation.

## Things to Investigate Further

- In Step 4 ad analysis, check whether the Februarylipbalm campaign is bidding on the Tier 1 queries (`spf lip balm`, `lip sunscreen`, etc.) and at what spend. If yes, the bid levels are the reason impression share is not moving. If no, that is the most obvious PPC lever.

## Questions for the Seller

- None from this step. Everything is answerable from the data and the next-step tools.
