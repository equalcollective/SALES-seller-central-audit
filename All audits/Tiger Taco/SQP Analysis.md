# Step 3: SQP Analysis - Tiger Taco Box Clips (P0)

Analysis window: Q1 2026 (Jan 1 - Mar 31, 2026). Annual aggregates also referenced for trend and seasonality where Q1 alone lacks volume.

## Tier Tagging

Tiger Taco is a single-product brand whose name partially defined the search vocabulary. Three meaningful tiers exist:

### Tier 1 (Hero - Direct Category)
Generic, high-intent category descriptors. These are what a first-time buyer who has never heard of Tiger Taco searches.

- box clips
- cardboard box clips
- box clip
- cardboard box clip

### Tier 2 (Functional Description)
The same use-case described differently. Lower volume per query but high relevance.

- box flap holder / box flap holders / cardboard box flap holder / card board box flap holder
- carton flap holder
- box flap clip / box flap clips
- carton clips / carton clip
- box clips for packing
- box holder clip
- packing box flap holder
- cardboard box corner flap holders
- cardboard box flap down clips
- industrial box flap holders
- large box clip
- box carton open clips
- clips to hold box flaps down
- tool meant to hold down box flaps
- cajas de cartón solapas (Spanish)

### Branded
All "tiger taco" name variants AND the "taco" derivative terms that originated from the product. Treated as branded because Tiger Taco coined the terminology, even if competitors now appear there.

- tiger taco / tiger tacos / tiger taco box clips / tiger taco box clip / tiger taco box holder / tiger taco hold boxes open / tiger taxo box clips / tiger paws box clips / b000u5u370 / various long-tail title variants
- taco clip / taco clips / box taco / box tacos / taco box holder / taco box holders / taco box clips / box holder taco / taco box lid holder / taco box flap / taco cardboard box holder / taco holder for boxes / packing taco / plastic tacos to hold boxes / orange tacos box / mivinf tacos

### No Tier 3
Pure broad / adjacent queries ("moving supplies," "moving boxes," "shipping boxes") were excluded. Tiger Taco appears on these but with effectively zero conversion (e.g., "moving boxes" 851K quarterly searches, brand 33 impressions, 0 clicks, 0 purchases). The product genuinely does not match the query intent. There is no growth to capture here.

## Market Sizing (Q1 2026)

| Tier | Q1 Search Volume | Q1 Cart Adds (Market) | Q1 Purchases (Market) | Est. Q1 Market Size ($) | Est. Annual Market Size ($) |
|------|------------------|----------------------|----------------------|------------------------|----------------------------|
| Tier 1 | 1,234 | 89 | 38 | $209 | ~$835 |
| Tier 2 | 625 | n/a (split) | 49 | $270 | ~$1,080 |
| Branded | 761 | n/a (split) | 67 | $369 | ~$1,475 |
| **Total P0** | **2,620** | n/a | **154** | **$847** | **~$3,390** |

*Estimated using $5.50 avg selling price (Q1 2026 actual).*

This is a small absolute market through tagged search funnels. Tiger Taco's $24K annual revenue clearly comes from beyond just these search queries (multi-unit per session, repeat buyers, off-Amazon traffic, untagged search variants). But for the SQP-driven growth thesis, the direct addressable market through tagged queries is approximately $3,400/year. The growth opportunity is large in **percentage terms** but capped in **absolute dollar terms** by the niche size.

## Brand Performance vs Industry (Q1 2026, Aggregated by Tier)

| Tier | Brand Impr Share | Brand CTR | Industry CTR | Brand ATC Rate | Industry ATC Rate | Brand CVR | Industry CVR | Brand Purchase Share |
|------|-----------------|-----------|--------------|----------------|-------------------|-----------|--------------|---------------------|
| Tier 1 | 2.4% | 8.9% | 1.1% | 32.1% | 23.3% | 12.8% | 9.9% | 26% |
| Tier 2 | 2.8% | 22.8% | 2.2% | varies | varies | 28.7% | 14.0% | 59% |
| Branded | 3.3% | varies (4-100%) | varies | varies | varies | varies | varies | high on direct brand |

## Catalog Overlap Check

Tiger Taco has only one product on Amazon. The adjusted impression share cap is the standard **~8-9% per tier** (single product, no halo from sibling SKUs).

## Blockers and Growth Path

| Tier | Brand Impr Share | Brand vs Industry CTR | Brand vs Industry CVR | Primary Blocker | Growth Path |
|------|------------------|----------------------|----------------------|-----------------|-------------|
| Tier 1 | 2.4% (cap ~8-9%) | 9x industry | 1.3x industry | **Impression Share** | Bid on the 4 Tier 1 keywords. CTR and CVR are both ahead of industry, the brand wins when shown. |
| Tier 2 | 2.8% (cap ~8-9%) | 10x industry | 2x industry | **Impression Share** | Bid on the top 4-6 Tier 2 keywords. Best ROAS opportunity, brand dominates conversion. |
| Branded | 3.3% (cap ~8-9%) | very high on direct brand, lower on "taco" derivatives | very high | **Impression Share + Defense** | Run a small branded defense campaign + Sponsored Brands header to dominate the brand-name SERP. |

