# Food Earth — Ad Analysis

## Analysis Window

Feb 15 - May 14, 2026 (89 days, matching the ad data window). All currently enabled campaigns.

## Account Summary

- 8 enabled campaigns
- Total spend: $7,621 | Total ad sales: $7,810 | Blended ROAS: **1.02** | TACoS: ~30% of Apr revenue
- Only 1 of 8 campaigns is profitable (above 1.5x ROAS): SPA Simmer Coconut VP at 1.76 ROAS

This audit confirms the seller's call observation: "to get $10K in sales we're spending $6K in ads." The actual blended ROAS is barely 1.0, which means ad cost equals ad sales before product cost is even subtracted. Every ad dollar is currently destroying margin.

---

## Account Level

### Campaign Structure

**Finding: Two manual campaigns are massively overstuffed, starving high-ROAS keywords of budget.**

| Campaign | Target Count | Spend | ROAS |
|----------|--------------|-------|------|
| EcomC - Ramadan - Manual - Noodles | **30** | $576 | 0.67 |
| EcomC - Manual - Dips, Simmer, Soup | **25** | $1,456 | 0.96 |
| SPM - Meals - Hero Master VP (P0) | 9 | $1,197 | 1.20 |
| All other manual campaigns | 1-4 | varies | varies |

**Problem:**

Inside the 25-target Dips/Simmer/Soup campaign, a single keyword ("soup" PHRASE) absorbs $705 (48% of campaign spend) at ROAS 1.04. Meanwhile, "organic lentil soup" PHRASE has ROAS 4.63 from just $15.53 of spend — a 4.5x return that the structure prevents from scaling. Same pattern in the 30-target Noodles campaign: "noodle" PHRASE eats $368 (64% of spend), with most other targets at $0-$2.

This is classic budget starvation. Amazon's algorithm picks 1-2 winners and starves the rest, regardless of their potential. The high-ROAS keywords never get a chance to compound.

**Solution:**

- Break out the proven high-ROAS keywords ("organic lentil soup", "soups fresh ready to eat", "indian ready to eat meals" — see Product Level below) into their own dedicated campaigns with 3-5 keywords each.
- Cap each new campaign at a meaningful daily budget so the keyword actually gets spend.
- Negate the harvested keywords from the original parent campaigns to prevent overlap.

**Impact:**

Take "organic lentil soup" as one example. At its current ROAS of 4.63, $200 of spend would yield ~$926 in sales (vs the $80 it generates today at $15.53 spend). The same shift applied to 3-4 starved-but-proven keywords across the 2 overstuffed campaigns could net $1,500-$2,500 of incremental monthly sales without any new spend.

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|--------|-------|-------|------|-----|-----|-----|
| Automatic | 3,423 | $4,390 | $4,590 | **1.05** | $25.22 | $1.28 | **5.32%** |
| Manual | 2,737 | $3,230 | $3,218 | 1.00 | $28.99 | $1.18 | 4.06% |

**Problem: Auto is outperforming Manual on every conversion metric.** Auto ROAS (1.05) > Manual ROAS (1.00). Auto CVR (5.32%) > Manual CVR (4.06%). Auto is also 58% of total ad spend.

This pattern is backwards. Auto is meant for discovery (smaller spend, lower ROAS), and Manual is where the proven winning search terms get scaled with controlled bids (larger spend, better ROAS). When Auto wins, it means Amazon's algorithm is finding better matches than the human-selected keywords in Manual. The harvest-and-scale loop is broken.

**Solution:** Mine the Auto campaign search terms, identify the top converters (the Q719 data already surfaces some: "indian food", "indian food ready to eat", "coconut curry sauce"), and migrate them into dedicated Manual exact-match campaigns with proper bids. Negate those terms from Auto to prevent duplication and budget conflict.

**Impact:** The current $3,230 of Manual spend at ROAS 1.00 is essentially break-even on ad cost (still loss-making after product cost). Lifting Manual ROAS to where Auto currently sits (1.05) would add ~$160/month in net sales at the same spend. Lifting Manual to a properly-managed 1.5x ROAS (still modest) would unlock ~$1,610/month in incremental sales.

### Campaign Profitability

