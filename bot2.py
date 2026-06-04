import requests

print("JUPITER QUOTE ENGINE START")

url = "https://quote-api.jup.ag/v6/quote"

params = {
    "inputMint": "So11111111111111111111111111111111111111112",  # SOL
    "outputMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", # USDC
    "amount": 100000000,  # 0.1 SOL
    "slippageBps": 50
}

try:
    r = requests.get(url, params=params, timeout=10)
    print("STATUS:", r.status_code)
    print("RESPONSE:")
    print(r.text[:500])
except Exception as e:
    print("ERROR:", e)
