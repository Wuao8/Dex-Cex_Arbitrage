import requests

print("Test connessione Jupiter Quote API...")

url = "https://quote-api.jup.ag/v6/quote"

params = {
    "inputMint": "So11111111111111111111111111111111111111112",  # SOL
    "outputMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", # USDC
    "amount": 100000000,  # 0.1 SOL (in lamports)
    "slippageBps": 50
}

response = requests.get(url, params=params, timeout=10)

print("Status Code:", response.status_code)
print("Response:")
print(response.text)