| Campaign | Spend | Sales | ROAS | Status |
|----------|-------|-------|------|--------|
| EcomC - Ramadan - Auto - Noodles | $1,147 | $423 | **0.37** | Burning $724 |
| EcomC - Ramadan - Manual - Noodles | $576 | $387 | 0.67 | Burning $189 |
| SPA - Dip - Hero Desi Fiery, Chilli garlic combo | $162 | $138 | 0.85 | Burning $24 |
| EcomC - Auto - All Top rat Listings | $396 | $317 | 0.80 | Burning $79 |
| EcomC - Manual - Dips, Simmer, Soup | $1,456 | $1,398 | 0.96 | Break-even |
| SPA - Meals - Hero Master VP (P0) | $1,657 | $1,904 | 1.15 | Sub-threshold |
| SPM - Meals - Hero Master VP (P0) | $1,197 | $1,434 | 1.20 | Sub-threshold |
| SPA - Simmer - Hero - Coconut VP | $1,029 | $1,809 | **1.76** | Only profitable |

**Problem: 7 of 8 campaigns are below the 1.5x ROAS profitability threshold. The two Noodles campaigns alone burned $913 in net loss over 90 days.** The Noodle category received $1,723 of ad investment to deliver $810 in sales. That is 22.6% of total ad spend producing 10.4% of ad sales.

**Solution:**

- **Immediately pause both Noodles campaigns.** The Noodle product was launched in March, has not found product-market fit on Amazon (per Step 1, P3 had 147% TACoS), and is bleeding the account.
- Reallocate the freed $1,723 / 90 days (~$574/month) to the only proven profitable campaign: SPA Simmer Coconut VP (ROAS 1.76).

**Impact:**

$574/month of reallocated budget at 1.76 ROAS = $1,010 in additional monthly sales. Net swing vs the current Noodle loss: ~$574 saved + $1,010 new sales = **$1,584/month improvement** without adding any new ad budget.

### Targeting Strategy

**Keyword vs Product Targeting:**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|-------------------|--------|-------|-------|------|-----|-----|-----|
| Keyword Targeting | 5,065 | $6,005 (79%) | $6,032 | 1.00 | $26.93 | $1.19 | 4.42% |
| Product Targeting | 1,095 | $1,615 (21%) | $1,776 | **1.10** | $25.74 | $1.48 | **6.30%** |

**Match Type Breakdown:**

| Match Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|------------|--------|-------|-------|------|-----|-----|-----|
| PHRASE | 2,444 | $2,873 (93%) | $3,017 | 1.05 | $29.29 | $1.18 | 4.21% |
| EXACT | 174 | $224 (7%) | $171 | 0.76 | $24.42 | $1.29 | 4.02% |

**Two issues:**

1. **Product targeting under-funded:** Product targeting converts 43% better than keyword targeting (CVR 6.30% vs 4.42%) and has a better ROAS (1.10 vs 1.00), yet receives only 21% of the spend. This is the same defensive-ads play (Sponsored Product targeting on own ASINs and key competitor ASINs) that often produces the best returns. Worth scaling.
2. **EXACT match barely exists:** $224 in EXACT vs $2,873 in PHRASE (8% of keyword spend). EXACT should normally outperform PHRASE because it is the most precise targeting. Here it is underperforming (0.76 vs 1.05 ROAS), which means either the wrong keywords were picked for EXACT, or no proper harvest from PHRASE/Auto has happened. Combined with the Auto > Manual finding, this confirms the account is not running the standard discover-then-scale playbook.

### Placement

| Placement | Spend | Sales | ROAS | CTR | CVR |
|-----------|-------|-------|------|-----|-----|
| Top of Search | $3,893 (51%) | $2,743 | 0.70 | **2.71%** | 4.42% |
| Rest of Search | $1,817 (24%) | $1,383 | 0.76 | 0.74% | 3.85% |
| Product Pages | $1,605 (21%) | $861 | **0.54** | 0.30% | 2.89% |
| Off Amazon | $300 (4%) | $0 | **0.00** | 0.34% | 0.00% |

**Problem: Product Pages and Off Amazon are bleeding.**

- Product Pages ($1,605 spend) converts at 2.89% CVR and ROAS 0.54. This is the worst placement and absorbs 21% of budget. CTR is just 0.30% — meaning the listing doesn't compete well when shown alongside another product on a PDP.
- Off Amazon ($300) has produced zero sales in 90 days. Pure waste.
- Top of Search has the best CTR (2.71%) and tied-best CVR (4.42%), but at a high CPC ($1.58) the ROAS is only 0.70. It is the premium placement but expensive.

**Solution:**

- Disable Off Amazon placement entirely. $300 saved over 90 days, no sales lost.
- Reduce Product Pages bid modifier aggressively. Reallocate to Top of Search where the CTR is 9x better.
- Note: even Top of Search converts at 4.42% CVR, far below SQP industry CVR of ~20%. This confirms the issue is structural to the listing/rating (per Step 2), not the placement. PPC alone cannot fix this. Listing fixes from Step 2 must come first.

