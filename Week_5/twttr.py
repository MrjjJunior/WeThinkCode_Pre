
def main():
    word = input("Input: ")
    print("Ouput: ", shorten(word))


def shorten(word):
    vwls = "AEIOUaeiou"
    output = ""

    for letter in word:
        if letter in vwls:
            continue
        else:
            output += letter
    return output


if __name__ == "__main__":
    main()
