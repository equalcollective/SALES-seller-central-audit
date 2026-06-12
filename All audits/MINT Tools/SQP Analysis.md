# SQP Analysis - P0 Curling Irons (B07RM2VQ77)

Period: March 2026 (most recent full month). Cross-checked against Jan-Feb 2026 for trend.

## Tier Tagging

55 curling-iron-relevant queries tagged across three tiers. Branded competitor queries (T3, Hot Tools, Bio Ionic, Beach Waver, Conair, BabylissPRO, GHD, Chi, Tyme, Revlon) are excluded from MINT's growth analysis since their searchers are buying those brands. Wand-only queries excluded (different product, P2). MINT's own branded queries are tracked separately.

### Tier 1 (Hero - Long-Barrel + Sized): 24 queries

Why: MINT's positioning is "Extra Long Hair Curling Iron" in 1, 1.25, 1.5 inch sizes. These queries match exactly. Includes "long barrel curling iron" variants and sized queries (1.5", 1.25", 1").

Examples: long barrel curling iron (17K), curling iron 1 1/2 inch (43K), 1.5 inch curling iron (29K), 1 1/4 inch curling iron (10K), large barrel curling iron (16K), curling iron for long hair (5.3K).

Total Tier 1 search volume: **301,372/month**.

### Tier 2 (Core market - Generic curling iron): 8 queries

Why: Head term "curling iron" plus its close synonyms. High volume, broad intent. MINT competes here against the entire category.

Examples: curling iron (527K), curling irons (19K), ceramic curling iron (8.2K), dual voltage curling iron (12K), best curling iron (4.6K), titanium curling iron (2.8K).

Total Tier 2 search volume: **588,104/month** (mostly the head term).

### Tier 3 (Adjacent - Wrong size or wave style): 14 queries

