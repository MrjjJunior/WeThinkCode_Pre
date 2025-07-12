import numpy as np


def main():
    user_input = input("Input mass(kg): ")
    output = einstein(user_input)

def einstein(mass):
    constant = 300000000 ** 2
    energy = np.zeros(mass * constant)
    return energy

if __name__ == "__main__":
    main()
