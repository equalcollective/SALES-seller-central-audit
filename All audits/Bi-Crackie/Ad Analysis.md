# Ad Analysis - Bi-Crackie

## Data Availability

**No ad data is available in the system for Bi-Crackie.**

- `ads_day_count` from Seller Analytics: 0
- Q699 (campaign view, last 90 days, no status filter): 0 rows
- Q698 (monthly campaign performance, all time, no status filter): 0 rows

This means none of the standard account-level or product-level ad analyses can be performed: campaign structure, auto vs manual split, profitability, targeting strategy, placement, search-term wastage. There is nothing to analyze.

## What This Tells Us

Two possible interpretations of the absence:

1. **No ads have been running in the last ~90 days.** The Seller Analytics ad pull only retains the last 90 days of advertised product reports. If the seller has not run ads in this window, the system shows zero. Historical ad activity cannot be inferred.
2. **The seller has never run paid ads on Amazon, OR the ad account was never connected to the integration.** Q698 looks across all available history (no date filter) and still returns zero. This is consistent with either of those scenarios.

**What we cannot rule out:** That the seller was running ads through spring/summer 2025 and paused. The SQP data does show brand impressions ramping up from April to June 2025 (matching peak season) and then sharply dropping after July 2025 (242 brand impressions on Tier 1 in September vs 3,081 in June). This pattern is consistent with both seasonal organic ranking AND with paid campaigns being seasonally enabled.

This needs to be confirmed with the seller directly. Question for the call: have you ever run Sponsored Products / Sponsored Brands / Sponsored Display ads on Amazon? If yes, when did you last run them, what was the rough monthly spend, and which products did you advertise?

## Implications for the Audit

The biggest single growth lever for Bi-Crackie right now is **starting to advertise**, not optimizing existing ads.

From the SQP analysis, the situation is:
- The brand has 0.32% impression share on its Tier 1 hero queries against a ~16-18% achievable cap (with two SKUs ranking).
- Even at peak season last year, impression share never crossed 0.5%.
- Tier 2 (broader weed-puller market, 184k monthly searches) is essentially untouched at 0.002% impression share.
- The brand sells one product family with strong fundamentals (4.7 rating, real differentiator, 4-7% CVR in season) but no traffic mechanism beyond organic.

For a brand entering peak season (April-July) with a one-product catalog and no ad account active, the action plan in the consolidated output is structured around:
1. Listing fix first (main image), to lift CVR before paid traffic hits the PDP
2. Launch Tier 1 PPC (Sponsored Products on the 12 hero keywords) to capture visible market share immediately
3. Once Tier 1 is stable, layer in Tier 2 PPC for the larger broader-intent market

Specific PPC structure recommendations (campaign architecture, bid ranges, budget allocation, match-type strategy) cannot be data-driven from this audit because there's no historical performance to learn from. They would be set conservatively at launch and iterated weekly.

## Insights

- **No ads currently running on a one-product seasonal brand entering peak season is the highest-leverage gap in this audit.** Without ads, Bi-Crackie is dependent on organic ranking. Sales rank is currently slipping (#985 to #1,240 in Manual Weeders through April) precisely because competitors are ramping ads into season and Bi-Crackie is not.

## Questions for the Seller

- Have you ever run Sponsored Products / Sponsored Brands / Sponsored Display ads on Amazon? If yes, when did you last run them, what was the rough monthly spend, and which products did you advertise? (We have no campaign data in the system, so we need this directly from you.)
- If you have run ads before and paused them, what drove the decision to pause, was it cost concerns, ROAS, time to manage, or something else? This affects how we structure the relaunch.
