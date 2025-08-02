months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    try:
        while True:
            user = input("Date: ")
            
            d = arrange(user)

            if user == "":
                break
            print(user.replace("/", "-"))
    except Exception:
        ...


def arrange(user):
    """ yyyy-dd-mm """
    seperate = user.split()
    if 


# year date month


if __name__ == "__main__":
    main()
