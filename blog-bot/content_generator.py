"""
content_generator.py
Uses GPT-4.1-mini to generate a unique, market-relevant blog post for Tyr Capital.
Includes duplicate prevention via a persistent post log.
"""

import os
import json
import re
import unicodedata
from datetime import datetime, timezone
from openai import OpenAI

POST_LOG_PATH = os.path.join(os.path.dirname(__file__), "post_log.json")

client = OpenAI()  # Uses OPENAI_API_KEY env var automatically


# ── Post Log Helpers ──────────────────────────────────────────────────────────

def load_post_log():
    """Load the list of previously published posts."""
    if not os.path.exists(POST_LOG_PATH):
        return []
    with open(POST_LOG_PATH, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_post_log(log):
    """Persist the updated post log."""
    with open(POST_LOG_PATH, "w") as f:
        json.dump(log, f, indent=2)


def slugify(text):
    """Convert a title to a URL-safe slug."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    text = re.sub(r"^-+|-+$", "", text)
    return text[:80]


def get_published_titles_and_topics(log):
    """Return a summary of all previously published titles and topics."""
    titles = [entry.get("title", "") for entry in log]
    topics = list(set(entry.get("topic", "") for entry in log if entry.get("topic")))
    return titles, topics


# ── AI Content Generation ─────────────────────────────────────────────────────

def build_market_summary(market_ctx):
    """Format the live market data into a readable string for the AI prompt."""
    lines = [f"Data fetched: {market_ctx.get('fetched_at', 'N/A')}"]

    # Prices
    prices = market_ctx.get("prices", [])
    if prices:
        lines.append("\n--- LIVE CRYPTO PRICES ---")
        for coin in prices:
            direction = "▲" if coin["change_24h"] >= 0 else "▼"
            lines.append(
                f"  {coin['name']}: ${coin['price_usd']:,.2f} "
                f"({direction}{abs(coin['change_24h'])}% 24h)"
            )

    # Dominance
    dom = market_ctx.get("dominance", {})
    if dom:
        lines.append(f"\n--- MARKET OVERVIEW ---")
        total_mcap = dom.get("total_market_cap_usd", 0)
        lines.append(f"  Total Market Cap: ${total_mcap/1e12:.2f}T")
        lines.append(f"  BTC Dominance: {dom.get('btc_dominance', 'N/A')}%")
        lines.append(f"  24h Market Cap Change: {dom.get('market_cap_change_24h', 'N/A')}%")

    # Fear & Greed
    fg = market_ctx.get("fear_greed", {})
    if fg:
        lines.append(f"\n--- FEAR & GREED INDEX ---")
        lines.append(f"  Score: {fg.get('value', 'N/A')} ({fg.get('classification', 'N/A')})")

    # Trending
    trending = market_ctx.get("trending_coins", [])
    if trending:
        lines.append("\n--- TRENDING COINS TODAY ---")
        for coin in trending:
            lines.append(f"  {coin['name']} ({coin['symbol']}) — Rank #{coin['market_cap_rank']}")

    # News
    news = market_ctx.get("news_headlines", [])
    if news:
        lines.append("\n--- LATEST CRYPTO NEWS HEADLINES ---")
        for item in news[:10]:
            lines.append(f"  [{item.get('source', '')}] {item.get('title', '')}")

    return "\n".join(lines)


def generate_post(market_ctx):
    """
    Generate a complete blog post using GPT-4.1-mini.
    Returns a dict with: title, slug, category, excerpt, read_time, html_body, topic
    """
    log = load_post_log()
    published_titles, published_topics = get_published_titles_and_topics(log)

    market_summary = build_market_summary(market_ctx)

    # Build the avoid list for the prompt
    avoid_titles_str = "\n".join(f"  - {t}" for t in published_titles[-60:]) if published_titles else "  (none yet)"
    avoid_topics_str = ", ".join(published_topics[-30:]) if published_topics else "none yet"

    today = datetime.now(timezone.utc).strftime("%B %d, %Y")

    system_prompt = """You are the lead content strategist and writer for Tyr Capital, a professional digital asset trading and private lending firm. 
Your writing style is authoritative, precise, and educational — like a seasoned institutional trader who also knows how to communicate clearly to a broad audience.
You write long-form blog posts that are genuinely useful, grounded in current market data, and never generic or repetitive.
You never use filler phrases like "In conclusion" or "In summary". You write in complete paragraphs, not bullet lists.
All content is for informational purposes only and does not constitute financial advice."""

    user_prompt = f"""Today is {today}. Write a complete, original blog post for the Tyr Capital website.

LIVE MARKET CONTEXT (use this data to make the post current and relevant):
{market_summary}

PREVIOUSLY PUBLISHED TITLES (DO NOT repeat or closely resemble any of these):
{avoid_titles_str}

PREVIOUSLY COVERED TOPICS (avoid these — pick something fresh):
{avoid_topics_str}

REQUIREMENTS:
- Choose a topic that is genuinely relevant to TODAY'S market conditions based on the data above
- Topic must be from: Bitcoin analysis, crypto market structure, private lending, risk management, crypto education, market cycles, altcoin analysis, macro/crypto correlation, DeFi, on-chain data, trading psychology, or current trending news
- The post must be 600–900 words of substantive body content
- Write in a professional but accessible tone — not academic, not casual
- Do NOT write bullet points or numbered lists — use full paragraphs only
- Include specific price levels, percentages, or market data from the context above where relevant
- End with a natural call-to-action paragraph mentioning Tyr Capital's private lending program

OUTPUT FORMAT — respond ONLY with valid JSON, no markdown, no code fences:
{{
  "title": "The exact post title (compelling, specific, SEO-friendly)",
  "category": "One of: Bitcoin | Lending | Risk | Trading Basics | Market Cycles | Weekly Outlook | Passive Income | Altcoins | Market Update | Crypto Education",
  "topic": "A 3-5 word topic descriptor for duplicate prevention (e.g. 'BTC support level analysis')",
  "excerpt": "A 1-2 sentence teaser for the blog card (max 160 chars)",
  "read_time": "X min",
  "html_body": "The full post body as clean HTML using only <p>, <h2>, <h3>, <strong>, <em> tags. No <html>, <head>, <body>, <style> tags."
}}"""

    print("[content_generator] Calling GPT to generate post...")
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.85,
        max_tokens=2000,
    )

    raw = response.choices[0].message.content.strip()

    # Strip markdown code fences if present
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)

    post_data = json.loads(raw)

    # Generate slug and add metadata
    post_data["slug"] = slugify(post_data["title"])
    post_data["date"] = datetime.now(timezone.utc).strftime("%b %Y")
    post_data["date_full"] = datetime.now(timezone.utc).strftime("%B %d, %Y")
    post_data["filename"] = f"{post_data['slug']}.html"

    print(f"[content_generator] Generated: '{post_data['title']}' [{post_data['category']}]")

    # Update post log
    log.append({
        "title": post_data["title"],
        "slug": post_data["slug"],
        "topic": post_data.get("topic", ""),
        "category": post_data.get("category", ""),
        "date": post_data["date_full"],
        "filename": post_data["filename"],
    })
    save_post_log(log)
    print(f"[content_generator] Post log updated. Total posts: {len(log)}")

    return post_data


if __name__ == "__main__":
    from data_fetcher import fetch_all_market_context
    ctx = fetch_all_market_context()
    post = generate_post(ctx)
    print("\n=== GENERATED POST ===")
    print(f"Title: {post['title']}")
    print(f"Category: {post['category']}")
    print(f"Slug: {post['slug']}")
    print(f"Excerpt: {post['excerpt']}")
    print(f"Read Time: {post['read_time']}")
    print(f"\nBody preview:\n{post['html_body'][:500]}...")
