import requests

BINANCE_URL = "https://api.binance.com/api/v3/ticker/price"

TOKENS = {
    "BNB": "BNBUSDT",
    "CAKE": "CAKEUSDT",
    "ETH": "ETHUSDT"
}


def get_binance_price(symbol):
    try:
        r = requests.get(BINANCE_URL, params={"symbol": symbol}, timeout=10)
        return float(r.json()["price"])
    except:
        return None


def get_pancake_price(symbol):
    """
    Lightweight DEX price via DexScreener (stable, works instantly)
    """
    try:
        url = f"https://api.dexscreener.com/latest/dex/tokens/{symbol}"
        r = requests.get(url, timeout=10)
        data = r.json()

        pair = data["pairs"][0]
        return float(pair["priceUsd"])

    except:
        return None


def get_market_snapshot():

    snapshot = {}

    for token, symbol in TOKENS.items():

        cex = get_binance_price(symbol)
        dex = get_pancake_price(symbol)

        if not cex or not dex:
            continue

        snapshot[token] = {
            "binance": cex,
            "dex": dex
        }

    print("BNB ARBITRAGE SNAPSHOT READY")

    return snapshot
