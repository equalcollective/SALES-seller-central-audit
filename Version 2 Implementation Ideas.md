# Version 2 Implementation Ideas

Ideas for improving the audit workflow, collected after each end-to-end execution. Each entry includes the idea, the specific example that triggered it, and which step it applies to.

---

## Aryan's V2 List

**8. Child variant sales split in Step 1**
- Show the percentage of parent ASIN sales that each child variant contributes. Helps identify when one child dominates or when variants are cannibalizing each other.
- Step: 1 (ASIN Selection)

**9. Ad analysis monthly trends (campaign-level)**
- Campaign report data covers 12 months, so we can show month-on-month trends at the campaign level using Q698. Useful on a product level: if a product's ad performance is declining over months and the current provider hasn't fixed it, that's a strong sales argument. Can be added as a product-level step in Step 4.
- Step: 4 (Ad Analysis, product-level)

**24. Remote audit triggering from phone/Slack**
- Trigger audits without being at the Mac. Cloud options (claude.ai/code, Slack) need MCP servers accessible from cloud. Remote Control works now but requires MacBook open. See table in conversation history for full comparison.
- Step: Entire workflow (pre-requisite infrastructure change)

**25. QA agent for audit accuracy scoring**
- Agent that reads completed audits and scores them against ~10 standardized metrics (tier relevance, blocker correctness, catalog overlap, statistical significance, action plan traceability). Outputs a cross-audit table for tracking accuracy over time.
- Step: Post-audit (standalone agent)

**26. Keepa price history for buy box diagnosis**
- Pull price history to verify MAP-related buy box suppression instead of asking the seller. Correlate price change timestamps with buy box % drops.
- Step: 1 (ASIN Selection), 2f (Historical Trends)

**27. 12-18 month ad data via campaign reports**
- Campaign reports on Metabase provide 12-18 months of month-on-month ad data. Would enable long-term ad trend analysis, identifying when ads started/stopped, and correlating with revenue changes from Step 1.
- Step: 4 (Ad Analysis)

---

## From: Sparkling White Smiles Full Audit (2026-03-22)

**14. Placement data should be pulled at the campaign level for P0, not just seller level**
- The seller-level placement data (Q706/Q737) aggregates across all campaigns, including unprofitable ones. For accounts with multiple products at very different ROAS levels, campaign-level placement data (Q705/Q740) filtered to P0 campaigns would give a more accurate picture.
- Example: Sparkling White Smiles seller-level placement showed 67% of spend on Product Pages at 0.36 ROAS, but this includes Remin Gel's 0.46 ROAS campaign.
- Step: 4f (Solving P0 Blockers via PPC)

**15. Multi-product brands with separate-product campaigns need a capital allocation section**
- When the seller has separate campaigns per product, the audit should explicitly compare campaign-level ROAS and frame the capital allocation problem as a headline finding.
- Example: Sparkling White Smiles had $13,619 on Teeth Sensitivity Kit vs $5,432 on Sport Mouth Guards. Framing this as "capital misallocation" rather than just "unprofitable campaign" made the finding more impactful.
- Step: 4c (Campaign Profitability), Final Output

**16. Brand-product mismatch worth calling out**
- When a brand's core identity doesn't match the product being audited, the listing needs to compensate harder with category-specific imagery and messaging. The mismatch affects CTR on search results.
- Example: Sparkling White Smiles is a dental whitening brand selling sport mouth guards. The main image and A+ content project "dental" not "athletic," contributing to below-industry CTR.
- Step: 2b (Brand Understanding), 2e (Listing Quality)

---

## From: Magic AutoCare Full Audit (2026-03-22)

**17. SQP CVR gap vs PDP CVR gap should be explicitly reconciled**
- When SQP brand CVR diverges significantly from Seller Analytics on-page CVR, add an explicit reconciliation. The gap is usually brand-level dilution (other products dragging down brand CVR) or cart-to-purchase abandonment.
- Example: Magic Shield's SQP CVR was 2.63% vs 5.6% PDP CVR. The ad analysis confirmed P0-specific keyword CVR was in line with PDP CVR.
- Step: 3d (Blocker Detection), 4f (Solving P0 Blockers via PPC)

**18. Child variant ROAS comparison should be standard in P0 campaign map**
- Different size variants can have dramatically different ROAS. Requires looking at Q726 at the child level, not just parent.
- Example: Magic AutoCare's 16oz Graphene Spray was the single biggest quick win ($830 improvement from shifting $1,000 in budget).
- Step: 4e (Product-to-Campaign Mapping)

**19. Perpetua/third-party tool detection should trigger specific diagnostic questions**
- When campaign naming conventions reveal a third-party management tool (Perpetua, Pacvue, etc.), flag it and adjust the campaign structure analysis.
- Example: Magic AutoCare's campaigns all followed Perpetua naming conventions. The broken harvest-and-scale loop is a common Perpetua misconfiguration.
- Step: 4a (Campaign Structure), Questions for the Seller

---

## From: SortJoy Full Audit (2026-03-26)

**20. No-ads sellers need a modified workflow path**
- When a seller has zero advertising data, Step 4 should be replaced with a "PPC Launch Plan" section that recommends campaign structure based on SQP tier data, estimates initial budget, and sequences the launch relative to listing improvements.
- Example: SortJoy had zero ad data. The Ad Analysis file became a brief note.
- Step: 4 (Ad Analysis), Action Plan

**21. DTC-first brands need a branded vs non-branded SQP split as a headline finding**
- When 90%+ of a brand's SQP cart adds come from branded search, this should be the opening frame for the entire audit.
- Example: SortJoy's top 7 queries by brand cart adds were all branded. The first non-branded query with meaningful traction was "felt storage bins with lids" at just 20 carts over 11 months.
- Step: 3a (Tagging), Final Output

**22. Keepa signals table can be empty for newer ASINs**
- For newer ASINs that Keepa hasn't fully processed, the listing quality assessment needs to rely entirely on raw product data and web research.
- Example: SortJoy B0DGQTYJG6 had zero signals rows, zero rating history rows, and only 1 sales rank data point.
- Step: 2e (Listing Quality)

**23. Account-wide buy box crisis should trigger a dedicated diagnostic section**
- When 6+ products across a catalog have buy box below 60%, this is an account-level structural problem deserving its own diagnostic section.
- Example: SortJoy had 6 ASINs with critically low buy box, several dropping from 100% to 0-50% within months.
- Step: 1 (ASIN Selection), Final Output

---

## Done

- **#1** Handle missing Keepa data - Added to Product Understanding.md and PDP Audits CLAUDE.md: prompt to ingest if ASIN not found
- **#2** Marketplace filter - Already in Product Understanding.md: query without marketplace filter, pick most relevant
- **#3** Shallow sales rank history - Mitigated by blocker detection time horizon fallback (3-month to annual) in CLAUDE.md
- **#4** Seller Analytics as fallback for Keepa rank - Step 1 already uses Seller Analytics trends
- **#5** Spanish-language queries - Removed: meaningful queries get picked up automatically during tagging
- **#6** Distributor/reseller brand handling - Removed: buy box domain knowledge covers this, edge cases handled separately
- **#7** Correlating SQP impression share with Seller Analytics sessions - Added as optional sub-step in SQP.md Step 3c
- **#10** Q699/Q703 return empty - Addressed via status filter guidance in Ad Analysis.md

### Removed (not needed)

- **#5** Spanish-language queries - Meaningful queries get picked up automatically during tagging
- **#6** Distributor/reseller brand handling - Buy box domain knowledge covers this, edge cases handled separately
- **#11** Multiple PPC management sources flagging - If it's visible in the data, it gets called out naturally
- **#12** Seasonal timing as headline finding - Seasonality detection via SQP is now in domain knowledge, timing follows from that
- **#13** Wholesale buy box vulnerability section - Buy box domain knowledge (child-level, MAP) covers this

---

## From: Dabbldoo Full Audit (2026-04-02)

**28. Zero-ad sellers should get a budget projection in the action plan**
- When the seller has zero ad history, the action plan recommends launching PPC but doesn't project what the expected spend, sales, and ROAS would look like at Week 4 and Week 8. A simple projection table (e.g., "$35/day spend, estimated $X in sales at assumed Y ROAS") would give the closer a concrete number to present on the call.
- Example: Dabbldoo's action plan recommends $35/day Tier 1 spend but doesn't estimate the expected return. The closer needs a number to justify the spend to the brand owner.
- Step: 4 (Ad Analysis), Section 6 (Action Plan)

**29. SQP data sparseness indicator needed for small brands**
- When brand click volumes are too low for statistical significance (under 30 clicks/tier over 3 months), the blocker detection table should explicitly state "data insufficient" rather than "N/A" and explain why. Currently the output does this in prose but a standardized indicator in the table format would be clearer.
- Example: Dabbldoo had 30 brand clicks on Tier 1 and 11 on Tier 2 over 3 months. The blocker table says "Insufficient data" but the format could be more standardized.
- Step: 3d (Blocker Detection)

**30. External traffic spike detection should cross-reference SQP and Seller Analytics systematically**
- When a seller shows a revenue spike that doesn't match SQP search volume patterns, this should be flagged as "externally-driven traffic" with a structured comparison table (month, seller sessions, SQP search volume, delta). Currently this is done in prose.
- Example: Dabbldoo's Nov 2025 spike (10x sessions) vs SQP volume increase (~2x) clearly indicated external traffic, but the comparison was narrative rather than tabular.
- Step: 3b (Market Sizing), Section 3 (Quantitative Understanding)

---

## From: Ghost Hunting Kit Full Audit (2026-04-09)

**31. UK marketplace SQP data gap needs a fallback workflow**
- When SQP data is not available (UK marketplace seller), the audit currently falls back to ad search term data as a proxy for market sizing and blocker detection. This works but is less rigorous than SQP. A standardized "Ad-Derived Market Analysis" sub-workflow should be documented for non-US sellers.
- Example: SpiritShack is a UK seller. SQP returned zero data. Market sizing and ICAP funnel analysis relied entirely on ad search term report keyword groupings, which only cover terms where the brand has impressions (not the full market).
- Step: 3 (SQP Analysis)

**32. 100% auto campaign accounts need a "Manual Campaign Launch Plan" template**
- When a seller has zero manual campaigns, the current workflow identifies the problem but the action plan recommendations are ad-hoc. A standardized template for "first manual campaign structure" (which keywords to extract, initial budget allocation, bid strategy, negative keyword list) would make the action plan more concrete and repeatable.
- Example: Ghost Hunting Kit runs 100% auto campaigns. The action plan recommends creating manual campaigns but the specific structure (how many campaigns, budget per campaign, bid amounts) would benefit from a template.
- Step: 4 (Ad Analysis), Section 6 (Action Plan)

