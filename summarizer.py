import openai
import os

client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def summarize_article(title, summary, link, thumbnail=""):
    prompt = f"""
以下はAIに関する最新ニュースにゃ。
これを Discord に投稿できるように、天才猫型Bot「ノエル」風に要点を**5つ**、箇条書きでかんたんに解説してにゃ。
ポイントは、
- 記事の重要な内容をちゃんと拾って、
- ノエルらしいちょっとゆる〜い語り口で、
- でも内容はわかりやすくしてにゃ！

【元タイトル】  
{title}

【本文（要約用）】  
{summary}

【リンク】  
{link}

【出力例（口調の雰囲気）】
【🐈ノエルのAI速報にゃ！】
・◯◯っていうAIが新しく発表されたらしいにゃ〜  
・人間のお仕事がまたひとつラクになるかも…！？  
・〇〇社が開発したこの技術、注目度バツグンにゃ！  
・業界の常識がひっくり返るかもって話もあるんだにゃ〜  
🐾詳しくはリンクをチェックにゃ → {link}

本文はこちらのURLにゃ ➡️ {link}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=400
        )

        summary_text = response.choices[0].message.content.strip()

        return {
            "title": title,
            "summary": summary_text,
            "link": link,
            "thumbnail": thumbnail
        }

    except Exception as e:
        print(f"❌ 要約エラー: {e}")
        return None
