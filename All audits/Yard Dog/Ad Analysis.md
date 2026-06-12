# Ad Analysis - YARDDOG

**Analysis period:** Dec 29, 2025 - Mar 15, 2026 (full ad data range)
**Total account ad spend:** $1,959.80 | **Total ad sales:** $5,631.52 | **Account ROAS:** 2.87

---

## Account Level

### Campaign Structure

5 campaigns total (within the visible ad data window, Dec 29 - Mar 15). The structure is simple but has issues.

| Campaign | Type | Targets | Active Targets | Spend | Sales | ROAS |
|----------|------|---------|---------------|-------|-------|------|
| SP - Auto Catch All | Auto | 2 | 2 | $737.79 | $2,047.15 | 2.77 |
| SP - KW - Broad - B0DSWJJY9C (2-Pack) | Manual Broad | 10 | 1 | $589.01 | $2,102.46 | 3.57 |
| SP - STR - KW - Exact - B0DSWMVBSZ (Black) | Manual Exact | 10 | 5 | $395.95 | $785.92 | 1.98 |
| SP - KW - Broad - B08LQWY8V4 (Silver) | Manual Broad | 9 | 3 | $170.07 | $454.19 | 2.67 |
| SP - ASIN - SELF - B08LQWY8V4 | Manual Product | 2 | 1 | $66.98 | $241.80 | 3.61 |

**Finding: Exact campaign is the weakest performer and has a bleeding keyword**

**Problem:**
- The exact campaign (Black 1 Pack) has 1.98 ROAS (50% ACoS), near break-even. The root cause is one keyword: "mole scissor trap" on exact match is spending $166.82 with only $94.47 in sales (0.57 ROAS). This single keyword accounts for 42% of the campaign's spend but delivers almost no return.
- Meanwhile, "mole traps that work best" in the same campaign has $6.00 spend, $81.24 sales, 13.54 ROAS. It's being starved of budget.

**Solution:**
- Pause or significantly reduce bid on "mole scissor trap" exact. Despite being a Tier 1 keyword, the brand's 3.8-star rating and higher price point make it uncompetitive on this specific high-intent query where shoppers compare scissor trap options directly.
- Increase bids on "mole killer" (3.57 ROAS) and "mole traps that work best" (13.54 ROAS) to capture more of their volume.

**Impact:**
- Redirecting the $166.82 from "mole scissor trap" to "mole killer" at its current 3.57 ROAS would generate ~$596 in sales vs the current $94.47. Net gain: ~$500 in additional sales from the same spend.

**Also notable:** The Broad 2-Pack campaign (B0DSWJJY9C) has 10 targets but only "mole traps" is spending ($580.97 of $589.01). The other 9 keywords are at $0-$3.45. This isn't necessarily a problem since the dominant keyword is performing well (3.55 ROAS), but it means the other keywords (including "mole scissor trap", "mole eliminator trap") are getting zero budget allocation despite being in the campaign.

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|--------|-------|-------|------|-----|-----|-----|
| Automatic | 488 | $737.79 | $2,047.15 | 2.77 | $23.53 | $1.51 | 17.83% |
| Manual | 736 | $1,222.01 | $3,584.37 | 2.93 | $31.72 | $1.66 | 15.35% |

Auto vs Manual split is reasonable. Manual drives 62% of spend at slightly better ROAS (2.93 vs 2.77). Auto has better CVR (17.83% vs 15.35%) and lower CPC ($1.51 vs $1.66), suggesting the auto algorithm is finding converting traffic that could be harvested into manual campaigns. The lower AOV on auto ($23.53 vs $31.72) indicates auto is driving more single-pack sales while manual is driving more 2-pack sales.

### Campaign Profitability

All campaigns are above the 1.5x ROAS break-even threshold except the exact campaign which is borderline at 1.98x. No campaigns need to be paused, but the exact campaign needs the "mole scissor trap" keyword fixed (covered above in Campaign Structure).

### Targeting Strategy

**Keyword vs Product Targeting:**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|-------------------|--------|-------|-------|------|-----|-----|-----|
| Keyword Targeting | 1,183 | $1,892.82 | $5,389.72 | 2.85 | $28.37 | $1.60 | 16.06% |
| Product Targeting | 41 | $66.98 | $241.80 | 3.61 | $24.18 | $1.63 | 24.39% |

Product targeting outperforms keyword targeting significantly (3.61 vs 2.85 ROAS, 24.39% vs 16.06% CVR) but gets only 3.4% of total spend. There is only one ASIN targeting campaign (self-targeting the Plunger trap, B08LQYJXRW). This is an opportunity to scale. Defensive ASIN targeting on the brand's own listings and competitor ASIN targeting would likely perform well given the strong product targeting CVR.

