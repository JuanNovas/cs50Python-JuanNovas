
names = []

try:
    while True:
        text = input("Name:")
        names.append(text)
except:
    print(f"Adieu, adieu, to {names[0]}", end="")
    if len(names) > 2:
        print(",", end="")
        for name in names[1:-1]:
            print(f" {name},", end="")
    if len(names) > 1:
        print(f" and {names[-1]}")


