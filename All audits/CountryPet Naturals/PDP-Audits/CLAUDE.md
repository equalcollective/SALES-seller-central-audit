# PDP Audit Workflow

This is the workflow for performing a Product Detail Page (PDP) audit on a prospect's Amazon listing. Within the MerchantBots sales process, this audit happens **before the discovery call** to prepare talking points and demonstrate expertise about the prospect's product, listing quality, and competitive positioning.

## About MerchantBots

- AI-powered Amazon marketing agency
- Parent company is Equal Collective, but MerchantBots operates as an independent brand. Customers must never know about the Equal Collective connection
- Equal Collective also sells "Jeff," an AI sales agent to Amazon agencies. MerchantBots' existence must be shielded from Jeff's customers to avoid conflict of interest

## Required Tools

1. **Metabase MCP** - Connected to the Keepa-sourced ASIN database (product snapshots, signals, price/rating/sales rank history). Used via `execute_query` against `orange_schema` tables (`new_asins`, `new_asin_signals`, `new_asin_rating_history`, `new_asin_sales_rank_history`).
2. **Web search** - For brand understanding and competitive landscape research.

## Important: Only Add What You Are Confident About

Do not add information, insights, or flags unnecessarily. If a bucket (Insights, Things to Investigate, Questions for the Seller) has nothing meaningful to add, leave it blank. Only include information you are genuinely confident is relevant and actionable.

## Important: No Duplication Across Insight Buckets

Every observation goes in exactly ONE bucket. Never repeat the same fact across Insights, Things to Investigate, and Questions for the Seller.

**How to decide which bucket:**
- **Insights:** You are confident about BOTH the what and the why, and you have a solution or clear implication. This is a conclusion, not a hypothesis.
- **Things to Investigate:** You notice something worth exploring further but need more data. Flag it for the discovery call or for a future Seller Central audit.
- **Questions for the Seller:** You have no way to figure out the "why" from the data or tools. Only the seller knows. Include a hypothesis when asking (e.g., "Sales rank dropped significantly in Q4. Is this a normal seasonal pattern, or has something changed?").

If you find yourself wanting to add the same fact to multiple buckets, you haven't decided what you actually know. Stop and decide.

## Important: High Readability

The closer needs to skim this quickly before the discovery call. To ensure this:
- Remove all unnecessary information
- Use bullet points and sub-bullets for clarity. Dense paragraphs are harder to skim than structured pointers
- Whenever referencing a product, include both the **ASIN and product name**

## Important: Writing Style

- **Never use long dashes (em dashes) anywhere in the output.** Use a comma, period, or restructure the sentence instead. Long dashes make text look AI-generated, and audit outputs may be shared with clients.
- Keep language natural and direct. Avoid overly polished or formulaic phrasing.

## Domain Knowledge: Listing and Content

### A+ Content Best Practice
A+ content should be image-only with no standalone text modules. In 2026, shoppers are visual and do not want to read blocks of text on a product page. The ideal A+ layout is high-quality images with any necessary text (feature callouts, comparison info, FAQs) designed directly onto the images themselves. When evaluating a listing's A+ content, do not flag "zero text word count" as an opportunity. Instead, assess whether the images themselves communicate the key selling points effectively. The only time A+ text is a concern is when the images are generic or fail to convey product benefits, in which case the fix is better images with text overlays, not adding standalone text modules.

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

Aryan will provide one or more ASINs to audit. For each ASIN, run the full workflow below.

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
- **A+ Content:** Absent. Baby keepsake = emotional purchase (parents preserving memories). A+ with lifestyle images (finished keepsakes framed on a wall, parent with baby) and comparison module (this product vs messy traditional ink) would strengthen the emotional driver.
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

## Output Format

Save the output to `All Audits/{Seller or Brand Name}/PDP Audit.md`.

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

## Publishing to Notion

After the audit is complete and saved locally, publish to Notion using the **Notion MCP** (`notion-create-pages` tool).

### Parent Page

All PDP audit pages live under **"PDP Audits"** (page ID: `329fde5f528280b5b639f86b80e63d9e`).

### Workflow

1. **Create the seller/brand page** under "PDP Audits" with the seller or brand name as the title
2. **Create a child page** under that seller page containing the full PDP Audit markdown content

### Notes

- Convert markdown content as-is. Notion's markdown renderer handles tables, bullet points, bold text, and headers natively.
- Do this as the last step after the full audit is complete.

## Folder Structure

For every new PDP audit, create a folder named after the seller or brand inside `All Audits/`. Example:

```
PDP-Audits/
├── All Audits/
│   ├── ReignDrop/
│   │   └── PDP Audit.md
│   ├── Magic AutoCare/
│   │   └── PDP Audit.md
```
