#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

typedef struct node
{
    string text;
    struct node *next;
}
node;

int main(void)
{
    node *list = NULL;
    for (int i = 1; i <= 3; i++)
    {
        string txt = get_string("Enter a word: ");
        node *text = malloc(sizeof(node));
        if (text == NULL)
        {
            return 1;
        }
        text->text = txt;
        text->next = list;
        list = text;
    }
    for (node *ptr = list; ptr != NULL; ptr = ptr->next)
    {
        printf("%s\n", ptr->text);
    }
    while (list != NULL)
    {
        node *ptr = list->next;
        free(list);
        list = ptr;
    }
    return 0;
}