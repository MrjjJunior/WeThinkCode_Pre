def main():
    try:
        grocery = {}
        while True:
            item = input().upper()
            if item == "":
                break
            elif item in grocery:
                grocery[item] = grocery[item] + 1
            else:
                grocery[item] = 1
        
        food = grocery.keys()
        number =  grocery.values()
        for num in number:
            for item in food:
                if num == grocery[item]:
                    print(f"{num} {item}")


    except EOFError:
        break

if __name__ == "__main__":
    main()
