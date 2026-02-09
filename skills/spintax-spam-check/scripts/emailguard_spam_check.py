#!/usr/bin/env python3
"""
EmailGuard Spam Check with Self-Annealing

This script checks email copy for spam triggers using:
1. Local learned-spam-words.json database (checked first)
2. EmailGuard API (for unknown content)

New spam words discovered via API are stored locally for future reference,
reducing API calls over time (self-annealing).

Usage:
    python emailguard_spam_check.py "Your email copy here"
    python emailguard_spam_check.py --file path/to/copy.txt
    python emailguard_spam_check.py --expand-spintax "Copy with {spintax|variations}"
"""

import argparse
import json
import os
import re
import sys
import http.client
from datetime import datetime
from pathlib import Path
from typing import Optional

# Paths
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent / "data"
LEARNED_WORDS_FILE = DATA_DIR / "learned-spam-words.json"

# Load API key from environment
def get_api_key() -> str:
    """Get EmailGuard API key from environment."""
    key = os.getenv("EMAILGUARD_API_KEY")
    if not key:
        # Try loading from .env file
        env_file = Path(__file__).parents[5] / ".env"  # Go up to repo root
        if env_file.exists():
            with open(env_file) as f:
                for line in f:
                    if line.startswith("EMAILGUARD_API_KEY="):
                        key = line.split("=", 1)[1].strip()
                        break
    if not key:
        print("Error: EMAILGUARD_API_KEY not found in environment or .env file", file=sys.stderr)
        sys.exit(1)
    return key


