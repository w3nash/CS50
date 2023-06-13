from datetime import date
import inflect
import sys
import re


def main():
    dob = input("Date of Birth: ")
    try:
        year, month, day = check_date(dob)
    except TypeError:
        sys.exit("Invalid Date")
    else:
        p = inflect.engine()
        minutes = convert(date(year, month, day))
        print(p.number_to_words(minutes, andword="").capitalize() + " minutes")


def convert(tosub):
    days = (date.today() - tosub).days
    return int(days) * 24 * 60


def check_date(tocheck):
    if matches := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", tocheck):
        return int(matches.group(1)), int(matches.group(2)), int(matches.group(3))
    else:
        return None


if __name__ == "__main__":
    main()
