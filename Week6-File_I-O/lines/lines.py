import sys

n_lines = 0
try:
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1][-3:] != ".py":
        sys.exit("Not a python file")
    with open(sys.argv[1], "r") as file:
        for row in file:
            if len(row.strip()) != 0 and row.strip()[0] != "#":
                n_lines += 1
        print(n_lines)
except ValueError:
    sys.exit("Too few command-line arguments")


