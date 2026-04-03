#!/usr/bin/env python3
"""Generate graphs of post frequency and content volume over time."""

import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

CONTENT_DIR = Path(__file__).resolve().parent.parent / "content"


def parse_articles():
    """Return list of (date, word_count) for each article."""
    articles = []
    for path in sorted(CONTENT_DIR.glob("*.md")):
        text = path.read_text()
        match = re.search(r"^Date:\s*(\d{4}-\d{2}-\d{2})", text, re.MULTILINE)
        if not match:
            continue
        date = datetime.strptime(match.group(1), "%Y-%m-%d")
        # Word count: everything after the first blank line (header/body separator)
        parts = re.split(r"\n\n", text, maxsplit=1)
        body = parts[1] if len(parts) > 1 else ""
        word_count = len(body.split())
        articles.append((date, word_count))
    articles.sort(key=lambda x: x[0])
    return articles


def main():
    articles = parse_articles()

    # --- Aggregate by quarter ---
    quarter_posts = defaultdict(int)
    for d, _ in articles:
        q = (d.month - 1) // 3
        quarter_start = datetime(d.year, q * 3 + 1, 1)
        quarter_posts[quarter_start] += 1

    q_dates = sorted(quarter_posts.keys())
    q_counts = [quarter_posts[d] for d in q_dates]

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(q_dates, q_counts, width=60, color="#4A90D9", alpha=0.85, align="edge")
    ax.set_title("Post Frequency (by quarter)")
    ax.set_ylabel("Number of posts")
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    fig.tight_layout()
    output_path = CONTENT_DIR.parent / "post_stats.png"
    fig.savefig(output_path, dpi=150)
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
