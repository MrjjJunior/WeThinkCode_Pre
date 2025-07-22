def main():
    time = input("What time is it? ")
    converted_time = convert(time)
    print(meal(converted_time))


def convert(time):

    hours, minutes = time.split(":")
    minutes = int(minutes) / 60
    m = str(minutes)
    if m.startswith("0."):
        new_minutes = m[2:]
        new_time = hours + "." + new_minutes
        # print(new_time)
    return float(new_time)


def meal(converted_time):
    time = converted_time
    # Breakfast times
    if time == 7 or time == 8:
        return "breakfast time"
    elif time > 7 and time < 8:
        return "breakfast time "
    elif time == 12 or time == 13:
        return "lunch time"
    elif time > 12 and time < 13:
        return "lunch time"
    elif time == 18 or time == 19:
        return "dinner time"
    elif time > 18 and time < 19:
        return "dinner time"
    else:
        return ""


if __name__ == "__main__":
    main()