**Match Type Breakdown:**

| Match Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|------------|--------|-------|-------|------|-----|-----|-----|
| BROAD | 431 | $759.08 | $2,556.65 | 3.37 | $36.01 | $1.76 | 16.47% |
| EXACT | 264 | $395.95 | $785.92 | 1.98 | $24.56 | $1.50 | 12.12% |

No PHRASE match campaigns exist. Broad significantly outperforms exact (3.37 vs 1.98 ROAS), which is an inverted pattern. Normally exact should be the highest ROAS because it's the most targeted. The inversion here is caused by the "mole scissor trap" exact keyword dragging down the entire exact match performance (0.57 ROAS on $166.82 spend). Fix that keyword, and exact match ROAS would improve to ~3.0.

---

## Product Level (P0: Mole Scissor Trap)

### P0 Campaign Map

| Campaign | ASIN | Spend | Sales | ROAS | Clicks | Orders |
|----------|------|-------|-------|------|--------|--------|
| SP - KW - Broad - B0DSWJJY9C (2-Pack) | Silver 2 Pack | $589.01 | $2,102.46 | 3.57 | 298 | 55 |
| SP - STR - KW - Exact - B0DSWMVBSZ (Black) | Black 1 Pack | $395.95 | $785.92 | 1.98 | 264 | 32 |
| SP - KW - Broad - B08LQWY8V4 (Silver) | Silver 1 Pack | $170.07 | $454.19 | 2.67 | 133 | 16 |
| Auto (Black 1 Pack) | Black 1 Pack | $110.89 | $421.05 | 3.80 | 72 | 19 |
| SP - ASIN - SELF - B08LQWY8V4 | Silver 1 Pack | $66.98 | $241.80 | 3.61 | 41 | 10 |
| Auto (Silver 1 Pack) | Silver 1 Pack | $50.31 | $230.42 | 4.58 | 34 | 8 |
| Auto (Silver 2 Pack) | Silver 2 Pack | $6.65 | $37.50 | 5.64 | 5 | 1 |
| **P0 Total** | | **$1,389.86** | **$4,273.34** | **3.08** | **847** | **141** |

P0 captures 70.9% of total ad spend ($1,389.86 of $1,959.80). The remaining 29.1% goes to P1 (Plunger Bite-Spike) via the auto campaign.

