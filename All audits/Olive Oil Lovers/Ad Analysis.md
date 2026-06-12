# Step 4: Ad Analysis

## Scope

The seller is running **one (1) ad campaign in the entire account**: an auto Sponsored Products campaign covering ~20 vinegar SKUs. There is no other paid activity to analyze, so this step is deliberately narrow: a single-campaign deep-dive plus the broader wholesaler buy-box story which is where most of the strategic upside actually sits.

**Time window:** 2026-02-04 to 2026-05-03 (89 days, the full ad data window).

## Account-Level Snapshot

| Metric | Account Total (90 days) |
|--------|--------------------------|
| Active campaigns | 1 |
| Total ad spend | $653.92 |
| Total ad sales | $956.49 |
| Total ad orders | 28 |
| ROAS | 1.46 |
| ACoS | 68.37% |
| Clicks | 541 |
| CTR | 0.26% |
| CVR | 5.18% |
| AOV | $34.16 |

The whole account ran $7.27/day in ad spend across the last 90 days. That is effectively no paid traffic.

## Campaign Deep-Dive: SP Vinegar 16-jan-2025 b99aa1

### Structure

This is a **Sponsored Products auto campaign** (not manual). All four spend buckets are Amazon's auto-targeting categories - close-match, loose-match, complements, substitutes. There is no manual keyword campaign anywhere in the account.

| Auto Target Type | Impressions | Clicks | CTR | Spend | Sales | ROAS | CVR |
|-------------------|-------------|--------|------|---------|---------|------|------|
| close-match | 75,796 | 259 | 0.34% | $345.99 | $491.86 | 1.42 | 5.41% |
| loose-match | 108,611 | 246 | 0.23% | $278.95 | $413.11 | 1.48 | 4.88% |
| complements | 13,628 | 25 | 0.18% | $23.81 | $51.52 | 2.16 | 8.00% |
| substitutes | 6,949 | 11 | 0.16% | $5.17 | $0.00 | 0.00 | 0.00% |

The campaign is below the profitable 1.5x ROAS threshold overall. Loose-match (the broadest, least relevant Amazon match) is getting 53% of impressions. Complements (which converts at 2.16x) gets 3.6% of spend. The auto algorithm is favouring the wrong targeting buckets.

### Advertised Products in the Campaign

The campaign advertises **20 different ASINs** simultaneously. This is the root cause of the campaign's problems: spend distributes across all 20 SKUs, the auto algorithm picks favourites based on its own signals, and the seller has no control over which product gets which budget.

Top spenders vs their performance:

| Advertised ASIN | Product | Spend | Sales | ROAS | Orders | CVR | Diagnosis |
|------------------|------------|---------|--------|------|--------|------|------------|
| B004JC8II6 | Vincotto Vinegar, Raspberry Selection | $232.98 | $128.64 | 0.55 | 6 | 3.09% | **Eating 36% of budget at sub-break-even** |
| B001YIV3OY | Badia a Coltibuono Red Wine Vinegar | $95.82 | $145.00 | 1.51 | 5 | 6.94% | Borderline profitable |
| B003YVODEG | (unnamed wholesaler vinegar) | $66.71 | $29.00 | 0.43 | 1 | 1.69% | Unprofitable |
| B005XG9VLU | (unnamed wholesaler vinegar) | $62.00 | $15.99 | 0.26 | 1 | 1.89% | Deeply unprofitable |
| B008RVTT88 | Volpaia Tuscany White Wine Vinegar | $41.04 | $74.04 | 1.80 | 3 | 9.68% | Healthy |
| B007W5OPQG | Gianni Calogiuri Fig Vincotto Balsamic Vinegar | $38.78 | $213.66 | **5.51** | 6 | 20.69% | **Strong winner** |
| B00IHJ229S | (unnamed) | $26.80 | $0.00 | 0.00 | 0 | 0.00% | Zero conversion |
| B008SC6W2W | Vigna Oro Balsamic Vinegar di Modena IGP | $22.61 | $0.00 | 0.00 | 0 | 0.00% | Zero conversion |
| B0D7WWWYVB | (unnamed) | $19.82 | $0.00 | 0.00 | 0 | 0.00% | Zero conversion |
| B003NY9NJO | Vincotto Calogiuri Fig Vincotto Vinegar | $11.94 | $234.51 | **19.64** | 4 | 40.00% | **Best ROAS in the account, starved of budget** |
| B0065MQAOM | Acetaia Cattani White Balsamic Vinegar variant | $4.22 | $67.40 | **15.97** | 1 | 16.67% | Winner, starved |
| B0049W6PJ0 | (unnamed) | $5.40 | $48.25 | **8.94** | 1 | 25.00% | Winner, starved |

