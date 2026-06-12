# Ad Analysis: OneRADON

**Analysis period:** 2026-01-12 to 2026-04-10 (89 days)
**Total ad spend:** $811.20 | **Total ad sales:** $4,712 | **Account ROAS:** 5.81

## Account Level

### Campaign Structure

Two campaigns, both advertising P0 (Lüft Radon Monitor):

| Campaign | Targeting Type | Keywords | Spend | Sales | ROAS | Clicks | Orders |
|----------|---------------|----------|-------|-------|------|--------|--------|
| AD\|Luft\|Auto | Automatic | 4 auto targets | $448.02 | $4,036 | 9.01 | 328 | 23 |
| AD\|Luft\|Manual-Exact | Manual | 6 exact keywords | $363.18 | $676 | 1.86 | 138 | 4 |

The manual campaign has 6 keywords but only 2 are actually spending:

| Targeting | Match Type | Impressions | Clicks | Orders | Spend | Sales | ROAS |
|-----------|-----------|-------------|--------|--------|-------|-------|------|
| radon detector for home | EXACT | 45,589 | 109 | 2 | $326.73 | $338 | 1.03 |
| radon detector | EXACT | 2,821 | 17 | 0 | $24.13 | $0 | 0.00 |
| luft | EXACT | 343 | 12 | 2 | $12.32 | $338 | 27.44 |
| air quality monitor | EXACT | 153 | 0 | 0 | $0 | $0 | - |
| radon air detector | EXACT | 17 | 0 | 0 | $0 | $0 | - |
| indoor air quality meters | EXACT | 3 | 0 | 0 | $0 | $0 | - |

> **Finding: "radon detector for home" is consuming 90% of manual budget at break-even ROAS**
>
> **Problem:**
> - "radon detector for home" absorbed $326.73 of the $363.18 manual campaign budget (90%) with 109 clicks and only 2 orders at 1.03 ROAS
> - This keyword has a 1.83% CVR, far below the auto campaign's 7.01% CVR on the same product
> - The remaining keywords are budget-starved: "radon detector" got only $24 in spend, "air quality monitor" got zero clicks despite 153 impressions
>
> **Solution:**
> - Isolate "radon detector for home" into its own campaign with a lower bid. At $3.00 CPC and 1.83% CVR, the economics don't work for aggressive bidding on this term
> - Give "radon detector" and "air quality monitor" their own campaigns with dedicated budgets to test properly. 17 clicks is not enough to conclude "radon detector" doesn't convert
>
> **Impact:**
> - $326.73 currently generates $338 in sales (1.03 ROAS). Reallocating even half of this budget ($163) to the auto campaign at its 9.01 ROAS would generate $1,469 in additional sales

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|--------|-------|-------|------|-----|-----|-----|
| Automatic | 328 | $448.02 | $4,036 | 9.01 | $175.48 | $1.37 | 7.01% |
| Manual | 138 | $363.18 | $676 | 1.86 | $169.00 | $2.63 | 2.90% |

> **Finding: Auto massively outperforms manual, indicating the harvest-and-scale loop is broken**
>
> **Problem:**
> - Auto drives 85.7% of ad sales ($4,036 of $4,712) at 9.01 ROAS
> - Manual contributes only 14.3% of ad sales at 1.86 ROAS
> - Auto CPC is nearly half of manual ($1.37 vs $2.63), confirming the manual bids are too aggressive on underperforming keywords
>
> **What this tells us:** Amazon's algorithm is finding converting search terms in auto that have never been harvested and scaled into manual campaigns. The auto campaign is doing the heavy lifting that manual should be doing.
>
> **Solution:** Mine the auto campaign search terms (see search term analysis below), identify the top converters, and launch dedicated manual campaigns for them. Negate those terms from auto to avoid bid duplication.
>
> **Impact:** The auto campaign's top search terms are converting at 7%+ CVR. Moving them to manual campaigns with targeted bids would maintain performance while allowing precise budget control and scaling.

### Campaign Profitability

Both campaigns are above the 1.5x ROAS threshold at the campaign level, though the manual campaign (1.86 ROAS) is barely profitable. The targeting-level analysis above reveals the problem is within the manual campaign: "radon detector for home" is at 1.03 ROAS (below break-even), while the branded "luft" keyword (27.44 ROAS) pulls the campaign average up.

### Targeting Strategy

**Keyword vs Product Targeting:**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|-------------------|--------|-------|-------|------|-----|-----|-----|
| Keyword Targeting | 456 | $806.25 | $4,712 | 5.84 | $174.52 | $1.77 | 5.92% |
| Product Targeting | 10 | $4.95 | $0 | 0.00 | - | $0.50 | 0% |

Product targeting (substitutes in the auto campaign) has negligible spend ($4.95) and zero conversions. Not a concern, just not being used.

**Match Type Breakdown:**

| Match Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|------------|--------|-------|-------|------|-----|-----|-----|
| EXACT | 138 | $363.18 | $676 | 1.86 | $169 | $2.63 | 2.90% |

Only EXACT match is being used. There is no PHRASE or BROAD match testing. This means the brand is not discovering new keyword variations through manual campaigns at all. All keyword discovery is happening through the auto campaign.

## Product Level (P0)

### P0 Campaign Map

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| AD\|Luft\|Auto | $448.02 | $4,036 | 9.01 | 328 | 23 |
| AD\|Luft\|Manual-Exact | $363.18 | $676 | 1.86 | 138 | 4 |
| **Total P0** | **$811.20** | **$4,712** | **5.81** | **466** | **27** |

