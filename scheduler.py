from rss_collector import fetch_latest_articles
from summarizer import summarize_article
from discord_poster import post_to_discord

def run():
    articles = fetch_latest_articles()
    for article in articles[:1]:  # まずは最新1件だけ
        summary = summarize_article(
            article["title"],
            article["summary"],
            article["link"]
        )
        post_to_discord(summary)

if __name__ == "__main__":
    run()
