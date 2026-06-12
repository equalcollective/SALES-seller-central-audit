# Step 3: SQP Analysis - P0 (Rhodium USB-C DAC/Amp)

**Note on window:** Periodic Audio's brand-level SQP footprint is extremely thin (it converts almost only on its own name). Per Aryan's direction and the blocker-detection fallback in CLAUDE.md, all metrics below use the full annual window (Jun 2025 to Apr 2026, the last ~11 months of available data) rather than a 3-month window, so the rate and share numbers accumulate enough volume to be meaningful.

## Tagging Rationale

The brand appears on three kinds of queries: its own name, true DAC-intent terms, and broad USB-C audio-adapter terms. Tiers (no keyword overlap):

- **Branded (existing equity, not a growth lever):** periodic audio, periodic audio rhodium, periodic audio rhodium dac, periodic audio dac, periodic rhodium, rhodium audio, rhodium dac, periodic audio electron, plus misspellings (pariodic/perodic audio). Customers who already know the brand. "Rhodium" is the product name, so "rhodium dac" is treated as branded.
- **Tier 1 (Hero, exact USB-C DAC intent):** usb c dac, usb dac, portable dac, dongle dac, dac dongle, headphone dac, audio dac, portable dac amp. The shopper wants exactly this kind of product. This is where the Rhodium is a credible, direct answer.
- **Tier 2 (Core DAC/amp market):** dac, dac amp, headphone amp, headphone amplifier, dac amp for pc. One step broader. Includes desktop DACs and amps, but the buyer wants a DAC/amp.
- **Tier 3 (Adjacent, USB-C audio adapters):** usb c headphone adapter, headphone jack to usb c, usb c to headphone jack, audio jack to usb c. High volume, but the intent skews heavily to sub-$15 commodity adapters (Apple-style dongles). Largely not capturable for a $49 audiophile DAC.

### Catalog Overlap Check
Only the Rhodium (P0) plausibly ranks for DAC-intent terms. The Neon (P1) is a Bluetooth receiver and would only touch "bluetooth dac"-type terms, which are not in these tiers. So **one product ranks per tier, impression-share cap stays at ~8-9%.**

## Market Sizing (annual averages, monthly)

| Tier | Monthly Search Volume | Monthly Add to Carts (Market) | Monthly Purchases (Market) | Est. Market Size ($/mo) |
|------|----------------------|-------------------------------|---------------------------|------------------------|
| Tier 1 (USB-C DAC) | ~26,100 | ~1,450 | ~415 | ~$65,000 |
| Tier 2 (DAC/amp) | ~71,800 | ~2,640 | ~630 | ~$118,800 |
| Tier 3 (USB-C adapters)* | ~25,000 | ~2,500 | ~1,340 | ~$30,000 |
| **Capturable focus (T1 + T2)** | **~98,000** | **~4,090** | **~1,045** | **~$184,000** |
| Branded | ~82 | ~9 | ~2 | (equity, not sized) |

*Estimated using a ~$45 average DAC price for Tier 1 and Tier 2. Tier 3 sized at a ~$12 adapter price because that is the real intent there. Tier 3 SQP coverage is partial (data present in only 7 of 11 months), so treat its figures as approximate.*

**Seasonality:** Tier 1/2 search volume lifts modestly in Nov-Jan (holiday), matching the Rhodium's December sales bump. The market is mildly seasonal, not dramatically so. The brand's revenue swings are driven more by its thin, lumpy branded/direct demand than by market seasonality.

## Market Share and Potential (annual)

| Tier | Impression Share | Click Share | Cart Share | Purchase Share | Trend |
|------|-----------------|-------------|------------|---------------|-------|
| Tier 1 (USB-C DAC) | 0.015% (914 of 5.95M impressions) | ~0.007% (7 clicks/yr) | 0% (0 carts) | 0% (0 purchases) | Flat at ~zero |
| Tier 2 (DAC/amp) | 0.002% (348 of 16.1M) | ~0.003% (3 clicks/yr) | ~0% | 0% | Flat at ~zero |
| Tier 3 (adapters) | 0.001% (11 of 1.25M) | 0% | 0% | 0% | Flat at ~zero |
| Branded | ~10% impression share | ~89% click share | ~95% cart share | ~100% purchase share | Stable |

**The headline:** Periodic Audio captures effectively 0% of the non-branded DAC market. Across Tier 1, Tier 2, and Tier 3 combined, it earned roughly 10 clicks and 0 purchases over the entire year from non-branded search. It wins its own name (where it holds ~89% click share and converts ~22 purchases/yr) and almost nothing else.

