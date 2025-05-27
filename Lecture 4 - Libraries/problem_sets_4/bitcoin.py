import locale
import requests
import sys

locale.setlocale(locale.LC_NUMERIC)

try:
    bitcoin = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=3116929d48acecb10d1eab25d22cc96f8d3457deb5c9c6be885dfbf834fccba3")
    # print(type(requests.get(bitcoin)))
    # print(bitcoin)
    # print(bitcoin.json())
    # print(type(bitcoin.json()))
    # print(bitcoin.json()["data"]["priceUsd"])
    rate = float(bitcoin.json()["data"]["priceUsd"])
    # print(type(rate))

    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
        # print(type(n))
        # print(f"{n:,.4f}")
        price = n * rate
        print(f"{price:,.4f}", sep="")

        
    except ValueError:
        sys.exit("Command-line argument is not a number")

except requests.RequestException:
    sys.exit("Request error")

# rest.coincap.io/v3/assets/bitcoin?apiKey=3116929d48acecb10d1eab25d22cc96f8d3457deb5c9c6be885dfbf834fccba3