import inflect

p = inflect.engine()

def main():
    
    names = []
    while True:
        name = input("Name: ")
        if name == "":
            break
        else:
            names.append(name)

    n = p.join(names)
    print("Adieu, adieu, to", n)



if __name__ == "__main__":
    main()
