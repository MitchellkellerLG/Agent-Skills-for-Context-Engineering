---
name: cross-client-ground-truth
description: Extract universal cold email patterns ranked by C/I (Contacts per Interested Reply) across all clients. Pulls live EmailBison API stats, computes C/I ratios, segments by ground truth threshold (C/I < 500), and abstracts campaign content into structural attributes. Use when reviewing cross-client performance, building new client copy from proven patterns, updating the LeadGrow playbook, or answering "what actually works?"
triggers:
  - cross-client patterns
  - ground truth extraction
  - what's working across clients
  - universal patterns
  - playbook update
  - copy patterns
  - C/I ratio
  - contacts per interested
tools: []
---

# Cross-Client Ground Truth Extraction

Extract universal cold email patterns ranked by **C/I (Contacts per Interested Reply)** — the number of contacts you burn to get one interested reply.

## The Only Metric: C/I Ratio

**C/I = Total Contacts / Interested Replies**

- Lower is better (134 = great, 10,327 = catastrophic)
- Reply rate lies (5.3% reply with 0 interested = worst campaign)
- Open rate lies (deliverability noise)
- C/I tells the truth about what it costs to start a conversation
- **Ground truth threshold: C/I < 500** — any campaign converting better than 1-in-500 qualifies regardless of contact volume

## When to Use

- Monthly review after campaign cycles complete
- Before writing copy for a new client (start from proven C/I patterns)
- After any client hits C/I < 200 (feed winner back in)
- When updating the LeadGrow internal playbook

## Inputs

| Input | Required | Source |
|-------|----------|--------|
| Live EmailBison stats | Yes | EmailBison MCP → `list_campaigns` + `campaign_split_test_stats` per workspace |
| Client winning copy | Yes | `Clients/*/campaigns/winning/` |
| Campaign analytics reports | Recommended | `Clients/*/campaign-reports/` |
| Research validation matrices | Recommended | `Clients/*/campaign-reports/*Validation*` |
| Sales intelligence | Optional | `Clients/*/sales-intelligence/` |

## Extraction Workflow

### Step 1: Pull Raw Numbers

For every client workspace in EmailBison:

1. `emailbison_rotate_workspace` to each client workspace
2. `emailbison_list_campaigns` to get all campaigns
3. `emailbison_campaign_split_test_stats` for campaigns with contacts > 0
4. Record: campaign ID, contacts, replies, interested, reply rate, interested rate

**Critical:** Get ACTUAL numbers from the API. Don't trust percentages in report files — compute C/I from raw contacted/interested counts.

### Step 2: Compute C/I and Classify

For every campaign with interested > 0, compute:

```
C/I = contacted / interested
```

Classify campaigns:

| Category | Criteria | What to Do |
|----------|----------|------------|
| **GROUND TRUTH** | C/I < 500 (interested > 0) | Extract patterns — volume adds confidence, not qualification |
| **OUTSIDE GROUND TRUTH** | C/I >= 500, interested > 0 | Not efficient enough to extract winning patterns from |
| **CONFIRMED FAILURES** | 0 interested regardless of scale | Equally important — what NOT to do |

**The threshold is C/I, not contact volume.** A campaign with 300 contacts and 4 interested (C/I = 75) qualifies. A campaign with 10,000 contacts and 1 interested (C/I = 10,000) does not. Volume is a confidence multiplier — weight high-volume ground truth campaigns heavier in decision-making, but don't exclude low-volume campaigns that clear the C/I bar.

### Step 3: Abstract Campaign Content

**Strip all client names, product names, and campaign topics.** Replace with structural attributes:

| Attribute | Categories |
|-----------|------------|
| **Hook Type** | hypothetical (blank-check, magic-wand), feedback-frame, pain-poke, emotional+exclusivity, direct-question, product-angle, ultra-short-1-liner, confrontational-challenge |
| **Copy Length** | ultra-short (<25w), short (35-45w), medium (60-75w) |
| **CTA Type** | see-options, email-exchange, binary (or-not-really), demo/trial, ROI-question |
| **Subject Type** | cultural-reference, pain-based, generic-safe, jargon-curiosity, emotional, benefit-based |
| **Platform** | Google, Outlook, Mixed |
| **Sequence Length** | 1-step, 2-step, 4-step |

