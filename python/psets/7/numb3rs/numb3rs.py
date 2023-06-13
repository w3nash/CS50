import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    matches = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    try:
        if all(int(octet) >= 0 and int(octet) <= 255 for octet in matches.groups()):
            return True
        return False
    except AttributeError:
        return False


if __name__ == "__main__":
    main()
