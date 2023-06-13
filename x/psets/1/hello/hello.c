/*
    JONASH MARCELINO
    CS50
*/
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Ask for name
    string name = get_string("What's your name? ");
    printf("hello, %s\n", name);
}