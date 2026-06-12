---
name: pdp-audit
description: Audit a single Amazon listing before the discovery call. Builds product, customer, brand, competitive, target keywords, listing-quality, and rating/sales-rank history from Keepa (Metabase) + web search, then publishes to Notion. Invoked as /pdp-audit <asin-or-brand>.
argument-hint: [ASIN or brand name]
---

# PDP Audit Workflow

MerchantBots is an AI-powered Amazon marketing agency. The sales process involves outreach, a discovery call, and then a deeper second call. This workflow covers the **PDP (Product Detail Page) audit**, which happens **before the discovery call**. The goal is to analyze a prospect's Amazon listing so the closer walks into the call with product knowledge, listing gaps, and competitive context ready to discuss.

## Required Tools

1. **Metabase MCP** - Connected to the Keepa-sourced ASIN database (product snapshots, signals, price/rating/sales rank history). Used via `execute_query` against `orange_schema` tables (`new_asins`, `new_asin_signals`, `new_asin_rating_history`, `new_asin_sales_rank_history`).
2. **Web search** - For brand understanding and competitive landscape research.

## Important: Only Add What You Are Confident About

Do not add information, insights, or flags unnecessarily. If a bucket (Insights, Things to Investigate, Questions for the Seller) has nothing meaningful to add, leave it blank. Only include information you are genuinely confident is relevant and actionable.

## Important: Insight Buckets

Throughout the audit, every step will surface observations. Each observation is categorized into exactly one of three buckets. These buckets accumulate across all steps and are consolidated in the final output.

**Where observations come from:** Every step can produce observations. Step 1 (Product & Customer) might reveal a confusing value prop. Step 2 (Brand) might reveal no online presence. Step 3 (Competitive Landscape) might reveal the product is priced 40% above market with no clear differentiator. Step 5 (Listing Quality) might reveal missing A+ content on an emotional-purchase product. Step 6 (Historical Trends) might reveal a declining rating. All of these feed into the three buckets below.

**The three buckets:**

- **Insights:** You are confident about BOTH the what and the why, and you have a clear implication or solution. This is a conclusion, not a hypothesis. Example: "No A+ content on an emotional-purchase product (baby keepsake). Adding lifestyle imagery showing finished keepsakes would strengthen the conversion driver."
- **Things to Investigate:** You noticed something interesting but need more data to draw a conclusion. This could be explored on the discovery call, or in a future Seller Central audit if the prospect converts. Example: "Sales rank improved significantly in Q4 but rating stayed flat. Could be promotion-driven or seasonal. Worth exploring in SQP data if we get access."
- **Questions for the Seller:** You have no way to figure out the "why" from the data or tools. Only the seller knows. Always include a hypothesis. Example: "Sales rank dropped significantly in Q4. Is this a normal seasonal pattern for this category, or has something changed (stockout, competitor launch, listing suppression)?"

**No duplication across buckets.** Every observation goes in exactly ONE bucket. If you find yourself wanting to add the same fact to multiple buckets, you haven't decided what you actually know. Stop and decide.

## Important: High Readability

The closer needs to skim this quickly before the discovery call. To ensure this:
- Remove all unnecessary information
- Use bullet points and sub-bullets for clarity. Dense paragraphs are harder to skim than structured pointers
- Whenever referencing a product, include both the **ASIN and product name**

## Data Sources

**Keepa-sourced ASIN database** via Metabase MCP (Database: "Jeff Azure Db Public", ID: 4, schema: `orange_schema`):

| Table | Metabase ID | Purpose |
|-------|-------------|---------|
| `new_asins` | 260 | Product snapshot: title, features, description, images, category, brand, ratings |
| `new_asin_rating_history` | 267 | Historical rating changes over time |
| `new_asin_sales_rank_history` | 272 | Historical sales rank by category |
| `new_asin_signals` | 270 | Computed listing quality signals: title, bullets, A+, images, videos |

**How tables link:** All history tables reference `new_asins` via `new_asin_id` (foreign key to `new_asins.id`). To query history for a specific ASIN, first get its `id` from `new_asins` by filtering on `asin = '<ASIN>'`.

**Marketplace handling:** The database may contain the same ASIN across multiple marketplaces (US, UK, CA, and more over time). Do NOT hardcode `marketplace = 'US'`. Instead:
1. Query by ASIN without a marketplace filter first
2. If multiple marketplace rows exist, pick the one where the product is selling more, using review count (`rating_dist_total`) or other snapshot signals as a proxy
3. Use that marketplace's `id` for all subsequent history queries

