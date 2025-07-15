
def main():
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    output = deep(user_input)
    print(output)


def deep(user_input):
    a = user_input 
    if "42" in a or "forty-two" in a or "forty two" in a:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    main()

