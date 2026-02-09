"""
Cold Email Reply Analyzer
Extracts GTM intelligence from cold email reply exports.
"""

import csv
import json
import re
from collections import Counter
from dataclasses import dataclass
from typing import List, Dict, Optional
from pathlib import Path


@dataclass
class Reply:
    """Structured reply data."""
    email: str
    first_name: str
    last_name: str
    title: str
    company_name: str
    company_domain: str
    classifications: List[str]
    subject: str
    content: str
    sequence_name: str
    sequence_step: str
    replied_at: str

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def is_bounce(self) -> bool:
        return any(c in self.classifications for c in ['HARD_BOUNCE', 'SOFT_BOUNCE'])

    @property
    def is_ooo(self) -> bool:
        return 'OUT_OF_OFFICE' in self.classifications

    @property
    def is_positive(self) -> bool:
        return any(c in self.classifications for c in ['POSITIVE_TONE', 'WILLING_TO_MEET'])

    @property
    def has_referral(self) -> bool:
        return 'REFERRAL' in self.classifications

    @property
    def needs_more_info(self) -> bool:
        return 'NEEDS_MORE_INFO' in self.classifications

    @property
    def has_solution(self) -> bool:
        return 'HAS_SOLUTION' in self.classifications


def load_replies(filepath: str) -> List[Reply]:
    """Load replies from CSV export."""
    replies = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            classifications = [c.strip() for c in row.get('reply_classifications', '').split(',') if c.strip()]
            reply = Reply(
                email=row.get('email', ''),
                first_name=row.get('first_name', ''),
                last_name=row.get('last_name', ''),
                title=row.get('title', ''),
                company_name=row.get('company_name', ''),
                company_domain=row.get('company_domain', ''),
                classifications=classifications,
                subject=row.get('reply_subject', ''),
                content=row.get('reply_content', ''),
                sequence_name=row.get('sequence_name', ''),
                sequence_step=row.get('sequence_step', ''),
                replied_at=row.get('replied_at', '')
            )
            replies.append(reply)
    return replies


def segment_replies(replies: List[Reply]) -> Dict[str, List[Reply]]:
    """Segment replies into meaningful categories."""
    segments = {
        'hot_leads': [],
        'warm_leads': [],
        'objections': [],
        'neutral_engaged': [],
        'ooo_with_referral': [],
        'bounces': [],
        'opt_outs': [],
        'other': []
    }

    for reply in replies:
        content_lower = reply.content.lower()

        # Bounces
        if reply.is_bounce or 'undeliverable' in content_lower or 'delivery has failed' in content_lower:
            segments['bounces'].append(reply)
            continue

        # Opt-outs
        if 'OPT_OUT' in reply.classifications:
            segments['opt_outs'].append(reply)
            continue

        # Hot leads
        if reply.is_positive:
            segments['hot_leads'].append(reply)
            continue

        # Warm leads (needs info or internal referral language)
        if reply.needs_more_info or any(phrase in content_lower for phrase in ['forwarding', 'connect you with', 'looking into who']):
            segments['warm_leads'].append(reply)
            continue

        # OOO with referral
        if reply.is_ooo and reply.has_referral:
            segments['ooo_with_referral'].append(reply)
            continue

        # Pure OOO (skip)
        if reply.is_ooo:
            segments['other'].append(reply)
            continue

        # Has solution (objection)
        if reply.has_solution:
            segments['objections'].append(reply)
            continue

        # Check for real human engagement
        if len(reply.content) > 50 and 'AUTOMATED' not in reply.classifications:
            segments['neutral_engaged'].append(reply)
            continue

        segments['other'].append(reply)

    return segments


def extract_title_patterns(replies: List[Reply]) -> Dict[str, List[Reply]]:
    """Group replies by title cluster."""
    clusters = {
        'c_level': [],
        'vp_director': [],
        'manager': [],
        'senior_ic': [],
        'ic': [],
        'other': []
    }

    for reply in replies:
        title_lower = reply.title.lower()

        if any(t in title_lower for t in ['ceo', 'cto', 'cfo', 'coo', 'founder', 'co-founder', 'chief']):
            clusters['c_level'].append(reply)
        elif any(t in title_lower for t in ['vp', 'vice president', 'director', 'head of']):
            clusters['vp_director'].append(reply)
        elif 'manager' in title_lower:
            clusters['manager'].append(reply)
        elif any(t in title_lower for t in ['senior', 'staff', 'principal', 'lead']):
            clusters['senior_ic'].append(reply)
        elif any(t in title_lower for t in ['engineer', 'scientist', 'analyst', 'developer']):
            clusters['ic'].append(reply)
        else:
            clusters['other'].append(reply)

    return clusters


