def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    lttrs = "QWERTYUIOPASDFGHJKLZXCVBNM"
    if s[0:1] in lttrs:
        return True
    if s > 2 and s < 6:
        ...


print("Hello")
if __name__ == "__main__":
    main()
