---
name: cold-email-personalization-v2
description: Complete cold email system teaching research-driven personalization with bracketed variables, "poke the bear" openers, custom signal hunting, follow-up sequences, and strict QA. Integrates creative ideas campaigns, skeptical ICP mapping, and value-exchange CTAs.
version: 2.0.0
thinking: disabled
---

# Cold Email Personalization (GEX Style) - Complete System

## When to use this Skill
Use this Skill for *cold outbound email* ideation, drafting, personalization, variant testing, research-to-first-line mapping, follow-up sequences, or QA cleanup.

## Philosophy (what "good" looks like)
- **Message market fit before cleverness**: Show you understand the person/company immediately
- **Research IS the personalization**: Custom signals prove you did your homework
- **Personalization in the first line** with variables `{VARIABLE_NAME}` or whole-offer strategy (see [copy-formats.md](copy-formats.md) for EmailBison variable convention)
- **Tight, conversational copy** (plain text, minimal fluff); 40-80 words for first email
- **No links in first email** (offer benchmarks, case studies, or demos in follow-ups)
- **One job per email**: Single sharp question or CTA
- **Evidence-led angles**: Competitor deltas, stack reveals, hiring signals, recent content, outcomes
- **Earn replies, not just meetings**: Confirm situation before selling

## Core Principles

### 0. Research Sufficiency Check (Before Writing)

**Before drafting any copy, verify you have sufficient context.** If missing critical information, request additional research rather than writing weak copy.

