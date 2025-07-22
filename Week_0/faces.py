def main():
    user_input = input("Say something with am emotion: \n")
    output = convert_to_emoji(user_input)
    print(output)


def convert_to_emoji(user_input):
    if ":)" in user_input:
        converted = user_input.replace(":)", "😊")
        return converted
    elif ":(" in user_input:
        converted = user_input.replace(":(", "🙁")
        return converted
    else:
        return user_input


if __name__ == "__main__":
    main()
