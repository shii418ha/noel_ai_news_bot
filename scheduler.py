from rss_collector import fetch_all_articles
from summarizer import summarize_article
from discord_poster import post_to_discord
from posted_tracker import load_posted_urls, save_posted_url

from datetime import datetime
import dateutil.parser
import json

# -------------------------------
# 投稿対象となる記事の「新しさ」条件（分単位）
# -------------------------------
FILTER_MINUTES = 2880  # ← 例：24時間以内の記事

def is_recent(published_str, threshold_minutes=FILTER_MINUTES):
    try:
        published_dt = dateutil.parser.parse(published_str)
        return (datetime.utcnow() - published_dt).total_seconds() < threshold_minutes * 60
    except Exception:
        return False

def run():
    raw_articles = fetch_all_articles()
    print(f"🟡 取得記事数（フィルター前）: {len(raw_articles)}")

    # 🔽 新しい順にソート
    articles = sorted(raw_articles, key=lambda x: x.get("published", ""), reverse=True)

    # 🔽 フィルター処理（しきい値超えたらコメントアウトで無効化OK）
    articles = [a for a in articles if is_recent(a.get("published", ""), FILTER_MINUTES)]

    print(f"🟡 取得記事数（フィルター後）: {len(articles)}")

    posted_urls = load_posted_urls()
    posted_this_time = 0

    print(f"📰 最新記事取得: {len(articles)}件 / 投稿済み: {len(posted_urls)}件")

    for article in articles:
        print("=================================")
        print(f"📄 タイトル: {article.get('title', '(不明)')}")
        print(f"📎 リンク: {article.get('link', '(不明)')}")
        print(f"🗓 投稿日: {article.get('published', '(不明)')}")
        print(f"📝 サマリー: {article.get('summary', '（なし）')}")
        print("=================================")

        if article["link"] in posted_urls:
            print(f"⏭️ スキップ: {article['title']}")
            continue

        summary = summarize_article(article["title"], article["summary"], article["link"])
        if not summary:
            print(f"⚠️ 要約失敗: {article['title']}")
            continue

        post_to_discord(summary)
        save_posted_url(article["link"])
        posted_this_time += 1

        print(f"✅ 投稿完了: {article['title']}")

    print(f"📦 投稿件数（今回）: {posted_this_time}件")

if __name__ == "__main__":
    run()
