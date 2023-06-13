/*
    JONASH MARCELINO
    CS50
*/
#include <cs50.h>
#include <stdio.h>

// Function declaration
void print_symbol(char, int);

int main(void)
{
    // Get the height of the pyramid
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    // Print the pyramid
    for (int i = 1; i <= height; i++)
    {
        print_symbol(' ', height - i);
        print_symbol('#', i);
        printf("\n");
    }
    return 0;
}

/*
    Function to print a symbol/char.
    c is the char to print.
    i is how many it will print.
*/
void print_symbol(char c, int n)
{
    for (int i = n; i > 0; i--)
    {
        printf("%c", c);
    }
}