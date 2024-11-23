import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(yt):
    try:
        matches = re.search(r'^<iframe(?:\s.+)?\s?src="https?://(www\.)?youtube\.com/embed/([^"]+)".*</iframe>$', yt)
        if matches:
            parsed = matches.group(2)
            return f'https://youtu.be/{parsed}'
        else:
            raise AttributeError
    except AttributeError:
        return None
        sys.exit()
if __name__ == "__main__":
    main()

# _______               __     __
#|_     _|.-----.-----.|  |--.|__|
#  |   |  |  _  |__ --||     ||  |
#  |___|  |_____|_____||__|__||__|
