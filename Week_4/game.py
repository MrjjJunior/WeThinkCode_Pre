import random

def main():

    level = int(input("Level: "))
    number =  random.randint(1,level)

    while True:
        guess = int(input("Guess: "))
        
        if guess == number:
            print("Just right!")
            break
        elif guess > number:
            print("Too large!")
        else:
            print("Too small!")


if __name__ == "__main__":
    main()

