from jupiter import get_quote

print("SOLANA ARBITRAGE ENGINE v1 (LIVE DATA)")

# --- TOKEN MINTS ---
TOKENS = {
    "SOL": "So11111111111111111111111111111111111111112",
    "USDC": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"
}

# --- CONFIG ---
AMOUNT = 100000000  # 0.1 SOL

# --- GET REAL PRICE ---
quote = get_quote(
    TOKENS["SOL"],
    TOKENS["USDC"],
    AMOUNT
)

if quote:
    in_amount = quote["in_amount"]
    out_amount = quote["out_amount"]

    price = int(out_amount) / int(in_amount)

    print("\nLIVE PRICE DATA")
    print("INPUT (lamports):", in_amount)
    print("OUTPUT (USDC base units):", out_amount)
    print("PRICE SOL -> USDC:", price)

else:
    print("Failed to fetch quote")
