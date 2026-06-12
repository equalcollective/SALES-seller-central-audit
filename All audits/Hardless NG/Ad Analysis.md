# Ad Analysis - Hardless NG

**Window:** Feb 15 to May 14, 2026 (89 days, the full available ad window). Status filter: ENABLED (currently-active campaigns). Account total: **$7,811 spend, $16,788 sales, 2.15 ROAS**.

## Account Level

### Campaign Structure

> **Finding: The account is cluttered with dormant campaigns, and nearly all real spend sits in a handful of "OMNI" campaigns.**
>
> **Problem:**
> - 67 enabled campaigns, but only ~11 carry meaningful spend. 54 campaigns spent under $50 in 89 days and 53 spent under $10. They are effectively dead weight (mostly old SP campaigns) that make the account hard to manage and read.
> - The top 10 campaigns hold **95.8%** of all spend. The structure is one tight cluster of active "OMNI" campaigns surrounded by ~56 dormant SP shells.
>
> **Solution:**
> - Archive or consolidate the dormant sub-$10 campaigns so the account reflects what is actually running.
> - Rebuild around a clean structure: separate NG4 vs NG4L, separate the converting salt-free/whole-house terms into their own campaigns with dedicated budgets (see Profitability and Blocker sections).
>
> **Impact:** Cleaner reads and bid control. The real money problems are in the active OMNI campaigns below, which the clutter currently hides.

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | CPC | CVR |
|----------------|--------|-------|-------|------|-----|-----|
| Automatic | 1,057 | $1,760 | $2,499 | 1.42 | $1.67 | 0.85% |
| Manual | 3,518 | $6,051 | $14,289 | 2.36 | $1.72 | 1.34% |

Healthy. Manual drives 77% of spend at a stronger 2.36 ROAS, auto is a smaller discovery channel at 1.42. The harvest-and-scale direction is correct. No action needed here.

### Campaign Profitability

> **Finding: About 75% of ad spend is running below break-even, concentrated in the NG4 (regular hard water) lines.**
>
> **Problem:**
> - 8 campaigns with meaningful click volume are below 1.5x ROAS, spending a combined **$5,894** (roughly three-quarters of the $7,811 account spend) and returning only ~$5,770 in sales (about 0.98x).
> - The bleed is concentrated in the **NG4** variant. The NG4L (extra hard water) equivalents convert.

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| OMNI Manual ASIN - NG4 | $2,623 | $3,022 | 1.15 | 1,674 | 8 |
| OMNI Manual KW - NG4 | $1,565 | $1,048 | 0.67 | 866 | 2 |
| OMNI Auto - Complements - NG4 | $849 | $776 | 0.91 | 406 | 4 |
| OMNI Manual ASIN - NG4L | $486 | $647 | 1.33 | 276 | 2 |
| OMNI Auto - Close Match - NG4L | $122 | $98 | 0.80 | 72 | 1 |
| OMNI Auto - Substitutes - NG4 | $92 | $0 | 0.00 | 87 | 0 |
| **Total wasted** | **~$5,894** | | | | |
>
> For contrast, the campaigns that **work**: OMNI Manual KW - NG4L ($1,085 at **3.45** ROAS, 10 orders) and the self-ASIN defensive campaign ($173 at **26.1** ROAS, 22 orders, driven by cartridge halo).
>
> **Solution:**
> - Pause or rebuild the NG4 keyword and complements campaigns (the $1,565 at 0.67 and $849 at 0.91 are clear bleeders with enough clicks to call).
> - Reallocate to the proven NG4L keyword structure and the salt-free/whole-house converting terms.
>
> **Impact:** Reallocating even half of the ~$5,894 from ~1.0x ROAS to the proven ~3.45x NG4L structure would roughly triple the return on that spend. The same budget would do materially more. Exact figures firm up once business-report margins are connected.

### Targeting Strategy

