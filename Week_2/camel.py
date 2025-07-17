
def main():
    camel = input("camelCase: ")
    snake = camel_to_snake(camel)
    print("snake_case: ",snake)

def camel_to_snake(camel):
    capital = "QWERTYUIOPASDFGHJKLZXCVBNM"
    snake_case = ""

    for letter in camel:
        if letter in capital:
            small_letter =  letter.lower()
            snake_case = snake_case + "_" + small_letter
        else:
            snake_case = snake_case + letter
    return snake_case



if __name__ == "__main__":
    main()

