# Ad Analysis - Ghost Hunting Kit (Spirit Shack)

**Data window:** January 9 - April 7, 2026 (89 days)
**Note:** Ad data is only available from January 2026 onward. This does not mean ads were not running before this date.

## Account-Level Analysis

### Campaign Structure

**Finding: The entire account runs on auto campaigns. There are zero manual campaigns.**

All 23 enabled campaigns use automatic targeting. The campaign names ("HexCom (Fixed bids)", "TripWire (Dynamic bids - down only)", etc.) suggest the seller organized campaigns by product and experimented with bid strategies, which shows intent. But they never created manual campaigns with specific keyword or product targets.

**Problem:**
- Amazon's algorithm decides which search terms to show ads on and how much to bid
- No keyword harvesting: high-performing search terms discovered in auto campaigns have never been extracted into manual campaigns with dedicated bids and budgets
- No negative keyword management: irrelevant search terms (e.g., "hunting" alone, "ghost detector" with 0 conversions) cannot be negated from auto campaigns without a manual campaign structure
- No ability to scale specific high-ROAS keywords independently

**Solution:**
1. Extract the top-converting search terms from auto campaigns (see Search Term Analysis below)
2. Create manual exact-match campaigns for Tier 1 keywords with dedicated budgets
3. Create manual broad/phrase campaigns for Tier 2/3 keyword discovery with negative keyword lists
4. Add negative keywords to auto campaigns for proven non-converters
5. Keep auto campaigns running at reduced budget for continued discovery

**Impact:**
- Manual campaigns with targeted keywords typically achieve 30-50% better ROAS than auto because bids, match types, and budgets are controlled per keyword
- Current auto ROAS is 5.53x. Manual campaigns targeting the proven converters should achieve 7-10x ROAS based on Top of Search performance data (see Placement section)

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|--------|-------|-------|------|-----|-----|-----|
| Automatic | 9,291 | £3,276 | £18,121 | 5.53 | £63.36 | £0.35 | 3.08% |
| Manual | 0 | £0 | £0 | n/a | n/a | n/a | n/a |

100% of ad spend is in auto campaigns. There is no manual layer at all. Despite this, the account is generating decent returns (5.53x ROAS) because the products convert well when shown to relevant audiences. This is a strong signal: the products work, the ads just need a manual structure to scale the winners.

### Campaign Profitability

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| HexCom (Fixed bids) | £845 | £7,316 | 8.66 | 2,457 | 82 |
| Music Box (Fixed bids) | £424 | £1,035 | 2.44 | 856 | 27 |
| SpiritPod (Fixed bids) | £408 | £1,641 | 4.02 | 1,231 | 43 |
| Laser Grid (Dynamic) | £298 | £1,165 | 3.92 | 764 | 23 |
| TripWire (Fixed bids) | £253 | £1,541 | 6.09 | 585 | 18 |
| White Bear (Dynamic) | £229 | £1,512 | 6.61 | 849 | 25 |
| SpiritPod (Dynamic) | £188 | £1,457 | 7.73 | 646 | 28 |
| HexBox (Dynamic) | £178 | £583 | 3.27 | 438 | 10 |
| TripWire (Dynamic) | £129 | £467 | 3.62 | 296 | 6 |
| Music Box (Dynamic) | £106 | £646 | 6.07 | 308 | 14 |
| **Account Total** | **£3,276** | **£18,121** | **5.53** | **9,291** | **286** |

Good news: almost every campaign is profitable. The HexCom is the clear star at 8.66x ROAS. TripWire and White Bear are also strong performers. No campaign is dramatically unprofitable or needs immediate pausing. The "Music Box (Fixed bids)" at 2.44x ROAS is the weakest significant campaign but still above the 1.5x break-even threshold.

The account's profitability is a strength. The issue is not wasted spend on bad campaigns, it is unrealized potential from the lack of manual campaign structure.

### Targeting Strategy

**Keyword vs Product Targeting (within auto campaigns):**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|-------------------|--------|-------|-------|------|-----|-----|-----|
| Keyword Targeting | 5,695 | £2,023 | £10,770 | 5.32 | £60.85 | £0.36 | 3.1% |
| Product Targeting | 3,754 | £1,315 | £7,393 | 5.62 | £67.21 | £0.35 | 2.9% |

