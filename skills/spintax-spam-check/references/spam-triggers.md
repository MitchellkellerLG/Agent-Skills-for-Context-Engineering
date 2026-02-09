---
name: spam-triggers
description: Common spam trigger words and safe replacements for cold email copy.
tools: []
---

# Spam Trigger Words & Replacements

## High Severity (Avoid Completely)

These words/phrases almost always trigger spam filters:

| Spam Word | Safe Replacements |
|-----------|-------------------|
| free | complimentary, no-cost, included, at no charge |
| guarantee | back, assure, confirm, commit to |
| guaranteed | backed, assured, confirmed, committed |
| act now | when you're ready, if interested, at your convenience |
| limited time | current, available now, while available |
| urgent | timely, time-sensitive, current |
| click here | learn more, see details, explore, find out more |
| congratulations | great news, exciting update, good news |
| winner | successful, selected, chosen |
| cash | funds, payment, compensation |
| earn money | generate income, create revenue, build earnings |
| make money | generate income, build revenue |
| double your | increase your, grow your, expand your |
| million dollars | significant returns, substantial growth |

## Medium Severity (Use Carefully)

These can trigger filters depending on context:

| Spam Word | Safe Replacements |
|-----------|-------------------|
| buy | get, acquire, invest in, pick up |
| cheap | affordable, cost-effective, budget-friendly |
| deal | opportunity, option, arrangement |
| discount | savings, reduced rate, special rate |
| exclusive | select, curated, tailored, specific |
| instant | quick, fast, prompt, immediate |
| limited | select, curated, specific, focused |
| offer | opportunity, option, possibility |
| order | request, get started, proceed |
| price | rate, investment, cost |
| profit | benefit, gain, return, growth |
| sale | opportunity, availability, option |
| save | keep, retain, preserve, reduce |
| special | unique, tailored, curated, custom |

## Low Severity (Context Dependent)

These are flagged in some contexts:

| Spam Word | Safe Replacements |
|-----------|-------------------|
| amazing | impressive, notable, significant |
| best | top, leading, strong |
| bonus | additional, extra, included |
| compare | evaluate, assess, review |
| incredible | impressive, significant, notable |
| new | recent, latest, updated |
| now | today, currently, at this time |
| opportunity | possibility, option, opening |
| success | results, outcomes, achievements |

## Spam Phrases

Full phrases that trigger filters:

| Spam Phrase | Safe Alternative |
|-------------|------------------|
| act now | when you're ready |
| apply now | get started |
| buy now | learn more |
| call now | reach out |
| click below | see below |
| click here | learn more |
| don't delete | - (remove entirely) |
| don't miss | consider |
| for free | included, complimentary |
| get it now | learn more |
| hurry | - (remove urgency) |
| limited offer | current opportunity |
| no obligation | flexible terms |
| no strings attached | straightforward |
| once in a lifetime | rare, unique |
| order now | get started |
| risk-free | low-risk, safe |
| sign up | get started, join |
| subscribe | join, follow |
| take action | get started |
| this won't last | available now |
| what are you waiting for | - (remove entirely) |

## Subject Line Red Flags

Especially dangerous in subject lines:

- ALL CAPS
- Excessive punctuation (!!!, ???)
- Dollar signs ($$$)
- Percentage symbols (%)
- "Re:" or "Fwd:" when not a reply
- Emojis (in B2B cold email)
- "Free" or "Urgent"

## Safe Patterns

### Instead of urgency:

```
# Bad
Act now before this expires!

# Good
Let me know if you'd like to explore this.
```

### Instead of hype:

```
# Bad
Amazing opportunity to double your revenue!

# Good
Wanted to share how we've helped similar companies grow.
```

### Instead of hard sells:

```
# Bad
Buy now and save 50%!

# Good
Would you be open to learning more?
```

## Deliverability Tips

1. **Keep it conversational** - Write like a human, not a marketer
2. **Avoid formatting** - Plain text > HTML for cold email
3. **One CTA per email** - Don't overwhelm
4. **Short sentences** - Long sentences look spammy
5. **No attachments** - Links only if necessary
6. **Personalization** - Generic = spam, personalized = legitimate
7. **Reasonable length** - 50-150 words ideal for cold email

## Testing

Always run copy through the spam check script before sending:

```bash
python scripts/emailguard_spam_check.py "Your copy here"
```
