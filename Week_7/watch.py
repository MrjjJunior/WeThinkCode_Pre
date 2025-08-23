import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r"https?://(www\.)?youtube\.com/.+\"", s)

    if match:
        link = match.group().split('"')
        if "www." in link[0]:
            link[0] = link[0].replace("youtube", "youtu.be")
            link[0] = link[0].replace("embed/", "")
            return link[0].replace("www.", "")
        return link[0]
    else:
        return None
if __name__ == "__main__":
    main()
