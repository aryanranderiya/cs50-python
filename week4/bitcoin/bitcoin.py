import requests
import json
import sys

try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")

    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")
    else:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response_json = response.json()

        amount = float(response_json["bpi"]["USD"]["rate"].replace(",", ""))

        amount = amount * float(sys.argv[1])
        print(f"${amount:,.4f}")

except IndexError:
    pass
except requests.RequestException:
    pass
