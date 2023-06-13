def main():
    due = 50
    while True:
        if due <= 0:
            break
        print("Amount Due:", due)
        coin = int(input("Insert Coin: "))
        if coin <= 25:
            if coin % 25 == 0 or coin % 10 == 0 or coin % 5 == 0:
                due -= coin
    print("Change Owed:", abs(due))


if __name__ == "__main__":
    main()
