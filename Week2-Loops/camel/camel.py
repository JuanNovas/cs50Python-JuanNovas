text = input("cameCase: ")

new_word = []

for caracter in text:
    if caracter.isupper():
        new_word.append("_")
        new_word.append(caracter.lower())
    else:
        new_word.append(caracter)

print("snake_case: ", end="")
for caracter in new_word:
    print(caracter, end="")
print("")
