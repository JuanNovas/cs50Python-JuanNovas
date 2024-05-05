text = input("Input: ")
vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
print("Output: ", end="")
for caracter in text:
    if caracter not in vowels:
        print(caracter, end="")
print("")