**Impact:** Eliminating Off Amazon + reducing Product Pages by 50% saves ~$1,100 / 90 days. Redirected to Top of Search at its current ROAS of 0.70 yields ~$770 sales. Net swing: roughly neutral on sales but eliminates clearly wasted spend, frees ~$370 / 90 days for better placements once listing CVR improves.

---

## Product Level (P0: Six Flavor Variety Pack)

### P0 Campaign Map

The "Ready to Eat Indian Cuisine Bundle (Pack of 6)" parent is advertised by 3 campaigns. **Within this parent, ~96% of ad spend goes to Vegetable Biryani (B086WPJGXQ), not the actual revenue-leader Six Flavor Variety Pack (B0D8Q9MMT9).**

| Campaign | Advertised Child | Spend | Sales | ROAS | Orders |
|----------|------------------|-------|-------|------|--------|
| SPA - Meals - Hero Master VP | Vegetable Biryani | $1,657 | $1,904 | 1.15 | 58 |
| SPM - Meals - Hero Master VP | Vegetable Biryani | $1,197 | $1,434 | 1.20 | 34 |
| EcomC - Auto - All Top rat Listings | Six Flavor Variety Pack | $107 | $174 | **1.62** | 5 |
| EcomC - Auto - All Top rat Listings | Vegetable Biryani | ~$30 | small | small | 1 |
| **Total P0** | | **~$2,991** | **~$3,512** | **1.17** | **98** |

Total P0 ad spend is ~$2,991 of the account's $7,621 (39%). Of that, $2,884 (96%) is on Vegetable Biryani at ROAS 1.15-1.20, and only $107 (4%) is on the Six Flavor Variety Pack at ROAS 1.62.

