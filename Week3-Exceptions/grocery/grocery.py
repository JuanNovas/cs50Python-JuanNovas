items = {}

while True:
    try:
        x = input("").lower()
        try:
            items[x] += 1
        except:
            items[x] = 1
    except EOFError:
        try:
            x = []
            for item in items:
                x.append(item)
            x.sort()
            for item in x:
                print(f"{items[item]} {item.upper()}")

            break
        except:
            break
