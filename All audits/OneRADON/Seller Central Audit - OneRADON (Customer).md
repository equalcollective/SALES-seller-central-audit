# OneRADON: Growth Audit

## Market Opportunity

**Tier Breakdown:**

- **Tier 1 (Hero):**
  - **Keywords:** radon detector, radon detector for home, radon monitor, continuous radon monitor, home radon detector
  - **Rationale:** Direct radon monitoring queries. The customer is searching for exactly the type of product Luft is.

- **Tier 2 (Core market):**
  - **Keywords:** air quality monitor indoor radon, radon air quality monitor, wifi radon monitor, air quality with radon, radon monitor plug in, air quality monitor indoor voc radon
  - **Rationale:** Queries combining radon with broader air quality monitoring. Perfect match for Luft's multi-sensor value prop, but very low search volume (~400/mo total).

- **Tier 3 (Broad/adjacent):**
  - **Keywords:** air quality monitor indoor, air quality monitor
  - **Rationale:** Generic air quality monitor queries. Luft competes here but against a much broader set (Airthings, Awair, IQAir). Radon is a differentiator, but not necessarily the primary purchase driver for these searchers.

**Market Sizing:**

| Tier | Monthly Search Volume | Monthly Add to Carts (Market) | Monthly Purchases (Market) | Est. Market Size ($/mo) |
|------|----------------------|-------------------------------|---------------------------|------------------------|
| Tier 1 | 59,939 | 6,866 | 2,742 | $1,160,354 |
| Tier 2 | ~400 | ~9 | ~3 | ~$1,500 |
| Tier 3 | ~30,000 | ~2,643 | ~853 | $446,667 |
| **Total** | **~90,339** | **~9,518** | **~3,598** | **~$1,608,521** |

*Estimated using $169 avg product price.*

**Current Blockers:**

| Tier | Impression Share | CTR (Brand vs Industry) | CVR (Brand vs Industry) | Primary Blocker |
|------|-----------------|------------------------|------------------------|-----------------|
| Tier 1 | 0.014% (of ~8-9% max) | 0.47% vs 1.71% (72% below) | Insufficient data (0 purchases from 29 clicks, annual) | Impression Share + CTR |
| Tier 2 | 0.36% (of ~8-9% max) | Insufficient data | Insufficient data | Impression Share |
| Tier 3 | 0% (invisible) | No data | No data | Impression Share |

The Luft is virtually invisible on Amazon search. On Tier 1 queries alone, the addressable market is $1.16M/month, and the brand captures approximately 0% of it through search. Current sales are almost entirely driven by customers who already know the brand.

When the product does appear, it gets clicked at less than a third the rate of competitors (0.47% vs 1.71% industry CTR). This is driven by the 4.0 rating (vs 4.3-4.5 for competitors), 58 reviews (vs thousands), and a title that doesn't communicate the value proposition clearly at thumbnail size.

## Ad Analysis: Solving for Impression Share

The current ad setup has two campaigns (one auto, one manual exact) spending ~$811 over the last 90 days. The auto campaign (9.01 ROAS) massively outperforms the manual campaign (1.86 ROAS). Five structural changes are needed:

1. **Negate branded search terms from the auto campaign.** The auto campaign's highest-converting terms are branded searches (customers already searching for the brand by name). These inflate the auto campaign's performance metrics but are not driving new customer acquisition. They should be moved to a small, dedicated branded defense campaign so the auto campaign's budget goes toward discovering new non-branded terms.

2. **Increase Top of Search bid modifiers.** Top of Search placement currently receives only 14% of ad spend but delivers 19.36 ROAS and 11.32% CVR. Product Pages receive 49% of spend at just 1.68 ROAS. Setting Top of Search bid modifiers to +150% on all campaigns would shift spend to the placement that actually converts.

3. **Launch Tier 1 keyword campaigns.** Dedicated manual campaigns for each high-volume Tier 1 keyword: "radon detector," "radon detector for home," "radon monitor," "continuous radon monitor," and "home radon detector." Each keyword gets its own campaign with a dedicated daily budget so they can be optimized independently.

4. **Launch broad match, exact match, and phrase match campaigns.** Currently only exact match is being used. Adding phrase and broad match for Tier 1 keywords enables keyword discovery, capturing long-tail variations like "plug in radon detector," "wifi radon monitor for home," and other search terms that exact match misses entirely.

5. **Harvest winners from the auto campaign.** The auto campaign has already identified several non-branded converting search terms (e.g., "indoor air quality monitor" at 5.16 ROAS). These should be extracted into dedicated manual campaigns and negated from auto to prevent bid duplication. Note: "luft radon detector" and similar branded terms should not be harvested into Tier 1 campaigns, as Luft and SunRADON are both the brand's own terms and belong in the branded defense campaign.

## Action Plan

### Weeks 1-2: PPC Restructuring

- Restructure the manual campaign: isolate Tier 1 keywords into separate campaigns with dedicated daily budgets ($10-15/day each)
- Set Top of Search bid modifier to +150% on all campaigns
- Launch exact, phrase, and broad match campaigns for Tier 1 keywords
- Negate branded terms from auto and create a dedicated branded defense campaign ($5/day)
- Harvest non-branded winners from the auto campaign into manual campaigns
- Launch defensive Sponsored Display ads on the Luft product page to block competitor ads (BREATHE and Airthings are currently running targeted ads directly on the listing)

