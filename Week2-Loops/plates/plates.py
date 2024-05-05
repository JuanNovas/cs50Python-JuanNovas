def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if 2 <= len(plate) <= 6 and plate[:2].isalpha() and plate.isalnum():

        for i in range(len(plate)):
            if plate[i].isnumeric():
                position = i
                break
        try:
            if plate[position] == "0":
                return False

            for caracter in plate[position:]:
                if caracter.isalpha():
                    return False
        except:
            pass

        return True
    else:
        return False


main()
