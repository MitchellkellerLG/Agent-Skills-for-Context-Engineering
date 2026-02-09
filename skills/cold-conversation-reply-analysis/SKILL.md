---
name: cold-conversation-reply-analysis
description: Analyze cold email/outreach reply exports to extract GTM intelligence including pain points, objections, persona patterns, campaign performance, and copy effectiveness. Use when client provides reply export CSV, wants to understand what messaging works, or needs ICP refinement from real conversation data.
invocation: user
---

# Cold Conversation Reply Analysis Skill

## Purpose

Extract actionable GTM intelligence from cold email/outreach reply data. Transforms raw conversation exports into:
- Pain points that resonate
- Objection patterns to address
- Persona targeting recommendations
- Campaign/sequence performance insights
- Copy effectiveness analysis
- ICP refinement data

## When to Use

- Client provides a cold email reply export (CSV, Excel)
- Need to understand what messaging is working
- ICP refinement based on who actually engages
- Objection handling playbook creation
- Campaign optimization recommendations
- Copy A/B test analysis

## Input Requirements

**Required:** Reply export file containing:
- Prospect information (name, title, company)
- Reply content (the actual response text)
- Campaign/sequence identifier
- Sequence step number
- Reply timestamp

**Optional but valuable:**
- Reply classification tags (positive, negative, OOO, bounce, etc.)
- Company domain/industry
- Original outbound message (often quoted in replies)

---

## Client Configuration

Before running analysis, load the client's competitor configuration from their `_master.md` or create one.

### Where to Find Competitors

1. **Check client's `_master.md`** - Look for `## Competitors` section
2. **Check client's Research folder** - May have prior competitive analysis
3. **Ask the user** - "Who are the main competitors in this space?"

### What to Capture

When extracting competitor mentions from replies, look for:
- Direct mentions ("we use X")
- Comparison requests ("how vs X")
- In-house solutions ("we built our own")

Add any new competitors discovered in replies back to the client's `_master.md`.

## Analysis Framework

### Phase 1: Data Cleaning & Segmentation

**Step 1.1: Load and inspect data**
```python
# Read CSV with proper encoding
conversations = []
with open(filepath, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        conversations.append(row)
```

**Step 1.2: Filter out noise**
Remove from analysis:
- Hard bounces (undeliverable)
- Soft bounces (mailbox full, etc.)
- Pure OOO without referrals
- Automated unsubscribe confirmations

**Step 1.3: Segment meaningful replies**
| Category | Definition | Priority |
|----------|------------|----------|
| Hot leads | POSITIVE_TONE, WILLING_TO_MEET | Immediate action |
| Warm leads | NEEDS_MORE_INFO, internal referral mentions | High priority |
| Objections | HAS_SOLUTION, BAD_TIMING, specific pushback | Learn from |
| Neutral engaged | Real human response, not automated | Nurture |
| OOO with referral | Contains alternative contact | New leads |
| Opt-outs | Explicit unsubscribe | Remove from lists |

---

### Phase 2: Pain Point Extraction

**Step 2.1: Extract original outbound copy from replies**

Most reply exports include quoted original messages. Parse these to see exactly what copy generated each response.

Look for patterns:
- `On [date], [sender] wrote:` (Gmail format)
- `From: [sender]` followed by `Subject:` (Outlook format)
- `>` quoted text blocks

**Step 2.2: Map responses to copy elements**

For each positive/warm response, identify which copy elements were present:

| Copy Element | Look For | Evidence of Effectiveness |
|--------------|----------|---------------------------|
| Accuracy claims | "X% accuracy", specific numbers | Prospect tested product, asked for proof |
| Feature mentions | Specific capabilities listed | Prospect asked about specific feature |
| Pain point hooks | "replace X", "cut Y in half" | Prospect acknowledged the pain |
| Credibility signals | Team background, customer logos | Prospect mentioned trust factor |
| Benchmark/proof | Links to data, comparisons | Prospect clicked or referenced |
| ROI promises | Cost/time savings | Prospect asked about pricing |

**Step 2.3: Extract pain points from prospect language**

Analyze actual prospect replies for pain language:

```
PAIN INDICATORS:
- "we currently use [competitor]" → Displacement opportunity
- "we're struggling with [X]" → Direct pain admission
- "how does this compare to [Y]" → Active evaluation
- "we built our own" → DIY pain (maintenance burden)
- "our current solution doesn't [Z]" → Feature gap pain
- "we've been looking for" → Active search
- "this is exactly what we need" → Problem-solution fit
```

