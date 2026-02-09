---
name: spintax-syntax
description: Complete guide to spintax syntax for cold email copy variations.
tools: []
---

# Spintax Syntax Guide

## Basic Syntax

Spintax uses curly braces with pipe-separated options:

```
{option1|option2|option3}
```

When processed, one option is randomly selected.

## Examples

### Greetings

```
{Hi|Hey|Hello} {FIRST_NAME}
```

Produces: "Hi John", "Hey John", or "Hello John"

### Value Props

```
We {help|support|work with} companies to {achieve|reach|hit} their goals.
```

### CTAs

```
{Would you be open to|Are you interested in|Want to} {discussing|exploring|chatting about} this?
```

```
{Let me know|Reply|Drop me a note} if {interested|you'd like to learn more|this sounds useful}.
```

## Best Practices

### Hybrid Approach (Recommended)

Use **word-level** spintax for safe, independent words:

- Verbs: `{take|repurpose|leverage|use}`
- Adjectives: `{quick|brief|short}`
- Simple adverbs: `{already|currently}`
- Prepositions: `{within|in}`

Use **phrase-level** spintax for complex structures:

- Bound phrases: `{your best content|what's working}`
- CTAs: `{give me feedback on|be open to reviewing}`
- Where word order matters

**Why hybrid?** Word-level = more variations. Phrase-level = grammar safety.

### DO

- **Check `data/learned-spam-words.json` BEFORE writing spintax options**
- Use hybrid approach: word-level for simple swaps, phrase-level for complex structures
- Target 10M+ variations with hybrid (vs 4M with phrase-only)
- Run spam check and grammar check on all variations
- Keep offer flow and CTA type consistent across all options

### DON'T

- **NEVER nest spintax** - `{Hi {there|friend}}` is NOT allowed
- **NEVER use known spam words** - check the learned database first
- Mix formal and casual in same block
- Create options with vastly different meanings
- Use spintax for critical information
- Mix singular/plural subjects (causes verb agreement issues)
- Mix singular/plural nouns with pronouns ("posts... it")

## Pre-Check: Spam Word Library

**BEFORE writing spintax options**, check `data/learned-spam-words.json` for known spam triggers.

### High-Hit Spam Words to Avoid

| Word/Phrase | Hit Count | Use Instead |
| ----------- | --------- | ----------- |
| "opportunity" | 50 | chance, option, possibility |
| "take a look at" | 50 | give me feedback on, review, look at |
| "for you" | 50 | (remove or rephrase) |
| "act now" | 29 | when you're ready, if interested |
| "exclusive" | 28 | select, curated, tailored |
| "double your" | 27 | increase your, grow your |
| "sign up" | 26 | get started, join, begin |
| "guarantee" | 20 | back, assure, confirm |

### Self-Annealing System

The spam word library grows over time:

1. **Check local first** - Scan `learned-spam-words.json` before writing
2. **Avoid known triggers** - Don't use words with high hit counts
3. **Run spam check** - API catches new words
4. **Library updates** - New discoveries auto-added to JSON
5. **Future writes** - You'll avoid those words next time

This makes the system smarter with each campaign.

---

## Common Patterns

### Opening Lines

```
{Hi|Hey|Hello} {FIRST_NAME}

{Saw|Noticed|Came across} {your LinkedIn post about|your recent article on|that you're working on} {HOOK_TOPIC}.
```

### Social Proof

```
We {work with|support|help} {over 70|70+|more than 70} companies {like yours|in your space|targeting similar personas}.
```

### Soft CTAs

```
{Would you be open to|Are you interested in|Open to} {reviewing|seeing|looking at} {a quick|a brief|an} {audit|analysis|breakdown}?
```

```
{Want to|Should we|Care to} {discuss|chat about|explore} this?
```

### P.S. Lines

```
p.s. {I'm preparing|Putting together|Assembling} a {full|detailed|complete} {audit|report|analysis}. {Reply to get it.|Just reply if you want it.|Shoot me a reply and I'll send it over.}
```

## EmailBison Compatibility

EmailBison uses standard spintax syntax. Special variables:

| Variable | Description |
|----------|-------------|
| `{FIRST_NAME}` | Lead's first name |
| `{LAST_NAME}` | Lead's last name |
| `{COMPANY}` | Company name |
| `{HOOK}` | Custom personalization field |
| `{SENDER_EMAIL_SIGNATURE}` | Sender signature |

**Note:** Don't put EmailBison variables inside spintax blocks.

```
# Good
{Hi|Hey} {FIRST_NAME}

# Bad - FIRST_NAME won't render
{Hi FIRST_NAME|Hey FIRST_NAME}
```

## Testing Spintax

Use the spam check script to expand and test:

```bash
python scripts/emailguard_spam_check.py --expand-spintax "Your {spintax|copy} here"
```

This will check all possible combinations for spam triggers.

## Variation Counts

| Spintax Blocks | Options Each | Total Variations |
|----------------|--------------|------------------|
| 1 | 3 | 3 |
| 2 | 3 | 9 |
| 3 | 3 | 27 |
| 4 | 3 | 81 |
| 5 | 3 | 243 |

**Tip:** Keep total variations under 50 for manageable testing.
