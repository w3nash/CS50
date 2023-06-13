// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    int uppercase_count = 0;
    int lowecase_count = 0;
    int number_count = 0;
    int symbol_count = 0;
    for (int i = 0; password[i] != '\0'; i++)
    {
        if (isdigit(password[i]))
        {
            number_count++;
        }
        else if (islower(password[i]))
        {
            lowecase_count++;
        }
        else if (isupper(password[i]))
        {
            uppercase_count++;
        }
        else if (ispunct(password[i])
                 || (password[i] >= 33 && password[i] <= 47)
                 || (password[i] >= 58 && password[i] <= 64)
                 || (password[i] >= 91 && password[i] <= 96)
                 || (password[i] >= 123 && password[i] <= 126))
        {
            symbol_count++;
        }
    }
    if (uppercase_count
        && lowecase_count
        && number_count
        && symbol_count)
    {
        return true;
    }
    return false;
}
