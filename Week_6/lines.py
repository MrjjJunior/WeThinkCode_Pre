import sys
""" script takes a file as an argument and counts lines of code """

def main():
    code = []
    with open(sys.argv[1]) as file:
        for line in file:
            if line.rstrip() == "" or line.startswith("#"):
                continue
            else:
                code.append(line.rstrip())
    print(len(code))


if __name__ == "__main__":
    main()
