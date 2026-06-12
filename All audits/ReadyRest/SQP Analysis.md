# SQP Analysis: ReadyRest

Brand in SQP Analyzer: `RR READYREST`. Single-product catalog (no catalog overlap across tiers, so the impression share cap stays at the default ~8-9% per tier).

## Tagging Rationale

22 queries tagged across 4 tiers. Tier definitions:

- **Tier 1 (Hero):** Queries where the customer is searching for exactly the product type the brand sells. Just 1 query qualifies: "shotgun rest". Low absolute volume but extremely high intent. The product is the direct answer.
- **Tier 2 (Core market):** Use-case accessory queries where a shotgun rest is one of several items shoppers might buy in this trip. 11 queries: pheasant/upland/dove/bird hunting gear & accessories, trap/skeet/sporting clays accessories, shotgun accessories, shotgun holster.
- **Tier 3 (Broad/adjacent):** Use-case general queries. 4 queries: pheasant hunting, upland hunting, dove hunting, quail hunting. Shoppers are researching the activity, not necessarily ready to buy gear.
- **Branded:** 6 queries on the brand name itself ("ready rest", "readyrest", "ready rest shotgun rest", etc.). These are existing customers and brand-aware shoppers, not a growth lever.

The high-volume "shooting rest", "shotgun sling", "shotgun shell holder" queries (30K+ volume each) were deliberately NOT tagged - they sound relevant but are intent-mismatched. "Shooting rest" mostly means rifle bench rest. "Shotgun sling" is a carry strap. "Shotgun shell holder" is for ammo. Targeting these would burn impressions on shoppers looking for unrelated products.

## Market Sizing

12-month window (Apr 2025 - Mar 2026), monthly averages.

| Tier | Monthly Search Volume | Monthly Add to Carts (Market) | Monthly Purchases (Market) | Est. Market Size ($/mo) |
|------|----------------------|-------------------------------|---------------------------|------------------------|
| Tier 1 (shotgun rest) | 190 | 11 | 4 | $440 |
| Tier 2 (Core market) | 43,080 | 2,724 | 433 | $108,960 |
| Tier 3 (Broad/adjacent) | 9,881 | 494 | 75 | $19,760 |
| Branded | 165 | 35 | 17 | $1,400 |
| **Total addressable (T1+T2+T3)** | **53,151** | **3,229** | **512** | **$129,160** |

*Estimated using $40 average product price across this category (ReadyRest at $59.99, AVAONE budget alternatives lower, leather barrel rests $15-25). The $40 represents the volume-weighted average across the cart-adds happening in these tiers, which include both rest-type products and adjacent accessories.*

**Seasonality confirmed.** Tier 2 search volume goes from 26-30K/mo in Apr-Jun (off-season) to 64-68K/mo in Aug-Sep (pre-hunting-season research) and a second 65K peak in Dec (holiday gifting). Tier 3 is even more extreme: 1.4K-3.5K in shoulder months, 33K in Aug. This matches the seller's own revenue pattern from Step 1 (Aug build-up, Oct-Dec peak, Jan-Mar trough), which confirms the seasonality is market-driven, not brand-specific.

## Market Share and Potential

3-month window (Jan-Mar 2026). Volume-weighted across the 3 months.

| Tier | Impression Share | Click Share | Cart Share | Purchase Share | Trend |
|------|-----------------|-------------|------------|---------------|-------|
| Tier 1 | 2.45% (of ~8-9% max) | 10.4% | 10.0% | 11.1% | Stable, ~2.2-2.7% all year |
| Tier 2 | 0.33% | 0.45% | 0.25% | 0.09% | Stable, ~0.3-0.5% all year |
| Tier 3 | 0.38% | 0.48% | 1.09% | 0% | Stable but tiny |

**Note on Q1 statistical significance:** Q1 is the seasonal trough. Tier 1 has only 15 brand clicks across the whole quarter; Tier 2 had 1 brand purchase in 3 months; Tier 3 had 0 purchases. Recent-window rates are noisy. The 12-month aggregates below (used for blocker detection) are more reliable.

**12-month aggregated rates (Apr 2025 - Mar 2026):**

| Tier | Brand Imp Share | Brand CTR | Industry CTR | Brand ATC Rate | Industry ATC Rate | Brand CVR | Industry CVR |
|------|-----------------|-----------|--------------|----------------|------------------|-----------|--------------|
| Tier 1 | 2.48% | 6.23% | 1.22% | 20.9% | 20.2% | 6.98% | 6.49% |
| Tier 2 | 0.45% | 2.28% | 1.24% | 12.7% | 18.99% | 1.60% | 3.21% |
| Tier 3 | 0.68% | 2.25% | 0.95% | 17.2% | 16.2% | 0.88% | 3.22% |

The story is the same in all three tiers: when the brand shows up, shoppers click on it more than industry average (above-industry CTR everywhere). The differences are downstream:
- **Tier 1:** ATC rate and CVR are also above industry. The listing converts well when shoppers find it.
- **Tier 2:** ATC rate is 33% below industry; CVR is 50% below. Shoppers click but don't add to cart, suggesting an intent-mismatch (they were looking for a vest, glasses, or shells, not a rest).
- **Tier 3:** ATC rate is healthy but CVR is 73% below industry. Same intent-mismatch in the cart-to-purchase stage.

## Blockers & Growth Path