**33. Multiple listings for the same product should trigger a listing consolidation analysis**
- When a seller has 3+ parent ASINs for what appears to be the same product (different keyword-stuffed titles), the audit should quantify the fragmentation impact: total combined sales, review split, session split, and estimate the benefit of consolidation.
- Example: SpiritShack has 5 separate HexCom listings (B0D4FCKX2F, B0D4FFR8SJ, B0D4FDVPWF, B0D4FFDGP7, B09X7CTVJS) generating combined £10,529 in 3-month sales. The main listing has 74% of revenue but reviews and sessions are split across all five.
- Step: 1 (ASIN Selection), 2e (Listing Quality)

---

## From: iSTOCK VR Full Audit (2026-04-10)

**34. Scattered catalog sellers need a catalog coherence assessment**
- When a seller's catalog spans unrelated categories (VR gunstocks + pickleball t-shirts + watering cans + card games), the audit should explicitly flag this as a brand dilution risk and recommend focusing ad spend and listing investment only on the core product line.
- Example: iSTOCK VR has 11 parent ASINs across VR accessories, apparel, garden tools, and tabletop games. The T-Shirts Auto campaign was wasting $10 on a product completely outside the brand's identity.
- Step: 1 (ASIN Selection), Section 6 (Action Plan)

**35. No-review products need a review timeline projection in the action plan**
- When P0 has zero or near-zero reviews after months of sales, the action plan should include a concrete review acquisition timeline: Vine enrollment date, expected first reviews, target review count by Week 4/8, and the CVR lift expected at each milestone.
- Example: iSTOCK VR's SMARTstock had ~240 units sold over 8 months with effectively no reviews. The action plan recommends Vine but doesn't project when reviews will accumulate or what CVR improvement to expect at 10, 20, 50 reviews.
- Step: 2e (Listing Quality), Section 6 (Action Plan)

**36. Buy box crash across multiple products should trigger a pricing history check before asking the seller**
- Related to idea #26 (Keepa price history). When 2+ products have simultaneous buy box crashes (both P0 and P1 dropped to 66% in the same month), this is almost certainly a pricing or account-level issue rather than individual listing problems. The audit should attempt to diagnose the cause before defaulting to a seller question.
- Example: Both P0 and P1 for iSTOCK VR dropped from 100% to 66% buy box in March 2026 simultaneously. This pattern strongly suggests a pricing change or account-level suppression rather than individual competitor entry.
- Step: 1 (ASIN Selection), 2f (Historical Trends)

---

## From: Z Blok Sunscreen Full Audit (2026-04-15)

**39. Customer-facing version of the final audit**
- The final consolidated audit currently reads like an internal closer-prep document. When the closer wants to send it directly to the prospect for review, several sections need to be tuned for the customer audience: Section 2 should trim Product and Customer sub-sections (the customer already knows their own product), the Brand sub-section should be removed entirely (can read as patronising when the customer knows their own brand), and the tone of Insights / Questions should be framed as "here's what we observed" rather than "here's what the closer needs to ask."
- Example: Aryan needed to manually edit the Z Blok v1 audit to strip the Brand section, shrink Product/Customer paragraphs, and trim a handful of low-volume Tier 1/Tier 2 keywords before sending to the Z Blok prospect for final review.
- Idea: add a "customer-facing formatting" mode to the final output. Either a second MD file (e.g., `Seller Central Audit - {Seller} - Customer.md`) or a flag at audit-start that produces the trimmed version in place. Specific rules:
  - Section 2: keep Product and Customer to one-line summaries; omit Brand entirely
  - Tiers: prune queries below a volume threshold (e.g., drop Tier 1/Tier 2 queries under ~1K peak monthly SV unless they are wedge-specific like "reef safe")
  - Keep the Competitive Landscape, Listing Quality, SQP tables, Ad Analysis, Action Plan, and Insights as-is (they are the value)
  - Questions for the Seller can stay — reads as "things we'd love to confirm with you"
- Step: Final Output

---

## From: The Restroom Kit Full Audit (2026-04-13)

**37. Third-party tool detection should include campaign naming pattern recognition**
- When campaign names include tool identifiers like "[AsteroidX]", "Amazify", "Perpetua", etc., the audit should automatically flag the tool and adjust expectations for campaign structure analysis. Currently this is done manually.
- Example: The Restroom Kit's campaigns all used "[AsteroidX]" and "Amazify" prefixes. The AsteroidX automation created the auto-heavy, overstuffed structure that caused the seller to abandon advertising. Recognizing the tool earlier would have framed the entire ad analysis around "automation misconfiguration" from the start.
- Step: 4a (Campaign Structure)

**38. Sellers who abandoned ads need a "What Went Wrong" narrative section**
- When a seller started and stopped advertising within a short window (under 3 months), the audit should explicitly reconstruct the timeline and explain why the experiment failed. This is more compelling than just analyzing the data, because it directly addresses the seller's lived experience and frustration.
- Example: The Restroom Kit ran ads for 69 days (Jan 12 - Mar 21), spent $2,251, saw 2.06 ROAS, and stopped. The "What Went Wrong" narrative (auto-heavy structure, no TOS modifiers, overstuffed campaigns) directly validates the seller's instinct that something was off while showing them that the product CAN respond to properly managed ads.
- Step: 4 (Ad Analysis), Final Output

---

## From: Healthy Living Proteins Full Audit (2026-04-16)

**40. Buy box + PPC sequencing should be a documented pattern**
- When the primary blocker is impression share AND the hero ASIN has a buy box issue (distributor, reseller), the audit needs to explicitly sequence: fix buy box first, THEN launch PPC. Currently this logic is applied through judgment, but it should be a documented decision tree in the workflow: "If impression share is the primary blocker AND buy box < 80% on the hero ASIN, PPC launch must wait for buy box resolution."
- Example: HLP's hero ASIN (B07VMJ4PQS) has 1-3% buy box from a distributor. Launching PPC would waste money because the distributor holds the buy box. The audit correctly sequences buy box fix before PPC, but this pattern should be codified.
- Step: 3d (Blocker Detection), 4f (Solving P0 Blockers via PPC), Section 6 (Action Plan)

**41. Zero-ad sellers with zero branded search need a "brand equity quantification" section**
- When a seller has no ads AND no branded search volume, the audit should attempt to quantify how much of their current revenue is from brand equity vs organic ranking. For HLP, the fact that customers navigate past a distributor's buy box to buy from HLP ($640/month at 1-3% buy box) is direct evidence of brand loyalty. This signal should be systematically surfaced as a "brand equity indicator" with an estimated dollar value.
- Example: HLP generates $640/month on B07VMJ4PQS despite 1-3% buy box, meaning customers are choosing to buy from HLP even when a cheaper option is in the buy box. This is quantifiable brand loyalty that should be positioned as a selling point.
- Step: 1 (ASIN Selection), Final Output

**42. Seller Analytics ad data coverage should trigger a workflow branch earlier**
- When ads_day_count < 30 (not just < 70), the workflow should immediately flag "zero-ad seller" and skip Steps 4a-4d entirely rather than attempting them. Currently the workflow reaches Step 4 and discovers there's nothing to analyze. A pre-check in Step 0 would save time.
- Example: HLP had 9 days of ad data with zero meaningful activity. Steps 4a-4d were all "not applicable."
- Step: 0 (Data Readiness), 4 (Ad Analysis)

---

## From: OneRADON Full Audit (2026-04-16)

**43. Extreme impression share deficit needs a spending projection in the action plan**
- When impression share is below 0.1% on Tier 1, the gap between current state and even 1% share is so large that the action plan should include a concrete spend projection: "To reach X% impression share on Tier 1, expect $Y/day in spend at current CPC." Without this, the closer doesn't know how to frame the investment required for the prospect.
- Example: OneRADON has 0.014% impression share on a $1.16M/month market. The action plan recommends PPC scaling but doesn't estimate what daily budget is needed to meaningfully move impression share from 0.01% to even 1%.
- Step: 3d (Blocker Detection), Section 6 (Action Plan)

**44. Products with very low review counts need a "review accumulation rate" analysis**
- When P0 has under 100 reviews after 2+ years on the market, the audit should calculate the review rate (reviews per unit sold) and project when the product will reach competitive review counts. This helps the closer frame whether the rating gap is solvable in a reasonable timeframe.
- Example: OneRADON's Luft has 58 reviews after ~2.5 years on market. At ~30 units/month and a typical 1-2% review rate, it would take 12-18 months to reach 100 reviews. Competing products have thousands. The closer needs to manage expectations about how quickly this headwind can be addressed.
- Step: 2e (Listing Quality), Section 6 (Action Plan)

---

## From: SnoreStop USA Full Audit (2026-04-21)

**45. Multi-product-line brands in SQP need an explicit query-relevance filter before tier tagging**
- When a brand on SQP sells both pet-line and human-line products (or any two unrelated product families) but the seller on Amazon only represents one family, the raw query universe is dominated by queries that cannot convert on the audited ASIN. The workflow should include an explicit "query relevance filter" step before tier tagging: isolate the subset of brand queries that the audited product can actually convert on, and exclude the rest up front.
- Example: "Snore Stop" on SQP covers both human and pet products. Human-intent queries like `snore stopper` (40k/mo) and `anti snore` (13k/mo) dominate the raw brand query set, but SnoreStop USA only sells pet products. Without an explicit exclusion step, the tagging can accidentally include human queries, which then distort market sizing and blocker detection.
- Step: 3a (Tagging)

**46. "Maxed Out Potential" pattern needs a tailored action plan template**
- The standard action plan assumes a blocker exists (impression share / CTR / CVR) and the PPC lever solves it. When the analysis reveals "Maxed Out Potential" (impression share already near cap, funnel above industry at every stage), the existing template doesn't fit. The workflow should have a dedicated "Maxed Out" action plan template that reframes Weeks 1-4 as PPC housekeeping / internal efficiency (placement shifts, harvest-and-scale, negatives) and Weeks 4-8 as listing improvements plus category-expansion discussion, without implying PPC will unlock new growth.
- Example: SnoreStop USA's P0 (Chewable Tablets) is at 14.5% impression share of a ~17% cap with 3x industry CTR and above-industry CVR. There is no traditional blocker. The final action plan had to be rewritten to reflect "PPC housekeeping, not scaling" and "listing lever + category growth as the real unlocks."
- Step: Section 6 (Action Plan), CLAUDE.md Domain Knowledge

