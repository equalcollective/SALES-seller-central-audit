# Step 4: Ad Analysis - Helmet Flair

**Window:** 2026-02-21 to 2026-05-20 (the full ~90 days of available ad data). Status = ENABLED.
**Account totals (ENABLED):** Spend $8,070 | Sales $32,845 | ROAS 4.07.

## Account Level

### Campaign Structure

> **Finding: The account is fragmented into 1,143 enabled campaigns (653 actively spending), most of them single-keyword campaigns, and a large share of the keyword campaigns target generic "buying-a-helmet" terms that do not convert.**
>
> **Problem:**
> - 1,143 enabled campaigns for a brand spending ~$2.7k/mo is unmanageable. Budget and attention are spread across hundreds of one-keyword campaigns, many with a handful of clicks or none at all.
> - The keyword campaigns are dominated by generic, intent-mismatched terms. Examples currently losing money: "motorcycle helmet | exact" (ROAS 0.41-0.98), "full face helmet", "motorcycle accessory | exact" (ROAS 0.54), "car devil horn" ($37 spend, 0 orders), even "cat ear | broad" (25 clicks, 0 orders). These are people shopping for an actual helmet or a Halloween costume, not a $34.50 magnetic flair attachment. This is the exact intent mismatch the SQP analysis (Section 4) identified.
>
> **Solution:**
> - Consolidate into a tight, manageable structure: a small set of campaigns organized by theme (hero ASIN-targeting, helmet-accessory keywords, auto discovery, branded defense) rather than 1,000+ micro-campaigns.
> - Pause the generic helmet-buyer and costume keyword campaigns. They will never convert because the searcher does not want this product.
>
> **Impact:** Cleaner structure lets budget concentrate on the proven winners (product targeting and Top of Search, below) and removes the management overhead that lets losers run unnoticed.

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|--------|-------|-------|------|-----|-----|-----|
| Automatic | 5,256 | $1,675 | $3,445 | 2.06 | $34.45 | $0.32 | 1.90% |
| Manual | 13,331 | $6,396 | $29,400 | 4.60 | $33.30 | $0.48 | 6.62% |

Healthy. Manual drives 79% of spend at a strong 4.60 ROAS; auto is a smaller discovery channel at 2.06 (still above the 1.5 break-even floor). The harvest-and-scale loop is working at the top level. No action needed here.

### Campaign Profitability

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| SP B08Q21BRGD \| motorcycle helmet \| exact | $106.63 | $104.85 | 0.98 | 231 | 3 |
| SP B09LVYGD73 \| motorcycle helmet women \| exact | $93.71 | $139.80 | 1.49 | 181 | 4 |
| SP B08Q1WLGKW \| motorcycle helmet \| exact | $84.49 | $34.95 | 0.41 | 199 | 1 |
| SP B0BXQ4KF6N \| auto | $75.77 | $94.80 | 1.25 | 179 | 4 |
| SP B08Q21BRGD \| motorcycle accessory \| exact | $64.26 | $34.95 | 0.54 | 126 | 1 |
| SP B08Q21BRGD \| car devil horn \| exact | $37.37 | $0.00 | 0.00 | 81 | 0 |
| SP B08HJ6JVSQ \| motorcycle helmet women \| exact | $49.78 | $34.95 | 0.70 | 99 | 1 |
| ...plus ~10 more sub-$35 losers | | | | | |
| **Total wasted (ROAS<1.5, 25+ clicks)** | **~$743** | | | | |

> **Problem:** ~$743 over 90 days is going to keyword campaigns below 1.5x ROAS that have enough clicks to be conclusive. Almost every one targets a generic helmet-buying or costume term. An additional ~40 micro-campaigns spend $5-37 each with zero orders, adding a few hundred dollars more of slow bleed.
>
> **Solution:** Pause these campaigns and negate the generic terms ("motorcycle helmet," "full face helmet," "motorcycle accessory," "car devil horn," "cat ear").
>
> **Impact:** Reallocating that ~$743 to the product-targeting campaigns (6.24 ROAS, below) would generate ~$4,600 in sales vs the ~$580 those campaigns produce now. Net gain ~$4,000 in sales over 90 days from the same budget, before touching the broader micro-campaign drag.