---

### Phase 3: Objection Pattern Analysis

**Step 3.1: Categorize objections**

| Objection Type | Example Language | Implication |
|----------------|------------------|-------------|
| **Already have solution** | "We have our own team", "We use [X]" | Wrong ICP or need displacement angle |
| **Not the right person** | "I'm just a [role]", "Not my area" | Targeting wrong titles |
| **Bad timing** | "Check back in Q2", "Busy until [date]" | Nurture sequence needed |
| **No need** | "We don't do [X]", "Not relevant" | ICP qualification issue |
| **Security/deployment** | "Not pursuing hosted", "On-prem only" | Product gap or messaging gap |
| **Price/value** | "Too expensive", "What's the ROI" | Need value proof |
| **Competitor preference** | "How vs [specific competitor]" | Competitive content needed |

**Step 3.2: Quantify objection frequency**

```
Objection Distribution:
- Already have solution: X%
- Wrong person: X%
- Bad timing: X%
- No need: X%
- Other: X%
```

**Step 3.3: Extract competitor mentions**

Track every competitor mentioned in replies:
- Direct mentions ("we use LlamaParse")
- Comparison requests ("how vs Reducto")
- Implicit references ("we built our own")

---

### Phase 4: Persona Analysis

**Step 4.1: Title pattern analysis**

Group responses by title patterns:

```
TITLE CLUSTERS:
- C-level: CEO, CTO, CXO, Founder
- VP/Director: VP Engineering, Director of Data
- Manager: Engineering Manager, Data Science Manager
- Senior IC: Senior Engineer, Staff Engineer, Principal
- IC: Engineer, Data Scientist, Analyst
- Other: Consultant, Freelancer, Academic
```

**Step 4.2: Conversion by persona**

| Title Cluster | Total Replies | Hot Leads | Conversion Rate |
|---------------|---------------|-----------|-----------------|
| C-level | X | Y | Z% |
| VP/Director | X | Y | Z% |
| ... | ... | ... | ... |

**Step 4.3: Response quality by persona**

Analyze HOW different personas respond:

```
C-LEVEL PATTERN:
- Shorter responses
- Delegate to team ("forwarding to my team")
- Schedule-focused ("after [date]")
- Decision language ("let's do it")

ENGINEER PATTERN:
- Technical questions
- Competitor comparisons
- Feature-specific inquiries
- Skeptical tone, need proof

MANAGER PATTERN:
- Process questions
- Team fit concerns
- Integration questions
```

**Step 4.4: Identify wrong-fit personas**

Flag titles that consistently produce:
- "Wrong person" responses
- No engagement
- Irrelevant objections

---

### Phase 5: Campaign Performance Analysis

**Step 5.1: Metrics by campaign/sequence**

| Campaign | Total Replies | Hot | Warm | Objection | Bounce Rate |
|----------|---------------|-----|------|-----------|-------------|
| Campaign A | X | Y | Z | W | V% |
| Campaign B | X | Y | Z | W | V% |

**Step 5.2: Sequence step analysis**

| Step | Responses | Hot Leads | Notes |
|------|-----------|-----------|-------|
| Step 1 | X | Y | First touch effectiveness |
| Step 2 | X | Y | Follow-up effectiveness |
| Step 3 | X | Y | Persistence payoff |
| Step 4+ | X | Y | Diminishing returns? |

**Step 5.3: Identify winning campaigns**

Calculate conversion rate (hot leads / total meaningful replies) per campaign.

---

### Phase 6: Copy Effectiveness Analysis

**Step 6.1: Reconstruct templates from quoted messages**

Extract the actual email templates used by parsing quoted content in replies.

**Step 6.2: Element-by-element analysis**

For each copy element, track:
- Presence in messages that generated hot leads
- Presence in messages that generated objections
- Specific responses to that element

| Element | In Hot Lead Emails | In Objection Emails | Verdict |
|---------|-------------------|---------------------|---------|
| "98% accuracy" claim | 4/5 | 2/5 | Effective |
| Competitor benchmark | 3/5 | 3/5 | Mixed |
| Feature list | 5/5 | 4/5 | Expected |
| Team credibility | 2/5 | 1/5 | Good for follow-up |

**Step 6.3: CTA analysis**

Track response rates by CTA type:
- "Open to a call?"
- "Worth a quick chat?"
- "Can I send more info?"
- "Want to test it?"

---

### Phase 7: GTM Recommendations

**Step 7.1: ICP refinement**

Based on analysis, recommend:

