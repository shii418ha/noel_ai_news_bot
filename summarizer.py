import openai
import os

# OpenAIクライアントを初期化
client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def summarize_article(title, summary, link, thumbnail=""):
    prompt = f"""
以下はAIに関する最新ニュースです。
これを Discord に投稿できるように、天才猫型Bot「ノエル」風に重要なポイントを1〜2文で簡潔に要約してください。

タイトル: {title}
本文: {summary}

出力形式の例：
【🐈ノエルのAI速報にゃ🐾】
・にゃんと！◯◯企業が新しいAIツールを発表したにゃん！
・政府がAI規制に向けた新法案を提出したんだってにゃ！
📎 詳しくはコチラにゃ ➡️ {link}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
        )

        summary_text = response.choices[0].message.content.strip()

        return {
            "title": title,
            "summary": summary_text,
            "link": link,
            "thumbnail": thumbnail  # 必要に応じて Discord 投稿側で使う
        }

    except Exception as e:
        print(f"❌ 要約エラー: {e}")
        return None
