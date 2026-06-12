# Step 4: Ad Analysis - Creative Gifts International

**Time window:** Feb 1 - Apr 21, 2026 (the full ad data window of 80 days, since the data only goes back ~90 days)

## Account-Level Analysis

### Campaign Structure

The seller has 7 enabled campaigns. 6 are auto-targeting, 1 is a manual campaign (Brush Sets) that has 4 impressions and zero spend (essentially dormant). There are no functioning manual keyword campaigns in the entire account.

> **Finding: There is no manual ad targeting in the account.**
>
> **Problem:**
> - Manual targeting: 4 impressions, 0 clicks, $0 spend over 80 days. Effectively non-existent.
> - Automatic targeting: 600,115 impressions, 4,345 clicks, $1,587 spend, $3,303 sales, ROAS 2.08.
> - The seller is letting Amazon's algorithm pick the keywords. There is no way to bid harder on the queries that matter (dog piggy bank, ceramic piggy bank, balloon dog) because no keyword has its own campaign.
> - This is the structural reason for the 0.59% impression share on Tier 1 queries identified in Section 4 (SQP Analysis).
>
> **Solution:**
> - Build manual keyword campaigns for each P0 tier from the SQP analysis (3 campaigns minimum: Tier 1 hero, Tier 2 broad piggy bank, Tier 3 balloon dog decor, once the listing supports it).
> - Limit each campaign to 3-5 keywords with dedicated bids.
> - Harvest top-performing search terms from auto into manual exact campaigns and negate them from auto so spend does not duplicate.
>
> **Impact:**
> - The "All Products | Auto | SP" campaign is currently doing $782 spend → $2,300 sales at 2.94 ROAS. The terms inside it (e.g. "dog piggy bank," "balloon dog") are converting at the auto level. Moving the top converters to manual exact at controlled bids typically lifts ROAS by 30-50% per [CLAUDE.md](./CLAUDE.md), so the same $782 could reasonably do $2,990 - $3,450 in sales (a $700-$1,150 lift) once harvested.

### Auto vs Manual Split

| Targeting Type | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|----------------|--------|-------|-------|------|-----|-----|-----|
| Automatic | 4,345 | $1,586.52 | $3,303.00 | 2.08 | $30.30 | $0.37 | 2.51% |
| Manual | 0 | $0.00 | $0.00 | 0 | n/a | n/a | n/a |

100% of working ad spend is on auto. Covered above under Campaign Structure.

### Campaign Profitability

3 of the 7 enabled campaigns are unprofitable, plus a 4th (Manual Brush Set) that exists but is not running.

| Campaign | Spend | Sales | ROAS | Clicks | Orders |
|----------|-------|-------|------|--------|--------|
| Wedding Products \| Auto \| SP | $112.48 | $0.00 | 0.00 | 195 | 0 |
| SP \| Easter - Bunny Boards/Banks | $211.40 | $123.96 | 0.59 | 335 | 5 |
| Children and Baby Gifts \| Auto \| SP | $178.94 | $224.93 | 1.26 | 359 | 9 |
| **Total wasted** | **$502.82** | **$348.89** | **0.69** | | |

> **Finding: 32% of ad spend is on unprofitable campaigns.**
>
> **Problem:**
> - $502.82 spent on campaigns running below the 1.5x ROAS profitability floor over the past 80 days.
> - Wedding Products: 195 clicks, 0 orders. Not a marginal call, just not converting at all.
> - Easter - Bunny Boards/Banks: ROAS 0.59. Seasonal campaign that's still running well past Easter (Apr 5, 2026), it should have ended weeks ago.
> - Children and Baby Gifts: ROAS 1.26. Has volume (359 clicks) but is not paying back.
>
> **Solution:**
> - Pause Wedding Products and Easter - Bunny Boards/Banks immediately.
> - Restructure Children and Baby Gifts: cut spend on the products that are not converting and re-target around the sippy cup and Noah's Ark coin bank, which are the children/baby products that *do* convert (sippy cup ROAS in the dedicated Bottles/Cups/Mugs campaign is 2.55).
>
> **Impact:**
> - Reallocating the $502.82 to All Products Auto SP at its current 2.94 ROAS would generate **$1,478 in additional sales**. Net gain: $1,129 in sales for the same total ad budget.

### Targeting Strategy

**Keyword vs Product Targeting:**

| Targeting Strategy | Clicks | Spend | Sales | ROAS | AOV | CPC | CVR |
|-------------------|--------|-------|-------|------|-----|-----|-----|
| Keyword Targeting | 2,861 | $1,114.32 | $2,237.30 | 2.01 | $31.07 | $0.39 | 2.52% |
| Product Targeting | 1,913 | $743.70 | $1,244.63 | 1.67 | $28.29 | $0.39 | 2.30% |

