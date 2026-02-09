---
name: campaign-state-of-market
description: Comprehensive campaign analysis with ICP refinement, copy pattern extraction, research validation, and test planning. Use when client needs full performance review, ICP validation from conversions, next-cycle test copy, or testing roadmap. Outputs State of Market report + Research Validation Matrix.
mcp: EmailBison
tools: []
---

# Campaign State of Market Analysis

Deep-dive campaign analysis that extracts ICP insights, validates research hypotheses, generates next-cycle test copy, and produces a comprehensive State of Market report.

## When to Use This Skill

- Client asks for "full campaign review" or "state of market"
- Need to validate ICP assumptions against actual conversions
- Want to extract winning copy patterns for replication
- Planning next test cycle (7/14/30 day roadmap)
- Comparing campaign learnings to prior research (EMERGENT vs CANONICAL)
- Need list segmentation recommendations based on conversion data

## When NOT to Use This Skill

- Quick metric check (use [[.claude/skills/email-campaign/analyze/SKILL]])
- Setting up new campaigns (use [[.claude/skills/email-campaign/setup/SKILL]])
- Writing net-new copy without performance data
- Weekly batch reviews across all clients

## Prerequisites

- EmailBison MCP configured
- Client has completed campaign (ideally 5,000+ contacts, 10+ interested)
- Export of interested leads (CSV from EmailBison)
- Prior research documents for comparison (ICP docs, copy research)

## Inputs Required

| Input | Source | Purpose |
|-------|--------|---------|
| Workspace name | User | EmailBison context |
| Interested leads CSV | EmailBison export | Lead profiling |
| Research docs | Client folder | Research validation |
| Copy variants doc | Client folder | Pattern extraction |

## Process

### Phase 1: Campaign Performance Data

1. **Switch workspace**
   ```
   mcp__bison_mcp__emailbison_rotate_workspace
   workspace_name: "[Client]"
   ```

2. **List campaigns and get details**
   ```
   mcp__bison_mcp__emailbison_list_campaigns
   mcp__bison_mcp__emailbison_campaign_details (for each)
   ```

3. **Get split test stats**
   ```
   mcp__bison_mcp__emailbison_campaign_split_test_stats
   ```

4. **Calculate efficiency metrics**
   - Primary: Contacts/Interested (lower = better)
   - Secondary: Reply rate, Interested conversion rate
   - Rank variants by efficiency

### Phase 2: Engaged Lead Analysis

5. **Request interested leads export**
   - User exports from EmailBison dashboard
   - CSV should include: Company, Title, Employee Count, Location

6. **Profile engaged leads**
   - Firm type distribution (PE vs VC vs other)
   - Firm size distribution (micro/small/mid/large)
   - Geographic distribution
   - Title analysis (which roles convert?)
   - Sector clustering

7. **Website deep dives** (optional, for high-priority leads)
   - Use WebFetch to crawl company websites
   - Extract: AUM, portfolio count, team size, focus areas
   - Score pain point alignment
   - Rate deal potential

### Phase 3: Pattern Extraction

8. **Copy pattern analysis**
   - What works: Common elements in winners
   - What doesn't: Common elements in losers
   - Extract winning formula structure

9. **Title analysis**
   - Group titles by seniority
   - Calculate conversion % by title category
   - Primary vs secondary targeting recommendations

10. **Firm size analysis**
    - Identify sweet spot (where conversions cluster)
    - Define list segmentation buckets
    - Set split point for targeting

### Phase 4: Research Validation

11. **Cross-reference with prior research**
    - Read existing ICP docs, copy research
    - For each hypothesis, classify:

| State | Definition | Action |
|-------|------------|--------|
| EMERGENT | 1-2 tests show signal | Monitor, test further |
| VALIDATED | 3-4 consistent signals | Lean into |
| CANONICAL | 5+ consistent results | Codify as truth |
| CONTRADICTED | Data conflicts with assumption | Investigate |
| INCONCLUSIVE | Not enough data | Needs dedicated test |
| RAW DATA | Never tested | Add to backlog |

12. **Document contradictions**
    - What did we think would work that didn't?
    - What surprised us?
    - What research needs updating?

### Phase 5: Next Cycle Planning

13. **Generate test copy for next cycle**
    - Use winning patterns + new hypotheses
    - Frame: Old way vs new way
    - Style: Founder card or intro-style offer
    - Inform by winning CTA patterns

14. **Create list segmentation**
    - Define buckets by firm size
    - Map copy variants to buckets
    - Set Apollo/LinkedIn filters

