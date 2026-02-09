---
name: copy-spintax-spam-check-native
description: Processes cold email copy with spintax, checks for spam triggers and grammar issues. Use when creating email variants, applying spintax, validating copy for deliverability, checking spam scores, or verifying grammar. REQUIRES control message anchoring - spintax must be variations OF the control, not rewrites.
tools:
  - scripts/emailguard_spam_check.py
  - data/learned-spam-words.json
  - references/spintax-syntax.md
  - references/spam-triggers.md
  - references/high-volume-spintax-examples.md
---

# Copy Spintax Spam Check (Native Grammar)

Full spintax + spam + grammar checking with **control message anchoring**.

**See also:** `Specs/Spintax_Grammar_Checker/SPEC.md` for automated checker architecture.

---

## Critical Concept: Control Message Anchoring

**Every spintax MUST have a control message** - the original plaintext copy that spintax is derived from.

**Why:** Prevents semantic drift. Variations must be OF the control, not rewrites.

```
CONTROL (user's original):
{FIRST_NAME} have to imagine you're growing after my analysis of your current marketing.

ANCHORED SPINTAX (correct):
{FIRST_NAME} - {have to imagine|gotta figure} you're growing after my {analysis|review} of your current {presence|traction}.

NOT ANCHORED (wrong - this is a rewrite):
{FIRST_NAME} - {gotta figure|have to think} you're {building|expanding} after my {look at|review of} your {online presence|digital footprint}.
```

**Anchoring rules:**
- Sentence structure MUST match control
- Only replace spam-flagged words, not rewrite
- Preposition patterns must be consistent (`analysis of` stays `of`, not mixed with `look at`)
- Key phrases/idioms preserved
- Less spintax that maintains quality > more spintax that drifts

---

## Workflow

### Step 1: Establish Control Message

Get the user's original plaintext copy. This is your **control message**.

```text
CONTROL:
{FIRST_NAME} have to imagine you're growing after my analysis of your current marketing.
We help 100's of small local businesses like yours add fuel to that fire with cheap capital.
Worth seeing your options to bet on yourself?
```

**Do NOT proceed without a control message.**

### Step 2: Run Spam Check on Control (Single Check)

Check the PLAINTEXT control for spam triggers - **ONE API call only**:

```bash
python scripts/emailguard_spam_check.py "Your plaintext control copy here"
```

**Pass criteria:** Maximum 1 spam word (`spam_score` 0-1)

**IMPORTANT:** Do NOT use `--expand-spintax` flag during iterative fixing. That expands to 50+ variations and wastes API calls. Check plaintext → fix → recheck plaintext.

### Step 3: Loop Until Spam Clean

If `spam_score > 1`:
1. Replace flagged words using suggestions from output
2. Check `references/spam-triggers.md` for alternatives
3. Re-run spam check on updated plaintext
4. **Repeat until spam_score ≤ 1**

Each API call learns new spam words -> stored in `learned-spam-words.json`.

### Step 4: Create Spintax Anchored to Control

Now create spintax that is anchored to your spam-clean control:

**Control (spam-clean):**
```text
{FIRST_NAME} have to imagine you're growing after my analysis of your current presence.
We help 100's of small local businesses like yours add fuel to that fire with low-cost capital.
Worth seeing your options to bet on yourself?
```

**Anchored spintax:**
```text
{FIRST_NAME} - {have to imagine|gotta figure|have to think} you're growing after my {analysis|review|assessment} of your current {presence|traction|momentum}.

We help {100's|hundreds|100s} of small local businesses like yours {add fuel to that fire|pour gas on that fire|fan those flames} with {low-cost|quick|accessible} capital. {100k+|$100k+|Six figures} in your account in {days|just days|a matter of days}.

{Worth seeing|Want to see|Open to seeing} your options to bet on yourself?
```

**Anchoring checklist:**

- [ ] Sentence structure matches control
- [ ] Preposition patterns consistent (all "of" or all "at", not mixed)
- [ ] Only spam words replaced, rest preserved
- [ ] Key phrases/idioms maintained
- [ ] No "building" vs "growing" false synonyms