The pattern is unmistakable. The two ASINs with 19.64x and 15.97x ROAS are getting $12 and $4 of budget respectively. The ASIN with 0.55 ROAS is getting $233.

### Search Term Performance

What customers are actually searching for and what the campaign is paying for:

**Winning specialty searches (high ROAS, very low spend - clear scaling opportunity):**

| Search Term | Spend | Sales | ROAS | Clicks | Orders | CVR |
|--------------|---------|---------|------|--------|--------|-----|
| vincotto fig vinegar | $5.00 | $35.61 | 7.12 | 4 | 1 | 25.00% |
| raspberry vinegar for salad | $2.63 | $21.44 | 8.15 | 2 | 1 | 50.00% |
| fig vinegar | $8.10 | $35.61 | 4.40 | 6 | 1 | 16.67% |
| fig vincotto | $4.29 | $21.44 | 5.00 | 3 | 1 | 33.33% |
| white wine vinegar | $8.08 | $22.52 | 2.79 | 6 | 1 | 16.67% |
| red wine vinegar | $33.44 | $58.00 | 1.73 | 23 | 2 | 8.70% |

**Generic terms bleeding budget:**

| Search Term | Spend | Sales | ROAS | Clicks | Orders | CVR | ACoS |
|--------------|---------|---------|------|--------|--------|-----|------|
| balsamic vinegar | $75.97 | $29.00 | 0.38 | 63 | 1 | 1.59% | 261.97% |
| raspberry vinegar | $71.27 | $21.44 | 0.30 | 50 | 1 | 2.00% | 332.42% |

**Completely irrelevant search terms (zero conversion, money wasted):**

| Search Term | Spend | Notes |
|--------------|---------|-------|
| balsamela | $3.64 | Unknown / nonsense |
| red wine | $11.88 | Wrong intent (wine, not vinegar) |
| bartenura moscato wine | $3.41 | Specific wine brand |
| arbor mist | $2.66 | Wine brand |
| bristol farms | $2.60 | Grocery store name |
| acetaia san giacomo | $3.91 | Competitor brand |
| manicardi balsamic vinegar | $2.67 | Competitor brand |
| garum | $3.90 | Roman fish sauce |
| balsamic vinaigrette | $3.46 | Salad dressing intent, not vinegar |
| balsamic vinaigrette salad dressing | $5.24 | Salad dressing intent |
| raspberry vinaigrette | $2.94 | Dressing intent |
| vincotto | $9.56 | (Generic Italian term, multiple ambiguous intents) |
| aged balsamic vinegar | $11.45 | Different product type, 0 conversion |
| balsamic vinegar of modena | $4.30 | Different product type |

The auto campaign is showing the seller's products on at least ~$55-65 of clearly off-target queries. Add the two generic-bleeders (balsamic vinegar, raspberry vinegar) at $147.24 combined and roughly **30-35% of campaign spend is going to traffic that does not convert**.

## Finding 1: The campaign is structurally wrong

> **Problem:** One auto campaign is doing all the advertising work for 20 different ASINs. Auto is meant for discovery only - find the search terms and product placements that work, then move them into dedicated manual campaigns where each can have its own budget and bid. None of that harvest-and-scale loop is happening here.
>
> The result: the auto algorithm has decided that 36% of the budget should go to B004JC8II6 (Vincotto Raspberry) at 0.55 ROAS. Meanwhile, B003NY9NJO (Fig Vincotto) is converting at **19.64 ROAS** and gets $12. The seller has no way to override this from inside an auto campaign.
>
> **Solution:** Restructure into a proper auto-plus-manual pattern:
> 1. **Pause the 4 underperforming ASINs** from the auto campaign: B004JC8II6, B003YVODEG, B005XG9VLU, B00IHJ229S, B008SC6W2W, B0D7WWWYVB. Combined wasted spend over 90 days: ~$430 at sub-1.5x ROAS. Specifically B004JC8II6 ($233 at 0.55 ROAS), B003YVODEG ($67 at 0.43 ROAS), B005XG9VLU ($62 at 0.26 ROAS) are the must-pause set.
> 2. **Launch manual exact-match campaigns** for the winning specialty search terms: "fig vinegar", "vincotto fig vinegar", "fig vincotto", "white wine vinegar", "raspberry vinegar for salad". Each gets its own campaign with $5-10/day budget so they actually win impression share at high ROAS. These are the seller's natural niche - specialty Italian vinegars that big competitors don't optimize for.
> 3. **Launch a manual product-targeting campaign** for the two top-ROAS ASINs (B003NY9NJO at 19.64x, B0065MQAOM at 15.97x) targeting competitor listings in the same category. They have room to absorb 5-10x the current spend before saturating.
> 4. **Negate the irrelevant search terms** in the auto campaign: "balsamic vinaigrette", "balsamic vinaigrette salad dressing", "raspberry vinaigrette", "bartenura moscato wine", "arbor mist", "bristol farms", "garum", "red wine", "manicardi balsamic vinegar", "acetaia san giacomo".
>
> **Impact:** Reallocating just $230 from the worst ASIN (B004JC8II6 at 0.55 ROAS) to manual campaigns built around the proven 4-8x ROAS specialty search terms produces, at a conservative 4x assumption, **$920 in additional sales over 90 days from the same budget**. The downside is bounded: pulling back from 0.55 ROAS spend can only improve account ROAS, even if the new manual campaigns underperform their isolated-search-term ROAS.
>
> Concretely (90 days, at minimum):
> - Current: $232.98 spend on B004JC8II6 returns $128.64 (loss of $104 vs. breakeven)
> - Proposed: same $232.98 split across manual "fig vinegar" / "vincotto fig vinegar" / "white wine vinegar" exact campaigns at a blended 4x ROAS = ~$932 in sales
> - **Net swing: +$800 in sales from the same dollar of ad budget, at a healthier account-level ROAS (~2.0x+)**