The Silver 2 Pack (the seller's focus product) is performing best among manual campaigns at 3.57 ROAS, validating the strategy of prioritizing this child.

### Impression Share Blocker: Keyword Spend vs. Tier 1/2 Queries

Section 4 (SQP) identified impression share as the primary blocker on Tier 1 (2.9% of ~8-9% max) and Tier 2 (1.3% of ~8-9% max). The PPC lever is bidding on the keywords where impression share is low. Here is what the ad data shows for the key search terms:

**Tier 1 Keywords:**

| Search Term | Spend | Sales | ROAS | Clicks | Orders | CVR |
|-------------|-------|-------|------|--------|--------|-----|
| mole trap | $283.38 | $801.78 | 2.83 | 194 | 33 | 17.0% |
| mole scissor trap | $116.54 | $75.00 | 0.64 | 68 | 2 | 2.9% |
| mole traps | $86.19 | $95.94 | 1.11 | 59 | 4 | 6.8% |
| scissor mole trap | $24.55 | $58.99 | 2.40 | 13 | 2 | 15.4% |
| mole traps for lawns | $14.99 | $21.77 | 1.45 | 13 | 1 | 7.7% |

**Tier 2 Keywords:**

| Search Term | Spend | Sales | ROAS | Clicks | Orders | CVR |
|-------------|-------|-------|------|--------|--------|-----|
| mole killer | $128.59 | $378.01 | 2.94 | 76 | 14 | 18.4% |
| mole traps that kill best | $28.93 | $31.98 | 1.11 | 21 | 2 | 9.5% |
| mole eliminator trap | $27.75 | $31.98 | 1.15 | 15 | 1 | 6.7% |
| mole traps that work best | $10.87 | $43.26 | 3.98 | 6 | 2 | 33.3% |
| mole traps scissor | $13.16 | $37.50 | 2.85 | 7 | 1 | 14.3% |
| scissor traps for moles | $8.09 | $37.50 | 4.64 | 5 | 1 | 20.0% |
| mole trap scissor 2 pack | $7.15 | $19.97 | 2.79 | 4 | 1 | 25.0% |

**Key observations:**

- "mole trap" (the hero keyword) is getting the most spend at $283.38 with healthy 2.83 ROAS. This is working and should be scaled further.
- "mole scissor trap" is a major problem: $116.54 spend at 0.64 ROAS with only 2.9% CVR. 68 clicks, 2 orders. This is enough data to be statistically meaningful. The keyword is consistently underperforming and should be paused or bid reduced dramatically. The hypothesis: when someone searches "mole scissor trap" specifically, they are comparing scissor trap options side by side, and YARDDOG's 3.8 rating loses against higher-rated competitors like Polaflex.
- "mole traps" is also underperforming at 1.11 ROAS. With 59 clicks and 4 orders, the 6.8% CVR is well below the account average.
- "mole killer" is the strongest Tier 2 performer at 2.94 ROAS and 18.4% CVR. This keyword is converting well and has room to scale.
- Several long-tail Tier 2 keywords ("mole traps that work best", "scissor traps for moles", "mole trap scissor 2 pack") show strong ROAS (3-5x) but are getting minimal spend ($7-11 each). These should be isolated into dedicated campaigns to get proper budget allocation.

**Branded search terms** ("yard dog mole trap" $50.45 at 9.75 ROAS, "yarddog mole trap" $29.36 at 9.27 ROAS) are performing well at $79.81 combined spend, which is 4.1% of total ad spend. This is within the acceptable range for branded defense.

**Competitor conquest terms** ("polaflex mole traps" $13.88, 0 orders; "wiretek mole trap" $11.08, 2 orders at 6.77 ROAS). Polaflex conquest is wasted, but Wire Tek conquest is working. The Wire Tek conquest spend is small enough to be noise, but it's a signal that customers comparing Wire Tek consider YARDDOG a viable alternative.

### CTR/CVR Blocker: Placement Distribution

Section 4 (SQP) identified CTR and ATC rate as secondary blockers. The PPC lever is better placements (Top of Search has higher CTR and conversion). Here is the placement breakdown:

| Placement | Spend | Sales | ROAS | CTR | CVR | Spend % |
|-----------|-------|-------|------|-----|-----|---------|
| Top of Search | $637.41 | $2,824.03 | 4.43 | 5.29% | 26.35% | 32.5% |
| Rest of Search | $689.91 | $2,001.70 | 2.90 | 1.58% | 16.87% | 35.2% |
| Product Pages | $632.00 | $805.79 | 1.27 | 0.42% | 7.46% | 32.3% |

**Finding: Product Pages placement is bleeding money**

**Problem:**
- $632.00 (32.3% of total spend) is going to Product Pages at 1.27 ROAS, below the 1.5x break-even threshold. Product Pages has the worst CTR (0.42%) and worst CVR (7.46%) by far.
- Meanwhile, Top of Search delivers 4.43 ROAS with 5.29% CTR and 26.35% CVR but only gets 32.5% of spend.

**Solution:**
- Increase Top of Search bid modifiers across all campaigns to shift more spend to the premium placement.
- Consider reducing bids on Product Page placements or using placement-level bid adjustments to decrease exposure there.

**Impact:**
- If just half of the Product Pages spend ($316) were redirected to Top of Search at its current 4.43 ROAS, it would generate ~$1,400 in additional sales vs the ~$402 currently generated by that spend on Product Pages.
- Net improvement: ~$1,000 in additional sales from the same ad budget.

---

## Insights

- P0 (Mole Scissor Trap) ad spend is concentrated on the right product (70.9% of total spend), and the best-performing campaign is the Silver 2 Pack broad campaign at 3.57 ROAS, which aligns with the seller's strategic focus.
- The single biggest waste is "mole scissor trap" on exact match: $116.54 at 0.64 ROAS. Pausing this keyword and fixing the placement distribution (away from Product Pages) would recover ~$280 in wasted spend and generate significantly more revenue from the reallocation.
- Top of Search placement is the clear winner (4.43 ROAS vs 1.27 on Product Pages). The brand converts exceptionally well when it appears at the top of search results, which is consistent with the SQP finding that CVR is close to industry when the product is properly positioned. The issue is visibility and placement, not the product itself.
- The account has no PHRASE match campaigns. Adding phrase match for the strongest converting terms would capture long-tail variations that broad currently catches but with more control than broad provides.

## Things to Investigate Further

- The "mole scissor trap" exact keyword has 2.9% CVR vs the account average of ~16%. This is a specific keyword-level issue, not a general conversion problem. Review the actual search term report for "mole scissor trap" to confirm that the search term matches exactly and isn't triggering on irrelevant variations.

## Questions for the Seller

- The ad campaigns were set up by an agency (tagged "MAG" in campaign names). Is MAG still managing the ads, or is this something the seller is managing themselves? This affects how we frame the optimization recommendations.
