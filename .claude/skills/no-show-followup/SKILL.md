---
name: no-show-followup
description: >-
  Write a short, curiosity-driven no-show follow-up message that gets an Amazon
  prospect back on a discovery call. Pulls one or two concrete findings from the
  prospect's completed PDP audit as proof of work, teases the rest as the tip of
  the iceberg, and gives away almost nothing. Use when a prospect no-showed a
  call and we need a re-engagement text/email/DM.
argument-hint: [brand name or ASIN]
allowed-tools: Read, Glob, Grep
---

# No-Show Follow-Up Message

Generate a re-engagement message for a prospect who no-showed their discovery
call. The job: prove we already did the work, spike curiosity, and get them
back on a 15-minute call. Short, value-driven, gives away almost nothing.

## Step 1: Identify the prospect

The argument is a brand name or ASIN.

- **If no brand or ASIN is provided, ask the user for the ASIN (or brand)
  before doing anything else.** Do not guess and do not proceed without it.
- Once you have it, look for the audit at `PDP audits/{Brand} - PDP Audit.md`.
- If not found, Glob `PDP audits/*.md` and match on brand or ASIN.
- If still not found, tell the user and offer to run the PDP audit first. Do
  not invent findings. Every value-added point must come from a real audit.

## Step 2: Pick the value-added points

Read the audit's Insights, Opportunities, Things to Investigate, and Questions
for the Seller. Rank candidate findings by:

1. Revenue impact (how much it could move sales)
2. Ease (how fast/cheap it is to fix)
3. How concrete and provable it is (does it name a real detail of THEIR listing)

Turn the top 3-4 into "value-added points": each is a 1-2 line tease that is
specific enough to prove we read their exact listing, but withholds the actual
fix. The default lead VAP is the single highest-impact AND easiest finding
(e.g. a missing top-volume keyword).

Each VAP must:
- Name a concrete detail from their listing (proof we looked).
- State the cost/consequence in plain terms.
- NOT explain how to fix it.

## Step 3: Write the output

Produce TWO sections.

### Section A: Value-added point menu (3-4 options)
Each as a drop-in block, so the user can swap which finding leads.

### Section B: Three message variants
- Variant 1: ONE value-added point.
- Variant 2: TWO value-added points.
- Variant 3: Creative / easiest-yes. Pick the single most compelling angle to
  pull a yes from a slightly-guilty no-show. Often a risk reversal ("even if we
  never work together, the list is yours"), a sharp curiosity gap, or a bold
  but credible revenue claim anchored to one proof point. Invent fresh each
  time; do not reuse a template.

End by asking which VAP and variant they want, then offer to finalize.

## Writing rules (non-negotiable)

- One idea per line. Hard line break after almost every sentence.
- Short sentences. No paragraph is more than 1-2 lines. Assume it is read on a
  phone, so lots of white space, never a wall of text.
- Keep the whole message short. The prospect's attention is the scarcest thing.
- Value-driven but stingy: reveal one concrete finding (two for Variant 2) to
  prove the audit. Withhold the fix and the other ~100 levers.
- Always include the curiosity frame: this is the tip of the iceberg, 100+
  levers, the big ones move real revenue.
- Open with a brief, warm acknowledgment of the no-show. No guilt-tripping.
- Close with a low-friction CTA: 15 minutes + [link].
- Use placeholders [Name] and [link].
- Never use long dashes (em dashes). Use a comma, period, or restructure.
- Keep language natural and direct. Avoid polished, formulaic, "AI" phrasing.
