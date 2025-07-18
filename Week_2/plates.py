def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    lttrs = "QWERTYUIOPASDFGHJKLZXCVBNM"
    nmbrs = "1234567890"

    if s[0:1] in lttrs:
        if s > 2 and s < 6:
            ...

if __name__ == "__main__":
    main()  