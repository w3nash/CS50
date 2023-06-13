import re


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    if matches := re.search(r'^(\d{1,2}):?(\d{1,2})? (AM|PM) to (\d{1,2}):?(\d{1,2})? (AM|PM)$', s):
        from_hours, from_seconds, from_meridiem, to_hours, to_seconds, to_meridiem = matches.groups()
        if from_seconds:
            if int(from_seconds) >= 60 or int(from_seconds) < 0:
                raise ValueError
        else:
            from_seconds = '00'
        if to_seconds:
            if int(to_seconds) >= 60 or int(to_seconds) < 0:
                raise ValueError
        else:
            to_seconds = '00'
        if from_meridiem == 'AM':
            if from_hours == '12':
                from_hours = '00'
            else:
                from_hours = f"{int(from_hours):02d}"
        elif from_meridiem == 'PM':
            if from_hours == '12':
                from_hours = '12'
            else:
                from_hours = f"{int(from_hours) + 12:02d}"
        if to_meridiem == 'AM':
            if to_hours == '12':
                to_hours = '00'
            else:
                to_hours = f"{int(to_hours):02d}"
        elif to_meridiem == 'PM':
            if to_hours == '12':
                to_hours = '12'
            else:
                to_hours = f"{int(to_hours) + 12:02d}"
        return f"{from_hours}:{from_seconds} to {to_hours}:{to_seconds}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()