import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower().strip()
    x = re.findall(r"([\s\.,\?]+um[\s\.,\?]+|^um[\s\.,\?]+|[\s\.,\?]+um$|^um$)", s)
    return len(x)


...


if __name__ == "__main__":
    main()
