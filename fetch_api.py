# fetch_api.py
import requests, json

url = "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd"
data = requests.get(url).json()

print("Current SOL price (USD):", data["solana"]["usd"])

with open("price.json", "w") as f:
    json.dump(data, f, indent=2)
