import re

def main():
    print(count(input("Text: ")))

def count(s):
    counted = 0
    um_list = re.findall(r'\bum\b', s, re.IGNORECASE)
    for um in um_list:
        counted += 1
    return counted

if __name__ == "__main__":
    main()
