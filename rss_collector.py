import json
import feedparser

def load_rss_list(path="rss_list.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def fetch_all_articles():
    rss_list = load_rss_list()
    all_articles = []

    for rss_url in rss_list:
        feed = feedparser.parse(rss_url)
        for entry in feed.entries:
            thumbnail = (
                entry.get("media_thumbnail", [{}])[0].get("url")
                or entry.get("media_content", [{}])[0].get("url")
                or entry.get("image", {}).get("url")
                or ""
            )
            article = {
                "title": entry.get("title", ""),
                "summary": entry.get("summary", entry.get("description", "")),
                "link": entry.get("link", ""),
                "published": entry.get("published", ""),
                "thumbnail": thumbnail
            }
            all_articles.append(article)

    return all_articles

__all__ = ["fetch_all_articles"]
