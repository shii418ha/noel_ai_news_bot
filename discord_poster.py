import os
import requests

DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

def post_to_discord(news_item):
    if not DISCORD_WEBHOOK_URL:
        print("❌ DISCORD_WEBHOOK_URL が未設定だよ！")
        return

    embed = {
        "title": news_item["title"],
        "description": news_item["summary"],
        "url": news_item["link"],
        "color": 0x00BFFF,  # 空色っぽいノエルカラー🎨
    }

    # サムネがあれば追加
    if news_item.get("thumbnail"):
        embed["thumbnail"] = {
            "url": news_item["thumbnail"]
        }

    data = {
        "username": "ノエル速報bot",
        "avatar_url": "https://i.imgur.com/dg4FQjv.png",  # 任意のアイコンURLに変更OK
        "embeds": [embed]
    }

    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=data)
        response.raise_for_status()
        print(f"✅ Discord投稿成功: {news_item['title']}")
    except Exception as e:
        print(f"❌ Discord投稿失敗: {e}")