def load_learned_words() -> dict:
    """Load the learned spam words database."""
    if not LEARNED_WORDS_FILE.exists():
        return {"words": {}, "phrases": {}, "last_updated": None}

    with open(LEARNED_WORDS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_learned_words(data: dict) -> None:
    """Save the learned spam words database."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    data["last_updated"] = datetime.now().isoformat()
    with open(LEARNED_WORDS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def expand_spintax(text: str) -> list[str]:
    """
    Expand spintax into all possible variations.

    Example: "Hello {world|there}" -> ["Hello world", "Hello there"]

    For large spintax, returns a sample to avoid combinatorial explosion.
    """
    # Find spintax patterns: {option1|option2|option3}
    pattern = r'\{([^{}]+)\}'

    def get_options(match):
        return match.group(1).split('|')

    # Find all spintax blocks
    matches = list(re.finditer(pattern, text))

    if not matches:
        return [text]

    # Generate all combinations (with limit)
    results = [text]
    MAX_COMBINATIONS = 50  # Limit to prevent explosion

    for match in matches:
        options = get_options(match)
        new_results = []
        for result in results:
            for option in options:
                new_result = result.replace(match.group(0), option.strip(), 1)
                new_results.append(new_result)
                if len(new_results) >= MAX_COMBINATIONS:
                    break
            if len(new_results) >= MAX_COMBINATIONS:
                break
        results = new_results
        if len(results) >= MAX_COMBINATIONS:
            break

    return results[:MAX_COMBINATIONS]


def check_local_database(content: str, learned_words: dict) -> dict:
    """
    Check content against local spam word database.

    Returns dict with:
    - found_words: list of spam words found
    - suggestions: dict of word -> replacements
    """
    content_lower = content.lower()
    found = {"words": [], "phrases": [], "suggestions": {}}

    # Check single words
    for word, data in learned_words.get("words", {}).items():
        if re.search(r'\b' + re.escape(word) + r'\b', content_lower):
            found["words"].append(word)
            found["suggestions"][word] = data.get("replacements", [])
            # Increment hit count
            learned_words["words"][word]["hit_count"] = data.get("hit_count", 0) + 1

    # Check phrases
    for phrase, data in learned_words.get("phrases", {}).items():
        if phrase.lower() in content_lower:
            found["phrases"].append(phrase)
            found["suggestions"][phrase] = data.get("replacements", [])
            # Increment hit count
            learned_words["phrases"][phrase]["hit_count"] = data.get("hit_count", 0) + 1

    return found


def call_emailguard_api(content: str, api_key: str) -> Optional[dict]:
    """
    Call EmailGuard API to check content for spam triggers.

    Returns API response or None on error.
    """
    try:
        conn = http.client.HTTPSConnection("app.emailguard.io")

        payload = json.dumps({"content": content})

        headers = {
            'Content-Type': "application/json",
            'Authorization': f"Bearer {api_key}"
        }

        conn.request("POST", "/api/v1/content-spam-check", payload, headers)

        res = conn.getresponse()
        data = res.read()

        if res.status == 200:
            return json.loads(data.decode("utf-8"))
        else:
            print(f"API Error: {res.status} - {data.decode('utf-8')}", file=sys.stderr)
            return None

    except Exception as e:
        print(f"API Connection Error: {e}", file=sys.stderr)
        return None
    finally:
        conn.close()


def extract_spam_words_from_response(response: dict) -> list[dict]:
    """
    Extract spam words/phrases from EmailGuard API response.

    Adapts to various response formats.
    """
    spam_items = []

    # Handle EmailGuard API nested format: data.message.spam_words
    if "data" in response and isinstance(response["data"], dict):
        message = response["data"].get("message", {})
        if isinstance(message, dict) and "spam_words" in message:
            for word in message.get("spam_words", []):
                if isinstance(word, str):
                    spam_items.append({"text": word, "severity": "medium", "category": "api_detected"})
                elif isinstance(word, dict):
                    spam_items.append(word)
            return spam_items  # Return early if we found the nested format

    # Handle different response formats
    if "issues" in response:
        for issue in response.get("issues", []):
            spam_items.append({
                "text": issue.get("word", issue.get("text", "")),
                "severity": issue.get("severity", "medium"),
                "category": issue.get("category", "unknown")
            })

    if "spam_words" in response:
        for word in response.get("spam_words", []):
            if isinstance(word, str):
                spam_items.append({"text": word, "severity": "medium", "category": "unknown"})
            elif isinstance(word, dict):
                spam_items.append(word)

    if "triggers" in response:
        for trigger in response.get("triggers", []):
            spam_items.append({
                "text": trigger.get("text", trigger) if isinstance(trigger, dict) else trigger,
                "severity": trigger.get("severity", "medium") if isinstance(trigger, dict) else "medium",
                "category": "trigger"
            })

    return spam_items


def add_to_learned_database(spam_items: list[dict], learned_words: dict) -> None:
    """
    Add newly discovered spam words to the local database.
    """
    today = datetime.now().strftime("%Y-%m-%d")

    for item in spam_items:
        text = item.get("text", "").lower().strip()
        if not text:
            continue

        # Determine if it's a word or phrase
        is_phrase = " " in text
        category = "phrases" if is_phrase else "words"

        # Skip if already in database
        if text in learned_words.get(category, {}):
            continue

        # Add to database
        if category not in learned_words:
            learned_words[category] = {}

        learned_words[category][text] = {
            "replacements": [],  # Will be filled in manually or by AI
            "severity": item.get("severity", "medium"),
            "category": item.get("category", "unknown"),
            "discovered": today,
            "hit_count": 1
        }

        print(f"  [NEW] Added '{text}' to local database")


def suggest_replacements(word: str) -> list[str]:
    """
    Suggest safe replacements for common spam words.

    This is a basic implementation - can be enhanced with AI suggestions.
    """
    common_replacements = {
        "free": ["complimentary", "no-cost", "included", "at no charge"],
        "guarantee": ["back", "assure", "confirm", "promise"],
        "guaranteed": ["backed", "assured", "confirmed", "promised"],
        "act now": ["when you're ready", "if interested", "at your convenience"],
        "limited time": ["current", "available now", "while available"],
        "urgent": ["timely", "time-sensitive", "current"],
        "buy": ["get", "acquire", "pick up", "invest in"],
        "cheap": ["affordable", "cost-effective", "budget-friendly"],
        "click here": ["learn more", "see details", "explore"],
        "congratulations": ["great news", "exciting update", "good news"],
        "deal": ["opportunity", "option", "offer"],
        "discount": ["savings", "reduced rate", "special rate"],
        "earn": ["generate", "create", "build"],
        "exclusive": ["select", "curated", "tailored"],
        "expire": ["end", "close", "conclude"],
        "instant": ["quick", "fast", "prompt"],
        "limited": ["select", "curated", "specific"],
        "money": ["investment", "budget", "resources"],
        "offer": ["opportunity", "option", "possibility"],
        "order": ["request", "get started", "proceed"],
        "price": ["rate", "investment", "cost"],
        "profit": ["benefit", "gain", "return"],
        "promise": ["commit", "assure", "guarantee"],
        "risk-free": ["low-risk", "safe", "secure"],
        "sale": ["opportunity", "availability", "option"],
        "save": ["keep", "retain", "preserve"],
        "special": ["unique", "tailored", "curated"],
        "winner": ["successful", "selected", "chosen"],
    }

    word_lower = word.lower()
    return common_replacements.get(word_lower, [])


def check_content(content: str, api_key: str, use_api: bool = True) -> dict:
    """
    Full spam check workflow:
    1. Check local database
    2. Call API if needed
    3. Store new findings

    Returns comprehensive results.
    """
    learned_words = load_learned_words()

    results = {
        "content_checked": content[:200] + "..." if len(content) > 200 else content,
        "local_matches": {},
        "api_matches": [],
        "all_suggestions": {},
        "is_clean": True,
        "api_called": False
    }

    # Step 1: Check local database
    local_found = check_local_database(content, learned_words)

    if local_found["words"] or local_found["phrases"]:
        results["local_matches"] = {
            "words": local_found["words"],
            "phrases": local_found["phrases"]
        }
        results["all_suggestions"].update(local_found["suggestions"])
        results["is_clean"] = False

        # Add default suggestions for words without replacements
        for word in local_found["words"] + local_found["phrases"]:
            if not results["all_suggestions"].get(word):
                results["all_suggestions"][word] = suggest_replacements(word)

    # Step 2: Call API if enabled
    if use_api:
        results["api_called"] = True
        api_response = call_emailguard_api(content, api_key)

        if api_response:
            spam_items = extract_spam_words_from_response(api_response)

            if spam_items:
                results["api_matches"] = [item["text"] for item in spam_items]
                results["is_clean"] = False

                # Add to local database
                add_to_learned_database(spam_items, learned_words)

                # Add suggestions
                for item in spam_items:
                    text = item["text"]
                    if text not in results["all_suggestions"]:
                        results["all_suggestions"][text] = suggest_replacements(text)

            # Include raw API response for debugging
            results["api_response"] = api_response

    # Save updated learned words
    save_learned_words(learned_words)

    return results


def format_results(results: dict) -> str:
    """Format results for display."""
    lines = []

    lines.append("=" * 60)
    lines.append("SPAM CHECK RESULTS")
    lines.append("=" * 60)

    if results["is_clean"]:
        lines.append("\n[PASS] Content appears clean!")
    else:
        lines.append("\n[ISSUES FOUND] Content may trigger spam filters")

    if results["local_matches"]:
        lines.append("\n--- LOCAL DATABASE MATCHES ---")
        if results["local_matches"].get("words"):
            lines.append(f"Words: {', '.join(results['local_matches']['words'])}")
        if results["local_matches"].get("phrases"):
            lines.append(f"Phrases: {', '.join(results['local_matches']['phrases'])}")

    if results["api_matches"]:
        lines.append("\n--- API DETECTED ---")
        lines.append(f"New triggers: {', '.join(results['api_matches'])}")

    if results["all_suggestions"]:
        lines.append("\n--- SUGGESTED REPLACEMENTS ---")
        for word, replacements in results["all_suggestions"].items():
            if replacements:
                lines.append(f"  '{word}' -> {', '.join(replacements)}")
            else:
                lines.append(f"  '{word}' -> [no suggestions - add manually]")

    lines.append("\n" + "=" * 60)

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Check email copy for spam triggers with self-annealing database",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python emailguard_spam_check.py "Your email copy here"
    python emailguard_spam_check.py --file copy.txt
    python emailguard_spam_check.py --expand-spintax "Hi {there|friend}"
    python emailguard_spam_check.py --local-only "Quick check without API"
        """
    )

    parser.add_argument("content", nargs="?", help="Email content to check")
    parser.add_argument("--file", "-f", help="Read content from file")
    parser.add_argument("--expand-spintax", "-e", action="store_true",
                        help="Expand spintax and check all variations")
    parser.add_argument("--local-only", "-l", action="store_true",
                        help="Only check local database, skip API call")
    parser.add_argument("--json", "-j", action="store_true",
                        help="Output results as JSON")

    args = parser.parse_args()

    # Get content
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
    elif args.content:
        content = args.content
    else:
        # Read from stdin
        content = sys.stdin.read()

    if not content.strip():
        print("Error: No content provided", file=sys.stderr)
        sys.exit(1)

    # Get API key
    api_key = get_api_key() if not args.local_only else ""

    # Expand spintax if requested
    if args.expand_spintax:
        variations = expand_spintax(content)
        print(f"Checking {len(variations)} spintax variations...")

        all_results = []
        for i, variation in enumerate(variations, 1):
            print(f"\n--- Variation {i}/{len(variations)} ---")
            result = check_content(variation, api_key, use_api=not args.local_only)
            all_results.append(result)

            if not args.json:
                print(format_results(result))

        if args.json:
            print(json.dumps(all_results, indent=2))
    else:
        result = check_content(content, api_key, use_api=not args.local_only)

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(format_results(result))


if __name__ == "__main__":
    main()
