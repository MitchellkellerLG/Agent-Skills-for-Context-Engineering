---
name: email-campaign/analyze
description: Analyzes EmailBison campaign performance, calculates metrics (reply rate, interested rate, contact-to-interested), classifies campaigns (WINNER/PERFORMING/UNDERPERFORMER/TOO EARLY), generates reports. Use when reviewing campaigns, identifying winning copy, or creating client reports.
mcp: EmailBison
---

# Campaign Analysis

Analyze EmailBison campaign performance for a client.

## Prerequisites

- [[Executions/MCPs/EmailBison]] - Workspace access
- Understanding of Performance Classification criteria

## When to Use This Skill

- Reviewing campaign performance for client reports
- Identifying winning copy angles to scale
- Classifying campaigns for weekly reviews
- Calculating metrics (reply rate, interested rate)
- Generating performance reports

## When NOT to Use This Skill

- Setting up new campaigns (use [[.claude/skills/campaign-setup-SKILL]])
- Writing campaign copy (use [[.claude/skills/copywriting/cold-email-v2/SKILL]])
- One-off metric checks without report generation
- Friday batch reviews across all clients (use [[.claude/skills/friday-campaign-review-sop-draft-SKILL]])

## Quick Reference

| Step | Action | Tool |
|------|--------|------|
| 1 | Switch workspace | `rotate_workspace` |
| 2 | List campaigns | `list_campaigns` |
| 3 | Get campaign details | `campaign_details` |
| 4 | Calculate metrics | Manual formulas |
| 5 | Classify performance | WINNER/PERFORMING/UNDERPERFORMER/TOO EARLY |
| 6 | Save report | Write to `Clients/[client]/reports/` |

## Related Skills

- [[.claude/skills/campaign-setup-SKILL]]
- [[.claude/skills/list-building-SKILL]]

## Used By Clients

- [[Clients/teachaid/_master|TeachAid]]
- [[Clients/boundless/_master|Boundless]]
- [[Clients/coherence/_master|Coherence]]

## Inputs

- Client name or workspace
- Date range (optional)
- Specific campaigns (optional, defaults to all active)

## Process

