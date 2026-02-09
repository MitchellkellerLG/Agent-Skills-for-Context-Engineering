# Vertical Adaptation Guide

When the user provides specific industry verticals, create separate adapted outputs for each. This guide shows how to adapt base copy for different industries.

---

## Core Principle

**If verticals are provided, always create separate versions.** Don't just use one generic version. Industry-specific copy outperforms generic copy by 2-3x.

---

## Common Verticals

| Vertical | Key Pain Points | Industry-Specific Language |
|----------|-----------------|---------------------------|
| **Insurance** | Claims leakage, ACORD forms, strikethroughs meaning "Denied" | claims, adjusters, ACORD, coverage, strikethrough, denied charges |
| **Finance/Lending** | Table extraction, footnotes, risk models, 10-Ks | filings, risk profiles, table geometry, footnotes, analysts |
| **Legal** | Contract review, redlines, due diligence, crossed-out clauses | contracts, clauses, redlines, due diligence, associates, deal docs |
| **Healthcare** | HIPAA, audit trails, clinical documents, citations | HIPAA, audit trail, clinical, patient records, compliance, VPC |
| **Identity/KYC** | Field drift, DOB vs Issue Date, verification accuracy | passport, ID scan, DOB, field coordinates, verification, compliance |
| **RAG/AI Apps** | Document ingestion, chunking, embeddings, pipeline failures | RAG pipeline, chunking, embeddings, vector store, LangChain |

---

## Adaptation Template

For each vertical, adapt these elements:

### 1. Pain Point
Replace generic pain with industry-specific pain.

**Generic:** "Your parser strips important information"
**Insurance:** "Your parser strips the strikethrough that says 'Denied'"
**Finance:** "Your parser orphans the footnote that says '*Pending Litigation'"
**Legal:** "Your parser strips the redline showing the clause was rejected"

### 2. Document Types
Replace generic "documents" with specific document types.

**Generic:** "documents", "files", "PDFs"
**Insurance:** "ACORD forms", "claims", "medical bills"
**Finance:** "10-Ks", "financial statements", "filings"
**Legal:** "contracts", "agreements", "due diligence packages"
**Healthcare:** "patient records", "clinical documents"

### 3. Roles
Replace generic roles with industry-specific roles.

**Generic:** "your team", "reviewers"
**Insurance:** "your adjusters", "claims team"
**Finance:** "your analysts", "risk team"
**Legal:** "your lawyers", "associates"
**Healthcare:** "your clinical team"

### 4. Outcomes
Replace generic outcomes with industry-specific outcomes.

**Generic:** "errors", "mistakes"
**Insurance:** "claims leakage", "approved charges that should be denied"
**Finance:** "missed risk signals", "bad data in risk models"
**Legal:** "agreeing to rejected terms", "missing redlines"
**Healthcare:** "audit failures", "can't cite sources"

### 5. Scale Numbers
Use industry-appropriate scale.

**Insurance:** "form 247 of 500", "10,000 claims"
**Finance:** "file 500 of 1,000", "1,000 filings"
**Legal:** "contract 150 of 200", "500 contracts"
**Healthcare:** "record 800 of 1,000"
**RAG:** "document 7,000 of 10,000"

---

## Example: Full Vertical Adaptation

### Base Copy (Generic)
```
{{first_name}}, your AI isn't broken. It's blind.

Your parser reads the text but strips the context. Strikethroughs disappear. Footnotes detach. By the time your agent sees the document, the truth is already mangled.

We hit 98% accuracy on complex PDFs where Azure averages 68%.

Worth discussing how this compares to what you're seeing, or not really?
```

### Insurance Version
```
{{first_name}}, your claims agent isn't broken. It's blind.

When a medical bill has a strikethrough that says "Denied," your parser strips that out. The agent never sees it. It approves the charge because, from its perspective, the charge was never rejected.

We preserve strikethroughs, handwritten notes, and crossed-out fields on ACORD forms. Your agent finally knows what "No" looks like.

Worth discussing how this changes your claims accuracy, or not really?
```

### Finance Version
```
{{first_name}}, your risk model isn't broken. It's blind.

When a 10-K table has a footnote that says "*Pending Litigation," your parser detaches it. The model sees clean revenue numbers. It never learns about the risk because the risk was stripped upstream.

We preserve table geometry. Footnotes stay attached to their cells. Data is queryable via SQL.

Worth discussing how this changes your risk accuracy, or not really?
```

### Legal Version
```
{{first_name}}, your contract AI isn't broken. It's blind.

When a clause is crossed out in negotiation, that means "No." But your parser strips the strikethrough. The agent sees the text, not the edit. It summarizes deleted terms as valid because, to it, they were never deleted.

We preserve redlines as semantic data. Your agent knows what "rejected" looks like.

Worth discussing how this handles your contract review, or not really?
```

---

## Workflow

When user provides verticals:

1. **Write base copy first** (generic version)
2. **Create separate version for each vertical** using adaptation template
3. **Label each version clearly** (e.g., "Insurance Version", "Finance Version")
4. **Adjust CTA** if persona differs by vertical

**Output format:**
```
## Base Copy
[generic version]

## Insurance Version
[adapted version]

## Finance Version
[adapted version]

## Legal Version
[adapted version]
```

---

## Triggers to Add Per Vertical

| Vertical | Optional Triggers |
|----------|-------------------|
| Insurance | VPC deployment, HIPAA compliance |
| Finance | Real-time parsing, table geometry preservation |
| Legal | Redline preservation, audit trail |
| Healthcare | VPC deployment, HIPAA, EU AI Act compliance |
| Identity/KYC | Field locking, coordinate preservation |
| RAG | Scale (5M pages/day), crash recovery |
