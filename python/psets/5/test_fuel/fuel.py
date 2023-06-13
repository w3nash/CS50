def main():
    fraction = input("Fraction: ").strip()
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    while True:
        try:
            num1, num2 = fraction.split("/")
            num1, num2 = int(num1), int(num2)
            f = num1 / num2
            if f <= 1:
                return round(f * 100)
            else:
                fraction = input("Fraction: ").strip()
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
