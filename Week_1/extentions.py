def main():
    usr_input = input("File name: ")
    print(extend(usr_input))


def extend(usr_input):
    i = "image/"
    a = "application/"
    if usr_input.endswith(".gif"):
        return  i+"gif"
    elif usr_input.endswith(".jpeg") or usr_input.endswith(".jpg"):
        return i+"jpeg"
    elif usr_input.endswith('.png'):
        return i+"png"
    elif usr_input.endswith('.pdf'):
        return a+"pdf"
    elif usr_input.endswith('.txt'):
        return a+"txt"
    elif usr_input.endswith('.zip'):
        return a+'zip'
    else:
        return a+"octet-stream"



if __name__ == "__main__":
    main()

