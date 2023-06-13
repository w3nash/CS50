/*
    JONASH MARCELINO
    CS50
*/
#include <cs50.h>
#include <stdio.h>

// Function Declaration
bool isPrime(int);

int main(void)
{
    // Get input
    int min = get_int("Minimum: ");
    int max = get_int("Maximum: ");
    
    // Loop from mix to max
    for (int i = min; i <= max; i++)
    {
        // Print if prime
        if (isPrime(i))
        {
            printf("%i\n", i);
        }
    }
}

// Function to check if num is prime
bool isPrime(int num)
{
    if (num == 1)
    {
        return false;
    }
    // Check if a number is divisible by every number
    for (int i = 2; i < num; i++)
    {
        if (num % i == 0)
        {
            return false;
        }
    }
    return true;
}