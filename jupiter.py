import requests

JUPITER_QUOTE_URL = "https://quote-api.jup.ag/v6/quote"

def get_quote(input_mint, output_mint, amount, slippage_bps=50):
    """
    Fetch real price quote from Jupiter API
    """

    params = {
        "inputMint": input_mint,
        "outputMint": output_mint,
        "amount": amount,
        "slippageBps": slippage_bps
    }

    try:
        response = requests.get(JUPITER_QUOTE_URL, params=params, timeout=10)

        if response.status_code != 200:
            print("ERROR: status code", response.status_code)
            return None

        data = response.json()

        # Jupiter returns routes, we take best outAmount
        best_route = data.get("data", [None])[0]

        if not best_route:
            print("No route found")
            return None

        out_amount = best_route.get("outAmount")

        return {
            "in_amount": amount,
            "out_amount": out_amount,
            "route": best_route
        }

    except Exception as e:
        print("Jupiter error:", e)
        return None
