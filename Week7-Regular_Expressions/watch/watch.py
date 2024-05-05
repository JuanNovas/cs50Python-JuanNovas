import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        x = re.search('youtube\\.com/embed/(\\w*)"', s)
        return f"https://youtu.be/{x.group(1)}"
    except:
        return None


if __name__ == "__main__":
    main()
