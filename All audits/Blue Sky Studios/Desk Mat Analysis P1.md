# Blue Sky Studios - Desk Mat (P1) Mini-Analysis

This is a focused follow-on to the main P0 audit. Same data window: Feb-Mar 2026 biz, Jan 29 - Apr 28 2026 ads.

## Child-Level Breakdown (Feb-Mar 2026)

The Desk Mat parent (B0FMKGCFXG) has 9 active children, each themed on a different IP. The top sellers are not the IPs you'd predict.

| Variant (IP) | Child ASIN | 2-Mo Sales | 2-Mo Sessions | CVR | Buy Box |
|---|---|---|---|---|---|
| **Kuromi** | B0D9KXKW29 | **£1,500** | 1,242 | 8.1% | 78.7% |
| Transformers | B0D2S5HZK8 | £795 | 830 | 6.5% | 99.4% |
| Snoopy Jumbo | B0FWS1HV16 | £733 (March only) | 930 | 4.4% | 92% |
| SpongeBob | B0CDTSX2H2 | £504 | 472 | 7.1% | 99.9% |
| TMNT | B0CDTTNWNL | £142 | 437 | 2.5% | 82.6% |
| Harry Potter Hogwarts | B0CDTSPV7H | £171 | 588 | 2.0% | 97.5% |
| Harry Potter Ollivanders | B0F2K8PQD1 | £140 | 437 | 2.5% | 92.4% |
| Pochacco | B0F2JR5NZR | £120 | 477 | 1.8% | 94.7% |
| Emily in Paris | B0CP5TMLS3 | £24 | 284 | 0.6% | 99.3% |

**Hero variant: Kuromi (B0D9KXKW29) at £1,500 / 36% of parent revenue.**

Notable patterns:
- **Snoopy Jumbo went 0 -> £675 in one month (Feb -> Mar).** Either a recent launch ramping, or a winning new variant. Watch list for next audit.
- **Both Harry Potter variants underperform.** Hogwarts and Ollivanders combined are £311, a small fraction of Kuromi. The wand pen owns the HP gift demand; on the desk mat parent, HP is not the winner.
- **Emily in Paris is essentially dead** at £24 over 2 months on 284 sessions (0.6% CVR). Consider phasing out.
- **Kuromi has 78.7% buy box** while every other top child sits at 92-99%. The £1,500 winner has the worst buy box in the parent. That alone is a non-trivial recoverable loss.

## Kuromi Desk Mat Product Profile

- **What it is:** A licensed Kuromi (Sanrio) gaming/writing desk pad, £15. Marketed as a mouse pad / desk mat with the Kuromi character print.
- **Who buys it:** Sanrio fans, anime/kawaii aesthetic shoppers, gift buyers (similar Q4 gift dynamic as the wand pen), and gamers who want a themed mouse pad.
- **Why it sells:** Kuromi is a fast-growing Sanrio character with a distinct gothic/dark-cute aesthetic. Most gaming mouse pads are masculine/RGB; Kuromi is one of the few cute-but-edgy options at this size and price point.
- **Brand vibe:** Same licensee-aggregator model as the rest of the BSS catalog. Customer is buying "Kuromi", not "Blue Sky Studios".

## SQP Analysis (Brand-Level, Filtered to Kuromi Desk-Mat-Relevant Queries)

> SQP is brand-level, so the queries here are the ones where the Kuromi desk mat / mouse pad is the primary product the brand could surface. Queries where other BSS products (Hello Kitty mouse pad, etc.) are the actual ranker have been excluded from the Kuromi tiers.

### Tier Framework

**Tier 1 (Hero):** Kuromi-specific desk pad queries
- `kuromi mouse pad` (the dominant query, UK terminology favors "mouse pad" over "desk mat")
- `kuromi desk mat`

**Tier 2 (Aesthetic-aligned):** Sanrio + cute/kawaii desk pads where Kuromi is a strong fit
- `sanrio mouse pad`
- `cute mouse pad`
- `cute desk mat`
- `kawaii mouse pad`
- `kawaii desk mat`

**Tier 3 (Broad/adjacent):** Anime, gothic, and aesthetic-broad desk pads
- `anime mouse pad`
- `anime desk mat`
- `gothic mouse pad`

**Excluded:** "desk mat" and "mouse pad" generic. Both are 50K-100K monthly UK volume but the brand has 0.05-0.2% impression share. Too broad to be capturable for one variant. The other character-specific queries ("hello kitty mouse pad", "pokemon desk mat", "star wars mouse pad", "harry potter mouse pad") are excluded because the Kuromi mat doesn't compete for those buyers, even if the BSS catalog has other products that do.

**Catalog overlap:** Tier 1 queries -> Kuromi mat is the only BSS product (1 product, ~8-9% cap). Tier 2 queries -> Kuromi mat plus possibly a sibling (e.g., "sanrio mouse pad" could surface Kuromi or another Sanrio product), call it 1-2 products (~8-18% cap). Tier 3 -> 1 product, ~8-9% cap.

### Tier 1 Numbers (the headline)

Aggregating `kuromi mouse pad` across the 9 monthly periods Apr 2025 - Feb 2026 where the query had any brand activity:

