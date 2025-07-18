def main():
    item = input("Item: ")
    print(nutrition(item))


def nutrition(item):
    fruits = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
              }
    
    a = item.capitalize()

    if a in fruits:
        return f"Calories: {fruits[a]}"
    else:
        return ""


if __name__ == "__main__":
    main()