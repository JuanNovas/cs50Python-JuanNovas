import random


def main():
    level = get_level()
    puntos = 0
    for i in range(10):
        intentos = 0
        x = generate_integer(level)
        y = generate_integer(level)
        r = x + y
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
            except:
                answer = 90000
            if answer != r:
                print("EEE")
                intentos += 1
                if intentos >= 3:
                    print(f"{x} + {y} = {r}")
                    break
            else:
                puntos += 1
                break
        print(f"Score: {puntos}")




def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in (1,2,3):
                return level
        except:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)


if __name__ == "__main__":
    main()
