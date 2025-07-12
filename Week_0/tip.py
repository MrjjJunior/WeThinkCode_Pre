def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    if "$" in d:
        dollar = d.replace("$","")
        return float(dollar)
    else:
        return float(d)

def percent_to_float(p):
    if "%" in p:
        percentage = p.replace("%","")
        per = float(percentage)
        return per / 100
    else:
        per = float(p)
        return per / 100


if __name__ == "__main__":
    main()