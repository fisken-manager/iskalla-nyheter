#!/usr/bin/env python3
"""
Iskalla Nyheter - RSS Fetcher
Hämtar nyheter från RSS-flöden (äntligen!)
"""

import feedparser
import json
import re
from datetime import datetime
from pathlib import Path

# RSS-källor för curling
RSS_SOURCES = {
    "google_news": "https://news.google.com/rss/search?q=curling&hl=sv&gl=SE&ceid=SE:sv",
    "thecurlingnews": "https://thecurlingnews.com/feed",  # om den finns
    # Kan lägga till fler
}

def fetch_rss(url, source_name):
    """Hämtar RSS-flöde"""
    try:
        feed = feedparser.parse(url)
        articles = []
        
        for entry in feed.entries[:10]:  # Senaste 10
            articles.append({
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "published": entry.get("published", ""),
                "summary": entry.get("summary", "")[:300],
                "source": source_name
            })
        
        return articles
    except Exception as e:
        print(f"❌ Fel vid hämtning av {source_name}: {e}")
        return []

def is_fresh(article, hours=48):
    """Kollar om artikeln är färsk"""
    # Förenklad check - i verkligheten skulle vi parsa datum
    return True  # Anta att RSS ger nya först

def main():
    print("🌑 Iskalla Nyheter - RSS Fetcher")
    print("=" * 40)
    
    all_articles = []
    
    for source_name, url in RSS_SOURCES.items():
        print(f"\n🔍 Hämtar från {source_name}...")
        articles = fetch_rss(url, source_name)
        print(f"   Hittade {len(articles)} artiklar")
        all_articles.extend(articles)
    
    # Spara resultat
    output = {
        "fetched_at": datetime.now().isoformat(),
        "total": len(all_articles),
        "articles": all_articles
    }
    
    output_path = Path("/tmp/rss_articles.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Sparade {len(all_articles)} artiklar till {output_path}")
    
    # Visa de senaste
    print("\n📰 Senaste nyheter:")
    for art in all_articles[:5]:
        print(f"\n   {art['title'][:60]}...")
        print(f"   Källa: {art['source']}")

if __name__ == "__main__":
    main()