### Weeks 2-6: Listing Optimization

The listing needs both a content refresh and a strategic repositioning to improve conversion on non-branded search terms. Below are the specific changes, ordered by impact.

**Repositioning: Radon Detector First, Air Quality Monitor Second**

The current listing positions Luft as an "indoor air quality monitor that also measures radon." But the vast majority of addressable search volume (Tier 1: 60K/mo) comes from shoppers searching specifically for a radon detector. These shoppers want the most accurate, trustworthy radon detection device. They are comparing against dedicated radon detectors (Airthings Corentium, Ecosense RadonEye) and asking: "Will this accurately detect radon in my home?"

The listing needs to lead with radon detection and SunRADON's 40-year professional heritage. The multi-sensor capability (VOC, CO2, humidity, temperature, pressure) should be positioned as a bonus, not the headline. The shift: "Professional-grade radon detector that also monitors your entire indoor environment."

**Title Rewrite**

Current: "SunRADON luft - Radon and Indoor Air Quality Monitor, Portable Plugin Continuously Measures Also VOC, eCO2, Temperature, Pressure, and Humidity | Wi-Fi Connected | Mobile App Included" (183 chars, readability score 2.7)

Suggested: "luft Radon Detector for Home, Plug-In Indoor Air Quality Monitor by SunRADON - Tracks Radon, VOC, CO2, Temperature, Humidity | Wi-Fi App, Made in USA"

Key changes: leads with "Radon Detector for Home" (the #1 search term), drops the clunky "Portable Plugin Continuously Measures Also," adds "Made in USA" (a trust signal currently absent from the title).

**Bullet Restructuring**

Current bullets are 300-413 characters of dense marketing copy. The strongest selling points are buried: "Made in USA" and "nearly 4 decades of research" are in bullet 5; "no batteries, just plug in" is buried mid-sentence in bullet 4.

Suggested rewrite:
- **Bullet 1:** "MONITOR 6 AIR QUALITY INDICATORS - Continuously tracks radon, VOCs, eCO2, temperature, humidity, and air pressure in one device. The front LED indicator changes color based on air quality levels so you always know your home's status at a glance."
- **Bullet 2:** "ACCURATE RADON DETECTION - Built by SunRADON, the leader in professional radon testing for nearly 40 years with 10 million+ homes tested. The same expertise behind professional-grade equipment, now in a home monitor."
- **Bullet 3:** "PLUG IN AND GO - No batteries, no charging, no maintenance. Plug into any standard wall outlet, connect to Wi-Fi, download the app, and you're monitoring in minutes. The LED doubles as a programmable nightlight."
- **Bullet 4:** "SMART ALERTS ON YOUR PHONE - The free mobile app lets you set custom thresholds for each air quality metric. Get push notifications when levels change so you can take action, whether you're home or away."
- **Bullet 5:** "DESIGNED AND MADE IN THE USA - Every luft monitor is backed by SunRADON's decades of research in radiation detection. Quality construction you can trust for long-term, continuous monitoring of your home's air."

**Image Gallery Optimization (3 of 8 slots to replace)**

| Slot | Current | Action | Replacement |
|------|---------|--------|-------------|
| 1 (Main) | Product + app | Improve | Add badge overlay: "6-in-1 Air Quality Monitor" or "From the Leader in Professional Radon Testing" |
| 3 | Side angle of device | Replace | LED color states explained (green = healthy, yellow = moderate, red = take action). The LED is the primary at-a-glance interface and is never shown in context |
| 4 | Back of device showing regulatory labels | Replace | Detailed app dashboard showing data readouts, trend charts, and alert notifications |
| 5 | Product packaging/box shot | Replace | "Made in USA by SunRADON" credibility image: "35+ Years of Professional Radon Expertise," "10 Million+ Homes Tested" |
| 8 | Duplicate family lifestyle (same concept as slot 7) | Replace | Comparison infographic: Luft vs. traditional test kits (continuous vs. one-time) or Luft vs. competitor features |

**A+ Content Refresh**

The current A+ is standard, not premium. Upgrading to Premium A+ unlocks video modules, interactive comparison tables, and carousel modules. Key changes:

- **Module 1:** Rework the "Trusted by Millions" claim to explicitly tie in SunRADON's heritage: "From the makers of America's #1 professional radon testing equipment, trusted by inspectors for 35+ years"
- **Module 4 (replace):** Current module repeats bullet content. Replace with an app experience walkthrough showing the actual UI: dashboard, historical trends, push notifications, threshold customization
- **Add comparison table module:** Luft vs. Ecosense EcoQube vs. Airthings Wave Plus on key dimensions (number of sensors, power source, heritage, price tier). This directly addresses the comparison-shopping behavior in this category
- **Add FAQ module:** Address top purchase hesitations: How accurate is it vs. a professional test? Is Wi-Fi setup difficult? How long until the first reading? What do I do if radon is high?
