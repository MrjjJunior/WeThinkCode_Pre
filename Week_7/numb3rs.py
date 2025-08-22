import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}$", ip):
        ip1 , ip2 , ip3 , ip4 = ip.split(".")
        if int(ip1) <= 255 and int(ip2) <= 255 and int(ip3) <= 255 and int(ip4) <= 255:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
