/*
    JONASH MARCELINO
    CS50
*/
#include <cs50.h>
#include <stdio.h>

// Functions Declaration
bool check_card(long);
int get_card_length(long);
int get_first_two_digits(long);

int main(void)
{
    // TODO: Promt for input
    long card_no;
    do
    {
        card_no = get_long("Number: ");
    }
    while (card_no < 1);

    // TODO: Calculate checksum
    bool isValid = check_card(card_no);

    // TODO: Check card length and starting digits.
    int ccLength = get_card_length(card_no);
    int digits = get_first_two_digits(card_no);

    // TODO: Print AMEX, MASTERCARD, VISA, or INVALID.
    if (!isValid)
    {
        printf("INVALID\n");
    }
    else if (digits / 10 == 4 && (ccLength == 16 || ccLength == 13))
    {
        printf("VISA\n");
    }
    else if ((digits == 34 || digits == 37) && ccLength == 15)
    {
        printf("AMEX\n");
    }
    else if ((digits >= 51 && digits <= 55) && ccLength == 16)
    {
        printf("MASTERCARD\n");
    }
    else
    {
        printf("INVALID\n");
    }
    return 0;
}

// Function to calculate checksum.
bool check_card(long num)
{
    int sum = 0;
    while (num > 0)
    {
        int lastDigit;
        // Get the last digit
        lastDigit = num % 10;
        // Add the last digit to sum
        sum += lastDigit;
        // Move to next digit
        num /= 10;
        // Get the last digit
        lastDigit = num % 10;
        // Multiply the last digit
        int timesTwo = lastDigit * 2;
        if (timesTwo > 9)
        {
            // Add the two digits to the sum not the number
            sum += (timesTwo % 10) + (timesTwo / 10);
        }
        else
        {
            // Add the multiplied number
            sum += timesTwo;
        }
        // Move to next digit
        num /= 10;
    }
    if (sum % 10 == 0)
    {
        return true;
    }
    return false;
}

// Function to check card length.
int get_card_length(long num)
{
    int length = 0;
    while (num > 0)
    {
        length++;
        num /= 10;
    }
    return length;
}

// Function to check card starting digits.
int get_first_two_digits(long num)
{
    int length = get_card_length(num);
    // We divide the num to 10 to finally to 2 digits only
    for (int i = length; i > 2; i--)
    {
        num /= 10;
    }
    return num;
}