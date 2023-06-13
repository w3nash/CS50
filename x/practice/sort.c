#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int unsorted[] = {5, 8, 2, 9, 0, 2, 1, -1, 10, 20, 1000};
    for (int i = 0; i < 11; i++)
    {
        for (int j = 0; j < 11; j++)
        {
            if(i == j)
            {
                continue;
            }
            int temp;
            if(unsorted[i] < unsorted[j])
            {
                temp = unsorted[i];
                unsorted[i] = unsorted[j];
                unsorted[j] = temp;
            }
        }
    }
    for (int i = 0; i < 11; i++)
    {
        printf("%i ", unsorted[i]);
    }
    printf("\n");
}