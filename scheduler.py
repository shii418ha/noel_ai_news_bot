from summarizer import summarize_article
from discord_poster import post_to_discord

def run():
    test_article = {
        "title": "OpenAI、新モデルGPT-4oをリリース",
        "summary": "GPT-4oはテキスト、画像、音声を同時に処理できるマルチモーダルモデル。応答速度も大幅向上。",
        "link": "https://openai.com/index/gpt-4o"
    }
    summary = summarize_article(
        test_article["title"],
        test_article["summary"],
        test_article["link"]
    )
    post_to_discord(summary)

if __name__ == "__main__":
    run()
