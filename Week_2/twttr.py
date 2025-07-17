
def main():
    usr_input = input("Input: ")
    print("Ouput: ", rm_vowels(usr_input))


def rm_vowels(usr_input):
    vwls = "AEIOUaeiou"
    output = ""

    for letter in usr_input:
        if letter in vwls:
            continue
        else:
            output += letter
    return output


if __name__ == "__main__":
    main()
