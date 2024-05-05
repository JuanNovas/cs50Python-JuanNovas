def main():
    text = input("Greeting:" ).lower().strip()
    print(f"${str(value(text))}")


def value(text):
    text = text.lower().strip()
    if text[:5] == "hello":
        return 0
    elif text[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
