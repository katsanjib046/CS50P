import requests
import sys

def main():
    try:
        n = float(sys.argv[1]) # number of bitcoin to be bought from the command-line-argument
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line arguemtn is not a number")
    rate = get_bitcoin_price() # current market rate
    amount = n*rate
    print(f"${amount:,.4f}")


def get_bitcoin_price():
    try:
        price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        out = price.json() # this is a dictionary
        rate = out["bpi"]["USD"]["rate"] # this is a string
        return float(rate.replace(',', ''))
    except requests.RequestException:
        sys.exit()



#########
if __name__ == "__main__":
    main()