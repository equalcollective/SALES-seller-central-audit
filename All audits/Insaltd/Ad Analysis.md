# Step 4: Ad Analysis — Insaltd™

## Critical Data Limitation

**The seller has effectively no Amazon advertising activity.**

- **Seller-analytics MCP** (advertised product report): 15 days of data (2026-02-16 to 2026-03-03), total spend $0.44, total clicks 0.
- **Metabase Campaign Analysis V1** (campaign report): Zero rows for the seller across all spelling variants ("Insaltd", "Insaltd™", "Insaltd Labs", "INSALTD") for the full year of 2025-Apr 2026.

This is genuinely a no-ads account. Step 1 already flagged this. The standard ad-analysis flow (auto vs manual split, campaign structure findings, wasted-spend audits, search-term reports) does not apply.

## Reframe: From Audit to Launch Plan

Insaltd's growth thesis is **80% PPC launch + 20% listing reinforcement**. There is no current ad infrastructure to optimize. The deliverable for the call shifts from "here is what is broken" to "here is the campaign architecture you do not have, mapped to the blockers Section 4 (SQP) identified."

Every recommendation below is anchored to the SQP blocker analysis: the brand has near-zero impression share across Tier 1, Tier 2, and Tier 3 (<0.01% vs ~8% cap), the listing converts well (16-26% organic CVR), and the product has a defensible wedge (no stevia, high sodium). Therefore PPC = the lever, and the campaign mix below is built from the blockers backwards.

## Recommended Initial Campaign Architecture

> Account-level note: Subscribe & Save is enabled on P0 (per Step 2), and the brand has a Brand Store. Both are prerequisites for the campaign mix below; they're already in place.

### Account-Level Findings

**Campaign Structure**

> **Finding: No campaign infrastructure exists. Build it.**
>
> **Problem:**
> - Zero active campaigns in 2025 or Q1 2026.
> - $0.44 total spend across 15 days of ad data.
> - Listing has been carrying 100% of P0's $5K-10K monthly run rate organically. This is unusual for a brand with this kind of competitive presence and DTC infrastructure.
>
> **Solution:**
> Launch a 4-campaign starter mix on P0. Sequence and budget priorities below.
>
> **Impact:**
> - SQP shows Tier 1 monthly market = $2.18M cart-add value at industry CVR.
> - Capturing 1% of Tier 1 cart-adds at the brand's likely PPC ROAS of 3-4x = +$22K/month incremental sales at ~$5-7K monthly ad spend.
> - Capturing 3% (still well below the 8-9% cap) = +$65K/month at ~$15-20K spend.

**Auto vs Manual Split**

Not applicable yet. Recommendation for launch:

| Phase | Auto | Manual SP (Keyword) | Manual SP (Product Targeting) | Sponsored Brands | Sponsored Display |
|-------|------|---------------------|-------------------------------|------------------|-------------------|
| Weeks 1-2 | 25% (discovery) | 40% (Tier 1 exact + phrase) | 15% (own-ASIN defense) | 10% (brand store) | 10% (LMNT/Ultima conquest) |
| Weeks 4+ | 15% | 50% (graduated Tier 1 + Tier 2) | 15% | 10% | 10% |

The 25% auto allocation in Weeks 1-2 is for keyword discovery; Insaltd has no PPC history, so harvesting search terms from auto is non-trivial. After 2-3 weeks, harvested converters move into manual exact and auto ramps down.

**Targeting Strategy: Keyword Targeting**

Tier 1 keywords (from Section 4 SQP) go into manual SP keyword campaigns split by match type:
- **Exact match:** electrolyte packets, electrolytes powder packets, sugar free electrolyte powder packets, hydration packets, electrolytes without stevia, zero sugar electrolytes, instant hydration packets
- **Phrase match (looser):** same set, broader reach
- **Broad:** save for week 4+ once exact/phrase have proven targets

Tier 2 keywords go into a separate campaign launched in week 3-4 once Tier 1 is operating at target ACoS:
- electrolytes (high volume, high competition — bid conservatively initially)
- electrolytes powder, electrolyte powder, electrolyte drink, hydration powder

**Targeting Strategy: Product Targeting**

