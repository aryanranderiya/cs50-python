from pyfiglet import Figlet
import sys
import random

f = Figlet()

fontlist = f.getFonts()

try:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font" :
        for font in fontlist :
            if sys.argv[2] == font:
                userinputfont = font

            if sys.argv[2] not in fontlist :
                sys.exit("Invalid usage")
    else :
        sys.exit("Invalid usage")
except IndexError : pass

if len(sys.argv) == 2:
    sys.exit("Invalid usage")

if len(sys.argv) == 1:
    userinputfont = fontlist[random.randrange(0,10)]

f.setFont(font=userinputfont)

userinput = input("Input: ")

print (f.renderText(userinput))