import requests
import os

DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

def post_to_discord(summary_data):
    embed = {
        "title": summary_data["title"],
        "description": summary_data["summary"],
        "url": summary_data["link"]
    }

    if summary_data.get("thumbnail"):
        embed["image"] = {"url": summary_data["thumbnail"]}

    content = {"embeds": [embed]}

    response = requests.post(DISCORD_WEBHOOK_URL, json=content)
    response.raise_for_status()
