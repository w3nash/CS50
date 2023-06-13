from pyfiglet import Figlet
import sys
import random

font_styles = ["slant", "rectangles", "alphabet"]

if len(sys.argv) == 1:
    fonts = font_styles[random.randint(0, 2)]

elif len(sys.argv) == 3:
    if not sys.argv[1].lower() in ["-f", "--font"]:
        print("Invalid usage")
        sys.exit(1);
    if not sys.argv[2].lower() in font_styles:
        print("Invalid usage")
        sys.exit(1);
    fonts = sys.argv[2]
else:
    print("Invalid usage")
    sys.exit(1);

f = Figlet(font=fonts)
text = input("Input: ")
print("Output: ")
print(f.renderText(text))