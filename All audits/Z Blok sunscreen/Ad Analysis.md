# Ad Analysis - Z Blok Sunscreen

## Data Window

Feb 1 - Apr 14, 2026 (entire life of the ad account). The "Februarylipbalm" campaign is the only campaign ever run, and it is currently ENABLED.

## Account-Level Overview

| Metric | Feb 1 - Apr 14, 2026 |
|--------|----------------------|
| Spend | $725.52 |
| Sales | $1,878.75 |
| Orders | 138 |
| ROAS | 2.59 |
| ACoS | 38.6% |
| TACoS | 2.82% (vs $25.7K P0 revenue in Jan-Mar) |
| Impressions | 86,253 |
| Clicks | 360 |
| CTR | 0.42% |
| CVR | 38.33% |
| CPC | $2.02 |
| AOV | $13.61 |

**Every dollar of ad spend is behind P0 (Lip Balm & SPF 30).** There are no campaigns on P1, P2, or P3.

## Account Level

### Campaign Structure

One campaign ("Februarylipbalm") containing two targets. One manual BROAD keyword (`lip balm`) and one "Keywords related to your product category" placeholder (Amazon's manual-suggested keyword group).

| Campaign | Target | Match | Clicks | Spend | Sales | ROAS | Orders |
|----------|--------|-------|--------|-------|-------|------|--------|
| Februarylipbalm | `lip balm` | BROAD | 317 | $647.33 | $1,645.65 | 2.54 | 122 |
| Februarylipbalm | Keywords related to your product category | - | 43 | $78.19 | $233.10 | 2.98 | 16 |

> **Finding: The entire ad strategy is one broad-match keyword on "lip balm."**
>
> **Problem:**
> - A single BROAD target on the most generic possible keyword means Amazon is deciding which search terms the product shows up on. The search-term report shows this is working as harvesting, not as targeting: 90+ distinct customer search terms have spent money over 10 weeks, with ROAS ranging from 0 to 8.75. The winners are buried inside the broad campaign at the same bid as the losers.
> - There is no Exact-match campaign for the proven-winner search terms. Every time a searcher types `zinc oxide lip balm` (3.87 ROAS), `spf 30 lip balm` (4.36 ROAS), `lip balm with spf 30` (7.36 ROAS), or `zinc lip balm` (2.43 ROAS), Amazon is bidding the same blended bid as it would for a throwaway term like `vitamin e lip balm stick`.
> - There is no Exact-match campaign for the Tier 1 SQP queries (`spf lip balm`, `lip sunscreen`, `sunscreen lip balm`, `lip balm spf`) where the SQP analysis showed impression share is 0.34% vs an 8-9% cap.
>
> **Solution:**
> - Restructure into a proper harvest-and-scale structure. Leave the broad discovery campaign running, but extract the top-performing search terms into dedicated Exact-match campaigns with their own budgets and higher bids. Specifically:
>   - **Exact campaign 1 (winner terms):** `zinc oxide lip balm`, `spf 30 lip balm`, `lip balm with spf 30`, `zinc lip balm`, `zinc spf lip balm`, `zinc for lips`. These already convert at 2.4-8.7 ROAS inside the broad campaign.
>   - **Exact campaign 2 (Tier 1 SQP headroom):** `spf lip balm`, `lip sunscreen`, `sunscreen lip balm`, `lip balm spf`. SQP showed these are the 112K/mo search volume where Z Blok has near-zero impression share.
>   - **Negate the winners from the broad campaign** so spend is not duplicated.
>
> **Impact:**
> - The Tier 1 SQP queries alone represent ~28,466 cart adds and ~11,365 purchases per month in the market. Z Blok's 3-month purchase share was 0.06% (~7 purchases/month). Even getting to 0.5% purchase share (still well below the 8-9% ceiling) is ~57 purchases per month at ~$13 AOV = ~$740/mo incremental, or ~$9K/yr at the recovery phase of the season. During peak summer months, Tier 1 demand is 3.5x higher, so the same share % produces that much more revenue. This is the single largest unlocked growth lever in the account.

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|--------|-------|-------|------|-----|-----|-----|
| Automatic | 0 | $0 | $0 | - | - | - | - |
| Manual | 360 | $725.52 | $1,878.75 | 2.59 | $13.61 | $2.02 | 38.3% |

> **Finding: No auto campaign exists.**
>
> **Problem:** Without an auto campaign, Amazon's algorithm is not running in the background finding new search terms to harvest. The current manual broad campaign is doing some of that job (it is how `zinc lip balm` and `zinc for lips` surfaced), but a dedicated auto campaign with Amazon's four default targets (close match, loose match, substitutes, complements) discovers terms a manual broad does not.
>
> **Solution:** Launch a small auto campaign with a modest daily budget ($5-10/day) specifically for discovery. Cap bids low. Mine its search term report every 2 weeks and move winners into Exact campaigns.
>
> **Impact:** Unknown until it runs, but this is how the harvest loop stays full over time. Without it, the account will exhaust the current broad campaign's term discovery and stop finding new winners.

### Campaign Profitability

Only one campaign, and it is profitable (2.59 ROAS, above the 1.5x threshold). No unprofitable campaigns to pause.

**However:** Within the campaign, one placement is unprofitable (Product Pages, 1.24 ROAS) - covered in the CTR/placement section below.

### Targeting Strategy

**Keyword vs Product Targeting:**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|--------------------|--------|-------|-------|------|-----|-----|-----|
| Keyword Targeting | 360 | $725.52 | $1,878.75 | 2.59 | $13.61 | $2.02 | 38.3% |
| Product Targeting | 0 | $0 | $0 | - | - | - | - |

No product targeting exists. No Sponsored Display, no ASIN/category targeting. This is an unused lever that can be deployed defensively (target own product to prevent competitor poaching) and offensively (target competitor ASINs like Sun Bum SPF 30 Lip Balm, Jack Black Intense Therapy, Supergoop Play).

**Match Type Breakdown:**

| Match Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|------------|--------|-------|-------|------|-----|-----|-----|
| EXACT | 0 | $0 | $0 | - | - | - | - |
| PHRASE | 0 | $0 | $0 | - | - | - | - |
| BROAD | 317 | $647.33 | $1,645.65 | 2.54 | $13.49 | $2.04 | 38.5% |

100% broad. No exact or phrase. This is the harvest-and-scale gap called out in Campaign Structure above. The specific recommendation is to extract the winning search terms into exact match.

## Product Level (P0)

### P0 Campaign Map

All ad spend is on P0. One campaign, `Februarylipbalm`, advertising the Lip Balm & SPF 30 Sunscreen (B01D4ZIOAA) exclusively.

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| Februarylipbalm | $725.52 | $1,878.75 | 2.59 | 360 | 138 |

**P0 ad spend share of total account ad spend: 100%.** No diagnostic concern here, the right product is being advertised.

### Blocker-Specific Findings

Section 4 of the SQP analysis identified three simultaneous blockers on Tier 1 for P0: impression share (0.34% vs 8-9% cap), CTR (1.07% vs industry 2.69%), and ATC rate (14.5% vs industry 37.9%). Ad data here is examined through that lens.

#### Impression Share Blocker: Keyword Spend vs. Tier 1/2/3 Queries

> **Section 4 of the SQP analysis found Z Blok's Tier 1 impression share is 0.34% against an ~8-9% ceiling. The PPC lever is to bid explicitly on those queries. Here is what the ad data shows on those exact search terms.**

| Tier 1 Search Term | Spend | Sales | ROAS | Clicks | Orders |
|--------------------|-------|-------|------|--------|--------|
| spf lip balm | $6.60 | $12.95 | 1.96 | 3 | 1 |
| lip balm spf | $8.12 | $25.90 | 3.19 | 4 | 2 |
| lip sunscreen | $17.17 | $51.80 | 3.02 | 9 | 2 |
| sunscreen lip balm | $6.47 | $0 | 0 | 3 | 0 |
| **Tier 1 total** | **$38.36** | **$90.65** | **2.36** | **19** | **5** |

> **Problem:**
> - Tier 1 is receiving $38 of spend across 10 weeks (about 5% of total ad budget) for queries that represent ~112,000 searches per month.
> - Where Tier 1 terms do convert (`lip balm spf` at 3.19 ROAS, `lip sunscreen` at 3.02 ROAS), they convert profitably. The click volume is simply too low to move the impression-share needle.
> - This is happening because the account is bidding via a broad match on `lip balm`, which has to compete against every other lip balm query. The Tier 1 queries are getting a sliver of the broad campaign's budget, not a dedicated push.
>
> **Solution:**
> - Move the Tier 1 queries into a dedicated Exact match campaign with its own daily budget ($15-20/day) and competitive bids ($2.50-$3.00 CPC).
> - Negate `spf lip balm`, `lip sunscreen`, `sunscreen lip balm`, `lip balm spf` from the broad campaign so spend is not duplicated.
> - Run this for 4-6 weeks, track impression share in Brand Analytics, and increase budget as share moves up.
>
> **Impact:**
> - Tier 1 market is 11,365 purchases/mo. Z Blok is at ~7 purchases/mo (0.06% share). Moving to 0.5% purchase share = ~57 purchases/mo at $13 AOV = ~$740/mo incremental revenue, or ~$9K/yr. During peak summer months (June-July), Tier 1 volume is 3.5x larger, so the same share % produces proportionally more. This caps at the ~8-9% impression share ceiling, so genuine long-term ceiling is many multiples higher if the listing can sustain the traffic without leaking (listing fix is prerequisite, see next section).

#### CTR & ATC Blocker: Placement Distribution + Listing Levers

> **Section 4 identified CTR (1.07% vs 2.69% industry) and ATC rate (14.5% vs 37.9% industry) as secondary blockers. For CTR, the PPC lever is shifting spend to better-converting placements. For ATC, the lever is listing-side, not PPC. Here is what the placement data shows.**

| Placement | Spend | Sales | ROAS | CTR | CVR | Clicks | Orders |
|-----------|-------|-------|------|-----|-----|--------|--------|
| Top of Search | $505.55 | $1,386.65 | 2.74 | 3.30% | 42.9% | 240 | 103 |
| Rest of Search | $167.86 | $427.35 | 2.55 | 0.18% | 33.0% | 91 | 30 |
| Product Pages | $52.11 | $64.75 | 1.24 | 0.10% | 17.2% | 29 | 5 |
| Off Amazon | $0 | $0 | - | - | - | 0 | 0 |

> **Problem:**
> - Top of Search is doing the heavy lifting: 70% of spend and 74% of sales at 2.74 ROAS and 42.9% CVR. Its CTR of 3.30% is *above* the Tier 1 industry CTR (2.69%).
> - Product Pages is running at 1.24 ROAS, below the 1.5x profitability threshold. 17.2% CVR on this placement is less than half the CVR of Top of Search. $52 of unprofitable spend over 10 weeks is not a large number, but it reveals the mechanic: when Z Blok shows up on a competitor's product page, the listing does not hold up against the adjacent product shown natively on that PDP.
> - The listing itself (empty bullets, no A+, no video, 3 images with one being unrelated stock art) cannot be fixed with bid modifiers. That is a listing project, not an ad project.
>
> **Solution:**
> - **PPC side (immediate):** Apply a negative bid modifier on Product Pages (at least -50%, ideally -80% until the listing is fixed). Shift that budget toward Top of Search with a positive bid modifier (+25-50%). Top of Search is already the winning placement and converts nearly 43% of clicks.
> - **Listing side (Weeks 4-6):** The listing fixes are the real CTR+ATC levers and are specified in Product Understanding Step 2e: write 5 bullets leading with "Clear Zinc" differentiator, publish A+ content with application video/imagery, add a demonstration video, replace the generic UV stock graphic with real product-use images, extend the title to include `mineral`, `zinc oxide`, `reef safe`, `waterproof`.
>
> **Impact:**
> - Bid-modifier shift alone: $52 of Product Pages spend redirected to Top of Search at its 2.74 ROAS = ~$142 in sales (vs current $65), net +$77 over 10 weeks, small but clean.
> - Listing CTR moving from 1.07% to industry 2.69% on the same impressions = 2.5x the clicks at the same spend. Listing ATC moving from 14.5% to industry 37.9% = 2.6x the orders at the same clicks. Compounded, that is a 6-7x increase in orders on the same ad spend, assuming impression share does not move. Combined with the impression-share fix above, the upside multiplies.

#### Wasted / Irrelevant Search Terms

Within the broad campaign, a small number of clearly irrelevant search terms are consuming budget. These should be negated in the broad campaign.

| Search Term | Spend | Orders | Reason to Negate |
|-------------|-------|--------|------------------|
| carmex classic medicated lip balm sticks | $3.30 | 0 | Not SPF, medicated lip balm, wrong intent |
| cortizone 10 lip balm | $2.99 | 2 | Hydrocortisone treatment, not SPF |
| zumbo kiss lip balm | $2.64 | 0 | Unrelated product |
| vitamin e lip balm stick | $2.64 | 0 | Not SPF |
| extreme weather lip balm | $2.64 | 0 | Not specifically SPF |
| tinted lip balm with spf | $3.96 | 0 | Tinted is a different product category |
| all good lip balm | $2.64 | 0 | Competitor brand, not SPF-specific |
| eos lip balm (from broad) | minimal | - | Not SPF |

Total wasted spend on clearly irrelevant terms: ~$20-25 over 10 weeks. A small cleanup, but tightens the campaign.

#### Branded Defense

Brand typos (`zblock sunscreen lip balm`, `z block sunscreen lip balm`, `v blick lip balm`) are already converting inside the broad campaign at 7-8 ROAS. There is no dedicated branded-defense campaign on `z blok`, `z blok lip balm`. SQP showed these branded queries exist (small volume, 27-57 monthly searches).

> **Recommendation:** Launch a small ($2-5/day) branded defense campaign on `z blok`, `z blok lip balm`, `z blok sunscreen`, and common typos (`zblock`, `z block`). Keep it under 3-5% of total spend per CLAUDE.md branded guidance. Purpose is protective, not growth.

## Insights

- The ad account is two months old, has one campaign, and is already at 2.59 ROAS and 2.82% TACoS. The fundamentals work. The bottleneck is not "ads don't work for this product." It is that the account has no structure to capture the opportunity SQP revealed.
- Top of Search CTR (3.30%) is above industry (2.69% on Tier 1). That is one strong signal that the product can win in search results when it is placed at the top. The listing's CTR problem in organic SQP is a function of the main image and title on the search card; ads force placement to the top and the product converts from there. That supports the case that main-image + title fixes (from Step 2) will disproportionately lift organic as well as ad CTR.
- Product Pages placement runs at 17% CVR, less than half of Top of Search's 43%. On competitor PDPs, the listing cannot compete. This is a direct argument for A+ content and a video before spending another dollar on product-targeting ads.

## Things to Investigate Further

- None. Each of the findings above is backed by specific search-term and placement data, and the next actions are specified.

## Questions for the Seller

- Was the "Februarylipbalm" campaign built by the seller, an agency, or an in-house hire? Understanding who owns ads informs whether the restructure is a conversation about implementation (we do it) or handoff (they do it with our plan).
- Has any listing work (images, A+, video) been scoped or attempted previously, or is this a greenfield project? Drives the Weeks 2-4 timeline in the action plan.