**47. Dormant/duplicate ASIN detection should be a standard Step 1 check**
- When the catalog includes parent ASINs with near-zero lifetime sessions and zero sales (indicating abandoned or duplicate listings), Step 1 should surface these explicitly with a "consolidation recommendation" rather than leaving them as context. A standard check: any parent ASIN with <10 lifetime sessions and $0 sales should be flagged and a brief consolidation suggestion added to the insights bucket.
- Example: SnoreStop USA has 6 parent ASINs, but 2 (B0D4JK6VMW and B0D4JKP7SH) are duplicates with essentially zero traffic. Currently this was caught in the priority table footnote but could be a first-class observation.
- Step: 1 (ASIN Selection)

---

## From: Beauticone Trends Full Audit (2026-04-21)

**48. Data availability can change mid-audit and should trigger a data re-check**
- When data uploads happen during an audit (e.g., ad data becomes available after Step 1 flagged it as missing), the workflow needs a cheap "data coverage re-check" before starting Step 4 so the ad window can be used fully. Currently ads_day_count is only checked in Step 0, so a mid-audit upload requires the auditor to notice and re-query manually. A simple 5-second data coverage ping at the start of Step 4 would make this automatic.
- Example: Beauticone Trends had 0 ad days at audit start. The seller uploaded ad data during Step 3 (SQP). Step 4 had to be rewritten from "no ad data" to a full 89-day ad analysis. The shift was caught because the user messaged the upload, not because the workflow detected it.
- Step: 0 (Data Readiness), 4 (Ad Analysis)

**49. "Hero product missing its SK Tier 1 exact campaign" should be a named structural check**
- When a multi-product account has dedicated SK (Sponsored Products Keyword) exact campaigns for some products but not for the hero (P0), this is one of the single highest-impact structural issues. It often explains a large chunk of P0 impression-share deficit. The workflow should codify it: for each product in the P0 campaign map (Step 4e), check whether an SK-style keyword-exact campaign exists on Tier 1 queries. If one is missing on P0 while it exists on P1/P2, surface this as a dedicated finding with a template-copy recommendation.
- Example: Beauticone's P2 (Pumice Stone) had a dedicated "SK | pumice stone for feet | Exact" campaign spending $1,544 over 90 days, which drove 326 orders. The P0 (Straight Razors) had no equivalent SK Tier 1 campaign, and this was the single biggest ad finding. The audit caught it through careful campaign inspection, but it should be a named check.
- Step: 4e (Product-to-Campaign Mapping), 4f (Solving P0 Blockers via PPC)

**50. Seasonality hypothesis from Step 1 needs a structured confirmation test in Step 3**
- When Step 1 flags a revenue trajectory that "could be seasonal" (e.g., Oct-Nov peak, Feb-Mar trough), Step 3 should run a structured two-way test: (a) does SQP market purchases show the same Oct-Nov peak / Feb-Mar trough pattern? (b) is the brand's share of market purchases stable across those months? If the market moves with the brand, it is seasonality. If the market is flat/growing while the brand declines, it is a brand-specific visibility issue. Currently this reasoning happens through judgment in prose; it should be a standard table output: "Brand revenue trend vs market purchases trend."
- Example: Beauticone's Step 1 flagged the Oct-Nov peak followed by Feb-Mar decline as possibly seasonal (grooming gift timing). Step 3 revealed Tier 1 market purchases actually GREW from Apr to Mar (10.7K → 14.2K/mo), while Beauticone's share fell from 6% to 2%. Market was flat-to-growing; the brand collapsed. This flipped the entire audit narrative from "seasonal decline, push for Father's Day" to "visibility collapse, fix impression share now."
- Step: 3b (Market Sizing), 3c (Market Share and Potential)

---

## From: Scary Peeper Full Audit (2026-04-21)

**51. Dual-product-line accounts need a "two businesses" framing in Step 1**
- When an account's current revenue is dominated by one product line but the brand identity is a different product line (e.g., a Halloween-brand seller currently deriving most of Q1 revenue from Harry's-compatible razor blade refills), the standard priority table buries the story. The workflow should recognize this pattern and produce a two-section Section 1: "Line A" (brand-identity products) and "Line B" (off-brand / diversification products). P0 is selected from Line A by default, but Line B is surfaced explicitly with its own spend/ROAS block so the sales conversation can address both.
- Example: Scary Peeper Inc. sells Halloween window-peeper props (the brand) but has also launched 4 Harry's-compatible razor blade ASINs that dominated Q1 ad spend at 8.93 ROAS. Without the two-line framing, the razor blade business gets either ignored or wrongly selected as P0.
- Step: 1 (ASIN Selection)

**52. Brand registry mismatch across SKUs should be a standard Step 2 check**
- When building Product Understanding on P0, query the `brand` field in Keepa for ALL sibling SKUs in the catalog and flag any inconsistency. A signature brand product sitting under a different brand name (sometimes legacy distributor, sometimes uncorrected) is common enough and high-impact enough (blocks Brand Store routing, fragments analytics, leaks branded impressions) that it warrants a standard pre-flight query rather than being caught through judgment.
- Example: Scary Peeper's P0 (B00F4HRW50) is registered as "Forum Novelties" while every other Scary Peeper SKU is correctly registered as "Scary Peeper Fright At First Sight." This was the single biggest zero-cost fix in the audit and would have been missed if only P0 was queried.
- Step: 2a (Product & Customer) - extend the query to all sibling SKUs

**53. Suppressed listings with massive session volume deserve their own finding block**
- When a child ASIN in the catalog has >10,000 sessions in 90 days with 0% buy box and near-zero sales, this is a high-impact finding independent of the normal priority table logic. The audit should surface it with its own mini Problem-Solution-Impact block in Section 1: what the listing is, why it has traffic, why it's not converting, and whether it's recoverable or needs removal.
- Example: Scary Peeper's B0FDQXP44B (Kidde smoke detector adapter) had 47,855 sessions in Q1 2026 with 0% buy box and 0 sales. This is a completely stranded listing on a high-traffic page. Currently flagged as a seller question, but it probably deserves a dedicated first-class finding.
- Step: 1 (ASIN Selection)

**54. Seasonal product ad-data gap needs a systematic flag**
- When the seller's business is seasonal (e.g., Halloween-driven) and the ad data window is shorter than the seasonal cycle (e.g., 90-day ad data but Halloween is annual), the audit cannot see the actual peak-season ad behavior. This should be explicitly flagged in the Ad Analysis section header (not as a mid-section caveat) so the reader immediately understands that ad findings reflect off-season/transition behavior only. Action plan recommendations around ad scale should explicitly depend on confirming peak-season ad history with the seller.
- Example: Scary Peeper's ad data covers Jan 22 - Apr 20 2026. Halloween 2025 activity is invisible. The audit had to flag this as a seller question ("did you run ads in Sep-Oct 2025?") to calibrate how aggressive the 2026 ramp should be.
- Step: 4 (Ad Analysis header), Section 6 (Action Plan)

---

## From: Creative Gifts International Full Audit (2026-04-27)

**55. Massive-catalog sellers (200+ parents) need a two-pass priority pull**
- When `parent_count` exceeds ~100 in `list_sellers`, the standard `get_pivot_table(aggregation_level=parent)` returns 30k+ tokens and forces file-based reading. The workflow should codify a two-pass approach: first run `get_cumulative_metrics(aggregation_level=parent)` with a minimal metric set (just total_sales, units, ad_spend) to rank, then run the full-metric pivot only on the top ~15-20 parents by sales. This would have saved a context-bursting 100kb file read on Creative Gifts International (302 parents).
- Example: Creative Gifts International has 302 parents / 328 ASINs. The full-catalog pivot returned 101k characters and required jq-based filtering. Pre-ranking would have made this a clean ~5k-token query.
- Step: 1 (ASIN Selection)

**56. Variant-level CVR concentration check as a standard Step 2/4 step**
- When P0 has multiple child variants (e.g., colors, sizes), run a standard "variant concentration" check: pull child-level CVR and order count for the most recent month, calculate what share each variant holds of parent sales and parent sessions, and flag when one variant disproportionately drives sales (>40% of parent sales from <20% of parent sessions). This frequently reveals that ad budget is spread across variants while only one converts. Currently this insight is found through judgment when the parent-level numbers look surprising.
- Example: Creative Gifts P0 (Dog Balloon Animal Piggy Bank) had Gold converting at 34.83% on 89 sessions (58% of parent sales on 12% of parent sessions) while 6 other colors averaged ~3% CVR. Gold also got the smallest share of ad budget. Concentrating ad spend on Gold was the single biggest CVR-side win.
- Step: 2e (Listing Quality), 4f (Solving P0 Blockers via PPC)

**57. Listing-category mismatch as a documented listing lever**
- When the leading competitor for P0 is in a different Amazon category (e.g., Home & Kitchen) and P0 is in a more "kid-oriented" or otherwise narrower category (e.g., Toys & Games), the category placement itself is a listing lever, not just an SEO tweak. The workflow should treat category change as a first-class option in Step 2e Opportunities and in the Action Plan, especially when SQP data shows the brand has impressions but below-industry CTR on decor / adult-buyer queries.
- Example: Creative Gifts P0 is in Toys & Games > Money Banks. The category leader (Made By Humans) is in Home & Kitchen. Tier 3 (balloon dog decor) brand impressions are present but CTR is 3.5x below industry, the decor buyer doesn't recognize the listing. Category change to Home & Kitchen would unlock this audience.
- Step: 2e (Listing Quality), CLAUDE.md Domain Knowledge (Listing levers list)

**58. Pre-publish em-dash check**
- The CLAUDE.md instruction "Never use long dashes (em dashes) anywhere in the output" can be missed during long, multi-step audit writing. Em dashes often slip in when listing rationale ("**P0, Description**" form). A pre-publish check that runs `grep "—"` on every audit file before Notion upload would catch this systematically.
- Example: All five Creative Gifts International audit files contained em dashes that had to be cleaned with a perl script before Notion publish. The cleanup also produced minor artifacts (" ,**" patterns) that needed a second pass.
- Step: Final Output, Publishing to Notion

---

## From: Bi-Crackie Full Audit (2026-04-28)

**59. Single-product catalog framing should be standardized in Step 1**
- When a brand has only 1 parent ASIN and a small handful of color/size SKU variants of the same product, the standard "P0/P1/P2/P3" priority framework feels artificial. The four "priorities" are really just SKU variations of the same product. The workflow should detect this case (parent_count=1 OR >80% of revenue concentrated in one parent) and reframe Section 1 explicitly: "single-product brand" header, priority table at variant level, and a clear note that subsequent steps will analyze the parent listing as one product. This avoids the awkward "P0 vs P1" deliberation when both are the same tool in different colors.
- Example: Bi-Crackie has 1 parent (B0D86S4HNF) with 5 SKU variants of the same BICRACKIE Stand-Up Crack Weeding Tool. The audit had to manually explain that the priorities are at variant level and that Step 2 onward focuses on the parent listing.
- Step: 1 (ASIN Selection), CLAUDE.md Domain Knowledge

