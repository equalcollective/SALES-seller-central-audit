# SQP Analysis - P0 (Terminal Velocity Sport)

**Product analyzed:** P0 = Motorcycle Cell Phone Mount with Dual USB-C (B0F2VQDVHM family)
**Period:** Trailing 3 months (Feb to Apr 2026), monthly granularity. April 2026 used for headline numbers; trend confirmed across all three months.

## Step 3a: Tagging

### Tier 1 (Hero) - Charger-inclusive intent
The wedge keywords that match P0's distinctive feature (integrated USB-C charger). Highest match between query intent and product positioning.

- motorcycle phone mount with charger
- motorcycle phone charger
- motorcycle usb charger
- phone charger for motorcycle
- motorcycle wireless phone charger

**Rationale:** These buyers explicitly want a phone holder with charging or a motorcycle charger. P0's integrated dual USB-C charger is the differentiator vs. mount-only competitors.

### Tier 2 (Core market) - Generic motorcycle phone mount
Largest-volume queries for the broader product category. P0 fits, but competes against cheaper mount-only products on these terms.

- motorcycle phone mount
- motorcycle phone holder
- phone holder for motorcycle
- phone mount for motorcycle
- motorcycle cell phone holder
- cell phone holder for motorcycle

**Rationale:** Core market for motorcycle phone mounts. P0 is technically relevant but competes at a price premium because it includes the charger; buyers on these terms may not value the charger and will pick the cheaper option.

### Tier 3 (Broad / adjacent)
Top-of-funnel motorcycle accessories searches plus bicycle/snowmobile cross-over. Volume is huge but purchase intent for a phone mount specifically is low.

- motorcycle accessories
- motorcycle accessories for men
- motorcycle accessories for women
- harley davidson accessories
- harley accessories
- indian motorcycle accessories
- snowmobile phone mount
- accesorios para motos
- accesorios para moto

**Rationale:** Adjacent intent. The buyer searching "motorcycle accessories" may want anything from saddlebags to gloves to lights. P0 is relevant but only one of many possible answers. Industry CVR on these queries is 0.5-2%, vs. ~10% on Tier 1/2.

### Excluded from tagging
- Bicycle phone-mount queries ("bike phone mount", "bike phone holder", "bicycle phone mount", "phone holder for bike", "porta celular para bicicleta") - bicycle fit-out, not motorcycle. Product CAN fit a bike but the SAE charging connector is irrelevant for bicycle riders. Bicycles get the bicycle-specific stem-piece SKUs (not P0).
- LED Wings / underglow queries ("motorcycle underglow kit", "motorcycle lights", "motorcycle led underglow kit", "led lights for motorcycles", "motorcycle lights underglow kit", "motorcycle underglow") - these belong to P2 (American Eagle LED Wings), not P0.
- Branded queries - none with meaningful volume appeared in the trailing 3-month data. Brand awareness is essentially zero, which is consistent with the small revenue scale.

## Step 3b: Catalog Overlap Check (Impression Share Cap Adjustment)

P0 sits in a catalog with **5 motorcycle phone mount parents** (B0F2VQDVHM, B0DY5DPK2G, B0FY4DC95Z, B0DJCM5S7Y, B0DY5J2MRR). For SQP purposes, all five contribute brand-level impressions on the same phone-mount queries because SQP is brand-level, not ASIN-level.

| Tier | Brand products that could rank | Adjusted impression share cap |
|------|-------------------------------:|------------------------------:|
| Tier 1 (with charger) | 1 product fits cleanly (P0) | ~8-9% |
| Tier 2 (generic mount) | 5 products fit | ~25-27% |
| Tier 3 (broad) | ~5 products fit | ~25-27% |

## Step 3c: Market Sizing (April 2026)

| Tier | Monthly Search Volume | Monthly Industry Clicks | Monthly Industry ATCs | Monthly Industry Purchases | Est Market Size ($/mo @ $22 AOV) |
|------|----------------------:|------------------------:|----------------------:|---------------------------:|---------------------------------:|
| Tier 1 (with charger) | 21,241 | 9,553 | 2,046 | 780 | $17,160 |
| Tier 2 (generic mount) | 161,209 | 64,047 | 16,401 | 7,036 | $154,792 |
| Tier 3 (broad) | 331,803 | 180,777 | 21,006 | 2,529 | $55,638 |
| **Total P0 addressable** | **514,253** | **254,377** | **39,453** | **10,345** | **~$227,590** |

