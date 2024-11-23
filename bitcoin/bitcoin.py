import requests
import sys

# Try to convert the command-line argument to a float and handle errors
try:
    n = float(sys.argv[1].replace(",", "."))
except IndexError:
    # Handle the case when there's no command-line argument
    print("Error: Missing command-line argument")
    sys.exit(1)
except ValueError:
    # Handle the case when the command-line argument is not a valid number
    print("Error: Command-line argument is not a valid number")
    sys.exit(1)

# Check if n is a positive number
if n > 0:
    try:
        # Fetch the current Bitcoin price from the CoinDesk API
        current = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
        # Calculate the Bitcoin price based on the rate_float and n
        price = float(current["bpi"]["USD"]["rate_float"] * n)
        # Print the calculated Bitcoin price with proper formatting
        print(f"Bitcoin: ${price:,.4f}")

