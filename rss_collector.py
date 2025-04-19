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
            # タイトル・リンク
            title = entry.get("title", "")
            link = entry.get("link", "")

            # 要約候補（順にチェック）
            summary = (
                entry.get("content", [{}])[0].get("value", "") or  # 最も詳細
                entry.get("summary", "") or
                entry.get("description", "")
            )

            article = {
                "title": title,
                "summary": summary,
                "link": link,
                "published": entry.get("published", "")
            }
            all_articles.append(article)

    return all_articles

__all__ = ["fetch_all_articles"]
