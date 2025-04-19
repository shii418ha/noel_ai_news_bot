from rss_collector import fetch_all_articles
from summarizer import summarize_article
from discord_poster import post_to_discord
from posted_tracker import load_posted_urls, save_posted_url
import json
from datetime import datetime, timezone
import dateutil.parser
import os

if os.getenv("STOP_NOW") == "1":
    print("🔕 自動実行停止モードです。")
    exit()
    
# 記事の公開日が最近かどうかを判定
def is_recent(published_str, threshold_minutes=2880):  # ← 2日分（48時間）
    try:
        published_dt = dateutil.parser.parse(published_str)

        # タイムゾーンが無ければUTCと仮定
        if published_dt.tzinfo is None:
            published_dt = published_dt.replace(tzinfo=timezone.utc)

        now_utc = datetime.now(timezone.utc)
        return (now_utc - published_dt).total_seconds() < threshold_minutes * 60
    except Exception as e:
        print(f"❌ 日付変換エラー: {published_str} / {e}")
        return False

def run():
    raw_articles = fetch_all_articles()
    print(f"🟡 取得記事数（フィルター前）: {len(raw_articles)}")

    articles = sorted(raw_articles, key=lambda x: x.get("published", ""), reverse=True)
    articles = [a for a in articles if is_recent(a.get("published", ""), 2880)]

    print(f"🟡 取得記事数（フィルター後）: {len(articles)}")

    # --- デバッグ: 取得した全記事の中身を見たいときはコメントアウト解除 ---
    # for a in raw_articles:
    #     print(json.dumps(a, indent=2, ensure_ascii=False))

    posted_urls = load_posted_urls()
    posted_this_time = 0

    print(f"📰 最新記事取得: {len(articles)}件 / 投稿済み: {len(posted_urls)}件")

    for article in articles:
        print(f"🔍 記事確認: {article['title']} / 投稿日: {article['published']}")

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