**Data conventions:**
- **Ratings:** Stored as rating x 10 (integer). `45` = 4.5 stars.
- **Images:** Stored as JSONB: `{"main": "imageId.jpg", "variants": ["id1.jpg", ...], "count": N}`. To view, prefix with `https://m.media-amazon.com/images/I/`.

## Workflow

### Input

Aryan will provide either:

1. **An ASIN directly** (e.g., "B07J298M2Z"). Search it in `orange_schema.new_asins` and proceed.
2. **A brand name** (e.g., "ReignDrop"). Search for it in `orange_schema.new_asins` by the `brand` field, review the products found, and confirm with Aryan which ASIN(s) to audit.

**If the ASIN is not found in the database:** The ASIN has not been ingested into our Keepa system yet. Prompt Aryan to ingest the ASIN using our ingestion system before proceeding. Do not attempt to run the audit without the Keepa data, as Steps 1, 5, and 6 depend on it.

For each confirmed ASIN, run the full workflow below.

### Step 1: Product & Customer Understanding

**Tool:** `execute_query` (Metabase MCP)

```sql
SELECT asin, marketplace, title, brand, description, features,
       category_tree, product_group, department,
       images, videos, aplus,
       current_rating, rating_dist_total,
       rating_dist_one_star, rating_dist_two_star,
       rating_dist_three_star, rating_dist_four_star,
       rating_dist_five_star,
       is_sns, id
FROM orange_schema.new_asins
WHERE asin = '<ASIN>'
```

If multiple rows (marketplaces) are returned, pick the one with the higher `rating_dist_total` and use that row's `id` going forward.

Then download and view the main product image:
1. Extract the `main` value from the `images` JSONB field
2. Construct URL: `https://m.media-amazon.com/images/I/{image_id}`
3. Download via curl and view

From this data + the image, build understanding of:

**Product:**
- One-line description of what the product is
- What makes it unique: key features, materials, formulation, design
- How it adds value: what problem does it solve
- Why people buy it: the core purchase motivation

**Customer:**
- Who is the target buyer (demographic, use case, skill level)
- What problem or need drives the purchase

### Step 2: Brand Understanding

**Source:** Product data (brand name, images already viewed) + web search

Steps:
1. Note the brand name from the product data
2. Search the web for the brand's website and online presence
3. If not confident the correct website was found, ask Aryan for the URL

**Output:**
- Is this a generic/white-label brand or a registered brand with real identity?
- Brand maturity: new, established, DTC-first, Amazon-native?
- Notable brand signals: professional website, social media presence, retail distribution, other sales channels
- Brand vibe: the aesthetic and emotional tone the brand projects

### Step 3: Competitive Landscape

**Source:** Web search (search for the product type/category)

Search for the product category to identify:
- Top 2-4 competitor brands in this space
- Their key products that compete directly with the ASIN
- General price range in the market, giving a proxy for where the ASIN sits (premium, mid-range, budget)

**Output:**
- Who are the main competitors (brand + product)?
- Where does the ASIN sit in the market: premium, mid-range, budget?
- Any obvious differentiation or gaps?

### Step 4: Target Keywords

**Source:** Inferred from everything above: product understanding, customer profile, competitive landscape

Identify 5-10 keywords that a customer would search on Amazon to find this product.

**Output:**
- Mix of high-intent specific terms and broader category terms
- Ordered by estimated relevance/volume (judgment call)

### Step 5: Listing Quality & Conversion Drivers

**Tool:** `execute_query` (Metabase MCP)

