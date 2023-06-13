def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s= s.strip()
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isdigit() and s[1].isdigit():
        return False
    if len(s) == 6:
        if s[2].isdigit() or s[3].isdigit():
            return False
    numc = 0
    for c in s:
        if not c.isalnum():
            return False
        if c.isdigit():
            if numc == 0 and c == "0":
                return False
            numc += 1
    return True


if __name__ == "__main__":
    main()
