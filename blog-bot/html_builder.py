"""
html_builder.py
Generates the individual HTML post file and injects a new card into blog.html.
"""

import os
import re

REPO_PATH = "/home/ubuntu/Tyr-Capital"
POSTS_DIR = os.path.join(REPO_PATH, "posts")
BLOG_HTML = os.path.join(REPO_PATH, "blog.html")

# Category → thumbnail image mapping
CATEGORY_THUMBS = {
    "Bitcoin":        "images/thumb-bitcoin.jpg",
    "Market Update":  "images/thumb-bitcoin.jpg",
    "Weekly Outlook": "images/thumb-outlook.jpg",
    "Lending":        "images/thumb-lending.jpg",
    "Passive Income": "images/thumb-passive.jpg",
    "Risk":           "images/thumb-risk.jpg",
    "Trading Basics": "images/thumb-trading.jpg",
    "Market Cycles":  "images/thumb-cycles.jpg",
    "Altcoins":       "images/thumb-outlook.jpg",
    "Crypto Education": "images/thumb-trading.jpg",
}

# Category → data-category slug mapping for the filter bar
CATEGORY_FILTER = {
    "Bitcoin":          "bitcoin",
    "Market Update":    "bitcoin",
    "Weekly Outlook":   "weekly-outlook",
    "Lending":          "lending",
    "Passive Income":   "passive-income",
    "Risk":             "risk",
    "Trading Basics":   "trading-basics",
    "Market Cycles":    "market-cycles",
    "Altcoins":         "market-cycles",
    "Crypto Education": "trading-basics",
}


def build_post_html(post):
    """
    Generate a full standalone HTML post page from the post data dict.
    Returns the HTML string.
    """
    title = post["title"]
    category = post["category"]
    excerpt = post["excerpt"]
    read_time = post["read_time"]
    date_full = post["date_full"]
    html_body = post["html_body"]
    slug = post["slug"]
    thumb = CATEGORY_THUMBS.get(category, "images/thumb-bitcoin.jpg")
    thumb_abs = f"https://tyrcapital.io/{thumb}"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-6HGF1EDX4Y"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-6HGF1EDX4Y');
  </script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Tyr Capital</title>
  <meta name="description" content="{excerpt}">
  <link rel="canonical" href="https://tyrcapital.io/posts/{slug}.html">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://tyrcapital.io/posts/{slug}.html">
  <meta property="og:title" content="{title} | Tyr Capital">
  <meta property="og:description" content="{excerpt}">
  <meta property="og:image" content="{thumb_abs}">
  <meta property="og:site_name" content="Tyr Capital">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title} | Tyr Capital">
  <meta name="twitter:description" content="{excerpt}">
  <meta name="twitter:image" content="{thumb_abs}">

  <!-- JSON-LD Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": "{title}",
    "description": "{excerpt}",
    "image": "{thumb_abs}",
    "author": {{"@type": "Person", "name": "Coley Grantham"}},
    "publisher": {{"@type": "Organization", "name": "Tyr Capital", "url": "https://tyrcapital.io"}},
    "datePublished": "{date_full}",
    "dateModified": "{date_full}",
    "mainEntityOfPage": {{"@type": "WebPage", "@id": "https://tyrcapital.io/posts/{slug}.html"}}
  }}
  </script>

  <link rel="icon" type="image/png" href="../favicon.png">
  <link rel="stylesheet" href="../styles.css">
