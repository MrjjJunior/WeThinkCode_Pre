def main():
    usr_input = input("Fraction:" )
    print(fraction(usr_input))

def fraction(usr_input):
    try:
        x,y = usr_input.split("/")
        percentage = int(x) * 10 / int(y) * 10
        percentage = int(percentage)
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return str(percentage) + "%"
    except (ValueError, ZeroDivisionError):
        main()
        return ""

if __name__ == "__main__":
    main()

