import sys
from pyfiglet import Figlet

def main():
    if len(sys.argv)== 1:
        f = "ogre"
        print(f)
    elif len(sys.argv) == 3 and sys.argv[1] in ("-f","--font"):
        f = sys.argv[2]
        print(f)
    else:
        print("Invalid usage")

def print(f):
    figlet = Figlet()
    figlet.getFonts()
    figlet.setFont(font=f)
    s = input("Input: ")
    print(figlet.renderText(s))

main()