**Why abstract:** The report must surface STRUCTURAL patterns, not "run the Toronto GEO campaign again." What made it work was the hook type + copy length + CTA, not the topic.

### Step 4: Pattern Analysis

Rank every structural attribute by average C/I across ground truth campaigns (C/I < 500):

#### A. Hook Types (ranked by avg C/I)
- Which hook types produce the lowest C/I?
- Which hooks are consistent (narrow range) vs volatile?
- Which hooks fail catastrophically?

#### B. Copy Length vs C/I
- Does short beat medium universally, or is it hook-dependent?
- Where does ultra-short fail?

#### C. CTA Type vs C/I
- Which CTAs pair with which hooks?
- Does friction level correlate with C/I?

#### D. Subject Line Pattern vs C/I
- Cultural-reference vs generic-safe vs pain-based
- Which patterns are safe defaults?

#### E. Platform Comparison
- Gmail vs Outlook on same copy (controlled comparison only)
- Is the gap real or noise?

#### F. Sequence Design
- Does adding steps improve C/I?
- What's the Step 2 pattern that works universally?
- Does colleague-referral (Step 3) work outside its original vertical?

### Step 5: Extract Anti-Patterns

**Equally important as winners.** For confirmed failures (0 interested) and outside-ground-truth campaigns:

- What hook type was used?
- What was the copy length?
- What was the reply rate? (high reply + 0 interested = vanity metric trap)
- Why did it fail? (wrong vertical, wrong CTA friction, stripped copy, etc.)

Key anti-patterns to check:
- Confrontational hooks (high reply, 0 conversion)
- Product-first framing (leads with what you built, not what they feel)
- Ultra-short stripped copy (removes personality that drives conversion)
- Reused copy on wrong list (audience-copy fit degradation)

### Step 6: Scaling Analysis

Compare C/I at different contact volumes for the same copy pattern:

```
C/I at <2K contacts → C/I at 2K+ contacts → Degradation factor
```

**Key question:** Does winning copy maintain its C/I when scaled to bigger lists? The answer determines whether to scale by writing better copy or finding better-fit audiences.

### Step 7: Report Generation

Output structured report with:

1. **Ground Truth Table** — All C/I < 500 campaigns ranked, abstracted by structural attributes
2. **Outside Ground Truth** — C/I >= 500 campaigns with lessons on what NOT to do
3. **Confirmed Failures** — 0 interested campaigns with anti-patterns
4. **Structural Pattern Rankings** — Hook, length, CTA, subject all ranked by avg C/I
5. **The Scaling Problem** — How C/I degrades with list expansion
6. **Ground Rules** — What the data PROVES vs what it DOESN'T prove
7. **Testing Priorities** — What experiments would add the most knowledge

## Output Location

```
Leadgrow/Operations/campaign_management/ground-truth-report-[YYYY-MM].md
```

## Refresh Cadence

- **Monthly:** Full extraction after campaign cycles complete
- **Ad-hoc:** After any client hits C/I < 200
- **Quarterly:** Deep review with trend analysis across months

## Integration Points

| Skill | How Ground Truth Feeds It |
|-------|--------------------------|
| `write-campaign-copy` | Proven C/I patterns become default hook/CTA/length choices |
| `spintax-spam-check` | Anti-pattern hooks feed "avoid" list |
| `deep-research` | ICP surprises from conversions inform new client onboarding |
| `comprehensive-email-campaign-analysis` | New winners get fed back into next extraction |
| `situation-miner` | Validated pain points (from interested replies, not just replies) inform targeting |
| `campaign-state-of-market` | C/I benchmarks for evaluating individual client performance |
