# SQP Analysis - P0 (SnoreStop for Pets 20 Chewable Tablets - B004GW338E)

**Data window:** 2025-04-01 to 2026-03-31 (12 months for market sizing; 2026-01-01 to 2026-03-31 for share/blocker analysis)

## Important Context on the Brand

The "Snore Stop" brand in SQP covers both the human SnoreStop product line and the pet line. Human-intent queries like "snore stopper" (~40k searches/mo) and "anti snore" (~13k searches/mo) make up the bulk of the brand's raw query universe in SQP. These are NOT capturable by P0 (pet tablets), which only converts on pet-intent searches. All pet-relevant queries were isolated for this tagging exercise and all human queries were excluded.

## Tagging Rationale

- **Tier 1 (Hero):** Queries where the customer is explicitly searching for a dog or cat snoring remedy. P0 (Tablets) is the direct answer. 6 queries tagged.
  - snore stopper for dogs, anti snoring for dogs, dog snoring relief, stop dog snoring, dog snoring, cat snoring
- **Tier 2 (Core market):** Pet nasal and breathing-related queries. The brand shows up here because it offers respiratory-adjacent products (nasal spray variant), but the homeopathic tablet is not the direct answer. 5 queries tagged.
  - dog nasal congestion relief, nasal spray for dogs, dog nasal spray, cpap for dogs, nasal drops for cats
- **Tier 3 (Broad):** Very general "pet snoring" terms (not species-specific). 3 queries tagged, but volume is tiny.
  - pet snoring, pet snoring relief, snoring for pets
- **Branded:** Terms containing the brand name for pets. Tagged separately for reporting, not treated as a growth lever. 2 queries tagged.

**Excluded:** Human-snoring queries (snore stopper, anti snore, snore, anti snore mouthpiece, snore strips, etc.) are excluded because P0 cannot convert on them. Also excluded is "anti snoring dog bed" (different product category, not a supplement).

## Catalog Overlap Check

SnoreStop USA runs 2 distinct active products on Amazon: **Tablets** (P0, B004GW338E) and **Spray** (P1, B000FL43XY), each with a 3-pack counterpart. Both products can and do rank for pet-snoring and pet-respiratory queries.

- **Tier 1 adjusted cap:** ~16-18% (2 products ranking)
- **Tier 2 adjusted cap:** ~16-18% (2 products ranking)

Anything below ~6% on Tier 1 or Tier 2 would be flagged as an impression share blocker.

## Market Sizing

| Tier | Monthly Search Volume | Monthly Add to Carts (Market) | Monthly Purchases (Market) | Est. Market Size ($/mo) |
|------|----------------------|-------------------------------|---------------------------|------------------------|
| Tier 1 (Pet Snoring) | 711 | 51 | 19 | ~$765 |
| Tier 2 (Pet Nasal/Breathing) | 1,884 | 205 | 89 | ~$3,075 |
| Tier 3 (Broad Pet Snoring) | 2 | 1 | <1 | ~$15 |
| **Total capturable for P0 (Tier 1 only)** | **711** | **51** | **19** | **~$765** |

*Estimated using $15 avg product price based on competitive landscape analysis.*

**Seasonality:** Tier 1 search volume is mildly seasonal. It climbed from ~470/mo in summer 2025 to ~1,000/mo between Oct 2025 and Jan 2026, then declined back to ~800/mo in March 2026. This is a ~2x winter-over-summer swing, consistent with pets (and their owners) spending more time indoors sleeping during colder months. The seller's own revenue pattern does NOT clearly follow this, so the seller's traffic decline is driven by something other than seasonality.

**Critical finding: The capturable market is very small.** Tier 2 volume looks large on paper but is not leverageable by P0 (see Blocker Detection below). Practical addressable market for P0 is Tier 1 only, which at $765/mo total is about half the size of the seller's current revenue on this ASIN.

## Market Share and Potential (3-Month, Jan-Mar 2026)

| Tier | Impression Share | Click Share | Cart Share | Purchase Share | Trend |
|------|-----------------|-------------|------------|---------------|-------|
| Tier 1 | 14.5% (of ~17% cap) | 44.5% | 52.0% | 64.1% | Stable, already near cap |
| Tier 2 | 2.0% (of ~17% cap) | 2.7% | 0.8% | **0.0%** | Stable low, not converting |
| Tier 3 | n/a | n/a | n/a | n/a | Too small to analyze |
| Branded | ~11% | ~70% | ~89% | ~95% | Stable, as expected |

