# Seller Central Audit - Olive Oil Lovers U.S.

## Section 1: Ad Analysis

### Account-Level Snapshot

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

There is a single Sponsored Products auto campaign running across the account: **SP Vinegar 16-jan-2025**. It advertises 20 vinegar SKUs together. Below the 1.5x ROAS profitability threshold overall, and the structure is the cause.

### Campaign Structure - Advertised Products

The auto campaign distributes spend across 20 ASINs. The auto algorithm chooses the favourites based on its own signals, which means there is no control over which product gets which share of budget. The result:

| Advertised ASIN | Product | Spend | Sales | ROAS | Orders | CVR | Status |
|------------------|---------|-------|-------|------|--------|-----|--------|
| B004JC8II6 | Vincotto Vinegar, Raspberry Selection | $232.98 | $128.64 | 0.55 | 6 | 3.09% | Eating 36% of budget at sub-break-even |
| B001YIV3OY | Badia a Coltibuono Red Wine Vinegar | $95.82 | $145.00 | 1.51 | 5 | 6.94% | Borderline profitable |
| B003YVODEG | (Wholesale vinegar) | $66.71 | $29.00 | 0.43 | 1 | 1.69% | Unprofitable |
| B005XG9VLU | (Wholesale vinegar) | $62.00 | $15.99 | 0.26 | 1 | 1.89% | Deeply unprofitable |
| B008RVTT88 | Volpaia Tuscany White Wine Vinegar | $41.04 | $74.04 | 1.80 | 3 | 9.68% | Healthy |
| B007W5OPQG | Gianni Calogiuri Fig Vincotto Balsamic | $38.78 | $213.66 | **5.51** | 6 | 20.69% | **Strong winner** |
| B00IHJ229S | (Wholesale vinegar) | $26.80 | $0.00 | 0.00 | 0 | 0.00% | Zero conversion |
| B008SC6W2W | Vigna Oro Balsamic Vinegar di Modena IGP | $22.61 | $0.00 | 0.00 | 0 | 0.00% | Zero conversion |
| B0D7WWWYVB | (Wholesale vinegar) | $19.82 | $0.00 | 0.00 | 0 | 0.00% | Zero conversion |
| B003NY9NJO | Vincotto Calogiuri Fig Vincotto | $11.94 | $234.51 | **19.64** | 4 | 40.00% | **Best ROAS in account, starved of budget** |
| B0065MQAOM | Acetaia Cattani White Balsamic variant | $4.22 | $67.40 | **15.97** | 1 | 16.67% | Winner, starved |
| B0049W6PJ0 | (Specialty vinegar) | $5.40 | $48.25 | **8.94** | 1 | 25.00% | Winner, starved |

The two ASINs with the highest ROAS (19.64x and 15.97x) are getting $12 and $4 of budget respectively. The ASIN with 0.55 ROAS is getting $233. The algorithm has settled on the wrong distribution and there is no manual override inside an auto campaign.

### Search Term Performance

**Winning specialty searches (high ROAS, very low spend):**

| Search Term | Spend | Sales | ROAS | Clicks | Orders | CVR |
|--------------|---------|---------|------|--------|--------|-----|
| vincotto fig vinegar | $5.00 | $35.61 | 7.12 | 4 | 1 | 25.00% |
| raspberry vinegar for salad | $2.63 | $21.44 | 8.15 | 2 | 1 | 50.00% |
| fig vinegar | $8.10 | $35.61 | 4.40 | 6 | 1 | 16.67% |
| fig vincotto | $4.29 | $21.44 | 5.00 | 3 | 1 | 33.33% |
| white wine vinegar | $8.08 | $22.52 | 2.79 | 6 | 1 | 16.67% |
| red wine vinegar | $33.44 | $58.00 | 1.73 | 23 | 2 | 8.70% |

**Generic terms bleeding budget:**

| Search Term | Spend | Sales | ROAS | Clicks | Orders | ACoS |
|--------------|---------|---------|------|--------|--------|------|
| balsamic vinegar | $75.97 | $29.00 | 0.38 | 63 | 1 | 261.97% |
| raspberry vinegar | $71.27 | $21.44 | 0.30 | 50 | 1 | 332.42% |