**60. Listing signals empty rows should not silently skip the analysis**
- When `new_asin_signals` returns 0 rows for the P0 ASIN (signals not yet computed), the audit currently falls back to assessing the listing from raw fields (title, bullets, A+, video, image JSON). This works but the fallback should be made explicit in the workflow with a documented "raw assessment checklist" so the auditor doesn't miss anything the signals would have surfaced (title length, bullet length distribution, A+ word count, image count, etc.). Without this, the auditor might compute one signal manually and forget another.
- Example: Bi-Crackie's P0 (B0C9KWVCTY) had zero rows in new_asin_signals. The audit assessed bullets, A+, video, and main image from raw data, but only manually inferred title length and never checked exact image count beyond the obvious "main: null".
- Step: 2e (Listing Quality)

---

## From: FMLaGame Full Audit (2026-04-28)

**61. Break-even ROAS should be calculated upfront and surfaced everywhere it matters**
- When the seller intake notes include COGS and retail price (profit-first sellers especially), break-even ROAS should be calculated in a Step 0 "Unit Economics" sub-step and used as the threshold for the rest of the audit, not just in Step 4. Currently the 1.5x ROAS threshold from CLAUDE.md is a generic placeholder; with COGS data, the actual break-even number (often 2-2.5x) is a much sharper diagnostic. Every "unprofitable campaign" call in Step 4 should reference the break-even number, and the Action Plan should frame ad scale-down decisions against the same number.
- Example: FMLaGame had COGS $4-5 and retail $19.95. Break-even ROAS computed to 2.23. The account ROAS was 0.66, meaning every active campaign was destroying margin (vs the 1.5x default which would have flagged just two campaigns). The audit was strengthened by anchoring every PPC recommendation against the 2.23 number.
- Step: 0 (Data Readiness) - new sub-step, Section 5 (Ad Analysis), Section 6 (Action Plan)

**62. Sponsored Display constraint should propagate into the action plan template**
- When the seller rules out Sponsored Display (intake notes), several CLAUDE.md domain-knowledge recommendations (defensive SD, retargeting for cart-to-purchase rate) become blocked. Currently the audit handles this in prose. The workflow should have an explicit "Constraint propagation" check that reviews each PPC recommendation against the seller's stated constraints before publishing the action plan, and adds a header note in Section 5 listing what's been removed.
- Example: FMLaGame's seller said "SD not allowed". Step 4's domain knowledge would normally recommend defensive SD on own listing (the textbook CVR fix). The audit had to manually note this exclusion and lean harder on listing-side fixes.
- Step: 0 (Data Readiness), Section 5 (Ad Analysis header)

**63. TikTok-driven brand archetype needs its own playbook chapter**
- When a brand's launch was driven by a single viral moment (TikTok creator, Instagram Reel) and revenue has decayed since without replacement, the action plan should treat off-Amazon demand generation as a first-class lever, not a footnote. Currently CLAUDE.md domain knowledge doesn't cover this archetype explicitly. The pattern: Dec viral peak, sustained decline through year, smaller Q4 echo, slow drift down. The audit needs to recognize this archetype and (a) ask for the original viral trigger, (b) frame Brand Store as essential infrastructure for capturing future TikTok traffic, (c) include a "rebuild off-Amazon motion" recommendation alongside the on-Amazon fixes.
- Example: FMLaGame had a $6,587 Dec 2024 viral month (no ads), declined to $2,890 Dec 2025 (-56% YoY despite holiday tailwind), now collapsing to $300-500/mo with paid ads losing money. The Dec 2024 trigger is unknown. The brand has invested in 6 listing videos (TikTok-style content), so the muscle exists but the off-Amazon motion has stalled. The action plan added "rebuild TikTok creator pipeline" alongside listing/PPC fixes.
- Step: CLAUDE.md Domain Knowledge (new chapter), Section 6 (Action Plan)

**64. Q4-seasonal product action plan should anchor on the seasonal peak, not 8 weeks from now**
- When SQP confirms strong seasonality (4x+ peak vs trough on Tier 1), the standard 8-week action plan can feel disconnected from when the work actually matters. The workflow should compute the months-to-next-peak from the audit date and reframe the timeline accordingly: "Weeks 1-2 (now)", "Weeks 3-8 (off-season foundation)", "Months 3-6 (steady-state iteration)", "Months 6-7 (peak ramp)". This makes the action plan honest about where the value is realized.
- Example: FMLaGame's audit was in late April 2026. Q4 2026 peak is 6-7 months away. The standard 8-week plan ended in late June with no clear bridge to Q4. Restructuring to a peak-anchored timeline would have made the off-season "fix and test" framing more explicit and the Q4 ramp a planned phase rather than an afterthought.
- Step: Section 6 (Action Plan)

**65. Single-ASIN accounts should auto-skip Step 1 ASIN selection logic**
- Related to idea #59 (single-product catalog framing). When `parent_count = 1` AND `child_count = 1`, Step 1's "select P0, P1, P2, P3" logic is entirely vestigial. The workflow should detect this and produce a minimal Section 1 (one row, "P0 by default") immediately, skipping the trend-direction-vs-other-products logic that doesn't apply. Saves time and avoids the awkward "no P1, P2, P3" caveat.
- Example: FMLaGame has 1 parent / 1 child. The Step 1 output had to manually note "P0 is automatic" and "no P1/P2/P3" rather than the workflow handling this case natively.
- Step: 1 (ASIN Selection)

**66. Third-party agency naming conventions in campaigns should be auto-flagged with provenance attribution**
- Extending ideas #19 (Perpetua), #37 (AsteroidX/Amazify): when campaign naming patterns reveal multiple agencies in the same account (e.g., Sophie Society set up the manual campaigns, Sellozo runs the auto), the audit should list each provenance and split findings by responsibility: "These campaigns were configured by Agency A; these by Agency B; these patterns indicate handoff issues." This helps the closer frame the conversation with the prospect ("Sophie Society's manuals are still running on the modifiers they set when they disengaged - those need updating now").
- Example: FMLaGame's manual campaigns are named "SO | FML | B0CTXKBB6X | SPM | ..." (Sophie Society convention) while the auto is "FML Auto - Sellozo". The TOS 60% / PP 80% modifiers were set by SS. The audit identified this and connected it to the placement bias finding, but recognizing the multi-agency handoff pattern as a named structural issue would make this faster.
- Step: 4a (Campaign Structure)

---

## From: Insaltd Full Audit (2026-04-30)

**67. Notion MCP unavailability needs a graceful fallback path**
- The publishing-to-Notion step assumes the Notion MCP is available, but it can disconnect mid-audit (happened during this run). When Notion tools are unavailable, the workflow should detect this at the start of the publish step and either save the audit as a single combined file ready for manual paste, or queue the publish for retry. Currently the audit completes locally but the closer has to remember to publish manually later.
- Example: Insaltd audit completed end-to-end locally but the Notion MCP disconnected before the publish step. All 5 files exist in `All audits/Insaltd/` but never made it to Notion in the same session.
- Step: Publishing to Notion

**68. Relisted brand SQP contamination needs an explicit reconciliation**
- When a seller has relisted under a new parent ASIN (Step 1 reveals a dead old listing + a healthy new listing for the same product), the brand-level SQP data combines impressions from BOTH the dead and live listings. For relisted brands, share metrics for the months before the relist reflect the OLD listing's performance, not the new one's. Step 3 should explicitly call out the relist boundary and either limit the SQP window to post-relist months or annotate the share data so the reader knows which listing is producing which signal.
- Example: Insaltd's brand-level SQP impressions for Q4 2025 came from the dying B0CBCJQRM1, while Q1-Q2 2026 impressions are increasingly from B0GC18NZC4. Without flagging this, the reader can't tell whether a tiny share-of-voice improvement reflects the new listing scaling or just the old one bleeding out.
- Step: 3a (Tagging), 3c (Market Share and Potential)

**69. Rating slide on a fast-growing listing is a named risk pattern**
- When a listing's organic traffic ramps quickly (e.g., 50x sessions growth in a quarter) AND the rating declines in the same window, this is a "new-cohort dilution" pattern: newer reviewers (lower-intent, broader audience) are leaving lower ratings than the early-adopter cohort. This pattern is high-risk because PPC scaling on a falling rating amplifies the dilution. The workflow should codify a standard check: pull rating history covering the same window as the session-growth window from Step 1; if rating direction is flat or down while sessions are up, surface this as a dedicated "Rating dilution risk" finding in Section 3 with a sequencing implication ("address before scaling Tier 2 PPC").
- Example: Insaltd's P0 hit a rating peak of 4.4 on Apr 10 and slid to 3.7 by Apr 23 while sessions were still growing. Without explicitly naming the pattern, this is easy to miss as just a recent-history rating dip.
- Step: 2f (Historical Trends), Section 3 (Quantitative Understanding)

**70. Customer-uploaded video positioning language as a PPC creative anchor**
- Keepa stores customer-uploaded videos with creator type tags (Main / Influencer / Customer / Seller). When a customer-uploaded video title contains positioning language that aligns with the brand's intended wedge (e.g., "frugal alternative to LMNT"), this is gold: the customer themselves has articulated the positioning we want to use in PPC creative. The workflow should treat this as a first-class artifact: scan customer-creator videos in Step 2 and surface positioning-relevant titles directly in the Section 5 ad creative recommendations, with attribution.
- Example: Insaltd's older parent (B0C9R1BDDV) carries a customer-uploaded video titled "Good frugal alternative to LMNT". This single video title validates the entire conquest-on-LMNT thesis and should anchor the creative for the Conquest SP and SD campaigns.
- Step: 2a (Product & Customer), Section 5 (Ad Analysis - Creative)

---

## Watch List (Monitor, Don't Act Yet)

Things that have happened once or are potential concerns. If they recur, investigate and promote to a proper V2 idea with a solution.

**1. Context window filling up mid-audit**
- Happened once. The audit consumed enough tokens that context compression kicked in or the session hit limits before completing.
- Potential mitigations if this becomes recurring: break the audit into separate sessions per step, use subagents more aggressively to offload data processing, reduce token usage by being more selective with data pulls (e.g., fewer columns, smaller result sets).
- Occurrences: 1

---

## MINT Tools audit (2026-04-30) - new ideas