1. **Switch workspace:** `mcp__bison_mcp__emailbison_rotate_workspace`
   - See: [[Executions/MCPs/Bison_MCP_tools#mcp__bison_mcp__emailbison_rotate_workspace|rotate_workspace documentation]]
   - Required first step - sets context for all subsequent operations
   - Use workspace_name for clarity: `workspace_name: "Boundless"`

2. **Get campaigns:** `mcp__bison_mcp__emailbison_list_campaigns`
   - See: [[Executions/MCPs/Bison_MCP_tools#mcp__bison_mcp__emailbison_list_campaigns|list_campaigns documentation]]
   - **Token optimization:** Use `format: "concise"` to minimize tokens (~70% reduction)
   - Filter by status if needed: `status: "active"` for live campaigns only

3. **For each campaign:**

   **Get details:** `mcp__bison_mcp__emailbison_campaign_details`
   - See: [[Executions/MCPs/Bison_MCP_tools#mcp__bison_mcp__emailbison_campaign_details|campaign_details documentation]]
   - Extract metrics object for classification
   - Use `format: "standard"` for performance analysis

   **Get copy:** `mcp__bison_mcp__emailbison_view_campaign_sequence_steps`
   - See: [[Executions/MCPs/Bison_MCP_tools#mcp__bison_mcp__emailbison_view_campaign_sequence_steps|view_sequence_steps documentation]]
   - **Token optimization:** Only retrieve for WINNER/PERFORMING campaigns
   - Use `include_variants: false` unless variants are needed for analysis
   - Skip for UNDERPERFORMER and TOO EARLY to save ~80% tokens

4. **Calculate metrics** (formulas in campaign_details response):
   ```
   Reply Rate = unique_replies / total_leads_contacted
   Interested Rate = interested / unique_replies
   Contact-to-Interested = interested / total_leads_contacted
   ```

5. **Classify performance:**
   - ASTRONOMICAL: 30%+ interested rate (≥ 0.30)
   - WINNER: 20-30% (0.20-0.30)
   - PERFORMING: 6-20% (0.06-0.20)
   - UNDERPERFORMER: <6% (< 0.06)
   - TOO EARLY: <500 contacts

   See: [[Executions/MCPs/Bison_MCP_tools#performance-classification-guidance|Performance Classification Guide]]

6. **Write recommendations**

7. **Save report** to `Clients/[client]/reports/[Campaign]_Analysis_[Date].md`

## Output

- Report in `Clients/[client]/reports/[Campaign]_Analysis_[Date].md`
- Git commit with descriptive message

## Deliverability Check

Reply rate <2% = investigate inbox placement

## Edge Cases

- New campaign: Note "too early to tell" with current stats
- No replies: Check if campaign is actually sending

## Examples

### Example 1: Weekly Client Report
```
User: "Analyze TeachAid campaigns and generate a report"
→ Switch to TeachAid workspace
→ List all active campaigns
→ Calculate metrics for each
→ Classify: NZ Principals (WINNER 24%), Ontario (PERFORMING 12%), UK (TOO EARLY)
→ Save to Clients/teachaid/reports/TeachAid_Campaign_Report_Dec27_2025.md
```

### Example 2: Identifying Winners to Scale
```
User: "Which Boundless campaigns should we scale?"
→ Pull all campaigns with 500+ contacts
→ Filter to 20%+ interested rate
→ List copy from winning sequences
→ Recommend scaling those with <500 leads remaining
```

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Analyzing campaigns with <500 contacts | Mark as "TOO EARLY" - not enough data |
| Missing workspace switch | Always `rotate_workspace` first |
| Pulling copy for all campaigns | Only pull copy for WINNER/PERFORMING (saves tokens) |
| Using wrong interested rate formula | interested / unique_replies (not total contacts) |

## Learnings

<!-- Add discoveries here as you work -->

## See Also

- [[Executions/MCPs/EmailBison]] - EmailBison MCP Server
- [[.claude/skills/campaign-setup-SKILL]] - Campaign Setup

[Executions/MCPs/EmailBison]: ../Executions/MCPs/EmailBison.md "EmailBison MCP Server"
[.claude/skills/campaign-setup-SKILL]: campaign-setup-SKILL.md "Campaign Setup"
[.claude/skills/list-building-SKILL]: list-building-SKILL.md "List Building"
[Clients/teachaid/_master|TeachAid]: ../Clients/teachaid/_master.md "TeachAid - Client Master Index"
[Clients/boundless/_master|Boundless]: ../Clients/boundless/_master.md "Boundless - Client Master Index"
[Clients/coherence/_master|Coherence]: ../Clients/coherence/_master.md "Coherence - Client Master Index"
[Executions/MCPs/Bison_MCP_tools#mcp__bison_mcp__emailbison_rotate_workspace|rotate_workspace documentation]: ../Executions/MCPs/Bison_MCP_tools.md "Bison MCP Tools Reference"
[Executions/MCPs/Bison_MCP_tools#mcp__bison_mcp__emailbison_list_campaigns|list_campaigns documentation]: ../Executions/MCPs/Bison_MCP_tools.md "Bison MCP Tools Reference"
[Executions/MCPs/Bison_MCP_tools#mcp__bison_mcp__emailbison_campaign_details|campaign_details documentation]: ../Executions/MCPs/Bison_MCP_tools.md "Bison MCP Tools Reference"
[Executions/MCPs/Bison_MCP_tools#mcp__bison_mcp__emailbison_view_campaign_sequence_steps|view_sequence_steps documentation]: ../Executions/MCPs/Bison_MCP_tools.md "Bison MCP Tools Reference"
[Executions/MCPs/Bison_MCP_tools#performance-classification-guidance|Performance Classification Guide]: ../Executions/MCPs/Bison_MCP_tools.md "Bison MCP Tools Reference"