**Irrelevant search terms wasting spend (combined ~$55):**

- balsamic vinaigrette, balsamic vinaigrette salad dressing, raspberry vinaigrette - salad dressing intent, not vinegar
- bartenura moscato wine, arbor mist - wine brands
- bristol farms - grocery store name
- garum - Roman fish sauce
- acetaia san giacomo, manicardi balsamic vinegar - competitor brands
- red wine, aged balsamic vinegar, balsamic vinegar of modena - wrong intent

Around 30-35% of campaign spend is going to traffic that does not convert.

### Finding: The campaign is structurally wrong

> **Problem:** One auto campaign is doing all the advertising work for 20 different ASINs. Auto is meant for discovery only - find the search terms and product placements that work, then move them into dedicated manual campaigns where each can have its own budget and bid. None of that harvest-and-scale loop is happening here.
>
> The result: the auto algorithm has put 36% of the budget on B004JC8II6 (Vincotto Raspberry) at 0.55 ROAS. Meanwhile, B003NY9NJO (Fig Vincotto) is converting at **19.64 ROAS** and gets $12.
>
> **Solution:** Restructure into a proper auto-plus-manual pattern:
> 1. **Pause the underperforming ASINs:** B004JC8II6, B003YVODEG, B005XG9VLU, B00IHJ229S, B008SC6W2W, B0D7WWWYVB. Combined wasted spend over 90 days: ~$430 at sub-1.5x ROAS.
> 2. **Launch manual exact-match campaigns** for the winning specialty search terms: "fig vinegar", "vincotto fig vinegar", "fig vincotto", "white wine vinegar", "raspberry vinegar for salad". Each gets its own campaign with $5-10/day budget so they actually win impression share at high ROAS. These are your natural niche - specialty Italian vinegars that big competitors don't optimize for.
> 3. **Launch a manual product-targeting campaign** for the two top-ROAS ASINs (B003NY9NJO at 19.64x, B0065MQAOM at 15.97x) targeting competitor listings in the same category. They have room to absorb 5-10x the current spend before saturating.
> 4. **Negate the irrelevant search terms** in the auto campaign: "balsamic vinaigrette", "balsamic vinaigrette salad dressing", "raspberry vinaigrette", "bartenura moscato wine", "arbor mist", "bristol farms", "garum", "red wine", "manicardi balsamic vinegar", "acetaia san giacomo".
>
> **Impact:** Reallocating just $230 from the worst ASIN (B004JC8II6 at 0.55 ROAS) to manual campaigns built around the proven 4-8x ROAS specialty search terms produces, at a conservative 4x assumption, **$920 in additional sales over 90 days from the same budget**, at a healthier account-level ROAS (~2.0x+).
>
> Concretely (90 days, at minimum):
> - Current: $232.98 spend on B004JC8II6 returns $128.64 (loss of $104 vs. breakeven)
> - Proposed: same $232.98 split across manual "fig vinegar" / "vincotto fig vinegar" / "white wine vinegar" exact campaigns at a blended 4x ROAS = ~$932 in sales
> - **Net swing: +$800 in sales from the same dollar of ad budget, at a healthier account-level ROAS**

### Specialty Italian is your natural advertising home

The data tells a clean story across products and search terms:

- The winning ASINs are all Vincotto / Fig / Calogiuri / specialty Italian vinegars
- The winning search terms are all specialty / Italian-niche queries
- The losing ASINs are mostly generic vinegars (raspberry, modena balsamic) where you compete with major brands
- The losing search terms are all generic vinegar terms where you compete with major brands

Stop trying to compete on "balsamic vinegar" and "raspberry vinegar" (huge volume, but mainstream brand territory). Double-down on specialty Italian/regional vinegar queries where your product authenticity is the differentiator. This same lens applies across the rest of the catalog. The defensible niche is the authentic, hard-to-find Italian products - the ad strategy should target the searches by buyers who already know what they want.

## Section 2: Buy Box - The Bigger Lever

Ad spend is one lever, but on a wholesaler account the much larger one is **buy box win rate**. The traffic is already arriving at the listings; revenue moves with whether you win the buy box on that traffic.

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