| Funnel Stage | Brand | Total | Share |
|---|---|---|---|
| Impressions | 2,205 | 34,233 | **6.44%** |
| Clicks | 230 | 666 | **34.5%** |
| Cart Adds | 132 | 224 | **58.9%** |
| Purchases | 39 | 59 | **66.1%** |

**Brand vs Industry rates:**

| Stage | Brand | Industry | Brand vs Industry |
|---|---|---|---|
| CTR | 10.43% | 1.94% | **+5.4x** |
| ATC Rate | 57.4% | 33.6% | +71% |
| CVR | 16.96% | 8.86% | +91% |

**The brand owns this query.** 66% purchase share with 6.4% impression share means the brand is converting impressions at 10x the rate of the average competitor. This is the strongest funnel signal in the entire audit, stronger than the wand pen.

Most recent 2 months (Jan-Feb 2026): impression share 7.27%, purchase share 61.1%. Stable / strong.

### Tier 1 Search Volume

Tier 1 monthly volume: ~150-300 (peak Dec 2025 = 292). Small absolute numbers, but high-intent and high-share. Tier 1 is a "lock-and-defend" tier, not the main growth lever.

### Tier 2 Numbers

Across `sanrio mouse pad`, `cute mouse pad`, `cute desk mat`, `kawaii mouse pad`, `kawaii desk mat`:
- Combined market volume: ~3,500-4,500/mo
- Brand impression share: ~1-3% (varies by query)
- Brand purchases: low single digits per month per query, mostly converting at industry parity or slightly above
- The brand sometimes spikes higher CTR (e.g., 7.5% on `anime desk mat` in April 2025) but the click volume is too small to draw conclusions

The wider audience here (cute, kawaii, sanrio) is where Kuromi would resonate but the brand is invisible. Tier 2 is the **primary growth lever for this product**.

### Tier 3 Numbers

`anime mouse pad`, `anime desk mat`, `gothic mouse pad`:
- Combined market volume: ~5,000-6,000/mo (mostly anime mouse pad at ~4,500/mo)
- Brand impression share: 0.3% to 1.5%
- Volume is large but the audience is broader; Kuromi is one option among many anime characters

Tier 3 is a brand-awareness lever for Q4 only, similar to T3 on the wand pen.

### Blockers and Growth Path

| Tier | Imp Share | Brand vs Industry CTR | Brand vs Industry CVR | Primary Blocker | Growth Path |
|---|---|---|---|---|---|
| Tier 1 | 6.44% (of ~8-9% cap) | 10.43% vs 1.94% (+5.4x) | 16.96% vs 8.86% (+91%) | At cap | Lock and defend. Very little headroom. |
| Tier 2 | 1-3% (of ~8-18% cap) | varied, often above industry | varied, mixed | Impression Share | Big visibility gap. Bid on sanrio/kawaii/cute terms. |
| Tier 3 | 0.3-1.5% (of ~8-9% cap) | mostly above industry | low volume to assess | Impression Share + audience drift | Q4 awareness play, secondary priority. |

**Tier 1 is essentially maxed.** Brand impression share at 6.44% on a ~8-9% cap means there's little PPC headroom for growth on Tier 1. The product is winning.

**Tier 2 is the unlock.** This is where Kuromi's audience lives at much larger scale. The brand is barely visible (1-3% imp share on a 8-18% cap), but where it does show up, it converts above or near industry.

## Ad Analysis (Kuromi-Specific)

From the wand-pen audit Q726 data, the Kuromi desk mat (B0D9KXKW29) campaigns currently running:

| Campaign | Spend (90d) | Sales | ROAS | Clicks | Orders | CVR |
|---|---|---|---|---|---|---|
| B0D9KXKW29 \| SP\|M\|Br \| kuromi mouse pad \| DO | £49 | £211 | **4.29** | 96 | 17 | 17.7% |
| Desk Pads & Blotters B0D9KXKW29 - kuromi desk mat | £17 | £88 | **5.19** | 39 | 6 | 15.4% |
| Pencil Cases B0D9KXSGRM - kuromi gifts | small | small | small | small | small | n/a |

**Total Kuromi desk mat ad spend ~£70 over 90 days.** ~£25/month on the second-biggest variant in P1, the strongest funnel-conversion product in the entire account.

The brand-name campaign on `kuromi mouse pad` runs at 4.29 ROAS but only £49 of spend. The desk mat name variant runs at 5.19 ROAS on £17. Both are starved.

**Search term in the master Q719 data showed:**
- `kuromi` (broad search): £160 spend, ROAS 1.03, 132 clicks, 13 orders. Mostly going to other Kuromi products in the catalog at low ROAS, not the mouse pad specifically.

### Findings

