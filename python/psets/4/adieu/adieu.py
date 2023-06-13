import inflect


def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            print("\nAdieu, adieu, to " + p.join(names))
            break
        else:
            names.append(name)


if __name__ == "__main__":
    main()