At ~45% account-level buy box, more than half of session-attributed traffic to your listings ends up sending the customer to a competing seller on the same listing. Sessions are stable (~2,400/week), but they only convert when the buy box is won.

### Where the buy box loss is concentrated

113 of the 537 active child ASINs sit at low-buy-box (under 60%). The four highest-revenue ASINs show how wide the spread is:

| ASIN | Product | Apr 2026 BB | Notable |
|------|---------|------------|---------|
| B001D6B0SG | Selezione Tartufi Black Truffle Sea Salt | 16.83% | Chronic since at least May 2025 |
| B0934BFDZP | Carlo Moro Pizzoccheri della Valtellina | 17.54% | Collapsed from 74.23% in March |
| B0C8926MS1 | Agrumato Lemon Olive Oil | 53.38% | Galbasa competitor running SP ads on this listing |
| B00D2WK03K | Acetaia Cattani White Balsamic Vinegar | 55.17% | Sessions tiny but Apr CVR is 68% - any BB gain is direct revenue |

The Black Truffle Sea Salt case shows the dynamic clearly: 12 months of session data sits steadily in the 400-650/month band, but revenue moves with buy box win rate. November 2025 hit a 23.3% buy box (the peak) and revenue hit $756 (also the peak). When buy box dropped to 0-3%, revenue dropped to $0-23. Sessions, listing quality, rating - none of those vary much. **Buy box is the lever.**

### The dynamic repricer solution

The most common reason for buy box loss is price - competing sellers undercut by a small margin and capture the box. A **dynamic repricer** monitors the listing in real time, identifies the current buy-box-winning price, and adjusts your price within MAP and margin floors that you control. The same algorithm that loses you the buy box also lets you win it back automatically. It is a one-time integration that recovers buy box on price-driven losses across the catalog.

In parallel, on listings where the price battle cannot be won (a wholesaler with structurally higher cost), **defensive Sponsored Display + Sponsored Brand ads** on your own ASINs capture the click traffic that would otherwise go to the competing seller. The Agrumato listing where Galbasa is running ads on you is the textbook case - the same play, run in reverse.

### Impact estimate

Going from 45% to 65% account-level buy box on the same ~2,400 sessions/week, at the same per-session revenue rate, is roughly **+$620 of additional weekly revenue, ~$2,700/month, ~$32k/year**. This is before any change to ad spend or listing content.

## Section 3: Action Plan

### Weeks 1-2: Immediate PPC Actions

The first two weeks are about stopping the bleeding inside the existing campaign.

- **Pause the unprofitable ASINs** from the SP Vinegar auto campaign: B004JC8II6, B003YVODEG, B005XG9VLU, B00IHJ229S, B008SC6W2W, B0D7WWWYVB. This frees up ~$430 of 90-day spend that was running below break-even.
- **Negate the 14 irrelevant search terms** in the auto campaign (salad dressing intent, wine brand names, grocery store names, competitor brands, off-target product types).
- **Reduce the loose-match bid** in the SP Vinegar auto campaign and let close-match consume more share. Loose-match currently gets 53% of impressions with the worst ROAS of all four buckets.
- **Launch defensive Sponsored Display** on the Agrumato Lemon listing to counter the Galbasa competitor running ads on that detail page.

Expected impact by end of Week 2: account-level ad ROAS climbs from 1.46 toward 1.8-2.0 just from cutting the worst spend, before adding any new campaigns.

### Weeks 2-4: Scale the Specialty Niche

With the bleeding stopped, build the manual structure that captures the high-ROAS searches we already know convert.

- **Launch manual exact-match campaigns** for the proven specialty search terms: "fig vinegar", "vincotto fig vinegar", "fig vincotto", "white wine vinegar", "raspberry vinegar for salad". $5-10/day per campaign so they actually capture impression share on terms that have been converting at 4-8x ROAS but getting <$10 of spend each.
- **Launch a manual product-targeting campaign** for B003NY9NJO (Fig Vincotto) and B0065MQAOM (Acetaia Cattani variant) targeting competitor balsamic and vincotto listings. These converted at 19.64x and 15.97x ROAS at near-zero spend - they can absorb 5-10x the current budget before diminishing returns.
- **Harvest the auto campaign weekly:** every Monday, look at the prior week's search-term report inside the auto campaign. Any new term that converted at 3x+ ROAS gets moved into a new exact-match manual campaign. Any new term that wasted budget gets negated. This is the loop that keeps the structure healthy.
- **Layer in a small Sponsored Brands campaign** targeting "italian vinegar" and "specialty vinegar" head terms. Sponsored Brands lets you put a custom hero image and brand message at the top of search results - this is where the "authentic Italian importer" positioning earns its keep on browse-intent traffic.

