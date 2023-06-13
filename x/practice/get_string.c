#include <stdio.h>
#include <stdlib.h>

typedef char *string;

string get_string(string);

int main(void)
{
    string name = get_string("What is your name? ");
    printf("%s\n", name);
    free(name);
}

string get_string(string prompt)
{
    char s[100];
    printf("%s", prompt);
    scanf("%s", s);
    int length = 0;
    for (int i = 0; s[i] != '\0'; i++)
    {
        length++;
    }
    string newString = malloc(length + 1);
    for (int i = 0; i < length + 1; i++)
    {
        newString[i] = s[i];
    }
    return newString;
}