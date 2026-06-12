---
name: sales-handover
description: Generate a sales-to-service handover note for a closed prospect. Pulls all Fathom calls with the brand, drafts the Sales Notes following the locked format, resolves the Sales Audit URL if missing, and pushes to the brand's Notion page. Invoked as /sales-handover <brand-name> [<email>].
---

# Sales Handover Skill

Generates the Sales Notes for a closed brand and pushes them (plus the Sales Audit URL if missing) to the brand's Notion page.

## Invocation

```
/sales-handover <brand-name> [<email>]
```

- `brand-name` (required): the brand's name as it appears in the Notion Brands database (e.g., "ReadyRest").
- `email` (optional): an email associated with the prospect. Strongly preferred when available — exact-email match against Fathom `calendar_invitees` is the highest-confidence call lookup signal.

If no brand name is supplied, ask the user before proceeding.

## Required MCP servers

- `notion` — for reading and updating the brand page, and for resolving the Sales Audit URL.
- `fathom` — for finding and pulling call transcripts.

If either is disconnected, surface this and wait for the user to reconnect rather than attempting workarounds.

## Steps

### 1. Locate the brand in Notion

The Brands database lives at `Brand Operations > Brands`. Use `mcp__notion__notion-search` with the brand name; prefer results whose ancestor path includes the Brands database. Fetch the matched page with `mcp__notion__notion-fetch`.

From the page, capture:
- **Brand Name** — the canonical spelling.
- **Status** — must be "Lead Closed." If it isn't, ask the user whether to proceed anyway.
- **Contact Details** — extract any emails. If the user did not provide an email in the invocation, use one from here.
- **Sales Notes** — should be empty. If non-empty, show the existing content to the user and ask whether to overwrite, append, or abort.
- **Sales Audit** — if blank, resolve it in step 5. If non-empty, leave it alone.
- **Account Owner** — for context only.

### 2. Pull all Fathom calls with the prospect

Apply the order of preference saved in memory (`reference_fathom_prospect_call_search.md`):

1. **Exact email match on `calendar_invitees`.** Call `mcp__fathom__list_meetings` with `recorded_by=["aryan@equalcollective.com"]` and a recent date range (default: last 6 months; widen if no hits). Filter to meetings where `calendar_invitees` contains the exact email.
2. **Domain match on `calendar_invitees`.** Derive the domain from the email and re-filter. Use this if exact-email returns zero or only a domain is known.
3. **`mcp__fathom__search_meetings`** with the brand name and `recorded_by="anyone"`. Skim summaries to drop false positives (generic word matches; e.g., "ready" + "rest" appearing separately).
4. **`mcp__fathom__find_person`** with the founder's name and `recorded_by="anyone"`. Extract the founder's name from a seed call's summary if not in Notion.

Combine results across all signals that ran. Deduplicate by `recording_id`. Then apply the internal-vs-external classification rule (`reference_fathom_call_classification.md`): drop any meeting where every entry in `calendar_invitees` is on `equalcollective.com` or a `merchantbots.*` domain.

**Call-count flagging:**
- Exactly 2 calls: proceed silently.
- 1 call: surface in chat ("only found 1 call with {brand}, expected ~2 — proceeding"). Continue.
- 3+ calls: surface in chat ("found {n} calls, expected ~2 — could be real or could indicate missing data, proceeding"). Continue.

### 3. Pull transcripts

For each confirmed call, call `mcp__fathom__get_meeting_transcript` with `recording_id` and `url`. Cap at 3 transcripts per Fathom's guidance; if more, prioritize the most recent ones since they reflect the closing context most directly.

### 4. Read the local audit folder

Read `All audits/{Brand}/Seller Central Audit - {Brand}.md` if it exists. Use this for **background context only** — never pull facts from the audit into Critical Context (per `feedback_sales_notes_handover.md`).

### 5. Resolve the Sales Audit URL (only if the field was blank)

Skip this step entirely if Sales Audit already had a value.

Audit pages live under "Seller Central Audits: MB Sales" (parent page ID `310fde5f528280ccac88e7b7a8373044`).

1. `mcp__notion__notion-search` with `query="Seller Central Audit - {Brand}"`.
2. Filter results to descendants of the parent page.
3. If multiple matches (versioned: v1, v2, v3, etc.):
   - Prefer titles with explicit version suffixes — pick the highest version.
   - If no explicit versions, compare last-edited timestamps and pick the most recent.
4. Use only the consolidated **Seller Central Audit** page URL. Never use the four sub-step pages (ASIN Selection, Product Understanding, SQP Analysis, Ad Analysis).

If the search returns zero matches, flag this in the chat and leave the Sales Audit field blank rather than guess.

### 6. Draft the Sales Notes

**Section order (mandatory unless conditional):**

1. **Brand & Founder** — founder, product, brand context.
2. **Numbers** — combines:
   - Landed cost of goods (assembly, pre/post-tariff caveats, margin implications).
   - Ad spend (current + history of what worked or failed). Omit the bullet if ads were never discussed; keep the section.
   - Commercials sold (commission % only).
3. **Why he's here** — what brought them to MerchantBots; current pain.
4. **Client Goal** *(if discussed)* — the seller's own framing of what they want to achieve. Skip the section entirely if not explicitly stated by the seller.
5. **What Was Pitched** — **always include.** Targets, mechanism, key strategic/creative commitments. Sales-to-service handover fails if the service team doesn't know what we sold.
6. **Critical Context** — call-derived only. Plus any off-topic-but-relevant items that didn't fit a standard heading.

**Strict format rules** (full set in `feedback_sales_notes_handover.md`):
- Never include onboarding fees — only commission %.
- Never include action plans, open questions for onboarding, or References/Links sections.
- Never include Promised Start Date or Permissions in Numbers (those have dedicated Notion fields).
- Critical Context: only items the seller said on the call. Do not pull from the audit. Off-topic but relevant items go in here, not in a separate section.
- For off-topic / unclassified facts, apply the **litmus test** in `feedback_sales_notes_handover.md` ("will the service team do something different because they know this?"). If no, skip silently. The test is *only* for items that don't fit any of the six buckets; the buckets themselves govern what goes in them.
- Follow the **writing style and length target** in `feedback_sales_notes_handover.md`: one idea per bullet, bold lead-ins, compact numbers, no hedging, no cross-references, bullets not prose. Sales Notes should fit one laptop screen ideally, with a hard ceiling of ~1.5 screens.

### 7. Show the draft inline and wait for approval

Show the drafted Sales Notes in chat. If Sales Audit was blank, also show the resolved URL with the page title for confirmation.

Tell the user: "Approve to push, or tell me what to change."

Do **not** push to Notion until the user explicitly approves.

### 8. Push to Notion

On approval, call `mcp__notion__notion-update-page` with `command="update_properties"`:

- Always update `Sales Notes` with the approved draft.
- Update `Sales Audit` only if it was blank at the start.

Confirm completion with the brand page URL.

## Behavioral notes

- Be transparent about which signal found which calls ("found 2 calls via exact email match" or "domain match returned 0, falling back to brand-name search").
- When drafting, briefly note inferences ("client goal not explicitly stated, skipping section").
- Memory rules (`reference_fathom_prospect_call_search.md`, `reference_fathom_call_classification.md`, `feedback_sales_notes_handover.md`) are authoritative — if anything in this skill conflicts with memory, follow memory.
- This skill never modifies the audit md files locally, never touches other Notion fields, and never publishes anything beyond the two specified properties.
