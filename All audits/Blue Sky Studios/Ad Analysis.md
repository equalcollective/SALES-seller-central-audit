# Blue Sky Studios - Ad Analysis

## Data Window

90 days, 2026-01-29 to 2026-04-28. Note: ad data didn't exist before Jan 29 (Step 1 confirmed the seller began running ads on the wand only in Jan 2026). The full Q4 2025 selling peak ran with zero ads.

**Account totals (90-day window, all campaigns including currently paused):**
- Total spend: £7,032
- Total sales: £13,704
- Account ROAS: 1.95
- Currently-enabled spend: £3,611 (about half of historical 90-day spend has been on campaigns the seller has since paused)

## Account-Level Findings

### Campaign Structure

> **Finding: Account is fragmented into 422 single-keyword campaigns, with 92% having only one targeting line.**
>
> **Problem:**
> - 422 unique campaigns in the 90-day data, 142 currently enabled.
> - Median targets per campaign: 1. P90: 1. Mean: 1.6.
> - 389 of 422 campaigns have exactly one target. Only 13 have 5+ targets.
> - For P0 alone: 55 unique campaigns running. Many at £0-£4 spend, indicating campaigns created and abandoned.
> - This is the opposite of the usual overstuffed-campaign issue. Each keyword having its own campaign means each one fights for its own daily budget independently. With 142 active campaigns at a £25/day average account spend, the math says many campaigns are getting nothing.
>
> **Solution:**
> - Audit the 142 active campaigns. Pause every campaign with under £5 spend in 90 days that has no orders. These are clutter, not signal.
> - Consolidate the surviving campaigns into a clean Tier 1 / Tier 2 / Tier 3 structure on P0, with 3-5 keywords per Tier 1 campaign so budgets are dense enough to drive meaningful impressions.
> - For PT (Product Targeting) campaigns, the 19-36 ASIN targets per campaign in the existing PT lists are fine. The problem is keyword campaigns, not PT campaigns.
>
> **Impact:**
> - Hard to quantify directly. The mechanism is clarity: with 50 dormant or near-dormant campaigns out of the way, the seller can read account performance, and the campaigns left on the field can absorb the budget that comes in for Q4 2026.

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|---|---|---|---|---|---|---|---|
| Manual | 7,852 | £3,612 | £9,582 | 2.65 | £11.84 | £0.46 | 10.3% |
| Auto | very small (~£70 across all auto campaigns) | <£100 | trace | n/a | n/a | n/a | n/a |

> **Finding: There is no working Auto -> Manual harvest loop. Auto spend is ~1% of the account.**
>
> **Problem:**
> - Auto campaigns exist on the wand parent (Close Match, Substitute Match, Loose Match), but each is funded with £0-£53 over 90 days. There is no meaningful discovery happening.
> - Manual campaigns are running at 2.65 ROAS, which is healthy, but the brand is not feeding new keywords into the manual side from auto data.
> - Combined with the over-fragmented manual structure, this means new opportunities (long-tail variants, emerging gift queries) are not being captured systematically.
>
> **Solution:**
> - Stand up one well-funded Auto campaign per hero ASIN (P0 wand, P1 desk mat, P2 notebook & pen set). Budget around £15-25/day each.
> - Run them for 30-60 days, then mine the converted search terms and promote winners into dedicated Manual Phrase / Exact campaigns.
> - Negate the harvested terms from Auto so spend isn't duplicated.
>
> **Impact:**
> - This is the discovery engine that systematically expands the keyword list. At today's manual ROAS of 2.65, every new high-converting keyword harvested into manual at the same ROAS is incremental margin. Expect 5-15 harvested winners per hero ASIN per quarter at this volume.

### Campaign Profitability

