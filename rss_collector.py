import feedparser

# 読み込むRSSフィードのリスト（今は仮）
RSS_FEEDS = [
    "https://openai.com/blog/rss.xml",
    "https://ai.googleblog.com/feeds/posts/default",
    "https://huggingface.co/blog/rss",
]

def fetch_latest_articles():
    articles = []
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:  # 最新3件だけ取得
            article = {
                "title": entry.title,
                "link": entry.link,
                "summary": entry.summary if "summary" in entry else "",
                "published": entry.published if "published" in entry else "",
                "source": url
            }
            articles.append(article)
    return articles

if __name__ == "__main__":
    data = fetch_latest_articles()
    for item in data:
        print(f"\n📰 {item['title']}\n🔗 {item['link']}\n📅 {item['published']}")