Keyword targeting is materially better (ROAS 2.01 vs 1.67). Product targeting at $744 is being underserved relative to its return, and most of that product targeting spend is the two "Conquesting" campaigns (Pearhead, Child to Cherish) that we'll dig into at the P0 level.

**Match Type Breakdown:** All match types (EXACT, PHRASE, BROAD) report 0 clicks and 0 spend over the period. Match type is a manual-targeting concept; since the account has no working manual targeting, this table is structurally empty. Once manual campaigns launch, this becomes a live metric.

### Placement Performance (Account-Level)

| Placement | Impressions | Clicks | Spend | Sales | ROAS | CTR | CVR |
|-----------|-------------|--------|-------|-------|------|-----|-----|
| Top of Search | 7,133 | 192 | $102.76 | $317.90 | **3.09** | 2.69% | 6.25% |
| Rest of Search | 202,066 | 2,285 | $943.93 | $1,790.44 | 1.90 | 1.13% | 2.80% |
| Product Pages | 415,483 | 2,186 | $791.03 | $1,333.59 | 1.69 | 0.53% | 1.78% |
| Off Amazon | 29,445 | 109 | $19.51 | $0.00 | 0.00 | 0.37% | 0.00% |

> **Finding: Top of Search is the best placement by a wide margin and is being severely underfunded.**
>
> **Problem:**
> - Top of Search ROAS 3.09, Product Pages ROAS 1.69. Top of Search converts at 6.25% vs 1.78% on Product Pages, a 3.5x gap.
> - Despite that, only 6.5% of spend ($103 of $1,587) is hitting Top of Search. The bulk is going to Product Pages and Rest of Search.
> - Off Amazon spend is wasted, 0 sales on 109 clicks. Should be disabled.
>
> **Solution:**
> - Increase Top of Search bid modifiers on the auto campaigns to push more spend to that placement.
> - Once manual keyword campaigns are built (per the campaign structure finding), set them with aggressive Top of Search modifiers from day one.
> - Disable Off Amazon placement on all campaigns.
>
> **Impact:**
> - If half of the Product Pages spend ($396) shifts to Top of Search at its current 3.09 ROAS, expected sales from that bucket move from $668 to $1,222. Net gain: ~$554 in sales.

## Product-Level Analysis (P0)

### P0 Campaign Map

| Campaign | Type | Spend | Sales | ROAS | Clicks | Orders |
|----------|------|-------|-------|------|--------|--------|
| All Products \| Auto \| SP | Auto | $121.46 | $335.86 | 2.77 | 428 | 15 |
| Child to Cherish Piggy Banks \| Conquesting \| SP | Product Targeting | $21.26 | $23.99 | 1.13 | 25 | 1 |
| Pearhead Piggy Banks \| Conquesting \| SP | Product Targeting | $19.10 | $0.00 | 0.00 | 23 | 0 |
| Piggy Bank \| Auto \| SP | Auto | $5.96 | $23.99 | 4.02 | 28 | 1 |
| **Total P0** | | **$167.78** | **$383.84** | **2.29** | 504 | 17 |

P0 receives only 11% of total account ad spend ($168 of $1,587) despite being the brand's #1 revenue product. There is no manual keyword campaign for P0 anywhere.

### Impression Share Blocker: P0 Has No Manual Keyword Campaigns Bidding on Tier 1 Terms

Section 4 (SQP) identified impression share as the primary blocker on Tier 1 (0.59% of a ~12-15% cap). The PPC lever is bidding on the keywords where impression share is low. The ad data shows that lever is not being pulled at all:

- The "Piggy Bank | Auto | SP" campaign is the only campaign whose name suggests piggy-bank intent, but it is auto-targeted (not keyword-targeted) and only spent **$5.96 on P0 over 80 days**. Auto targeting cannot be controlled to bid hard on "dog piggy bank" or "ceramic piggy bank."
- "All Products | Auto | SP" is doing the heavy lifting ($121 spend, ROAS 2.77 on P0). It works but is spread across the entire catalog and cannot be tuned for a specific Tier 1 term.
- There are zero exact-match or phrase-match keyword campaigns for "dog piggy bank," "ceramic balloon dog," or "ceramic piggy bank."

> **Finding: The impression share blocker has a clear, untouched PPC lever, there is no manual keyword campaign for P0.**
>
> **Problem:**
> - Tier 1 impression share is 0.59% against a ceiling of ~12-15%. The market has 590 cart adds/month available; P0 captures essentially none.
> - The mechanism for fixing this (manual keyword campaigns with dedicated budgets) does not exist in the account.
>
> **Solution:**
> - Build a "P0 | Tier 1 | Exact" manual campaign with three keywords: dog piggy bank, ceramic balloon dog, ceramic piggy bank. Aggressive Top of Search bid modifier from day one.
> - Build a smaller "P0 | Tier 1 | Phrase" campaign for discovery on long-tail variations.
> - This must be sequenced *after* the listing CVR fixes from Section 2 land, otherwise the impressions feed a leaky funnel.