**Multi-generation product handling in Step 1/2**
- MINT has both B07RM2VQ77 (original curling iron, 2019) and B0GGJ7P2VJ (REVAMP 2026) - same product family, different parent ASINs, $20 price gap, partially overlapping ads. The current workflow treats each parent as a separate product but the strategic question (phase out vs. run both) requires looking at them together. Consider adding a "product family" detection step that flags multi-parent overlaps.
- Step: 1 (ASIN Selection) and 2 (Product Understanding)

**Direct buy-box diagnosis from price history (codify)**
- Used Keepa price history + offer history to confirm MAP-suppression diagnosis on MINT's curling iron (price went from $79.97 promo to $109.97 over 10 weeks; buy box dropped Aug 2025 and held at 75% for 8 months; zero 3P offers means no competition explanation). This pattern is now well-defined enough to codify as a sub-step in Step 1: "If buy box <90% on a private-label brand, pull price history + offer count and look for the trigger event." Idea #26 already touches this; this audit gives the working template.
- Step: 1 (ASIN Selection), buy box diagnosis sub-step

**Notion publishing fragility**
- Notion MCP disconnected mid-audit. The CLAUDE.md publishing step couldn't run. Currently no fallback - the audit instructions assume Notion MCP works. Two options: (a) detect disconnection and skip with a flagged TODO, (b) add a manual publishing checklist as a fallback.
- Step: Final publishing step

**Placement findings deserve their own subsection in the action plan**
- The biggest single ad lever in this audit was placement reallocation (~$48K/year from shifting Top of Search vs Product Pages bid modifiers). Current workflow tucks this into "CTR Blocker" but it's often the highest-impact PPC finding regardless of which blocker is primary. Consider promoting placement to a top-line account-level account-level step (4d.5 or similar) so it doesn't get lost when CTR isn't the primary blocker.
- Step: 4 (Ad Analysis, account-level)

---

## From: Blue Sky Studios Full Audit (2026-04-30)

**71. Multi-IP licensee-aggregator pattern needs its own playbook chapter**
- Blue Sky Studios is a license-aggregator brand: 113 parents, mostly single-product formats with multi-IP variant children (e.g., one Desk Mat parent with 10 children that are Harry Potter, Spongebob, Sanrio, Wednesday, TMNT etc.). The customer is buying the IP, not the brand. Several workflow assumptions break: branded-keyword strategy is mostly meaningless (no one searches "Blue Sky Studios"), the Step 2 "Brand" sub-section reads thin, and the catalog overlap check in Step 3 must consider all IP-aligned siblings as ranking together. Codify this as a brand archetype with its own guidance: skip branded defense recommendation, run the SQP overlap check on IP not on parent ASIN format, and surface the "one product format, many IPs" template as a pattern.
- Example: Blue Sky Studios. Catalog overlap on "harry potter gifts" was 5+ products from the catalog. Branded queries on "Blue Sky Studios" had near-zero meaningful volume. The brand vibe is the IPs, not the seller.
- Step: 2b (Brand Understanding), 3a (Tagging) catalog overlap, CLAUDE.md Domain Knowledge (new chapter on licensee/aggregator brands)

**72. Auto vs Manual query (Q703) appears to undercount when split rows are present**
- Q703 returned a single "Manual targeting" row even though Q726 (ASIN level) clearly showed Auto campaigns existed (just with very small spend, ~£70 total). The query may be filtering out Auto when its volume is below a threshold, which is misleading. The workflow should either: (a) cross-check Auto presence via Q699/Q726 campaign names ("Auto" pattern match) before concluding "no auto", or (b) document that Q703 has this limitation and to verify with a secondary source.
- Example: Blue Sky Studios. Q703 showed only Manual; Q726 revealed multiple Auto campaigns at low budgets. Without the cross-check, the audit could have falsely claimed "zero Auto exists" when the actual finding is "Auto exists but is starved."
- Step: 4b (Auto vs Manual Split)

**73. Pre-ad organic-only Q4 hits need a "what did organic do alone" section**
- Blue Sky Studios' P0 hit £35.9K in December 2025 and £17.8K in November 2025 with zero ads, then ads started in January 2026. This is a really powerful sales-conversation framing ("here's what your product did with no ads, imagine with ads") but the standard audit template doesn't have a dedicated place to hammer this home. Consider promoting "Organic-only Q4 baseline" to a first-class header in Section 3 when the data shows it (revenue concentration in Q4 with zero ad spend during peak).
- Example: Blue Sky Studios P0 quad wand pen. The £53.7K organic-only Q4 is the single most compelling number in the entire audit. Currently it's discussed inline in Section 3 but could be its own called-out box.
- Step: Section 3 (Quantitative Understanding), Final Output formatting

**74. Sub-£20 average price products with seasonal Q4 demand should trigger a "Q4 readiness" checklist in Action Plan**
- Q4 gift-driven products at sub-£20 prices share a recurring pattern: huge volume swing, inventory and licensing capacity become the binding constraint, and PPC scaling has to be timed with stock arrival. The audit currently catches this in Section 6 prose but a templated "Q4 Readiness Checklist" (inventory plan, licensing capacity, branded defense launch timing, ad budget ramp schedule) would make this systematic.
- Example: Blue Sky Studios P0 (£13.92 wand pen). The action plan called out Q4 inventory and licensing as a question but didn't structure it as a checklist with concrete dates working backward from November.
- Step: Section 6 (Action Plan)

**75. UK-marketplace category IDs lack a translation table**
- For UK sellers, Keepa returns numeric category IDs (e.g., 192413031 = Stationery & Office Supplies, 49980677031 = Ballpoint Pens) but there's no in-database name lookup. The auditor has to infer category names from rank context or search Amazon UK directly. A small `category_lookup` table or an inline mapping for common UK categories would speed Step 2f sales rank analysis.
- Example: Blue Sky Studios. Sales rank in cat 5246803031 was top 10 in Q4, top 30-60 currently, but the auditor had to guess the subcategory name (Pens & Refills) from context rather than read it from the data.
- Step: 2f (Historical Trends)

---

## From: GoSun Full Audit (2026-05-04)

