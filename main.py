import requests

response = requests.get(
    "https://api.freecurrencyapi.com/v1/latest?apikey=YOUR-APIKEY"
    params={"apikey": "fca_live_vhEdvpyiOAQFGVunV2OtY5puuSAQEREhL7rQXpWt",
            "base_currency": "BRL",
            "currencies": "USD,EUR,JPY"
            }
)

print(response.status_code)
print(response)