**Reconciliation with Seller Analytics:** The Rhodium sells ~84 units/yr (Seller Analytics), but SQP attributes only ~22 to branded search and ~0 to non-branded. That means roughly three-quarters of sales come from outside captured Amazon search, i.e. direct, repeat, and off-Amazon (DTC site, enthusiast community) demand. The Amazon listing is functioning as a fulfillment endpoint for demand generated elsewhere, not as a discovery engine.

**Branded note:** On the brand's own name, competitors take ~90% of impressions (Periodic holds ~10% impression share but ~89% of clicks). Competitors are showing up on "periodic audio" searches. There is a small branded-defense case, though absolute branded volume (~82 searches/mo) is tiny.

## Blockers & Growth Path

| Tier | Impression Share | CTR (Brand vs Industry) | CVR (Brand vs Industry) | Primary Blocker | Growth Path |
|------|-----------------|------------------------|------------------------|-----------------|-------------|
| Tier 1 (USB-C DAC) | 0.015% of ~8-9% max | 0.77% vs 1.78% (base too thin) | n/a (0 purchases) | **Impression Share** | Fix listing first (CVR risk), then PPC on high-intent terms. Best opportunity. |
| Tier 2 (DAC/amp) | 0.002% of ~8-9% max | n/a (3 clicks) | n/a | **Impression Share** | Same as Tier 1 but broader/harder. Enter only after Tier 1 proves out. |
| Tier 3 (adapters) | 0.001% of ~8-9% max | n/a | n/a | Intent mismatch | Mostly not capturable at $49. Skip. |

- **Tier 1 (USB-C DAC)** is the clear opportunity. The market is real (~$65k/mo demand, ~415 purchases/mo) and the Rhodium is a credible answer. The blocker is pure visibility: the brand is invisible (0.015% of a possible ~8-9%). But this is a "low impression share with unproven CVR" situation, so the listing must be fixed before scaling spend (see below).
- **Tier 2 (DAC/amp)** is larger but harder (more desktop-DAC and broad intent, more entrenched competitors). Pursue after Tier 1 converts.
- **Tier 3 (adapters)** is high-volume but the shopper wants a $9 dongle. Not capturable at $49. Skip for paid, do not build the listing around it.

**Critical caveat on CVR (why we cannot just buy impressions):** Because the brand has essentially zero non-branded clicks, we have no proof it converts cold traffic. The risk factors are concrete: a 4.0 rating vs 4.4-4.7 competitors, only 101 reviews vs thousands, and a main image that looks like a $9 commodity adapter. In a pay-per-click model, pouring spend onto the current listing would likely burn money. The growth path is therefore: fix the listing (main image, image count, brand video, reviews) first, then turn on tightly-targeted PPC starting with the most specific Tier 1 terms where a $49 audiophile DAC is a believable choice.

## ICAP Funnel (Tier 1, highest-opportunity tier)

The funnel for Tier 1 collapses at the very first stage. There is so little traffic past impressions that downstream rates cannot be assessed; the wall is visibility.

```
graph TD
    A["🔍 Impressions
    Share: 0.015% (of ~8-9% max)
    ⚠️ PRIMARY BLOCKER"] --> B["👆 Clicks
    7 clicks/yr (CTR ~0.8% vs ~1.8% industry)
    Gated by impressions"]
    B --> C["🛒 Add to Cart
    0 cart adds/yr
    No data, gated upstream"]
    C --> D["💰 Purchases
    0 purchases/yr
    No data, gated upstream"]

    style A fill:#ff6b6b,color:#fff
    style B fill:#ffd43b,color:#000
    style C fill:#ffd43b,color:#000
    style D fill:#ffd43b,color:#000
```

## Insights
- P0 (Rhodium DAC) holds ~0% share of a ~$184k/mo non-branded DAC market (Tier 1 + Tier 2). It lives almost entirely on its own brand name and off-Amazon demand. The entire growth thesis is: enter the non-branded market that the brand has never touched.
- The blocker is impression share, not conversion mechanics, but conversion is unproven on cold traffic and at real risk given the 4.0 rating and commodity-looking listing. So this is a "fix the listing, then scale PPC" play, not a "just buy impressions" play.
- Declining sessions from Step 1 line up with a brand coasting on existing demand with no acquisition engine. Without paid entry into non-branded search, organic visibility will keep eroding.

## Questions for the Seller
- About three-quarters of Amazon sales come from outside captured search (direct/repeat/DTC). Is Amazon a deliberate secondary channel behind your DTC site, or do you want to actively grow it? This determines whether a paid-acquisition investment makes sense.
