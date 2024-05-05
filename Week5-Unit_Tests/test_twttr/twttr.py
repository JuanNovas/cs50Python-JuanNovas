def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    new_word = ""
    for caracter in word:
        if caracter not in vowels:
            new_word = new_word + caracter
    return new_word


if __name__ == "__main__":
    main()
