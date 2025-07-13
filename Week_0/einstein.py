import numpy as np


def main():
    user_input = int(input("Input mass(kg): "))
    output = einstein(user_input)
    print(output)

def einstein(mass):
    constant = 300000000 ** 2
    energy = mass * constant
    return energy

if __name__ == "__main__":
    main()
