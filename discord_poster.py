import os
import requests
from dotenv import load_dotenv

load_dotenv()
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def post_to_discord(content: str):
    data = {
        "content": content
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("✅ Discordに投稿成功！")
    else:
        print(f"❌ 投稿失敗！ステータスコード: {response.status_code}")
        print(response.text)

# テスト用
if __name__ == "__main__":
    test_message = """
【🧠 AI速報にゃ！】
◤ OpenAI、新モデルGPT-4oをリリースにゃ ◢

GPT-4oはテキスト、画像、音声を同時に処理できるスーパーにゃんこモデルにゃ！
応答速度もアップして、にゃんともすごい進化なのにゃ！

📎 https://openai.com/index/gpt-4o

Powered by 🐾 N.O.E.L.
"""
    post_to_discord(test_message)
