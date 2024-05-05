def main():
    text = input("What time is it? ")
    time = convert(text)
    if 7<= time <= 8:
        print("breakfast time")
    elif 12<= time <= 13:
        print("lunch time")
    elif 18<= time <= 19:
        print("dinner time")

def convert(time):
    dot = time.find(":")
    return (float(time[:dot]) + (float(time[dot+1:]) / 60))

if __name__ == "__main__":
    main()
