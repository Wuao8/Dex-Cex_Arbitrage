from price_provider import get_market_snapshot
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
import requests

print("CRYPTO OPPORTUNITY ENGINE V2 START")

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": msg,
        "parse_mode": "HTML"
    }
    requests.post(url, json=payload)


snapshot = get_market_snapshot()

opportunities = []

for token, prices in snapshot.items():

    cex = prices["cex"]
    dex = prices["dex"]

    if cex <= 0 or dex <= 0:
        continue

    spread = abs((cex - dex) / cex) * 100

    score = min(spread * 10, 100)

    if score < 70:
        continue

    opportunities.append({
        "token": token,
        "score": score,
        "spread": spread,
        "cex": cex,
        "dex": dex
    })

opportunities.sort(key=lambda x: x["score"], reverse=True)
top = opportunities[:3]

if not top:
    print("NO SIGNALS")
    exit()

msg = "🚨 <b>CRYPTO OPPORTUNITIES V2</b>\n\n"

for i, op in enumerate(top, 1):

    msg += (
        f"{i}. <b>{op['token']}</b>\n"
        f"Score: {op['score']:.1f}/100\n"
        f"Spread: {op['spread']:.2f}%\n"
        f"CEX: {op['cex']}\n"
        f"DEX: {op['dex']}\n\n"
    )

send_telegram(msg)
print(msg)
