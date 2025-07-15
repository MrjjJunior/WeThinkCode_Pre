

def main():
    usr_input = input("Greeting: ")
    print(bank(usr_input.lower()))


def bank(usr_input):
    if usr_input == "hello":
        return "$0"
    elif usr_input.startswith("h"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()