Expected impact by end of Week 4: account-level ad sales doubling on the same total budget, with a clear list of which search terms and products to scale further.

### Weeks 4-6: Inventory Implications of Scaling

By Week 4, several specialty SKUs will be selling 3-5x their pre-audit volume from PPC alone. Before increasing ad spend further, inventory needs to be aligned.

- **Pre-buy on the proven specialty winners.** B003NY9NJO (Fig Vincotto), B007W5OPQG (Gianni Calogiuri Fig Vincotto Balsamic), B0065MQAOM (Acetaia Cattani White Balsamic), and B008RVTT88 (Volpaia White Wine Vinegar) are the four ASINs we will be scaling hardest. With the 1-month Italy lead time, the order placed in Week 4 lands on the shelf in Week 8 just in time to support the higher-spend phase.
- **Inventory depth target:** at minimum 60 days of forward cover at the projected scaled run rate for each of those four SKUs. This protects against the August 2025-style stockout we saw on the Sicilian Oregano (BB collapsed from 100% to 5.36% when stock ran out, recovery took 6 weeks).
- **Pause PPC scaling on any ASIN whose inventory cover drops below 30 days.** Better to slow the campaign than to win the buy box, run out of stock, and lose the organic rank along with it.
- **For FBA-eligible specialty SKUs (vinegar, taralli, dried herbs, pasta):** consider sending a small first batch (50-100 units per SKU) into FBA in this phase. Prime badge improves both CVR and BB share, and the smaller commitment lets you test without putting climate-sensitive inventory at risk.

### Weeks 6-8: Forward Growth Path

By Week 6 the PPC restructure is producing measurable lift and the inventory is positioned for the next phase. Now layer in the longer-cycle levers.

- **Deploy a dynamic repricer** across the top 50 wholesaler ASINs by revenue, starting with the four hero ASINs above. Repricer integrations typically take 1-2 weeks to configure rules and validate behaviour, so Week 6 is the right time to start. The same lever continues compounding through Weeks 9-12 as more ASINs come into the rule set.
- **Begin listing optimization on the owned-brand catalogue.** The Sicilian Oregano (B01N2Z8FQV) is the highest-impact starting point: zero bullets, no A+ content, no video, only 2 images today, and it's miscategorized under Produce > Fresh Vegetables instead of Herbs & Spices. A full rebuild plus recategorization closes a 31% CVR gap on Tier 1 queries (vs. industry) and opens organic eligibility on a wider keyword set. The same template applies to the other Olio2go-owned SKUs (Sicilian Thyme, the gift sets, the specialty olive oils) once we prove it on oregano.
- **Initiate Brand Registry on the Gragnano in Corsa pasta line.** This is your only exclusive importer brand and the registry has not been done. Completing it unlocks A+ content, Sponsored Brand campaigns, Brand Story modules, and protection against listing hijacking. Pasta is also the only line in the catalog with a 2-year shelf life, which makes it the strongest candidate for FBA at scale. The full Gragnano build-out is the next major growth lever beyond the 8-week window.
- **Plan the Black Truffle Sea Salt ad launch.** This product currently has zero ad spend despite being the revenue leader. Once the listing is in a stronger state (whether via coordination with the brand owner on Premium A+ and video, or via defensive Sponsored Display covering the buy box loss), a $10-15/day Sponsored Products test on truffle salt queries should produce fast results given the 15.82% CVR already achieved when the listing wins the buy box.

The Week 6+ phase is when the audit's full set of levers - PPC scaling, repricer, listing rebuilds, brand registry, FBA expansion - start compounding together. The PPC structure built in Weeks 1-4 stays running; the inventory positioning in Weeks 4-6 prevents the stockout failure mode; and the longer-cycle levers from Week 6 onward build the durable, multi-quarter growth path.
