# Ad Analysis: Ecodrop

Window: 2026-01-24 to 2026-04-23 (90 days, full available ad window). ENABLED campaigns only where noted.

## Account Overview

- Total ad spend (ENABLED, 90d): **£5,742** (~£1,900/month)
- Total ad sales: **£17,707**
- Account ROAS: **3.08**
- TACoS: ~6% (below the client's 10% target, meaningful headroom to scale)
- ENABLED campaigns: 426. 312 have spend >£0. 124 have ≥10 clicks (statistically significant).

The client's worry that they're already spending heavily is not borne out by the data. Account-level TACoS is 6% against a 10% target; there is approximately £1,200-1,500/month of budget headroom before hitting the stated ceiling.

## Account-Level Findings

### Campaign Structure

Not a headline issue. 426 ENABLED campaigns is a lot for £1.9k/month, but none of the top campaigns look egregiously overstuffed (most run 1-16 ASINs and a handful of targets each). Move on.

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|-------:|-------:|-------:|-----:|------:|------:|------:|
| Automatic | 1,044 | £349 (6%) | £1,752 | 5.02 | £13.27 | £0.33 | 12.6% |
| Manual | 6,999 | £5,393 (94%) | £15,955 | 2.96 | £10.80 | £0.77 | 21.1% |

**Problem:** Auto ROAS 5.02 vs Manual ROAS 2.96. Auto is converting at a 70% higher return, which signals that winning search terms inside auto haven't been fully harvested into dedicated manual campaigns. The split itself (94% manual) is healthy in proportion, but the premium on auto is a harvest signal.

**Solution:** Mine the auto campaigns' converting search terms, promote top converters into their own manual exact/phrase campaigns, and negate them out of auto.

**Impact:** Small in absolute terms because auto is only £349 of spend. A realistic lift from harvesting would add maybe £200-300/month in sales. Minor finding, not the main lever.

### Campaign Profitability

| | Campaigns (≥10 clicks) | Spend | Sales | ROAS |
|---|---:|---:|---:|---:|
| Unprofitable (ROAS < 1.5) | 16 | £458 | £533 | 1.16 |
| Profitable | 107 | £4,930 | £15,279 | 3.10 |

**Problem:** £458 of spend (8% of account) is running below breakeven on ~16 campaigns.

**Solution:** Pause or restructure. Top offenders:

| Campaign | Spend | Sales | ROAS |
|---|---:|---:|---:|
| EV - SP - Ylang Ylang - Broad | £163 | £243 | 1.49 |
| S. - Essential Oil - Gift Set - Broad | £73 | £77 | 1.04 |
| S. - Essential Oil - Gift Set - Exact | £37 | £38 | 1.04 |
| S. - Essential Oil - Vanilla - Broad | £26 | £21 | 0.80 |
| S. - Diffuser 250ml - All - TOF - Reed - Broad | £23 | £25 | 1.09 |

**Impact:** £458 reallocated to the account's average profitable ROAS of 3.10 would generate ~£1,420 in additional sales over 90 days. Small, but clean.

### Targeting Strategy

**Keyword vs Product Targeting (90d, all statuses):**

| Strategy | Clicks | Spend | Sales | ROAS | CVR | CPC |
|---|---:|---:|---:|---:|---:|---:|
| Keyword Targeting | 7,432 | £6,890 (78%) | £16,186 | 2.35 | 19.85% | £0.93 |
| Product Targeting | 2,805 | £1,986 (22%) | £5,443 | 2.74 | 17.75% | £0.71 |

Product targeting has slightly better ROAS at lower CPC, but the split is reasonable. Not a major reallocation signal.

**Match Type Breakdown:**

| Match Type | Clicks | Spend | Sales | ROAS | CVR | CPC |
|---|---:|---:|---:|---:|---:|---:|
| BROAD | 4,184 | £3,624 (54%) | £8,314 | 2.29 | 18.76% | £0.87 |
| EXACT | 1,647 | £1,964 (29%) | £3,911 | 1.99 | 22.16% | £1.19 |
| PHRASE | 1,048 | £1,119 (17%) | £2,820 | 2.52 | 23.28% | £1.07 |

**Problem:** EXACT match has the highest CVR (22.16%) but the worst ROAS (1.99) because its CPC is 36% higher than BROAD. And PHRASE has the best ROAS and CVR but gets the smallest share of spend.

**Solution:** (1) Audit exact keyword bids — the premium being paid isn't being recovered. (2) Shift more spend toward PHRASE match, which has the best all-around metrics.

**Impact:** A 10-percentage-point shift from EXACT to PHRASE at current ROAS would add ~£160/month in sales.

### Placement Performance

| Placement | Impressions | CTR | CVR | Spend | Sales | ROAS | ACoS |
|---|---:|---:|---:|---:|---:|---:|---:|
| **Top of Search** | 83,815 | **5.08%** | **26.81%** | £3,876 (44%) | £12,221 | **3.15** | 31.72% |
| Rest of Search | 818,710 | 0.51% | 15.99% | £3,544 (40%) | £7,624 | 2.15 | 46.49% |
| Product Pages | 1,063,976 | 0.17% | 9.01% | £1,453 (16%) | £1,804 | **1.24** | **80.54%** |

> **Finding: Product Pages placement is unprofitable and eating 16% of ad spend.**
>
> **Problem:**
> - Product Pages ROAS is 1.24, well below the 1.5x profitability floor.
> - CTR on Product Pages is 0.17% vs 5.08% on Top of Search — Ecodrop's ads don't win attention against competitor products on PDPs.
> - CVR on Product Pages is 9.01% vs 26.81% on Top of Search — customers who click from PDP don't convert.
> - Total £1,453 spent on Product Pages over 90 days returned £1,804 in sales.
>
> **Solution:** Reduce Product Pages bid modifier to 0% or heavily negative across campaigns. Reallocate the freed budget to Top of Search via a higher Top-of-Search bid modifier.
>
> **Impact:** £1,453 reallocated to Top of Search at 3.15 ROAS would generate £4,577 in additional sales over 90 days (vs the £1,804 it generated on Product Pages). Net gain: **~£2,770 in sales over 90 days, or ~£920/month**, from the same ad budget.

Top of Search is the clear winner on every metric. The account should be pushing hard to win that placement for its highest-intent queries.

## Product-Level Analysis: Reed Diffuser (P0)

### P0 Campaign Map

**100ml parent (B0CNSC2D85):**

- Impressions: 454,249
- Clicks: 1,404
- Orders: 242
- Spend: **£1,370** (15.4% of account) = ~£457/month
- Sales: £3,148
- ROAS: 2.30

**250ml parent (B0GTWLTMFH):**

- Spend: £146 (1.6% of account) = ~£49/month
- Sales: £437
- ROAS: 2.99

**Combined P0 spend: £1,516 (17% of account). The 250ml is underfunded proportional to its growth potential, but the bigger story is on the 100ml.**

Top Reed Diffuser 100ml campaigns (by spend):

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|---|---:|---:|---:|---:|---:|
| S. - Diffuser - All - Broad - TOF | £174 | £619 | 3.55 | 264 | 50 |
| SP - Broad - Reed Diffuser - Gold Panning | £171 | £390 | 2.28 | 170 | 25 |
| SP - Reed Diffusers - Phrase - Multi Kw(1) | £144 | £410 | 2.84 | 172 | 33 |
| Reed Diffuser Oil Set (Orange & Bergamot) - PT | £130 | £211 | 1.62 | 89 | 15 |
| Reed Diffuser Oil Set (Orange Bergamot) - Exact | £104 | £158 | 1.52 | 67 | 12 |
| EV \| SP \| Reed Diffuser Refills \| Broad | £102 | £91 | **0.89** | 77 | 8 |
| SP - B0BPRCHJGZ - Gold Panning - Reed Difuser | £64 | £54 | **0.84** | 37 | 5 |
| SP - Reed Diffusers - Broad - Multi Kw(1) | £58 | £46 | **0.80** | 41 | 4 |
| EV \| SP \| Reed Diffuser Refills \| Exact | £51 | £45 | **0.88** | 24 | 4 |

~£275 of the 100ml Reed Diffuser spend (20%) is on campaigns running below 1.5x ROAS. Pause or negate and reallocate.

Top 250ml campaigns:

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|---|---:|---:|---:|---:|---:|
| S. - Diffuser 250ml - All - TOF - Broad | £72 | £187 | 2.61 | 99 | 15 |
| S. - Diffuser 250ml - All - TOF - Reed - Broad | £27 | £37 | 1.37 | 38 | 3 |
| S. - Diffuser 250ml - Orange Blossom - Competitor PT | £12 | £75 | 6.08 | 16 | 6 |
| S. - Diffuser 250ml - White Jasmine - Competitor PT | £11 | £50 | 4.65 | 14 | 4 |

The Competitor PAT campaigns on 250ml are showing excellent early ROAS. Scale these.

### Impression Share Blocker: The Headline Finding

Section 4 identified impression share as the primary blocker on Tier 1 reed diffuser queries, with Ecodrop's impression share collapsing from 1.10% (Oct 2025) to 0.16% (Mar 2026). The PPC lever is bidding on those Tier 1 keywords. Here's what the ad data shows.

**Current spend on Tier 1 reed diffuser search terms (90 days):**

| Search Term | Tier | SQP Monthly Volume | Spend (90d) | Sales | ROAS | Clicks | Orders | CVR |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| reed diffuser | T1 | ~75k | £39 | £167 | **4.26** | 50 | 13 | 26.0% |
| reed diffuser refill | T1 | ~24k | £25 | £154 | **6.14** | 37 | 12 | 32.4% |
| reed diffusers for home | T1 | ~10k | £28 | £52 | 1.83 | 18 | 4 | 22.2% |
| diffuser refill | T1 | ~5k | £10 | £22 | 2.07 | 12 | 2 | 16.7% |
| reed diffuser oil | T1 | ~3k | £7 | £32 | **4.40** | 7 | 3 | 42.9% |
| diffuser refills | T1 | ~13k | £6 | £11 | 1.88 | 7 | 1 | 14.3% |
| diffuser oil refill | T1 | ~3k | £4 | £11 | 2.48 | 4 | 1 | 25.0% |
| reed diffuser bottles | T1 | ~1k | £4 | £0 | 0.00 | 3 | 0 | 0% |
| reed diffusers | T1 | ~4k | £2 | £12 | 5.14 | 3 | 1 | 33.3% |
| diffuser reed | T1 | ~1k | £2 | £0 | 0.00 | 2 | 0 | 0% |
| **TOTAL Tier 1** | | ~142k | **£129** | **£461** | **3.58** | 143 | 37 | **25.9%** |

> **Finding: Ecodrop is spending £129 over 90 days (£43/month) on the exact search terms that are the account's primary blocker — and the ROAS on those terms is 3.58.**
>
> **Problem:**
> - Ecodrop's Tier 1 spend is 2.1% of total ad spend, or £43/month.
> - These terms are the core of Ecodrop's product. "Reed diffuser" alone has ~75k monthly UK search volume.
> - ROAS on "reed diffuser" is 4.26; "reed diffuser refill" is 6.14. Both are among the highest ROAS terms in the entire account.
> - Per Step 3, impression share on these terms dropped from 1.10% to 0.16% — the listing isn't showing up and the ad spend isn't making up the gap.
> - Meanwhile, the account is spending £162 on "frankincense oil" alone (ROAS 2.11) and £96 on "frankincense essential oil" (ROAS 1.61). Essential oils are consuming Tier 1 reed diffuser's rightful budget.
>
> **Solution:**
> 1. Build dedicated manual exact-match campaigns for each Tier 1 keyword (reed diffuser, reed diffuser refill, diffuser refills, reed diffuser oil, diffuser refill). Each keyword in its own campaign for independent bid control.
> 2. Scale spend on these terms from £43/month combined to ~£500/month combined. Budget is available from (a) account headroom (TACoS 6% vs 10% target), (b) Product Pages placement reallocation (£480/month freed up), (c) pausing unprofitable campaigns (~£150/month).
> 3. Set Top of Search bid modifier high on these campaigns (the 5.08% CTR vs 0.17% at Product Pages proves this is where the conversion happens).
> 4. Negate the sub-1.5x-ROAS Reed Diffuser campaigns (Refills Broad at 0.89, Gold Panning at 0.84, Multi Kw at 0.80) and move that £275/90d into the scaled Tier 1 campaigns.
>
> **Impact:** At 3.58 ROAS, £500/month of new Tier 1 spend generates £1,790/month in incremental sales = **~£21.5k/year.** Plus the organic halo as velocity rebuilds BSR over 2-3 months, which should add further lift. This single move is the biggest growth lever in the account.

Context: Tier 2 (broad diffuser) search terms currently get £78/90d at ROAS 1.82, and Tier 3 (scent + diffuser) gets £11/90d at ROAS 2.19. Tier 3 is a clean secondary opportunity to scale but volume is small (~3k monthly SV). Tier 2 should stay minimal given the poor conversion from generic "diffuser" buyers who are actually looking for electric models.

### Secondary Blocker: CTR

The SQP showed brand CTR was 0.80% vs industry 1.25% on Tier 1 (36% below). The placement data explains part of this: Ecodrop is getting only 44% of its ad budget into Top of Search, where its CTR jumps to 5.08% (4x industry for that query set). The rest is diluted in Rest of Search (0.51%) and Product Pages (0.17%).

**PPC lever for CTR:** Push Top of Search bid modifiers up, pull Product Pages down (addressed above).

**Listing lever for CTR:** Main image / ratings / price signaling on the 100ml Reed Diffuser — covered in Step 2 (Product Understanding) as opportunities. Specifically: refresh main image (add scent/size callouts), ensure ratings show clearly on SERP thumbnail, and consider a video to differentiate.

## Summary of Ad Actions, Ranked by Impact

| # | Action | Monthly Sales Impact | Difficulty |
|---|---|---:|---|
| 1 | Scale Tier 1 reed diffuser spend from £43 to ~£500/month | **+£1,790** | Low (bid + budget edits) |
| 2 | Kill Product Pages placement, reallocate to Top of Search | **+£920** | Low (bid modifier) |
| 3 | Pause 16 unprofitable campaigns, reallocate | +£470 | Low |
| 4 | Scale 250ml Competitor PAT campaigns (Orange Blossom, White Jasmine) | +£200 | Low |
| 5 | Shift EXACT → PHRASE match type | +£160 | Medium |
| 6 | Harvest auto campaign winners into manual | +£200 | Medium |

**Combined ad-side impact: ~£3,740/month in incremental sales** using existing budget + headroom to 10% TACoS. This is before listing fixes or BSR recovery effects.

Reed Diffuser parent alone currently sits at ~£6k/month. The ad-side lift here plus BSR recovery makes a credible path to ~£10-12k/month on Reed Diffuser over the next 8-12 weeks. That's a material contribution to the £60k monthly goal.
