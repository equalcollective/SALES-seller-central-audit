# Step 1: ASIN Selection - Creative Gifts International

## Data Readiness

- Business data: 2024-07-01 to 2026-04-12 (21 months)
- Ad data: 2026-02-01 to 2026-04-21 (59 days, **below the 70-day threshold**)
- **Analysis window:** Feb 1 - Mar 31, 2026 (2 complete months with both ad + business data)

This is the largest catalog audited so far (302 parents, 328 child ASINs), with 208 parents recording sales in the window. Reported Amazon revenue is ~$3.4k/month, much smaller than the $6-7k/month the seller mentioned, which is consistent with the bulk of their volume being offline / wholesale / distributor business. Ad spend on Amazon was ~$504/month vs. the seller's stated $500/week, again pointing to other channels.

## Priority Table

| Priority | Product | 2-Mo Sales | 2-Mo Ad Spend | ROAS | TACoS | Organic Sales | Ad Sales % | Buy Box % | CVR | Trend |
|----------|---------|-----------|---------------|------|-------|---------------|-----------|-----------|-----|-------|
| P0 | Dog Balloon Animal Piggy Bank (B0BK5QQCML) | $984 | $105 | 2.29 | 10.7% | $744 | 24.4% | 85-97% | 1.56% → 6.21% | Growing (4.1x Feb → Mar) |
| P1 | Custom Vanity Set (B0BM8SKGYL) | $924 | $0 | n/a | 0% | $924 | 0% | **1-2%** | 1.52% → 5.32% | Growing (3x Feb → Mar) |
| P2 | Noah's Ark and Animals Coin Bank (B009W24ZBC) | $765 | $22 | 34.1 | 2.9% | $225 | 70.5% | 72-96% | 2.63% → 13.64% | Growing (7.5x Feb → Mar) |
| P3 | Silverplated Baby's First Sippy Cup (B000X24Z10) | $526 | $54 | 4.46 | 10.3% | $286 | 45.6% | 66-77% | 5.15% → 3.81% | Growing (2.2x Feb → Mar) |

### Why these four

