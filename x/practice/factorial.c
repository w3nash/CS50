#include <cs50.h>
#include <stdio.h>

int factorial(int);

int main(void)
{
    int n = get_int("Enter num: ");
    for (int i = n; i > 0; i--)
    {
        printf("%i! = %i\n", i, factorial(i));
    }
    return 0;
}

int factorial(int n)
{
    if (n == 1)
    {
        return 1;
    }
    return n * factorial(n - 1);
}