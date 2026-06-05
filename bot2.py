import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from price_provider import get_market_snapshot


from price_provider import get_market_snapshot

print("SOLANA ARBITRAGE ENGINE v3 (TELEGRAM ENABLED)")

snapshot = get_market_snapshot()


def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    try:
        r = requests.post(url, data=payload, timeout=10)
        print("Telegram status:", r.status_code)
        print("Telegram response:", r.text)
    except Exception as e:
        print("Telegram ERROR:", e)




print("SOLANA ARBITRAGE ENGINE v4 (CLEAN MODE)")

snapshot = get_market_snapshot()

best_trade = None

for token, prices in snapshot.items():

    binance = prices["binance"]
    dex = prices["dex"]

    print(f"\nTOKEN: {token}")
    print(f"BINANCE: {binance}")
    print(f"DEX: {dex}")

    # spread reale tra mercati
    spread = (binance - dex) / dex

    spread_percent = spread * 100

    print(f"SPREAD: {spread_percent:.2f}%")

    # soglia minima per evitare rumore
    MIN_EDGE = 0.5

    if abs(spread_percent) > MIN_EDGE:

        direction = "DEX -> CEX" if binance > dex else "CEX -> DEX"

        net_signal = {
            "token": token,
            "binance": binance,
            "dex": dex,
            "spread": spread_percent,
            "direction": direction
        }

        if spread_percent > 0:
            print("POSSIBILE OPPORTUNITÀ (BUY DEX / SELL CEX)")
        else:
            print("POSSIBILE OPPORTUNITÀ (BUY CEX / SELL DEX)")

    else:
        print("NO TRADE (spread too small)")

    print(f"\nTOKEN: {token}")
    print(f"NET PROFIT: {net_profit_percent:.2f}%")

    if net_profit_percent > 0.5:

        trade = {
            "token": token,
            "net": net_profit_percent,
            "gross": gross_spread * 100,
            "buy": buy,
            "sell": sell,
            "orca": orca,
            "raydium": raydium
        }

        if best_trade is None or trade["net"] > best_trade["net"]:
            best_trade = trade

    else:
        print("NO TRADE (after fees)")


if best_trade:

    if best_trade["orca"] < best_trade["raydium"]:
        buy_dex = "ORCA"
        sell_dex = "RAYDIUM"
    else:
        buy_dex = "RAYDIUM"
        sell_dex = "ORCA"

    msg = (
        "TOP ARBITRAGE SIGNAL\n\n"
        f"TOKEN: {best_trade['token']}\n\n"
        f"BUY ON: {buy_dex}\n"
        f"SELL ON: {sell_dex}\n\n"
        f"NET PROFIT: {best_trade['net']:.2f}%\n"
        f"GROSS SPREAD: {best_trade['gross']:.2f}%\n\n"
        f"BUY PRICE: {best_trade['buy']}\n"
        f"SELL PRICE: {best_trade['sell']}"
    )

    print("\nSEND BEST SIGNAL")
    send_telegram(msg)

else:
    print("\nNO GOOD OPPORTUNITIES")