### Targeting Strategy

**Keyword vs Product Targeting:**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|-------------------|--------|-------|-------|------|-----|-----|-----|
| Keyword Targeting | 12,777 | $5,141 | $14,773 | 2.87 | $33.57 | $0.40 | 3.44% |
| Product Targeting | 5,885 | $2,972 | $18,547 | 6.24 | $33.30 | $0.50 | 9.46% |

> **Finding: Product targeting is more than 2x the ROAS of keyword targeting (6.24 vs 2.87) and nearly 3x the conversion rate (9.46% vs 3.44%), yet receives only 37% of the budget.**
>
> **Problem:** The account leans on keyword targeting, but generic keywords are where the intent mismatch lives. Product targeting (showing the ears on relevant helmet/accessory product pages and on the brand's own listings) reaches the right person at the right moment and converts almost 3x better.
>
> **Solution:** Shift budget from generic keyword campaigns toward product/ASIN targeting. Expand product targeting onto more relevant helmet and motorcycle-gear listings (and competitor accessory listings). This is the PPC expression of the SQP finding that this product sells by placement, not by search.
>
> **Impact:** Moving even $1,500 from keyword targeting (2.87 ROAS) to product targeting (6.24 ROAS) lifts sales on that spend from ~$4,300 to ~$9,400, roughly $5,000 additional over the period.

**Match Type Breakdown:**

| Match Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|------------|--------|-------|-------|------|-----|-----|-----|
| EXACT | 4,466 | $2,129 | $6,305 | 2.96 | $33.90 | $0.48 | 4.16% |
| BROAD | 3,305 | $1,405 | $5,232 | 3.72 | $32.70 | $0.43 | 4.84% |

Broad outperforms exact (3.72 vs 2.96). Normally that signals a harvesting gap, but here it reflects something simpler: the exact-match keywords chosen are largely the generic head terms ("motorcycle helmet," "motorcycle accessory") that do not convert. The fix is keyword selection (drop the generics), which the structure consolidation above already addresses.

## Product Level (P0 - Cat Ears)

### P0 Campaign Map

P0 (Cat Ears) is advertised across many of the fragmented campaigns. Aggregated by product:

| Product | Spend | Sales | ROAS | Clicks | Orders |
|---------|-------|-------|------|--------|--------|
| Cat Ears for Helmet (P0) | $2,796 | $12,232 | 4.38 | 6,180 | 362 |
| Large Devil Horns (P1) | $2,848 | $11,279 | 3.96 | 6,748 | 325 |
| Small Devil Horns (P2) | $1,836 | $7,060 | 3.84 | 4,331 | 203 |
| Extra Nubbins (P3) | $66 | $484 | 7.28 | 141 | 27 |

P0 ad spend is ~$2,796, about 35% of the $8,070 account total, at a healthy 4.38 ROAS. The hero gets appropriate investment.

### Impression Share Blocker (Tier 2: Helmet Accessories) - Keyword & Placement Levers

Section 4 (SQP) identified the growth path as **impression share on the helmet-accessory market (Tier 2)**, where the brand holds only ~4.3% of a ~24-27% achievable cap but converts above industry. The PPC levers are (a) more spend on the terms/placements that work and (b) better placement mix. The data supports both.

**The brand already converts on the right helmet-accessory keywords, it just underfunds them:**

| Search Term / Target | Spend | Sales | ROAS | Clicks | Orders |
|-----------|-------|-------|------|--------|--------|
| helmet ear \| broad (B09LVYGD73) | $356.73 | $928.65 | 2.60 | 671 | 27 |
| helmet horn \| exact (B08Q21BRGD) | $94.70 | $873.75 | 9.23 | 176 | 24 |
| devil horn \| broad (B0BXQ4KF6N) | $153.21 | $768.55 | 5.02 | 364 | 28 |
| motorcycle helmet accessory \| exact (B08HJ6JVSQ) | $149.46 | $229.65 | 1.54 | 323 | 7 |
| ASIN/product targeting ("asinSameAs") - top campaigns | $938 / $229 / $163 | $5,387 / $1,503 / $1,608 | 5.74 / 6.57 / 9.85 | - | - |

The accessory-intent terms ("helmet ear," "helmet horn," "devil horn") and ASIN targeting convert well. The generic terms ("motorcycle helmet," "motorcycle accessory") do not. The lever is clear: concentrate budget on the accessory-intent and product-targeting winners, drop the generics.

### CTR Lever (Placement Distribution)

The SQP Tier 2 funnel showed CTR as the one soft spot (brand 1.25% vs 1.61% industry). The placement data explains why, and points to the fix.

| Placement | Spend | Sales | ROAS | CTR | CVR |
|-----------|-------|-------|------|-----|-----|
| Top of Search | $2,459 | $10,964 | 4.46 | 7.20% | 6.74% |
| Rest of Search | $3,497 | $6,765 | 1.93 | 0.93% | 2.36% |
| Product Pages | $2,150 | $4,623 | 2.15 | 0.74% | 2.67% |

> **Finding: Rest of Search consumes the most spend ($3,497) at the worst ROAS (1.93) and a 0.93% CTR, while Top of Search converts more than 2x better (4.46 ROAS, 6.74% CVR) on a 7.20% CTR but gets less budget.**
>
> **Problem:** The blended CTR looks low mostly because the budget is weighted toward the low-CTR Rest of Search placement. Top of Search is where this impulse, visual product wins (7.2% CTR).
>
> **Solution:** Increase Top of Search placement bid modifiers and pull back Rest of Search exposure. Pair this with the main-image fix from Step 2 (lifestyle hero showing the ears on a helmet) to lift CTR further at the premium placement.
>
> **Impact:** Shifting ~$1,500 from Rest of Search (1.93 ROAS) to Top of Search (4.46 ROAS) would lift sales on that spend from ~$2,900 to ~$6,700, roughly $3,800 additional over the period.

## Branded Defense

Several top campaigns labeled "SP brand ... asinSameAs" target the brand's own ASINs (e.g., b09lvygd73, b08q21brgd) and post the highest ROAS in the account (5.7-9.9). These function as cross-sell/defensive placements on the brand's own and sibling listings, which is healthy. There is no sign of disproportionate spend on branded keyword terms. Keep the defensive product-targeting; no branded keyword scaling needed.

## Insights

- **Product/ASIN targeting is the brand's best-performing channel (6.24 ROAS, 9.46% CVR) but gets only 37% of budget.** This is the PPC proof of the SQP thesis: the product sells by appearing on the right listings, not by winning generic keyword auctions. Shifting budget here is the single highest-confidence growth lever.
- **~$743+ over 90 days is wasted on generic helmet-buyer and costume keyword campaigns** ("motorcycle helmet," "full face helmet," "car devil horn," "cat ear"), all of which the SQP intent analysis predicted would fail. Pausing them funds the winners.
- **Top of Search is dramatically more efficient (4.46 ROAS, 7.2% CTR) than Rest of Search (1.93 ROAS, 0.93% CTR), yet Rest of Search gets the most spend.** Rebalancing placement modifiers is a fast, high-impact efficiency gain.

## Questions for the Seller

- The account is split into 1,100+ single-keyword campaigns. Was this built by a previous agency or an automated tool, and is there any reason to preserve that structure before we consolidate it? (Hypothesis: it is legacy SKAG sprawl that can be safely consolidated, but we want to confirm there is no reporting dependency on it.)