### Step 5: Run Grammar Check with Smart Sampling

After creating anchored spintax, check grammar using **smart sampling** (50 random permutations):

**Subagent prompt:**

```
=== CONTROL MESSAGE ===
[PASTE ORIGINAL CONTROL HERE]

=== SPINTAX VARIATIONS (50 random samples) ===
[PASTE 50 EXPANDED VARIATIONS HERE]

=== CHECK EACH VARIATION AGAINST CONTROL ===

1. STRUCTURE PRESERVED? - Does sentence structure match control?
2. OFFER FLOW PRESERVED? - Same pitch flow as control?
3. CTA TYPE PRESERVED? - Same type of ask as control?
4. BROKEN ENGLISH? - Subject-verb agreement, word order issues
5. VERB + INFINITIVE COMPATIBILITY?
   - "help" works WITHOUT "to": "We help you grow" ✓
   - "support/work with/partner with" REQUIRE "to": "We support you to grow" ✓
   - BROKEN: "We support you grow" ✗
6. PREPOSITION CONSISTENCY? - Same preposition pattern as control?
   - Control has "analysis of" → all options must use "of"
   - NOT mixed with "look at"

=== DO NOT FLAG ===
- True synonym swaps: ChatGPT -> AI -> LLMs (same meaning)
- Number format: 100's -> hundreds -> 100s
- Timeline wording: "in days" -> "within days"

=== FLAG IF ===
- Structure diverged from control
- False synonyms: "building" ≠ "growing"
- Mixed preposition patterns: "analysis of" mixed with "look at"
- Broken grammar in any permutation
- Meaning drift from control

For each variation: [PASS] or [FAIL: specific reason]
```

**How to spawn:**
Use Task tool with `subagent_type: "general-purpose"` and the prompt above.

**Pass criteria:** All 50 sampled variations show `[PASS]`

### Step 6: Loop Until Grammar Clean

If any variation fails:

1. Identify the problematic spintax block
2. Fix the issue (remove bad option OR restructure block)
3. Re-run grammar check with fresh 50 samples
4. **Repeat until all variations pass**

### Step 7: Final Output

After both checks pass, restore custom variables:

```text
{Hi|Hey} {FIRST_NAME}, {HOOK} - want to discuss?
{SENDER_EMAIL_SIGNATURE}
```

Copy is now ready for EmailBison upload.

---

## Self-Annealing System

This skill gets smarter over time:

1. **First check:** Scans local database (`learned-spam-words.json`)
2. **API check:** Calls EmailGuard for unknown content
3. **Learn:** New spam words discovered -> added to local database
4. **Future checks:** Local database catches more -> fewer API calls

The `learned-spam-words.json` file tracks:
- Spam words and phrases
- Safe replacement suggestions
- Severity levels
- Hit counts (how often each word is encountered)
- Discovery date

---

## When to Use This Skill

- Creating new cold email copy with spintax variations
- Validating existing copy for spam triggers before sending
- Checking copy deliverability before uploading to EmailBison
- Generating multiple email variants from a single template
- When you don't have OpenRouter API access but still need grammar checking

## When NOT to Use This Skill

- Writing the initial copy from scratch (use copywriting skills first)
- Warm email replies (spam filters less strict)
- Internal communications
- Copy already validated and performing well

---

## Files in This Skill

| File | Purpose |
| ---- | ------- |
| **SKILL.md** | Main workflow (this file) |
| `scripts/emailguard_spam_check.py` | Spam checking with self-annealing |
| `data/learned-spam-words.json` | Self-annealing spam word database |
| `references/spintax-syntax.md` | Spintax syntax guide |
| `references/spam-triggers.md` | Common spam words + replacements |
| `references/high-volume-spintax-examples.md` | Approved 50k+ variation examples |

---

## Tool Integration

### EmailGuard API (Spam Check)

- Endpoint: `POST https://app.emailguard.io/api/v1/content-spam-check`
- Auth: Bearer token from `.env` (`EMAILGUARD_API_KEY`)
- See API docs: https://app.emailguard.io/api/reference

