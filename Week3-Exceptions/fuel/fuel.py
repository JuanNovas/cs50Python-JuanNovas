while True:
    fuel = input("Fraction: ")
    try:
        slash = fuel.find("/")
        percent = round(int(fuel[:slash]) / int(fuel[slash+1:]) * 100)
        if percent > 100:
            pass
        elif percent >= 99:
            print("F")
            break
        elif percent <= 1:
            print("E")
            break
        elif percent >= 0:
            print(f"{percent}%")
            break
    except:
        pass

