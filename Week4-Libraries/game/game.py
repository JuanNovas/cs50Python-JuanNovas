import random

while True:
    try:
        level = input("Level: ")
        level = int(level)
        if level > 0:
            break
    except:
        pass

number = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess == number:
            break
        elif guess > number:
            print("Too large!")
        elif guess < number:
            print("Too small!")
    except:
        pass

print("Just right!")