</head>
<body>

  <div class="topbar">
    <div class="container nav">
      <a href="../index.html" class="brand">
        <span class="brand-mark"></span>
        <span>Tyr Capital</span>
      </a>
      <button class="hamburger" id="hamburgerBtn" aria-label="Toggle navigation" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
      <div class="nav-links" id="navLinks">
        <a href="../index.html#about">About</a>
        <a href="../blog.html">Blog</a>
        <a href="../index.html#ceo">Leadership</a>
        <a href="../index.html#contact">Contact</a>
        <a class="telegram-btn" href="../index.html#lender">Become A Lender</a>
      </div>
    </div>
  </div>

  <article class="post-article">
    <div class="container post-container">

      <div class="post-header">
        <a href="../blog.html" class="back-link">← Back to Blog</a>
        <span class="post-category">{category}</span>
        <h1 class="post-article-title">{title}</h1>
        <div class="post-meta">
          <span class="post-author">&#9998; Coley Grantham</span>
          <span class="post-date">&#128197; {date_full}</span>
          <span class="post-read-time">&#9201; {read_time} read</span>
        </div>
        <div class="gold-line"></div>
      </div>

      <div class="post-hero-image">
        <img src="../{thumb}" alt="{title}" loading="lazy">
      </div>

      <div class="post-body">
        {html_body}
      </div>

      <div class="post-footer-cta">
        <h3>Put Your Capital to Work</h3>
        <p>Tyr Capital offers structured private lending opportunities for accredited investors seeking consistent, defined returns in the digital asset space. If you're interested in learning more, reach out directly.</p>
        <a class="cta-btn" href="../index.html#lender">Become A Lender</a>
      </div>

    </div>
  </article>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-inner">
        <div class="footer-brand">
          <a href="../index.html" class="brand" style="margin-bottom:12px; display:inline-flex;">
            <span class="brand-mark"></span>
            <span>Tyr Capital</span>
          </a>
          <p class="footer-tagline">Disciplined execution.<br>Structured risk. Long-term thinking.</p>
          <a href="https://t.me/tyrcapitaltrades" target="_blank" rel="noopener noreferrer" class="footer-telegram">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>
            Join Telegram Channel
          </a>
        </div>
        <div class="footer-nav">
          <h4 class="footer-heading">Navigation</h4>
          <ul>
            <li><a href="../index.html#about">About</a></li>
            <li><a href="../blog.html">Blog</a></li>
            <li><a href="../index.html#ceo">Leadership</a></li>
            <li><a href="../index.html#lender">Become A Lender</a></li>
            <li><a href="../index.html#contact">Contact</a></li>
          </ul>
        </div>
        <div class="footer-nav">
          <h4 class="footer-heading">Contact</h4>
          <ul>
            <li><a href="mailto:tyrcapitalllc@gmail.com">tyrcapitalllc@gmail.com</a></li>
            <li><a href="https://t.me/tyrcapitaltrades" target="_blank" rel="noopener noreferrer">Telegram: Tyr Capital Trades</a></li>
            <li><a href="https://www.linkedin.com/in/coley-grantham-1b10a4bb/" target="_blank" rel="noopener noreferrer">LinkedIn: Coley Grantham</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="footer-disclaimer">Tyr Capital research and blog content are provided for informational purposes only and do not constitute financial or investment advice.</p>
        <p class="footer-copy">&copy; <span id="footerYear"></span> Tyr Capital LLC. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <script>
    document.getElementById('footerYear').textContent = new Date().getFullYear();
    const hamburgerBtn = document.getElementById('hamburgerBtn');
    const navLinks = document.getElementById('navLinks');
    if (hamburgerBtn && navLinks) {{
      hamburgerBtn.addEventListener('click', function () {{
        const isOpen = navLinks.classList.toggle('open');
        hamburgerBtn.classList.toggle('open', isOpen);
        hamburgerBtn.setAttribute('aria-expanded', isOpen);
      }});
      navLinks.querySelectorAll('a').forEach(function (link) {{
        link.addEventListener('click', function () {{
          navLinks.classList.remove('open');
          hamburgerBtn.classList.remove('open');
          hamburgerBtn.setAttribute('aria-expanded', 'false');
        }});
      }});
    }}

    // GA read time tracking
    const readMilestones = {{30: false, 60: false, 120: false}};
    setInterval(function() {{
      Object.keys(readMilestones).forEach(function(sec) {{
        if (!readMilestones[sec]) {{
          readMilestones[sec] = true;
          if (typeof gtag === 'function') {{
            gtag('event', 'read_time', {{event_category: 'Engagement', event_label: sec + 's', page_title: document.title}});
          }}
        }}
      }});
    }}, 1000);
  </script>

