# Agent Skills for Context Engineering

A comprehensive, open collection of Agent Skills focused on context engineering principles for building production-grade AI agent systems. These skills teach the art and science of curating context to maximize agent effectiveness across any agent platform.

## What is Context Engineering?

Context engineering is the discipline of managing the language model's context window. Unlike prompt engineering, which focuses on crafting effective instructions, context engineering addresses the holistic curation of all information that enters the model's limited attention budget: system prompts, tool definitions, retrieved documents, message history, and tool outputs.

The fundamental challenge is that context windows are constrained not by raw token capacity but by attention mechanics. As context length increases, models exhibit predictable degradation patterns: the "lost-in-the-middle" phenomenon, U-shaped attention curves, and attention scarcity. Effective context engineering means finding the smallest possible set of high-signal tokens that maximize the likelihood of desired outcomes.

## Skills Overview

### Foundational Skills

These skills establish the foundational understanding required for all subsequent context engineering work.

| Skill | Description |
|-------|-------------|
| [context-fundamentals](skills/context-fundamentals/) | Understand what context is, why it matters, and the anatomy of context in agent systems |
| [context-degradation](skills/context-degradation/) | Recognize patterns of context failure: lost-in-middle, poisoning, distraction, and clash |

### Architectural Skills

These skills cover the patterns and structures for building effective agent systems.

| Skill | Description |
|-------|-------------|
| [multi-agent-patterns](skills/multi-agent-patterns/) | Master orchestrator, peer-to-peer, and hierarchical multi-agent architectures |
| [memory-systems](skills/memory-systems/) | Design short-term, long-term, and graph-based memory architectures |
| [tool-design](skills/tool-design/) | Build tools that agents can use effectively |

### Operational Skills

These skills address the ongoing operation and optimization of agent systems.

| Skill | Description |
|-------|-------------|
| [context-optimization](skills/context-optimization/) | Apply compaction, masking, and caching strategies |
| [evaluation](skills/evaluation/) | Build evaluation frameworks for agent systems |

### Cold Email & Copywriting Skills

Skills for writing, testing, and optimizing cold outbound email campaigns.

| Skill | Description |
|-------|-------------|
| [cold-email-v2](skills/cold-email-v2/) | Complete cold email system: research-driven personalization, "poke the bear" openers, variable schemas, follow-up sequences, QA checklist, and scoring rubric |
| [spintax-spam-check](skills/spintax-spam-check/) | Spintax processing with control message anchoring, spam trigger detection via EmailGuard API, self-annealing spam word database, and native grammar checking |

### Campaign Management Skills

Skills for managing email campaigns in EmailBison — setup, analysis, and cross-client intelligence.

| Skill | Description |
|-------|-------------|
| [email-campaign/setup](skills/email-campaign/setup/) | Create and launch campaigns in EmailBison: workspace switching, sequence creation, schedule configuration, and safety rules |
| [email-campaign/analyze](skills/email-campaign/analyze/) | Analyze campaign performance: metric calculation, classification (WINNER/PERFORMING/UNDERPERFORMER/TOO EARLY), and report generation |
| [campaign-state-of-market](skills/campaign-state-of-market/) | Deep-dive campaign analysis with ICP refinement, copy pattern extraction, research validation matrix, and 7/14/30-day testing roadmaps |
| [cold-conversation-reply-analysis](skills/cold-conversation-reply-analysis/) | Extract GTM intelligence from reply exports: pain points, objection patterns, persona analysis, copy effectiveness, and ICP refinement |
| [cross-client-ground-truth](skills/cross-client-ground-truth/) | Cross-client pattern extraction ranked by C/I (Contacts per Interested Reply) — the metric that tells the truth about what works |

## Design Philosophy

### Progressive Disclosure

Each skill is structured for efficient context use. At startup, agents load only skill names and descriptions. Full content loads only when a skill is activated for relevant tasks.

### Platform Agnosticism

These skills focus on transferable principles rather than vendor-specific implementations. The patterns work across Claude Code, Cursor, and any agent platform that supports skills or allows custom instructions.

### Conceptual Foundation with Practical Examples

Scripts and examples demonstrate concepts using Python pseudocode that works across environments without requiring specific dependency installations.

## Usage

### For Claude Code

Install skills by referencing this repository or by copying skill folders into your configured skills directory. When working on context engineering tasks, activate relevant skills to load their instructions.

### For Cursor

Copy skill content into `.cursorrules` or create project-specific rules files. The skills provide the context and guidelines that Cursor's agent needs for effective context engineering.

### For Custom Implementations

Extract the principles and patterns from any skill and implement them in your agent framework. The skills are deliberately platform-agnostic.

## Structure

Each skill follows the Agent Skills specification:

```
skill-name/
├── SKILL.md              # Required: instructions + metadata
├── scripts/              # Optional: executable code demonstrating concepts
└── references/           # Optional: additional documentation and resources
```

See the [template](template/) folder for the canonical skill structure.

## Contributing

This repository follows the Agent Skills open development model. Contributions are welcome from the broader ecosystem. When contributing:

1. Follow the skill template structure
2. Provide clear, actionable instructions
3. Include working examples where appropriate
4. Document trade-offs and potential issues
5. Keep SKILL.md under 500 lines for optimal performance

## License

MIT License - see LICENSE file for details.

## References

The principles in these skills are derived from research and production experience at leading AI labs and framework developers. Each skill includes references to the underlying research and case studies that inform its recommendations.