100% of ad spend goes to P0. No other products are being advertised.

### Impression Share Blocker: Keyword Spend vs. Tier 1 Queries

Section 4 (SQP) identified impression share as the primary blocker across all tiers. The brand has 0.014% impression share on Tier 1 queries (a $1.16M/month market). The PPC lever is bidding on the keywords where impression share is low. Here's what the ad data shows.

**Tier 1 keyword coverage in ad data:**

| Search Term | Tier | Spend | Sales | ROAS | Clicks | Orders | CVR |
|-------------|------|-------|-------|------|--------|--------|-----|
| radon detector for home | Tier 1 | $268.94 | $338 | 1.26 | 91 | 2 | 2.20% |
| radon detector | Tier 1 | $19.65 | $0 | 0.00 | 14 | 0 | 0% |
| radon monitor | Tier 1 | $4.00 | $0 | 0.00 | 2 | 0 | 0% |
| continuous radon monitor | Tier 1 | $2.00 | $0 | 0.00 | 1 | 0 | 0% |
| home radon detector | Tier 1 | - | - | - | - | - | Not in ad data |
| **Tier 1 Total** | | **$294.59** | **$338** | **1.15** | **108** | **2** | **1.85%** |

**The disconnect:** The brand is spending on Tier 1 keywords, but the CVR on manual exact targeting (1.85%) is dramatically lower than the auto campaign CVR (7.01%) and the organic CVR (7.0%). This suggests the manual bids are landing on low-converting placements.

**Placement data confirms this:**

| Placement | Spend | Sales | ROAS | CTR | CVR | Clicks |
|-----------|-------|-------|------|-----|-----|--------|
| Top of Search | $112.47 | $2,177 | 19.36 | 6.87% | 11.32% | 106 |
| Rest of Search | $297.40 | $1,859 | 6.25 | 0.44% | 6.18% | 178 |
| Product Pages | $401.33 | $676 | 1.68 | 0.23% | 2.20% | 182 |

> **Finding: 49% of ad spend goes to Product Pages at 1.68 ROAS, while Top of Search converts at 19.36 ROAS with only 14% of budget**
>
> **Problem:**
> - Product Pages absorb $401 (49.5% of total spend) at 1.68 ROAS and 2.20% CVR
> - Top of Search receives only $112 (13.9%) but delivers 19.36 ROAS and 11.32% CVR
> - The manual exact campaign's "radon detector for home" keyword is almost certainly landing on Product Pages at $3.00 CPC, which explains its 1.03 ROAS
>
> **Solution:**
> - Set Top of Search bid modifier to +100-200% on both campaigns to shift impression share to the premium placement
> - Reduce bids on "radon detector for home" in the manual campaign to lower CPC and avoid Product Page placements
> - The auto campaign already naturally wins Top of Search (most of its $2,177 in Top of Search sales), but the manual campaign is dragging performance into Product Pages
>
> **Impact:**
> - Currently: $401 on Product Pages generates $676 (1.68 ROAS)
> - If redirected to Top of Search at its 19.36 ROAS: $401 would generate $7,763
> - Realistic estimate (diminishing returns at higher spend): even a 50% shift from Product Pages to Top of Search would significantly improve blended ROAS
> - The $112 currently on Top of Search already generates $2,177. Doubling this to $225 at even half the current ROAS (9.7x) would generate $2,183 in additional sales

### Auto Campaign Search Term Mining

The auto campaign is finding high-converting search terms that should be harvested into manual campaigns:

| Search Term | Source | Spend | Sales | ROAS | Clicks | Orders |
|-------------|--------|-------|-------|------|--------|--------|
| indoor air quality monitor | Auto (loose-match) | $32.78 | $169 | 5.16 | 17 | 1 |
| luft radon detector | Auto (close-match) | $33.64 | $676 | 20.10 | 29 | 4 |
| luft air quality monitor | Auto | $4.92 | $338 | 68.70 | 4 | 2 |
| air quality monitor indoor radon | Auto | $5.28 | $169 | 32.01 | 3 | 1 |
| vocs | Auto | $2.00 | $169 | 84.50 | 1 | 1 |

"indoor air quality monitor" is a Tier 3 keyword with 5.16 ROAS on just $33 in spend. This validates that the broader air quality market IS capturable for P0. The branded terms also convert extremely well, confirming brand awareness is generating demand that the auto campaign captures.

## Insights

- The auto campaign is the best-performing asset in this account (9.01 ROAS, 23 orders), and it is doing the job that a well-structured manual campaign setup should be doing. The seller has never harvested winning search terms from auto into manual campaigns. This is the single most impactful operational fix.
- Placement distribution is severely misaligned. Top of Search delivers 11.5x the ROAS of Product Pages (19.36 vs 1.68) but receives 3.6x less spend ($112 vs $401). Shifting spend toward Top of Search is the fastest ROAS improvement lever.
- "radon detector for home" as an exact match manual keyword has consumed $327 at 1.03 ROAS. This is the primary source of wasted manual spend. The keyword itself is valid (Tier 1, high volume), but the current bid ($3.00 CPC) and placement (Product Pages) make it unprofitable.

## Things to Investigate Further

- None remaining. The ad data clearly connects to the SQP blocker (impression share) and reveals the specific fixes needed.

## Questions for the Seller

- None. The ad issues are structural and operationally fixable without seller input.