**Keyword vs Product Targeting:**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|-------------------|--------|-------|-------|------|-----|-----|-----|
| Product Targeting | 2,603 | $4,364 | $9,135 | 2.09 | $247 | $1.68 | 1.42% |
| Keyword Targeting | 1,973 | $3,450 | $7,653 | 2.22 | $402 | $1.75 | 0.96% |

Roughly balanced and both healthy (~2.1 to 2.2 ROAS). Product targeting (heavily self-ASIN defensive plus competitor ASINs) drives more orders at higher CVR; keyword targeting has higher AOV. No imbalance to act on.

**Match Type Breakdown:**

| Match Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|------------|--------|-------|-------|------|-----|-----|-----|
| EXACT | 1,388 | $2,674 | $4,785 | 1.79 | $399 | $1.93 | 0.86% |
| PHRASE | 38 | $62 | $1,323 | 21.5 | $441 | $1.62 | 7.89% |
| BROAD | 33 | $26 | $0 | 0.00 | n/a | $0.80 | 0% |

Keyword spend is almost entirely EXACT, at a soft 1.79 ROAS and 0.86% CVR. The tiny PHRASE sliver printed at 21.5x (3 orders from 38 clicks, too small to lean on but worth scaling carefully). The takeaway: the exact-match keyword list is converting weakly, which ties back to the SQP finding that the broad "water softener" terms draw clicks but not sales. Match-type is not the lever; keyword **selection** is (see Blocker section).

## Product Level (P0)

### P0 Campaign Map

P0 (Whole House Water Filter) is **99% of account ad spend** ($7,739 of $7,811). The map is the OMNI cluster split by variant:

| Campaign group | Spend | Sales | ROAS | Read |
|----------|-------|-------|------|------|
| NG4 manual + auto (ASIN, KW, complements, substitutes) | ~$5,200 | ~$4,900 | ~0.94 | The bleed |
| NG4L manual + auto (KW, ASIN, loose/close match) | ~$2,100 | ~$5,400 | ~2.6 | The performer |
| Self-ASIN defensive (cartridge halo) | $173 | $4,512 | 26.1 | Healthy, keep |

The single clearest pattern: **NG4L spend converts, NG4 spend does not.** Whatever the reason (NG4L = extra hard water buyers have sharper intent, or the NG4 listing/price is weaker), the budget is currently weighted toward the losing variant.

### Blocker-Specific Findings

#### CVR Blocker (Tier 1): Where the spend goes vs where it converts

> **Connecting to SQP:** Section 4 (SQP) identified CVR as the primary Tier 1 blocker, conversion, not clicks. The ad data confirms it and shows that even within paid traffic, the brand wins clicks on broad terms and loses the sale.
>
> **Problem (search-term level, top spenders):**

| Search Term | Spend | Sales | ROAS | Clicks | Orders | Read |
|-------------|-------|-------|------|--------|--------|------|
| b07f175c2r (competitor ASIN) | $906 | $1,347 | 1.49 | 585 | 3 | High spend, weak conversion |
| water softener (broad) | $464 | $89 | 0.19 | 298 | 1 | Burning money: shoppers want salt softeners |
| water softener system | $292 | $549 | 1.88 | 167 | 1 | Marginal |
| whole house water softener | $270 | $1,545 | 5.72 | 109 | 4 | **Converts well (matched intent)** |
| salt free water softener system | $65 | $597 | 9.24 | 33 | 2 | **Converts well (matched intent)** |
| whole house water filter | $96 | $399 | 4.15 | 57 | 1 | **Converts (Tier 2 whitespace)** |
| hardless ng4 whole house water filter | $49 | $1,471 | 29.7 | 19 | 4 | Branded, prints |
| hard water filter | $87 | $0 | 0 | 54 | 0 | Pure waste |
| well water filter | $52 | $0 | 0 | 27 | 0 | Pure waste |
| water filter system | $45 | $0 | 0 | 24 | 0 | Pure waste |
>
> The pattern is unmistakable: **specific, matched-intent terms convert at 4x to 9x ROAS** (`whole house water softener`, `salt free water softener system`, `whole house water filter`), while **generic and mismatched terms bleed** (`water softener` at 0.19, `hard water filter` and `well water filter` at 0.00). Roughly $700+ across the top search terms is on terms returning under 1.0 ROAS.
>
> **Solution:**
> - Negate the mismatched generics (`hard water filter`, `well water filter`, `water filter system`, plain `water softener` where it does not convert) and the irrelevant salt/cleaner terms surfaced in SQP.
> - Pull the proven converters into their own dedicated, well-funded exact campaigns: `whole house water softener`, `salt free water softener system`, `whole house water filter`.
> - Hold a small branded-defense campaign (the `hardless ng4...` terms already print at 29x; keep this small, under ~5% of budget, it protects existing demand and is not a growth lever).
>
> **Impact:** Stops the ~$700+ of clearly wasted search-term spend and concentrates budget on terms already proving 4x to 9x ROAS. Combined with the campaign-profitability reallocation, the same ad budget should generate materially more sales. This is the PPC half. The listing half (rating + salt-free perception from Step 2) is what unlocks scaling beyond the matched terms.