### CVR Blocker: Conquesting Campaigns and Non-Gold Variants Are Wasted Spend

Section 4 (SQP) also identified CVR as a co-primary blocker on Tier 1 (cart-to-purchase 7.7% vs 21.8% industry). Section 2 narrowed the cause to the variant-level conversion gap (Gold converts at 34.83%, other colors at 1-6%). The ad data shows the spend pattern across variants:

| Color | Clicks | Spend | Sales | Orders | CVR |
|-------|--------|-------|-------|--------|-----|
| Rose Gold | 156 | $46.04 | $143.94 | 6 | 3.85% |
| Pink | 109 | $40.10 | $71.97 | 3 | 2.75% |
| Black | 53 | $18.55 | $0.00 | 0 | 0.00% |
| Blue | 50 | $17.36 | $0.00 | 0 | 0.00% |
| Gold | 47 | $14.91 | $23.99 | 1 | 2.13% |
| Silver | 41 | $8.50 | $71.97 | 3 | 7.32% |
| White/Gold | 27 | $10.11 | $47.98 | 3 | 11.11% |
| **Total P0** | **483** | **$155.57** | **$359.85** | **16** | **3.31%** |

Two distinct problems:

1. **Gold gets less ad budget than every selling color except Silver/White/Gold.** Step 2 showed Gold is the conversion hero (34.83% CVR organic), but in the ad data Gold has only $15 of spend and 47 clicks. Rose Gold and Pink are getting 3-4x the ad budget despite converting at 1/10th the rate of Gold organic.
2. **Conquesting campaigns are mostly wasted.** Pearhead Conquesting: $19.10 / 0 orders. Child to Cherish Conquesting: $21.26 / 1 order at ROAS 1.13. These product-targeting campaigns are placing P0 ads on competitor product detail pages, but customers who clicked through aren't converting.

> **Finding: Ad budget on P0 is misallocated across variants and wasted on conquesting campaigns.**
>
> **Problem:**
> - Conquesting campaigns: $40.36 spend, 1 order. ROAS 0.59 combined. Lost money.
> - Gold variant (the conversion hero) gets the smallest ad share among the colors that actually sell.
> - Non-Gold colors (Black, Blue, Pink, Rose Gold) collectively absorbed $122 in spend but converted at <4% CVR.
>
> **Solution:**
> - Pause both Conquesting campaigns until the listing is repositioned (the conquesting strategy works only if the click-through experience converts; right now it doesn't).
> - In the new manual Tier 1 campaign, advertise Gold as the headline variant only. Let the variant picker on the listing surface the other colors organically.
> - On auto campaigns, add the under-converting variants as negative ASINs for the time being or set very low default bids.
>
> **Impact:**
> - Reallocating the $40 conquesting + ~$80 of non-Gold variant spend (~$120 total) to a Gold-led Tier 1 manual campaign at the auto-level ROAS of 2.94 would generate ~$352 in sales (vs the $24 those campaigns produced). Net gain on this single P0 reallocation: ~$330.

## Insights

- **Account-level, the entire $1,587 of working ad spend is on auto-targeted campaigns. Manual keyword targeting does not exist in the account.** This is the structural cause of low Tier 1 impression share, and it's a single fix (build manual campaigns) rather than a series of optimizations.
- **Account-level, Top of Search has 3.09x ROAS but only 6.5% of spend.** Bidding it up is one of the highest-leverage actions in the entire audit.
- **Account-level, $502.82 (32% of spend) is on three unprofitable campaigns, including an Easter campaign still running 3 weeks after Easter.** Easy reclaim.
- **P0 (Dog Balloon Animal Piggy Bank), the conquesting campaigns (Pearhead, Child to Cherish) cost $40 over 80 days and produced 1 order.** Pause and reallocate. They are unwinnable until the listing is repositioned to convert the audience that lands from competitor product pages.
- **P0 (Dog Balloon Animal Piggy Bank), Gold converts ~10x better than the other colors organically but receives the smallest ad share.** Concentrating ad spend on Gold is a quick CVR-side win that requires no listing change.

## Things to Investigate Further

- Once manual campaigns launch, watch Tier 2 ("piggy bank," "piggy bank for adults") performance closely. Tier 2 is a $725k/mo market and is the long-term destination once Tier 1 + listing fixes prove the funnel.

## Questions for the Seller

- The Easter campaign was still active 3 weeks past Easter. Is this an oversight, or is there an intentional reason to keep seasonal campaigns running outside their season? This affects how we structure future seasonal campaigns (e.g., for graduation/Mother's Day).
- The two "Conquesting" campaigns target Pearhead and Child to Cherish (direct piggy bank competitors). Was that strategic choice based on past performance, or was it set up speculatively? We're recommending pausing them until the listing is repositioned.
