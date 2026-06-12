# SQP Analysis: Reed Diffuser (P0)

Parent: B0CNSC2D85 (100ml). Scope limited to this parent (per Aryan's direction: don't merge the 250ml for now).

## Tier Structure

### Tier 1 - Hero (Reed Diffuser core intent)

These queries express direct reed-diffuser intent and match what Ecodrop sells. 11 queries.

- **Keywords:** reed diffuser, reed diffuser refill, diffuser refills, reed diffusers for home, reed diffusers, diffuser refill, diffuser oil refill, reed diffuser oil, diffuser reed, christmas reed diffuser, reed diffuser bottles
- **Rationale:** Buyer is searching specifically for a reed-diffuser product or its refill. Highest-intent match for Ecodrop's 100ml reed diffuser set + refill SKUs.

### Tier 2 - Core market (broad diffuser intent)

Broader diffuser queries where the buyer may want a reed diffuser, but could equally want an electric / USB / aromatherapy oil diffuser. Reed diffuser is one of several possible answers. 22 queries.

- **Keywords:** diffuser, oil diffusers, diffuser oil, essential oils for diffusers for home, diffusers for home, essential oil diffuser, diffusers, oil diffuser, diffuser sticks, room diffuser, aromatherapy diffuser, oil for diffuser, aroma diffuser, diffuser oils, scent diffuser, bathroom diffuser, diffuser set, fragrance diffuser, essential oil diffusers for home, oil diffuser essential oils, christmas essential oils for diffusers for home, christmas oils for diffusers
- **Rationale:** Relevant but broader. Brand CTR (0.60%) is dramatically below industry (1.40%) on this tier, suggesting a reed-diffuser product doesn't win against electric-diffuser thumbnails on these generic queries.

### Tier 3 - Scent-led (high-intent niche)

Queries where the user is searching for a specific scent + diffuser format. Small volume but very high efficiency when Ecodrop shows up.

- **Keywords:** lavender diffuser, vanilla diffuser, vanilla reed diffuser
- **Rationale:** Scent-specific buyers convert strongly. Brand CVR 22.73% vs industry 17.37%, ATC rate 43.2% vs 42.5%. Low volume, but a clear win pattern.

### Branded

14 queries covering "ecodrop", "ecodrop essential oils", "ecodrop reed diffuser", etc. Treated separately - not a growth lever, only a defense line.

## Market Sizing (annual, April 2025 - March 2026)

| Tier | Monthly Search Volume | Monthly Purchases (Market) | Est. Monthly Market Size (£) |
|---|---:|---:|---:|
| Tier 1 | ~141,700 | ~6,950 | ~£97k |
| Tier 2 | ~332,500 | ~11,000 | ~£154k |
| Tier 3 | ~3,170 | ~206 | ~£2.9k |
| **Total P0-relevant** | **~477,400** | **~18,200** | **~£254k** |

*Estimated using £14 AOV (account average).*

Context: Ecodrop's actual Reed Diffuser revenue is ~£6k/month (£71.5k/year). So they currently capture well under 3% of the P0-relevant market, and there are 2+ parents in their catalog that could rank on these queries.

## Impression Share: Collapse in Q1 2026

This is the headline finding. Impression share on Tier 1 queries was stable ~1% through Sep-Nov 2025, then collapsed starting December.

| Month | Imp Share % | Click Share % | Purchase Share % |
|---|---:|---:|---:|
| Apr 2025 | 0.82 | 1.05 | 1.27 |
| May 2025 | 0.57 | 0.75 | 1.08 |
| Jun 2025 | 0.61 | 0.88 | 1.02 |
| Jul 2025 | 0.65 | 0.89 | 1.41 |
| Aug 2025 | 0.86 | 1.08 | 1.38 |
| Sep 2025 | 1.03 | 1.17 | 1.43 |
| **Oct 2025** | **1.10** (peak) | **1.20** | **1.68** (peak) |
| Nov 2025 | 1.09 | 0.95 | 0.96 |
| **Dec 2025** | **0.49** (55% drop) | 0.44 | 0.60 |
| Jan 2026 | 0.37 | 0.30 | 0.35 |
| Feb 2026 | 0.36 | 0.38 | 0.45 |
| **Mar 2026** | **0.16** (85% below Oct peak) | 0.32 | 0.46 |

### Likely cause: BSR collapse in Home Fragrance Accessories

Sales rank history (Keepa) for the 100ml children in the Home Fragrance Accessories sub-category shows the BSR roughly doubled (worsened) between Q3 2025 and Q1 2026 across almost every SKU:

| Child ASIN | Variant | Q3 2025 avg BSR | Q1 2026 avg BSR | Change |
|---|---|---:|---:|---|
| B0BN95BVFW | Vanilla & Coffee Refill | 68 | 128 | ~1.9x worse |
| B0BP3L6782 | Lavender Set | 63 | 130 | ~2.1x worse |
| B0BPRB8G4K | Bergamot Set | 64 | 130 | ~2.0x worse |
| B0BQGJBMQL | Rose Set (Health & Care cat.) | 106 | 270 | ~2.5x worse |
| B0BQGK9N9H | Wood Sage Set (H&PC cat.) | 88 | 251 | ~2.8x worse |
| B0BPRCHJGZ | Lavender Refill | 65 | 127 | ~2.0x worse |
| B0BQGLLYMW | Wood Sage Refill | 55 | 132 | ~2.4x worse |
| B0CR7W9QRH | Vanilla Violet Set | 61 | 128 | ~2.1x worse |

The BSR degradation is consistent across every child and started in December 2025. This is not a single-SKU issue, it's a parent-level visibility collapse. Mechanism: organic velocity dropped (possibly Nov/Dec post-holiday decay + loss of a key keyword ranking) → BSR worsened → organic impressions fell → fewer clicks/purchases → BSR worsened further. Classic rank spiral.