**Minimum requirements to write effective copy:**
- [ ] Clear understanding of the **offer** (what we're selling, key differentiator)
- [ ] Defined **ICP** (who we're targeting, their role, their pains)
- [ ] At least one **proof point** (case study, metric, social proof)
- [ ] Understanding of **current state** (how they solve this today)

**If any are missing, STOP and request:**
- Client's `_master.md` file (see `Clients/[client]/_master.md`)
- Previous campaign copy from `Clients/[client]/Campaigns_Copy/`
- ICP research from `Clients/[client]/Research/`
- Case studies or proof points
- Competitor/market context

**Red flags that indicate insufficient research:**
- Can't articulate the offer in one sentence
- Don't know the ICP's current workaround/status quo
- No specific metrics or proof points available
- Unclear on what makes this offer different

**Action:** Ask for the missing context before proceeding. Better to pause and gather intel than write generic copy that won't convert.

### 1. Targeting > Messaging (But Both Matter)
Good targeting with bad messaging wastes qualified prospects. This skill assumes decent targeting and focuses on making the message match your list quality. However, if specific data isn't available, you can still send effective emails using broader strategies.

### 2. Two Paths to Personalization
**Path A: Custom Signal Research** (when you have time/data)
- 10-minute research method
- Find 1-2 custom signals unique to this prospect
- Lead with that signal in first line using `{VARIABLE_NAME}` format

**Path B: Whole Offer Strategy** (when you lack specific data)
- Subject + first line preview text = entire value prop
- Self-selection: they either need it (open) or don't (ignore, less likely to mark spam)
- Still targeted to your ICP, just broader personalization

**Both are valid.** Choose based on data availability and campaign scale.

### 3. Conversational & Punchy Tone

Write like you're texting a smart colleague, not drafting a business letter:
- **Short sentences.** Fragments are fine.
- **Questions > Statements** (questions engage, statements inform)
- **Active voice always:** "Your parser strips the data" not "The data gets stripped"
- **Cut corporate speak:** Never use "leverage", "utilize", "optimize", "synergy", "innovative"
- **No em-dashes (—):** Use periods or commas instead

### 4. Formatting Rules (Non-Negotiable)

| Rule | Do This | Not This |
|------|---------|----------|
| **No em-dashes (—)** | Periods, commas | "We help—" |
| **No en-dashes (–)** | Periods, commas | "Save time–money" |
| **No double hyphens (--)** | Periods, commas | "Results--fast" |
| **No double spaces** | Single space | "word  word" |

**Why:** Em-dashes look sales-y, trigger spam filters, and break the conversational tone.

### 5. "See Feel Touch" Sensory Language

Use visceral, concrete words that create mental images:

| Abstract (Avoid) | Sensory (Use) |
|------------------|---------------|
| "data loss" | "all that work, gone" |
| "process failure" | "crash at step 47, start over at step 1" |
| "accuracy issues" | "your parser strips the strikethrough" |
| "inefficient" | "80% of your week is glue code" |
| "unreliable" | "your agent has amnesia" |

**Sensory word bank:**
- Visual: blind, see, strip, hide, vanish, expose
- Physical: crash, break, drift, lock, freeze, burn
- Emotional: amnesia, lie, betray, embarrass, trust

**Examples:**
- "Your agent isn't broken. It's blind." (sensory: blindness)
- "The parser lied. The model believed it." (sensory: betrayal)
- "All that context, vanished." (sensory: disappearance)

### 6. The "Specifically" Line (3x Conversion Booster)
When reaching out to companies that all do different things but your service applies universally:

> "Specifically, it looks like you're trying to sell to {{customer_type}}, and we can help with that."

**When to use:**
- Outbound agencies, newsletters, marketing services (universal application)
- Any B2B service where you can AI-generate their customer type
- NOT for obvious target markets (vacuum cleaners → hotels)

**Why it works:** Shows you understand THEIR specific business, not just yours.

## Variable Schema

### Core Variables (always try to include)
- {{first_name}}, {{company_name}}, {{role_title}}, {{department}}
- {{company_domain}}, {{industry}}, {{hq_location}}

### High-Signal Variables (use when available)
- {{tenure_years}}, {{recent_post_topic}}, {{recent_post_date}}
- {{press_headline}}, {{event_webinar_title}}, {{event_date}}
- {{competitor}}, {{category_competitors}}
- {{stack_crm}}, {{stack_marketing}}, {{stack_data}}
- {{hiring_roles}}, {{open_roles_count}}
- {{traffic_trend}}, {{conversion_goal}}, {{kpi_at_risk}}

### AI-Generated Variables (dynamic)
- {{ai_customer_description}}: "fitness enthusiasts who want to breathe better"
- {{ai_customer_type}}: "VPs of Finance" or "professional men looking for classic styles"
- {{ai_generation}}: Flexible contextual generation based on website/LinkedIn

### Custom Signal Variables (campaign-specific)
Define these per campaign based on your offer:
- {{g2_review_complaint}}, {{github_repo_found}}, {{security_page_outdated}}
- {{pricing_page_insight}}, {{hiring_spike_dept}}, {{competitor_mentioned}}
- {{negative_review}}, {{google_cid}}, {{follower_count}}

### Case Study Variables
- {{case_study_company}}, {{case_study_result}}, {{case_study_metric}}
- {{case_study_customer_type}}, {{case_study_timeframe}}

**Formatting rules:**
- Always show variables in `{{double_braces}}` in drafts
- Never invent facts; if unknown, omit or use broader strategy
- Variables can be dynamically generated via AI or scraped via Claygent/ZenRows

## Research Method

### Before Research: Define Your Perfect Signal
Complete this sentence for every campaign:
> "The ideal prospect would show evidence of **[specific behavior/change/problem]** because it means they're experiencing **[pain]** right now."

### Research Priority (10 minutes max)

**Tier 1: Case Studies (3 min) - START HERE**
1. Go to company website → case studies/customers page
2. Extract 3 examples: customer type, problem, metric, outcome, timeframe
3. Look for patterns: "Most [customer type] see [result] within [timeframe]"
4. Variables to capture: {{case_study_company}}, {{case_study_result}}, {{case_study_metric}}

**Tier 2: Custom Signals (6-7 min) - THE DIFFERENTIATOR**
Hunt for campaign-specific signals:
- **If selling to sales:** Hiring velocity, G2 reviews of their tools, job posts mentioning quotas
- **If selling to marketing:** Competitor insights via SimilarWeb, pricing page analysis, ad creative
- **If selling to ops:** GitHub repos, Zapier templates, manual processes mentioned in job posts
- **If selling to local businesses:** Google reviews (negative reviews = opportunity), follower counts
- **If selling to SaaS:** Pricing tiers (use Claygent + ZenRows), LinkedIn posts, funding news

**Tier 3: Standard Variables (3-4 min) - BACKUP**
- LinkedIn: role, tenure, recent posts, follower count
- Company site: blog, press, events
- Hiring page: open roles, department growth
- Tech stack: footer badges, BuiltWith, job descriptions

**Time budget:**
- If you find a Tier 1 or Tier 2 signal → Write the email
- If you find only Tier 3 → Consider whole-offer strategy instead
- If you find nothing after 10 min → Skip this prospect or use fallback campaign

### Tools & Techniques
- **Claygent**: Find pricing pages, case studies, news
- **ZenRows**: Scrape full page text (pricing, reviews)
- **Serper**: Google Places CID, reviews, local business data
- **SimilarWeb**: Competitor traffic, keyword overlap
- **Clay's sitemap tool**: Find specific pages (pricing, about, case studies)

## Subject Line Strategy

### Two Approaches

**Approach A: 2-4 Words (Intrigue)**
Best when using custom research signals.

Examples:
- "Partnership?"
- "Quick question"
- "Outbound edge"
- "Competitor insights"
- "Saw your post"
- "LinkedIn ideas"

**Test:** Can a colleague or potential customer send this? If yes, good.

**Approach B: Whole Offer in Subject + Preview**
Best when data is limited or offer is self-selecting.

Example:
- Subject: "Ever chase renters to pay on time?"
- Preview: "We built a platform that rewards renters for paying on time so you can increase your NOI."

**When to extend beyond 4 words:** Only when pitching the whole product between subject + preview text, and the offer is punchy enough to fit.

**Rules:**
- Keep it conversational (not salesy)
- Don't explain everything (intrigue > information)
- Match it to email content (no bait-and-switch)

## Email Structure

### PRIORITY: Shorter & Punchier (40-80 words target)

**Default to tight format. Every word must earn its place.**

### Standard Email Structure

**Line 1: Situation Recognition (1 sentence)**
Describe THEIR exact situation. Be direct.
- "Saw you posted about {{ai_generation}}—seems like it was {{days_ago}} days since the one before that."
- "Noticed you sell to {{job_titles}}."
- NOT: "I hope this email finds you well!" (delete)
- NOT: Long-winded observations (cut)

**Line 2: Value Prop + Proof (1-2 sentences MAX)**
What you do + metric. No fluff.
- "We helped companies like Lemlist double down on social with our scheduling tool."
- "We've attributed a 4.7x increase in upgrades after adding product videos."
- NOT: "We help companies scale their marketing efforts through innovative solutions..." (too vague, too long)

**Optional: The "Specifically" Line (1 sentence)**
If applicable:
> "Specifically, it looks like you're trying to sell to {{customer_type}}, and we can help with that."

**Line 3: Low-Effort CTA (1 sentence)**
Binary question or simple offer.
- "Worth a look?"
- "Could I send you access?"
- "Just confirm Vanta is a good example and I can send the engagers."
- NOT: "Would you be open to scheduling 15 minutes next Tuesday at 2pm to discuss how we might be able to help you achieve your goals?" (way too long)

### Punchy Example (72 words)
```
Saw you hired 4 SEs last quarter—building custom workflows for every deal?

Most teams hit a wall at deal #30 when workflows don't scale. We helped similar teams automate this and 3x deal volume.

Worth a look?
```

### Even Tighter (48 words)
```
{{First_name}}—noticed {{hiring_spike}} on the team.

Have you figured out {{process}} without adding headcount, or still manual?

We help teams 3x volume with same headcount. {{case_study_metric}} for similar companies.

Worth exploring?
```

## How to Make Emails Punchier

### The Cutting Process

**After drafting, go through 3 cutting passes:**

**Pass 1: Delete fluff (target: cut 20%)**
- Remove all greetings ("I hope this finds you well")
- Remove all "I wanted to" / "I was wondering" phrases
- Remove all hedging ("perhaps", "maybe", "I think")
- Remove corporate speak ("solutions", "innovative", "cutting-edge")

**Pass 2: Compress sentences (target: cut 15%)**
- Replace clauses with periods (break long sentences)
- "We built a platform that can do X" → "We do X"
- "It seemed like X is focused on Y" → "X is for Y"
- Combine redundant ideas into one sentence

**Pass 3: Cut adjectives (target: cut 10%)**
- Keep only adjectives that are specific data ("4.7x", "Series B", "23%")
- Delete all others ("great", "amazing", "powerful", "robust")

**Total target: 40-45% shorter after 3 passes**

### Quick Compression Tactics

**Tactic 1: Kill intro phrases**
- "I wanted to reach out because..." → Just start with the point
- "I was wondering if..." → Just start with the point
- "I hope you don't mind me asking..." → Just start with the point

**Tactic 2: Break long sentences with periods or commas (never use em-dashes)**
- "Saw your post, and I noticed you haven't posted in a while, so I thought..."
- Better: "Saw your post. Noticed it was {{days}} days since the one before."

**Tactic 3: Delete all "that" and "which"**
- "We built a platform that can pull everyone that is engaging..."
- Better: "We pull everyone engaging..."

**Tactic 4: Active voice always**
- "It seemed like Starter is focused on getting people access..."
- Better: "Starter gives platform access..."

**Tactic 5: Numbers > words**
- "thirty days" → "30 days"
- "three times" → "3x"
- "four point seven times" → "4.7x"

**Tactic 6: Abbreviate where clear**
- "versus" → "vs."
- "Chief Revenue Officer" → "CRO" (if they'd know it)
- But NOT "b/c" or "w/" (too casual)

### The 50-Word Challenge

**Exercise:** Can you say the same thing in 50 words?

If your draft is 90 words, challenge yourself to get it to 50 without losing:
- The situation recognition
- The value prop
- The metric/proof
- The CTA

**Usually you can.** And it'll be better.

## Campaign Types

**See [copy-formats.md](copy-formats.md) for 4 proven copy templates:** Founder Card, Deliverable Hook, Direct Offer, Outcome-First.

### 1. Custom Signal Campaign
**When:** You have strong research data (case studies, pricing insights, reviews, hiring, etc.)

**Structure:**
- Subject: 2-4 words, intriguing
- First line: Custom signal with {{variable}}
- Body: Value prop + case study proof
- CTA: Low-effort question

### 2. Creative Ideas Campaign
**When:** You can generate specific, credible ideas for them

**Requirements:**
- Define 3-5 specific features/capabilities you offer (the constraint box)
- Research their website/challenges
- Generate 3 bullet point ideas, each using ONE feature

**Structure:**
```
{{First name}} – I was back on your site today and had some marketing ideas for you.

{{Creative Ideas}}
• Idea 1: [Specific action using Feature X]—would help with [their pain]
• Idea 2: [Specific action using Feature Y]—could improve [their goal]
• Idea 3: [Specific action using Feature Z]—might address [their challenge]

But of course, I wrote this without knowing anything about your current bottlenecks and goals.

If it's interesting, we could hop on a call and I'd be happy to share what's working in the {{industry}} industry.
```

**Critical:** Ideas must be credible (feature-constrained) and specific to them.

### 3. Whole Offer Campaign
**When:** Limited data availability or self-selecting offer

**Structure:**
- Subject: Describes the pain/outcome (can be longer than 4 words)
- Preview text: Completes the offer
- Body: Explain the offer, add light personalization if possible
- CTA: Simple yes/no or low-friction

### 4. Fallback Campaign ("Let Me Know If...")
**When:** You're not 100% sure they're the right person

**Structure:**
```
{{First name}} – let me know if {{employee_1}} or {{employee_2}} would be better to speak about {{specific_problem}}.

[Rest of email]
```

**Why it works:** Gets personalized with employee names, shows you did research, gives them an easy out (or forward).

## Follow-Up Sequence Philosophy

**IMPORTANT: All sequences are 2 emails only.** Research shows diminishing returns after Email 2. Keep it tight.

### Email 1 (Day 0)
- New subject line
- Full campaign (research + value prop + CTA)
- Try to book meeting or earn reply

### Email 2 (Day 3-4)

- **No subject line** (threads to Email 1 in SmartLead/Instantly)
- **Different value proposition** - rotate through "save time / save money / make money"
- **OR** offer resources/redirect if Email 1 was strong
- This is the **final email** - no Email 3 or 4

**After Email 2:** If no reply, mark for re-engagement in 90 days with a NEW signal. Do not send more emails.

## ICP & Objection Mapping

**See [icp-objection-mapping.md](icp-objection-mapping.md) for the full skeptical ICP role-play framework.**

Key principles:
- Role-play the skeptical ICP before writing (how do they do this now? why switch?)
- Personal benefit matters (they want to look smart, leave on time, get promoted)
- Preempt objections in copy ("Have you figured out X, or still manual?")

## CTAs: Value-Exchange > Generic Asks

### Bad CTAs (Delete These)
- "Can we schedule 15 minutes?"
- "Are you available for a quick call?"
- "Let's chat sometime"
- "Would love to connect"

### Good CTAs (What They Get)

**Category 1: Confirmation (Earn Reply)**
- "Is this still the case?"
- "Curious—are you already doing X?"
- "Worth exploring?"
- "Just confirm [example] is accurate or any others"

**Category 2: Value-Exchange (Why Meet)**
Explain what THEY get in exchange for their time:
- "...so I can understand the situation and plead your case to Google"
- "...to walk you through 3 custom ideas specific to {{company}}"
- "...so I can show you the engagers of your competitor's last 10 posts"
- "...to share what's working in the {{industry}} industry right now"

**Category 3: Resource Offer (Low Commitment)**
- "Could I send you access to try it out?"
- "Would it be useful if I sent those over?"
- "Let me know if I should send a video of how this works"

**The Test:** Can they reply in 5 words or less? If no, simplify.

## Opener Patterns ("Poke the Bear")

### #1 Classic
- Do you already have a reliable way to {{problem}}?
- How are you currently handling {{process}}?
- Who owns {{area}} internally today?

### #2 Status Pressure / FOMO
- Have you solved {{problem}} yet or is it still manual?
- Are you already doing {{practice}} like the top firms in your space?
- Have you figured out how to do {{outcome}} without adding headcount?

### #3 Soft Humility
- I may be wrong, but do you have something in place for {{area}}?
- Totally possible you solved this—how do you handle {{process}} today?

### #4 Efficiency / Leverage
- How are you doing {{task}} without adding headcount?
- What's your process for {{task}} without manual work?

### #5 Risk-Based
- How are you avoiding {{negative_outcome}} as you scale?
- How do you make sure {{critical_task}} doesn't slip through the cracks?

### #6 Binary
- Is your process for {{area}} where you want it?
- Will your current setup scale 12 more months?

### #7 Redirect (Fallback)
- Let me know if {{employee_1}} or {{employee_2}} would be better to speak about {{problem}}

## QA Checklist

**See [qa-checklist.md](qa-checklist.md) for the full 13-point checklist and autofix rules.**

Quick reference:
- 40-80 words (strict)
- No em-dashes, en-dashes, or double hyphens
- Email 2 must use casual opener (e.g., "Oh totally forgot to mention")
- Variables in `{{double_braces}}`
- "Would I reply?" test = YES

## Scoring Rubric (0-100)

| Dimension | Weight | What's Measured |
|-----------|--------|----------------|
| Situation Recognition | 25 pts | Specific data about them? |
| Value Clarity | 25 pts | Clear offer + proof? |
| Personalization Quality | 20 pts | Custom signal OR AI insight? |
| CTA Effort | 15 pts | 5 words or less to reply? |
| Punchiness | 10 pts | **40-80 words? No fluff?** |
| Subject Line | 5 pts | 2-4 words OR whole offer? |

**85+ = Ship it**
**70-84 = Needs one more pass**
**<70 = Start over**

## Generation Workflow

### Step 1: Campaign Setup
1. Define your offer (1-2 sentences)
2. Complete the sentence: "The ideal prospect shows evidence of [behavior] because..."
3. List 3-5 specific features/capabilities (for creative ideas campaigns)
4. Identify personal benefit (not just business ROI)

### Step 2: Research (10 min max)
1. Hunt case studies (3 min)
2. Hunt custom signals (6-7 min)
3. Fill standard variables (backup, 3-4 min)
4. If no strong signal found → Use whole-offer strategy OR skip prospect

### Step 3: Choose Strategy
- Custom signal campaign (if you found Tier 1/2 signal)
- Creative ideas campaign (if you can generate credible ideas)
- Whole offer campaign (if data is limited but targeting is solid)
- Fallback campaign (if unsure about fit)

### Step 4: Draft Variants
Generate 3 variants using different:
- Opener patterns
- Value props (save time vs save money vs make money)
- CTAs (confirmation vs value-exchange vs resource offer)

### Step 5: QA
Run checklist (see above)

### Step 6: Output
Return JSON:
```json
{
  "v1": "email text",
  "v2": "email text",
  "v3": "email text",
  "subject_lines": ["option 1", "option 2", "option 3"],
  "notes": "Explanation of angles and why they should work",
  "used_variables": ["{{first_name}}", "{{ai_generation}}", ...],
  "missing_variables": ["{{tenure_years}}", ...],
  "score": 85,
  "recommended_variant": "v2"
}
```

## Files in This Skill

- **SKILL.md** (this file): Main framework and principles
- **copy-formats.md**: 4 copy templates (Founder Card, Deliverable Hook, Direct Offer, Outcome-First)
- **research-playbook.md**: Deep dive on finding custom signals with tools
- **follow-ups.md**: 2-email sequences only, with value prop rotation and casual openers
- **creative-ideas.md**: How to generate credible, feature-constrained ideas
- **icp-objection-mapping.md**: Role-play skeptical ICP before writing
- **qa-checklist.md**: 13-point checklist and autofix rules
- **examples.md**: Real campaign examples with annotations
- **frameworks.md**: All email frameworks including Hormozi Formula and Binary Soft CTA
- **8th-grade-modifier.md**: Reading level enforcement (Flesch-Kincaid ≤ 8.0)
- **persona-modifiers.md**: How to adapt copy for Technical Founders, Engineering Leaders, IC Engineers, and Ops Owners
- **vertical-adaptation.md**: How to create industry-specific versions for Insurance, Finance, Legal, Healthcare, KYC, and RAG

## Final Reminders

1. **Research IS the personalization** - Custom signals > clever copy
2. **Earn replies, not just meetings** - Confirm situation first
3. **When in doubt, simplify** - Shorter, clearer, more direct
4. **Test and iterate** - Use scoring rubric to improve over time
5. **Whole offer strategy is valid** - Not every email needs deep personalization if targeting is solid

Now draft with confidence.
