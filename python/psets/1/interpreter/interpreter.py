def main():
    expression = input("Expression: ").strip()
    num1, opperation, num2 = expression.split()
    match opperation:
        case "+":
            print(float(num1) + float(num2))
        case "-":
            print(float(num1) - float(num2))
        case "*":
            print(float(num1) * float(num2))
        case "/":
            print(float(num1) / float(num2))


if __name__ == "__main__":
    main()
