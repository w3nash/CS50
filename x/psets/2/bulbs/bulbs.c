/*
    JONASH R. MARCELINO
    CS50
*/
#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

// Function declaration
void print_bulb(int bit);
int *decimal_to_binary(int);

int main(void)
{
    // TODO
    string message = get_string("Message: ");
    for (int i = 0; message[i] != '\0'; i++)
    {
        int *binary = decimal_to_binary(message[i]);
        for (int j = BITS_IN_BYTE - 1; j >= 0; j--)
        {
            print_bulb(binary[j]);
        }
        printf("\n");

    }

}

// Function to print bulb
void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}

// Function to convert decimal to binary
int *decimal_to_binary(int decimal)
{
    static int binary[BITS_IN_BYTE];
    for (int i = 0; i < BITS_IN_BYTE; i++, decimal /= 2)
    {
        binary[i] = decimal % 2;
    }
    return binary;
}
