import re


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"\bum\b", s, flags=re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
