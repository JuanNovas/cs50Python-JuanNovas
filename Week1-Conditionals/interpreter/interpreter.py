text = input("Exrepssion: ")

symbols = ["+", "-", "*", "/"]

for symbol in symbols:
    a = text.find(symbol)
    if a != -1:
        c = text[a]
        break

match c:
    case "+":
        print(float(text[:a-1]) + float(text[a+2:]))
    case "-":
        print(float(text[:a-1]) - float(text[a+2:]))
    case "*":
        print(float(text[:a-1]) * float(text[a+2:]))
    case "/":
        print(float(text[:a-1]) / float(text[a+2:]))
