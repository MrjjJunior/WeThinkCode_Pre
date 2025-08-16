import sys
from tabulate import tabulate
'''
'''


def main():
    try:
        table = []
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")

        with open(sys.argv[1]) as file:
            for line in file:
                table.append(line.rstrip().split(","))

        
        print(tabulate(table, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