**Key observations:**
- **Tier 1 dominance is remarkable.** Brand holds 64% of category purchases on only 14.5% impression share. This is the category-leader advantage: when SnoreStop shows up, it wins. Impression share is already near the adjusted cap (~17% for 2 products), so there is limited visibility upside left on Tier 1.
- **Tier 2 is non-capturable.** 0 purchases on 55 clicks across 3 months. Shoppers searching for nasal spray, CPAP, or nasal congestion products for pets consistently do not convert on a homeopathic anti-snoring tablet. Intent mismatch is absolute.
- **Branded volume is tiny.** ~90 cart adds/year (~$1,350 in branded sales), indicating minimal existing brand recognition outside of the pet-snoring category. Branded searches do not represent a meaningful growth lever.

## Blockers & Growth Path

| Tier | Impression Share | CTR (Brand vs Industry) | CVR (Brand vs Industry) | Primary Blocker | Growth Path |
|------|-----------------|------------------------|------------------------|-----------------|-------------|
| Tier 1 | 14.5% (of ~17% cap) | 5.63% vs 1.83% (3x healthy) | 8.0% vs 5.5% (healthy) | **None internal. Market size.** | Maxed out. Near cap, winning the funnel. Little room to scale through ads or listing. |
| Tier 2 | 2.0% (of ~17% cap) | 2.38% vs 1.70% (healthy) | **0% vs 10.3% (blocker)** | **CVR / Intent mismatch** | Not capturable. The product does not match query intent (homeopathic tablet vs. nasal spray / CPAP). Skip. |
| Tier 3 | n/a | n/a | n/a | Too small | Ignore. |

**ICAP funnel verdict: This is the "Maxed out potential" pattern from [CLAUDE.md](../../CLAUDE.md) Domain Knowledge.**

The uncomfortable conclusion: **P0 has already captured most of the available demand for pet-snoring searches on Amazon.** The brand is the category leader in a very small category, winning at the impression-share cap, beating industry on every funnel metric. There is no hidden visibility unlock, no obvious conversion gap, no wasted impressions on irrelevant keywords.

The market is the ceiling, not the brand.

**Where does growth actually come from for P0?**
1. **Grow the category.** Pet snoring is under-searched relative to how many pets actually snore. Owner education (content marketing, veterinarian partnerships, social proof around common snoring breeds) can expand Tier 1 volume over time. This is not an Amazon ad lever.
2. **Fix the rating.** At 3.3 stars, the listing is converting well despite the rating. Moving to 4.0+ would lift CTR further and Amazon may algorithmically allocate more impressions, potentially pushing impression share above the current 14.5%.
3. **Channel mix.** Amazon may not be the primary growth channel for this product. The DTC site sells the same SKU at a higher price, suggesting the true TAM lives partially outside Amazon.
4. **Product expansion.** The spray variant (P1) is under-utilized on Amazon ($705 in 3-month sales). Growing the spray could capture part of Tier 2 (nasal spray queries) where the tablet cannot, since a spray product would match that search intent.

## Insights

- **P0 (Tablets) already dominates Tier 1.** 14.5% impression share near the ~17% cap, 64% purchase share, 3x industry CTR. This is the category-defining advantage playing out.
- **P0 (Tablets) session decline is not a demand problem.** Tier 1 search volume has held steady or grown over the past 12 months while the seller's sessions dropped ~50%. The cause is likely the Q2 2025 price increase from $10 to $15 (flipping the listing out of the budget-shopper consideration set) or a listing rank penalty triggered by the Nov-Dec 2025 buy box dips, not market shrinkage.
- **Tier 2 cannot be converted into a growth lever for P0.** 0 purchases on 55 clicks over 3 months proves the intent mismatch. Any future ad spend that bids on nasal-spray or CPAP keywords will burn budget.
- **The addressable Amazon market for P0 is about $765/mo.** Even at 100% capture the brand adds ~$200/mo over current revenue. This is the hardest truth of the audit: Amazon search is not the growth channel for this ASIN.

## Things to Investigate Further

- **Ad spend on Tier 2 keywords.** Step 4 should verify whether the seller is bidding on nasal spray / CPAP / nasal congestion keywords despite the 0% conversion rate. If yes, this is wasted spend that should be immediately redirected.
- **Ad spend split between branded and non-branded.** Step 4 should confirm that branded ad spend (snorestop for pets, snore stop for pets) is capped at a small defensive percentage, not used as a growth engine.
- **Keyword coverage in the listing.** Title and bullets should surface Tier 1 winning queries (snore stopper for dogs, anti snoring for dogs, stop dog snoring, cat snoring). Confirm in Step 4 that all Tier 1 queries are captured in the listing copy for organic SEO.

## Questions for the Seller

- **Growth expectations on Amazon:** Given the Amazon-addressable market for pet-snoring queries is ~$750/mo and you are already capturing most of it, what is your growth hypothesis for this ASIN on Amazon? Is there a category expansion play you are counting on (e.g., broader pet respiratory, anxiety, sleep), or is Amazon expected to plateau while DTC/retail drives growth?