15. **Build testing roadmap**

| Day | Actions |
|-----|---------|
| 7 | Pause losers, scale winners, export replies |
| 14 | Launch A/B tests with new variants |
| 30 | Scale winners, launch segment campaigns |

### Phase 6: Deliverables

16. **Write State of Market report**
    - Save to: `Clients/[client]/reports/[YYYY-MM]-[Client]-Campaign-Analysis-State-of-Market.md`

17. **Write Research Validation Matrix**
    - Save to: `Clients/[client]/reports/[YYYY-MM]-Research-Validation-Matrix.md`

18. **Push to GitHub**
    ```bash
    git add reports/
    git commit -m "Add State of Market report and Research Validation Matrix"
    git push
    ```

## Output Structure

### State of Market Report Sections

1. **Executive Summary** - Key metrics, top 3 findings, immediate actions
2. **Campaign Leaderboard** - Variants ranked by contacts/interested
3. **Copy Pattern Analysis** - What works, what doesn't, why
4. **Engaged Lead Profiles** - Company deep dives with pain point alignment
5. **ICP Refinement** - Updated targeting based on conversions
6. **List Segmentation** - Buckets, filters, title targeting
7. **Deliverability Report** - ESP analysis, infrastructure recommendations
8. **Test Copy (Day 14)** - New variants for next cycle
9. **Testing Roadmap** - 7/14/30 day plan
10. **Appendix** - Raw data, methodology

### Research Validation Matrix Sections

1. **Knowledge States** - Definition table
2. **Copy & Messaging Research** - Hypothesis status
3. **ICP Research** - Hypothesis status
4. **Deliverability Research** - Hypothesis status
5. **New Emergent Findings** - Discoveries not in prior research
6. **Documents to Update** - What needs revision
7. **Testing Backlog** - RAW DATA hypotheses

## Key Formulas

```
Contacts/Interested = total_leads_contacted / interested
Reply Rate = unique_replies / total_leads_contacted
Interested Conversion = interested / unique_replies
```

## Classification Thresholds

| Metric | Threshold | Classification |
|--------|-----------|----------------|
| Contacts/Interested | <200 | WINNER |
| Contacts/Interested | 200-300 | PERFORMING |
| Contacts/Interested | >300 | NEEDS OPTIMIZATION |
| Reply Rate (Gmail) | >3% | HEALTHY |
| Reply Rate (Outlook) | <2% | INVESTIGATE |

## List Segmentation Template

| Bucket | Employee Count | Copy Focus | Rationale |
|--------|----------------|------------|-----------|
| Small | 1-19 | Current winners | Conversions cluster here |
| Mid-Large | 20-500 | DD-focus / new tests | Test hypothesis |
| Enterprise | 500+ | Exclude | Needs direct sales |

## Title Targeting Template

| Priority | Titles | Rationale |
|----------|--------|-----------|
| PRIMARY | GP, MP, Founder, MD | Decision makers |
| SECONDARY | Director, Partner | Still influence |
| DEPRIORITIZE | Associate, Analyst | Junior roles |

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Marking findings as CANONICAL after 1 campaign | Use EMERGENT until 5+ consistent tests |
| Ignoring contradictions | Document and investigate |
| Generating test copy without winning pattern reference | Always inform new variants by winners |
| Missing list segmentation | Always define buckets for next cycle |
| Not pushing to GitHub | Reports live in repo, not local only |

## Example Usage

```
User: "Give me a full state of market analysis for AgenticPM"

1. Switch to AgenticPM workspace
2. Pull campaign stats (6,308 contacts, 17 interested)
3. Calculate variant efficiency (Close the Gap: 198 contacts/interested)
4. Analyze interested leads export (76% VC, 47% micro firms)
5. Extract winning patterns (feedback frame + tangible offer)
6. Compare to PE-Firm-Targeting-V1-Master.md research
7. Mark findings as EMERGENT (only 1 campaign)
8. Generate DD-focus test copy for larger firms
9. Create 7/14/30 testing roadmap
10. Write State of Market report
11. Write Research Validation Matrix
12. Push both to gtm-client-agentpm GitHub repo
```

## See Also

- [[.claude/skills/email-campaign/analyze/SKILL]] - Basic campaign analysis
- [[.claude/skills/cold-conversation-reply-analysis/SKILL]] - Reply content analysis
- [[.claude/skills/copywriting/cold-email-v2/SKILL]] - Copy generation
- [[Executions/MCPs/EmailBison]] - EmailBison MCP
