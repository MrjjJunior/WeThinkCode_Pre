import requests
import os
import sys
'''
 user inputs number of bitcoins and the price is presented 
'''

api_key = os.getenv("API_KEY")

def main():

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        number_of_bitcoin = float(sys.argv[1])
        price = get_bitcoin_price(number_of_bitcoin)
    except ValueError:
        sys.exit("Command-line argument is not a number")


def get_bitcoin_price(number_of_bitcoin):
    try:
        # get info in json format 
        response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}")
        data = response.json()
        # filter info 
        price = float(data['data']['priceUsd']) * number_of_bitcoin
        print(f"${price: ,.4f}")
    except requests.RequestException:
        sys.exit("404: Reqeust Failed")



if __name__ == "__main__":
    main()

