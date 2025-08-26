import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    #if re.search(r"^\<iframe+(\w\W\s)*+\>\</iframe\>&",s, re.IGNORECASE):
    try:
        values = s.split('src=')
        part = values[1].split('"')
        url = part[1]
        if re.search(r"^https?://(?:www\.)youtube.com/embed/", url):
            url_part = url.split('embed/')[1]
            url = 'https://youtu.be/' + url_part
            return url
        else:
            return None
    except IndexError:
        return None
    #else:
        #return None


if __name__ == "__main__":
    main()