### Spam Check Script

```bash
# Basic check
python scripts/emailguard_spam_check.py "Your email copy"

# Check from file
python scripts/emailguard_spam_check.py --file copy.txt

# Expand spintax and check all variations
python scripts/emailguard_spam_check.py --expand-spintax "{Hi|Hey} there"

# Local check only (no API)
python scripts/emailguard_spam_check.py --local-only "Quick check"

# JSON output
python scripts/emailguard_spam_check.py --json "Copy here"
```

### Native Grammar Check (Claude Code Subagent)

Instead of calling OpenRouter API, grammar checking runs natively via Claude Code Task tool:

```
Task tool:
  subagent_type: "general-purpose"
  prompt: [grammar check prompt with expanded variations]
```

**Advantages over API:**
- No additional API key required
- Same quality as main Claude instance
- Full context awareness
- No rate limits or costs

---

## Common Mistakes

| Mistake | Why Bad | Fix |
| ------- | ------- | --- |
| **No control message** | Spintax drifts from original intent | Always establish control FIRST |
| **Rewriting instead of varying** | Changes meaning, structure, tone | Only vary within control structure |
| **False synonyms** | "building" ≠ "growing", different meanings | Use TRUE synonyms only |
| **Mixed preposition patterns** | "analysis of" + "look at" breaks grammar | Keep preposition consistent with control |
| **Running 50+ spam checks** | `--expand-spintax` wastes API calls | Check plaintext → fix → recheck |
| Checking with custom variables | `{FIRST_NAME}` etc. aren't real content | Strip variables, use placeholder text |
| Stopping at first check | Copy may still have spam words | Loop until `spam_score` ≤ 1 |
| Ignoring severity levels | High severity words tank deliverability | Prioritize replacing high severity |
| Checking HTML copy | Script expects plain text | Strip HTML before checking |
| Using nested spintax | Not supported, breaks expansion | Use flat spintax only |
| Skipping grammar check | Some variations may have errors | Run smart sampling after spam |
| Mixing verb + infinitive patterns | "We support you grow" is broken | Use verbs with same infinitive pattern, or add "to" for all |
| Mixing singular/plural subjects | "AI tools starts" broken grammar | Use all singular OR all plural subjects |
| Pronoun mismatch | "your posts... distribute it" | Keep noun number consistent with pronouns |

---

## Examples

### Example 1: Full Workflow with Control Anchoring

**Step 1 - Establish Control:**

```text
CONTROL:
{FIRST_NAME} have to imagine you're growing after my analysis of your current marketing.
We help 100's of small local businesses like yours add fuel to that fire with cheap capital.
Worth seeing your options to bet on yourself?
```

**Step 2 - Spam Check Control (single check):**

```bash
python scripts/emailguard_spam_check.py "FIRST_NAME have to imagine..."
```

Result: `[FAIL] spam_score: 2` - flagged: "marketing", "cheap"

**Step 3 - Fix Spam Words:**

Replace "marketing" → "presence", "cheap" → "low-cost"

Re-run: `[PASS] spam_score: 0`

**Step 4 - Create Anchored Spintax:**

```text
{FIRST_NAME} - {have to imagine|gotta figure|have to think} you're growing after my {analysis|review|assessment} of your current {presence|traction|momentum}.

We help {100's|hundreds|100s} of small local businesses like yours {add fuel to that fire|pour gas on that fire} with {low-cost|quick|accessible} capital.

{Worth seeing|Want to see|Open to seeing} your options to bet on yourself?
```

**Step 5 - Grammar Check (50 samples):**

Spawn Task with control + 50 random variations.

Result:

```
Variation 1: [PASS]
Variation 2: [PASS]
...
Variation 47: [FAIL: "gotta figure you're building" - false synonym]
```

**Step 6 - Fix:**

Remove "building" - control says "growing", keep only "growing".

Re-run with fresh 50 samples -> All `[PASS]`

**Final Output:** Ready for EmailBison.

---

**Created:** 2025-12-31
**Last Updated:** 2026-01-16
