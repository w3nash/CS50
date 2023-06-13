# TODO
from cs50 import get_int


def main():
    # Get input from user
    while True:
        card_no = get_int("Number: ")
        if card_no > 1:
            break

    # Check the card_no if valid
    is_valid = check_card(card_no)
    # Int to string
    cc_str = str(card_no)
    # Get length
    length = len(cc_str)
    # Get two digits
    first_two = cc_str[0] + cc_str[1]

    # Conditions for printing
    if not is_valid:
        print("INVALID")
    elif first_two[0] == '4' and length == 16 or length == 13:
        print("VISA")
    elif first_two == '34' or first_two == '37' and length == 15:
        print("AMEX")
    elif int(first_two) >= 34 and int(first_two) <= 55 and length == 16:
        print("MASTERCARD")
    else:
        print("INVALID")


def check_card(ccn):
    """ Check the card's validity """
    sum = 0
    while ccn > 0:
        last_digit = ccn % 10
        sum += last_digit
        ccn = int(ccn / 10)
        last_digit = ccn % 10
        times_two = last_digit * 2
        if times_two > 9:
            sum += (times_two % 10) + (int(times_two / 10))
        else:
            sum += times_two
        ccn = int(ccn / 10)
    if sum % 10 == 0:
        return True
    return False


if __name__ == '__main__':
    main()