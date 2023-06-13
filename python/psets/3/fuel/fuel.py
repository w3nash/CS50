def main():
    indicator = indicate("Fraction: ")
    print(indicator)


def indicate(prompt):
    while True:
        toindicate = input(prompt).strip()
        try:
            num1, num2 = toindicate.split("/")
            if int(num1) <= int(num2):
                indicate = round(int(num1) / int(num2) * 100)
                if indicate <= 1:
                    return "E"
                elif indicate >= 99:
                    return "F"
                else:
                    return str(indicate) + "%"
        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
