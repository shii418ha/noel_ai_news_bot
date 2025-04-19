from rss_collector import fetch_all_articles
from summarizer import summarize_article
from discord_poster import post_to_discord

def run():
    articles = fetch_all_articles()

    # 記事が1件も取れなかったら終了
    if not articles:
        print("記事が見つかりませんでした。")
        return

    # 今回はとりあえず最新の1件だけ投稿
    article = articles[0]

    summary = summarize_article(
        article["title"],
        article["summary"],
        article["link"]
    )

    post_to_discord(summary)

if __name__ == "__main__":
    run()
