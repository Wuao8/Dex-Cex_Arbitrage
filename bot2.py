from price_provider import get_market_snapshot

print("SOLANA ARBITRAGE ENGINE v2 (STABLE ARCH)")

snapshot = get_market_snapshot()

for token, prices in snapshot.items():

    orca = prices["orca"]
    raydium = prices["raydium"]

    buy = min(orca, raydium)
    sell = max(orca, raydium)

    spread = ((sell - buy) / buy) * 100

    print(f"\nTOKEN: {token}")
    print(f"ORCA: {orca}")
    print(f"RAYDIUM: {raydium}")
    print(f"SPREAD: {spread:.2f}%")

    if spread > 1.0:
        print("🔥 OPPORTUNITÀ INTERESSANTE")
    else:
        print("❌ NO TRADE")