</body>
</html>
"""


def write_post_file(post):
    """Write the generated post HTML to the posts/ directory."""
    filepath = os.path.join(POSTS_DIR, post["filename"])
    html = build_post_html(post)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[html_builder] Post file written: {filepath}")
    return filepath


def inject_blog_card(post):
    """
    Prepend a new post card to the post-grid in blog.html and update the post count badge.
    Also updates the featured article to the latest post.
    """
    with open(BLOG_HTML, "r", encoding="utf-8") as f:
        content = f.read()

    title = post["title"]
    slug = post["slug"]
    filename = post["filename"]
    category = post["category"]
    excerpt = post["excerpt"]
    read_time = post["read_time"]
    date = post["date"]
    thumb = CATEGORY_THUMBS.get(category, "images/thumb-bitcoin.jpg")
    filter_cat = CATEGORY_FILTER.get(category, "bitcoin")

    # --- New post card HTML ---
    new_card = f"""
        <article class="post-card fade-in" data-category="{filter_cat}">
          <a href="posts/{filename}" class="post-thumb-link">
            <div class="post-thumb" style="background-image: url('{thumb}');">
              <span class="post-category">{category}</span>
            </div>
          </a>
          <div class="post-content">
            <div class="post-meta">
              <span class="post-author">&#9998; Coley Grantham</span>
              <span class="post-date">&#128197; {date}</span>
              <span class="post-read-time">&#9201; {read_time}</span>
            </div>
            <h3 class="post-title">
              <a href="posts/{filename}">{title}</a>
            </h3>
            <p class="post-excerpt">
              {excerpt}
            </p>
            <a class="post-link" href="posts/{filename}">Read Article →</a>
          </div>
        </article>
"""

    # Inject at the top of the post grid
    grid_marker = '<div class="post-grid" id="postGrid">'
    if grid_marker in content:
        content = content.replace(grid_marker, grid_marker + new_card, 1)
    else:
        print("[html_builder] WARNING: Could not find post-grid marker in blog.html")
        return

    # --- Update featured article ---
    featured_pattern = re.compile(
        r'(<div class="featured-article">.*?</div>\s*</div>\s*</div>)',
        re.DOTALL
    )
    new_featured = f"""<div class="featured-article">
        <a href="posts/{filename}" class="featured-thumb">
          <img src="{thumb}" alt="{title}" loading="lazy">
          <span class="featured-label">Featured</span>
        </a>
        <div class="featured-content">
          <span class="post-category post-category-featured">{category}</span>
          <h2 class="featured-title">
            <a href="posts/{filename}">{title}</a>
          </h2>
          <p class="featured-excerpt">
            {excerpt}
          </p>
          <div class="post-meta">
            <span class="post-author">&#9998; Coley Grantham</span>
            <span class="post-date">&#128197; {post['date_full']}</span>
            <span class="post-read-time">&#9201; {read_time} read</span>
          </div>
          <a class="post-link" href="posts/{filename}">Read Article →</a>
        </div>
      </div>"""

    content = featured_pattern.sub(new_featured, content, count=1)

    # --- Update post count badge ---
    # Count all post-card articles
    card_count = len(re.findall(r'<article class="post-card', content))
    content = re.sub(
        r'<span class="post-count-badge">\d+ Articles</span>',
        f'<span class="post-count-badge">{card_count} Articles</span>',
        content
    )

    with open(BLOG_HTML, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[html_builder] blog.html updated. New card prepended. Total cards: {card_count}")


if __name__ == "__main__":
    # Quick test with dummy data
    test_post = {
        "title": "Test Post: Bitcoin Holds Key Support at $78K",
        "slug": "test-post-bitcoin-holds-key-support",
        "filename": "test-post-bitcoin-holds-key-support.html",
        "category": "Bitcoin",
        "excerpt": "Bitcoin is holding a critical support level as the market digests macro headwinds.",
        "read_time": "5 min",
        "date": "Apr 2026",
        "date_full": "April 23, 2026",
        "html_body": "<p>This is a test post body.</p>",
        "topic": "BTC support level test",
    }
    filepath = write_post_file(test_post)
    inject_blog_card(test_post)
    print("Test complete.")