## Finding 2: One specialty niche is the brand's natural advertising home

The data tells a clean story across products and search terms:

- The winning ASINs are all Vincotto / Fig / Calogiuri / specialty Italian vinegars
- The winning search terms are all specialty / Italian-niche queries
- The losing ASINs are mostly generic vinegars (raspberry, modena balsamic) where they compete with major brands
- The losing search terms are all generic vinegar terms where they compete with major brands

This mirrors the SQP finding from Step 3 (oregano product): the brand wins on Italian-specialty intent and loses on generic intent. The ad strategy should mirror that. Stop trying to compete on "balsamic vinegar" and "raspberry vinegar" (huge volume, but mainstream brand territory). Double-down on specialty Italian/regional vinegar queries where the seller's product authenticity is the differentiator.

This same lens applies across the whole catalog. The seller's defensible niche is "we are the importer of authentic, hard-to-find Italian products." The ad strategy should target the exact searches by buyers who know what they want (specialty, regional, named-by-Italian-name), not the searches dominated by generic supermarket buyers.

## Wholesaler Buy Box - The Bigger Lever

Ad spend is a small lever for this seller because the entire account is doing ~$7/day. The much bigger lever - and the one most relevant to a wholesaler model - is **buy box win rate**, where the seller is leaving real revenue on the table on listings they don't even need to "scale" because the traffic is already there.

### The account-level buy box picture (last 8 weeks)

| Week | Buy Box % | Total Sales | Sessions |
|------|-----------|-------------|----------|
| 2026-03-01 | 41.26% | $1,281 | 2,306 |
| 2026-03-08 | 44.81% | $1,469 | 2,260 |
| 2026-03-15 | 43.34% | $1,749 | 2,111 |
| 2026-03-22 | 46.40% | $1,340 | 2,408 |
| 2026-03-29 | 47.12% | $1,153 | 2,896 |
| 2026-04-05 | 41.63% | $1,004 | 2,604 |
| 2026-04-12 | 45.65% | $1,399 | 2,412 |
| 2026-04-19 | 48.04% | $1,744 | 2,554 |
| **Average** | **~45%** | **~$1,400** | **~2,444** |

**The seller is invisible to slightly over half of every shopper who lands on their listings.** Account-level buy box at ~45% means more than half of session-attributed traffic to their ASINs ends up sending the customer to a competing seller on the same listing. Sessions are stable (~2,400/week), but they only convert when they win the buy box.

### Where the buy box loss is concentrated

113 of the seller's 537 active child ASINs are flagged as low-buy-box (under 60%) in our seller-analytics critical issues data. The four hero ASINs from Step 1 show the spread:

| ASIN | Product | Apr 2026 BB | Notable |
|------|---------|------------|---------|
| B001D6B0SG | Selezione Tartufi Black Truffle Sea Salt | 16.83% | Chronic since at least May 2025, despite 4.6-star listing |
| B0934BFDZP | Carlo Moro Pizzoccheri della Valtellina | 17.54% | Collapsed from 74.23% in March - new competing seller likely |
| B0C8926MS1 | Agrumato Lemon Olive Oil | 53.38% | "Galbasa" competitor explicitly running SP ads on this listing (per call) |
| B00D2WK03K | Acetaia Cattani White Balsamic Vinegar | 55.17% | Sessions are tiny but CVR is 68% in April - any buy box gain is direct revenue |

