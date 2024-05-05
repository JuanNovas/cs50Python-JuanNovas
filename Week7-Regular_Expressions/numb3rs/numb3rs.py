import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        if  x := re.search("^(25[0-5]|2[0-4][0-9]|[1]?[1-9]?[0-9]|10[0-9])\\.(25[0-5]|2[0-4][0-9]|[1]?[1-9]?[0-9]|10[0-9])\\.(25[0-5]|2[0-4][0-9]|[1]?[1-9]?[0-9]|10[0-9])\\.(25[0-5]|2[0-4][0-9]|[1]?[1-9]?[0-9]|10[0-9])$",ip):
            return True
        else:
            return False
    except:
        return False

if __name__ == "__main__":
    main()
