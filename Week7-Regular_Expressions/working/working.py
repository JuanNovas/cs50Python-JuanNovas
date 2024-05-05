import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()
    x = s.index("to")
    first = s[:x]
    second = s[x+3:]
    dd = first.find(":")

    s.index(" AM")
    s.index(" PM")

    if dd != -1:
        firstNum = re.search("^\\d*:\\d\\d",first)
        if len(firstNum.group()) == 4:
            firstNum = "0" + firstNum.group()
        else:
            firstNum = firstNum.group()
    else:
        firstNum = re.search("^\\d*",first)
        if len(firstNum.group()) == 1:
            firstNum = "0" + firstNum.group() + ":00"
        else:
            firstNum = firstNum.group() + ":00"


    dd = second.find(":")
    if dd != -1:
        secondNum = re.search("^\\d*:\\d\\d",second)
        if len(secondNum.group()) == 4:
            secondNum = "0" + secondNum.group()
        else:
            secondNum = secondNum.group()
    else:
        secondNum = re.search("^\\d*",second)
        if len(secondNum.group()) == 1:
            secondNum = "0" + secondNum.group() + ":00"
        else:
            secondNum = secondNum.group() + ":00"

    if int(firstNum[:2]) > 12 or int(secondNum[:2]) > 12:
        s.index("oihfehoifwhiofwe")
    elif int(firstNum[3:]) >= 60 or int(firstNum[3:]) >= 60:
        s.index("oihfehoifwhiofwe")

    if l := re.search("AM",first):
        if int(firstNum[:2]) == 12:
            firstNum = "00" + firstNum[2:]
        if int(secondNum[:2]) != 12:
            secondNum = str(int(secondNum[:2]) + 12) + secondNum[2:]
        return f"{firstNum} to {secondNum}"
    else:
        if int(secondNum[:2]) == 12:
            secondNum = "00" + secondNum[2:]
        if int(firstNum[:2]) != 12:
            firstNum = str(int(firstNum[:2]) + 12) + firstNum[2:]
        return f"{firstNum} to {secondNum}"




if __name__ == "__main__":
    main()