Run a Sponsored Display + Sponsored Products product-targeting campaign on these competitor ASINs:
- LMNT 30-stick variety pack (LMNT is the brand's primary conquest target; also try LMNT single-flavor 30-sticks)
- Ultima Replenisher (~170K monthly searches in own brand alone)
- Liquid IV Hydration Multiplier (volume leader in category; conquest-heavy)
- Cure Hydration single-flavor packs
- Element Electrolytes
- Drip Drop ORS

The narrative on creative: "no stevia, same sodium tier, same flavors as LMNT but cleaner sweetener." This was literally validated by an existing customer-uploaded video on the older listing titled *"Good frugal alternative to LMNT"*.

**Branded Defense (small, mandatory)**

Insaltd's own branded volume on Amazon is low (no significant "insaltd" SQP queries surfaced in top-50 monthly results), but a 2-3% budget defensive campaign on the brand's own name is non-optional. Without it, any competitor that decides to run conquest on "insaltd" can poach customers who already intend to buy.

### Product-Level (P0) Findings

**P0 Campaign Map (recommended)**

| Campaign | Type | Targeting | Budget Share | Tier Mapping |
|----------|------|-----------|--------------|--------------|
| INSALTD - Auto Discovery | Sponsored Products Auto | All match types | 25% (W1-2), 15% (W4+) | All tiers, harvest into manual |
| INSALTD - Tier 1 Exact | SP Manual Keyword | Exact match Tier 1 keywords | 25% | Tier 1 — primary blocker |
| INSALTD - Tier 1 Phrase | SP Manual Keyword | Phrase match Tier 1 | 15% | Tier 1 |
| INSALTD - Tier 2 Conservative | SP Manual Keyword | Exact + phrase Tier 2 | 10% (W4+ ramp) | Tier 2 |
| INSALTD - Conquest | SP Product Targeting | Competitor ASINs | 10% | Conquest sub-lever |
| INSALTD - Conquest SD | Sponsored Display | LMNT / Ultima ASINs | 5% | Conquest |
| INSALTD - Brand Store | Sponsored Brands | Brand store + headline | 7% | Brand awareness |
| INSALTD - Branded Defense | SP Manual Keyword | "insaltd" + variants | 3% | Defense |

Total recommended starting daily budget: **$150-250/day ($4.5K-7.5K/month)** scaling to $500-700/day ($15K-21K/month) by week 8 as winners are identified.

### Blocker-Specific Findings

> **Impression Share Blocker: Tier 1 keyword visibility (the entire growth thesis)**
>
> Section 4 (SQP) identified impression share as the primary blocker on every tier. The brand has 0.0094% impression share on Tier 1 against an ~8-9% cap. The PPC lever is bidding on the keywords where impression share is low.
>
> **Problem:**
> - 0.0094% Tier 1 impression share — essentially invisible.
> - 0 brand purchases on Tier 1 in Jan 2026 SQP.
> - Industry CVR on Tier 1 is 15.29%. Brand listing organic CVR is 16-26% (Step 2). The brand should convert at or above industry rates the moment traffic arrives.
>
> **Solution:**
> - Launch Tier 1 exact-match SP campaigns at aggressive starting bids (top-of-search modifiers +50%) to win the early-cohort visibility battle.
> - Use day-parted budgets aligned with peak hydration purchase windows (early morning + early afternoon based on category norms, refine after 2 weeks of data).
>
> **Impact:**
> - Industry Tier 1 cart-adds: 72.6K/month at $30 avg = $2.18M/month market.
> - Conservative target: 0.5% cart-add share by month 3 = ~$11K/month incremental ad-attributed sales.
> - Stretch target: 2-3% cart-add share by month 6 (still well below the 8-9% cap) = ~$50-65K/month incremental.

> **CTR/CVR Blockers: Not the immediate issue, but listing prep matters before scaling**
>
> SQP rates are too thin to confidently call CTR/CVR blockers (Tier 1 has only 19 brand clicks across Q1). However, two listing items from Step 2 should be addressed in parallel with the PPC launch because they will compound ad efficiency:
>
> **Problem:**
> - Rating slid from 4.4 (Apr 10) to 3.7 (Apr 23) on the Variety Pack child. CVR-sensitive PPC scaling against a falling rating wastes spend.
> - Per Step 2 Keepa snapshot, the new parent (B0GC18NZC4) is missing the seller-uploaded brand video that exists on the older parent.
>
> **Solution:**
> - Read the recent 1-3 star reviews on B0GC1LNJ76 and identify the cause of the rating slide before scaling Tier 2 spend (Tier 1 launch can begin in parallel).
> - Re-attach the brand video and influencer videos to B0GC18NZC4. Total effort 1-2 hours, immediate CVR-supportive lift.
>
> **Impact:**
> - A 0.3-star rating recovery (3.7 → 4.0) typically delivers 3-8% CVR improvement on this category type. At target Tier 1 traffic levels by month 3, that's $1-3K/month additional sales for zero additional ad spend.

## Insights

- **Insaltd's entire account-level finding for the call is positive, not corrective: the growth lever is unbuilt, not broken.** This reframing matters for how the seller hears the audit — it's not a critique of bad ads, it's a roadmap for what Amazon ads can unlock.
- **The conquest opportunity (LMNT, Ultima, etc.) is unusually strong.** Most brands don't have the spec parity + differentiation combo (same sodium, no stevia) that justifies aggressive competitor-ASIN targeting. Insaltd does. Section 4 SQP showed competitor-branded queries already drawing organic impressions (~200+/month combined) with zero conversion — paid product-targeting can convert that intent.

## Things to Investigate

None at the data level. The remaining open items for the call are seller-facing questions, captured below.

## Questions for the Seller

- **Have you ever run Amazon ads at any point, even briefly?** The 15-day MCP window may not be the full history. If there's prior search-term data anywhere (legacy account access, an old agency's reports), it would shortcut keyword discovery.
- **What's the current monthly profit margin on the Variety Pack and on the single-flavor 28-packs?** PPC scaling targets ROAS 3-4x at launch, dropping toward TACoS 12-15% as the listing matures. Without margin numbers we're guessing at sustainable bid ceilings.
- **What's an acceptable monthly ad spend ramp?** Recommendation above is $4.5-7.5K/month at launch scaling to $15-21K by month 2-3. Need confirmation this is reasonable for the seller's cash position.
