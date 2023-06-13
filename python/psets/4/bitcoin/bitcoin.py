import requests
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoin = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response = response.json()
    except (requests.RequestException, requests.exceptions.JSONDecodeError):
        pass
    else:
        price = response["bpi"]["USD"]["rate_float"] * bitcoin
        print(f"${price:,.4f}")


if __name__ == "__main__":
    main()
