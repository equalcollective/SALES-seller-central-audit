# Step 1: ASIN Selection — Insaltd™

## Context

Catalog has only **2 parent ASINs**, both for the same product line (sugar-free electrolyte powder packets). The catalog is effectively a single-product brand with a relisting story:

- **B0CBCJQRM1** ("Sugar Free Electrolytes Powder Packets") — older listing, live since at least Dec 2024. Was doing $3K-6K/month consistently through 2025, then collapsed in Dec 2025 / Jan 2026. Effectively dead since Feb 2026 ($0 sales).
- **B0GC18NZC4** ("Electrolytes") — new listing, first sales Jan 2026. Same product line, same 4 flavors + variety pack. Scaled organically from $192 (Jan) → $2,137 (Feb) → $5,338 (Mar). April run-rate is ~$10K/month.

The two parents share the same product (sugar-free electrolyte hydration packets, no stevia, keto/fasting positioning). The newer parent is a fresh relist of the same SKU set under a new ASIN.

## Data Readiness

- **Biz data:** Available 2024-07-01 through 2026-04-19. Full Q1 2026 covered.
- **Ad data:** Only 15 days available (2026-02-16 through 2026-03-03). Total ad spend across the entire window: **$0.44**. The seller is effectively not running advertising on Amazon. This is the central finding of the entire audit.

## Priority Table (Jan-Mar 2026)

| Priority | Product | 3-Mo Sales | 3-Mo Ad Spend | ROAS | TACoS | Organic Sales | Ad Sales % | Buy Box % | CVR | Trend |
|----------|---------|-----------|--------------|------|-------|---------------|-----------|-----------|-----|-------|
| P0 | Electrolytes (B0GC18NZC4) — new listing | $7,667 | $0 | n/a | 0% | $7,667 | 0% | ~96% | 16.7% | Growing |
| P1 | Sugar Free Electrolytes Powder Packets (B0CBCJQRM1) — old listing | $597 | $0.44 | n/a | 0% | $597 | 0% | ~62% | 7.0% | Declining (effectively dead) |

P2 and P3 are not applicable. There are only 2 parents in the catalog and the older one is dead.

**P0 selection rationale:** Unambiguous. B0GC18NZC4 is the only meaningfully active product. Mar 2026 sales were 12.4x B0CBCJQRM1's 3-month total. Trajectory is steeply growing. April weekly data continues at $2-3K/week.

## Hero Child SKU

Within P0 (B0GC18NZC4), the **Variety Pack (B0GC1LNJ76)** is the dominant child:
- Mar 2026: $2,760 (52% of parent revenue), 745 sessions, 18.5% CVR, 97.9% buy box
- Apr 19 week: $1,338 (57% of parent's weekly), 23.9% CVR

Single-flavor children (Mango Passionfruit, Citrus, Lemon Ginger) each contribute $200-900/month. Grapefruit is the weakest (5.6% CVR in March; investigate in Step 3).

## P0 Trajectory

The P0 listing only launched Jan 2026, so the relevant view is launch-to-date plus the most recent April weeks.

| Metric | Jan 2026 | Feb 2026 | Mar 2026 | Apr 2026 (partial, 3 wks) |
|--------|---------|---------|---------|---------------------------|
| Total Sales | $192 | $2,137 | $5,338 | $7,369 (run rate ~$10K/mo) |
| Sessions | 24 | 383 | 1,229 | ~1,317 (3 wks) |
| CVR | 20.8% | 18.0% | 16.4% | 22.0% |
| Buy Box % | 100% | 96.4% | 96.5% | ~96% (child level) |

- The listing is on a steep organic ramp. Sessions grew 50x in 3 months with zero ad investment, suggesting the product is winning organic traffic on its own merits (likely a combination of relevance, listing quality, and possibly external traffic).
- CVR is consistently strong (16-26% weekly) and well above typical electrolyte-category benchmarks (~10-12%). Conversion is not the blocker.
- Buy box is healthy at the child level (94-100% on every flavor). The parent-level dip to 81.8% in the week of Apr 19 is dilution from a placeholder child ASIN (B0GC18NZC4 itself, with 0% buy box and 1 session). Ignore at parent level, monitor at child level.

## Old Listing Context (B0CBCJQRM1)

Worth noting because the relisting decision sits behind the entire growth story:

| Period | Sales | Sessions | CVR | Buy Box % |
|--------|-------|----------|-----|-----------|
| 2025 monthly avg (Mar-Nov) | $3,800 | 870 | 14% | 87% |
| Nov 2025 | $2,656 | 493 | 14.2% | 77% |
| **Dec 2025** | $4,469 | **2,208** | **6.2%** | **51.7%** |
| Jan 2026 | $554 | 223 | 9.0% | 52.5% |
| Feb 2026 | $0 | 60 | 0% | 88.7% |

Dec 2025 shows a major external-traffic event (sessions spiked 4.5x to 2,208) but buy box collapsed to 51.7% and CVR fell to 6.2%, meaning the seller failed to capture the demand. The new listing (B0GC18NZC4) starts Jan 2026, suggesting a deliberate relist to escape the buy box / listing health issues on the old parent.

## Insights

- **Zero ad spend is the single biggest growth lever.** P0 is generating $5K+ months and a $10K April run rate purely on organic traffic. The brand has never built PPC infrastructure. Any reasonable Sponsored Products campaign would scale this account significantly. This is the headline finding for the call.
- **P0 (Electrolytes) CVR is exceptional (16-26%).** This is well above category norms. Organic traffic is converting at a rate that suggests strong product-listing-price fit. Adding paid traffic should compound, not dilute.
- **The Variety Pack drives the brand.** 52% of P0's March revenue and 57% in the latest week. This is the SKU to scale first in PPC.

## Things to Investigate

- P0 (Electrolytes) **Grapefruit child (B0GBZ337FV)** has 5.6% CVR vs 13-19% on other flavors despite similar buy box and sessions. Investigate in Step 2 (listing) and Step 3 (search query relevance) — could be an image, title, or query mismatch issue.
- **Source of the Mar-Apr 2026 organic traffic surge** on P0. Sessions jumped from 261 (week of Mar 22) to 1,306 (week of Mar 29), a 5x increase with no ad spend and no obvious seasonal driver for electrolytes. Likely candidates: an external creator/social mention, a TikTok or Reddit post, or an Amazon algorithm boost. Check in SQP Step 3 whether a specific keyword cluster spiked.

## Questions for the Seller

- The original listing (B0CBCJQRM1) was doing $3-6K/month for over a year, then buy box collapsed in Dec 2025 and the listing went dead. **Was this a deliberate relist (creating B0GC18NZC4 as a fresh parent), or did something happen to the old listing (suppression, hijack, MAP issue)?** Understanding what happened matters because the same risk applies to the new listing.
- The P0 (Electrolytes) listing went from 261 sessions (Mar 22 week) to 1,306 sessions (Mar 29 week) with no ad spend. **Did anything external drive that spike — a creator post, a press mention, a TikTok video?** This would change how we plan PPC scaling against organic momentum.
- **Why no ads?** Given the listing's strong CVR and growing organic demand, the absence of any meaningful Amazon PPC is the most consequential gap in the account. Is this intentional (budget, channel preference, prior bad experience), or has it just not been a priority?
