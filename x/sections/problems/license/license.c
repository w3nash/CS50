#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Check for command line args
    if (argc != 2)
    {
        printf("Usage: ./read infile\n");
        return 1;
    }

    // Create buffer to read into
    char *buffer = malloc(7);
    if (buffer == NULL)
    {
        printf("Cannot make memory.\n");
    }

    FILE *infile = fopen(argv[1], "r");
    if (infile == NULL)
    {
        printf("Cannot find such file.\n");
    }

    while (fread(buffer, 1, 7, infile) == 7)
    {
        buffer[6] = '\0';
        printf("%s\n", buffer);
    }

    fclose(infile);
    free(buffer);
}
