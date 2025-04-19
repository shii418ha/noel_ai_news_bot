import json

# 作成するRSSリストの候補
rss_feeds = [
    # ✅ 国内
    "https://www.itmedia.co.jp/rss/ai_plus.xml",  # ITmedia AI+ のRSS（https://www.itmedia.co.jp/aiplus/）

    # ✅ ニュースプラットフォームのAIカテゴリ
    "https://news.google.com/rss/search?q=AI&hl=ja&gl=JP&ceid=JP:ja",  # Googleニュース「AI」カテゴリ（日本語）
    "https://news.yahoo.co.jp/rss/topics/it.xml",  # YahooニュースITカテゴリ（AI特化ではないが関連多し）

    # ✅ 海外インフルエンサー系（Substack経由など）
    "https://www.bensbites.co/feed",             # Ben's Bites（Substack）
    "https://tldr.tech/ai/rss.xml",              # TLDR AI
    "https://www.aibreakfast.com/feed",          # AI Breakfast（週刊）

    # 🔍 まだRSS見つかってないが候補にしたい（コメントアウト中）
    # "https://www.therundown.ai/rss",           # Rowan Cheung（The Rundown AI）※RSS未確認
    # "https://www.aivalley.substack.com/feed",  # Nathan Lands（AI Valley）※RSS確認要
    # "https://www.paulsnewsletter.com/rss",     # Paul Couvert（仮）※RSS要確認
]

# 保存用JSONとしてエクスポート
rss_list_json = json.dumps(rss_feeds, indent=2, ensure_ascii=False)
rss_list_json
