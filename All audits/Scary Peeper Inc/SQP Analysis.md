# SQP Analysis - P0 (Peeping Tom Face Mask, Level 1)

**Hero ASIN:** B00F4HRW50
**Data window:** Market sizing Mar 2025 - Feb 2026 (12 months). Blocker analysis same window (seasonal product, short windows too thin).

## Tagging Rationale

Queries were tagged into four buckets based on how closely they match P0 intent and how cleanly the customer need maps to a peeping tom window mask.

- **Tier 1 (Hero):** Queries where the customer is searching for exactly the product concept ("peeping tom window prank", "window peeper", "scary face for window", etc.). P0 is the direct answer.
- **Tier 2 (Core market):** Halloween prank and jump-scare queries where P0 is one valid option among other prop formats. Broader intent, but still matches the product's use case.
- **Tier 3 (Broad/adjacent):** Massive-volume generic Halloween decoration queries ("halloween decorations outdoor", "halloween decor"). Technically relevant but intent is too broad; the market is saturated with every Halloween product imaginable.
- **Branded:** Five "scary peeper" variants. Tracked separately because branded traffic behaves differently from non-branded growth demand.

**Queries excluded from tagging:**
- Krampus queries (5 queries, 27 carts on "krampus decorations"). Scary Peeper is unexpectedly converting on Germanic-Christmas-demon search terms; not P0 relevant. Flagged as a question for the seller.
- Hitchhiker-specific branded queries ("scary peeper hitchhiker" branded volume) grouped with Branded rather than split into a separate P1-related bucket because the goal here is P0 analysis.
- Tapping witch queries and wearable-scary-mask queries that clearly don't match P0.

## Catalog Overlap Check

Multiple Scary Peeper products can rank for Tier 1 peeping tom queries. Every parent in the Scary Peeper Halloween portfolio uses "peeping tom" language in the listing:
- B00F4HRW50 (P0 Peeping Tom Face Mask, Level 1)
- B012U6OSZO (Peeping Tom Face Mask, Level 3 "Giggle")
- B075757SFG (Creeper Window Clown; title includes "Peeping Tom Halloween Prop")
- B07HS2CHKX (Electronic Tapping Peeper; title includes "Motion Activated Peeping Tom")
- B073X583YZ (Hitchhiker Prop; description includes "peeping tom window prank gags")

Realistic number of products ranking for the same Tier 1 queries: **3-4**. Adjusted impression share cap for Tier 1: **~24-27%** (not the default ~8-9%). This matters a lot for interpreting the 19.7% impression share observed below.

Tier 2 and Tier 3 have similar multi-product overlap because all Scary Peeper Halloween SKUs would surface for generic Halloween/prank searches.

## Market Sizing (12 months)

| Tier | Avg Monthly Search Volume | Avg Monthly Market Cart Adds | Avg Monthly Market Purchases | Est. Market Size ($/mo) |
|------|--------------------------|------------------------------|------------------------------|-------------------------|
| Tier 1 (Hero) | 1,003 | 79 | 19 | $1,580 |
| Tier 2 (Core market) | 51,814 | 4,883 | 902 | $97,660 |
| Tier 3 (Broad) | ~2.4M | ~260,500 | ~N/A | $6.5M+ |
| **Total P0-addressable (T1 + T2)** | **~52,800** | **~4,960** | **~920** | **~$99K/mo** |

*Estimated using $20 avg product price (midpoint across the peeping tom family and common substitute props).*

**Seasonality:** Clear and strong. Tier 1 search volume in October 2025 (2,925) was **5.8x** the Feb 2026 trough (296). Tier 2 search volume peaked at 387K in October vs. sub-3K in Dec/Jan/Feb, a 100x+ swing. This matches the seller's own revenue pattern in Step 1 (Halloween SKUs going from $9K+/month in Oct 2025 to near-zero in Jan 2026), confirming this is genuine market seasonality driven by Halloween demand, not a brand-specific issue.

