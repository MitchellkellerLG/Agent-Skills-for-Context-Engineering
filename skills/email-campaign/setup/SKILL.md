---
name: email-campaign/setup
description: Create and launch email campaigns in EmailBison. Use when setting up new campaigns, configuring sequences, or launching outbound.
mcp: EmailBison
---

# Campaign Setup

Launch a campaign in EmailBison.

**Tool Reference:** [[Executions/MCPs/Bison_MCP_tools]]

## Prerequisites

- [[Executions/MCPs/EmailBison]] - Workspace access
- [[.claude/skills/list-building-SKILL]] - Enriched leads ready
- Approved copy from [[.claude/skills/copywriting/cold-email-v2/SKILL]]

## Related Skills

- [[.claude/skills/campaign-analysis-SKILL]]
- [[.claude/skills/list-sourcing-SKILL]]

## Used By Clients

- [[Clients/teachaid/_master|TeachAid]]
- [[Clients/boundless/_master|Boundless]]
- [[Clients/diversys/_master|Diversys]]

## Inputs

- Client workspace name or ID
- Enriched lead list
- Approved copy sequence
- Schedule preferences

## Process

1. `rotate_workspace` - Set client context (workspace_name or workspace_id)
2. `create_campaign` - Create container (name required)
3. `create_sequence_steps` - Build email sequence (campaign_id, title, sequence_steps)
4. `update_campaign_settings` - Configure behavior (max_emails_per_day, open_tracking, can_unsubscribe)
5. `create_campaign_schedule` - Set send times (days, start_time, end_time, timezone)
6. Upload leads (manual or bulk_create_leads)
7. `resume_campaign` - Launch (⚠️ confirm with user first)

**Quick Setup:** Use `create_campaign_workflow` to combine steps 2-5 with dryRun validation

## Output

- Live campaign in EmailBison
- Campaign ID logged in `Clients/[client]/campaigns/`

## Safety Rules

**NEVER use:**
- Delete/remove/archive operations
- Force operations

**ALWAYS:**
- Pause instead of delete
- Duplicate instead of overwrite
- Confirm with user before launching

## Edge Cases

- Workspace not found: List workspaces first
- Schedule conflict: Check existing campaigns

## Learnings

<!-- Add discoveries here as you work -->

## See Also

- [[Executions/MCPs/EmailBison]] - EmailBison MCP Server
- [[.claude/skills/campaign-analysis-SKILL]] - Campaign Analysis

[Executions/MCPs/EmailBison]: ../Executions/MCPs/EmailBison.md "EmailBison MCP Server"
[.claude/skills/list-building-SKILL]: list-building-SKILL.md "List Building"
[.claude/skills/copywriting/cold-email-v2/SKILL]: copywriting/cold-email-v2/SKILL.md "Cold Email Personalization (GEX Style) - Complete System"
[.claude/skills/campaign-analysis-SKILL]: campaign-analysis-SKILL.md "Campaign Analysis"
[Clients/teachaid/_master|TeachAid]: ../Clients/teachaid/_master.md "TeachAid - Client Master Index"
[Clients/boundless/_master|Boundless]: ../Clients/boundless/_master.md "Boundless - Client Master Index"
[Clients/diversys/_master|Diversys]: ../Clients/diversys/_master.md "Diversys - Client Master Index"