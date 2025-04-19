from rss_collector import fetch_all_articles
from summarizer import summarize_article
from discord_poster import post_to_discord
from posted_tracker import load_posted_urls, save_posted_url
import json
from datetime import datetime
import dateutil.parser  # 必要なら requirements.txt に `python-dateutil` を追記


# 記事の公開日が最近かどうかを判定
def is_recent(published_str, threshold_minutes=1440):
    try:
        published_dt = dateutil.parser.parse(published_str)
        return (datetime.utcnow() - published_dt).total_seconds() < threshold_minutes * 60
    except Exception:
        return False


def run():
    raw_articles = fetch_all_articles()
    print(f"💡 取得記事数（フィルター前）: {len(raw_articles)}")

    # 新しい順に並べ替え → 時間でフィルター
    articles = sorted(raw_articles, key=lambda x: x.get("published", ""), reverse=True)
    articles = [a for a in articles if is_recent(a.get("published", ""), 1440)]
    print(f"💡 取得記事数（フィルター後）: {len(articles)}")

    posted_urls = load_posted_urls()
    posted_this_time = 0

    print(f"📰 最新記事取得: {len(articles)}件 / 投稿済み: {len(posted_urls)}件")

    for article in articles:
        title = article["title"]
        link = article["link"]
        published = article["published"]
        summary_raw = article.get("summary", "")

        print("========================================")
        print(f"🔍 記事確認: {title}")
        print(f"📅 投稿日: {published}")
        print(f"🔗 リンク: {link}")
        print(f"📝 サマリー元: {'（あり）' if summary_raw else '（なし）'}")

        if link in posted_urls:
            print(f"⏭️ スキップ理由: 既に投稿済み")
            continue

        if not is_recent(published, 120):
            print(f"⏭️ スキップ理由: 古い記事")
            continue

        summary = summarize_article(title, summary_raw, link)
        if not summary:
            print(f"⚠️ 要約失敗 or 空なのでスキップ")
            continue

        print("📤 投稿送信！")
        post_to_discord(summary)
        save_posted_url(link)
        posted_this_time += 1
        print(f"✅ 投稿完了: {title}")

    print(f"📦 投稿件数（今回）: {posted_this_time}件")


if __name__ == "__main__":
    run()