**76. Datadive niche export as a documented SQP fallback**
- When SQP is unavailable, a Datadive niche keyword export is a viable substitute that gives search volume per keyword, relevance %, and per-ASIN organic ranking position across the niche. The workflow should formalize this: document the columns Datadive provides, the analysis path (tier the keywords by SV, build a catalog visibility map by counting top-3/top-5/top-10 placements per ASIN, infer blockers by combining Datadive ranking with seller-analytics CVR), and the limitations (no true purchase volume, no brand-level CTR/CVR, can't compute share of voice the same way SQP can).
- Example: GoSun. No SQP available, Datadive 47-keyword niche export provided complete substitute. The catalog visibility map (P2 GoSun Go appears in 22/25 keywords with 13 top-5 placements) was the single biggest insight in the audit and would have been hard to replicate via search-term harvesting alone.
- Step: 3 (SQP Analysis), CLAUDE.md (new fallback workflow)

**77. Traffic-vs-CVR mismatch should be a named Step 1 finding**
- When an ASIN has dramatically more sessions than its sales suggest (e.g., 30K sessions/quarter at 0.18% CVR vs catalog avg 1-2%), this is the highest-leverage finding in the entire audit. The workflow currently catches it in prose. Codify it: in Step 1, after the priority table, run a "traffic-CVR mismatch check" - if any ASIN's sessions/sales ratio is more than 5x the catalog median, surface as a dedicated headline insight with the unlock math ("at category-baseline CVR, this ASIN does $X instead of $Y").
- Example: GoSun. P2 (GoSun Go) had 29,771 sessions over 3 months at 0.18% CVR, while the catalog average was 1-2%. Moving CVR to 2% would 11x sales on that ASIN at zero traffic cost. This was the single biggest insight and drove the entire audit thesis.
- Step: 1 (ASIN Selection)

**78. Spanish (or other-language) opportunity surfacing as standard in Datadive/SQP analysis**
- When the keyword export contains non-English keywords with meaningful aggregate SV (e.g., 15%+ of niche demand in Spanish), this is consistently underserved by competitors. The workflow should systematically isolate non-English keywords, sum their SV, check competitor presence on them, and surface as a "blue-ocean opportunity" finding with concrete recommendation (Spanish backend keywords + Sponsored Products campaign). Currently caught through judgment.
- Example: GoSun. 19 Spanish keywords totaling 4,750 SV/mo (15% of niche). No competitor specifically targeting Spanish. GoSun ranked #7-#12 organically with no localization effort. A clean ~$300-$500/mo PPC campaign could claim this segment.
- Step: 3 (SQP Analysis / Datadive)

**79. Duplicate listing detection by exact-title match in Step 1**
- When two parent ASINs in the catalog share the exact same listing title, this almost always means a duplicate or accidentally-relisted SKU. The workflow should run a title-similarity check (exact match or 90%+ token overlap) across all parents in Step 1 and surface duplicates explicitly with consolidation guidance. Currently this was caught manually because both showed up in the priority table top 10.
- Example: GoSun. B0CSWVM2W3 and B0DNRBHHF3 both have title "GOSUN Portable Solar Oven Kit for 1-2 Meals | Effortless Outdoor Cooking with Solar Oven Kit | Vacuum Insulated Oven | Cook meals in 20 min, Great For Camping, Travel, Beach etc". P1 converts at 3.86%, the duplicate at ~2%. Consolidating would compound rank, reviews, and ad efficiency.
- Step: 1 (ASIN Selection)

**80. Catalog-coverage mismatch between Datadive niche and seller catalog**
- When the Datadive niche export covers some but not all of the seller's relevant ASINs, this is itself a finding: the missing ASINs may have low search visibility (deserving listing/SEO work) or be in a different niche entirely. The workflow should explicitly cross-reference: list which seller ASINs are in the niche header, which are not, and explain the gap. This was done implicitly here but worth codifying.
- Example: GoSun has 5 solar-cooker parents. Datadive niche covered 4 of them (B07CJP52D6, B0BRQY4KR4, B00KLKJB72, B0DNRBHHF3, B07WRF6PN4). P1 (B0CSWVM2W3 - the highest-CVR ASIN) was NOT in the niche, despite an identical product to B0DNRBHHF3 which IS in the niche. This is part of the duplicate-listing fragmentation issue.
- Step: 3 (SQP Analysis / Datadive)

---

## From: Terminal Velocity Sport Full Audit (2026-05-12)

**81. Parent-level ad attribution duplication when sibling variant parents share campaigns**
- When a seller has multiple parent ASINs that are variant-design splits of the same product (e.g., Skull / Base / Flame variants of one mount), and one ad campaign covers them all, the parent-level pivot in Seller Analytics shows the same ad spend/sales on each parent. This triple-counts at the parent level and inflates the trailing-3mo ad spend per priority product. Workflow needs to either (a) detect identical-value ad columns across sibling parents and treat parent-level ad data as "approximate" in the priority table, or (b) always fall back to child-level ad attribution for the priority table when sibling parents are detected.
- Example: Terminal Velocity Sport had B0DY5DPK2G, B0DJCM5S7Y, B0DY5J2MRR all showing identical ad spend ($299.55 in April) because they share a campaign. Account-level ad spend is clean ($1,201) but parent-level totals summed to $1,800.
- Step: 1 (ASIN Selection priority table)

**82. Color/variant ad coverage check as a Step 4 standard finding**
- When P0 is a multi-color variant family, the audit should explicitly check what share of the variants are being advertised. Many sellers concentrate ad spend on a single variant out of habit, leaving 3+ variants with zero ad-driven traffic despite shared listing, reviews, and ratings. This is a quick reallocation opportunity that's invisible at the parent level.
- Example: Terminal Velocity Sport's P0 (Motorcycle Cell Phone Mount with Dual USB-C) has 4 color variants. Only Orange (B0CWKTJM9Q) received meaningful ad spend ($603+ across campaigns); Black, Blue, and Yellow each got under $10 in 89 days. The audit caught this in prose but a standardized "variant-level ad coverage" table in Step 4e would surface it as a headline finding.
- Step: 4e (Product-to-Campaign Mapping)

**83. Over-fragmented campaign structure (the inverse of over-stuffed)**
- The current Step 4a Campaign Structure check looks for "too many keywords per campaign" (over-stuffed). The opposite problem - "too many campaigns each starved of budget" (over-fragmented) - has a different signature: many campaigns with $0 or near-zero spend over a multi-month window, paired with proven high-ROAS campaigns getting <$50 of budget. This is common when sellers set up a full Auto/Manual/Match-Type campaign suite per product without active budget management. Detection rule: if more than 50% of active campaigns have <$25 spend over 89 days, flag as over-fragmented and shift the finding to "campaigns are too granular, budget needs consolidating into the proven winners".
- Example: Terminal Velocity Sport has 37 active campaigns. Only 10 spent >$25 over 89 days. The high-ROAS P0 Phrase campaign got $28 of spend while loss-making P0 Broad got $501.
- Step: 4a (Campaign Structure)

**84. YoY revenue + ad-spend cross-check as a headline diagnostic**
- When a seller is running ads but YoY revenue is flat or declining (especially with sessions UP YoY but units flat), this is strong evidence of ad cannibalization (broad-match spending on queries the brand was winning organically). The current workflow catches this in prose. Codify it: a standardized "YoY diagnostic" in Step 1 that compares YoY revenue, YoY sessions, and YoY units. If sessions are up and units are flat or down while ads are running, flag as "likely ad cannibalization, investigate in Step 4".
- Example: Terminal Velocity Sport's Apr 2026 was -15% revenue YoY (1,323 vs 1,538) despite ads turning on. Sessions were UP YoY (1,813 vs 1,559) but units flat (58 vs 63). The ad spend bought traffic at lower intent than the previously-organic traffic it replaced.
- Step: 1 (ASIN Selection), 4 (Ad Analysis)

**85. Sibling-variant parent listings: detection rule beyond exact title match**
- GoSun #79 covers exact-title duplicates. A different but related case: sibling parent listings split by variant *design family* (e.g., Skull, Flame, Base) with overlapping but not identical titles. These also fragment reviews/ranking and inflate parent-level data. Detection rule: parents with shared product category, shared core product type in title, but variant-only differentiation should be flagged for consolidation analysis.
- Example: Terminal Velocity Sport has three parents (B0DJCM5S7Y, B0DY5DPK2G, B0DY5J2MRR) all titled with "Bike Phone Holder/Motorcycle Mount" but split by design theme (Skull / base / Flame). Combined trailing-3mo revenue is $1,524 which would consolidate to a clear #2 product after P0.
- Step: 1 (ASIN Selection)

---

## From: NutriGardens Full Audit (2026-05-14)

**86. Catalog rows with NULL title indicate dead/discontinued products and should be flagged in Step 1**
- When `new_asins.title` is NULL for an ASIN that previously had sales (visible in Seller Analytics history but with $0 in recent windows), this is a stronger signal than "dormant ASIN" - the listing itself is no longer queryable. The workflow should treat NULL title as a "delisted/suppressed" classification distinct from "dormant" (low sales) and surface as its own row in the priority table with a "Was this an intentional discontinuation?" question for the seller.
- Example: NutriGardens has B074JD3QG9 with NULL title in the catalog. Seller Analytics history shows it was generating $1-2K/mo through April 2025, then went to absolute zero (no sessions, no sales, no ads). This is qualitatively different from Berry Boost (which still gets 1-2 sessions/month). Should be flagged as "delisted" not "dormant."
- Step: 1 (ASIN Selection)

**87. Auto/manual inversion paired with placement bias should be presented as one combined finding**
- The auto-vs-manual inversion finding (auto outperforming manual on ROAS) and the placement bias finding (Top of Search outperforming Product Pages) are mechanistically related - auto campaigns dominate Product Pages placement by default (close/loose/substitute/complement targeting), so an auto-heavy account naturally shows high Product Pages exposure. When both findings appear together, the workflow should explicitly connect them in one combined section rather than treating them as separate independent findings. The closer can then frame the unified narrative ("you're not advertising in the right places because your auto campaigns are doing the heavy lifting").
- Example: NutriGardens had auto ROAS 18.51 vs manual 3.86 AND Top of Search ROAS 7.28 vs Product Pages 2.17. Both findings have the same root cause (harvest-and-scale loop broken) but were presented as separate sections.
- Step: 4 (Ad Analysis) - combined account-level structural finding

**88. "RS400-style" branded-ingredient products need a supplier-relationship investigation**
- When P0's product name (e.g., "RS400") appears as a trademark or product line for a different seller / supplier (e.g., Red Spinach Company also selling RS400), this could indicate the audited seller is licensing an ingredient or buying a private-label version. This matters because: (a) margin structure differs from a fully-owned product, (b) supplier relationships can dictate pricing floors and exclusivity, (c) the differentiation story changes (you're selling someone else's IP, not your own formulation). The workflow should standardize a 5-minute web check for trademark / supplier overlap when the product name looks branded.
- Example: NutriGardens RS400 - both NutriGardens and "Red Spinach Company" sell RS400-branded products. RS400 has a registered trademark symbol on the NutriGardens label. Likely indicates a shared ingredient supplier or licensed product line. Flagged as "worth investigating" but didn't get answered in the audit.
- Step: 2c (Competitive Landscape)

---

## From: Prendi Il Caffe Full Audit (2026-05-18)

**89. SQP "brand exists but zero queries" needs a distinct diagnosis from "brand not in SQP"**
- When `list_brands` includes the brand but every `search_queries` call returns 0 rows across all granularities and thresholds (including unfiltered), this is a Brand Registry / Brand Analytics enrollment gap, NOT a missing-data issue that will resolve with a re-ingest. Currently the workflow treats SQP unavailability as one bucket. The fix: in Step 3a Phase 1, check `list_brands` first; if the brand exists but all queries return zero, surface this as a "Brand Registry / Brand Analytics not enabled" finding with a Week 1 action item (have the seller confirm Brand Registry status). This is distinct from "brand not in list_brands" which usually means an ingestion gap on our side.
- Example: Prendi Il Caffe is listed in list_brands but every query returned zero. The audit had to pivot to a fully qualitative SQP analysis. The first Week 1 action item became "confirm Amazon Brand Registry enrollment."
- Step: 3a Phase 1 (Tagging - See where we're selling)

**90. Same-product duplicate-campaign cannibalization needs an explicit count**
- When the same product (e.g., P0) is advertised by multiple campaigns simultaneously (5+), they are competing with each other for the same auction slots, inflating CPCs and fragmenting bid control. This is distinct from "over-stuffed" (too many keywords per campaign) and "over-fragmented" (too many campaigns total). The workflow should run a standard "campaigns per product" check in Step 4e: for each priority ASIN, count how many distinct campaigns advertise it. If any product has 4+ campaigns, surface as a dedicated finding with consolidation recommendation. Currently caught in prose but a standardized count would make this systematic.
- Example: Prendi Il Caffe's P0 (Spinel Ciao Espresso Machine) was advertised by 6 different campaigns (Campaign - 11/13/2025, Ciao 03/2026, Ciao 03/2026 Manual, Ciao M, Espresso machine, Emachine). They were competing with each other for the same impressions. This was the most actionable Section 5 finding but had to be inferred manually from Q726.
- Step: 4e (Product-to-Campaign Mapping), 4a (Campaign Structure)

**91. Reseller / co-branded hardware product detection as a Step 2 sub-check**
- When P0 is the same physical product sold by multiple brands under different labels (e.g., Italian Spinel espresso machines resold by Prendi, Tre Spade, Musetti, Caffe Caroli, Caffelab, all with the same chassis), the competitive differentiation story changes meaningfully. The brand cannot win on hardware specs (everyone has the same hardware) and the moat shifts to bundling, brand story, and consumables flywheel. The workflow should detect this case (when a quick web search shows the same product image/name sold by 3+ other brands) and adjust the Step 2c competitive landscape framing accordingly, plus add a specific note in Section 2 about the "consumables flywheel" being the real moat.
- Example: Prendi Il Caffe's Spinel Ciao Espresso Machine is the same Italian-built Spinel chassis sold by 5+ other Amazon sellers under different brand labels. Prendi's actual moat is the integrated ESE pod catalog, not the machine. This shifted the listing and ad recommendations toward "bundle the consumables story harder" rather than "compete on machine specs."
- Step: 2c (Competitive Landscape)

**92. Parent ASIN restructure should be detected and flagged when get_metrics ignores parent_asin filters**
- When a parent ASIN has been recently created (e.g., a child was promoted to its own parent, or a new parent was created to group existing children), the `get_metrics` tool can silently return account-level data instead of parent-level data because the new parent has no history before its creation date. The workflow currently doesn't detect this. Fix: when get_metrics returns `aggregation_level: "account"` despite a parent_asin filter being passed, flag this as "parent restructure detected" and fall back to either (a) querying the longest-running child ASIN directly, or (b) using account-level data as a proxy with an explicit note that the data reflects the broader account due to parent restructure.
- Example: Prendi Il Caffe's P0 parent (B0G15PDRLK) is a newer parent that took over the long-running Red variant child (B0DQLQYRXM). get_metrics with `parent_asin=B0G15PDRLK` returned account-level data without warning, and the audit had to use account-level annual trend as a proxy with an explicit note.
- Step: 1 (ASIN Selection Step 5 - P0 Annual Trend)

**93. New-to-ads sellers with explosive Feb-Mar growth need a "honeymoon period" diagnostic**
- When a seller's first month of ads is also their best month ever (Feb 2026 was Prendi's biggest month at $8,076, March even bigger at $11,601, all driven by a single auto campaign), this is the "PPC honeymoon period" pattern: low competition + high relevance + Amazon's algorithm favoring new advertisers. It typically lasts 2-4 months before ROAS normalizes downward. The workflow should detect this and frame the action plan accordingly: don't treat current ROAS as the sustainable baseline; expect a 20-30% efficiency decline over the next 90 days and plan accordingly. Currently the audit treats the current ROAS as steady-state.
- Example: Prendi Il Caffe started ads Feb 2026 with a single auto campaign delivering 3.17x ROAS. The action plan assumed this ROAS could be reallocated and scaled, but didn't account for the typical honeymoon-period decay.
- Step: 1 (ASIN Selection annual trend), Section 6 (Action Plan)

---

## From: Abokichi Inc CA Full Audit (2026-05-21)

**94. SQP Analyzer MCP should expose a marketplace filter**
- The SQP Analyzer MCP returns US data only and has no marketplace parameter, even though the underlying Metabase table (`orange_schema.rpt_search_query_performance_brand`) has a `marketplace` column with separate CA/US/UK rows. Brands with multiple marketplaces (Abokichi has 29K CA rows + 27.7K US rows for the same brand_id 229) need a marketplace filter on the MCP to get correct CA SQP data without falling back to direct Metabase SQL. Until this is fixed, multi-marketplace audits must either (a) use US SQP as a proxy with explicit disclaimers, or (b) bypass the MCP and query Metabase directly with `marketplace='CA'`, then re-do tag application manually because the MCP tag store is brand-keyed not (brand, marketplace)-keyed.
- Example: For Abokichi CA, we had to flag in Step 3 that the SQP analysis reflects US market dynamics. Direct Metabase queries showed CA volumes are very different from US ("ramen" 17K CA vs 312K US, "chili oil" 5K CA vs 58K US), so the US numbers significantly mis-represent the CA market sizing.
- Step: 3 (SQP Analysis) - MCP infrastructure

**95. Multi-marketplace seller audits need a sibling-marketplace cross-reference section**
- When a brand sells on both US and CA (or US and UK, etc.), each marketplace audit should explicitly reference the sibling audit's findings where they apply, and flag where they differ. The Abokichi CA audit benefits enormously from the US audit's product understanding (same physical product, same brand story, same customer driver), but the strategic frame is opposite (US is dormant relaunch; CA is profitable scale-up). A standard cross-reference paragraph at the top of each section saying "Sibling marketplace finding: X. Same/different in this marketplace because Y." would speed up the closer's prep when the seller has both.
- Example: Abokichi US TTM revenue is $15K vs CA's $472K. The US audit recommended restarting paused 2023 Auto campaigns ($147 YTD spend); the CA audit recommends scaling Tier 1 dedicated campaigns at $25-40/day. Same brand, same product, opposite levers. Without explicit cross-references, the audit reader has to derive these contrasts themselves.
- Step: All sections in multi-marketplace audits

**96. Master parent rollup in Seller Analytics under-reports parent-level ad attribution**
- When a CA catalog uses a "master parent" structure (one parent ASIN containing many product types as children), `get_pivot_table` at `aggregation_level='parent'` significantly under-reports ad spend because the report's `adjusted_parent_asin` doesn't always match the actual ad-attribution parent on Amazon's side. For Abokichi CA, the master parent B07L53JJVR showed $164 of 90-day ad spend at the parent rollup, but child-level aggregation totaled $7,858 of spend. The workflow should detect this mismatch (parent-level ad_spend << child-level ad_spend on the same date range) and default to child-level aggregation with a note in the audit.
- Example: Abokichi CA's master parent B07L53JJVR has 5 active children (Spicy Single, Mild Single, Curry Single, Mild 2-pack, Spicy 2-pack). Parent-level rollup dropped most of the ad spend; child-level analysis was required for the priority table. We flagged this explicitly in the audit but it should be detected automatically.
- Step: 1 (ASIN Selection)

**97. CA marketplace audit playbook needs a separate frame from US**
- The US audit playbook assumes a relaunch-style frame (small revenue, minimal ads, restart paused campaigns). For CA-only or CA-side audits where the brand is already operating profitably, the framing is "scale and allocation" not "relaunch." The action plan template, the question prompts (the seller is already actively managing, not absent), and the impact-sizing math (proportional to a much bigger TTM base) all need to be adjusted. Create a marketplace-aware variant of the audit playbook or at least an explicit "frame the audit by stage" pre-flight check.
- Example: Abokichi CA has $472K TTM and 3.76 account ROAS already. Recommending "restart paused 2023 campaigns" or framing them as "the brand is barely advertising" would be wrong. The Step 4 frame became "where is the unspent opportunity in an otherwise well-run account?" which required leaning more heavily on Tier 1 underfunding and Product Targeting absence than on cleanup.
- Step: Workflow framing / playbook variant

---

## From: Food Earth Full Audit (2026-05-22)

**98. Misleading parent ASIN structure (9 distinct meals as "variants") needs an extreme-case handler**
- Idea #56 (variant concentration check) and the existing CLAUDE.md note about "meaningfully different products under one parent" both address this, but Food Earth's P0 parent (B0GX9VV9ST) was an extreme case: 9 completely distinct meal SKUs (Vegetable Biryani, Chickpeas Curry, Madras Coconut Curry, Bombay Lentil Curry, Five Lentil Curry, Split Lentil Curry, plus 2 multi-trio bundles, plus the Six Flavor Variety Pack) grouped under one parent. This isn't a color/size variation, it's a catalog-level structural issue that affects ad allocation, buy box analysis, and customer-fit reasoning. When a parent has 5+ children with distinct product names (not variant attribute names like "Color: Red"), the workflow should auto-flag this as a "non-variant parent" pattern and force a child-level priority table in Step 1, not just a parent-level one.
- Example: Food Earth's parent showed 79% buy box at the parent level, but child-level data revealed B086VPCC7N at 14% and B0CQLYTFPK at 56% (likely MAP), while the Variety Pack child sat at 97%. The parent-level number was actively misleading. Same problem on ad allocation: 96% of parent ad spend goes to one child (Vegetable Biryani) while the hero child gets 4%.
- Step: 1 (ASIN Selection), CLAUDE.md Domain Knowledge

**99. Q4-vs-buy-box historical correlation as a named diagnostic**
- When the annual trend (Step 1 Step 5) shows sessions spiking during a known seasonal window (Q4 for Indian food, holiday for gifts, summer for outdoor) AND CVR/buy box dropped simultaneously, this is a "lost peak" diagnostic that deserves its own framing. The audit should: (a) compute the implied lost revenue (if CVR had held at pre-collapse levels, how much extra revenue would the Q4 sessions have produced), and (b) anchor the action plan around the next peak window with a "be ready by" date. Currently this analysis happens through judgment but the framing of "your buy box ate your Q4" is exceptionally compelling for the sales conversation.
- Example: Food Earth's P0 buy box collapsed from 84% to 58% Sep-Dec 2025. Sessions doubled to 3,748 in Dec (vs ~1,700 baseline) but CVR halved from 6.18% to 3.20%. Sales stayed flat at $3K during what should have been the peak demand window. At pre-collapse CVR, those 3,748 sessions would have generated ~$5.7K instead of $3.2K = ~$2.5K of lost peak-month revenue, compounded across 3-4 peak months = $8-10K of lost Q4 revenue. This single framing reframes the entire audit narrative.
- Step: 1 (ASIN Selection Step 5), Section 3 (Quantitative Understanding)

**100. Starved high-ROAS keywords inside overstuffed campaigns deserve a dedicated Step 4a sub-check**
- The current Step 4a (Campaign Structure) detects overstuffed campaigns by target count, then narratively identifies starved keywords. But the single highest-impact ad finding in many audits is a specific keyword with absurdly high ROAS (5x+) sitting at near-zero spend because it's trapped in an overstuffed campaign. The workflow should codify a standard sub-check: after pulling Q713 by campaign, scan for any target with ROAS > 5 AND spend < $20 (or some similar high-ratio threshold), and surface these as a dedicated "Starved Winners" table in the Campaign Structure output. This gives the closer a concrete keyword name to reference, which is much more compelling than a structural critique.
- Example: Food Earth had "indian ready to eat meals" PHRASE at ROAS 14.55 on $11.54 of spend (6 clicks, 4 orders), buried in a 9-target campaign. Also "organic lentil soup" at ROAS 4.63 on $15.53. These were the single most actionable findings in the audit but had to be hand-discovered by reading the Q713 output line-by-line.
- Step: 4a (Campaign Structure)

**101. P0 child misallocation should auto-flag when ad spend is on a different child than organic revenue leader**
- The Food Earth audit's single largest finding was that 96% of P0 ad spend goes to Vegetable Biryani (the second-highest-revenue child) while only 4% goes to the Six Flavor Variety Pack (the highest-revenue child by 33%). This is detectable mechanically: cross-reference the Step 1 child-level revenue table with Q726 child-level ad spend, and if the top revenue child receives < 25% of parent ad spend, flag this as "P0 child misallocation" in Step 4e. Currently this requires the auditor to notice the mismatch by visually comparing two tables.
- Example: Food Earth's Variety Pack child generated $5,333 in 3-mo organic sales (33% of parent revenue) but received $107 of $2,991 in 90-day ad spend (4% of P0 ad budget). The Vegetable Biryani child generated $4,017 (25% of parent revenue) and received $2,884 (96% of ad budget). The mismatch is the entire finding.
- Step: 4e (Product-to-Campaign Mapping)

**102. "Indian/Asian/ethnic food" brand archetype needs Q4 seasonality + Brand Analytics access caveats codified**
- Indian and Asian food brands on Amazon have a specific Q4 seasonality pattern (search volume ~50% higher Nov-Jan vs spring) that the audit caught for Food Earth via SQP. Other ethnic food categories (Mexican, Thai, Filipino) likely have similar patterns. Codify this as a brand archetype with: (a) expected Q4 seasonality multiplier, (b) "be ready by September" action plan anchor, (c) typical category competitors (Tasty Bite, Maya Kaimal, Kitchens of India for Indian; corresponding brands for other ethnic categories), (d) typical rating range for the category (4.2-4.5 for Indian ready-to-eat). This would compress the brand-research time and make audits more consistent.
- Example: Food Earth audit took ~3-4 web searches to establish the competitive set (Tasty Bite, Maya Kaimal, Kitchens of India, Deep Indian Kitchen) and the typical price band ($25-45 for 6-pack). A documented "Indian ready-to-eat brand archetype" reference in CLAUDE.md would compress this to a lookup.
- Step: 2c (Competitive Landscape), CLAUDE.md Domain Knowledge

**103. Catalog overlap check should auto-suggest the adjusted cap rather than rely on judgment**
- The Phase 5 catalog overlap check currently relies on the auditor to look at sibling product names and decide whether they could rank for the same Tier queries, then manually set the adjusted cap. For multi-product Indian food brands like Food Earth, the overlap on "indian food" was 3+ products (P0 bundle, P1 simmer sauce, dips) but the overlap on "tasty bites indian food" was really just P0. The workflow should: (a) for each tagged Tier 1 query, compute a fuzzy-match similarity score between the query and each catalog product name, (b) auto-suggest "N products could rank" based on the score threshold, (c) let the auditor override but show the suggestion. This would make the cap-setting more rigorous and less judgment-driven.
- Example: Food Earth Tier 1 overlap calculation was done in prose. "indian food" → could be served by 3+ products. "tasty bites indian food" + "deep indian kitchen" → mostly P0. The audit manually averaged this to "~16% cap (assuming 2 products on average)" but a more rigorous per-query calculation would have given a sharper cap per query.
- Step: 3a Phase 5 (Catalog Overlap Check)

---

## From: Helmet Flair Full Audit (2026-05-26)

**104. "Wrong-keyword-market" detection: the high-volume queries the brand appears on are an intent trap**
- Helmet Flair's top SQP queries by volume were all intent-mismatched: generic "cat ears" (827k/mo, Halloween costume buyers) and "motorcycle helmets" (450k/mo, helmet buyers), where the brand got impressions but converted at a fraction of industry (3% ATC vs 42%). The actual on-intent queries ("cat ears for helmet" ~800/mo, "motorcycle helmet accessories" ~15k/mo) only surface with a keyword-filtered search, not the default volume-sorted Phase 1/2 pulls. The workflow should add a standard guard: after the Phase 1/2 pulls, run keyword-filtered searches on the literal product type ("for helmet", "<product> accessories") to find the true-intent niche queries, because for category-defining products the high-volume head terms are almost always a different market. Without this, an auditor could mis-tag the generic head term as Tier 1 (I did initially, then corrected).
- Example: Helmet Flair. Generic "cat ears" looked like the obvious Tier 1 hero query but is a costume market that peaks in October (opposite of the brand's spring sales peak). The real Tier 1 ("cat ears for helmet") only appeared via a keyword="for helmet" search and showed the brand already dominating it (~15% impression share, above-industry conversion).
- Step: 3a Phase 1/2 (Tagging)

**105. Seasonality proof via tier-vs-tier search-volume timing (not just brand-vs-market)**
- Beyond idea #50 (brand revenue vs market purchases), Helmet Flair showed a cleaner seasonality proof: the on-intent Tier 2 market (helmet accessories) peaked in spring/summer matching the brand's sales, while the intent-mismatched Tier 3 generic ("cat ears") peaked in October (Halloween). The opposing seasonal timing of two tiers is itself proof that one tier is the brand's real market and the other is a different audience. Codify this as a seasonality cross-check when a brand straddles a generic head term and a niche term.
- Example: Helmet Flair. "cat ears" peaks October (costume); "motorcycle helmet accessories" peaks May-Aug (riding season); brand sales peak May. The timing alignment proved the rider market is real and the costume market is noise.
- Step: 3b (Market Sizing - seasonality check)

**106. Product-targeting-vs-keyword ROAS gap as the PPC proof of an intent-mismatch SQP finding**
- When SQP concludes "this product sells by placement, not by generic search" (category-defining/intent-mismatch case), the Q709 Product-vs-Keyword targeting split is the direct PPC confirmation, and it should be explicitly cross-referenced. The workflow should connect these two findings: if SQP shows intent mismatch on head terms AND product targeting materially outperforms keyword targeting, present them as one unified thesis ("the product wins by appearing on the right listings, not by winning generic keyword auctions").
- Example: Helmet Flair product targeting ran 6.24 ROAS / 9.46% CVR vs keyword targeting 2.87 / 3.44%, perfectly confirming the SQP thesis. The wasted-spend list was almost entirely generic helmet-buyer keyword campaigns ("motorcycle helmet," "full face helmet"), exactly the Tier 3 terms SQP flagged.
- Step: 4d (Targeting Strategy), 4f (Solving P0 Blockers via PPC)

**107. Re-confirm the get_metrics parent-filter limitation (recurring)**
- Same issue as idea #92 (Prendi): `get_metrics` with a `parent_asin` filter silently returned account-level data (aggregation_level: "account") for Helmet Flair. This is now the second confirmed occurrence and is not restricted to recently-restructured parents (Helmet Flair's parents are long-running). Recommend treating it as a general tool limitation: always pull parent-level annual trends via `get_pivot_table(aggregation_level=parent)` and never trust get_metrics' parent_asin filter. Worth fixing at the MCP level.
- Example: Helmet Flair. Two get_metrics calls with different parent_asin values returned byte-identical account-level data. All parent trends were re-pulled via get_pivot_table.
- Step: 1 (ASIN Selection Step 5), MCP infrastructure

---

## From: Dockside Market Full Audit (2026-06-05)

**71. Micro-brand scale pre-check should gate audit depth in Step 1**
- When the trailing-12-month revenue is very small (e.g., under ~$25k/yr) the full multi-step deep-dive (Keepa + SQP + Notion publish) may be disproportionate to the account. Step 1 should compute annual revenue early and, if it falls below a threshold, surface a one-line scale flag and offer a scope choice (full vs lean) before committing tokens. The economics of the engagement change the framing of the whole audit.
- Example: Dockside Market is ~$16.5k/yr. Confirming scope up front (the user chose "full audit") avoided sinking the full deep-dive into a micro-brand without the closer knowing how small it is.
- Step: 1 (ASIN Selection)

**72. Blended tier share can mask a per-query hero - surface the standout query**
- When a tier mixes a low-volume term the brand dominates with high-volume terms where it is invisible, the volume-weighted tier impression share hides the win. The workflow should check within-tier dispersion and, when one query has materially higher brand share than the tier average, call it out separately as the "owned" query with its own funnel read.
- Example: Dockside's blended Tier 1 impression share was 0.27%, but `key lime cake` alone held ~4% share with above-industry CTR and a 16% CVR (vs 5.7% market). The tier average completely buried the brand's single best asset.
- Step: 3c (Market Share), 3d (Blocker Detection)

**73. Gift-occasion / single-SKU-Q4-spike brands need a seasonal-bundle action-plan anchor**
- When a gift brand's December spike is driven primarily by one bundle SKU (not the year-round hero), the action plan should explicitly anchor on the Sep-Dec ramp for that bundle, separate from the year-round hero growth plan. Related to #64 (peak-anchored timeline) but specific to the case where the seasonal engine is a different product from P0.
- Example: Dockside's December was ~40% of annual revenue, led by the Tropical Tower gift bundle ($3,380 in Dec vs ~1 unit/mo otherwise), while P0 (Bundt Cake) is the year-round growth vehicle. The plan had to carry two threads: build the P0 listing/PPC year-round, and front-load the Tropical Tower gift campaigns ahead of Q4.
- Step: 1 (ASIN Selection), Section 6 (Action Plan)

**74. Listing-gates-PPC sequencing for never-advertised sellers with weak PDP conversion**
- For a never-advertised seller whose SQP shows healthy CTR but weak ATC/CVR, the launch plan should explicitly gate the broad/high-volume campaigns behind the listing fix, while still launching the low-risk campaigns (branded + the query the brand already converts on) immediately. This hybrid (launch-the-safe-now, gate-the-broad) is more precise than a blanket "fix listing first, then PPC."
- Example: Dockside has zero ads, healthy CTR, and 15.5% vs 37.4% ATC on Tier 1. The plan launches branded + key lime (proven converters) in Weeks 1-2 but gates the coconut/lemon/orange/rum campaigns until A+/bullets ship in Weeks 4-6.
- Step: 4 (Ad Analysis / launch plan), Section 6 (Action Plan)

**75. Reconcile SQP-attributed purchases against Seller Analytics actual units to quantify off-search demand**
- For brands whose SQP footprint is almost entirely branded (near-zero non-branded share), make a standard SQP output: compare SQP-attributed purchases (branded + non-branded) against the real units sold from Seller Analytics. The gap quantifies how much demand comes from outside captured Amazon search (direct, repeat, off-Amazon/DTC). This single number reframes the whole thesis far better than the share tables alone.
- Example: Periodic Audio sells ~84 units/yr (Seller Analytics) but SQP attributes only ~22 to branded search and ~0 to non-branded, so ~75% of sales come from outside captured search. That reframed the listing as a fulfillment endpoint for off-Amazon demand, not a discovery engine, and made "enter non-branded search" the explicit growth thesis.
- Step: 3c (Market Share and Potential)

**76. Flag premium-priced products whose main image looks like a budget commodity**
- When viewing the P0 main image in Step 2, explicitly cross-check it against the product's price position in the category. If a mid/premium-priced product's main image is visually indistinguishable from the budget commodity version of the same item, flag it as a top-priority CTR and price-credibility fix (not just a generic "improve images" note). This is a distinct, high-impact failure mode from "too few images."
- Example: Periodic Audio's $49 Rhodium DAC main image shows a plain braided cable + USB-A adapter that looks identical to a $9 USB-C-to-3.5mm adapter. The Keepa signals engine's `main_image_optimization` recommendation independently flagged the same fix (add "Hi-Res Audio DAC" overlay, show headphones). Viewing the image plus the price context made it the single clearest conversion lever.
- Step: 2a / 2e (Product & Listing Quality)

**77. Detect the "catalog-on-Amazon gap" for brands with a deep off-Amazon line**
- When the Amazon account is a small slice of a known brand's full product line (verified via the brand website in Step 2b), the biggest growth lever is often bringing more of the catalog onto Amazon, not optimizing the few SKUs that are listed. Elevate this to a primary seller question rather than treating the listed SKUs as the whole opportunity.
- Example: Periodic Audio sells only 3 accessory SKUs on Amazon (one of them dead) while its core identity products, the element-named IEMs and other DACs (Nickel, BlueDAC), are entirely absent. Optimizing a single $49 dongle has a low ceiling; the real question for the closer is whether the full line can come to Amazon.
- Step: 1 (ASIN Selection), 2b (Brand Understanding)