Among 142 currently-enabled campaigns, 6 are running below 1.5x ROAS with 30+ clicks (the noise threshold for a real call):

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|---|---|---|---|---|---|
| SP/ M / Br / Harry Potter Gifts / DO / All Harry Products | £318 | £437 | 1.37 | 546 | 36 |
| SP_EX_B0D2S9BF2S - harry potter gifts | £61 | £82 | 1.36 | 128 | 6 |
| B0D2S9BF2S / SP/M/ Br / Harry potter self stirring mug / DO | £34 | £42 | 1.24 | 70 | 3 |
| SP_BR_wednesday gift_B0D14YZG5G_Wednesday Desk Tidy | £32 | £36 | 1.10 | 36 | 3 |
| Desk Lamps B0F9FQNK7V - snoopy gifts for women | £23 | £11 | 0.47 | 37 | 1 |
| B0F2JQCYK8/ SP / M / EX /harry potter pen / FB | £22 | £23 | 1.06 | 38 | 2 |
| **Total** | **£491** | **£632** | | | |

Below the 30-click threshold there are dozens more campaigns at 0.x ROAS, but the data is too thin to act on individually.

> **Finding: ~£500 of unprofitable spend across 6 campaigns over 90 days is small in absolute terms, but the issue is what it represents: lazy structural overlap.**
>
> **Problem:**
> - Three of the six unprofitable campaigns target some flavor of "harry potter gifts" (the all-Harry broad campaign, the cauldron mug exact campaign, and the cauldron mug brand campaign). The brand has a more profitable Triple Wand Pack "harry potter gifts" exact campaign running at 3.02 ROAS in parallel. These three are competing internally and losing to a sibling campaign.
> - The Snoopy gifts for women campaign at 0.47 ROAS is a clear "wrong product for the query intent" loss.
>
> **Solution:**
> - Pause all 6 unprofitable campaigns.
> - Reallocate the £491 to the existing high-ROAS campaigns identified below.
>
> **Impact:**
> - £491 reallocated to top P0 wand-pen-specific Phrase campaigns (current ROAS 5-10 on those) = roughly £2,500 in additional sales over the equivalent 90-day window. Annualized = £10K incremental sales.

### Targeting Strategy

**Keyword vs Product Targeting (90 days):**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|---|---|---|---|---|---|---|---|
| Keyword Targeting | 11,970 | £6,357 | £12,542 | 1.97 | £11.55 | £0.53 | 9.07% |
| Product Targeting | 1,448 | £675 | £1,162 | 1.72 | £13.51 | £0.47 | 5.94% |

Keyword is 90% of spend at slightly better ROAS. Product targeting is doing fine but small. No reallocation needed at the strategy level.

**Match Type Breakdown (90 days):**

| Match Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|---|---|---|---|---|---|---|---|
| EXACT | 4,459 | £3,122 | £5,849 | 1.87 | £10.97 | £0.70 | 11.95% |
| BROAD | 4,973 | £2,195 | £4,277 | 1.95 | £12.33 | £0.44 | 6.98% |
| PHRASE | 1,962 | £660 | £2,179 | 3.30 | £11.59 | £0.34 | 9.58% |

> **Finding: Phrase match is the highest-ROAS match type by far (3.30 vs 1.87 EXACT and 1.95 BROAD), but receives only 11% of keyword budget.**
>
> **Problem:**
> - Phrase ROAS at 3.30 is 76% better than Exact and 69% better than Broad.
> - Phrase has the lowest CPC (£0.34 vs £0.70 Exact), so each impression is cheaper as well.
> - The 11% spend allocation on Phrase suggests the seller is not leaning into it deliberately, even though the data has been consistently saying it works.
>
> **Solution:**
> - Move budget from underperforming Exact and Broad campaigns into expanded Phrase coverage on Tier 1 and Tier 2 SQP keywords.
> - Specifically: take the proven phrase performers (e.g. "harry potter wand pen" Phrase at 10.45 ROAS, "harry potter pen set" Phrase at 9.03 ROAS) and increase their daily budgets.
>
> **Impact:**
> - If the Phrase share of spend grows from 11% to 30% (£660 -> £2,100 over 90 days), and Phrase ROAS holds at 3.30, the incremental £1,440 spend would generate £4,750 sales vs £2,840 if it stayed in Exact/Broad at 1.9 ROAS. Net gain: ~£1,900 sales over 90 days.