**This is the single largest misallocation in the account.** The Variety Pack is the higher-ROAS child, the higher-organic-revenue child (per Step 1, $5,333 / 3-mo vs Biryani's $4,017), and the natural entry product for new customers. It is functionally unsupported by PPC.

### Blocker Analysis

Step 3 identified that on Tier 1 queries ("indian food", "tasty bites indian food", "deep indian kitchen"), the primary blocker is a compound of **impression share (0.33% of ~16% cap) and CVR (5.13% vs industry 20.7%)**. The pattern from CLAUDE.md is "Low impression share + poor CVR" → fix CVR first, then scale impressions.

#### Impression Share Blocker: Keyword Spend vs Tier 1/2/3 Queries

Search term data for the Tier 1/2/3 keywords from Step 3:

| Search Term | Tier | Spend | Sales | ROAS | Clicks | Orders | CVR |
|-------------|------|-------|-------|------|--------|--------|-----|
| indian food | Tier 1 | $107 | $134 | **1.25** | 53 | 4 | 7.5% |
| indian food ready to eat | Tier 1 (close) | $62 | $62 | 1.00 | 25 | 2 | 8.0% |
| ready to eat meals | Tier 2 | $162 | $261 | **1.60** | 88 | 6 | 6.8% |
| soups fresh ready to eat | n/a (P2) | $54 | $131 | **2.42** | 32 | 4 | 12.5% |
| tasty bites / deep indian kitchen | Tier 1 | not visible | not visible | — | — | — | — |

**Finding: Tier 1 keywords are converting well (ROAS 1.0-1.6) but absurdly underfunded.**

> **Problem:** "indian food" — the highest-volume Tier 1 query for the variety pack — gets only $107 of 90-day spend and converts at a healthier CVR (7.5%) and ROAS (1.25) than the account average. "tasty bites indian food" and "deep indian kitchen" do not appear at all in the customer search terms, meaning the brand likely is not bidding on competitor-brand terms.
>
> Meanwhile, the SPM Meals Hero VP campaign has a target called "meals" (PHRASE) that absorbs $1,083 of spend at ROAS 1.14 — broad and generic, captures non-Indian intent. The 30+ keyword "indian ready to eat meals" PHRASE target in the same campaign has ROAS **14.55** from $11.54 of spend (6 clicks, 4 orders) and is being starved.
>
> **Solution:**
> 1. Extract "indian ready to eat meals" into its own EXACT-match campaign with a $30/day budget and bid up. At a conservative scaled ROAS of 5 (assuming diminishing returns from the current 14.55), $900/month spend = $4,500/month in sales.
> 2. Launch new campaigns bidding on: "indian food", "tasty bites indian food", "deep indian kitchen", "tasty bites", "indian variety pack", "indian meals". These are direct-intent Tier 1 keywords with zero or near-zero current spend.
> 3. Reallocate budget from the broad "meals" PHRASE target (which captures non-Indian intent and converts at industry-average rates) toward Indian-specific terms.
>
> **Impact:** Even at conservative ROAS of 2.0 across new Tier 1 keywords, an additional $500/month in spend on these keywords would add ~$1,000 in monthly sales. The bigger impact comes once listing CVR is improved (per Step 2): the same Tier 1 spend would scale 3-4x.

#### CVR Blocker: Wasted Targeting & Misallocated Spend

Within P0 specifically:

> **Problem:** The P0 budget is concentrated on the wrong child ASIN. $2,884 of the $2,991 P0 spend (96%) advertises Vegetable Biryani, even though the Six Flavor Variety Pack:
> - Has higher organic revenue ($5,333 vs $4,017 / 3-mo, per Step 1)
> - Has higher ad ROAS in the limited spend it does receive (1.62 vs 1.15-1.20)
> - Has near-100% buy box (97.6% vs 95-98% for Biryani)
> - Is the natural entry SKU for first-time buyers ("try a sample of everything before committing")
>
> The Variety Pack should be the hero ad target. The current allocation appears to be inherited from how the campaign was originally set up, not from a data-driven decision.
>
> **Solution:**
> 1. Launch a dedicated Sponsored Products campaign for B0D8Q9MMT9 (Variety Pack) with Indian-themed keywords (from the impression share section above).
> 2. Reduce the budget on the existing Vegetable Biryani-only campaigns (SPA/SPM Meals Hero VP) by 30-50%, redirecting that spend to the Variety Pack campaign.
> 3. Add Sponsored Display product targeting on the Variety Pack's own listing (defensive ads), and on top competitor ASINs (Tasty Bite Variety Pack, Maya Kaimal Everyday Dal Variety, Kitchens of India Dinner Variety).
>
> **Impact:** Shifting $800/month of spend from Biryani campaigns (ROAS 1.18) to a properly-targeted Variety Pack campaign (assuming 1.5 ROAS at scale, based on current 1.62 small-sample): swap of $944 → $1,200 in monthly sales = $256 incremental monthly sales. The bigger value is positioning the actual hero product as the brand's ad-supported hero, which compounds organically over months.

---

## Insights

- **P0's $2,991 in 90-day ad spend is 96% allocated to the wrong child ASIN.** The Variety Pack is the natural hero — higher revenue, higher ROAS, healthier buy box — but receives 4% of P0 ad support. This is the single most impactful reallocation in the account.
- **The brand's most promising Tier 1 keyword is being starved by overstuffed campaign structure.** "indian ready to eat meals" PHRASE target has ROAS 14.55 on $11.54 of spend, trapped in a 9-target campaign where the broad "meals" PHRASE eats $1,083.
- **22.6% of ad spend goes to a product that has no product-market fit yet.** Noodle campaigns burned $913 net over 90 days. Pausing them and redirecting to the only profitable campaign (SPA Simmer Coconut VP at 1.76 ROAS) is a guaranteed ~$1,500/month improvement.
- **The account is running the discovery playbook backwards.** Auto outperforms Manual, PHRASE outperforms EXACT, and high-ROAS keywords inside Auto/PHRASE have never been harvested into dedicated EXACT campaigns. The agency has not run the standard scale-what-works loop.
- **CVR ceiling cannot be solved with PPC alone.** Even on the best placement (Top of Search), the brand converts at 4.42% CVR vs SQP industry's 20.7%. The 4x gap is structural: rating (3.7 stars vs comp 4.2-4.5), wasted image slot #2, no video, weak A+ comparison. Listing fixes from Step 2 must precede any aggressive PPC scaling.

## Things to Investigate Further

- **Is the Noodle product permanently unprofitable or just early-stage?** A 3-month launch window with TACoS 147% should not be extended further without a major repositioning. Confirm with the seller whether this is a deliberate runway investment or whether the agency just kept the campaigns running.
- **Why are EXACT keywords underperforming PHRASE?** Likely the wrong terms were placed in EXACT. The fix is to seed EXACT campaigns from the proven Auto/PHRASE winners (notably "indian food", "ready to eat meals", "soups fresh ready to eat", "coconut curry sauce").

## Questions for the Seller

- Was the decision to put 96% of the Ready-to-Eat Bundle ad budget on Vegetable Biryani (vs the Six Flavor Variety Pack) intentional, or did the agency default to it because it was the top-converting child during a historical period?
- The 30-target Noodles campaign and 25-target Dips/Simmer/Soup campaign are stuffed beyond what is manageable. Did your agency design them this way, or were keywords added over time without restructuring? This directly causes the budget-starvation problems we identified.
- The Noodle product launched in March, has burned $913 net in 90 days, and accounts for 22.6% of ad budget. Is this a runway you have a defined cutoff for, or has it been on autopilot?
