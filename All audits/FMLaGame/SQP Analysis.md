# Step 3: SQP Analysis - FMLaGame (P0: B0CTXKBB6X)

## Tagging Rationale

**Tier 1 (Hero):** Direct adult-party-card-game intent. The customer searching these terms is shopping for exactly this product type. Includes "cards against humanity" because shoppers searching the category-leading incumbent are the highest-intent audience for an alternative.
- Queries: adult party games, adult card games, card games for adults, games for adults, board games for adults, cards against humanity

**Tier 2 (Core market):** Broader card and board game queries. The customer is shopping for "a game" but not necessarily an adult-themed party card game.
- Queries: card games, board games

**Tier 3 (Adjacent / gift):** Gift-occasion queries where this product surfaces as one option among many. Highly seasonal, dominated by Q4 holiday volume.
- Queries: gag gifts, gag gifts funny adult, white elephant gifts for adults, white elephant gifts for adults funny, white elephant christmas gifts, funny gifts, christmas games

**Branded:** "fml" - a branded query, but with only 350-590 monthly volume, too small to act on as a growth lever. Brand defense level only.

**Catalog overlap:** Single ASIN. No catalog overlap. Default impression-share cap of ~8-9% applies to every tier.

**Excluded high-volume noise:** "snacks", "ps5 games", "gifts for teen girls", "family games", "mens valentines gifts", "secret santa gifts", "couples gifts" - the brand picks up impressions on these but they are intent-mismatched and not capturable.

## Market Sizing

12-month window: Apr 2025 - Mar 2026. Note that SQP only reports queries that meet a per-period volume threshold. In low-volume months, fewer queries report, so monthly totals are lower-bound. Q4 (Nov-Dec) drives 40-50% of annual volume across all tiers.

| Tier | Avg Monthly Search Volume | Avg Monthly Add to Carts (Market) | Avg Monthly Purchases (Market) | Est. Avg Market Size ($/mo) |
|------|---------------------------|-----------------------------------|--------------------------------|------------------------------|
| Tier 1 | ~508,000 | ~68,400 | ~16,900 | ~$1.37M |
| Tier 2 | ~960,000 | ~139,400 | ~28,200 | ~$2.78M |
| Tier 3 (Q4-heavy) | ~860,000 (avg, but ~9M in Dec) | ~159,000 (avg, but ~896K in Dec) | ~44,800 | ~$3.18M |

*Estimated using $20 avg product price (mid-range of competitive landscape: $15-25).*

**Seasonality:** Tier 1 search volume runs ~340-510K/mo Apr-Oct, then jumps to **1.08M (Nov)** and **1.37M (Dec)**, then collapses to 204K in Jan. That's a 4x peak vs trough. This matches the seller's own revenue pattern (Dec 2024: $6,587, Dec 2025: $2,890). The product is genuinely market-seasonal; revenue swings are driven by holiday demand, not brand-specific issues. Tier 3 is even more Q4-heavy: 80% of annual gift-query volume falls in Nov-Dec.

## Market Share and Potential

Two windows are shown: **Q4 peak (Nov-Dec 2025)**, when the brand actually has meaningful traffic, and **Q1 2026 (Jan-Mar)**, the current state.

### Q4 Peak (Nov-Dec 2025)

| Tier | Impression Share | Click Share | Cart Share | Purchase Share |
|------|------------------|-------------|------------|----------------|
| Tier 1 | 1.8% (Nov) -> 3.6% (Dec) | 4.5% -> 4.7% | 1.7% -> 1.6% | 0% -> 0.5% |
| Tier 2 | 0.4% -> 0.1% | 1.1% -> 0.5% | 0.2% -> 0.2% | 0% -> 0% |
| Tier 3 | 0.002% -> 0.04% | 0.06% -> 0.10% | 0% -> 0.02% | 0% -> 0% |

### Current State (Jan-Mar 2026)

| Tier | Impression Share | Click Share | Cart Share | Purchase Share |
|------|------------------|-------------|------------|----------------|
| Tier 1 | 0.05% -> 0.02% -> 0.02% | 0.09% -> 0.03% -> 0.06% | 0.03% -> 0.004% -> 0.02% | 0% -> 0.009% -> 0.02% |
| Tier 2 | ~0% | ~0% | ~0% | 0% |
| Tier 3 | ~0% | ~0% | ~0% | 0% |

**Key observations:**
- **Click share is consistently ~2-3x impression share on Tier 1**, even at peak. This is the most important finding: when the brand shows up, it wins clicks at well above the industry rate. The listing branding (FML mascot, distinctive packaging) stands out on the search results page. CTR is not the blocker.
- **Cart share collapses to 30-40% of click share, and purchase share collapses further.** The funnel breaks on the product detail page after click, not on the search results page.
- **Tier 1 share is essentially zero outside Q4.** Dec 2025 was the only period with non-trivial impression share (3.6%) and even then it's well below the ~9% cap.
- **Tier 2 and Tier 3 share are ~zero year-round.** These tiers are dominated by category leaders. Capturing here requires a step-change in brand recognition or a step-change in PPC investment that the unit economics cannot support.

## Blockers and Growth Path

Volume-weighted rates across the 12-month window:

