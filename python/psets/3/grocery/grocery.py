def main():
    items = {}

    while True:
        try:
            item = input().upper()
        except EOFError:
            print()
            break
        else:
            if item in items:
                items[item] += 1
            else:
                items[item] = 1

    for item in sorted(items.keys()):
        print(items[item], item)


if __name__ == "__main__":
    main()
