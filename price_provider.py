import requests

MEXC_TICKER_URL = "https://api.mexc.com/api/v3/ticker/price"
MEXC_24H_URL = "https://api.mexc.com/api/v3/ticker/24hr"

DEXSCREENER_URL = "https://api.dexscreener.com/latest/dex/search?q="


def get_top_mexc_symbols(limit=100):
    try:
        r = requests.get(MEXC_24H_URL, timeout=10)
        data = r.json()

        sorted_data = sorted(
            data,
            key=lambda x: float(x.get("quoteVolume", 0)),
            reverse=True
        )

        symbols = []
        for item in sorted_data:
            symbol = item["symbol"]
            if symbol.endswith("USDT"):
                base = symbol.replace("USDT", "")
                symbols.append(base)

            if len(symbols) >= limit:
                break

        return symbols

    except Exception as e:
        print("MEXC TOP ERROR:", e)
        return []


def get_mexc_price(symbol):
    try:
        r = requests.get(MEXC_TICKER_URL, timeout=10)
        data = r.json()

        for item in data:
            if item["symbol"] == symbol + "USDT":
                return float(item["price"])

        return None

    except Exception as e:
        print("MEXC PRICE ERROR:", e)
        return None


def get_dex_price(symbol):
    try:
        r = requests.get(DEXSCREENER_URL + symbol, timeout=10)
        data = r.json()

        pairs = data.get("pairs", [])
        if not pairs:
            return None

        best = max(pairs, key=lambda x: float(x.get("liquidity", {}).get("usd", 0)))
        return float(best["priceUsd"])

    except Exception as e:
        print("DEX ERROR:", e)
        return None


def get_market_snapshot():
    snapshot = {}

    symbols = get_top_mexc_symbols(100)

    for symbol in symbols:

        cex = get_mexc_price(symbol)
        dex = get_dex_price(symbol)

        if cex is None or dex is None:
            continue

        snapshot[symbol] = {
            "cex": cex,
            "dex": dex
        }

        print(symbol, "OK")

    return snapshot
