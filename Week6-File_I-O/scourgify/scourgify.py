import sys
import csv
try:

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    with open(sys.argv[1], "r") as file1, open(sys.argv[2], "w") as file2:
        reader = csv.DictReader(file1)
        writer = csv.writer(file2)
        writer.writerow(["first","last","house"])
        for row in reader:
            coma = row["name"].find(",")
            writer.writerow([row["name"][coma+2:], row["name"][:coma], row["house"]])


except ValueError:
    sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
