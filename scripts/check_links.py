#!/usr/bin/env python3
"""Check external links in articles and find archive.org replacements for dead ones."""

import argparse
import json
import re
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import quote, urlparse

import httpx

CONTENT_DIR = Path(__file__).resolve().parent.parent / "content"
HEADERS = {"User-Agent": "bryceboe.com-link-checker/1.0 (+https://bryceboe.com/)"}
LINK_PATTERNS = [
    re.compile(r"\[([^\]]*)\]\((https?://[^)]+)\)"),
    re.compile(r"^\s*\[([^\]]*)\]:\s+(https?://\S+)", re.MULTILINE),
]
MAX_WORKERS = 10
TIMEOUT = 10


def check_domain_urls(*, domain, url_info, urls):
    """Check all URLs for a single domain using one client."""
    results = []
    with httpx.Client(
        follow_redirects=True,
        headers=HEADERS,
        http2=True,
        timeout=TIMEOUT,
    ) as client:
        for url in urls:
            status, final_url = check_url(client=client, url=url)
            if status != "ok":
                results.append(
                    {
                        "archive_url": None,
                        "date": url_info[url]["date"],
                        "files": url_info[url]["files"],
                        "final_url": final_url,
                        "status": status,
                        "url": url,
                    }
                )
    return results


def check_url(*, client, url):
    """Return (status, final_url) tuple. status is 'ok', 'redirected', 'blocked', or 'dead'."""
    try:
        resp = client.head(url)
        if resp.status_code >= 400:
            resp = client.get(url)
        if resp.status_code >= 400:
            if resp.headers.get("server", "").lower() == "cloudflare":
                return "blocked", None
            return "dead", None
        final_url = str(resp.url)
        if final_url != url:
            # Ignore redirects that are only temporary (302)
            if resp.history and all(r.status_code == 302 for r in resp.history):
                return "ok", None
            return "redirected", final_url
        return "ok", None
    except Exception:
        return "dead", None


def extract_links():
    """Return deduplicated URL map: url -> {date, files}."""
    url_info = {}
    for path in sorted(CONTENT_DIR.glob("*.md")):
        text = path.read_text()
        date_match = re.search(r"^Date:\s*(\d{4}-\d{2}-\d{2})", text, re.MULTILINE)
        date = date_match.group(1) if date_match else "unknown"
        seen = set()
        for pattern in LINK_PATTERNS:
            for match in pattern.finditer(text):
                url = match.group(2)
                if "web.archive.org" in url or "wikipedia.org" in url:
                    continue
                if url not in seen:
                    seen.add(url)
                    if url not in url_info:
                        url_info[url] = {"date": date, "files": []}
                    url_info[url]["files"].append(path.name)
    return url_info


def find_archive_url(*, date, url):
    """Check archive.org for a snapshot near the article date."""
    ts = date.replace("-", "")
    api_url = f"https://archive.org/wayback/available?url={quote(url, safe='')}&timestamp={ts}"
    try:
        resp = httpx.get(api_url, timeout=TIMEOUT, headers=HEADERS)
        data = resp.json()
        snapshot = data.get("archived_snapshots", {}).get("closest", {})
        if snapshot and snapshot.get("available"):
            return snapshot["url"]
    except Exception:
        pass
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--archive",
        action="store_true",
        help="Check archive.org for dead links",
    )
    args = parser.parse_args()

    url_info = extract_links()
    print(f"Found {len(url_info)} unique external links.\n")

    # Group by domain
    by_domain = defaultdict(list)
    for url in url_info:
        domain = urlparse(url).netloc
        by_domain[domain].append(url)
    print(f"Across {len(by_domain)} domains.\n")

    # Check all domains in parallel
    issues = []
    checked = 0
    total = len(url_info)
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {
            pool.submit(
                check_domain_urls, domain=domain, url_info=url_info, urls=urls
            ): domain
            for domain, urls in by_domain.items()
        }
        for future in as_completed(futures):
            domain_results = future.result()
            issues.extend(domain_results)
            checked += len(by_domain[futures[future]])
            sys.stdout.write(
                f"\r  Checked {checked}/{total} URLs, {len(issues)} issues so far..."
            )
            sys.stdout.flush()

    print(f"\n\nFound {len(issues)} issues.\n")

    if not issues:
        return

    # Look up archive.org for dead links in parallel
    dead = [r for r in issues if r["status"] == "dead"]
    if dead and args.archive:
        print(f"Checking archive.org for {len(dead)} dead links...")
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
            futures = {
                pool.submit(find_archive_url, date=r["date"], url=r["url"]): r
                for r in dead
            }
            for future in as_completed(futures):
                futures[future]["archive_url"] = future.result()

    # Print results
    blocked = [r for r in issues if r["status"] == "blocked"]
    if blocked:
        print(f"\n--- Blocked by Cloudflare ({len(blocked)}) ---\n")
        for r in sorted(blocked, key=lambda x: x["url"]):
            print(f"  {r['url']}")
            print(f"    Files: {', '.join(r['files'])}")

    redirected = [r for r in issues if r["status"] == "redirected"]
    if redirected:
        print(f"\n--- Redirected ({len(redirected)}) ---\n")
        for r in sorted(redirected, key=lambda x: x["url"]):
            print(f"  {r['url']}")
            print(f"    -> {r['final_url']}")
            print(f"    Files: {', '.join(r['files'])}")

    if dead:
        print(f"\n--- Dead ({len(dead)}) ---\n")
        for r in sorted(dead, key=lambda x: x["url"]):
            print(f"  {r['url']}")
            print(f"    Files: {', '.join(r['files'])}")
            print(f"    Date: {r['date']}")
            print(f"    Archive: {r['archive_url'] or 'not found'}")

    # Save results
    out_path = CONTENT_DIR.parent / "dead_links.json"
    with open(out_path, "w") as f:
        json.dump(sorted(issues, key=lambda x: x["url"]), f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