The Black Truffle Sea Salt case shows the dynamic clearly: 12 months of session data sits steadily in the 400-650/month band, but revenue moves with buy box win rate. November 2025 hit a 23.3% buy box (the peak) and revenue hit $756 (also the peak). When buy box was 0-3%, revenue was $0-23. Sessions, listing quality, rating - none of those vary much. **Buy box is the lever.**

### Why this is so common for wholesalers

Per the sales call, the seller is one of several resellers on most of their top listings. The pattern is well-known for Italian-import wholesalers: the original importer/distributor often becomes a direct Amazon seller after a few years, and at that point the wholesaler's pricing/inventory margin gets squeezed by the upstream supplier itself competing for the buy box. Vally confirmed this is what's happening (their vendor is "also in here" now).

There are three buy-box levers we can actually pull:

1. **Repricing automation.** A dynamic repricer that tracks the buy box winner and price-matches within set MAP / margin floors. This is a one-time integration that recovers buy box on price-driven losses, which is the most common reason. The seller does not currently use one (the catalogue is being managed manually by Vally).
2. **Defensive Sponsored Display + Sponsored Brand placements.** When the seller does not have the buy box organically, paid placements still capture some of the click traffic that would otherwise go to a competing seller on the same listing. This is the only way to monetise sessions on listings they no longer win. The Agrumato listing is the textbook case - the "Galbasa" competitor running SP ads is exactly what the seller should be doing in reverse.
3. **Categorise and rank the catalogue.** Of the 537 child ASINs, only a subset are worth fighting for. Most are dead, slow-moving, or have margins too thin to defend. Build a triage: "winnable + worth winning" (e.g. Black Truffle Sea Salt - hold), "unwinnable but visible" (defensive ads only), "neither" (deprioritise to free up Vally's attention).

These three levers, even before any ad spend increase, are likely the largest single revenue swing available in the audit window. Going from 45% to 65% account-level buy box on the same ~2,400 sessions per week, at the same per-session revenue rate, is ~$620 of additional weekly revenue, ~$2,700/month, ~$32k/year. That is bigger than the entire current ad-spend lever combined.

## Insights

- **The seller's one ad campaign is leaking budget at the structure level, not the bid level.** Pausing 4-6 unprofitable advertised ASINs and reallocating to manual exact-match on the 4-5 winning specialty search terms could roughly double campaign sales without increasing total spend.
- **The same Italian-specialty positioning that wins on the SQP side (oregano product, Step 3) also wins on the ad side (Vincotto Fig Vinegar campaign performance).** This is the actual brand wedge: the seller is the authentic-Italian-importer, and their advertising and listing optimisation should lean into named-Italian-regional queries rather than generic categories.
- **Buy box is the much larger lever than ad spend.** Account-level BB sits at ~45%, hero ASINs sit at 15-55% on listings where the listing fundamentals are healthy. Going to 65% buy box across the top 20 listings is a ~$2,500-3,000/month swing - bigger than what the ad budget is even capable of producing at current size.

## Things to Investigate Further

- The 6 unnamed ASINs (B003YVODEG, B005XG9VLU, B00IHJ229S, B008SC6W2W, B0D7WWWYVB, B0049W6PJ0) are not in the Keepa-named list from Steps 1-2. Worth pulling titles from `orange_schema.new_asins` before the call so we can name them concretely when we recommend pause vs. scale.
- The campaign-level CTR sits at 0.26%, well below the typical 0.4-0.6% Amazon SP benchmark. CTR is suppressed across all targeting types, which suggests the issue is the main listing images or placements, not bidding. Once the campaign is restructured, run a placement report (Q705 at the new manual-campaign level) to confirm whether Top of Search is being starved.

## Questions for the Seller

- Are you currently using any repricer (Sellerboard, Aura, Bqool, RepricerExpress, etc.) to maintain buy box, or is pricing being managed manually? If manual, that alone explains a large share of the buy box loss across the catalogue.
- On the Vincotto Raspberry vinegar (B004JC8II6) - this is currently your top ad-spend ASIN and your worst ROAS. Was there a strategic reason it was prioritised, or did the auto algorithm just lock onto it?
- The Vincotto Fig Vinegar (B003NY9NJO) is converting at 40% on tiny spend. Do you have meaningful inventory of this SKU? Before we recommend scaling 10x+ on this product we need to know whether the supply can handle it.
- "Galbasa" was named on the call as running ads on your Agrumato listing. Have you ever defended that listing with Sponsored Display on your own ASIN, or has this gone unchallenged? Similar question for Selezione Tartufi - is there any defensive ad activity on the truffle salt listing where you lose 80%+ of the buy box?
