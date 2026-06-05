import requests

BINANCE_URL = "https://api.binance.com/api/v3/ticker/price"

# Jupiter PRICE API CORRETTA (ATTUALE)
JUPITER_URL = "https://api.jup.ag/price/v2"

TOKENS = {
    "SOL": {
        "binance": "SOLUSDT",
        "jupiter": "So11111111111111111111111111111111111111112"
    },
    "JUP": {
        "binance": "JUPUSDT",
        "jupiter": "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"
    },
    "BONK": {
        "binance": "BONKUSDT",
        "jupiter": "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263"
    }
}


def get_binance_price(symbol):
    try:
        r = requests.get(BINANCE_URL, params={"symbol": symbol}, timeout=10)
        data = r.json()
        return float(data["price"])
    except Exception as e:
        print("BINANCE ERROR:", e)
        return None


def get_jupiter_price(mint):
    try:
        r = requests.get(JUPITER_URL, params={"ids": mint}, timeout=10)
        data = r.json()

        return float(data["data"][mint]["price"])
    except Exception as e:
        print("JUPITER ERROR:", e)
        return None


def get_market_snapshot():

    snapshot = {}

    for token, addrs in TOKENS.items():

        binance_price = get_binance_price(addrs["binance"])
        jupiter_price = get_jupiter_price(addrs["jupiter"])

        if binance_price is None or jupiter_price is None:
            continue

        snapshot[token] = {
            "binance": binance_price,
            "dex": jupiter_price
        }

    print("CEX vs DEX SNAPSHOT LOADED")

    return snapshot