## Market Share and Potential (12 months)

| Tier | Impression Share | Click Share | Cart Add Share | Purchase Share | Context |
|------|-----------------|-------------|----------------|---------------|---------|
| Tier 1 (Hero) | 19.7% | 40.7% | 40.5% | 45.4% | Brand dominates conversion but impression share has ~30% more headroom vs the ~24-27% adjusted cap |
| Tier 2 (Core) | 0.16% | 0.13% | 0.05% | 0.03% | Effectively invisible; massive room to grow |
| Tier 3 (Broad) | 0.0009% | ~0% | ~0% | ~0% | Too broad and saturated; not actionable |
| Branded | 29.3% | 59.8% | 67.3% | 73.6% | Strong on conversion. But 71% of "scary peeper" brand impressions go to non-Scary-Peeper-registered listings (Forum Novelties-tagged P0 is one driver) |

**Observations:**
- P0's big untapped opportunity is Tier 2, not Tier 1. Tier 1 is already partially captured and the market is small (~$1.6K/mo). Tier 2 is 60x larger (~$100K/mo) and the brand is essentially invisible there.
- On Tier 1, the brand wins when it shows up: 45% purchase share from 20% impression share means when the customer has the intent and sees Scary Peeper, they pick it. The growth lever on Tier 1 is pure impression share.
- On Branded queries, 71% of impressions go to non-Scary-Peeper-registered listings. A significant chunk of that leak is P0 itself being registered as Forum Novelties (flagged in Product Understanding). Fixing that registry error alone reclaims branded impression share without any ad spend.

## Blockers and Growth Path

| Tier | Impression Share | CTR (Brand vs Industry) | CVR (Brand vs Industry) | Primary Blocker | Growth Path |
|------|-----------------|------------------------|------------------------|-----------------|-------------|
| Tier 1 (Hero) | 19.7% (of ~24-27% cap) | 3.25% vs 1.57% (2.1x) | 5.90% vs 5.30% | **Impression Share (partial)** | PPC scaling: bid harder on Tier 1 queries to close the gap to cap. Brand converts above industry when it shows up, so every incremental impression is high-value |
| Tier 2 (Core) | 0.16% | 1.12% vs 1.37% (thin sample) | 1.06% vs 4.92% (thin sample) | **Impression Share** | PPC scaling: the brand barely shows up on "halloween jump scare", "halloween prank", "scary halloween decorations". Bid for visibility. Rates are unreliable at this sample size but will reveal themselves once traffic starts |
| Tier 3 (Broad) | 0.0009% | N/A | N/A | **Not capturable** | Skip. Market is too broad, intent too generic. The scale of competition on "halloween decorations outdoor" means even meaningful spend buys insignificant share. Win in Tier 1 and Tier 2 first, not here |
| Branded | 29.3% | Industry-aligned | Strong | **Impression Share (defensive)** | Fix brand registry (P0 as Forum Novelties) and launch a small branded defense campaign (2-3% of budget). Not a growth lever, but closing the leak reclaims existing demand |

**Additional context on Tier 2:** Brand stats are based on only 282 total clicks over 12 months, which is too thin to draw reliable CTR/CVR conclusions. The primary blocker is unambiguous: the brand is invisible. Bid to get traffic, then diagnose rates once volume arrives. One risk to flag: "scary halloween mask" (228K monthly search volume, largest Tier 2 query) carries mixed intent, some shoppers want a wearable costume mask, not a window prop. If CVR on this query comes back weak after scaling impressions, pull back and reallocate to the cleaner-intent Tier 2 queries ("halloween jump scare", "halloween prank", "scary halloween decorations").

## ICAP Funnel (Tier 2 — Primary Growth Opportunity)

The funnel below visualizes Tier 2 since it represents the biggest unlocked revenue potential. Tier 1 is partially captured and the tier ceiling is low; Tier 2 is 60x the market size and the brand isn't showing up at all.

