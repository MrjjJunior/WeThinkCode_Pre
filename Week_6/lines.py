import sys

""" script takes a file as an argument and counts lines of code """


def main():
    code = []

    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        with open(sys.argv[1]) as file:
            for line in file:
                if line.rstrip() == "" or line.startswith("#"):
                    continue
                else:
                    code.append(line.rstrip())
        print(len(code))
    except FileNotFoundError:
        print("File does not exist")


if __name__ == "__main__":
    main()
