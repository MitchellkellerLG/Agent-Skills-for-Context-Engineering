# Persona Modifiers for Cold Email

Use these modifiers to adapt copy based on who you're targeting. Layer persona-specific language into base copy.

---

## Core Persona Table

| Persona | Typical Titles | What They Care About | Language to Add |
|---------|----------------|----------------------|-----------------|
| **Technical Founder** | Founder, CEO (technical), CTO at seed/Series A | Ship faster, competitive edge, taste preservation | "Your competitors are shipping while you're configuring Kubernetes." |
| **Engineering Leader** | VP Engineering, Head of AI, Director of Engineering | Roadmap, headcount efficiency, build vs buy | "How many more agents could you launch this year with built-in durable execution?" |
| **IC Engineer** | ML Engineer, AI Engineer, Platform Engineer | Tools that work, less infra pain, Python-native | "Built by the team behind Netflix's container scheduler and HashiCorp's Nomad." |
| **Ops/Process Owner** | VP Operations, Head of Innovation, Chief of Staff | Scale transformation, same headcount, automation | "From 100 documents manually reviewed to a million. Same team." |

---

## No DevOps/Infra Team Modifier

Use when targeting teams without dedicated platform engineers:

> "No Kubernetes. No Terraform. No platform team hire. Write Python, deploy, done."

> "You're hiring AI engineers, not DevOps. You shouldn't need DevOps for this."

**When to use:**
- Startups (seed to Series B)
- Teams with < 20 engineers
- Job posts showing AI/ML hires but no DevOps/Platform roles

---

## Team Credibility Modifier

Use when targeting technical buyers who value pedigree:

> "Built by the team behind Netflix's container scheduler, HashiCorp's Nomad, and Meta's ML training platform."

**When to use:**
- Engineering leaders evaluating build vs buy
- IC engineers who respect technical depth
- Enterprise buyers who need to justify vendor choice

---

## Persona-Specific CTAs

| Persona | Recommended CTA |
|---------|-----------------|
| Technical Founder | "Worth a conversation, or not really?" |
| Engineering Leader | "Worth discussing how this affects your roadmap, or not really?" |
| IC Engineer | "Worth testing on your workflows, or not really?" |
| Ops/Process Owner | "Worth discussing if this applies to your operations, or not really?" |

---

## Persona-Specific Pain Points

### Technical Founder
- Time to market (competitors shipping faster)
- Engineering leverage (getting more from small team)
- Technical debt accumulation
- Investor pressure on milestones

### Engineering Leader
- Roadmap eaten by infrastructure
- Headcount efficiency
- Build vs buy decisions
- Team morale (engineers doing plumbing vs product)

### IC Engineer
- Tool frustration (things that don't work)
- Infrastructure pain (Kubernetes, Terraform, YAML)
- Wanting to build product, not plumbing
- Framework complexity

### Ops/Process Owner
- Manual review bottlenecks
- Headcount constraints
- Error rates and quality
- Scale limitations

---

## How to Use

1. **Identify persona** from title, LinkedIn, or job post
2. **Select base copy** from campaign
3. **Layer in persona modifier** where relevant
4. **Adjust CTA** to match persona preference
5. **Add specific pain points** if you have research signals

**Example transformation:**

Base copy:
```
{{first_name}}, what happens when your agent crashes at step 47 of 50?

Most systems: start over from step 1. All that compute, wasted.

Tensorlake has durable execution. Crash at step 47, resume at step 47.

Worth discussing, or not really?
```

With Technical Founder modifier:
```
{{first_name}}, what happens when your agent crashes at step 47 of 50?

Most systems: start over from step 1. All that compute, wasted. Your competitors using managed infrastructure are shipping while you're debugging retry logic.

Tensorlake has durable execution. Crash at step 47, resume at step 47. No Kubernetes. No platform team hire.

Worth a conversation, or not really?
```