Both targeting strategies perform similarly. Product targeting has slightly higher ROAS (5.62 vs 5.32) and higher AOV (£67 vs £61), suggesting product page placements attract buyers purchasing higher-value items. The split is healthy and balanced.

**Match Type Breakdown:** Not applicable. No manual keyword campaigns exist, so there is no exact/phrase/broad breakdown.

## Product-Level Analysis

### P0 Campaign Map (HexCom Ghost Kit)

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| HexCom (Fixed bids) | £845 | £7,316 | 8.66 | 2,457 | 82 |
| HexCom (Dynamic bids - down only) | £9 | £150 | 16.36 | 29 | 2 |
| **P0 Total** | **£854** | **£7,466** | **8.74** | **2,486** | **84** |

P0 captures 26% of total ad spend (£854 of £3,276) but generates 41% of total ad sales (£7,466 of £18,121). The HexCom is the most efficient product in the account by a significant margin.

### Placement Analysis (Account Level, Applicable to P0)

| Placement | Spend | Sales | ROAS | CTR | CVR | CPC |
|-----------|-------|-------|------|-----|-----|-----|
| **Top of Search** | **£866** | **£8,568** | **9.89** | **4.03%** | **5.1%** | **£0.33** |
| Rest of Search | £1,827 | £7,193 | 3.94 | 1.26% | 2.1% | £0.36 |
| Product Pages | £643 | £2,402 | 3.74 | 0.35% | 2.6% | £0.37 |

**Finding: Top of Search Massively Outperforms Other Placements**

**Problem:**
- Top of Search generates ROAS 9.89x, which is 2.5x better than Rest of Search (3.94x) and Product Pages (3.74x)
- Top of Search CTR is 4.03% vs 1.26% (Rest of Search) and 0.35% (Product Pages)
- Top of Search CVR is 5.1% vs 2.1% and 2.6%
- Yet Top of Search only receives 26% of total spend. Rest of Search receives 55%.

**Solution:**
- Increase Top of Search bid modifier on all campaigns to shift more impressions to the premium placement
- In manual campaigns (once created), set Top of Search bid adjustments of 50-100%

**Impact:**
- If spend shifted from Rest of Search to Top of Search at the same CPC, every £1 reallocated moves from 3.94x ROAS to 9.89x ROAS
- Shifting £500 from Rest of Search to Top of Search: current £500 at 3.94x = £1,970 sales. At Top of Search rates (9.89x): £4,945 sales. Net gain: £2,975 in additional sales from the same budget.

### Search Term Analysis

**Top-performing keyword groups:**

| Keyword Group | Spend | Sales | ROAS | Clicks | Orders | CVR |
|--------------|-------|-------|------|--------|--------|-----|
| "spirit box" terms | £211 | £1,736 | 8.2 | 687 | 25 | 3.6% |
| "ghost hunting equipment" terms | £647 | £2,790 | 4.3 | 1,719 | 51 | 3.0% |
| "rem pod" / "rempod" terms | £169 | £1,308 | 7.7 | 597 | 32 | 5.4% |
| "paranormal equipment" terms | £167 | £725 | 4.4 | 426 | 12 | 2.8% |
| "ghost hunting kit" terms | £7 | £124 | 18.7 | 22 | 2 | 9.1% |
| "word generator" terms | £4 | £217 | 52.3 | 15 | 2 | 13.3% |
| "ghost box" terms | £16 | £108 | 6.7 | 54 | 1 | 1.9% |
| Branded ("hexcom", "spiritshack") | £34 | £1,071 | 31.3 | 109 | 13 | 11.9% |
| Competitor ("alice box", "ovilus") | £39 | £692 | 17.9 | 115 | 8 | 7.0% |

**Key findings from search terms:**

1. **"word generator" is the highest-converting keyword group at 13.3% CVR and 52x ROAS, but only £4 in spend.** This is the most directly relevant search term for the HexCom product, yet auto campaigns are barely surfacing it. A manual exact-match campaign on "word generator ghost hunting" and related terms would be the single highest-impact action.

2. **"ghost hunting kit" converts at 9.1% CVR and 18.7x ROAS with only £7 spend.** Another high-intent term that auto campaigns are underfunding.

