def main():
    fuel = input("Fraction: ")
    print(gauge(convert(fuel)))


def convert(fuel):
    try:
        slash = fuel.find("/")
        percent = round(int(fuel[:slash]) / int(fuel[slash+1:]) * 100)
        if percent > 100:
            return 100
        elif percent < 0:
            return 0
        else:
            return percent
    except ValueError:
        return ValueError
    except ZeroDivisionError:
        return ZeroDivisionError

def gauge(percent):
    try:
        if percent >= 99:
            return ("F")
        elif percent <= 1:
            return ("E")
        elif percent >= 0:
            return (f"{percent}%")
    except TypeError:
        return TypeError

if __name__ == "__main__":
    main()
