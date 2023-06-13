/*
    JONASH MARCELINO
    CS50
*/
#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

// Function Declaration
string cipher(string, int);

bool check_argv(string);

int main(int argc, string argv[])
{
    // EXIT IF NOT USED PROPERLY
    if (argc != 2 || !check_argv(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    // Get text from user
    string text = get_string("plaintext:  ");

    // Print and cipher the text
    printf("ciphertext: %s\n", cipher(text, atoi(argv[1])));
    return 0;
}

// Function to cipher the text
string cipher(string plain, int key)
{
    for (int i = 0; plain[i] != '\0'; i++)
    {
        char c = plain[i];
        // Check if lowercase
        if (isalpha(plain[i]) && islower(plain[i]))
        {
            c = ((c - 'a') + key) % 26 + 'a';
            if (c < 'a')
            {
                c = c + 'z' - 'a' + 1;
            }
            plain[i] = c;
        }
        // Check if uppercase
        else if (isalpha(plain[i]) && isupper(plain[i]))
        {
            c = ((c - 'A') + key) % 26 + 'A';
            if (c < 'A')
            {
                c = c + 'Z' - 'A' + 1;
            }
            plain[i] = c;
        }
        else
        {
            plain[i] = plain[i];
        }
    }
    return plain;
}

bool check_argv(string s)
{
    for (int i = 0; s[i] != '\0'; i++)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}