"""
run_daily_post.py
Main pipeline orchestrator for the Tyr Capital Daily Blog Automation System.

Execution order:
  1. Fetch live crypto market data and news
  2. Generate a unique AI-written post (with duplicate prevention)
  3. Write the post HTML file to /posts/
  4. Inject a new card into blog.html and update the featured article
  5. Commit and push everything to GitHub

Run manually:   python3.11 run_daily_post.py
Scheduled via:  Manus scheduler (daily at 8AM EST)
"""

import sys
import traceback
from datetime import datetime, timezone

# ── Import pipeline modules ───────────────────────────────────────────────────
sys.path.insert(0, "/home/ubuntu/tyr-blog-bot")

from data_fetcher import fetch_all_market_context
from content_generator import generate_post
from html_builder import write_post_file, inject_blog_card
from git_publisher import publish_post


def run():
    start = datetime.now(timezone.utc)
    print(f"\n{'='*60}")
    print(f"TYR CAPITAL DAILY BLOG BOT — {start.strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"{'='*60}\n")

    try:
        # Step 1: Fetch live market data
        print("STEP 1/4 — Fetching live market data...")
        market_ctx = fetch_all_market_context()

        # Step 2: Generate AI post
        print("\nSTEP 2/4 — Generating AI blog post...")
        post = generate_post(market_ctx)
        print(f"  Title    : {post['title']}")
        print(f"  Category : {post['category']}")
        print(f"  Slug     : {post['slug']}")
        print(f"  Excerpt  : {post['excerpt'][:80]}...")

        # Step 3: Write post HTML file
        print("\nSTEP 3/4 — Writing post HTML file...")
        write_post_file(post)

        # Step 4: Update blog.html
        print("\nSTEP 4/4 — Updating blog.html...")
        inject_blog_card(post)

        # Step 5: Commit and push to GitHub
        print("\nSTEP 5/5 — Publishing to GitHub...")
        published = publish_post(post)

        elapsed = (datetime.now(timezone.utc) - start).seconds
        print(f"\n{'='*60}")
        if published:
            print(f"SUCCESS — Post published in {elapsed}s")
            print(f"  File: posts/{post['filename']}")
        else:
            print(f"SKIPPED — No changes to publish")
        print(f"{'='*60}\n")

    except Exception as e:
        print(f"\n{'='*60}")
        print(f"ERROR — Pipeline failed: {e}")
        print(f"{'='*60}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    run()
