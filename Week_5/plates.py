def main():
    plate = input("Plate: ")
    print(is_valid(plate))


def is_valid(s):
    lttrs = "QWERTYUIOPASDFGHJKLZXCVBNM"
    numbers = "1234567890"

    for i in s:
        if s[0] in numbers:
            return "Invalid"

    if len(s) == 1 or len(s) > 6:
        return "Invalid"
    elif s[0] in lttrs and s[1] in lttrs:
        if len(s) >= 2:
            if len(s) <= 6:
                return "Valid"
    else:
        return "Invalid"


print("Hello")
if __name__ == "__main__":
    main()
