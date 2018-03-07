import requests

url = 'https://api.coinmarketcap.com/v1/ticker/'
response = requests.get(url, headers={"Accept": "application/json"}).json()
print(response)
for i in response[0:21]:
    print(f"Current price of {i['id'].title()}: {i['price_usd']} USD.")