```
graph TD
    A["🔍 Impressions
    Share: 0.16% (of ~24-27% adjusted cap)
    ⚠️ PRIMARY BLOCKER"] --> B["👆 Clicks
    CTR: 1.12% vs 1.37% industry
    Thin sample, unreliable"]
    B --> C["🛒 Add to Cart
    ATC Rate: 11.3% vs 26.6% industry
    Thin sample, unreliable"]
    C --> D["💰 Purchases
    CVR: 1.06% vs 4.92% industry
    Thin sample, unreliable"]

    style A fill:#ff6b6b,color:#fff
    style B fill:#ffd43b,color:#000
    style C fill:#ffd43b,color:#000
    style D fill:#ffd43b,color:#000
```

The brand converts well on direct peeping tom intent (Tier 1, 45% purchase share from 20% impression share). If impression share on Tier 2 even gets to 5% (out of a 24-27% cap) during Halloween preseason, at market conversion norms that would translate to roughly 250 incremental monthly carts during peak season (Sep-Oct), or an estimated ~$5,000/mo revenue lift in peak months from this tier alone. That is a meaningful 50%+ lift vs the seller's current Halloween SKU run-rate.

## Insights

- **P0 (Peeping Tom Face Mask, Level 1) dominates Tier 1 conversion but is capped at ~20% impression share against a ~24-27% ceiling.** The brand wins when it shows up (45% purchase share from 20% impression share), but the Tier 1 market is small (~$1.6K/mo) and the ceiling is near. Marginal PPC spend on Tier 1 has immediate payback but limited total upside.
- **Tier 2 is the growth lever, not Tier 1.** The addressable Tier 2 market is 60x bigger than Tier 1 ($98K vs $1.6K monthly) and the brand has 0.16% impression share. Even a modest impression share gain during Halloween preseason (Aug-Oct) would meaningfully lift Halloween revenue for the whole Scary Peeper portfolio, not just P0.
- **Halloween seasonality is confirmed at the market level.** Tier 1 search volume in Oct 2025 was 5.8x Feb 2026; Tier 2 was 100x+. The seller's revenue pattern (near-zero winter, $9K+ peaks in Oct) matches market demand, not a brand-specific issue. This confirms the 8-week plan should focus on Halloween preseason prep (Aug-Sep launch window), with ad ramp-up starting late July.
- **Branded impression share at 29.3% hides a significant leak.** On "scary peeper" branded searches, 71% of impressions go to non-Scary-Peeper-registered listings. A real chunk of that leak is P0 itself being registered under "Forum Novelties" instead of "Scary Peeper Fright At First Sight" (flagged in Product Understanding). Fixing the brand registry recaptures branded traffic with zero incremental ad cost.

## Things to Investigate Further in Step 4 (Ad Analysis)

- **Is the brand currently bidding on Tier 2 queries at all?** If there is zero ad spend on "halloween jump scare", "halloween prank", and "scary halloween decorations" today, that confirms impression share is missed due to zero-bid rather than inefficient bidding.
- **On Branded queries, are competitors bidding on "scary peeper"?** The 71% impression leak on branded searches suggests either competitor conquest ads or Amazon routing some of those impressions to the Forum-Novelties-registered P0 (where they count as non-Scary-Peeper). Check search term reports for evidence.
- **Tier 1 impression share stall.** Brand sits at 19.7% against an adjusted cap of ~24-27%. What's blocking the last ~5% — budget caps, bid ceilings, or query-level dayparting?

## Questions for the Seller

- **Why is Scary Peeper appearing on Krampus queries?** "Krampus decorations" (108K quarterly volume) has 27 cart adds attributed to the brand, and 5 other Krampus queries also convert. Krampus (the Germanic Christmas demon) has no obvious overlap with peeping tom masks. Is there a Krampus-themed SKU we haven't discovered, or is Amazon fuzzy-matching the catalog into this query cluster unintentionally? If intentional, it's a real secondary revenue lane; if unintentional, the spend behind it should be checked.
