    
def main():
    amount_dued = 50

    while amount_dued > 0:
        print("Amount Due: ",amount_dued)
        coin_inserted = int(input("Insert Coin: "))
        amount_dued -= coin_inserted

    if amount_dued < 0:
        neg = str(amount_dued)
        amount_owed = neg[1:]
        print(int(amount_owed))
    else:
        print("Amount Owed: ", amount_dued)



if __name__ == "__main__":
    main()