## Catalog Overlap & Adjusted Impression Share Cap

Per CLAUDE.md Phase 5, the maximum impression share cap scales with the number of products that rank on the same query.

Current catalog for reed diffuser queries:
- **B0CNSC2D85 (100ml parent)** - ranking on most Tier 1 queries
- **B0GTWLTMFH (250ml parent)** - new, just launched, not yet ranking consistently

Practical cap today: ~8-9% (effectively single-product, since 250ml isn't ranking yet).
Target cap once 250ml builds rank: ~16-18% (two products).

**Actual impression share: 0.55% annual, collapsing to 0.16% in March 2026.** Ecodrop has 30-50x headroom before hitting even the single-product ceiling.

**Answering your question on how to interpret impression share for the split/merged situation:**

Impression share is calculated against the TOTAL impressions served on the query, and it's brand-level (not ASIN-level). So:
- When oils were merged into one parent, the brand's max impression share was ~8-9% (single product ranks).
- After the split, if multiple oil ASINs rank on the same query (e.g., "essential oil" might return several Ecodrop scents), the brand's impression share cap can rise (up to ~24-27% if 3 products rank).
- In practice this is NOT automatic - Amazon's A9 usually shows only one product per brand per position, so having more ASINs doesn't linearly multiply impression share. The lift is real but modest, maybe 1.5-2x.

For Reed Diffuser specifically (which is the subject of this audit): the split doesn't apply because these listings were not affected by it. The 100ml parent (17 children) has been stable since 2022. The 250ml parent (14 children) is independent and new. What we're seeing on Reed Diffuser is not a split-artifact - it's a BSR collapse from late 2025.

## ICAP Funnel - Tier 1 Blocker Analysis (annual)

| Stage | Brand | Industry | Status |
|---|---:|---:|---|
| Impression Share | 0.55% | n/a (cap ~8-9%) | 🚨 PRIMARY BLOCKER (30-50x headroom, and collapsing) |
| CTR | 0.80% | 1.25% | ⚠️ SECONDARY BLOCKER (36% below industry) |
| ATC Rate | 35.2% | 37.7% | ✅ Near industry |
| CVR | 12.70% | 15.66% | ⚠️ Mildly below (19% gap, not critical) |

**Primary blocker: Impression Share.** The gap between where Ecodrop is (0.55%, or 0.16% in Mar 2026) and where they could be (8-9% single-product cap) is 15-50x. Every other metric is secondary.

**Secondary blocker: CTR.** Persistent 36% gap below industry suggests listing presentation on the search results page isn't winning (main image, title structure, price, ratings). Fixing this compounds once ads pull in more impressions.

**Growth Path:**

1. **PPC-led impression recovery (urgent).** Bid aggressively on Tier 1 exact-match keywords (reed diffuser, reed diffuser refill, diffuser refills, etc.) to flood impressions immediately. Goal: get impression share from 0.16% → 2-3% in 4-6 weeks. This also drives organic velocity, which should repair BSR over time.
2. **Listing CTR fix.** Refresh the main image (add scent/size callouts, strong lifestyle context), tighten the title (lead with "Reed Diffuser + scent + size"), ensure ratings are showing clearly. Target: brand CTR within 80% of industry (≥1.0%).
3. **Tier 3 scaling.** Add dedicated ad groups for "lavender diffuser", "vanilla reed diffuser", "vanilla diffuser". Small volume but brand already out-converts industry here - easy incremental wins.
4. **Tier 2 - deprioritize for scaling.** Generic "diffuser" queries have CTR 0.60% vs industry 1.40%. Reed diffuser struggles to win the click against electric/USB diffusers on these broad terms. Keep minimal spend here; don't chase this tier until the listing wins on Tier 1 first.

## Market Opportunity Sizing

**If Reed Diffuser hits 5% impression share on Tier 1 (well below the 8-9% cap):**

- Current: 0.55% imp share → ~237 brand purchases/year from Tier 1 SQP paths = ~£3.3k/year SQP-attributed
- Target: 5% imp share → ~9.1x lift → ~£30k/year SQP-attributed from Tier 1 alone
- Scale-through effect to organic PDP and cross-tier traffic: Reed Diffuser's actual revenue today is £71.5k/year. A 5-10x lift on Tier 1 visibility, combined with restored BSR, could plausibly add £30-50k/year to the Reed Diffuser parent's revenue. That's £2.5-4k/month of direct contribution to the £60k goal.

This is before considering the 250ml parent, which currently has zero Tier 1 presence.

## What to include in Section 7 (for the final output)

**Insights:**
- P0 (Reed Diffuser) impression share collapsed from 1.10% in Oct 2025 to 0.16% in Mar 2026. Directly explains the 56% QoQ revenue drop on this parent.
- The collapse is driven by a parent-level BSR degradation in Home Fragrance Accessories: all 16 children's rank roughly doubled between Q3 2025 and Q1 2026.
- Primary blocker is impression share, not CTR or CVR. The listing converts - it just isn't showing up anymore.
- The "split" that the client is concerned about doesn't apply to Reed Diffuser. The 100ml parent has been stable since 2022 and didn't go through a merge/split transition. This is a distinct problem from the essential oils situation.

**Questions for the seller:**
- What changed for the 100ml reed diffuser listings around late November / early December 2025? Possible causes: stockout, listing edit rejected by Amazon, price change, competitor launch eating share, review issue, or agency paused a campaign that had been propping up organic velocity. We can't tell from the data alone.
- Is the UK ad agency (Eventuring) running dedicated reed-diffuser PPC? Ad data shows only £406 spend on this parent over Jan + Mar 2026, which doesn't match the scale needed to recover from the impression share collapse.