Estimated using $22 average product price (current AOV; aligns with category competitive pricing).

**Reality check:** Tier 2 is by far the biggest pot ($155K/mo), but P0's price-premium positioning means it captures a small share of this pot. Tier 1 is small but is the product's natural battlefield ($17K/mo, 780 purchases). Tier 3 is enormous in volume but has 0.5-2% industry CVR, so the $-equivalent opportunity is small.

## Step 3d: Brand Funnel Performance (April 2026)

| Tier | Brand Impressions | Brand CTR (vs Industry) | Brand ATC Rate (vs Industry) | Brand CVR (vs Industry) | Brand Impression Share | Share Cap | Headroom |
|------|------------------:|------------------------:|----------------------------:|------------------------:|-----------------------:|----------:|---------:|
| Tier 1 | 4,988 | 1.9% (vs 1.8%) ✅ | 8.4% (vs 21.4%) ⚠️ | 2.1% (vs 8.2%) ⚠️ | 0.94% | ~8-9% | ~7-8 pts |
| Tier 2 | 3,834 | 2.6% (vs 1.7%) ✅ | 11.1% (vs 25.6%) ⚠️ | 1.0% (vs 11.0%) ⚠️ | 0.10% | ~25-27% | ~25 pts |
| Tier 3 | 8,639 | 1.7% (vs 2.2%) ⚠️ | low base | 0.7% (vs 1.4%) ⚠️ | 0.11% | ~25-27% | ~25 pts |

Note on statistical significance: brand purchases are 1-2 per tier per month, so brand CVR is noisy. CTR has hundreds of clicks per tier, so that signal is reliable. ATC rate is in between (40-100 ATCs at the brand level total per tier per quarter).

## Step 3e: Blocker Identification

### Tier 1 (with charger): IMPRESSION SHARE first, CVR second
- Brand CTR (1.9%) is competitive with industry (1.8%). When the listing appears in search, it gets clicked at industry rate. **CTR is not a blocker.**
- Brand impression share is 0.94% against a ~8-9% cap. **~7-8 percentage points of impression headroom.** Big lever.
- Brand ATC rate and CVR are well below industry, which is a real but secondary issue.
- **Primary growth path:** Bid into Tier 1 keywords to capture more impression share. CTR will hold and even if CVR stays at current 2.1%, more impressions = more clicks = more purchases at a constant rate.
- Per CLAUDE.md domain knowledge, however, "low impression share + poor CVR" pattern means CVR should be fixed first (or in parallel) to avoid burning ad budget. Tier 1 CVR gap is moderate (2.1% vs 8.2% = 4x). Fixable via listing improvements (Step 2e opportunities) and listing comparison copy.

### Tier 2 (generic mount): IMPRESSION SHARE
- Brand CTR (2.6%) outperforms industry (1.7%) - the listing is clicked when it shows up. **CTR is not a blocker.**
- Brand impression share is 0.10% against an adjusted ~25-27% cap. **~25 percentage points of headroom.**
- Brand CVR (1.0%) is **11x below industry** (11.0%). This is the key issue: P0 is priced and positioned as a premium product (mount + charger), but on the generic "motorcycle phone mount" query buyers compare against cheaper mount-only options and don't pick P0.
- **Primary blocker = impression share + CVR.** The CVR gap is so large on Tier 2 that simply scaling impressions would burn ad budget. Per CLAUDE.md "low impression share + poor CVR" path: address CVR first via listing positioning, then scale.
- **Realistic path:** Tier 2 is a CVR fix project. Without the listing change (clearer "this replaces 2 products" positioning), bidding hard on Tier 2 will only generate clicks that don't convert.

### Tier 3 (broad): Limited near-term opportunity
- Brand CTR slightly below industry (1.7% vs 2.2%) on extremely broad terms.
- Industry CVR is 0.5-1.4% across these queries. Even the leaders don't convert well here. Tier 3 is brand-discovery traffic, not buyer-ready traffic.
- **Not a near-term growth lever.** Worth a small budget for brand exposure, but not where to invest the next dollar.

