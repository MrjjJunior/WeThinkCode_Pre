from pyfiglet import Figlet
import pyfiglet
import sys
import random
"""
    sys.argv[0] is the name of script
    sys.argv[1] ,sys..[2] arguments passed

"""

def main():
    figlet = Figlet() 
    fonts = figlet.getFonts()

    if len(sys.argv) == 1: #sys.argv is a list ['txt.py','-c', 'hello'] 
        font = random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
        if sys.argv[2] in fonts:
            font = sys.argv[2]
        else:
            sys.exit("Error: font not found")
    else:
        sys.exit("2 arguments were not used")


    figlet.setFont(font=font)
    text = input("Input: ")
    print("Output: ")
    print(figlet.renderText(text))



#usr_txt = input("Input: ")
#print("Output: ")
#f = pyfiglet.figlet_format(usr_txt, font="slant")
#print(f)
#print(figlet.renderText(usr_txt))
# print(figlet.renderText('Text to render'))

if __name__ == "__main__":
    main()

