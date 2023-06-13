import sys
from pyfiglet import Figlet
from random import choice


def main():
    fonts = ["slant", "rectangles", "alphabet"]
    if len(sys.argv) == 1:
        text = input("Input: ")
        print("Output:", Figlet(font=choice(fonts)).renderText(text), sep="\n")
    elif (
        len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts
    ):
        text = input("Input: ")
        print("Output:", Figlet(font=sys.argv[2]).renderText(text), sep="\n")
    else:
        sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