- **P0, Dog Balloon Animal Piggy Bank**, highest revenue with active ad spend. Falls into the "banks" category the seller flagged as a focus, and is evergreen (gifting / kids' room).
- **P1, Custom Vanity Set**, the seller's flagged "unique brush and mirror set." Selling $924 over 2 months with $0 ad spend AND a 1-2% buy box is the largest unrealized opportunity in the catalog. If we fix buy box and start advertising, this product can scale aggressively.
- **P2, Noah's Ark Coin Bank**, also a "bank," sitting at 30x ROAS in March on $22 of ad spend. Tells us there's room to scale here. Sessions are very low (76-110/month) so the ceiling is unknown but the unit economics look excellent.
- **P3, Silverplated Baby's First Sippy Cup**, the seller's flagged baby sippy cup. Strong session growth (136 → 315) the moment ad spend was turned on in March.

### Products considered but not prioritized

- **Optic Glass Trophy Point ($608)**, corporate award/recognition product, not in the seller's evergreen-gifting thesis. Sessions are only 17-26/month, so growth ceiling is small even if CVR is 46%. Worth flagging to the seller as a quietly profitable line, not as a focus ASIN.
- **Ceramic Swan with Crown Piggy Bank ($308)**, flagged by the seller but TACoS is 45.7% and ROAS is 1.81. The product is selling almost entirely on ads (82.6% ad-attributed). Smaller, less efficient than Dog Balloon and Noah's Ark.
- **Other piggy banks (Puffy Unicorn, Sloth, Flamingo, Ombre Unicorn)**, each $60-$200 over 2 months. Combined, the bank category is ~$2.5k of the ~$6.9k Amazon revenue (~36%), confirming the seller's instinct that banks are a meaningful pillar. They are all separate parent ASINs today; merging them as variations is **not advisable** because customers searching for "unicorn piggy bank" don't want a "dog piggy bank", these are different products, not variants of one.

## P0 Annual Trend (Dog Balloon Animal Piggy Bank)

| Metric | Aug 2025 (Summer Peak) | Dec 2025 (Holiday Peak) | Feb 2026 (Trough) | Mar 2026 (Latest) |
|--------|-----------------------|-------------------------|-------------------|-------------------|
| Total Sales | $456 | $528 | $192 | $792 |
| Sessions | 296 | 608 | 513 | 773 |
| CVR | 6.42% | 3.62% | 1.56% | 6.21% |
| Buy Box % | 97.6% | 93.4% | 97.0% | 85.1% |

- Sales swing widely month-to-month over the past year ($192 - $792). There is a visible Q4 holiday lift (Oct → Dec sessions climb from 248 to 608) and a March 2026 rebound that lines up with the seller turning on ads more aggressively. Whether this is a seasonal pattern (Easter, baby showers, graduation) or purely ad-driven needs SQP confirmation.
- Feb 2026 was a steep CVR collapse (1.56%) despite buy box being healthy at 97%. Sessions held at 513 but conversions disappeared. The recovery in March (CVR 6.21%) tracks with ad spend going from $17 to $87, suggesting the ads pulled more intent-driven traffic.
- Buy box dropped from 97% to 85% in March 2026. That's a 12-point drop happening at the same time as the ad ramp. Worth checking whether a price change or competing offer triggered this.

## Insights

- **P1 (Custom Vanity Set) buy box is at 1-2% and the seller is running zero ads on it, yet it's still doing $924 over 2 months purely on organic traffic.** This is the single biggest unlocked lever in the catalog. The product is clearly resonating; we just have to capture the sessions instead of leaking them to whoever is winning the buy box. Note: this is a private-label-style product so the buy box loss is most likely MAP / pricing related rather than a competing 3P seller, per the domain note in the workflow.
- **P2 (Noah's Ark Coin Bank) is running at 30x ROAS in March on $22 of ad spend with 80% of sales ad-attributed.** This is a textbook signal that ad spend is far below the efficient frontier, there is room to scale spend before ROAS deteriorates.
- **The "banks" category is ~36% of total Amazon revenue across 7+ separate parent ASINs.** Confirms the seller's instinct that banks are a real pillar, but each animal/style is a distinct product with distinct keywords (dog, swan, unicorn, sloth, flamingo, Noah's ark). They should not be merged into one parent.

## Things to Investigate Further

- P0 (Dog Balloon Animal Piggy Bank), is the Q4 lift seasonal demand or just better ad timing? SQP search volume will confirm.
- P0 (Dog Balloon Animal Piggy Bank), buy box dropped from 97% to 85% in March 2026. Need to verify at the child level (per workflow domain note) whether this is a real issue or a parent-level dilution from one underperforming child.
- P1 (Custom Vanity Set), confirm buy box is broken at the child level too, and identify which child SKU(s) are losing buy box. Cross-reference with pricing/MAP.
- P2 (Noah's Ark Coin Bank), only 110 sessions in March despite $675 in sales. Where is this traffic coming from (search query? product targeting?) and what's the ceiling if we double or triple ad spend?

## Questions for the Seller

- **P1 (Custom Vanity Set)**, buy box is at 1-2% despite this being your private-label product. Have there been recent price changes, MAP violations, or anyone else listing on the ASIN? This is likely the single highest-impact fix in the account.
- **P0 (Dog Balloon Animal Piggy Bank)**, does the Dog Balloon Animal piggy bank typically sell harder around any specific holidays (Easter, baby showers, graduation, Christmas)? Want to confirm whether the volatility we see is seasonal or ad-driven.
- **All P0/P1/P2/P3**, when did you start running ads on each of these products? Our data only goes back to early February. Knowing when the ad ramp actually started will let us judge how much of the recent lift is real growth vs. just the ad data appearing.
