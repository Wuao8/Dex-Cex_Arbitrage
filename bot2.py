import requests

print("TEST JUPITER STABLE CONNECTION...")

urls = [
    "https://api.github.com",
    "https://price.jup.ag",
    "https://jup.ag"
]

for url in urls:
    try:
        r = requests.get(url, timeout=10)
        print(url, "->", r.status_code)
    except Exception as e:
        print(url, "-> ERROR:", e)
