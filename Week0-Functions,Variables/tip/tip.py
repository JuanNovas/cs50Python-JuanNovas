def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dot = d.find(".")
    a = int(d[1:dot])
    return a + (int(d[-2:])/100)


def percent_to_float(p):
    return int(p[:-1])/100


main()