### Placement Performance (Account)

| Placement | Spend | % of Spend | Sales | ROAS | CTR | CVR |
|---|---|---|---|---|---|---|
| Top of Search | £2,408 | 34% | £5,791 | 2.40 | 3.12% | 12.42% |
| Rest of Search | £3,032 | 43% | £6,577 | 2.17 | 0.77% | 8.91% |
| Product Pages | £1,589 | 23% | £1,348 | 0.85 | 0.25% | 3.57% |

> **Finding: Top of Search converts at 12.4% (3.5x Product Pages) and clicks at 3.12% (12x Product Pages), but only takes 34% of placement budget. Product Pages is unprofitable at 0.85 ROAS.**
>
> **Problem:**
> - The Top of Search placement is doing the heavy lifting on conversion. Product Pages is leaking £1,589 of spend at sub-1x ROAS.
> - The current Top of Search bid modifier is too low for the spread between TOS and Product Pages.
>
> **Solution:**
> - Increase Top of Search bid modifier to +50% to +100% on the top P0 campaigns. This pushes more spend into the placement that converts.
> - Reduce or zero out Product Pages bid modifier on Tier 1 wand-pen campaigns. For brand-defense and competitor-conquesting campaigns Product Pages remains useful, but the Tier 1 keyword campaigns should focus on Top of Search.
>
> **Impact:**
> - If Product Pages spend (£1,589 at 0.85 ROAS) shifts to Top of Search at 2.40 ROAS, the £1,589 generates £3,815 sales vs £1,348 today. Net gain: ~£2,500 sales over 90 days from same budget. Annualized: ~£10K.

## Product-Level Findings (P0)

### P0 Campaign Map

55 unique campaigns advertise the wand parent (B0FT54R9CP) over 90 days. Total: **£2,464 spend / £6,619 sales / 2.69 ROAS / 4,854 clicks / 571 orders**. P0 takes **35% of account ad spend** but **48% of account ad sales** (P0 is more efficient than the rest of the catalog).

Top 8 P0 campaigns:

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|---|---|---|---|---|---|
| B0F2JQCYK8 / SP / M / EX / harry potter gifts / FB (Triple Pack) | £729 | £2,199 | 3.02 | 1,201 | 192 |
| B0F9FRV1MM / SP / Phrase / SKW (harry potter) / DO (Quad Pack) | £498 | £1,711 | 3.43 | 1,679 | 145 |
| Ballpoint Pens B0F9FRV1MM - **harry potter lego** (PT) | £376 | £615 | **1.64** | 445 | 56 |
| B0F9FRV1MM / SP / M / Br / harry potter wand pen | £83 | £198 | 2.39 | 88 | 18 |
| Ballpoint Pens B0F9FRV1MM - harry potter (PT) | £85 | £77 | **0.90** | 83 | 7 |
| Collectible Props & Memorabilia B0F9FRV1MM - **harry potter wand that shoots fire** | £49 | £0 | **0.00** | 82 | 0 |
| Collectible Props & Memorabilia B0F9FRV1MM - harry potter wand pens | £46 | £211 | 4.55 | 84 | 18 |
| SP/M/ Br / wand Pen / DO / Harry Potter pen | £43 | £186 | 4.32 | 93 | 15 |

Below this, dozens of campaigns each with £0-£20 spend.

### Blocker-Specific Findings

#### Impression Share Blocker (Tier 1, Tier 2, Tier 3)

**Tier 1 Impression Share Blocker: PPC spend is starved on the wand-pen-specific keywords where the brand wins decisively.**

The SQP analysis (Section 4) identified Tier 1 impression share (11.19% of ~16-18% adjusted cap) as the primary blocker, with brand CTR 67% above industry and brand CVR 75% above industry. The PPC lever is to bid harder on Tier 1 keywords where the brand converts.