Why: Customer intent is curling-related but doesn't match MINT's SKU lineup (e.g., 2-inch barrel which MINT doesn't sell, or 1/2-inch and 3/4-inch variants).

Examples: 2 inch curling iron (43K), 1/2 inch curling iron (16K), 3/4 inch curling iron (14K), wave curling iron (13K), marcel curling iron (7.5K).

Total Tier 3 search volume: **147,247/month**.

### Branded (informational, separate)

MINT branded queries are small-volume but high-share. "mint curling iron" gets 340 monthly searches with MINT capturing ~55% impression share. Total MINT-branded curling iron volume is under 500/month - branded recognition for the curling iron is modest. Compare to "mint s waver" (waver product) at 1,811/month with 86% MINT purchase share - the waver has built much stronger brand equity than the iron.

## Market Sizing (March 2026)

| Tier | Monthly Search Volume | Monthly Total Clicks | Monthly Total Add-to-Carts | Monthly Total Purchases | Est. Market Size at $100 ASP |
|------|----------------------|----------------------|----------------------------|-------------------------|-------------------------------|
| Tier 1 | 301,372 | 141,649 | 52,323 | **18,555** | **$1.86M / month** |
| Tier 2 | 588,104 | 236,264 | 71,917 | 20,047 | $2.00M / month |
| Tier 3 | 147,247 | 72,298 | 25,948 | 8,549 | $855K / month |
| **Total addressable** | **1,036,723** | **450,211** | **150,188** | **47,151** | **$4.72M / month** |

*ASP estimated at $100 based on competitive landscape (MINT $89-105, market mid-tier $80-130).*

The Tier 1 market alone is **~$22M/year** and MINT has captured roughly $1.2M annual run-rate of it. The brand has sub-1% share of the market that most directly fits its product positioning.

## Blockers & Growth Path

| Tier | Brand Impression Share | Brand CTR vs Industry | Brand CVR vs Industry | Primary Blocker | Growth Path |
|------|------------------------|----------------------|----------------------|-----------------|-------------|
| Tier 1 | **0.76%** (vs ~30% multi-product cap) | 0.72% vs 1.90% (38% of industry) | 3.71% vs 13.10% (**28% of industry**) | **Impression Share + CVR (stacked)** | Fix CVR (buy box + listing) FIRST, then scale impressions |
| Tier 2 | 0.11% (vs ~16% cap) | 1.02% vs 1.67% (61% of industry) | 0.65% vs 8.48% (**8% of industry**) | CVR catastrophic | De-prioritize. Head term "curling iron" doesn't convert at this brand tier |
| Tier 3 | 0.27% (vs ~16% cap) | 0.70% vs 2.06% (34% of industry) | 2.99% vs 11.82% (25% of industry) | Wrong-fit (no 2-inch SKU) | De-prioritize. Largest queries are sizes MINT doesn't sell |

### Why Tier 1 has stacked blockers

**MINT has 6 ASINs that can rank on Tier 1 queries** (3 sizes × 2 generations: original + REVAMP). Per the catalog overlap rule, the impression share cap on Tier 1 is roughly 30-50% (cap of ~8-9% per product, scaled by number of ranking products). MINT is at 0.76% - sub-3% of their realistic ceiling.

Even more telling: when MINT does show up in Tier 1 impressions, **CTR is 38% of industry and CVR is 28% of industry**. So the brand is failing at all three funnel stages simultaneously. This is not "barely showing up" - this is "barely showing up AND not converting when we do."

Per the [CLAUDE.md](../../CLAUDE.md) ICAP framework: "Low impression share + poor CVR. Before scaling impressions, CVR must be addressed first, because this is a pay-per-click model: more clicks with poor conversion just burns money."

### Why CVR is below industry

Two factors:
1. **Buy box at 74% on the original parent.** Per Step 1, the August 2025 price increase from $89 to $109.97 likely triggered Amazon's MAP suppression. 25% of clicks land on a degraded buy box experience (out of stock or competitor offer shown). This alone explains a CVR gap of roughly 25-30%.
2. **Mid-tier price + 4.3 rating in a category where premium players have 4.5+ ratings.** When the buy box appears, MINT competes against T3/GHD/Bio Ionic etc. on the search page. The price is fine but the rating is a visible-at-glance gap.

The first factor is the immediate fix. Once buy box is recovered, expected CVR lift = +30-40% (back from 3.71% toward industry 13.10%, though full closure of the gap isn't realistic since there's also a price/rating component).

## ICAP Funnel - Tier 1 (March 2026)

```
graph TD
    A["🔍 Impressions
    Share: 0.76% (of ~30% multi-product max)
    ⚠️ PRIMARY BLOCKER (Long-term)"] --> B["👆 Clicks
    Brand CTR: 0.72% vs 1.90% industry
    ⚠️ Below industry (38%)"]
    B --> C["🛒 Add to Cart
    Brand ATC Rate: 19.8% vs 36.9% industry
    ⚠️ Below industry (53%)"]
    C --> D["💰 Purchases
    Brand CVR: 3.71% vs 13.10% industry
    ⚠️ PRIMARY BLOCKER (Immediate fix)"]

    style A fill:#ff6b6b,color:#fff
    style B fill:#ffd43b,color:#000
    style C fill:#ffd43b,color:#000
    style D fill:#ff6b6b,color:#fff
```

The funnel has two red flags. Impression share is the long-term ceiling (massive headroom from 0.76% toward 30%+) but CVR must be fixed first because scaling impressions while CVR is at 28% of industry will burn ad spend at sub-2x ROAS (which is exactly what's happening - see Ad Analysis).

## Notable observations

- **MINT is winning the "long barrel" niche.** "long barrel curling iron 1.5 inch" shows 3.61% impression share, "long barrel curling iron 1.25" shows 2.35% - the highest shares in MINT's entire SQP footprint. The brand owns this micro-niche, which validates the product positioning ("Extra Long Barrel"). The growth question is how big this niche can get; it's currently ~17K monthly searches for the head term but 30K+ if you include sized variants.
- **MINT is poaching from Bio Ionic queries.** "bio ionic long barrel curling iron 1.25" - a query that is technically a Bio Ionic branded search - shows MINT capturing 2.30% impression share. This means Amazon is showing MINT as a relevant alternative to Bio Ionic shoppers, validating that MINT can compete with the premium brand on long-barrel intent.
- **Branded share is improving Q1 2026.** Tier 1 brand impression share grew from 0.55% (Jan) to 0.76% (Mar), a +38% lift, driven by ad spend ramp. CVR did NOT improve in the same period (3.65% → 3.71%) - confirming that the ad-driven impressions aren't being captured because of the buy box issue.

## Insights

- **Tier 1 is a $22M annual market and MINT has <1% share.** Their product literally fits the niche better than any competitor (long barrel + 1/1.25/1.5 inch sizes), but they're stuck at <1% because clicks aren't converting. Fix the conversion problem and the impression-share unlock will follow naturally with ad spend.
- **The waver (P1) has stronger brand equity than the curling iron.** "mint s waver" gets 5.3x the search volume of "mint curling iron" and MINT captures 86% of those purchases. The brand could borrow waver-style marketing energy (visual, viral) to lift the iron's CTR.

## Things to Investigate

- **Why is industry CVR on Tier 1 so high (13%)?** Industry CVR of 13% on long-barrel/sized curling iron queries is unusually high - the broader Tier 2 head term "curling iron" runs at 8.5%. This suggests Tier 1 queries are higher-intent (people search for sized irons because they know what they want). MINT's 3.71% on Tier 1 is therefore even more under-indexed than it looks. Worth confirming on a 6-month rolling window to ensure not seasonal.
- **Why isn't the REVAMP curling iron capturing more of MINT's branded search?** "mint curling iron" has 340 monthly searches; the REVAMP got 0 of those purchases per the parent breakdown in Step 1. Either branded shoppers are landing on the original SKU (no awareness of the REVAMP), or the REVAMP isn't appearing for the brand's own name yet.

## Questions for the Seller

(Buy box question moved to ASIN Selection - it's the same root question.)

- The brand has 6 ASINs that could rank on long-barrel curling iron queries (3 sizes × 2 generations) but is at 0.76% impression share. Is the goal to phase out the original parent in favor of the 2026 REVAMP, or keep both indefinitely? The answer changes the SEO and PPC strategy materially.