```markdown
## ICP Refinement

### Target (High Conversion)
- Company type: [X]
- Company size: [X]
- Titles: [X, Y, Z]
- Signals: [X]

### Deprioritize (Low ROI)
- Company type: [X]
- Titles: [X]
- Signals: [X]
```

**Step 7.2: Messaging recommendations**

```markdown
## Messaging Updates

### Keep (Working)
- [Element]: [Evidence]

### Change (Not Working)
- [Element]: [Problem] → [Recommendation]

### Add (Gap)
- [New element]: [Why needed based on objections]
```

**Step 7.3: Campaign recommendations**

```markdown
## Campaign Optimization

### Scale
- [Campaign]: [Why - conversion rate, volume]

### Fix
- [Campaign]: [Problem] → [Recommendation]

### Kill
- [Campaign]: [Why - low performance, wrong audience]
```

---

### Phase 8: Knowledge Base Update

**After analysis, update the client's `_master.md` with learnings.**

This creates a feedback loop where every conversation analysis enriches the client's knowledge base.

**Step 8.1: Update Competitors section**

Add any newly discovered competitors:
```markdown
## Competitors

### Direct Competitors (mentioned in replies)
- [Competitor]: Mentioned X times, context: "[quote]"

### In-House Solutions
- X prospects mentioned building their own
```

**Step 8.2: Update Pain Points**

Add validated pain points with evidence:
```markdown
## Pain Points (Validated)

### [Pain Point Name]
- Evidence: "[prospect quote]"
- Frequency: X mentions
- Effective copy: "[what worked]"
```

**Step 8.3: Update Objection Handling**

Add common objections and recommended responses:
```markdown
## Objection Handling

### "[Objection]"
- Frequency: X%
- Root cause: [Why this happens]
- Response: [How to address]
```

**Step 8.4: Update ICP (Exclude List)**

Add wrong-fit personas to avoid:
```markdown
## ICP Exclusions

### Titles to Avoid
- [Title]: [Why - evidence]

### Company Signals to Avoid
- [Signal]: [Why]
```

**Step 8.5: Confirm updates with user**

Before writing to `_master.md`:
1. Show proposed additions
2. Get user approval
3. Append to appropriate sections

---

## Output Deliverables

### 1. Reply Analysis Summary
`[client]/Research/[date]-reply-analysis-summary.md`

Contents:
- Total replies analyzed
- Segmentation breakdown
- Key metrics

### 2. Pain Point & Objection Report
`[client]/Research/[date]-pain-points-objections.md`

Contents:
- Pain points extracted (with evidence quotes)
- Objection patterns (with frequency)
- Competitor mentions

### 3. Persona Analysis
`[client]/Research/[date]-persona-analysis.md`

Contents:
- Conversion by title
- Response patterns by persona
- Wrong-fit personas to avoid

### 4. Copy Effectiveness Report
`[client]/Research/[date]-copy-effectiveness.md`

Contents:
- Winning templates (full text)
- Element-by-element analysis
- CTA performance

### 5. GTM Intelligence Summary
`[client]/Research/[date]-gtm-intelligence.md`

Contents:
- ICP refinement recommendations
- Messaging updates
- Campaign optimization
- Competitive intelligence

---

## Example Queries to Extract Intelligence

### Pain Point Extraction
```
"What specific problems did prospects mention?"
"Which features did prospects ask about?"
"What are they currently using and why is it failing them?"
```

### Objection Analysis
```
"Why did prospects say no?"
"Which competitors are they comparing against?"
"What concerns do they have?"
```

### Persona Patterns
```
"Which titles convert best?"
"How do CTOs respond differently than engineers?"
"Who should we stop targeting?"
```

### Copy Analysis
```
"What messaging drove the hot leads?"
"Which claims generated the most engagement?"
"What's missing from our current messaging?"
```

---

## Integration with Other Skills

- **Enrichment Agent**: Enrich companies from positive responses
- **Cold Email Copywriting**: Apply learnings to new copy
- **Campaign Management**: Update targeting based on findings
- **Proposal Generation**: Use pain points in proposals

---

## Quality Checklist

Before delivering analysis:

- [ ] Filtered out bounces and noise
- [ ] Extracted actual email templates from quoted text
- [ ] Quantified objection patterns
- [ ] Identified persona conversion rates
- [ ] Mapped pain points to specific copy elements
- [ ] Provided actionable recommendations
- [ ] Included evidence quotes for key findings
- [ ] Saved outputs to appropriate client folder
