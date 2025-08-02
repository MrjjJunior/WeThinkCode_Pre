
def main():
    price_list = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
    try:
        total = 0
        while True:
            item = input("Item: ").capitalize()
            if item == "":
                break
            if item in price_list:
                total = total + price_list[item]
            print("Total: $",total)
    except EOFError:
        print("Done")


if __name__ == "__main__":
    main()
