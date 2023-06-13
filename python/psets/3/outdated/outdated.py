def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:
        date = input("Date: ").strip()
        date = date.replace(" ", "/")
        datelist = date.split("/")
        if datelist[0].isalpha() and datelist[1].endswith(","):
            try:
                mm = months.index(datelist[0]) + 1
            except ValueError:
                pass
            else:
                day = datelist[1].replace(",", "")
                day = int(day)
                if mm <= 12 and day <= 31:
                    print(f"{datelist[2]}-{mm:02}-{day:02}")
                    break
        else:
            try:
                mm = int(datelist[0])
                day = int(datelist[1])
            except ValueError:
                pass
            else:
                if mm <= 12 and day <= 31:
                    print(f"{datelist[2]}-{mm:02}-{day:02}")
                    break


if __name__ == "__main__":
    main()