Pull the computed listing signals for this ASIN. Reference: [Signals Documentation](https://mb-prod-docs.vercel.app/docs/jeff/signals)

**Table structure:** `new_asin_signals` uses an EAV (row-per-signal) format. Each row has: `signal_name`, `value_int`, `value_float`, `value_bool`, `value_text`, `computed_at`, `new_asin_id`.

```sql
SELECT signal_name, value_int, value_float, value_bool, value_text
FROM orange_schema.new_asin_signals
WHERE new_asin_id = <id from Step 1>
  AND signal_name IN (
    'title_character_length', 'title_repeated_keywords_count', 'title_repeated_keywords',
    'title_has_brand', 'title_readability_score',
    'bullet_count', 'bullet_total_length',
    'bullet_1_length', 'bullet_2_length', 'bullet_3_length', 'bullet_4_length', 'bullet_5_length',
    'bullet_has_allcaps_first_word', 'bullet_readability_score',
    'has_aplus', 'aplus_module_count', 'aplus_is_premium', 'aplus_text_word_count',
    'aplus_image_count', 'aplus_has_alt_text',
    'image_count', 'main_image_optimization',
    'has_video', 'video_count', 'video_has_over_30_sec',
    'has_brand_store'
  )
ORDER BY signal_name
```

**Signals to skip:** Rating rates (`rating_rate_*`), pricing (`price_changes_*`, `has_coupon_*`), units sold (`units_sold_growth_*`), sales rank (`bsr_change_*`), PPC keywords. These are either unreliable or covered better by other data sources.

**How to analyze:** Do not just report the raw signal values. Cross-reference them with what you already know:

- **From Step 1:** You have seen the product images and read the title, bullets, and features. You know what the listing actually looks like.
- **From Step 3:** You have researched competitors and seen their listings, images, titles. You know what "good" looks like in this category.
- **From Step 4:** You know the target keywords. You can check whether the title and bullets actually contain them.

For each listing component (title, bullets, images, A+ content, video), only flag it if there is a genuine gap. If it's fine, skip it. The goal is actionable observations, not a checklist.

**Examples of good observations** (from ReignDrop baby ink pad, B07J298M2Z):

- **Title:** 184 chars, includes brand, no repeated keywords
  - Safety angle ("Safe & Gentle Acid Free") buried at the end, cut off on mobile
  - Middle section is marketing fluff ("Creates Impressive Long Lasting Keepsake Stamp")
  - Suggested rewrite: "ReignDrop Baby Ink Pad for Footprint & Handprint - Safe, Acid-Free, Easy to Wipe Off Skin - Smudge Proof Keepsake Stamp for Newborn, Infant & Toddler (Black)"
- **Bullets:** 3 bullets (should be 5)
  - Bullet 3 is a generic Amazon international product disclaimer, not a real selling point. Wasted slot.
  - Neither real bullet addresses the #1 parent concern: safety. "Safe for baby skin" and "acid-free" appear in the title but are never expanded in the bullets. Safety should be bullet #1.
  - Pet paw prints (strong secondary use case) is buried mid-sentence in the multipurpose bullet. Should lead or get its own bullet.
  - **Suggested rewrite:**
    - Bullet 1: "SAFE FOR BABY SKIN - Made with acid-free, non-toxic ink that's gentle on newborn hands and feet. Wipes clean with baby wipes or warm water, no scrubbing needed."
    - Bullet 2: "MESS-FREE PRINTS EVERY TIME - Our ink pad creates crisp, smudge-proof prints without the mess of liquid ink. Press, print, done."
    - Bullet 3: "PERFECT KEEPSAKE - Capture your baby's tiny handprints and footprints in the first weeks. Frame-ready prints that last a lifetime."
    - Bullet 4: "WORKS FOR PET OWNERS TOO - Create paw print keepsakes for dogs and cats. Same safe, easy-to-clean formula."
    - Bullet 5: "INCLUDES EVERYTHING YOU NEED - 2 ink pads, 4 imprint cards, and a reusable storage case. Makes a great baby shower gift."

**Bullet length guidance:** When bullets are too long (200+ characters of dense text), shoppers stop reading. Optimize for scannability: lead with the benefit in caps, follow with 1-2 short supporting sentences. When bullets are too short (under 80 characters), they waste an opportunity to add relevant keywords and address buyer concerns. Every bullet should earn its space by communicating a distinct benefit and containing relevant search terms.

- **A+ Content:** Absent. Baby keepsake = emotional purchase (parents preserving memories). A+ with lifestyle images (finished keepsakes framed on a wall, parent with baby) and comparison module (this product vs messy traditional ink) would strengthen the emotional driver.

**A+ Content analysis tip:** When A+ content IS present, load and view the actual A+ module images. The `aplus` field in `new_asins` contains the A+ module data, and images can be viewed by constructing the URL from the image IDs (same prefix: `https://m.media-amazon.com/images/I/`). Review the actual images to give specific feedback, e.g., "Module 3 shows a generic lifestyle image that doesn't demonstrate the product in use. Replace with a side-by-side comparison showing the ink pad result vs. a traditional ink mess." Generic feedback like "improve A+ content" is not useful. Look at what's actually there and suggest specific changes.
- **Video:** Absent. Product's biggest selling point is "easy, no-mess process" but there's no way to demonstrate that without video. A 30-second clip (ink pad to finished print to wiping baby's foot clean) would address the main purchase hesitation.

**Examples of bad observations (avoid these):**
- "Title length is 87 characters" (so what?)
- "Consider adding A+ content" (generic, no context)
- "Image count is 5" (just restating a number)
- "Bullets are short, avg 80 chars each. Competitors use 200+ chars." (character length is objective and obvious. What content should change?)

### Step 6: Historical Trends

**Tool:** `execute_query` (Metabase MCP)

#### Rating History

```sql
SELECT rh.timestamp, rh.rating
FROM orange_schema.new_asin_rating_history rh
WHERE rh.new_asin_id = <id from Step 1>
ORDER BY rh.timestamp DESC
```

Rating is stored as integer x 10 (so `45` = 4.5 stars).

Look for:
- **Rating trajectory:** Improving, declining, or stable?
- **Recent drops:** Could indicate a product quality issue, bad batch, or listing hijack
- **Rating relative to category:** Context matters (4.2 in supplements is different from 4.2 in electronics)

#### Sales Rank History

```sql
SELECT srh.timestamp, srh.category_id, srh.rank
FROM orange_schema.new_asin_sales_rank_history srh
WHERE srh.new_asin_id = <id from Step 1>
ORDER BY srh.timestamp DESC
```

Look for:
- **Rank trend:** Lower rank = more sales. Gaining or losing momentum?
- **Seasonality:** Recurring patterns (e.g., better in winter, worse in summer)
- **Spikes:** Sudden improvements (promotions?) or sudden drops (stockouts?)
- **Stability:** Stable good rank = consistent demand. High volatility = unpredictable.

If nothing stands out in the historical trends, note "stable" and move on.

### Step 7: Save, Publish & Deliver

Once Steps 1-6 are complete, save the output locally and publish to Notion.

#### Save Locally

Save the output to `PDP audits/{Brand Name} - PDP Audit.md`.

### PDP Audit: {Product Name} ({ASIN})

**Product:**
- One-line description of what the product is
- What makes it unique: key features, materials, formulation, design
- How it adds value: what problem it solves
- Why people buy it: the core purchase motivation

**Customer:**
- Who is the target buyer (demographic, use case)
- What problem or need drives the purchase

**Brand:**
- Generic/white-label vs registered brand with real identity
- Brand maturity: new, established, DTC-first, Amazon-native
- Notable signals: website quality, social presence, retail distribution
- Brand vibe

**Competitive Landscape:**
- **Price positioning:** One line showing average market price, ASIN price, percentage difference
- Top 2-4 competitor brands and their key competing products (table format)
- Key differentiators or gaps

**Target Keywords:** 5-10 keywords ordered by estimated relevance

**Listing Quality:**

Split into two sub-sections. Each listing component (Rating, Title, Bullets, Images, A+ Content, Video, Brand Store) goes into exactly one based on whether it's a strength or an opportunity.

**Strengths:**
- Components where the listing is genuinely strong. If nothing stands out, leave blank.

**Opportunities:**
- Components with genuine gaps or improvements. No minor nitpicks.

Rating (X.X from N reviews, note star distribution only if skewed) goes in whichever sub-section fits.

**Rating Trajectory:** Improving / Stable / Declining + brief context

**Sales Rank Trajectory:** Improving / Stable / Declining / Seasonal + brief context

### Insights

Confident conclusions from the data. The "what" and "why" are both clear.

### Things to Investigate

Observations worth exploring on the discovery call or in a future Seller Central audit.

### Questions for the Seller

Questions where the data alone cannot explain the "why." Always include a hypothesis.

#### Publish to Notion

Publish to Notion using the **Notion MCP** (`notion-create-pages` tool).

All PDP audit pages live under **"PDP Audits"** (page ID: `329fde5f528280b5b639f86b80e63d9e`).

1. **Create a page** under "PDP Audits" with the brand name as the title (e.g., "ReignDrop")
2. The page content is the full PDP Audit markdown

Notes:
- Convert markdown content as-is. Notion's markdown renderer handles tables, bullet points, bold text, and headers natively.

## Folder Structure

All audit files live directly inside `PDP audits/`, named as `{Brand Name} - PDP Audit.md`. No subfolders per brand since each audit is a single file.

```
seller-central-audits/
├── PDP audits/
│   ├── ReignDrop - PDP Audit.md
│   ├── Magic AutoCare - PDP Audit.md
│   ├── SortJoy - PDP Audit.md
```
