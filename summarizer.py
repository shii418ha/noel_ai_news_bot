import openai
import os

client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def summarize_article(title, summary, link, thumbnail=""):
    prompt = f"""
以下はAI関連のニュース記事本文です。この内容から重要なポイントを5つ、簡潔に箇条書きでまとめてください。
内容を正確に抽出し、表現はわかりやすく整えてください。
タイトルや記事全体の要約ではなく、**具体的な内容のポイント抽出**にしてください。

【記事タイトル】
{title}

【記事本文】
{summary}

【出力形式】
- 箇条書き1
- 箇条書き2
- 箇条書き3
- 箇条書き4
- 箇条書き5
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
        )

        points = response.choices[0].message.content.strip()

        summary_text = f"""【🐾ノエルのAI速報にゃ！】
{points}
📎 詳しくはこちら ➡️ {link}"""

        return {
            "title": title,
            "summary": summary_text,
            "link": link,
            "thumbnail": thumbnail,
        }

    except Exception as e:
        print(f"❌ 要約エラー: {e}")
        return None