### Overall summary
**Tier 1 is the priority.** It's the natural fit for the product, brand CTR is winning, and the impression-share opportunity is ~7-8 percentage points (roughly 8x current). Tier 2 is the next milestone after CVR is addressed via listing work.

## Step 3f: ICAP Funnel Visualization (Tier 1)

```
graph TD
    A["🔍 Impressions
    Share: 0.94% (of ~8-9% max)
    ⚠️ PRIMARY BLOCKER"] --> B["👆 Clicks
    CTR: 1.9% vs 1.8% industry
    ✅ Healthy"]
    B --> C["🛒 Add to Cart
    ATC Rate: 8.4% vs 21.4% industry
    ⚠️ SECONDARY BLOCKER"]
    C --> D["💰 Purchases
    CVR: 2.1% vs 8.2% industry
    ⚠️ SECONDARY BLOCKER"]

    style A fill:#ff6b6b,color:#ffffff
    style B fill:#51cf66,color:#ffffff
    style C fill:#ffd43b,color:#000000
    style D fill:#ffd43b,color:#000000
```

## Step 3g: Seasonality

Search volume for the head Tier 2 query "motorcycle phone mount" went from 54,615 (Feb 2026) to 101,562 (Mar) to 114,799 (Apr) - a **2.1x ramp Feb to Apr**. Same pattern on "motorcycle accessories" (144K → 207K). Riding-season seasonality is confirmed. May to Sep are likely to be peak months.

**Implication for action plan:** the next 4-5 months (May-Sep) are the highest-demand period. Whatever fixes are made in the next 8 weeks will land in the heart of the season, so the timing of the engagement is favorable.

## Insights

- **Primary blocker on P0 across all tiers is impression share.** The brand is essentially invisible on its natural keywords: 0.10% share on Tier 2 (against a ~25% cap), 0.94% on Tier 1 (against ~8% cap). When the brand DOES appear, it gets clicked at industry rate or better, so the listing's outside-the-PDP packaging is working.
- **Tier 1 (charger-inclusive keywords) is the highest-leverage near-term opportunity.** The product was built for this niche and the brand is already winning at the CTR stage. Filling out the impression share alone could 5-8x P0's volume from these keywords.
- **CVR is broken on Tier 2 (1.0% vs 11.0% industry).** The brand shows up on broad "motorcycle phone mount" queries but loses to cheaper mount-only options. Scaling Tier 2 impressions without first fixing the PDP positioning will burn budget. Per the listing diagnostics (Step 2e), the fixes are concrete: rewrite/move the caveats bullet, add a "mount + charger replaces 2 products" comparison module, fix the title typo.
- **Branded search is effectively zero.** No "terminal velocity sport" or "TV sport" queries appeared in the trailing 3-month top 60. Brand awareness has not been built. There is no current need for a branded defense campaign, only the right to keep it minimal (<3% of budget) when ads scale later.
- **Catalog has multiple sibling phone-mount parents** (B0DY5DPK2G, B0DJCM5S7Y, B0DY5J2MRR, B0FY4DC95Z) which all contribute to brand-level SQP impressions but fragment ad-spend efficiency at the ASIN/campaign level. Consolidation discussion belongs in Step 4 / action plan.

## Things to Investigate (forward into Step 4)

- Whether current ad spend is concentrated on Tier 1 (correct) or scattered across Tier 2/Tier 3 (waste). Specifically, does the ad data show high-spend search terms that match Tier 2 "motorcycle phone mount" broad queries with poor ROAS?
- Whether ad-driven brand impressions on Tier 2 are converting at industry rate or at the broken 1.0% rate. If 1.0%, that confirms the listing CVR issue.
- Whether any current spend goes to bicycle keywords (which P0 is poorly suited for due to the SAE 12V connector). Wasted targeting.

## Questions for the Seller

- The product is built around the integrated charger ("mount + charger in one"). When ads were turned on in February, did the team intentionally target charger-inclusive keywords (e.g., "motorcycle phone mount with charger") or were broad "motorcycle phone mount" queries also bid on? The CVR data suggests the latter is where most spend went - we want to confirm.
- You have four colorways and a separate root B0F2VQDVHM listing. Customers searching for "motorcycle phone mount with charger" are seeing roughly 5,000 brand impressions/month split across these. Do you have a view on whether one color clearly outperforms (so we can focus PPC there)?