| Tier | Brand CTR | Industry CTR | Brand ATC Rate | Industry ATC Rate | Brand CVR | Industry CVR | Primary Blocker | Growth Path |
|------|-----------|--------------|----------------|-------------------|-----------|--------------|-----------------|-------------|
| Tier 1 | 3.20% | 1.74% (1.84x) | 9.72% | 32.82% (30% of industry) | 1.01% | 8.13% (12% of industry) | **CVR / ATC Rate** | **Listing fix first, then scale PPC** |
| Tier 2 | 3.10% | 1.20% | 11.29% | 42.61% | 0.81% | 8.63% | Impression share + ATC rate | Skip - too broad to win |
| Tier 3 | 4.17% (low base) | 1.33% | 5.88% (low base) | 32.73% | 0% (3 carts, 0 purchases over 12mo) | 9.22% | Intent mismatch + invisibility | Skip - gift-query intent is too broad for this product |

**Tier 1 detail:** This is where the action is. Brand CTR (3.20%) is **1.84x industry CTR** (1.74%) - the listing wins the click battle on the search results page. But brand ATC rate is only 30% of industry, and brand CVR is only 12% of industry. Out of 2,582 brand clicks across Tier 1 over the past 12 months, only 26 became purchases. The PDP is leaking the entire funnel: shoppers click, browse, and bounce.

This matches the **"Low impression share + poor CVR"** pattern in CLAUDE.md but with an important nuance: CTR is actually strong, so the listing's main image and title are doing their job at the top of funnel. The collapse happens AFTER click - on the product detail page itself. The fixable PDP-side levers (per CLAUDE.md domain knowledge): bullets, images post-main, A+ content, B+ brand story (currently absent), social proof / review count, price positioning.

**Tier 2 detail:** Total Tier 2 impression share is 0.004%. The brand had 372 clicks over the entire 12-month period across "card games" and "board games" combined. These queries are dominated by Cards Against Humanity, Exploding Kittens, Catan, Monopoly, and similar mega-brands. Even at maximum bid spend, breaking through to ~3% impression share on a 27M-impression-per-month tier would require burning through PPC budget that the unit economics cannot support (break-even ROAS is ~2.0; current ROAS is 0.65). Skip.

**Tier 3 detail:** Q4 gift queries are massive (Dec 2025: 9M searches, 896K cart adds across the market) but the brand had 785 impressions and 0 purchases. The shopper searching "white elephant gifts" wants ideas; they're not committed to an adult party card game. The CTR (4.17%) looks high but is on a tiny base (only 815 impressions across 12 months). Cracking Tier 3 would require either (a) much stronger brand recognition so this product becomes a known gift answer, or (b) heavy off-Amazon demand generation (TikTok) so shoppers come back to Amazon already searching for the brand. Not an Amazon PPC play. Note for the call but don't make this a Year 1 priority.

## Insights

- **The blocker on the only winnable tier (Tier 1) is post-click, not visibility.** The brand wins clicks at 1.84x the industry rate (3.20% vs 1.74%) which is exceptional. But ATC rate drops to 30% of industry and CVR to 12% of industry. Pushing more impressions onto a broken PDP just burns budget. Fixing the listing comes BEFORE PPC scaling.
- **Q4 seasonality is real and confirmed.** Tier 1 search volume jumps 4x in Nov-Dec vs off-season. Tier 3 jumps 10x+. The seller's Dec 2024 ($6,587) and Dec 2025 ($2,890) revenue patterns track the SQP demand surge. The audit's planning horizon should anchor on **prepping the listing and PPC engine for Q4 2026**, with off-season months used to fix and test.
- **Even at peak (Dec 2025), Tier 1 impression share was 3.6% out of ~9% cap.** There is real room to grow visibility, but only after the PDP is converting at industry rates. If we doubled impression share on the current PDP, ATC and CVR stay broken and we'd just spend 2x as much for the same poor outcome.
- **Tier 2 and Tier 3 are not viable.** Year-round share is essentially zero on both. Tier 2 is dominated by Cards Against Humanity and similar incumbents that the brand cannot outbid economically. Tier 3 has intent mismatch (the shopper isn't committed to an adult card game). Action plan should focus 100% on Tier 1.

## Things to Investigate Further

- The strong Tier 1 CTR vs industry suggests the listing's main image and title are working well at the search-results stage. In Step 4 (Ad Analysis), check whether ad-driven traffic shows the same CTR strength or a different pattern. If ad CTR matches, the search-results-page presentation is healthy. If ad CTR is weak, the issue is targeting/placements.
- ATC rate is the cleanest signal for "PDP is broken" because it requires fewer events to be statistically significant than CVR. Verify in Step 4 whether ad-driven CVR matches organic CVR (~1%) or is materially different. If ad CVR is also ~1%, the PDP is the universal bottleneck.

## Questions for the Seller

- Tier 1 CTR is consistently 1.84x industry - when shoppers see the listing on search results, they click. But on the PDP, they bounce: ATC rate is 30% of industry, CVR is 12% of industry. (Hypothesis: the title/main image set an expectation that the actual PDP doesn't deliver on. Maybe the storytelling mechanic isn't visible quickly enough on the PDP, or the listing doesn't read as "worth $20" against the 4.3-star / 76-review social proof.) Have you reviewed PDP heat maps or session recordings, even informally, to see where shoppers drop off?