The actual ad data:

| Search Term | Tier | Spend (90d) | Sales | ROAS | Clicks | CVR |
|---|---|---|---|---|---|---|
| harry potter wand pen | T1 | £36 | £158 | 4.46 | 71 | 19.7% |
| harry potter wand pens | T1 | £22 | £132 | 6.00 | 36 | 33.3% |
| harry potter wand pen set | T1 | £4 | £52 | 13.03 | 10 | 40.0% |
| harry potter pens | T2 | £19 | £193 | 10.22 | 48 | 29.2% |
| harry potter pen | T2 | £28 | £166 | 5.88 | 70 | 18.6% |
| harry potter pen set | T1 | £7 | £22 | 3.15 | 9 | 22.2% |
| harry potter pens set | T1 | £12 | £61 | 5.05 | 20 | 30.0% |
| wand pen | T1 | £13 | £52 | 4.01 | 23 | 21.7% |
| harry potter levitating wand pen | T1 | £4 | £25 | 6.17 | 6 | 33.3% |
| **Tier 1 + Tier 2 wand-pen-specific subtotal** | | **~£170** | **~£900** | **~5.3** | **~310** | |

**Problem:** The brand spends £170 over 90 days (~2.4% of total ad budget) on the search terms where it converts at 5x ROAS. Meanwhile, £928 (13% of spend) goes to "harry potter gifts" at 2.19 ROAS, and £387 to "harry potter lego" at 1.76 ROAS. The capital allocation is upside-down.

**Solution:**
- Increase Tier 1 / Tier 2 wand-pen-specific keyword bids and budgets by 4-5x.
- Move the keywords currently buried in tiny fragmented campaigns (5-15 of them) into 2-3 well-funded Phrase + Exact campaigns at the Tier 1 level.
- Pull the existing Phrase campaign on "harry potter wand pen" (10.45 ROAS, £10 spend) up to £150-£250 daily budget and observe scaling efficiency.

**Impact:**
- Conservatively, scaling Tier 1 wand-pen-specific spend from £170 to £1,000 over 90 days at half the current ROAS (2.5x instead of 5.3x, accounting for diminishing returns) generates £2,500 in incremental sales. Annualized: ~£10K.
- The bigger prize is the Q4 lever. Tier 1 SQP search volume goes 1,130 -> 3,131 from March to December (3x). With Tier 1 campaigns properly funded going into Q4 2026, capturing an additional 5-7pp of impression share against a 3x larger demand pool would mean a materially bigger Q4 than Q4 2025's organic-only £53K.

> **Tier 3 Impression Share Blocker: 'harry potter gifts' is consuming 26% of ad spend and is doing fine, but it is not the right target for further scale.**
>
> The Tier 3 search "harry potter gifts" is the highest-volume term the brand bids on and gets £928 spend over 90 days at 2.19 ROAS. This is reasonable but not the lever to scale.
>
> The reason: SQP Section 4 showed Tier 3 has brand at industry parity on every funnel rate. The wand pen, mug, notebook, and other products all compete inside this query. Scaling Tier 3 on the wand alone is fine but the marginal gain is much smaller than scaling Tier 1 where the brand has dominant funnel performance.
>
> **Solution:** Hold Tier 3 spend roughly steady. Concentrate net-new budget on Tier 1, then scale Tier 3 deliberately starting September 2026 ahead of Q4 demand.

#### Wasted Spend on Intent Mismatch

**Finding: ~£600 over 90 days is going to wand-toy intent search terms where the wand pen is structurally not the answer.**

**Problem:**

| Search Term | Spend | Sales | ROAS | Orders |
|---|---|---|---|---|
| harry potter lego | £387 | £680 | 1.76 | 62 |
| harry potter | £201 | £286 | 1.42 | 28 |
| harry potter wand | £61 | £53 | 0.87 | 5 |
| harry potter wand that shoots fire | £19 | £0 | 0.00 | 0 |
| harry potter wand shoots fire | £16 | £12 | 0.73 | 1 |
| magic wand harry potter | £1 | £0 | 0.00 | 0 |
| harry potter fire wand | £2 | £0 | 0.00 | 0 |
| **Subtotal** | **£687** | **£1,031** | **1.50** | **96** |

