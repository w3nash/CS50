/*
    JONASH MARCELINO
    CS50
*/

#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

// Function declaration
string encrypt(string, string);

int main(int argc, string argv[])
{
    // Check count
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // Check length
    int length = 0;
    while (argv[1][length] != '\0')
    {
        length++;
    }
    if (length != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    // Check if valid
    bool isValid = true;
    for (int i = 0; argv[1][i] != '\0'; i++)
    {
        if (!isalpha(argv[1][i]))
        {
            isValid = false;
            break;
        }
    }
    if (!isValid)
    {
        printf("Key must only contain alphabetic characters.\n");
        return 1;
    }

    // Check repeats
    bool isRepeated = false;
    for (int i = 0; argv[1][i] != '\0'; i++)
    {
        for (int j = 0; argv[1][j] != '\0'; j++)
        {
            if (i != j)
            {
                if (argv[1][i] == argv[1][j])
                {
                    isRepeated = true;
                    break;
                }
            }
        }
        // Uppercase the keys
        argv[1][i] = toupper(argv[1][i]);
    }
    if (isRepeated)
    {
        printf("Key must not contain repeated characters.\n");
        return 1;
    }

    // Get plain text from user
    string plain;
    do
    {
        plain = get_string("plaintext:  ");
    }
    while (!plain);
    string ciphertext = encrypt(argv[1], plain);
    printf("ciphertext: %s\n", ciphertext);
    return 0;
}

// Function to encrypt the plain
string encrypt(string key, string plain)
{
    // Loop in plain text
    for (int i = 0; plain[i] != '\0'; i++)
    {
        // If not alpha just skip
        if (!isalpha(plain[i]))
        {
            continue;
        }
        // If alpha and lower assign the lowercased key
        else if (isalpha(plain[i]) && islower(plain[i]))
        {
            // Subracting the char 'a' will assign the keys to its dedicated lowercased keys
            plain[i] = tolower(key[plain[i] - 'a']);
        }
        // If alpha and upper assign the uppercased key
        else if (isalpha(plain[i]) && isupper(plain[i]))
        {
            // Subracting the char 'A' will assign the keys to its dedicated uppercased keys
            plain[i] = key[plain[i] - 'A'];
        }
    }
    // Return the encrypted key
    return plain;
}