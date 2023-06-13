def main():
    camel = input("camelCase: ").strip()
    snake = to_snake_case(camel)
    print("snake_case:", snake)


def to_snake_case(to_snake):
    snake = ""
    for c in to_snake:
        if c.isupper():
            snake += "_" + c.lower()
        else:
            snake += c
    return snake


if __name__ == "__main__":
    main()
