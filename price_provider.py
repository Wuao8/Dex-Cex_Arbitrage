import random

# --- MOCK PRICES (sempre disponibili) ---
MOCK_PRICES = {
    "SOL": 100.0,
    "JUP": 0.75,
    "BONK": 0.00002
}

def get_price(token, mode="mock"):
    """
    Returns price for token.
    mode:
        - mock = always works
        - live = future integration (Jupiter etc.)
    """

    if mode == "mock":
        return MOCK_PRICES.get(token)

    # LIVE MODE (disabled for now, fallback safe)
    # We keep structure ready for Jupiter / Orca / Raydium
    try:
        # placeholder for future API calls
        return MOCK_PRICES.get(token)
    except:
        return MOCK_PRICES.get(token)


def get_market_snapshot():
    """
    Simulates market snapshot across DEXs
    (later replaced with real Orca/Raydium data)
    """

    snapshot = {}

    for token in MOCK_PRICES.keys():
        base = MOCK_PRICES[token]

        snapshot[token] = {
            "orca": round(base * random.uniform(0.99, 1.02), 6),
            "raydium": round(base * random.uniform(0.98, 1.03), 6)
        }

    return snapshot
