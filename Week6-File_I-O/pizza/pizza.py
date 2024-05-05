import csv
import tabulate
import sys

try:
    if sys.argv[1][-4:] != ".csv":
        sys.exit("Not a csv file")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")



    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        print(tabulate.tabulate(reader,headers="firstrow", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
except ValueError:
    sys.exit("Too few command-line arguments")

