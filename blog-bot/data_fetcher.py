"""
data_fetcher.py
Fetches live crypto market data and trending news headlines
for use by the Tyr Capital daily blog automation system.
"""

import requests
import json
from datetime import datetime, timezone


def get_crypto_market_data():
    """Fetch live BTC, ETH, SOL prices and 24h changes from CoinGecko (free API)."""
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,solana,ripple,cardano,avalanche-2,chainlink,polkadot",
        "vs_currencies": "usd",
        "include_24hr_change": "true",
        "include_market_cap": "true",
        "include_24hr_vol": "true",
    }
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        coins = []
        name_map = {
            "bitcoin": "Bitcoin (BTC)",
            "ethereum": "Ethereum (ETH)",
            "solana": "Solana (SOL)",
            "ripple": "XRP",
            "cardano": "Cardano (ADA)",
            "avalanche-2": "Avalanche (AVAX)",
            "chainlink": "Chainlink (LINK)",
            "polkadot": "Polkadot (DOT)",
        }
        for coin_id, info in data.items():
            coins.append({
                "name": name_map.get(coin_id, coin_id),
                "price_usd": info.get("usd", 0),
                "change_24h": round(info.get("usd_24h_change", 0), 2),
                "market_cap": info.get("usd_market_cap", 0),
                "volume_24h": info.get("usd_24h_vol", 0),
            })
        return coins
    except Exception as e:
        print(f"[data_fetcher] Market data error: {e}")
        return []


def get_btc_dominance():
    """Fetch BTC dominance and total crypto market cap."""
    url = "https://api.coingecko.com/api/v3/global"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json().get("data", {})
        return {
            "btc_dominance": round(data.get("market_cap_percentage", {}).get("btc", 0), 2),
            "total_market_cap_usd": data.get("total_market_cap", {}).get("usd", 0),
            "total_volume_24h": data.get("total_volume", {}).get("usd", 0),
            "market_cap_change_24h": round(data.get("market_cap_change_percentage_24h_usd", 0), 2),
        }
    except Exception as e:
        print(f"[data_fetcher] Dominance data error: {e}")
        return {}


def get_crypto_news():
    """Fetch latest crypto news from CoinDesk and Decrypt RSS feeds."""
    import xml.etree.ElementTree as ET
    feeds = [
        ("CoinDesk", "https://www.coindesk.com/arc/outboundfeeds/rss/"),
        ("Decrypt", "https://decrypt.co/feed"),
        ("CoinTelegraph", "https://cointelegraph.com/rss"),
    ]
    headlines = []
    for source, feed_url in feeds:
        try:
            resp = requests.get(feed_url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
            resp.raise_for_status()
            root = ET.fromstring(resp.content)
            items = root.findall(".//item")
            for item in items[:5]:
                title = item.findtext("title", "").strip()
                description = item.findtext("description", "").strip()
                pub_date = item.findtext("pubDate", "").strip()
                if title:
                    headlines.append({
                        "title": title,
                        "description": description[:200] if description else "",
                        "source": source,
                        "published_at": pub_date,
                    })
        except Exception as e:
            print(f"[data_fetcher] RSS error ({source}): {e}")
    return headlines[:15]


def get_trending_coins():
    """Fetch trending coins on CoinGecko today."""
    url = "https://api.coingecko.com/api/v3/search/trending"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        items = resp.json().get("coins", [])
        trending = []
        for item in items[:7]:
            coin = item.get("item", {})
            trending.append({
                "name": coin.get("name", ""),
                "symbol": coin.get("symbol", ""),
                "market_cap_rank": coin.get("market_cap_rank", "N/A"),
            })
        return trending
    except Exception as e:
        print(f"[data_fetcher] Trending coins error: {e}")
        return []


def get_fear_greed_index():
    """Fetch the Crypto Fear & Greed Index."""
    url = "https://api.alternative.me/fng/"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json().get("data", [{}])[0]
        return {
            "value": data.get("value", "N/A"),
            "classification": data.get("value_classification", "N/A"),
        }
    except Exception as e:
        print(f"[data_fetcher] Fear & Greed error: {e}")
        return {"value": "N/A", "classification": "N/A"}


def fetch_all_market_context():
    """Aggregate all live market data into a single context dict for the AI."""
    print("[data_fetcher] Fetching live market data...")
    context = {
        "fetched_at": datetime.now(timezone.utc).strftime("%B %d, %Y at %H:%M UTC"),
        "prices": get_crypto_market_data(),
        "dominance": get_btc_dominance(),
        "news_headlines": get_crypto_news(),
        "trending_coins": get_trending_coins(),
        "fear_greed": get_fear_greed_index(),
    }
    print(f"[data_fetcher] Fetched {len(context['prices'])} coins, "
          f"{len(context['news_headlines'])} headlines, "
          f"{len(context['trending_coins'])} trending coins.")
    return context


if __name__ == "__main__":
    ctx = fetch_all_market_context()
    print(json.dumps(ctx, indent=2))