3. **Competitor terms ("alice box", "ovilus") convert at 7% CVR and 17.9x ROAS.** Customers searching for competitor products (Infraready Alice Box, Ovilus 5) are buying SpiritShack products instead. This is likely driven by price comparison: the HexCom at £130 vs Alice NEO at £250 and Ovilus at £350+. A manual product targeting campaign on these competitor ASINs would scale this winning behavior.

4. **Branded terms ("hexcom", "spiritshack") convert at 11.9% CVR and 31.3x ROAS with £34 spend.** This is expected for branded traffic. Current branded spend is small (1% of total), which is appropriate. A small branded defense campaign (£20-30/mo) is already effectively running through auto.

5. **"ghost detector" is a zero-converter: £34 spend, 96 clicks, 0 orders.** Customers searching for "ghost detector" are looking for EMF meters (physical detection), not word generators. This search term should be negated.

### Wasted Spend

| Search Term | Spend | Clicks | Orders | Notes |
|-------------|-------|--------|--------|-------|
| "hunting" | £19.55 | 54 | 0 | Too generic, not ghost-related |
| Various non-converting ASINs | £70+ | 200+ | 0 | Product page placements on irrelevant listings |
| "ghost detector" / "ghost detector equipment" | £28 | 80 | 0 | Intent mismatch (EMF meter shoppers) |
| "ghost" | £6.30 | 17 | 0 | Too broad |
| "emf" | £7.60 | 21 | 0 | Too broad |
| "laser grid" | £8.41 | 30 | 0 | Different product category |
| Other zero-order terms | £129 | - | 0 | Various irrelevant/broad terms |
| **Total wasted** | **£269** | | | **8.2% of total spend** |

£269 in wasted spend over the period. This is not catastrophic (8.2% of total spend), but in a manual campaign structure with proper negative keywords, most of this could be eliminated.

### P1 HexBox Campaign Performance

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| HexBox (Dynamic bids - down only) | £178 | £583 | 3.27 | 438 | 10 |
| HexBox (Dynamic bids up and down) | £9 | £67 | 7.06 | 29 | 1 |
| HexBox (Fixed bids) | £5 | £0 | 0.00 | 14 | 0 |
| **P1 Total** | **£192** | **£650** | **3.38** | **481** | **11** |

HexBox ROAS (3.38x) is significantly lower than HexCom (8.74x). This confirms the concern raised in ASIN Selection. The HexBox is a newer product (launched Sep 2025) at a higher price point (~£70-80), and the auto campaigns are not yet dialed in. The "Dynamic bids up and down" campaign shows promise (7.06x ROAS) but has minimal spend. The HexBox needs manual campaigns with targeted keywords ("spirit box", "ghost box", "hex box") to improve ad efficiency.

## Insights

- **The account is profitable but structurally immature.** ROAS of 5.53x on 100% auto campaigns is a strong foundation. The products convert well. The problem is entirely structural: no manual campaigns, no keyword control, no scaling mechanism for winners. This is a classic "good product, undermanaged ads" scenario.
- **Top of Search is the growth lever.** At 9.89x ROAS vs 3.94x elsewhere, Top of Search is where this brand wins. The products look good, the prices are competitive, and shoppers who see them at the top of search results buy at 5.1% CVR. Manual campaigns with Top of Search bid modifiers would dramatically improve overall efficiency.
- **"Word generator" and "ghost hunting kit" are massively underserved keywords.** Combined, they have £11 in spend, ROAS 34x, and 11% CVR. These are the highest-intent, most relevant terms for the HexCom, and auto campaigns are barely surfacing them. Manual exact-match campaigns on these terms are the single highest-impact PPC action.
- **Competitor conquest is a proven strategy.** Customers searching for Alice Box and Ovilus products convert to SpiritShack at 7% CVR and 17.9x ROAS. The HexCom's price advantage (£130 vs £250-450) is winning comparison shoppers. This should be deliberately scaled through product targeting campaigns on competitor ASINs.

## Questions for the Seller

- Are the duplicate campaign structures per product (e.g., "HexCom (Fixed bids)" + "HexCom (Dynamic bids - down only)") an intentional A/B test of bid strategies? If so, the "Fixed bids" strategy is getting the vast majority of spend. Have you considered consolidating to one bid strategy per product?
- Have you considered creating manual campaigns? The auto campaign performance is strong, suggesting the products convert well. Manual campaigns would give you control over which keywords to scale and allow you to set Top of Search bid adjustments.