Across all three tiers, **the primary blocker is identical: impression share is well below the cap, and the funnel from impression to purchase is healthy enough that more impressions will translate directly into more sales.** Tiger Taco doesn't have a CTR problem or a CVR problem on its core queries. It has a "we don't show up" problem, which is the easiest type of blocker to fix because PPC can solve it deterministically.

### Statistical Significance Check

- Tier 1 Q1: 78 brand clicks, 10 brand purchases. Above the 20-click threshold for CVR analysis. Confident in CVR comparison.
- Tier 2 Q1: 101 brand clicks, 29 brand purchases. Comfortably significant.
- Branded Q1: 226 brand clicks, 67 brand purchases. Very significant.

All three tiers have enough volume in Q1 alone to support the conclusions. No need to fall back to annual aggregation.

### Year-Over-Year Search Volume on the Hero Query

"box clips" quarterly search volume:
- Q2 2025 (Apr-Jun): 443
- Q3 2025: not available with brand purchases (low volume)
- Q4 2025: 709
- Q1 2026: 801

Search demand on the hero query is **growing year-over-year (~80% from Q2 2025 to Q1 2026)**. Whether this is true demand growth or a seasonal pattern (moving / packing peaks in summer for the moving season and around holidays for shipping) cannot be confirmed without 2-year history. The 12-month trend is the only horizon available.

## ICAP Funnel - Tier 1 (Hero, Highest-Growth Tier)

```
graph TD
    A["🔍 Impressions
    Brand IS: 2.4% (of ~8-9% max)
    ⚠️ PRIMARY BLOCKER"] --> B["👆 Clicks
    Brand CTR: 8.9% vs 1.1% industry
    ✅ 9x above industry"]
    B --> C["🛒 Add to Cart
    Brand ATC: 32.1% vs 23.3% industry
    ✅ 1.4x above industry"]
    C --> D["💰 Purchases
    Brand CVR: 12.8% vs 9.9% industry
    ✅ Above industry"]

    style A fill:#ff6b6b,color:#fff
    style B fill:#51cf66,color:#fff
    style C fill:#51cf66,color:#fff
    style D fill:#51cf66,color:#fff
```

The funnel below impressions is healthy at every stage. Tier 1 only needs more visibility.

## SQP Observations

- **The brand owns conversion in its niche but loses the visibility battle.** On Tier 1, brand purchase share is 26% with only 2.4% impression share, meaning the brand wins the click and the cart way more than its visibility justifies. This is the cleanest "fix the top of the funnel" pattern in the workflow.
- **"Taco" terminology has been semi-genericized.** Queries that originated from this brand (taco clip, box taco, etc.) now show competitor products. The brand has no ad defense running, so even on its own coined terms competitors capture some traffic. Branded defense is needed before scaling non-brand campaigns.
- **Keyword search alone has a small ceiling.** All tagged tiers combined represent ~10,500 annual searches, ~616 annual market purchases. Even at full impression share capture, incremental revenue from keyword targeting is ~$2-3K/year. The bigger growth lever is upstream of search.

## Product Targeting Opportunity (Non-Keyword Lever)

Keyword targeting on broad queries like "moving boxes" (851K quarterly), "moving supplies" (466K), "shipping boxes" (352K), "cardboard boxes" (118K) does not work for this product. The shopper typing those queries wants the box itself, not an accessory clip. Industry CVR on those queries when Tiger Taco appears is 0%.

But these same shoppers, once they land on a moving-box or packing-supply PDP, are in active packing-or-moving mode, which is exactly when a box flap clip becomes a logical add-on. **The play is product targeting (PAT and Sponsored Display) on adjacent product detail pages, not keyword targeting on adjacent search queries.**

Targets to bid on:
- Top-selling moving box ASINs (small/medium/large variants)
- Top-selling packing tape and dispenser ASINs
- Top-selling bubble wrap and packing paper ASINs
- Top-selling moving labels and markers
- Top-selling shipping/storage box ASINs
- Box cutter and packing knife ASINs
- Moving supply kits / bundles
- Shrink wrap

Why this works where keyword targeting doesn't:
- The shopper has already committed to the project (they are buying boxes, tape, etc.)
- Tiger Taco is a complementary purchase, not a substitute
- The PDP placement is a "people also bought" or sponsored-related-products surface where complementary accessories convert at meaningfully higher rates than generic search ads
- Each placement is competing against other accessories, not against actual boxes (which is what made keyword targeting fail)

The addressable market through product targeting is an order of magnitude larger than keyword targeting because the upstream box / tape / supply market is in the millions of monthly purchases, and Tiger Taco only needs a small attach rate to materially grow.

This is the primary non-branded growth lever for Tiger Taco. Keyword search captures the existing intent-to-buy-flap-clips; product targeting creates the intent.