#### Impression-Share Blocker (Tier 2): Placement, the fastest visibility win

> **Connecting to SQP:** Section 4 flagged Tier 2 (whole house water filter) as wide-open whitespace (0.05% impression share). The most immediate visibility lever is placement, because the brand's best-converting placement is starved of budget.
>
> **Problem (placement, seller level):**

| Placement | Spend | Sales | ROAS | CTR | CVR | Share of Spend |
|-----------|-------|-------|------|-----|-----|---------------|
| Top of Search | $565 | $3,018 | **5.34** | 4.41% | 4.48% | 7.2% |
| Rest of Search | $4,749 | $4,924 | 1.04 | 0.77% | 0.44% | 60.8% |
| Product Pages | $2,470 | $3,105 | 1.26 | 0.23% | 0.84% | 31.6% |
| Off Amazon | $6 | $0 | 0 | 0.52% | 0% | 0.1% |
>
> Top of Search converts at **4.48% CVR and 5.34 ROAS** (10x the CVR of Rest of Search) but receives only **7% of spend**. Meanwhile Rest of Search eats **61% of budget at a near-break-even 1.04 ROAS**.
>
> **Solution:**
> - Increase Top-of-Search bid modifiers / placement bids to shift budget from Rest of Search to Top of Search.
> - This simultaneously raises impression share on the Tier 2 "whole house water filter" terms (visibility) and improves blended ROAS (Top of Search converts far better).
>
> **Impact:** Illustratively, moving $1,000 from Rest of Search (1.04 ROAS, ~$1,040 sales) to Top of Search, even assuming ROAS compresses from 5.34 to a conservative ~3.0 as volume rises, would yield ~$3,000 sales, roughly **+$2,000 per period** from the same spend, plus the visibility gain on the whitespace tier.

## Insights

- **P0 ad spend is misallocated by variant and placement, not by structure type.** Auto/manual and keyword/product splits are healthy. The money is leaking through (1) the NG4 lines at ~0.94 ROAS vs NG4L at ~2.6, (2) Rest of Search holding 61% of budget at 1.04 ROAS while Top of Search prints 5.34, and (3) generic "water softener / hard water filter" search terms that draw clicks but not sales.
- **The converting terms are already visible in the data.** `whole house water softener`, `salt free water softener system`, and `whole house water filter` run 4x to 9x ROAS on tiny budgets. The growth plan is to defund the bleeders and concentrate here.

## Questions for the Seller

- The NG4 (regular hard water) campaigns convert far worse than the NG4L (extra hard water) campaigns. Is there a known difference in price, reviews, or demand between the two variants, or should we simply rebalance budget toward NG4L? Knowing this avoids us pausing a variant you have a strategic reason to push.