> **Finding: The Kuromi mouse pad campaign is starved despite winning Tier 1 outright.**
>
> **Problem:** £66 over 90 days on the two campaigns that matter (kuromi mouse pad + kuromi desk mat). Tier 1 imp share is 6.44% (near 8-9% cap), and ROAS on the dedicated campaigns is 4-5x. There is no clear headroom to scale further within Tier 1, but the budget is so small that the brand is losing easy daily incremental sales. £66/90d = 73p per day across both campaigns.
>
> **Solution:** Push these two campaigns to £4-5/day each (~£300/90d combined). Expected to maintain ROAS in 3-5 range. This is a defend-the-fortress action, not a moonshot.
>
> **Impact:** Conservatively, +£250 / 90d in incremental sales, ~£1K annualized.

> **Finding: Tier 2 (Sanrio / cute / kawaii) is the unexplored growth lever.**
>
> **Problem:** The Kuromi desk mat is structurally a strong fit for `sanrio mouse pad`, `cute mouse pad`, `kawaii mouse pad`, `cute desk mat`, `kawaii desk mat`. Combined volume is ~3,500-4,500/mo. Brand has 1-3% impression share. Where the brand has shown up, CTR is above industry. There is no dedicated PPC campaign on these terms today. The "kuromi" broad campaign at £160 spend is hitting these terms incidentally at 1.03 ROAS, suggesting low quality match.
>
> **Solution:** Stand up dedicated Phrase or Exact campaigns on Tier 2 terms. Start at £8-10/day, observe CTR and ROAS for 30 days, scale or kill based on data.
>
> **Impact:** If Tier 2 brand impression share reaches 6% (against ~16% cap), and brand purchase share follows the Tier 1 pattern of out-converting industry, this could 2-3x the Kuromi mat's revenue. This is a hypothesis, not a guaranteed outcome.

> **Finding: Kuromi desk mat buy box is 78.7% in the latest window, lowest among top 3 desk mat children.**
>
> **Problem:** Other top children sit at 92-99% buy box. Kuromi at 78.7% is dragging down both organic conversion and ad efficiency. Most likely cause on a private-label-style listing: MAP price changes triggering buy box suppression.
>
> **Solution:** Same as P3 (Cauldron Mug). Diagnose at the offer level. Check for price changes in the last 60 days that could have triggered the suppression.
>
> **Impact:** A 78.7% -> 95%+ recovery on the £1,500/2-mo product would lift sales by ~20%. ~£300/2-mo, £1,800/year, plus the ad efficiency gain on the £66 currently being spent.

## Recommendations Added to Action Plan

These are additions to Section 6 of the main audit, not replacements.

### Weeks 1-2 (Immediate)
- Increase the two existing Kuromi campaign budgets (kuromi mouse pad + kuromi desk mat) from £0.73/day combined to £8-10/day combined.
- Diagnose Kuromi buy box (78.7%): check pricing history and offer-level data for the last 60 days.

### Weeks 2-4 (Short-Term)
- Stand up Tier 2 campaigns on `sanrio mouse pad`, `cute mouse pad`, `kawaii mouse pad`, `cute desk mat`, `kawaii desk mat` at £8-10/day each.
- Begin listing review on the Kuromi child (B0D9KXKW29). Same template fixes as the wand pen if applicable.

### Weeks 4-6 (Medium-Term)
- Mine Tier 2 campaign search terms after 30 days. Promote winners into dedicated Phrase / Exact campaigns.
- Launch dedicated campaigns on the next two desk mat winners: Transformers (B0D2S5HZK8, £795 in 2 months at 99.4% buy box) and Snoopy Jumbo (B0FWS1HV16, £675 in March alone). Same Tier 1 / Tier 2 template.

### Weeks 6-8 (Scale and Evaluate)
- Q4 readiness for the desk mat parent: Kuromi, Transformers, Snoopy, SpongeBob are likely Q4 gift drivers. Inventory plan and PPC ramp on each.
- Phase out or pause Emily in Paris desk mat (B0CP5TMLS3) - £24 in 2 months on 284 sessions is dead.

## Insights

- **The Kuromi mouse pad has the strongest funnel performance in the entire audit, including the wand pen.** 66% purchase share, 10.4% brand CTR vs 1.9% industry. The product is winning at category-leader scale on its hero query.
- **Within the desk mat parent, the IP rankings don't follow brand intuition.** Kuromi (Sanrio gothic) and Transformers outperform every Harry Potter variant. The catalog winner is determined by which IP's audience overlaps best with the desk-mat purchase intent (gamer-adjacent + cute aesthetic), not by which IP is generally most popular.
- **Emily in Paris is dead.** £24 / 2 months on 284 sessions. Consider phasing.
- **Snoopy Jumbo Desk Mat went 0 -> £675 in one month.** Worth flagging in next audit cycle. Either a successful launch or an organic algorithmic shift on Snoopy queries.

## Questions for the Seller

- **Kuromi buy box at 78.7%:** Same MAP-style diagnostic as the cauldron mug. Recent price changes?
- **Snoopy Jumbo Desk Mat sudden ramp:** Did the seller do anything specific in March (relisted, paid review push, new Brand Story)? If yes, that playbook may apply to other under-performing IP variants.
- **IP licensing portfolio for desk mat:** Are there other IPs the brand has the rights to launch as a desk mat (Bluey, Pokemon, Stranger Things, Marvel)? "pokemon desk mat" gets ~500/mo with no brand presence; an opportunity if licensed.
