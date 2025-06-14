import requests
import sys

try:
    if len(sys.argv) > 1:
        value = float(sys.argv[1])
        url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=059077a6cd224b83aee6516264bb7bb40991e6457e50de151de7273d495daaca"
        result = requests.get(url)
        response = result.json()
        price = float(response['data']['priceUsd'])
        amount = price * float(sys.argv[1])
        print(f"${amount:,.4f}")
    else:
        sys.exit("Missing command-line argument")
except requests.RequestException:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