| Tier | Impression Share | CTR (Brand vs Industry) | CVR (Brand vs Industry) | Primary Blocker | Growth Path |
|------|-----------------|-------------------------|------------------------|-----------------|-------------|
| Tier 1 | 2.48% (of ~8-9% max) - Blocker | 6.23% vs 1.22% - Healthy | 6.98% vs 6.49% - Healthy | **Impression Share** | PPC scaling on "shotgun rest". Listing converts above industry at every funnel stage; just needs visibility. |
| Tier 2 | 0.45% - Blocker | 2.28% vs 1.24% - Healthy | 1.60% vs 3.21% - Below | **Impression Share** | PPC test across the full Tier 2 keyword set. Prune underperformers based on early ACoS data, do not exclude categories upfront. |
| Tier 3 | 0.68% - Blocker | 2.25% vs 0.95% - Healthy | 0.88% vs 3.22% - Below | **Intent mismatch** | Not capturable efficiently. Shoppers are researching activities, not buying gear. Skip in initial PPC scaling. |

**Tier 1 detail:** This is a textbook "low impression share + healthy CVR" pattern (per CLAUDE.md Domain Knowledge). The brand has 2.48% of a ~8-9% cap, meaning there is room for 3-4x growth on this query alone. Above-industry CTR/ATC/CVR confirms the listing converts when shoppers find it. The fastest path to revenue: bid on "shotgun rest" via Sponsored Products and Sponsored Brands, climb toward the 8-9% cap. Volume is small (190 searches/mo), so this isn't the largest dollar opportunity, but it is the highest-leverage one - every impression added converts.

**Tier 2 detail:** Bigger market ($109K/mo) and proven brand traction across multiple keywords annually. The volume-weighted CVR is below industry, but that average is across queries with varying intent and gets dragged down by traffic on tail queries. Looking at brand cart-adds and purchases per query over the full 12 months tells a more useful story: shotgun holster (43 cart-adds, 14 purchases - the second-highest converter after Tier 1), upland hunting gear (31 cart-adds), dove hunting gear (29), skeet shooting accessories (26), bird hunting accessories (19). These are real conversions, not noise.

Recommended approach: launch PPC across the full Tier 2 keyword set with conservative initial bids and tight ACoS gates (pause anything above 40% by end of Week 4). Let early data, not category semantics, decide which keywords to scale.

**Tier 3 detail:** The CVR gap is too large and the queries are too research-oriented to be a viable PPC target. Even with the listing's strong organic conversion, broad activity-level queries don't filter for buyers. If budget remains after Tier 1 and Tier 2 are saturated, this could be a Sponsored Display interest-targeting candidate - but not Sponsored Products on the keyword itself.

## ICAP Funnel - Tier 1 (Primary Growth Tier)

```
graph TD
    A["🔍 Impressions
    Brand share: 2.48% (of ~8-9% max)
    ⚠️ PRIMARY BLOCKER"] --> B["👆 Clicks
    Brand CTR: 6.23% vs 1.22% industry
    ✅ Above industry (5x)"]
    B --> C["🛒 Add to Cart
    Brand ATC: 20.9% vs 20.2% industry
    ✅ Healthy"]
    C --> D["💰 Purchases
    Brand CVR: 6.98% vs 6.49% industry
    ✅ Above industry"]

    style A fill:#ff6b6b,color:#fff
    style B fill:#51cf66,color:#fff
    style C fill:#51cf66,color:#fff
    style D fill:#51cf66,color:#fff
```

The funnel is healthy at every stage *after* the impression. The only thing stopping growth is showing up. With zero ad spend today (Step 1), even modest PPC investment on this single keyword should produce visible results.

## Insights

- P0 (ReadyRest Shotgun Rest) is the textbook "PPC scaling" case on its hero query. 12-month brand CTR is 5x industry, ATC and CVR are above industry, but impression share is locked at 2.5% with zero ad spend. Closing even half the gap to the 8-9% cap doubles the conversions on this tier.
- The seasonality in SQP search volume (Aug-Sep build-up, Dec peak, Jan-Mar trough) maps cleanly onto the seller's revenue from Step 1. This confirms the off-season decline is market-wide demand, not a brand-specific issue. Q1 should not be diagnosed as "something broke" - it's the natural cycle.
- Tier 2 has proven brand traction beyond just the obvious "rest-adjacent" queries. Shotgun holster alone produced 14 brand purchases over the last 12 months - the second-best converting Tier 2 keyword after the Tier 1 hero. Upland hunting gear, dove hunting gear, skeet shooting accessories, and bird hunting accessories all show meaningful annual cart-adds. The right PPC strategy launches across the full Tier 2 set with ACoS gating, not pre-filters based on which queries "feel" closest to a rest. Tier 3, by contrast, has below-industry CVR and is genuinely research-intent.

## Things to Investigate Further

- The brand has near-zero impression share on "shooting rest" (31K vol/mo, 316 brand impressions, 0 clicks). This is technically intent-mismatched (refers mostly to rifle bench rests), but worth confirming in Step 4 whether any of the brand's listings are surfacing there as misaligned ad placements wasting impressions, or whether organic indexing is correctly excluding it.

## Questions for the Seller

- Have you ever tested PPC on "shotgun rest" or your branded terms before? If yes, at what spend, and what was the ROAS / why was it stopped? If no, what was the rationale for staying organic-only - margin, lack of expertise, or something else?
