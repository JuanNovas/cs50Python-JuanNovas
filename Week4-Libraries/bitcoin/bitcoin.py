import sys
import requests

try:
    n = float(sys.argv[1])
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r = r.json()
    r = r["bpi"]["USD"]["rate"]
    r = r.replace(",","")
    amount = n * float(r)
    print(f"${amount:,.4f}")
except IndexError:
    sys.exit("Missing command-line argument")

except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    pass