The "harry potter lego" line is interesting: it's converting at 1.76 ROAS and 12.3% CVR. So shoppers searching for LEGO sets are actually buying the wand pen at modest rate, possibly as an add-on or impulse. But ROAS is below the 2.0 floor and well below the 5x available on wand-pen specific terms.

The fire-wand and "harry potter wand" generic queries are clearer: they convert poorly because customers want a toy/replica wand, not a pen.

**Solution:**
- Negate "fire wand", "shoots fire", "lego" (and variants) as exact-match negatives in the Quad Wand Pack and Triple Wand Pack campaigns.
- Keep the broad "harry potter" queries running but shift budget toward the specific Tier 1 keywords above.

**Impact:**
- £687 reallocated. At 50% redirected to Tier 1 (avg ROAS 5x): £344 -> £1,720 sales (vs £516 at current 1.5 ROAS). Net gain: ~£1,200 sales over 90 days.

#### Zero-Converting ASIN Search Terms

> **Finding: £137 over 90 days is being spent against raw ASIN strings (e.g., "b0f2jk7jr8", "b0716yvp6j") that produce no sales.**
>
> **Problem:** When customers search for ASINs directly, they are usually looking for a specific competitor product they have a link to. The wand pen showing in those search results doesn't lead to a sale.
>
> **Solution:** Add ASIN-format negative keywords (regex pattern: 10-char alphanumeric starting with B0). All Auto campaigns and Phrase/Broad campaigns should exclude these.
>
> **Impact:** Small in absolute terms (£137/90d = £550/year), but it's free money and a 30-second fix.

## Insights

- **The brand has a strong PPC product but a weak PPC operation.** The wand pen converts at 5-13x ROAS on its specific keywords. The data has been telling the seller this for 90 days, but spend is going to "harry potter gifts" generic, "harry potter lego" mismatch, and "harry potter wand" toy intent. Reallocating £1,000-£1,500 over 90 days from underperforming general queries to Tier 1 wand-pen-specific keywords is the highest-leverage action in the audit.
- **The Q4 ad lever is untouched.** P0 sold £53K organic in Nov+Dec 2025. With Tier 1 keywords properly funded and capacity in place, the Q4 2026 ceiling is materially higher. Time to test bid floors and campaign structure is now (off-season), not in October.
- **Phrase match is being underused at the structural level.** Account-wide, Phrase ROAS is 3.30 (76% above Exact). At 11% spend share, this is the most asymmetric allocation in the account. Lean in.

## Things to Investigate Further

- **Why is the seller's currently-active spend (£3.6K over 90d, ~£40/day) so low for a brand at £33K/month revenue?** Could be deliberate margin protection, could be cash-flow constraint, could be capacity for ad management. Worth asking on the call. A brand this efficient in PPC could absorb 3-5x today's daily spend at acceptable ROAS.
- **Catalog-level campaign hygiene.** 422 historical campaigns with only 13 having multiple keywords suggests an account that has accumulated a lot of campaign cruft. Worth a one-time cleanup in Weeks 1-2.

## Questions for the Seller

- **Ad budget posture for the next 6 months:** Is there a hard cap on monthly ad spend, or is the seller open to scaling proportional to ROAS? This shapes the Q4 plan materially.
- **Inventory readiness for Q4 2026:** P0 hit £35.9K in December alone with 3,069 units organic. With ads scaled, units could 1.5-3x. Is licensing (Warner Bros for HP) and inventory able to support that?
- **Campaign management cadence:** With 142 active campaigns and a manual-only structure, who is currently optimizing bids and harvesting search terms? If it's the seller themselves, the volume of manual work alone may be the binding constraint on PPC scale.
