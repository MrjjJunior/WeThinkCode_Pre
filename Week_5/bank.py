def main():
    usr_input = input("Greeting: ")
    print(bank(usr_input.lower()))


def bank(usr_input):
    if usr_input == "hello" or usr_input == "Hello":
        return "$0"
    elif usr_input.startswith("h") or usr_input.startswith("H"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()
