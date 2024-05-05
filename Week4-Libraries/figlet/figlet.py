import sys
from pyfiglet import Figlet

if len(sys.argv) == 1:
    text = input("Input: ")
    f = Figlet()
    print(f.renderText(text))
elif len(sys.argv) == 3 and sys.argv[1] in ("-f","--font"):
    try:
        figlet = Figlet()
        f = sys.argv[2]
        list = figlet.getFonts()
        if f not in list:
            sys.exit("Invalid usage")
        text = input("Input: ")
        figlet.setFont(font=f)
        print(figlet.renderText(text))
    except:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

