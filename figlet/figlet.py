import sys
from pyfiglet import Figlet
import random

if len(sys.argv) != 3 and len(sys.argv) != 1:
    sys.exit("Invalid usage")

fonts = Figlet().getFonts()

if (len(sys.argv) == 3):
    if (sys.argv[1] != "-f" and  sys.argv[1] != "--font"):
        sys.exit("Invalid usage")
    elif sys.argv[2] not in fonts:
        sys.exit("Invalid usage")


user_input = input("Input: ")

if len(sys.argv) == 1:
    randfont = random.choice(fonts)
    randfiglet = Figlet(font = randfont)
    print(randfiglet.renderText(user_input))
else:
    print(Figlet(font = sys.argv[2]).renderText(user_input))