def extract_competitors(replies: List[Reply], competitor_list: Optional[List[str]] = None) -> Dict[str, int]:
    """
    Extract competitor mentions from reply content.

    Args:
        replies: List of Reply objects
        competitor_list: List of competitor names to search for.
                        If None, searches for common patterns like "we use X", "compared to X"
    """
    mentions = Counter()

    for reply in replies:
        content_lower = reply.content.lower()

        if competitor_list:
            # Search for provided competitors
            for competitor in competitor_list:
                if competitor.lower() in content_lower:
                    mentions[competitor] += 1

        # Always look for these universal patterns
        # "we use X" / "we're using X" / "currently use X"
        use_pattern = r'(?:we|they|i)\s+(?:use|using|have|built)\s+(\w+(?:\s+\w+)?)'
        for match in re.finditer(use_pattern, content_lower):
            tool = match.group(1).strip()
            if len(tool) > 2 and tool not in ['our', 'own', 'the', 'this', 'that', 'some']:
                mentions[f"(detected) {tool}"] += 1

        # "built our own" / "internal team" patterns
        if any(phrase in content_lower for phrase in ['built our own', 'own ai team', 'internal team', 'in-house']):
            mentions["Built in-house"] += 1

    return dict(mentions.most_common())


def extract_original_message(content: str) -> Optional[str]:
    """Extract the original outbound message from quoted reply content."""
    # Gmail format: "On [date], [name] wrote:"
    gmail_pattern = r'On .+? wrote:\s*\n(.*?)(?=\n\n--|$)'

    # Outlook format: "From: [sender]" block
    outlook_pattern = r'From:.+?Subject:.+?\n\n(.*?)(?=\n\n--|$)'

    # Try Gmail format first
    match = re.search(gmail_pattern, content, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()

    # Try Outlook format
    match = re.search(outlook_pattern, content, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()

    return None


def analyze_campaign_performance(replies: List[Reply]) -> Dict[str, Dict]:
    """Analyze performance by campaign/sequence."""
    campaigns = {}

    for reply in replies:
        seq = reply.sequence_name
        if not seq:
            continue

        if seq not in campaigns:
            campaigns[seq] = {
                'total': 0,
                'hot_leads': 0,
                'warm_leads': 0,
                'bounces': 0,
                'steps': Counter()
            }

        campaigns[seq]['total'] += 1
        campaigns[seq]['steps'][reply.sequence_step] += 1

        if reply.is_positive:
            campaigns[seq]['hot_leads'] += 1
        elif reply.needs_more_info:
            campaigns[seq]['warm_leads'] += 1
        elif reply.is_bounce:
            campaigns[seq]['bounces'] += 1

    return campaigns


def generate_summary(replies: List[Reply]) -> Dict:
    """Generate comprehensive analysis summary."""
    segments = segment_replies(replies)
    title_clusters = extract_title_patterns([r for r in replies if not r.is_bounce])
    competitors = extract_competitors(replies)
    campaigns = analyze_campaign_performance(replies)

    # Classification distribution
    all_classifications = []
    for reply in replies:
        all_classifications.extend(reply.classifications)
    classification_counts = Counter(all_classifications)

    return {
        'total_replies': len(replies),
        'segments': {k: len(v) for k, v in segments.items()},
        'segment_details': {
            'hot_leads': [{'company': r.company_name, 'title': r.title, 'campaign': r.sequence_name} for r in segments['hot_leads']],
            'warm_leads': [{'company': r.company_name, 'title': r.title, 'campaign': r.sequence_name} for r in segments['warm_leads']],
        },
        'title_clusters': {k: len(v) for k, v in title_clusters.items()},
        'classification_distribution': dict(classification_counts.most_common()),
        'competitor_mentions': competitors,
        'campaign_performance': campaigns
    }


def main(filepath: str, output_path: Optional[str] = None):
    """Main analysis function."""
    print(f"Loading replies from: {filepath}")
    replies = load_replies(filepath)
    print(f"Loaded {len(replies)} replies")

    summary = generate_summary(replies)

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        print(f"Summary saved to: {output_path}")

    return summary


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python reply_analyzer.py <csv_filepath> [output_json_path]")
        sys.exit(1)

    filepath = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    summary = main(filepath, output_path)
    print(json.dumps(summary, indent=2))
