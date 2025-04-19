import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def summarize_article(title: str, summary: str, link: str) -> str:
    prompt = f"""
以下はAIに関する最新ニュースです。
これを Discord に投稿できるように、天才猫型Bot「ノエル」風の文章にまとめてください。

# ニュース記事
タイトル: {title}
本文要約: {summary}

# 出力フォーマット
【🧠 AI速報にゃ！】
◤ {title} ◢

📌 要点をにゃんこ口調で簡潔に！
📎 詳しくはこちら ➡️ {link}

Powered by 🐾 N.O.E.L.
    """

    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "あなたは明るく知的な天才猫型AIです。ニュース要約が得意です。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )

    return chat_completion.choices[0].message.content

# テスト
if __name__ == "__main__":
    test = summarize_article(
        "OpenAI、新モデルGPT-4oをリリース",
        "GPT-4oはテキスト、画像、音声を同時に処理できるマルチモーダルモデル。応答速度も大幅向上。",
        "https://openai.com/index/gpt-4o"
    )
    print(test)
