import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    try:
        with open(sys.argv[1]) as before:
            reader = csv.DictReader(before)
            with open(sys.argv[2], "w") as after:
                writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    last, first = row["name"].split(", ")
                    writer.writerow(
                        {"first": first, "last": last, "house": row["house"]}
                    )
    except FileNotFoundError:
        sys.exit("Could not read " + sys.argv[1])


if __name__ == "__main__":
    main()
